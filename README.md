# ensemble-alldata

Zaman serisi sınıflandırma için kombinasyon-farkında binary ensemble. 10 bağımsız binary classifier,
tsfresh EfficientFCParameters (777 feature) üzerinde LightGBM/XGBoost/MLP ile eğitilmiştir.
Her classifier'ın pozitif sınıfı, o tipin bulunduğu **tüm kombinasyon klasörlerini** kapsar —
bu sayede ensemble hem tekli hem de karışık sinyallerde çalışır.

**Kombinasyon testi sonucu: 282/290 full match (%97.2) — no match: 0**

---

## Motivasyon

Klasik çok sınıflı sınıflandırıcı (örneğin 10-class softmax) 2-3-4'lü kombinasyonları tek başına
öğrenemez; olası kombinasyon sayısı 2^10 = 1024'tür ve bunların büyük çoğunluğu için etiketli
veri yoktur. Binary ensemble bu problemi çözer:

- Her model "bu sinyalde X var mı?" sorusunu bağımsız yanıtlar
- Aynı sinyal birden fazla anomali içerebilir, her biri ayrı classifier'dan geçer
- Yeni bir kombinasyon tipi eklenmek istendiğinde sadece ilgili modeller yeniden eğitilir

**Eski ensemble problemi:** Argmax (winner-takes-all) inference → kombinasyon testinde %0 full match.
**Yeni strateji:** Eşik tabanlı çok etiket inference + kombinasyon-dahil eğitim → **%97.2 full match, %0 no match**.

---

## Mimari

```
Girdi: Zaman Serisi (CSV)
         |
         v
[tsfresh EfficientFCParameters]
  777 feature / seri
         |
         v
  ┌─────────────────────────────────────────────────────┐
  │               10 Binary Classifier                  │
  │                                                     │
  │  Base Tipler:          Anomali Tipleri:             │
  │  [stationary?]         [collective_anomaly?]        │
  │  [det_trend?]          [contextual_anomaly?]        │
  │  [stoch_trend?]        [mean_shift?]                │
  │  [volatility?]         [point_anomaly?]             │
  │                        [trend_shift?]               │
  │                        [variance_shift?]            │
  └─────────────────────────────────────────────────────┘
         |
         v
  base_type  = argmax(4 base model)          ← zorunlu tek seçim
  anomalies  = [a if P(a) >= 0.5]            ← sıfır veya daha fazla
```

---

## Veri Seti

### Kaynak Yapısı

39 kaynak grubu (10 tekli tip + 29 kombinasyon):

**Tekli tipler (1-10):**
- 1: `stationary` — AR, MA, ARMA, White Noise (12 leaf klasör)
- 2: `deterministic_trend` — cubic, damped, exponential, linear, quadratic, sinusoidal (72 leaf)
- 3: `stochastic_trend` — ARI, ARIMA, IMA, Random Walk, RWD (15 leaf)
- 4: `volatility` — APARCH, ARCH, EGARCH, GARCH (12 leaf)
- 5-10: tekli anomali tipleri (collective, contextual, mean_shift, point, trend_shift, variance_shift)

**Kombinasyonlar (11-39):**
- 11-14: Cubic Base + anomali (collective, mean_shift, point_anomaly, variance_shift)
- 15-18: Damped Base + anomali
- 19-22: Exponential Base + anomali
- 23-27: Linear Base + anomali (trend_shift dahil)
- 28-31: Quadratic Base + anomali
- 32-35: Stochastic Trend + anomali
- 36-39: Volatility + anomali

### Model Başına Örnekleme (N=1320)

| Model | Pos grup | Pos/grup | Neg grup | Neg/grup | Toplam |
|---|---|---|---|---|---|
| stationary | 7 | 188 | 32 | 41 | ~2628 |
| deterministic_trend | 22 | 60 | 17 | 77 | ~2629 |
| stochastic_trend | 5 | 264 | 34 | 38 | ~2612 |
| volatility | 5 | 264 | 34 | 38 | ~2612 |
| collective_anomaly | 8 | 165 | 31 | 42 | ~2622 |
| contextual_anomaly | 1 | 1320 | 38 | 34 | ~2612 |
| mean_shift | 8 | 165 | 31 | 42 | ~2622 |
| point_anomaly | 8 | 165 | 31 | 42 | ~2622 |
| trend_shift | 2 | 660 | 37 | 35 | ~2615 |
| variance_shift | 8 | 165 | 31 | 42 | ~2622 |

