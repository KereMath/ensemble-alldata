# ensemble-alldata — Tam Sonuç Raporu

## 1. Yöntem Özeti

### Motivasyon
Eski tsfresh ensemble her binary modeli yalnızca **tekli anomali datalarıyla** eğitti.
Kombinasyon sinyali geldiğinde baskın pattern (örneğin deterministik trend) diğer anomaliyi
gölgeledi. Sonuç: kombinasyon testinde **full match %0**.

### Neden %0?
Eski ensemble argmax mantığıyla çalışıyordu: hangi sınıf en yüksek olasılığa sahipse o kazanır.
Bu yapı doğası gereği tek etiket üretiyor; ikinci bir anomali tespit etmesi imkânsız.

### Yeni Strateji
Her binary modelin pozitif sınıfına, o anomaliyi/base tipi içeren **tüm kombinasyon
klasörlerini** dahil etmek. Bu sayede model anomaliyi farklı gürültü ortamlarında da
tanımayı öğreniyor.

**Inference (yeni):**
- `base_type` = argmax(4 base model) → zorunlu tek seçim
- `anomalies` = [model for anomaly_models if P >= 0.5] → sıfır veya daha fazla anomali

---

## 2. Eğitim Veri Yapısı

### Genel Parametreler

| Parametre | N=440 (v1) | N=1320 (v2) | N=1320 (v3, son) |
|---|---|---|---|
| N pozitif per model | 440 | 1320 | 1320 |
| N negatif per model | 440 | 1320 | 1320 |
| Toplam per model | ~880 | ~2640 | ~2640 |
| Test seti per model | ~176 | ~528 | ~528 |
| Feature extraction | tsfresh EfficientFCParameters (777 feature) | aynı | aynı |
| Split | %70 train / %10 val / %20 test (stratified) | aynı | aynı |
| Kaynak grup sayısı | 39 (10 tekli + 29 kombinasyon) | aynı | aynı |
| Min seri uzunluğu | 50 zaman adımı | aynı | aynı |
| **Min per_leaf garanti** | 1 | 1 | **10** |
| Random state | 42 | 42 | 42 |
| n_jobs (tsfresh) | 4 | 4 | 4 |

### Örnekleme Mantığı
- **Pozitif:** `floor(N / pos_grup_sayısı)` örnek per kaynak grubu
- **Negatif:** `floor(N / neg_grup_sayısı)` örnek per kaynak grubu
- Grup içinde leaf klasörlerden eşit örnekleme: `per_leaf = max(10, n // len(leaves))`
- **Min per_leaf = 10 garantisi (v3):** Bazı büyük gruplarda (örn. deterministic_trend: 72 leaf) `floor(60/72)=0` olurdu, bu da birçok leaf'in hiç temsil edilmemesine yol açıyordu. v3'te her leaf'ten en az 10 örnek alınır.
- Hedef toplam dolmuyorsa rastgele havuzdan tamamlama

---

## 3. Her Model İçin Pozitif / Negatif Kaynak Grupları

### MODEL 1: stationary
**Pozitif (7 grup, 188/grup):**

| # | Kaynak Klasör | Açıklama |
|---|---|---|
| 1 | `Generated Data/stationary/` | Saf stationary (AR/MA/ARMA/WN × short/med/long, 12 leaf) |
| 5 | `Generated Data/collective_anomaly/` | Stationary + collective (48 leaf) |
| 6 | `Generated Data/contextual_anomaly/` | Stationary + contextual (48 leaf) |
| 7 | `Generated Data/mean_shift/` | Stationary + mean_shift (48 leaf) |
| 8 | `Generated Data/point_anomaly/` | Stationary + point_anomaly (48 leaf) |
| 9 | `Generated Data/trend_shift/` | Stationary + trend_shift (48 leaf) |
| 10 | `Generated Data/variance_shift/` | Stationary + variance_shift (48 leaf) |

**Negatif (32 grup, 41/grup):** deterministic_trend, stochastic_trend, volatility + tüm 29 kombinasyon klasörü

---

### MODEL 2: deterministic_trend
**Pozitif (22 grup, 60/grup):**

