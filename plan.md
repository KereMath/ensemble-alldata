# ensemble-alldata — Plan

## Motivasyon

Eski tsfresh ensemble her binary modeli sadece tekli anomali datalarıyla eğitti.
Kombinasyon sinyali geldiğinde baskın pattern (trend gibi) diğer anomaliyi gölgeledi.
Sonuç: full match %0 — ikinci anomaliyi hiç bulamadı.

Çözüm: Her binary modelin pozitif sınıfına, o anomaliyi/base tipi içeren tüm
kombinasyon klasörlerini dahil etmek. Model anomaliyi farklı gürültü ortamlarında
da tanımayı öğrenir. Inference'ta argmax değil threshold (>=0.5) — multi-label çıktı.

---

## Genel Mimari

- 10 binary classifier (4 base tip + 6 anomali tipi)
- Her model: LightGBM + XGBoost + MLP — en iyi val F1 seçilir
- Feature extraction: tsfresh EfficientFCParameters (777 feature)
- Split: %70 train / %10 val / %20 test (stratified)
- Inference: her classifier bagimsiz olasilik uretir, >=0.5 olanlar pozitif

---

## Örnekleme Stratejisi

### Tanımlar

Tüm veri kaynaklarının "kaynak grubu" olarak düzenlenmesi:
Toplam 39 kaynak grubu var (alldata-models'in 39 kategorisiyle birebir örtüşür):

**10 tekli kaynak grubu:**
1. stationary (GD/stationary/)
2. deterministic_trend (GD/deterministic_trend/)
3. stochastic_trend (GD/Stochastic Trend/)
4. volatility (GD/Volatility/)
5. collective_anomaly (GD/collective_anomaly/)
6. contextual_anomaly (GD/contextual_anomaly/)
7. mean_shift (GD/mean_shift/)
8. point_anomaly (GD/point_anomaly/)
9. trend_shift (GD/trend_shift/)
10. variance_shift (GD/variance_shift/)

**29 kombinasyon kaynak grubu:**
11. cubic + collective_anomaly
12. cubic + mean_shift
13. cubic + point_anomaly
14. cubic + variance_shift
15. damped + collective_anomaly
16. damped + mean_shift
17. damped + point_anomaly
18. damped + variance_shift
19. exponential + collective_anomaly
20. exponential + mean_shift
21. exponential + point_anomaly
22. exponential + variance_shift
23. linear + collective_anomaly
24. linear + mean_shift
25. linear + point_anomaly
26. linear + trend_shift
27. linear + variance_shift
28. quadratic + collective_anomaly
29. quadratic + mean_shift
30. quadratic + point_anomaly
31. quadratic + variance_shift
32. stochastic + collective_anomaly
33. stochastic + mean_shift
34. stochastic + point_anomaly
35. stochastic + variance_shift
36. volatility + collective_anomaly
37. volatility + mean_shift
38. volatility + point_anomaly
39. volatility + variance_shift

### Kural

- **N_pos = N_neg = 440** örnek (her model için sabit)
- Pozitif örnekler: `floor(440 / pos_grup_sayisi)` örnek per pozitif kaynak grubu
- Negatif örnekler: `floor(440 / neg_grup_sayisi)` örnek per negatif kaynak grubu
- Grup içi örnekleme: grubun tüm leaf klasörlerinden random (leaf yapısı gözetilmez)
- Kalan örnekler (440 % grup_sayisi) rastgele gruplara dağıtılır

### Neden N=440?
440 pek çok grup sayısına tam bölünür:
- 440 / 22 = **20** (deterministic_trend pozitif grubu)
- 440 /  8 = **55** (8 pozitif gruba sahip modeller)
- 440 /  5 = **88** (stochastic/volatility pozitif grubu)
- 440 /  2 = **220** (trend_shift pozitif grubu)
- 440 /  1 = **440** (contextual_anomaly pozitif grubu)
- 440 /  7 ≈ 63 (stationary: 6 grup 63, 1 grup 62)

---

## 10 Binary Model — Pozitif ve Negatif Kaynak Grupları

### 1. stationary
- **Pozitif (7 grup):** #1 stationary, #5 collective, #6 contextual, #7 mean_shift, #8 point_anomaly, #9 trend_shift, #10 variance_shift
- **Negatif (32 grup):** #2 det_trend, #3 stoch, #4 vol + tüm 29 kombinasyon grubu
- Per pozitif grup: ~63 örnek | Per negatif grup: 440/32 = ~14 örnek

### 2. deterministic_trend
- **Pozitif (22 grup):** #2 det_trend + #11-31 (tüm det_trend tabanlı kombinasyonlar: cubic×4, damped×4, exp×4, linear×5, quad×4 = 21 kombo)
- **Negatif (17 grup):** #1 stat, #3 stoch, #4 vol, #5 collective, #6 contextual, #7 mean, #8 point, #9 trend, #10 variance + #32-39 (stoch ve vol tabanlı kombinasyonlar = 8 kombo)
- Per pozitif grup: 440/22 = **20 tam** | Per negatif grup: 440/17 = ~26 örnek

### 3. stochastic_trend
- **Pozitif (5 grup):** #3 stoch + #32 stoch+coll, #33 stoch+mean, #34 stoch+point, #35 stoch+variance
- **Negatif (34 grup):** geri kalan 34 kaynak grubu
- Per pozitif grup: 440/5 = **88 tam** | Per negatif grup: 440/34 = ~13 örnek

### 4. volatility
- **Pozitif (5 grup):** #4 vol + #36 vol+coll, #37 vol+mean, #38 vol+point, #39 vol+variance
- **Negatif (34 grup):** geri kalan 34 kaynak grubu
- Per pozitif grup: 440/5 = **88 tam** | Per negatif grup: 440/34 = ~13 örnek

### 5. collective_anomaly
- **Pozitif (8 grup):** #5 collective + #11 cubic+coll, #15 damped+coll, #19 exp+coll, #23 linear+coll, #28 quad+coll, #32 stoch+coll, #36 vol+coll
- **Negatif (31 grup):** geri kalan 31 kaynak grubu
- Per pozitif grup: 440/8 = **55 tam** | Per negatif grup: 440/31 = ~14 örnek

### 6. contextual_anomaly
- **Pozitif (1 grup):** #6 contextual
- **Negatif (38 grup):** geri kalan 38 kaynak grubu
- Per pozitif grup: 440/1 = **440 tam** | Per negatif grup: 440/38 = ~12 örnek

### 7. mean_shift
- **Pozitif (8 grup):** #7 mean_shift + #12 cubic+mean, #16 damped+mean, #20 exp+mean, #24 linear+mean, #29 quad+mean, #33 stoch+mean, #37 vol+mean
- **Negatif (31 grup):** geri kalan 31 kaynak grubu
- Per pozitif grup: 440/8 = **55 tam** | Per negatif grup: 440/31 = ~14 örnek

### 8. point_anomaly
- **Pozitif (8 grup):** #8 point + #13 cubic+point, #17 damped+point, #21 exp+point, #25 linear+point, #30 quad+point, #34 stoch+point, #38 vol+point
- **Negatif (31 grup):** geri kalan 31 kaynak grubu
- Per pozitif grup: 440/8 = **55 tam** | Per negatif grup: 440/31 = ~14 örnek

### 9. trend_shift
- **Pozitif (2 grup):** #9 trend_shift + #26 linear+trend
- **Negatif (37 grup):** geri kalan 37 kaynak grubu
- Per pozitif grup: 440/2 = **220 tam** | Per negatif grup: 440/37 = ~12 örnek

### 10. variance_shift
- **Pozitif (8 grup):** #10 variance + #14 cubic+var, #18 damped+var, #22 exp+var, #27 linear+var, #31 quad+var, #35 stoch+var, #39 vol+var
- **Negatif (31 grup):** geri kalan 31 kaynak grubu
- Per pozitif grup: 440/8 = **55 tam** | Per negatif grup: 440/31 = ~14 örnek

---

## Özet Tablo

| Model | Pos Grup | Neg Grup | Pos/Grup | Neg/Grup | Toplam |
|---|---|---|---|---|---|
| stationary | 7 | 32 | ~63 | ~14 | 880 |
| deterministic_trend | 22 | 17 | 20 | ~26 | 880 |
| stochastic_trend | 5 | 34 | 88 | ~13 | 880 |
| volatility | 5 | 34 | 88 | ~13 | 880 |
| collective_anomaly | 8 | 31 | 55 | ~14 | 880 |
| contextual_anomaly | 1 | 38 | 440 | ~12 | 880 |
| mean_shift | 8 | 31 | 55 | ~14 | 880 |
| point_anomaly | 8 | 31 | 55 | ~14 | 880 |
| trend_shift | 2 | 37 | 220 | ~12 | 880 |
| variance_shift | 8 | 31 | 55 | ~14 | 880 |

Her model: **440 pozitif + 440 negatif = 880 örnek** (train+val+test birlikte)

---

## Kaynak Grup → Klasör Eşlemesi (config.py için)

```
GD   = C:\Users\user\Desktop\Generated Data
COMB = C:\Users\user\Desktop\Generated Data\Combinations

#  Grup No  |  Klasör
#  ---------|--------
#  1        |  GD\stationary\
#  2        |  GD\deterministic_trend\
#  3        |  GD\Stochastic Trend\
#  4        |  GD\Volatility\
#  5        |  GD\collective_anomaly\
#  6        |  GD\contextual_anomaly\
#  7        |  GD\mean_shift\
#  8        |  GD\point_anomaly\
#  9        |  GD\trend_shift\
# 10        |  GD\variance_shift\
# 11        |  COMB\Cubic Base\Cubic Base\cubic_collective_anomaly\
# 12        |  COMB\Cubic Base\Cubic Base\Cubic + Mean Shift\
# 13        |  COMB\Cubic Base\Cubic Base\Cubic + Point Anomaly\
# 14        |  COMB\Cubic Base\Cubic Base\Cubic + Variance Shift\
# 15        |  COMB\Damped Base\Damped Base\Damped + Collective Anomaly\
# 16        |  COMB\Damped Base\Damped Base\Damped + Mean Shift\
# 17        |  COMB\Damped Base\Damped Base\Damped + Point Anomaly\
# 18        |  COMB\Damped Base\Damped Base\Damped + Variance Shift\
# 19        |  COMB\Exponential Base\Exponential Base\exponential_collective_anomaly\
# 20        |  COMB\Exponential Base\Exponential Base\Exponential + Mean Shift\
# 21        |  COMB\Exponential Base\Exponential Base\exponential_point_anomaly\
# 22        |  COMB\Exponential Base\Exponential Base\exponential_variance_shift\
# 23        |  COMB\Linear Base\Linear Base\Linear + Collective Anomaly\
# 24        |  COMB\Linear Base\Linear Base\Linear + Mean Shift\
# 25        |  COMB\Linear Base\Linear Base\Linear + Point Anomaly\
# 26        |  COMB\Linear Base\Linear Base\Linear + Trend Shift\
# 27        |  COMB\Linear Base\Linear Base\Linear + Variance Shift\
# 28        |  COMB\Quadratic Base\Quadratic Base\Quadratic + Collective anomaly\
# 29        |  COMB\Quadratic Base\Quadratic Base\Quadratic + Mean Shift\
# 30        |  COMB\Quadratic Base\Quadratic Base\Quadratic + Point Anomaly\
# 31        |  COMB\Quadratic Base\Quadratic Base\Quadratic + Variance Shift\
# 32        |  COMB\Stochastic Trend + Collective Anomaly\
# 33        |  COMB\Stochastic Trend + Mean Shift\
# 34        |  COMB\Stochastic Trend + Point Anomaly\
# 35        |  COMB\Stochastic Trend + Variance Shift\Stochastic Trend + Variance Shift\
# 36        |  COMB\Volatility + Collective Anomaly\
# 37        |  COMB\Volatility + Mean Shift\
# 38        |  COMB\Volatility + Point Anomaly\
# 39        |  COMB\Volatility + Variance Shift\
```

---

## Feature Extraction

- tsfresh EfficientFCParameters — 777 feature
- Her binary model için ayri feature matrix
- processed_data/<model_adi>/ altina cache'lenir
- .gitignore ile repoya pushlanmaz

---

## Model Egitimi

Her binary classifier icin:
1. LightGBM (300 estimator, class_weight=balanced)
2. XGBoost (300 estimator, scale_pos_weight ile dengeleme)
3. MLP (hidden: 256-128-64, early stopping)

En iyi validation F1 skoru olan model secilir, trained_models/ altina kaydedilir.

---

## Inference

Giris: tek bir zaman serisi CSV

Her 10 binary model calisir — P(positive) uretir

Cikti:
  base_type = argmax(stationary, det_trend, stoch_trend, volatility)   [tek secim]
  anomalies = [tip for tip if P(tip) >= 0.5]                           [sifir veya fazla]

---

## Klasor Yapisi

```
ensemble-alldata/
  plan.md
  config.py       <- 39 kaynak grubu tanimi, model-grup eslesmesi, N=440
  processor.py    <- CSV yukleme, tsfresh feature extraction, cache
  trainer.py      <- her model icin binary egitim dongusu
  main.py         <- orchestrator: extract -> train -> evaluate
  evaluator.py    <- combination test: full/partial/no match metrikleri
  results/
  processed_data/  <- .gitignore
  trained_models/  <- .gitignore
```