**Örnekleme garantileri:**
- Pozitif sınıf: tüm kaynak gruplarından eşit sayıda örnek
- Negatif sınıf: tüm dışlanan gruplardan eşit sayıda örnek
- Grup içi leaf örnekleme: `per_leaf = max(10, n // len(leaves))` — her leaf'ten **en az 10 örnek** garanti edilir
- Bu garanti, büyük leaf sayılı gruplarda (deterministic_trend: 72 leaf) sınır örneklemesini önler

---

## Feature Extraction

tsfresh `EfficientFCParameters` kullanılmıştır:
- **777 feature** per zaman serisi
- 4 parallel job (`n_jobs=4`)
- Imputation: NaN değerler `tsfresh.utilities.dataframe_functions.impute` ile doldurulur
- Minimum seri uzunluğu: 50 zaman adımı (kısa seriler atlanır)

```python
from tsfresh.feature_extraction import EfficientFCParameters

X = extract_features(
    timeseries_df,
    column_id="id", column_sort="time", column_value="value",
    default_fc_parameters=EfficientFCParameters(),
    n_jobs=4, disable_progressbar=True
)
```

---

## Eğitim Pipeline

```
CSV dosyaları
    → read_series()          # seri okuma ve validasyon
    → extract_features()     # tsfresh 777-feature
    → train/val/test split   # 70/10/20, stratified
    → LightGBM / XGBoost / MLP  # 3 classifier yarışı
    → val F1'e göre best seç
    → test seti üzerinde final değerlendirme
    → model .pkl olarak kaydet (scaler dahil)
```

**Split:** %70 train / %10 val / %20 test, `stratify=y`, `random_state=42`

---

## Sonuçlar

### Binary Model Performansı (N=1320, Test Seti)

| Model | Kazanan | Test F1 | Test Acc |
|---|---|---|---|
| stationary | LightGBM | 0.9568 | %95.63 |
| deterministic_trend | LightGBM | 0.9924 | %99.24 |
| stochastic_trend | LightGBM | 0.9830 | %98.28 |
| volatility | XGBoost | 0.9720 | %97.13 |
| collective_anomaly | XGBoost | 0.9153 | %91.43 |
| contextual_anomaly | LightGBM | 0.9981 | %99.81 |
| mean_shift | LightGBM | 0.8835 | %88.00 |
| point_anomaly | LightGBM | 0.9268 | %92.57 |
| trend_shift | LightGBM | 0.9754 | %97.51 |
| variance_shift | XGBoost | 0.9182 | %91.62 |
| **Ortalama** | LightGBM (7/10) | **0.9522** | **%95.12** |

### Kombinasyon Testi (290 test, 29 kombinasyon × 10 seri)

| | N=440 (v1) | N=1320 (v2, per_leaf≥1) | N=1320 (v3, per_leaf≥10) |
|---|---|---|---|
| Full match | 264/290 (%91.0) | 272/290 (%93.8) | **282/290 (%97.2)** |
| Partial match | 22/290 (%7.6) | 16/290 (%5.5) | 8/290 (%2.8) |
| No match | 4/290 (%1.4) | 2/290 (%0.7) | **0/290 (%0.0)** |

**En iyi kombinasyonlar (%100 full match, v3):** Tüm Cubic, Damped, Exponential, Linear, Quadratic kombinasyonları + Stochastic/Volatility + Variance Shift.

**En zor kombinasyonlar (v3):**
- Volatility + Collective Anomaly: %70 (v2: %60)
- Volatility + Point Anomaly: %70 (v2: %60)
- Volatility + Mean Shift: %90 (v2: %80)
- Stochastic Trend + Collective/Point Anomaly: %90 (v2: %80)

### Manuel Test (440 leaf klasör, 1 sample/leaf)

Her kaynak grubun her leaf klasöründen 1 CSV alınarak ensemble sınıflandırması yapıldı.

| | v3 (per_leaf≥10) |
|---|---|
| Full match | 251/440 (%57.0) |
| Partial match | 114/440 (%25.9) |
| No match | 75/440 (%17.0) |

**Grup bazlı öne çıkanlar:**
- Contextual anomaly: **%98** full match (47/48)
- Kombinasyon klasörleri (gr. 11-39): **%90** full match
- Deterministic_trend (tek): %31 — linear/quadratic short seriler stationary ile karışıyor
- Stochastic_trend (tek): %20 — kısa random walk seriler yeterli trend sergileyemiyor