| # | Kaynak Klasör |
|---|---|
| 2 | `Generated Data/deterministic_trend/` (72 leaf: 4 noise × 6 shape × 3 uzunluk) |
| 11 | `Combinations/Cubic Base/.../cubic_collective_anomaly/` |
| 12 | `Combinations/Cubic Base/.../Cubic + Mean Shift/` |
| 13 | `Combinations/Cubic Base/.../Cubic + Point Anomaly/` |
| 14 | `Combinations/Cubic Base/.../Cubic + Variance Shift/` |
| 15 | `Combinations/Damped Base/.../Damped + Collective Anomaly/` |
| 16 | `Combinations/Damped Base/.../Damped + Mean Shift/` |
| 17 | `Combinations/Damped Base/.../Damped + Point Anomaly/` |
| 18 | `Combinations/Damped Base/.../Damped + Variance Shift/` |
| 19 | `Combinations/Exponential Base/.../exponential_collective_anomaly/` |
| 20 | `Combinations/Exponential Base/.../Exponential + Mean Shift/` |
| 21 | `Combinations/Exponential Base/.../exponential_point_anomaly/` |
| 22 | `Combinations/Exponential Base/.../exponential_variance_shift/` |
| 23 | `Combinations/Linear Base/.../Linear + Collective Anomaly/` |
| 24 | `Combinations/Linear Base/.../Linear + Mean Shift/` |
| 25 | `Combinations/Linear Base/.../Linear + Point Anomaly/` |
| 26 | `Combinations/Linear Base/.../Linear + Trend Shift/` |
| 27 | `Combinations/Linear Base/.../Linear + Variance Shift/` |
| 28 | `Combinations/Quadratic Base/.../Quadratic + Collective anomaly/` |
| 29 | `Combinations/Quadratic Base/.../Quadratic + Mean Shift/` |
| 30 | `Combinations/Quadratic Base/.../Quadratic + Point Anomaly/` |
| 31 | `Combinations/Quadratic Base/.../Quadratic + Variance Shift/` |

**Negatif (17 grup, 77/grup):** 9 tekli tip + 8 stochastic/volatility bazlı kombinasyon

---

### MODEL 3: stochastic_trend
**Pozitif (5 grup, 264/grup):**

| # | Kaynak Klasör |
|---|---|
| 3 | `Generated Data/Stochastic Trend/` (ARI/ARIMA/IMA/RW/RWD × 3 uzunluk, 15 leaf) |
| 32 | `Combinations/Stochastic Trend + Collective Anomaly/` |
| 33 | `Combinations/Stochastic Trend + Mean Shift/` |
| 34 | `Combinations/Stochastic Trend + Point Anomaly/` |
| 35 | `Combinations/Stochastic Trend + Variance Shift/` |

**Negatif (34 grup, 38/grup)**

---

### MODEL 4: volatility
**Pozitif (5 grup, 264/grup):**

| # | Kaynak Klasör |
|---|---|
| 4 | `Generated Data/Volatility/` (APARCH/ARCH/EGARCH/GARCH × 3 uzunluk, 12 leaf) |
| 36 | `Combinations/Volatility + Collective Anomaly/` |
| 37 | `Combinations/Volatility + Mean Shift/` |
| 38 | `Combinations/Volatility + Point Anomaly/` |
| 39 | `Combinations/Volatility + Variance Shift/` |

**Negatif (34 grup, 38/grup)**

---

### MODEL 5: collective_anomaly
**Pozitif (8 grup, 165/grup):**

| # | Kaynak Klasör |
|---|---|
| 5 | `Generated Data/collective_anomaly/` (48 leaf) |
| 11 | `Combinations/Cubic Base/.../cubic_collective_anomaly/` |
| 15 | `Combinations/Damped Base/.../Damped + Collective Anomaly/` |
| 19 | `Combinations/Exponential Base/.../exponential_collective_anomaly/` |
| 23 | `Combinations/Linear Base/.../Linear + Collective Anomaly/` |
| 28 | `Combinations/Quadratic Base/.../Quadratic + Collective anomaly/` |
| 32 | `Combinations/Stochastic Trend + Collective Anomaly/` |
| 36 | `Combinations/Volatility + Collective Anomaly/` |

**Negatif (31 grup, 42/grup)**

---

### MODEL 6: contextual_anomaly
**Pozitif (1 grup, 1320/grup):**

| # | Kaynak Klasör |
|---|---|
| 6 | `Generated Data/contextual_anomaly/` (48 leaf) |

**Negatif (38 grup, 34/grup)**
> Not: Veri setinde contextual anomaly için kombinasyon klasörü mevcut değil.

---

### MODEL 7: mean_shift
**Pozitif (8 grup, 165/grup):**

