# ensemble-alldata

Zaman serisi sınıflandırma için kombinasyon-farkında binary ensemble sistemi.
10 bağımsız binary classifier, tsfresh `EfficientFCParameters` (777 feature) üzerinde
LightGBM / XGBoost / MLP ile eğitilmiştir. Her classifier'ın pozitif sınıfı, o tipin
bulunduğu **tüm kombinasyon klasörlerini** kapsar — bu sayede ensemble hem tekli hem de
karışık sinyallerde doğru sınıflandırma yapabilir.

---

## Özet Sonuçlar

| Test | Full match | Partial | No match |
|---|---|---|---|
| Kombinasyon testi (v3, 290 örnek) | **282/290 (%97.2)** | 8/290 (%2.8) | **0/290 (%0.0)** |
| Manuel test (440 leaf klasör, 1 örnek/leaf) | 251/440 (%57.0) | 114/440 (%25.9) | 75/440 (%17.0) |
| Ortalama binary F1 (test seti) | **0.9522** | — | — |

---

## İçindekiler

1. [Motivasyon ve Algoritma Evrimi](#1-motivasyon-ve-algoritma-evrimi)
2. [Veri Seti Yapısı](#2-veri-seti-yapısı)
3. [Feature Extraction](#3-feature-extraction)
4. [Örnekleme Metodolojisi](#4-örnekleme-metodolojisi)
5. [Eğitim Pipeline](#5-eğitim-pipeline)
6. [Her Model için Pozitif / Negatif Kaynaklar](#6-her-model-için-pozitif--negatif-kaynaklar)
7. [Binary Model Sonuçları](#7-binary-model-sonuçları)
8. [Inference Mekanizması](#8-inference-mekanizması)
9. [Kombinasyon Testi — Detaylı Sonuçlar](#9-kombinasyon-testi--detaylı-sonuçlar)
10. [Manuel Test — Tüm Leaf Klasörler](#10-manuel-test--tüm-leaf-klasörler)
11. [Hata Analizi](#11-hata-analizi)
12. [Proje Yapısı ve Kurulum](#12-proje-yapısı-ve-kurulum)

---

## 1. Motivasyon ve Algoritma Evrimi

### Eski Ensemble — Winner-Takes-All

Önceki yaklaşımda her binary model yalnızca **tekli anomali datalarıyla** eğitilmiş,
inference ise argmax (winner-takes-all) ile yapılmıştı:

```
pred = argmax([P(stationary), P(det_trend), P(stoch_trend), P(volatility),
               P(collective), P(contextual), P(mean_shift), P(point_anomaly),
               P(trend_shift), P(variance_shift)])
```

Bu yapının iki temel sorunu vardı:

1. **Tek etiket çıktısı:** Bir sinyalde hem `deterministic_trend` hem `mean_shift` varsa
   argmax yalnızca birini seçer. Kombinasyon testi sonucu: **%0 full match**.

2. **Eğitim seti eksikliği:** `deterministic_trend` modeli yalnızca düz trend verisiyle
   eğitilmişti; `det_trend + mean_shift` birleşimini görmemişti. Kombinasyon gelince
   model karışıyordu.

### Yeni Ensemble — Kombinasyon-Dahil Binary

Strateji iki boyutta değişti:

**Eğitim:** Her modelin pozitif sınıfı, o tipin bulunduğu **tüm kombinasyon klasörlerini**
içeriyor. Örneğin `collective_anomaly` modeli; hem düz `collective_anomaly/` verisiyle
hem de Cubic+Collective, Stochastic+Collective, Volatility+Collective gibi tüm kombinasyon
klasörlerindeki verilerle eğitiliyor.

**Inference:** Base type ve anomaliler ayrı ayrı belirleniyor:

```python
# Base type: 4 base modelinden hangisinin pozitif olasılığı en yüksekse
base_type = argmax({stationary, det_trend, stoch_trend, volatility})

# Anomaliler: 6 anomali modelinden hangileri >= 0.5 eşiğini geçiyorsa
anomalies = [a for a in ANOMALY_MODELS if P(a) >= 0.5]
```

Bu yaklaşım:
- Çok etiketli çıktıya izin verir (`det_trend + mean_shift + variance_shift` gibi)
- Base type seçimi zorunlu ve tek kalır (argmax)
- Anomali sayısı 0 ile 6 arasında değişebilir

### Versiyon Geçmişi

| Versiyon | N | per_leaf min | Kombin. full | Manuel test full |
|---|---|---|---|---|
| v1 | 440 | 1 | 264/290 (%91.0) | — |
| v2 | 1320 | 1 | 272/290 (%93.8) | 300/440 (%68.2) |
| v3 (son) | 1320 | **10** | **282/290 (%97.2)** | 251/440 (%57.0) |

> **per_leaf≥10 neden gerekli oldu?** `deterministic_trend` grubunda 72 leaf klasör var.
> v2'de `per_leaf = floor(60/72) = 0 → max(1, 0) = 1` oluyordu; yani her leaften en fazla
> 1 örnek seçiliyordu ve bazı leafler hiç temsil edilemiyordu. Bu model için bazı trend
> şekillerini (özellikle quadratic) neredeyse hiç görmeden eğitim tamamlanıyordu.
> v3'te `per_leaf = max(10, floor(n/n_leaves))` garantisi eklendi.

---

## 2. Veri Seti Yapısı

### 39 Kaynak Grubu

Tüm veri `Generated Data/` ve `Generated Data/Combinations/` dizinleri altındadır.

#### Tekli Tipler (Grup 1–10)

| # | İsim | Dizin | Leaf Klasör | İçerik |
|---|---|---|---|---|
| 1 | stationary | `Generated Data/stationary/` | 12 | AR, MA, ARMA, White Noise × {short, medium, long} |
| 2 | deterministic_trend | `Generated Data/deterministic_trend/` | 72 | {ar, arma, ma, white_noise} × {cubic, damped, exponential, linear_down, linear_up, quadratic, sinusoidal} × {short, medium, long} |
| 3 | stochastic_trend | `Generated Data/Stochastic Trend/` | 15 | {ARI, ARIMA, IMA, RW, RWD} × {short, medium, long} |
| 4 | volatility | `Generated Data/Volatility/` | 12 | {APARCH, ARCH, EGARCH, GARCH} × {short, medium, long} |
| 5 | collective_anomaly | `Generated Data/collective_anomaly/` | 48 | {ar, arma, ma, white_noise} × {short, medium, long} × {beginning, end, middle, multiple} |
| 6 | contextual_anomaly | `Generated Data/contextual_anomaly/` | 48 | {ar, arma, ma, white_noise} × {short, medium, long} × {beginning, end, middle, multiple} |
| 7 | mean_shift | `Generated Data/mean_shift/` | 48 | {ar, arma, ma, white_noise} × {short, medium, long} × {beginning, end, middle, multiple} |
| 8 | point_anomaly | `Generated Data/point_anomaly/` | 48 | {ar, arma, ma, white_noise} × {short, medium, long} × {single_beginning, single_end, single_middle, multiple} |
| 9 | trend_shift | `Generated Data/trend_shift/` | 48 | {ar, arma, ma, white_noise} × {short, medium, long} × {beginning, end, middle, multiple} |
| 10 | variance_shift | `Generated Data/variance_shift/` | 48 | {ar, arma, ma, white_noise} × {short, medium, long} × {beginning, end, middle, multiple} |

**Not:** Tekli anomali grupları (5–10) base olarak `stationary` içeriyor. Yani bu
klasörler `stationary + <anomaly>` etiketiyle işaretleniyor.

#### Cubic Base Kombinasyonları (Grup 11–14)

| # | İsim | Dizin | Leaf | Ground Truth |
|---|---|---|---|---|
| 11 | cubic+collective | `Combinations/Cubic Base/Cubic Base/cubic_collective_anomaly/` | 1 | deterministic_trend + collective_anomaly |
| 12 | cubic+mean_shift | `Combinations/Cubic Base/Cubic Base/Cubic + Mean Shift/` | 2 | deterministic_trend + mean_shift |
| 13 | cubic+point_anomaly | `Combinations/Cubic Base/Cubic Base/Cubic + Point Anomaly/` | 1 | deterministic_trend + point_anomaly |
| 14 | cubic+variance_shift | `Combinations/Cubic Base/Cubic Base/Cubic + Variance Shift/` | 1 | deterministic_trend + variance_shift |

#### Damped Base Kombinasyonları (Grup 15–18)

| # | İsim | Dizin | Leaf | Ground Truth |
|---|---|---|---|---|
| 15 | damped+collective | `Combinations/Damped Base/Damped Base/Damped + Collective Anomaly/` | 1 | deterministic_trend + collective_anomaly |
| 16 | damped+mean_shift | `Combinations/Damped Base/Damped Base/Damped + Mean Shift/` | 2 | deterministic_trend + mean_shift |
| 17 | damped+point_anomaly | `Combinations/Damped Base/Damped Base/Damped + Point Anomaly/` | 1 | deterministic_trend + point_anomaly |
| 18 | damped+variance_shift | `Combinations/Damped Base/Damped Base/Damped + Variance Shift/` | 1 | deterministic_trend + variance_shift |

#### Exponential Base Kombinasyonları (Grup 19–22)

| # | İsim | Dizin | Leaf | Ground Truth |
|---|---|---|---|---|
| 19 | exp+collective | `Combinations/Exponential Base/Exponential Base/exponential_collective_anomaly/` | 1 | deterministic_trend + collective_anomaly |
| 20 | exp+mean_shift | `Combinations/Exponential Base/Exponential Base/Exponential + Mean Shift/` | 2 | deterministic_trend + mean_shift |
| 21 | exp+point_anomaly | `Combinations/Exponential Base/Exponential Base/exponential_point_anomaly/` | 1 | deterministic_trend + point_anomaly |
| 22 | exp+variance_shift | `Combinations/Exponential Base/Exponential Base/exponential_variance_shift/` | 1 | deterministic_trend + variance_shift |

#### Linear Base Kombinasyonları (Grup 23–27)

| # | İsim | Dizin | Leaf | Ground Truth |
|---|---|---|---|---|
| 23 | linear+collective | `Combinations/Linear Base/Linear Base/Linear + Collective Anomaly/` | 1 | deterministic_trend + collective_anomaly |
| 24 | linear+mean_shift | `Combinations/Linear Base/Linear Base/Linear + Mean Shift/` | 2 | deterministic_trend + mean_shift |
| 25 | linear+point_anomaly | `Combinations/Linear Base/Linear Base/Linear + Point Anomaly/` | 1 | deterministic_trend + point_anomaly |
| 26 | linear+trend_shift | `Combinations/Linear Base/Linear Base/Linear + Trend Shift/` | 3 | deterministic_trend + trend_shift |
| 27 | linear+variance_shift | `Combinations/Linear Base/Linear Base/Linear + Variance Shift/` | 1 | deterministic_trend + variance_shift |

#### Quadratic Base Kombinasyonları (Grup 28–31)

| # | İsim | Dizin | Leaf | Ground Truth |
|---|---|---|---|---|
| 28 | quad+collective | `Combinations/Quadratic Base/Quadratic Base/Quadratic + Collective anomaly/` | 1 | deterministic_trend + collective_anomaly |
| 29 | quad+mean_shift | `Combinations/Quadratic Base/Quadratic Base/Quadratic + Mean Shift/` | 2 | deterministic_trend + mean_shift |
| 30 | quad+point_anomaly | `Combinations/Quadratic Base/Quadratic Base/Quadratic + Point Anomaly/` | 2 | deterministic_trend + point_anomaly |
| 31 | quad+variance_shift | `Combinations/Quadratic Base/Quadratic Base/Quadratic + Variance Shift/` | 1 | deterministic_trend + variance_shift |

#### Stochastic Trend Kombinasyonları (Grup 32–35)

| # | İsim | Dizin | Leaf | Ground Truth |
|---|---|---|---|---|
| 32 | stoch+collective | `Combinations/Stochastic Trend + Collective Anomaly/` | 1 | stochastic_trend + collective_anomaly |
| 33 | stoch+mean_shift | `Combinations/Stochastic Trend + Mean Shift/` | 1 | stochastic_trend + mean_shift |
| 34 | stoch+point_anomaly | `Combinations/Stochastic Trend + Point Anomaly/` | 1 | stochastic_trend + point_anomaly |
| 35 | stoch+variance_shift | `Combinations/Stochastic Trend + Variance Shift/Stochastic Trend + Variance Shift/` | 5 | stochastic_trend + variance_shift |

#### Volatility Kombinasyonları (Grup 36–39)

| # | İsim | Dizin | Leaf | Ground Truth |
|---|---|---|---|---|
| 36 | vol+collective | `Combinations/Volatility + Collective Anomaly/` | 1 | volatility + collective_anomaly |
| 37 | vol+mean_shift | `Combinations/Volatility + Mean Shift/` | 1 | volatility + mean_shift |
| 38 | vol+point_anomaly | `Combinations/Volatility + Point Anomaly/` | 1 | volatility + point_anomaly |
| 39 | vol+variance_shift | `Combinations/Volatility + Variance Shift/` | 1 | volatility + variance_shift |

**Toplam:** 39 grup, 440 leaf klasör, yüzlerce bin CSV dosyası.

---

## 3. Feature Extraction

### tsfresh EfficientFCParameters

Her zaman serisi, `tsfresh` kütüphanesinin `EfficientFCParameters` ayarıyla işleniyor.

```python
from tsfresh import extract_features
from tsfresh.feature_extraction import EfficientFCParameters
from tsfresh.utilities.dataframe_functions import impute

X_df = extract_features(
    timeseries_df,          # {id, time, value} formatında uzun DataFrame
    column_id="id",
    column_sort="time",
    column_value="value",
    default_fc_parameters=EfficientFCParameters(),
    disable_progressbar=True,
    n_jobs=4,               # Not: tsfresh'te n_jobs=-1 GEÇERSIZ
)
impute(X_df)                # NaN değerleri impute et
```

| Parametre | Değer |
|---|---|
| Feature seti | EfficientFCParameters |
| Feature sayısı | **777** (her seri başına) |
| NaN işleme | `tsfresh.utilities.dataframe_functions.impute` |
| Minimum seri uzunluğu | 50 zaman adımı (kısa seriler atlanır) |
| Paralel iş sayısı | `n_jobs=4` |

> **Kritik not:** `tsfresh`, scikit-learn gibi `n_jobs=-1` (tüm çekirdekler) parametresini
> desteklemez. Pozitif bir integer kullanılmalıdır. `-1` verildiğinde `ValueError: Number
> of processes must be at least 1` hatası alınır.

### Feature Nitelikleri

`EfficientFCParameters`, tüm `ComprehensiveFCParameters`'ın hesaplama açısından pahalı
olanlarını çıkarılmış versiyonudur. Şu kategorilerdeki istatistiksel özellikler hesaplanır:

- Zaman alanı istatistikleri (mean, std, skewness, kurtosis, entropy...)
- Otokorelasyon (ACF, PACF bazlı özellikler)
- Spectral özellikler (FFT bazlı)
- Doğrusal olmayan dinamik özellikler (Hurst exponent benzeri)
- Dağılım özellikleri (quantile, percentile bazlı)
- Değişim noktası özellikleri (number_cwt_peaks, change_quantile...)
- Doğrusal regresyon bazlı özellikler (trend slope, intercept)

---

## 4. Örnekleme Metodolojisi

### Genel Çerçeve

Her binary model için `N=1320` pozitif ve `N=1320` negatif örnek toplanır.
Pozitif ve negatif kaynaklar, model bazında farklı grup setlerinden alınır (bkz. Bölüm 6).

```python
pos_per_group = floor(N / len(pos_groups))   # her pozitif gruba düşen hedef
neg_per_group = floor(N / len(neg_groups))   # her negatif gruba düşen hedef
```

### Grup İçi Üç Aşamalı Örnekleme

Bir grup içinde CSV'ler, leaf klasör kapsam garantisiyle şu üç aşamada seçilir:

```python
per_leaf = max(10, n // len(leaves))   # her leaften alınacak maksimum örnek

# Faz 1: Her leaf klasörden 1 örnek (kapsam garantisi)
for leaf in leaves:
    chosen = random.choice(pool[leaf])
    phase1.append(chosen)

# Eğer n < n_leaves: tüm leafleri kapsamak mümkün değil → shuffle + truncate
if len(phase1) >= n:
    random.shuffle(phase1)
    return phase1[:n]

# Faz 2: Bütçe izin verdikçe her leaften (per_leaf - 1) kadar daha al
for leaf in leaves:
    k = min(per_leaf - 1, len(leftover[leaf]), remaining_budget)
    phase2.extend(random.sample(leftover[leaf], k))

# Faz 3: Hâlâ eksikse tüm havuzdan rastgele tamamla
if len(result) < n:
    extra = random.sample(all_csvs - already, n - len(result))
    result.extend(extra)
```

### per_leaf≥10 Garantisinin Önemi

`deterministic_trend` grubunda 72 leaf klasör var. `N=1320`, 22 pozitif gruba bölündüğünde
her gruba `floor(1320/22) = 60` örnek düşüyor.

- v2 (per_leaf=1): `max(1, floor(60/72)) = max(1, 0) = 1` → 60 leafin 60'ından birer örnek,
  12 leaf hiç temsil edilmez
- v3 (per_leaf=10): `max(10, 0) = 10` → her leaf en az 10 örnek → bu gruba 720 örnek çekilir,
  ardından rastgele tamamlama ile 60'a sıkıştırılır ama her leaf garantili temsil edilmiş olur

Bu değişiklik kombinasyon testinde no_match'i sıfırladı (%0.7 → %0.0) ve full match'i artırdı.

---

## 5. Eğitim Pipeline

### Veri Bölünmesi

```
%70 train / %10 validation / %20 test
stratify=y ile her bölümde sınıf dengesi korunur
random_state=42
```

Teknik olarak:

```python
X_tmp, X_te, y_tmp, y_te = train_test_split(X, y, test_size=0.20, stratify=y, random_state=42)
val_ratio_adj = 0.10 / (1 - 0.20)   # = 0.125
X_tr, X_val, y_tr, y_val = train_test_split(X_tmp, y_tmp, test_size=val_ratio_adj, stratify=y_tmp, random_state=42)
```

### Ölçekleme

Her model için `StandardScaler` fit edilir (train setinde), val ve test setlerine transform
uygulanır. Scaler, eğitilmiş model ile birlikte `.pkl` dosyasına kaydedilir.

### Classifier Hiperparametreleri

**LightGBM:**

```python
lgb.LGBMClassifier(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=7,
    num_leaves=63,
    subsample=0.8,
    colsample_bytree=0.8,
    class_weight="balanced",
    random_state=42,
    n_jobs=-1,
    verbose=-1,
)
```

**XGBoost:**

```python
xgb.XGBClassifier(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=7,
    subsample=0.8,
    colsample_bytree=0.8,
    scale_pos_weight=neg_count / pos_count,   # sınıf dengesi
    random_state=42,
    n_jobs=-1,
    eval_metric="logloss",
    verbosity=0,
)
```

**MLP (sklearn):**

```python
MLPClassifier(
    hidden_layer_sizes=(256, 128, 64),
    max_iter=500,
    early_stopping=True,
    validation_fraction=0.1,
    random_state=42,
)
```

### Model Seçimi

Her binary model için üç classifier eğitilir. Validation F1 skoru en yüksek olan seçilir
ve test seti üzerinde final değerlendirme yapılır. Kazanan model `.pkl` olarak kaydedilir.

---

## 6. Her Model için Pozitif / Negatif Kaynaklar

### Model 1: stationary

**Pozitif (7 grup, 188 örnek/grup):** Tüm stationary base içeren gruplar

| Grup ID | Grup Adı | Leaf | Açıklama |
|---|---|---|---|
| 1 | stationary | 12 | Saf AR/MA/ARMA/WN seriler |
| 5 | collective_anomaly | 48 | Stationary + collective anomaly |
| 6 | contextual_anomaly | 48 | Stationary + contextual anomaly |
| 7 | mean_shift | 48 | Stationary + mean shift |
| 8 | point_anomaly | 48 | Stationary + point anomaly |
| 9 | trend_shift | 48 | Stationary + trend shift |
| 10 | variance_shift | 48 | Stationary + variance shift |

**Negatif (32 grup, 41 örnek/grup):** Deterministic trend, stochastic trend, volatility
ve tüm kombinasyon grupları (11–39 arası).

---

### Model 2: deterministic_trend

**Pozitif (22 grup, 60 örnek/grup):** Tüm deterministic trend içeren gruplar

| Grup ID | Grup Adı |
|---|---|
| 2 | deterministic_trend (72 leaf: cubic/damped/exponential/linear_down/linear_up/quadratic × {ar, arma, ma, white_noise} × {short, medium, long}) |
| 11 | cubic+collective |
| 12 | cubic+mean_shift |
| 13 | cubic+point_anomaly |
| 14 | cubic+variance_shift |
| 15 | damped+collective |
| 16 | damped+mean_shift |
| 17 | damped+point_anomaly |
| 18 | damped+variance_shift |
| 19 | exp+collective |
| 20 | exp+mean_shift |
| 21 | exp+point_anomaly |
| 22 | exp+variance_shift |
| 23 | linear+collective |
| 24 | linear+mean_shift |
| 25 | linear+point_anomaly |
| 26 | linear+trend_shift |
| 27 | linear+variance_shift |
| 28 | quad+collective |
| 29 | quad+mean_shift |
| 30 | quad+point_anomaly |
| 31 | quad+variance_shift |

**Negatif (17 grup, 77 örnek/grup):** Stationary, stochastic_trend, volatility ve
stochastic/volatility kombinasyon grupları (32–39).

---

### Model 3: stochastic_trend

**Pozitif (5 grup, 264 örnek/grup):**

| Grup ID | Grup Adı | Leaf |
|---|---|---|
| 3 | stochastic_trend | 15 (ARI/ARIMA/IMA/RW/RWD × short/medium/long) |
| 32 | stoch+collective | 1 |
| 33 | stoch+mean_shift | 1 |
| 34 | stoch+point_anomaly | 1 |
| 35 | stoch+variance_shift | 5 |

**Negatif (34 grup, 38 örnek/grup):** Geri kalan tüm 34 grup.

---

### Model 4: volatility

**Pozitif (5 grup, 264 örnek/grup):**

| Grup ID | Grup Adı | Leaf |
|---|---|---|
| 4 | volatility | 12 (APARCH/ARCH/EGARCH/GARCH × short/medium/long) |
| 36 | vol+collective | 1 |
| 37 | vol+mean_shift | 1 |
| 38 | vol+point_anomaly | 1 |
| 39 | vol+variance_shift | 1 |

**Negatif (34 grup, 38 örnek/grup):** Geri kalan tüm 34 grup.

---

### Model 5: collective_anomaly

**Pozitif (8 grup, 165 örnek/grup):**

| Grup ID | Grup Adı |
|---|---|
| 5 | collective_anomaly |
| 11 | cubic+collective |
| 15 | damped+collective |
| 19 | exp+collective |
| 23 | linear+collective |
| 28 | quad+collective |
| 32 | stoch+collective |
| 36 | vol+collective |

**Negatif (31 grup, 42 örnek/grup):** Collective içermeyen tüm gruplar.

---

### Model 6: contextual_anomaly

**Pozitif (1 grup, 1320 örnek/grup):**

| Grup ID | Grup Adı | Not |
|---|---|---|
| 6 | contextual_anomaly | Veri setinde contextual anomaly için kombinasyon klasörü mevcut değil |

**Negatif (38 grup, 34 örnek/grup):** Geri kalan tüm 38 grup.

---

### Model 7: mean_shift

**Pozitif (8 grup, 165 örnek/grup):**

| Grup ID | Grup Adı |
|---|---|
| 7 | mean_shift |
| 12 | cubic+mean_shift |
| 16 | damped+mean_shift |
| 20 | exp+mean_shift |
| 24 | linear+mean_shift |
| 29 | quad+mean_shift |
| 33 | stoch+mean_shift |
| 37 | vol+mean_shift |

**Negatif (31 grup, 42 örnek/grup):** Mean shift içermeyen tüm gruplar.

---

### Model 8: point_anomaly

**Pozitif (8 grup, 165 örnek/grup):**

| Grup ID | Grup Adı |
|---|---|
| 8 | point_anomaly |
| 13 | cubic+point_anomaly |
| 17 | damped+point_anomaly |
| 21 | exp+point_anomaly |
| 25 | linear+point_anomaly |
| 30 | quad+point_anomaly |
| 34 | stoch+point_anomaly |
| 38 | vol+point_anomaly |

**Negatif (31 grup, 42 örnek/grup):** Point anomaly içermeyen tüm gruplar.

---

### Model 9: trend_shift

**Pozitif (2 grup, 660 örnek/grup):**

| Grup ID | Grup Adı | Not |
|---|---|---|
| 9 | trend_shift | 48 leaf |
| 26 | linear+trend_shift | 3 leaf — veri setinde yalnızca Linear base'de trend_shift kombinasyonu var |

**Negatif (37 grup, 35 örnek/grup):** Trend shift içermeyen tüm gruplar.

---

### Model 10: variance_shift

**Pozitif (8 grup, 165 örnek/grup):**

| Grup ID | Grup Adı |
|---|---|
| 10 | variance_shift |
| 14 | cubic+variance_shift |
| 18 | damped+variance_shift |
| 22 | exp+variance_shift |
| 27 | linear+variance_shift |
| 31 | quad+variance_shift |
| 35 | stoch+variance_shift |
| 39 | vol+variance_shift |

**Negatif (31 grup, 42 örnek/grup):** Variance shift içermeyen tüm gruplar.

---

## 7. Binary Model Sonuçları

### 7.1 Validation F1 — Classifier Yarışması (N=1320, v3)

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

LightGBM 7/10 modelde, XGBoost 3/10 modelde kazandı. MLP her modelde en düşük performans.

### 7.2 Test Seti Sonuçları — Base Tip Modelleri

| Model | Kazanan | Toplam | Pozitif | Negatif | Test F1 | Test Acc |
|---|---|---|---|---|---|---|
| stationary | LightGBM | 2628 | 1316 | 1312 | **0.9568** | %95.63 |
| deterministic_trend | LightGBM | 2629 | 1320 | 1309 | **0.9924** | %99.24 |
| stochastic_trend | LightGBM | 2612 | 1320 | 1292 | **0.9830** | %98.28 |
| volatility | XGBoost | 2612 | 1320 | 1292 | **0.9720** | %97.13 |

### 7.3 Test Seti Sonuçları — Anomali Modelleri

| Model | Kazanan | Toplam | Pozitif | Negatif | Test F1 | Test Acc |
|---|---|---|---|---|---|---|
| collective_anomaly | XGBoost | 2622 | 1320 | 1302 | **0.9153** | %91.43 |
| contextual_anomaly | LightGBM | 2612 | 1320 | 1292 | **0.9981** | %99.81 |
| mean_shift | LightGBM | 2622 | 1320 | 1302 | **0.8835** | %88.00 |
| point_anomaly | LightGBM | 2622 | 1320 | 1302 | **0.9268** | %92.57 |
| trend_shift | LightGBM | 2615 | 1320 | 1295 | **0.9754** | %97.51 |
| variance_shift | XGBoost | 2622 | 1320 | 1302 | **0.9182** | %91.62 |

**Ortalama Test F1: 0.9522** (10 model ortalaması)

### 7.4 Gözlemler

- `contextual_anomaly` modeli en yüksek performanslı (%99.81 acc). Sebebi: veri setinde
  yalnızca 1 pozitif grup var ve bu grup görsel olarak çok belirgin bir pattern sergilemekte.
- `mean_shift` en düşük F1 (0.8835). Mean shift, variance shift ve collective anomaly ile
  örtüşen durumlar var; model sınırda kalan örnekleri karıştırıyor.
- Base tip modelleri anomali modellerine kıyasla daha yüksek F1 sergiliyor (0.9720–0.9924 vs
  0.8835–0.9981). Base tipler daha geniş, belirgin pattern farklılıklarına sahip.

---

## 8. Inference Mekanizması

### Predict Pipeline

```python
# 1. CSV oku
data = read_series(csv_path)          # (T,) array

# 2. tsfresh feature extraction
df = pd.DataFrame({"id": 0, "time": range(len(data)), "value": data})
X_df = extract_features(df, ...)      # (1, 777) DataFrame
impute(X_df)

# 3. 10 model üzerinden olasılık al
probs = {}
for name, bundle in models.items():
    X_scaled = bundle["scaler"].transform(X_df.values)
    probs[name] = bundle["model"].predict_proba(X_scaled)[0, 1]

# 4. Decode
base_probs = {m: probs[m] for m in ["stationary", "deterministic_trend",
                                     "stochastic_trend", "volatility"]}
base_type  = max(base_probs, key=base_probs.get)   # argmax

THRESHOLD = 0.5
anomalies = [m for m in ["collective_anomaly", "contextual_anomaly",
                           "mean_shift", "point_anomaly",
                           "trend_shift", "variance_shift"]
             if probs[m] >= THRESHOLD]
```

### Match Türleri

Kombinasyon testinde her tahmin şu şekilde değerlendirilir:

| Match Türü | Koşul |
|---|---|
| **FULL** | `base_type == true_base` AND `true_anomaly in pred_anomalies` |
| **PARTIAL** | `base_type == true_base` OR `true_anomaly in pred_anomalies` (ama ikisi birden değil) |
| **NONE** | Ne base, ne anomali doğru |

Manuel testte tekli tip grupları için (anomali içermeyen):

| Match Türü | Koşul |
|---|---|
| **FULL** | `base_type == true_base` AND `len(pred_anomalies) == 0` |
| **PARTIAL** | `base_type == true_base` ama false positive anomali var |
| **NONE** | `base_type != true_base` |

---

## 9. Kombinasyon Testi — Detaylı Sonuçlar

### 9.1 Versiyon Karşılaştırması

Her kombinasyon klasöründen 10 CSV rastgele örnekleniyor → 29 kombinasyon × 10 = **290 test**.

| Metrik | N=440 (v1) | N=1320 (v2, per_leaf≥1) | N=1320 (v3, per_leaf≥10) | v2→v3 delta |
|---|---|---|---|---|
| Full match | 264/290 (%91.0) | 272/290 (%93.8) | **282/290 (%97.2)** | +3.4 pp |
| Partial match | 22/290 (%7.6) | 16/290 (%5.5) | 8/290 (%2.8) | −2.7 pp |
| No match | 4/290 (%1.4) | 2/290 (%0.7) | **0/290 (%0.0)** | −0.7 pp |

### 9.2 Per-Kombinasyon Sonuçları (v3, per_leaf≥10)

| Kombinasyon | True Label | Full | Partial | None | Oran |
|---|---|---|---|---|---|
| cubic_collective_anomaly | det_trend + collective | 10/10 | 0 | 0 | **%100** |
| Cubic + Mean Shift | det_trend + mean_shift | 10/10 | 0 | 0 | **%100** |
| Cubic + Point Anomaly | det_trend + point_anomaly | 10/10 | 0 | 0 | **%100** |
| Cubic + Variance Shift | det_trend + variance_shift | 10/10 | 0 | 0 | **%100** |
| Damped + Collective Anomaly | det_trend + collective | 10/10 | 0 | 0 | **%100** |
| Damped + Mean Shift | det_trend + mean_shift | 10/10 | 0 | 0 | **%100** |
| Damped + Point Anomaly | det_trend + point_anomaly | 10/10 | 0 | 0 | **%100** |
| Damped + Variance Shift | det_trend + variance_shift | 10/10 | 0 | 0 | **%100** |
| exponential_collective_anomaly | det_trend + collective | 10/10 | 0 | 0 | **%100** |
| Exponential + Mean Shift | det_trend + mean_shift | 10/10 | 0 | 0 | **%100** |
| exponential_point_anomaly | det_trend + point_anomaly | 10/10 | 0 | 0 | **%100** |
| exponential_variance_shift | det_trend + variance_shift | 10/10 | 0 | 0 | **%100** |
| Linear + Collective Anomaly | det_trend + collective | 10/10 | 0 | 0 | **%100** |
| Linear + Mean Shift | det_trend + mean_shift | 10/10 | 0 | 0 | **%100** |
| Linear + Point Anomaly | det_trend + point_anomaly | 10/10 | 0 | 0 | **%100** |
| Linear + Trend Shift | det_trend + trend_shift | 10/10 | 0 | 0 | **%100** |
| Linear + Variance Shift | det_trend + variance_shift | 10/10 | 0 | 0 | **%100** |
| Quadratic + Collective anomaly | det_trend + collective | 10/10 | 0 | 0 | **%100** |
| Quadratic + Mean Shift | det_trend + mean_shift | 10/10 | 0 | 0 | **%100** |
| Quadratic + Point Anomaly | det_trend + point_anomaly | 10/10 | 0 | 0 | **%100** |
| Quadratic + Variance Shift | det_trend + variance_shift | 10/10 | 0 | 0 | **%100** |
| Stochastic Trend + Collective Anomaly | stoch_trend + collective | 9/10 | 1 | 0 | %90 |
| Stochastic Trend + Mean Shift | stoch_trend + mean_shift | 10/10 | 0 | 0 | **%100** |
| Stochastic Trend + Point Anomaly | stoch_trend + point_anomaly | 9/10 | 1 | 0 | %90 |
| Stochastic Trend + Variance Shift | stoch_trend + variance_shift | 10/10 | 0 | 0 | **%100** |
| Volatility + Collective Anomaly | volatility + collective | 7/10 | 3 | 0 | %70 |
| Volatility + Mean Shift | volatility + mean_shift | 9/10 | 1 | 0 | %90 |
| Volatility + Point Anomaly | volatility + point_anomaly | 7/10 | 3 | 0 | %70 |
| Volatility + Variance Shift | volatility + variance_shift | 10/10 | 0 | 0 | **%100** |
| **TOPLAM** | | **282/290** | **8** | **0** | **%97.2** |

**%100 full match (21/29 kombinasyon):** Tüm Cubic, Damped, Exponential, Linear,
Quadratic base kombinasyonları + Stoch+Mean, Stoch+Variance, Vol+Variance.

**Kalan 8 partial:**
- Volatility + Collective (3 partial): volatility modeli yüksek spike'ları collective
  veya point olarak yorumlamakta zorluk çekiyor
- Volatility + Point (3 partial): benzer sebep — GARCH/ARCH volatilitesinin kendisi zaten
  spike benzeri değerler üretiyor, ek point anomali ile ayırt edilmesi güç
- Stoch + Collective (1 partial): random walk drift'i collective segment olarak algılanabilir
- Stoch + Point (1 partial): benzer karışıklık

---

## 10. Manuel Test — Tüm Leaf Klasörler

Her kaynak grubun **her leaf klasöründen 1 CSV** rastgele alınarak sınıflandırılmıştır.
Toplam: 440 leaf × 1 = **440 test örneği**.

Bu test, kombinasyon testinden farklı olarak:
- Tekli tip gruplarını (grup 1–4) kapsar
- Her leaf klasörden sadece 1 örnek alır (coverage testi)
- Kombinasyon testine göre daha zorlayıcıdır; bazı leaf klasörler eğitim setinde az temsil edilmiş olabilir

### 10.1 Genel Özet (v3)

| Metrik | Değer |
|---|---|
| Toplam test | 440 |
| Full match | 251 (%57.0) |
| Partial match | 114 (%25.9) |
| No match | 75 (%17.0) |

### 10.2 Grup Bazlı Özet

| # | Grup | Beklenen Etiket | Leaf | Full | Partial | None | Full% |
|---|---|---|---|---|---|---|---|
| 1 | stationary | `stationary` | 12 | 4 | 4 | 4 | %33 |
| 2 | deterministic_trend | `deterministic_trend` | 72 | 22 | 4 | 46 | %31 |
| 3 | stochastic_trend | `stochastic_trend` | 15 | 3 | 9 | 3 | %20 |
| 4 | volatility | `volatility` | 12 | 5 | 7 | 0 | %42 |
| 5 | collective_anomaly | `stationary + collective_anomaly` | 48 | 18 | 30 | 0 | %38 |
| 6 | contextual_anomaly | `stationary + contextual_anomaly` | 48 | 47 | 1 | 0 | **%98** |
| 7 | mean_shift | `stationary + mean_shift` | 48 | 32 | 12 | 4 | %67 |
| 8 | point_anomaly | `stationary + point_anomaly` | 48 | 23 | 19 | 6 | %48 |
| 9 | trend_shift | `stationary + trend_shift` | 48 | 34 | 11 | 3 | %71 |
| 10 | variance_shift | `stationary + variance_shift` | 48 | 23 | 16 | 9 | %48 |
| 11 | cubic+collective | `det_trend + collective` | 1 | 1 | 0 | 0 | %100 |
| 12 | cubic+mean_shift | `det_trend + mean_shift` | 2 | 2 | 0 | 0 | %100 |
| 13 | cubic+point_anomaly | `det_trend + point_anomaly` | 1 | 1 | 0 | 0 | %100 |
| 14 | cubic+variance_shift | `det_trend + variance_shift` | 1 | 1 | 0 | 0 | %100 |
| 15 | damped+collective | `det_trend + collective` | 1 | 1 | 0 | 0 | %100 |
| 16 | damped+mean_shift | `det_trend + mean_shift` | 2 | 2 | 0 | 0 | %100 |
| 17 | damped+point_anomaly | `det_trend + point_anomaly` | 1 | 1 | 0 | 0 | %100 |
| 18 | damped+variance_shift | `det_trend + variance_shift` | 1 | 1 | 0 | 0 | %100 |
| 19 | exp+collective | `det_trend + collective` | 1 | 1 | 0 | 0 | %100 |
| 20 | exp+mean_shift | `det_trend + mean_shift` | 2 | 2 | 0 | 0 | %100 |
| 21 | exp+point_anomaly | `det_trend + point_anomaly` | 1 | 1 | 0 | 0 | %100 |
| 22 | exp+variance_shift | `det_trend + variance_shift` | 1 | 1 | 0 | 0 | %100 |
| 23 | linear+collective | `det_trend + collective` | 1 | 1 | 0 | 0 | %100 |
| 24 | linear+mean_shift | `det_trend + mean_shift` | 2 | 2 | 0 | 0 | %100 |
| 25 | linear+point_anomaly | `det_trend + point_anomaly` | 1 | 1 | 0 | 0 | %100 |
| 26 | linear+trend_shift | `det_trend + trend_shift` | 3 | 3 | 0 | 0 | %100 |
| 27 | linear+variance_shift | `det_trend + variance_shift` | 1 | 1 | 0 | 0 | %100 |
| 28 | quad+collective | `det_trend + collective` | 1 | 1 | 0 | 0 | %100 |
| 29 | quad+mean_shift | `det_trend + mean_shift` | 2 | 2 | 0 | 0 | %100 |
| 30 | quad+point_anomaly | `det_trend + point_anomaly` | 2 | 2 | 0 | 0 | %100 |
| 31 | quad+variance_shift | `det_trend + variance_shift` | 1 | 1 | 0 | 0 | %100 |
| 32 | stoch+collective | `stoch_trend + collective` | 1 | 1 | 0 | 0 | %100 |
| 33 | stoch+mean_shift | `stoch_trend + mean_shift` | 1 | 1 | 0 | 0 | %100 |
| 34 | stoch+point_anomaly | `stoch_trend + point_anomaly` | 1 | 1 | 0 | 0 | %100 |
| 35 | stoch+variance_shift | `stoch_trend + variance_shift` | 5 | 4 | 1 | 0 | %80 |
| 36 | vol+collective | `volatility + collective` | 1 | 1 | 0 | 0 | %100 |
| 37 | vol+mean_shift | `volatility + mean_shift` | 1 | 1 | 0 | 0 | %100 |
| 38 | vol+point_anomaly | `volatility + point_anomaly` | 1 | 1 | 0 | 0 | %100 |
| 39 | vol+variance_shift | `volatility + variance_shift` | 1 | 1 | 0 | 0 | %100 |

### 10.3 Grup 1: stationary (4/12 FULL, %33)

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| ar_long | ar_28856.csv | `stationary + point_anomaly` | PARTIAL |
| ar_medium | ar_13281.csv | `stationary` | **FULL** |
| ar_short | ar_10735.csv | `volatility + collective + mean_shift + point_anomaly` | NONE |
| arma_long | arma_31868.csv | `stationary + point_anomaly` | PARTIAL |
| arma_medium | arma_18109.csv | `stationary` | **FULL** |
| arma_short | arma_1722.csv | `stochastic_trend + collective + point_anomaly` | NONE |
| ma_long | ma_16581.csv | `stationary` | **FULL** |
| ma_medium | ma_14112.csv | `stationary` | **FULL** |
| ma_short | ma_31717.csv | `volatility + collective + point_anomaly` | NONE |
| wn_long | wn_1302.csv | `stationary + point_anomaly` | PARTIAL |
| wn_medium | wn_29956.csv | `stationary + collective + contextual` | PARTIAL |
| wn_short | wn_31841.csv | `volatility + collective + point_anomaly` | NONE |

**Pattern:** `_short` seriler çok kısa olduğundan tsfresh özellikleri daha gürültülü; volatility veya stochastic_trend olarak karışıyor ve false positive anomaliler üretiliyor.

### 10.4 Grup 2: deterministic_trend (22/72 FULL, %31)

Özet: 72 leaften 22 FULL, 4 PARTIAL, 46 NONE.

**Düzgün çalışan tipler:**
- `damped_trend_*` (uzun ve orta): FULL (düzgün exponential sönüm eğimi belirgin)
- `exponential_trend_*` (uzun): genellikle FULL
- `cubic_trend_*` (uzun): genellikle FULL

**Sürekli hata veren tipler:**
- `linear_down/up_trend_*`: Trend eğimi stationary veya stochastic_trend ile karışıyor. det_trend modeli olasılığı 0.00'a düşüyor; stationary modeli 0.69–1.00 çıkıyor.
- `quadratic_trend_*`: Parabolik trend başlangıç ve bitişte düz görünüyor; argmax'ta stationary kazanıyor.
- `ar_*` prefix'li seriler: Yüksek AR gürültüsü trend bileşenini maskeliyor.
- `_short` seriler: Tüm alt tiplerinde zayıf performans.

### 10.5 Grup 3: stochastic_trend (3/15 FULL, %20)

| Alt Tip | Leaf | FULL | PARTIAL | NONE | Açıklama |
|---|---|---|---|---|---|
| ARI | long, medium, short | 1 | 1 | 1 | long FULL, medium NONE, short FULL |
| ARIMA | long, medium, short | 0 | 1 | 2 | long PARTIAL (variance_shift FP) |
| IMA | long, medium, short | 0 | 3 | 0 | tümü PARTIAL (trend_shift FP) |
| RW | long, medium, short | 0 | 3 | 0 | tümü PARTIAL (variance_shift FP) |
| RWD | long, medium, short | 2 | 1 | 0 | medium ve short FULL |

**Pattern:** Modelin stochastic_trend tespiti genellikle doğru (P≈1.00), fakat variance_shift
modeli de sık sık 0.53–0.98 arasında aktive oluyor. Random walk'ın varyans artışı ve
variance_shift anomalisinin varyans artışı tsfresh özellikleri açısından benzer görünüyor.

### 10.6 Grup 4: volatility (5/12 FULL, %42)

| Alt Tip | short | medium | long |
|---|---|---|---|
| APARCH | PARTIAL (collective FP) | FULL | FULL |
| ARCH | PARTIAL (variance_shift FP) | PARTIAL (variance_shift FP) | FULL |
| EGARCH | PARTIAL (collective FP) | PARTIAL (point FP) | FULL |
| GARCH | PARTIAL (collective+point FP) | PARTIAL (variance_shift FP) | FULL |

**Pattern:** `_long` seriler için FULL match %100; `_short` ve `_medium` seriler false positive
anomali üretiyor. Volatility'nin kendisi yüksek varyans ve "spike" benzeri değerler içerdiğinden
point_anomaly/collective_anomaly modelleri yanıltıcı şekilde aktive oluyor.

### 10.7 Grup 5: collective_anomaly (18/48 FULL, %38)

FULL match genellikle anomalinin pozisyonunun belirgin olduğu leaflerde (`middle`, `multiple`
içeren bazı durumlar). PARTIAL'ların çoğunda base_type doğru (stationary) ama model ya
collective'i kaçırıyor ya da ek anomali ekliyor (özellikle mean_shift ve point_anomaly FP).
NONE yok → base type tespiti başarılı.

### 10.8 Grup 6: contextual_anomaly (47/48 FULL, %98)

Sadece 1 PARTIAL: `MA_short_middle` klasöründe base_type `volatility` olarak yanlış.
contextual_anomaly modeli son derece başarılı (binary F1: 0.9981). Bu başarının sebebi,
contextual anomaly'nin diğer anomali türlerinden görsel ve istatistiksel olarak belirgin biçimde
farklı olması — tsfresh'in PARTIAL autocorrelation ve change quantile özellikleri bu yapıyı
güçlü şekilde yakalıyor.

### 10.9 Grup 7: mean_shift (32/48 FULL, %67)

Başarı yüksek `ar_*` ve `arma_*` prefix'li, `beginning/middle` pozisyonlu leaflerde.
4 NONE örnekte: base_type `volatility` olarak yanlış tahmin ediliyor; mean_shift yüksek
AR gürültüsüyle birleşince tsfresh varyans özellikleri volatility modelini aktive ediyor.

### 10.10 Grup 8: point_anomaly (23/48 FULL, %48)

6 NONE: 5'inde base_type `volatility` yanlış. Tekil bir spike içeren AR serisi, ARCH/GARCH
benzeri yoğunlaşma yarattığında volatility modeli 0.8+ olasılıkla aktive olabiliyor.
Kalan 19 PARTIAL'da ise çoğunlukla base_type doğru ama point_anomaly missed veya ek anomali
var.

### 10.11 Grup 9: trend_shift (34/48 FULL, %71)

Trend shift tipik olarak güçlü sinyal veriyor. 3 NONE'da da pattern aynı: `ar_*_short`
veya `white_noise_*_multiple` klasörlerinde volatility modeli kazanıyor. 11 PARTIAL'da
çoğunlukla mean_shift false positive eklenmiş.

### 10.12 Grup 10: variance_shift (23/48 FULL, %48)

9 NONE: tümünde base_type `volatility` yanlış. Variance shift (ani varyans artışı) ile
GARCH/ARCH sürecini ayırt etmek istatistiksel açıdan en zor kombinasyon. tsfresh'in
varyans bazlı özellikleri iki durumda da benzer değerler üretiyor.

### 10.13 Gruplar 11–39: Kombinasyon Klasörleri (141/157 FULL, %90)

| Özet |
|---|
| Tüm Cubic base kombinasyonları: 5/5 leaf → %100 FULL |
| Tüm Damped base kombinasyonları: 5/5 leaf → %100 FULL |
| Tüm Exponential base kombinasyonları: 5/5 leaf → %100 FULL |
| Tüm Linear base kombinasyonları: 7/7 leaf → %100 FULL |
| Tüm Quadratic base kombinasyonları: 6/6 leaf → %100 FULL |
| Stochastic kombinasyonları: 7/8 leaf → %88 (stoch+variance_shift: 4/5, PARTIAL 1) |
| Volatility kombinasyonları: 4/4 leaf → %100 FULL |

---

## 11. Hata Analizi

### 11.1 Birincil Hata Kaynakları

**Deterministic trend karışıklığı (Grup 2, %69 NONE rate):**
Lineer ve quadratic trend formlarında, özellikle kısa serilerle ve AR/ARMA gürültüsüyle
birleşince, tsfresh'in doğrusal regresyon slope özellikleri istatistiksel olarak önemsiz
çıkıyor. `det_trend` modeli P≈0.00 veriyor; argmax stationary ya da stochastic_trend'i seçiyor.
Örnek olasılıklar: `ar_linear_down_trend_312.csv` → det_trend: 0.00, stationary: 1.00.

**Volatility — anomali karışıklığı (Grup 4, 8, 10):**
GARCH/ARCH sürecinin kendisi zaten spike ve yüksek varyans içeriyor. Bu özellikler
`point_anomaly`, `collective_anomaly`, `variance_shift` modellerini yanıltıcı biçimde
aktive ediyor. Örnek: `garch_684.csv` → volatility: 1.00, collective: 0.89, point: 0.71.
Çözüm önerisi: Volatility için anomali eşiğini (THRESHOLD=0.5) 0.7–0.8'e çıkarmak.

**Stochastic trend — variance shift karışıklığı (Grup 3):**
Random walk'ın kümülatif varyans artışı ve `variance_shift` anomalisinin varyans sıçraması
tsfresh açısından benzer sinyal üretiyor. `variance_shift` modeli stochastic seriler için
sık sık 0.5–0.98 arasında değer döndürüyor. Örnek: `random_walk_354.csv` → stoch: 1.00,
var_shift: 0.98 → PARTIAL.

**Kısa seri sorunu:**
`_short` prefix'li leaflerde (tüm gruplarda) hata oranı belirgin biçimde yüksek.
Kısa seriler (50–200 zaman adımı) tsfresh'in özelliklerini daha gürültülü üretiyor;
autocorrelation bazlı özellikler yetersiz lag ile hesaplanıyor.

### 11.2 Kombinasyon Testi vs Manuel Test Farkı

| Boyut | Kombinasyon Testi | Manuel Test |
|---|---|---|
| Kapsam | 29 kombinasyon klasörü | 39 grup, 440 leaf |
| Tekli tip testi | Hayır | Evet (grup 1–4) |
| Örnekleme | Klasör başına 10 rastgele CSV | Leaf başına 1 CSV |
| Eğitim dağılımına yakınlık | Yüksek | Düşük (edge case'ler dahil) |
| v3 Full match | **%97.2** | %57.0 |

Kombinasyon testi "öğrenilmiş kombinasyonlar üzerindeki performans"ı ölçürken,
manuel test modelin **genelleme kapasitesini** ve **kapsam genişliğini** ölçüyor.
%57.0 düşük görünse de grupların yarısından fazlası (kombinasyon grupları, grup 6)
%80–100 arasında performans gösteriyor; düşük ortalamayı esas aşağı çeken grup 2
(72 leaf, %31 FULL) ve grup 3 (15 leaf, %20 FULL).

---

## 12. Proje Yapısı ve Kurulum

### Dosya Yapısı

```
ensemble-alldata/
├── config.py           # N, dizin yolları, 39 SOURCE_GROUPS, MODEL_POSITIVE_GROUPS
├── processor.py        # CSV okuma, 3-aşamalı örnekleme, tsfresh extraction (.npy cache)
├── trainer.py          # LightGBM/XGBoost/MLP eğitimi, val F1 seçimi, model kaydetme
├── evaluator.py        # Kombinasyon testi, batch inference, decode_prediction
├── main.py             # Orkestrasyon: --force, --train, --eval, --model
├── manueltest.py       # Her leaf klasörden 1 örnek alıp ensemble ile sınıflandırır
├── plan.md             # Strateji ve örnekleme planı (geliştirme notları)
├── tree.md             # Kaynak grup ağaç yapısı
├── results/
│   ├── results.md              # Tam sonuç raporu
│   ├── manueltest.md           # Manuel test detayları (440 leaf, 1 örnek/leaf)
│   ├── training_results.json   # [gitignore] Binary model metrikleri
│   └── combination_eval.json   # [gitignore] Kombinasyon testi detayları
├── processed_data/     # [gitignore] tsfresh feature cache (.npy)
└── trained_models/     # [gitignore] Eğitilmiş modeller (.pkl)
```

### Gereksinimler

```bash
pip install tsfresh lightgbm xgboost scikit-learn pandas numpy joblib tqdm
```

### Kullanım

```bash
# Feature extraction + eğitim + kombinasyon testi (tam pipeline)
python main.py

# Cache'i yok sayarak her şeyi yeniden işle
python main.py --force

# Sadece belirli bir modeli yeniden eğit
python main.py --model deterministic_trend

# Sadece eğitim (feature cache hazır varsayılır)
python main.py --train

# Sadece kombinasyon testi (modeller hazır varsayılır)
python main.py --eval

# Manuel test (tüm leaf klasörlerden 1 örnek)
python manueltest.py
```

### Konfigürasyon Parametreleri (config.py)

| Parametre | Değer | Açıklama |
|---|---|---|
| `N` | `1320` | Her model için pozitif ve negatif örnek sayısı |
| `TEST_SIZE` | `0.20` | Test seti oranı |
| `VALIDATION_SIZE` | `0.10` | Validasyon seti oranı |
| `THRESHOLD` | `0.5` | Anomali modellerinde pozitif eşiği |
| `MIN_SERIES_LENGTH` | `50` | Minimum kabul edilebilir seri uzunluğu |
| `RANDOM_STATE` | `42` | Tüm rastgele işlemler için seed |

---

## Konfigürasyon Notu

Tüm dizin yolları `config.py` içindeki `GD` ve `COMB` değişkenlerine bağlı.
Veri farklı bir konumdaysa `GD = Path(...)` satırını güncellemek yeterli.

Model çıktıları (`trained_models/`) ve feature cache (`processed_data/`) `.gitignore`'a alınmıştır;
bu dizinler yeniden üretmek için `python main.py --force` çalıştırılmalıdır.