> Kombinasyon testi ve manuel test arasındaki fark, kombinasyon test setinin eğitim dağılımına yakın örneklerden oluşmasından kaynaklanmaktadır. Manuel test, her leaf klasörden 1 örnek aldığı için daha zorlayıcı ve dağılım dışı senaryoları kapsar.

---

## Proje Yapısı

```
ensemble-alldata/
├── config.py           # Yollar, N, kaynak grupları, model pozitif grupları
├── processor.py        # CSV okuma, örnekleme, tsfresh extraction
├── trainer.py          # LightGBM/XGBoost/MLP eğitimi, model kaydetme
├── evaluator.py        # Kombinasyon testi, decode_prediction
├── main.py             # Orkestrasyon (--force, --train, --eval)
├── plan.md             # Detaylı strateji ve örnekleme planı
├── tree.md             # Kaynak grup ağaç yapısı
├── manueltest.py       # Her leaf klasörden 1 örnek alıp ensemble ile sınıflandırır
├── results/
│   ├── results.md              # Tam sonuç raporu (bu dosya)
│   ├── manueltest.md           # Manuel test sonuçları (440 leaf, 1 sample/leaf)
│   ├── training_results.json   # [gitignore] Binary model test metrikleri
│   └── combination_eval.json   # [gitignore] Kombinasyon testi detayları
├── processed_data/     # [gitignore] tsfresh features (.npy)
└── trained_models/     # [gitignore] eğitilmiş modeller (.pkl)
```

---

## Kurulum ve Çalıştırma

### Gereksinimler

```bash
pip install tsfresh lightgbm xgboost scikit-learn pandas numpy tqdm
```

### Tam Pipeline

```bash
# Feature extraction + Training + Kombinasyon testi
python main.py

# Zorla yeniden işle (cache varsa bile)
python main.py --force

# Sadece belirli model
python main.py --model stationary

# Sadece eğitim (features hazır varsayılır)
python main.py --train

# Sadece kombinasyon testi (modeller hazır varsayılır)
python main.py --eval
```

### config.py Parametreleri

```python
N = 1320           # pozitif ve negatif örnek sayısı per model
TEST_SIZE = 0.20   # test seti oranı
VALIDATION_SIZE = 0.10  # validasyon seti oranı
THRESHOLD = 0.5    # anomali modellerinde pozitif eşik
MIN_SERIES_LENGTH = 50  # minimum seri uzunluğu
RANDOM_STATE = 42
```

---

## Teknik Notlar

### tsfresh n_jobs
`n_jobs=-1` tsfresh'te geçersizdir (sklearn'den farklı). Pozitif integer kullanılmalıdır.
Mevcut konfigürasyon: `n_jobs=4`.

### Örnekleme Denklemi
```
pos_per_group = floor(N / len(pos_groups))
neg_per_group = floor(N / len(neg_groups))
per_leaf      = max(10, n // len(leaves))   # her leaf'ten en az 10 örnek
```
Grup içi leaf klasörlerden eşit örnekleme yapılır; hedef sayıya ulaşılamazsa rastgele tamamlama.

### Kombinasyon Testi vs Manuel Test Farkı

| | Kombinasyon Testi | Manuel Test |
|---|---|---|
| Amaç | Çok-etiket (combo) doğruluğu | Her leaf klasörden coverage |
| Sample sayısı | 290 (29 combo × 10) | 440 (tüm leafler × 1) |
| Kapsam | Sadece kombinasyon klasörleri | Tekli + kombinasyon tüm leafler |
| Zorluk | Orta (eğitim dağılımına yakın) | Yüksek (dağılım dışı senaryolar) |
| v3 Full match | **%97.2** | %57.0 |

Kombinasyon testi "öğrenilmiş kombinasyonlar" üzerindeki performansı ölçerken,
manuel test modelin genelleme kapasitesini ve kenar senaryolardaki davranışını gösterir.

### Inference
```python
base_probs  = [models[b].predict_proba(X) for b in BASE_MODELS]
base_type   = BASE_MODELS[argmax(base_probs)]

anomalies   = [
    a for a in ANOMALY_MODELS
    if models[a].predict_proba(X)[1] >= THRESHOLD
]
```