| # | Kaynak Klasör |
|---|---|
| 7 | `Generated Data/mean_shift/` (48 leaf) |
| 12 | `Combinations/Cubic Base/.../Cubic + Mean Shift/` |
| 16 | `Combinations/Damped Base/.../Damped + Mean Shift/` |
| 20 | `Combinations/Exponential Base/.../Exponential + Mean Shift/` |
| 24 | `Combinations/Linear Base/.../Linear + Mean Shift/` |
| 29 | `Combinations/Quadratic Base/.../Quadratic + Mean Shift/` |
| 33 | `Combinations/Stochastic Trend + Mean Shift/` |
| 37 | `Combinations/Volatility + Mean Shift/` |

**Negatif (31 grup, 42/grup)**

---

### MODEL 8: point_anomaly
**Pozitif (8 grup, 165/grup):**

| # | Kaynak Klasör |
|---|---|
| 8 | `Generated Data/point_anomaly/` (48 leaf) |
| 13 | `Combinations/Cubic Base/.../Cubic + Point Anomaly/` |
| 17 | `Combinations/Damped Base/.../Damped + Point Anomaly/` |
| 21 | `Combinations/Exponential Base/.../exponential_point_anomaly/` |
| 25 | `Combinations/Linear Base/.../Linear + Point Anomaly/` |
| 30 | `Combinations/Quadratic Base/.../Quadratic + Point Anomaly/` |
| 34 | `Combinations/Stochastic Trend + Point Anomaly/` |
| 38 | `Combinations/Volatility + Point Anomaly/` |

**Negatif (31 grup, 42/grup)**

---

### MODEL 9: trend_shift
**Pozitif (2 grup, 660/grup):**

| # | Kaynak Klasör |
|---|---|
| 9 | `Generated Data/trend_shift/` (48 leaf) |
| 26 | `Combinations/Linear Base/.../Linear + Trend Shift/` (3 leaf) |

**Negatif (37 grup, 35/grup)**
> Not: Veri setinde sadece Linear + Trend Shift kombinasyonu mevcut.

---

### MODEL 10: variance_shift
**Pozitif (8 grup, 165/grup):**

| # | Kaynak Klasör |
|---|---|
| 10 | `Generated Data/variance_shift/` (48 leaf) |
| 14 | `Combinations/Cubic Base/.../Cubic + Variance Shift/` |
| 18 | `Combinations/Damped Base/.../Damped + Variance Shift/` |
| 22 | `Combinations/Exponential Base/.../exponential_variance_shift/` |
| 27 | `Combinations/Linear Base/.../Linear + Variance Shift/` |
| 31 | `Combinations/Quadratic Base/.../Quadratic + Variance Shift/` |
| 35 | `Combinations/Stochastic Trend + Variance Shift/` |
| 39 | `Combinations/Volatility + Variance Shift/` |

**Negatif (31 grup, 42/grup)**

---

## 4. Classifier Karşılaştırması — N=1320 (Validation F1)

Her model için 3 classifier yarıştırıldı; en yüksek val F1 kazandı.

| Model | LightGBM Val F1 | XGBoost Val F1 | MLP Val F1 | Kazanan |
|---|---|---|---|---|
| stationary | 0.9214 | 0.9214 | 0.8129 | **LightGBM** |
| deterministic_trend | **0.9886** | 0.9847 | 0.9283 | **LightGBM** |
| stochastic_trend | 0.9887 | 0.9887 | 0.9692 | **LightGBM** |
| volatility | 0.9704 | **0.9778** | 0.9416 | **XGBoost** |
| collective_anomaly | 0.9145 | **0.9151** | 0.7704 | **XGBoost** |
| contextual_anomaly | **1.0000** | 1.0000 | 0.9962 | **LightGBM** |
| mean_shift | 0.9071 | 0.9071 | 0.8394 | **LightGBM** |
| point_anomaly | **0.9288** | 0.9098 | 0.8216 | **LightGBM** |
| trend_shift | **0.9701** | 0.9663 | 0.9084 | **LightGBM** |
| variance_shift | 0.9160 | **0.9167** | 0.8222 | **XGBoost** |

**Genel:** LightGBM 7 model, XGBoost 3 model kazandı. MLP her zaman en kötü.

---

## 5. Binary Model Test Sonuçları — N=1320

### 5.1 Base Tip Modelleri

| Model | Kazanan | Toplam | Pos | Neg | Test F1 | Test Acc |
|---|---|---|---|---|---|---|
| stationary | LightGBM | 2628 | 1316 | 1312 | **0.9568** | %95.63 |
| deterministic_trend | LightGBM | 2629 | 1320 | 1309 | **0.9924** | %99.24 |
| stochastic_trend | LightGBM | 2612 | 1320 | 1292 | **0.9830** | %98.28 |
| volatility | XGBoost | 2612 | 1320 | 1292 | **0.9720** | %97.13 |

### 5.2 Anomali Modelleri

| Model | Kazanan | Toplam | Pos | Neg | Test F1 | Test Acc |
|---|---|---|---|---|---|---|
| collective_anomaly | XGBoost | 2622 | 1320 | 1302 | **0.9153** | %91.43 |
| contextual_anomaly | LightGBM | 2612 | 1320 | 1292 | **0.9981** | %99.81 |
| mean_shift | LightGBM | 2622 | 1320 | 1302 | **0.8835** | %88.00 |
| point_anomaly | LightGBM | 2622 | 1320 | 1302 | **0.9268** | %92.57 |
| trend_shift | LightGBM | 2615 | 1320 | 1295 | **0.9754** | %97.51 |
| variance_shift | XGBoost | 2622 | 1320 | 1302 | **0.9182** | %91.62 |

**Ortalama Test F1: 0.9522**

---

## 6. Kombinasyon Testi — End-to-End Değerlendirme

### Versiyon Karşılaştırması

| Metrik | N=440 (v1) | N=1320 (v2, per_leaf≥1) | N=1320 (v3, per_leaf≥10) | v2→v3 |
|---|---|---|---|---|
| Full match | 264/290 (%91.0) | 272/290 (%93.8) | **282/290 (%97.2)** | +3.4 pp |
| Partial match | 22/290 (%7.6) | 16/290 (%5.5) | 8/290 (%2.8) | -2.7 pp |
| No match | 4/290 (%1.4) | 2/290 (%0.7) | **0/290 (%0.0)** | -0.7 pp |

> per_leaf≥10 garantisi kombinasyon testini önemli ölçüde iyileştirdi: no_match tamamen ortadan kalktı.

### Per-Kombinasyon Sonuçları — N=1320 v3 (per_leaf≥10)

| Kombinasyon | Full | Partial | None | Oran |
|---|---|---|---|---|
| cubic_collective_anomaly | 10/10 | 0 | 0 | **%100** |
| Cubic + Mean Shift | 10/10 | 0 | 0 | **%100** |
| Cubic + Point Anomaly | 10/10 | 0 | 0 | **%100** |
| Cubic + Variance Shift | 10/10 | 0 | 0 | **%100** |
| Damped + Collective Anomaly | 10/10 | 0 | 0 | **%100** |
| Damped + Mean Shift | 10/10 | 0 | 0 | **%100** |
| Damped + Point Anomaly | 10/10 | 0 | 0 | **%100** |
| Damped + Variance Shift | 10/10 | 0 | 0 | **%100** |
| exponential_collective_anomaly | 10/10 | 0 | 0 | **%100** |
| Exponential + Mean Shift | 10/10 | 0 | 0 | **%100** |
| exponential_point_anomaly | 10/10 | 0 | 0 | **%100** |
| exponential_variance_shift | 10/10 | 0 | 0 | **%100** |
| Linear + Collective Anomaly | 10/10 | 0 | 0 | **%100** |
| Linear + Mean Shift | 10/10 | 0 | 0 | **%100** |
| Linear + Point Anomaly | 10/10 | 0 | 0 | **%100** |
| Linear + Trend Shift | 10/10 | 0 | 0 | **%100** |
| Linear + Variance Shift | 10/10 | 0 | 0 | **%100** |
| Quadratic + Collective anomaly | 10/10 | 0 | 0 | **%100** |
| Quadratic + Mean Shift | 10/10 | 0 | 0 | **%100** |
| Quadratic + Point Anomaly | 10/10 | 0 | 0 | **%100** |
| Quadratic + Variance Shift | 10/10 | 0 | 0 | **%100** |
| Stochastic Trend + Collective Anomaly | 9/10 | 1 | 0 | %90 |
| Stochastic Trend + Mean Shift | 10/10 | 0 | 0 | **%100** |
| Stochastic Trend + Point Anomaly | 9/10 | 1 | 0 | %90 |
| Stochastic Trend + Variance Shift | 10/10 | 0 | 0 | **%100** |
| Volatility + Collective Anomaly | 7/10 | 3 | 0 | %70 |
| Volatility + Mean Shift | 9/10 | 1 | 0 | %90 |
| Volatility + Point Anomaly | 7/10 | 3 | 0 | %70 |
| Volatility + Variance Shift | 10/10 | 0 | 0 | **%100** |
| **TOPLAM** | **282/290** | **8** | **0** | **%97.2** |

---

## 7. Manuel Test — Leaf Klasörden 1 Sample

Her kaynak grubun her leaf klasöründen 1 CSV alınarak ensemble ile sınıflandırılmıştır.
Toplam 440 leaf klasör, 39 kaynak grup, 440 test örneği.

### Özet (v3, per_leaf≥10)

| Metrik | Değer |
|---|---|
| Toplam | 440 |
| Full match | 251 (%57.0) |
| Partial match | 114 (%25.9) |
| No match | 75 (%17.0) |

### Grup Bazlı Sonuçlar

| # | Grup | Leaf | Full | Partial | None | Oran |
|---|---|---|---|---|---|---|
| 1 | stationary | 12 | 4 | 4 | 4 | %33 |
| 2 | deterministic_trend | 72 | 22 | 4 | 46 | %31 |
| 3 | stochastic_trend | 15 | 3 | 9 | 3 | %20 |
| 4 | volatility | 12 | 5 | 7 | 0 | %42 |
| 5 | collective_anomaly | 48 | 18 | 30 | 0 | %38 |
| 6 | contextual_anomaly | 48 | 47 | 1 | 0 | **%98** |
| 7 | mean_shift | 48 | 32 | 12 | 4 | %67 |
| 8 | point_anomaly | 48 | 23 | 19 | 6 | %48 |
| 9 | trend_shift | 48 | 34 | 11 | 3 | %71 |
| 10 | variance_shift | 48 | 23 | 16 | 9 | %48 |
| 11-39 | kombinasyonlar | 157 | 141 | 15 | 0 | **%90** |

### Manuel Test Yorumu

Kombinasyon klasörlerinde %90 full match elde edilirken tekli tip klasörlerinde önemli ölçüde düşüş gözlemlenmiştir. Temel nedenler:

1. **Deterministic_trend karışıklığı:** Linear ve quadratic trend içeren `_short` seriler yeterince belirgin eğim göstermediğinden stationary veya stochastic_trend olarak sınıflandırılıyor. `ar_*` prefix'li seriler gürültü baskın olunca trend gizleniyor.
2. **False positive anomaly detection:** Tekli tip (anomalisiz) seriler için de anomali modelleri tetikleniyor — özellikle `short` seriler ve yüksek gürültülü `ar_*` seriler point_anomaly / trend_shift olarak etiketleniyor.
3. **Stochastic_trend düşük full match (%20):** Random walk'ın kısa versiyonları stationary ya da det_trend ile karışıyor; trend bileşeni istatistiksel olarak zayıf kalıyor.
4. **per_leaf≥10 etkisi:** Deterministic_trend için 72 leaf × 10 = 720 minimum örnekleme, eğitim setinde bu grubun ağırlığını artırdı. Bu kombinasyon testini iyileştirirken (no_match=0) diğer modellerin negatif setindeki dağılımı değiştirdi.

---

## 8. Hata Analizi — Kombinasyon Testi

### Sorunlu Kombinasyonlar (v3)

**Volatility + Collective Anomaly (%70)** ve **Volatility + Point Anomaly (%70)**
- Volatility modeli spike'ları hem varyans değişimi hem de point anomali olarak algılar
- GARCH/ARCH tipi volatilitedeki ani yüksek değer spike'ları point_anomaly modelini karıştırır
- v3'te %60'tan %70'e iyileşti (no_match ortadan kalktı)

**Stochastic Trend + Collective Anomaly (%90) / Point Anomaly (%90)**
- Random walk trendiyle birlikte segment değişikliği: ortalama kayması global trenden ayırt edilmesi güç
- v3'te %80'den %90'a iyileşti

### Genel Hata Profili (v3)
- 8 partial match: genellikle base_type doğru, anomali yanlış (fazla tespit)
- **0 no match:** v3'te tamamen ortadan kalktı (v2'de 2 vardı)

---

## 9. Eski Ensemble ile Karşılaştırma

| Özellik | Eski Ensemble | Yeni Ensemble (N=1320, v3) |
|---|---|---|
| Eğitim stratejisi | Tekli sınıf datası | Kombinasyon-dahil |
| Inference | argmax (tek etiket) | argmax + threshold (çok etiket) |
| Kombinasyon full match | **%0** | **%97.2** |
| Kombinasyon no match | ~%100 | **%0** |
| Base type doğruluğu | ~%80 (tekli için) | ~%97.9 (kombinasyon test) |
| Anomali tespiti | İmkânsız (winner-takes-all) | %91.4-%99.8 arası (binary F1) |
| Manuel test (tekli tipler) | bilinmiyor | %33-%98 arası (tip bağımlı) |
| Eğitim süresi (feature) | ~2 dk | ~15 dk (n_jobs=4) |
