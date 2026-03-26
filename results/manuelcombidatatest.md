# Manuel Combination-Only Data Test

Sadece kombinasyon gruplarından (grup 11–39) her leaf klasörden
en fazla 10 CSV alınarak ensemble ile sınıflandırılmıştır.
Tekli tip gruplar (1–10) bu testte yer almaz.

## Özet

| Metrik | Değer |
|---|---|
| Toplam test | 410 |
| Full match | 393 (95.9%) |
| Partial match | 17 (4.1%) |
| No match | 0 (0.0%) |

## Grup Bazlı Özet

| # | Grup | Beklenen | Örnek | Full | Partial | None | Full% |
|---|---|---|---|---|---|---|---|
| 11 | cubic+collective | deterministic_trend + collective_anomaly | 10 | 10 | 0 | 0 | %100 |
| 12 | cubic+mean_shift | deterministic_trend + mean_shift | 20 | 18 | 2 | 0 | %90 |
| 13 | cubic+point_anomaly | deterministic_trend + point_anomaly | 10 | 10 | 0 | 0 | %100 |
| 14 | cubic+variance_shift | deterministic_trend + variance_shift | 10 | 10 | 0 | 0 | %100 |
| 15 | damped+collective | deterministic_trend + collective_anomaly | 10 | 10 | 0 | 0 | %100 |
| 16 | damped+mean_shift | deterministic_trend + mean_shift | 20 | 18 | 2 | 0 | %90 |
| 17 | damped+point_anomaly | deterministic_trend + point_anomaly | 10 | 10 | 0 | 0 | %100 |
| 18 | damped+variance_shift | deterministic_trend + variance_shift | 10 | 9 | 1 | 0 | %90 |
| 19 | exp+collective | deterministic_trend + collective_anomaly | 10 | 10 | 0 | 0 | %100 |
| 20 | exp+mean_shift | deterministic_trend + mean_shift | 20 | 20 | 0 | 0 | %100 |
| 21 | exp+point_anomaly | deterministic_trend + point_anomaly | 10 | 10 | 0 | 0 | %100 |
| 22 | exp+variance_shift | deterministic_trend + variance_shift | 10 | 10 | 0 | 0 | %100 |
| 23 | linear+collective | deterministic_trend + collective_anomaly | 10 | 10 | 0 | 0 | %100 |
| 24 | linear+mean_shift | deterministic_trend + mean_shift | 20 | 20 | 0 | 0 | %100 |
| 25 | linear+point_anomaly | deterministic_trend + point_anomaly | 10 | 10 | 0 | 0 | %100 |
| 26 | linear+trend_shift | deterministic_trend + trend_shift | 30 | 30 | 0 | 0 | %100 |
| 27 | linear+variance_shift | deterministic_trend + variance_shift | 10 | 10 | 0 | 0 | %100 |
| 28 | quad+collective | deterministic_trend + collective_anomaly | 10 | 10 | 0 | 0 | %100 |
| 29 | quad+mean_shift | deterministic_trend + mean_shift | 20 | 20 | 0 | 0 | %100 |
| 30 | quad+point_anomaly | deterministic_trend + point_anomaly | 20 | 20 | 0 | 0 | %100 |
| 31 | quad+variance_shift | deterministic_trend + variance_shift | 10 | 9 | 1 | 0 | %90 |
| 32 | stoch+collective | stochastic_trend + collective_anomaly | 10 | 10 | 0 | 0 | %100 |
| 33 | stoch+mean_shift | stochastic_trend + mean_shift | 10 | 6 | 4 | 0 | %60 |
| 34 | stoch+point_anomaly | stochastic_trend + point_anomaly | 10 | 9 | 1 | 0 | %90 |
| 35 | stoch+variance_shift | stochastic_trend + variance_shift | 50 | 48 | 2 | 0 | %96 |
| 36 | vol+collective | volatility + collective_anomaly | 10 | 9 | 1 | 0 | %90 |
| 37 | vol+mean_shift | volatility + mean_shift | 10 | 10 | 0 | 0 | %100 |
| 38 | vol+point_anomaly | volatility + point_anomaly | 10 | 8 | 2 | 0 | %80 |
| 39 | vol+variance_shift | volatility + variance_shift | 10 | 9 | 1 | 0 | %90 |

---

## Grup 11: cubic+collective
**Beklenen:** `deterministic_trend + collective_anomaly`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `cubic_collective_ma_154.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `cubic_collective_arma_114.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `cubic_collective_arma_025.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `cubic_collective_white_noise_009.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `cubic_collective_ar_031.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `cubic_collective_ar_000.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `cubic_collective_arma_228.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `cubic_collective_arma_142.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `cubic_collective_white_noise_004.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `cubic_collective_arma_104.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
---

## Grup 12: cubic+mean_shift
**Beklenen:** `deterministic_trend + mean_shift`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `cubic_meanshift1_ma_187.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `cubic_meanshift1_white_noise_003.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `cubic_meanshift1_white_noise_156.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `cubic_meanshift1_ma_053.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `cubic_meanshift1_arma_086(1).csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `cubic_meanshift1_ma_099.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `cubic_meanshift1_ar_177.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `cubic_meanshift1_arma_032.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `cubic_meanshift1_arma_030.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `cubic_meanshift1_arma_091.csv` | `deterministic_trend + variance_shift` | ~ PARTIAL |
| `data` | `cubic_meanshift2_arma_223.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `cubic_meanshift2_arma_238.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `cubic_meanshift2_ma_017.csv` | `deterministic_trend + variance_shift` | ~ PARTIAL |
| `data` | `cubic_meanshift2_ma_116.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `cubic_meanshift2_arma_027.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `cubic_meanshift2_ma_074.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `cubic_meanshift2_arma_203.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `cubic_meanshift2_ma_233.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `cubic_meanshift2_ma_165.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `cubic_meanshift2_ma_218.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
---

## Grup 13: cubic+point_anomaly
**Beklenen:** `deterministic_trend + point_anomaly`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `cubic_point_ma_058.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `cubic_point_ar_179.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `cubic_point_arma_225.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `cubic_point_ar_209.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `cubic_point_ma_103.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `cubic_point_ar_034.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `cubic_point_white_noise_078.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `cubic_point_white_noise_140.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `cubic_point_arma_006.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `cubic_point_white_noise_027.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
---

## Grup 14: cubic+variance_shift
**Beklenen:** `deterministic_trend + variance_shift`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `cubic_varshift_white_noise_075.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `cubic_varshift_arma_163.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `cubic_varshift_ma_214.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `cubic_varshift_ar_182.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `cubic_varshift_ar_098.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `cubic_varshift_ar_034.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `cubic_varshift_arma_159.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `cubic_varshift_arma_220.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `cubic_varshift_white_noise_230.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `cubic_varshift_white_noise_031.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
---

## Grup 15: damped+collective
**Beklenen:** `deterministic_trend + collective_anomaly`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `damped_collective_ar_094.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `damped_collective_arma_104.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `damped_collective_arma_094.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `damped_collective_ar_139.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `damped_collective_arma_099.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `damped_collective_ar_117.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `damped_collective_white_noise_117.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `damped_collective_ar_102.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `damped_collective_ma_118.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `damped_collective_ar_020.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
---

## Grup 16: damped+mean_shift
**Beklenen:** `deterministic_trend + mean_shift`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `damped_meanshift1_white_noise_076.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `damped_meanshift1_arma_044.csv` | `deterministic_trend + variance_shift` | ~ PARTIAL |
| `data` | `damped_meanshift1_ma_247.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `damped_meanshift1_ar_220.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `damped_meanshift1_ma_049.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `damped_meanshift1_arma_127.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `damped_meanshift1_white_noise_246.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `damped_meanshift1_white_noise_194.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `damped_meanshift1_ar_137.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `damped_meanshift1_arma_080.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `damped_meanshift2_ma_065.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `damped_meanshift2_ar_050.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `damped_meanshift2_white_noise_099.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `damped_meanshift2_ma_143.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `damped_meanshift2_ma_133.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `damped_meanshift2_white_noise_156.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `damped_meanshift2_white_noise_132.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `damped_meanshift2_ar_120.csv` | `deterministic_trend + variance_shift` | ~ PARTIAL |
| `data` | `damped_meanshift2_ma_091.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `damped_meanshift2_arma_196.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
---

## Grup 17: damped+point_anomaly
**Beklenen:** `deterministic_trend + point_anomaly`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `damped_point_ma_221.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `damped_point_arma_071.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `damped_point_arma_046.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `damped_point_ma_177.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `damped_point_arma_233.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `damped_point_white_noise_041.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `damped_point_ar_046.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `damped_point_arma_081.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `damped_point_white_noise_125.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `damped_point_arma_238.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
---

## Grup 18: damped+variance_shift
**Beklenen:** `deterministic_trend + variance_shift`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `damped_varshift_white_noise_137.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `damped_varshift_arma_103.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `damped_varshift_ar_139.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `damped_varshift_ar_034.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `damped_varshift_ar_214.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `damped_varshift_ma_150.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `damped_varshift_white_noise_104.csv` | `deterministic_trend + mean_shift` | ~ PARTIAL |
| `data` | `damped_varshift_ar_123.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `damped_varshift_arma_166.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `damped_varshift_ar_129.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
---

## Grup 19: exp+collective
**Beklenen:** `deterministic_trend + collective_anomaly`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `exp_collective_ar_113.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `exp_collective_arma_214.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `exp_collective_ma_186.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `exp_collective_ar_023.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `exp_collective_ma_218.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `exp_collective_white_noise_209.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `exp_collective_ma_199.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `exp_collective_ma_163.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `exp_collective_arma_073.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `exp_collective_ma_123.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
---

## Grup 20: exp+mean_shift
**Beklenen:** `deterministic_trend + mean_shift`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `exp_meanshift1_ma_150.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `exp_meanshift1_arma_175.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `exp_meanshift1_ma_046.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `exp_meanshift1_ma_246.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `exp_meanshift1_ar_000.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `exp_meanshift1_arma_167.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `exp_meanshift1_ar_223.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `exp_meanshift1_ar_138.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `exp_meanshift1_ar_026.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `exp_meanshift1_white_noise_197.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `exp_meanshift2_ma_155.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `exp_meanshift2_ma_204.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `exp_meanshift2_ma_070.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `exp_meanshift2_arma_224.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `exp_meanshift2_ma_201.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `exp_meanshift2_ar_082.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `exp_meanshift2_white_noise_113.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `exp_meanshift2_white_noise_036.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `exp_meanshift2_white_noise_044.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `exp_meanshift2_arma_057.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
---

## Grup 21: exp+point_anomaly
**Beklenen:** `deterministic_trend + point_anomaly`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `exp_point_arma_234.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `exp_point_white_noise_091.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `exp_point_arma_032.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `exp_point_white_noise_074.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `exp_point_ar_073.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `exp_point_ar_160.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `exp_point_ar_024.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `exp_point_arma_067.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `exp_point_arma_216.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `exp_point_white_noise_185.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
---

## Grup 22: exp+variance_shift
**Beklenen:** `deterministic_trend + variance_shift`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `exp_varshift_white_noise_215.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `exp_varshift_ma_080.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `exp_varshift_white_noise_147.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `exp_varshift_ma_235.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `exp_varshift_ar_072.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `exp_varshift_arma_217.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `exp_varshift_ma_171.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `exp_varshift_ma_011.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `exp_varshift_ar_155.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `exp_varshift_white_noise_155.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
---

## Grup 23: linear+collective
**Beklenen:** `deterministic_trend + collective_anomaly`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `linear_collective_white_noise_up_122.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `linear_collective_ma_up_066.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `linear_collective_ar_up_189.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `linear_collective_arma_up_042.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `linear_collective_ar_down_042.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `linear_collective_arma_up_035.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `linear_collective_ar_down_005.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `linear_collective_white_noise_down_025.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `linear_collective_ma_down_149.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `linear_collective_ma_down_103.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
---

## Grup 24: linear+mean_shift
**Beklenen:** `deterministic_trend + mean_shift`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `linear_meanshift1_ar_down_019.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `linear_meanshift1_white_noise_down_014.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `linear_meanshift1_ma_down_098.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `linear_meanshift1_ar_up_063.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `linear_meanshift1_white_noise_up_044.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `linear_meanshift1_ma_down_097.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `linear_meanshift1_ar_up_033.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `linear_meanshift1_ar_down_120.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `linear_meanshift1_arma_up_099.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `linear_meanshift1_arma_up_016.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `linear_meanshift2_ma_down_021.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `linear_meanshift2_ma_down_005.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `linear_meanshift2_arma_down_093.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `linear_meanshift2_white_noise_down_023.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `linear_meanshift2_arma_down_048.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `linear_meanshift2_white_noise_up_006.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `linear_meanshift2_arma_down_112.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `linear_meanshift2_arma_up_031.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `linear_meanshift2_ma_up_017.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `linear_meanshift2_arma_up_038.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
---

## Grup 25: linear+point_anomaly
**Beklenen:** `deterministic_trend + point_anomaly`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `linear_point_white_noise_down_122.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `linear_point_ma_up_143.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `linear_point_ar_up_114.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `linear_point_ma_down_221.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `linear_point_arma_down_130.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `linear_point_ar_up_038.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `linear_point_ar_up_031.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `linear_point_ma_down_220.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `linear_point_ar_up_208.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `linear_point_ma_down_083.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
---

## Grup 26: linear+trend_shift
**Beklenen:** `deterministic_trend + trend_shift`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `trendshift_direction_and_magnitude_change_ar_down_007.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_and_magnitude_change_white_noise_up_119.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_and_magnitude_change_ma_down_066.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_and_magnitude_change_white_noise_up_006.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_and_magnitude_change_white_noise_up_090.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_and_magnitude_change_arma_down_011.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_and_magnitude_change_ma_up_071.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_and_magnitude_change_ma_up_113.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_and_magnitude_change_arma_down_117.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_and_magnitude_change_ma_up_073.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_change_white_noise_up_031.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_change_ma_down_049.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_change_white_noise_down_018.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_change_ar_down_023.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_change_white_noise_down_037.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_change_ma_up_031.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_change_ar_down_098.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_change_arma_down_114.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_change_ar_down_050.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_change_ar_up_070.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_magnitude_change_arma_up_036.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_magnitude_change_ar_up_089.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_magnitude_change_arma_down_003.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_magnitude_change_white_noise_up_101.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_magnitude_change_ma_up_114.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_magnitude_change_white_noise_up_021.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_magnitude_change_ma_up_111.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_magnitude_change_ar_down_019.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_magnitude_change_white_noise_up_120.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_magnitude_change_ma_down_012.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
---

## Grup 27: linear+variance_shift
**Beklenen:** `deterministic_trend + variance_shift`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `linear_varshift1_white_noise_down_029.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `linear_varshift1_arma_up_057.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `linear_varshift1_ma_down_018.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `linear_varshift1_white_noise_up_058.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `linear_varshift1_arma_down_108.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `linear_varshift1_white_noise_up_015.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `linear_varshift1_ma_up_014.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `linear_varshift1_ar_down_055.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `linear_varshift1_white_noise_down_110.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `linear_varshift1_ma_up_028.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
---

## Grup 28: quad+collective
**Beklenen:** `deterministic_trend + collective_anomaly`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `quadratic_collective_ma_019.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `quadratic_collective_ma_123.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `quadratic_collective_arma_203.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `quadratic_collective_arma_156.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `quadratic_collective_ar_132.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `quadratic_collective_white_noise_030.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `quadratic_collective_arma_165.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `quadratic_collective_ma_052.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `quadratic_collective_white_noise_226.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `quadratic_collective_white_noise_047.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
---

## Grup 29: quad+mean_shift
**Beklenen:** `deterministic_trend + mean_shift`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `quadratic_meanshift1_white_noise_194.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `quadratic_meanshift1_ma_043.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `quadratic_meanshift1_white_noise_190.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `quadratic_meanshift1_arma_000.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `quadratic_meanshift1_ma_113.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `quadratic_meanshift1_ar_081.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `quadratic_meanshift1_ma_000.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `quadratic_meanshift1_arma_019.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `quadratic_meanshift1_arma_114.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `quadratic_meanshift1_white_noise_201.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `quadratic_meanshift2_ar_121.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `quadratic_meanshift2_white_noise_149.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `quadratic_meanshift2_white_noise_101.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `quadratic_meanshift2_white_noise_076.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `quadratic_meanshift2_ar_064.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `quadratic_meanshift2_arma_245.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `quadratic_meanshift2_arma_059.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `quadratic_meanshift2_arma_246.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `quadratic_meanshift2_ma_080.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `quadratic_meanshift2_white_noise_219.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
---

## Grup 30: quad+point_anomaly
**Beklenen:** `deterministic_trend + point_anomaly`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `quadratic_point_arma_080.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_arma_087.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_ma_249.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_ar_247.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_white_noise_085.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_arma_070.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_white_noise_028.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_ma_045.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_white_noise_034.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_arma_128.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_arma_131.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_ma_175.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_ar_236.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_white_noise_219.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_ma_062.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_arma_169.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_ar_021.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_ma_040.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_white_noise_143.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_ma_121.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
---

## Grup 31: quad+variance_shift
**Beklenen:** `deterministic_trend + variance_shift`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `quadratic_varshift_ar_183.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `quadratic_varshift_white_noise_237.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `quadratic_varshift_arma_216.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `quadratic_varshift_white_noise_201.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `quadratic_varshift_ma_052.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `quadratic_varshift_white_noise_023.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `quadratic_varshift_ma_247.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `quadratic_varshift_ma_206.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `quadratic_varshift_arma_205.csv` | `deterministic_trend + mean_shift` | ~ PARTIAL |
| `data` | `quadratic_varshift_ma_230.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
---

## Grup 32: stoch+collective
**Beklenen:** `stochastic_trend + collective_anomaly`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `Stochastic Trend + Collective Anomaly` | `rwd_single_collective_anomaly_middle_386.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ✓ FULL |
| `Stochastic Trend + Collective Anomaly` | `rwd_single_collective_anomaly_middle_466.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ✓ FULL |
| `Stochastic Trend + Collective Anomaly` | `rwd_single_collective_anomaly_middle_717.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ✓ FULL |
| `Stochastic Trend + Collective Anomaly` | `rwd_single_collective_anomaly_middle_698.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ✓ FULL |
| `Stochastic Trend + Collective Anomaly` | `rwd_single_collective_anomaly_middle_442.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ✓ FULL |
| `Stochastic Trend + Collective Anomaly` | `rwd_single_collective_anomaly_middle_501.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ✓ FULL |
| `Stochastic Trend + Collective Anomaly` | `rwd_single_collective_anomaly_middle_928.csv` | `stochastic_trend + collective_anomaly + mean_shift + point_anomaly` | ✓ FULL |
| `Stochastic Trend + Collective Anomaly` | `rwd_single_collective_anomaly_middle_575.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ✓ FULL |
| `Stochastic Trend + Collective Anomaly` | `rwd_single_collective_anomaly_middle_514.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ✓ FULL |
| `Stochastic Trend + Collective Anomaly` | `rwd_single_collective_anomaly_middle_209.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ✓ FULL |
---

## Grup 33: stoch+mean_shift
**Beklenen:** `stochastic_trend + mean_shift`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `Stochastic Trend + Mean Shift` | `rwd_single_mean_shift_increase_middle_326.csv` | `stochastic_trend + mean_shift` | ✓ FULL |
| `Stochastic Trend + Mean Shift` | `rwd_single_mean_shift_increase_middle_305.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ✓ FULL |
| `Stochastic Trend + Mean Shift` | `rwd_single_mean_shift_increase_middle_157.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ✓ FULL |
| `Stochastic Trend + Mean Shift` | `rwd_single_mean_shift_increase_middle_41.csv` | `stochastic_trend + collective_anomaly` | ~ PARTIAL |
| `Stochastic Trend + Mean Shift` | `rwd_single_mean_shift_increase_middle_117.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ✓ FULL |
| `Stochastic Trend + Mean Shift` | `rwd_single_mean_shift_increase_middle_640.csv` | `stochastic_trend + collective_anomaly` | ~ PARTIAL |
| `Stochastic Trend + Mean Shift` | `rwd_single_mean_shift_increase_middle_609.csv` | `stochastic_trend + collective_anomaly` | ~ PARTIAL |
| `Stochastic Trend + Mean Shift` | `rwd_single_mean_shift_increase_middle_31.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ✓ FULL |
| `Stochastic Trend + Mean Shift` | `rwd_single_mean_shift_increase_middle_300.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ✓ FULL |
| `Stochastic Trend + Mean Shift` | `rwd_single_mean_shift_increase_middle_104.csv` | `stochastic_trend` | ~ PARTIAL |
---

## Grup 34: stoch+point_anomaly
**Beklenen:** `stochastic_trend + point_anomaly`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `Stochastic Trend + Point Anomaly` | `rwd_single_point_anomaly_middle_163.csv` | `stochastic_trend + collective_anomaly + point_anomaly` | ✓ FULL |
| `Stochastic Trend + Point Anomaly` | `rwd_single_point_anomaly_middle_750.csv` | `stochastic_trend + collective_anomaly + mean_shift + point_anomaly` | ✓ FULL |
| `Stochastic Trend + Point Anomaly` | `rwd_single_point_anomaly_middle_680.csv` | `stochastic_trend + point_anomaly` | ✓ FULL |
| `Stochastic Trend + Point Anomaly` | `rwd_single_point_anomaly_middle_152.csv` | `stochastic_trend + point_anomaly + trend_shift` | ✓ FULL |
| `Stochastic Trend + Point Anomaly` | `rwd_single_point_anomaly_middle_309.csv` | `stochastic_trend + collective_anomaly + point_anomaly` | ✓ FULL |
| `Stochastic Trend + Point Anomaly` | `rwd_single_point_anomaly_middle_160.csv` | `stochastic_trend + collective_anomaly + point_anomaly` | ✓ FULL |
| `Stochastic Trend + Point Anomaly` | `rwd_single_point_anomaly_middle_933.csv` | `stochastic_trend + point_anomaly` | ✓ FULL |
| `Stochastic Trend + Point Anomaly` | `rwd_single_point_anomaly_middle_127.csv` | `stochastic_trend + collective_anomaly + mean_shift + point_anomaly` | ✓ FULL |
| `Stochastic Trend + Point Anomaly` | `rwd_single_point_anomaly_middle_891.csv` | `stochastic_trend + mean_shift + point_anomaly` | ✓ FULL |
| `Stochastic Trend + Point Anomaly` | `rwd_single_point_anomaly_middle_402.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ~ PARTIAL |
---

## Grup 35: stoch+variance_shift
**Beklenen:** `stochastic_trend + variance_shift`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `ARI + Variance Shift` | `ari_multiple_variance_shifts_620.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `ARI + Variance Shift` | `ari_single_variance_shift_increase_beginning_289.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `ARI + Variance Shift` | `ari_single_variance_shift_decrease_beginning_953.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `ARI + Variance Shift` | `ari_single_variance_shift_decrease_end_351.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `ARI + Variance Shift` | `ari_single_variance_shift_increase_end_530.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `ARI + Variance Shift` | `ari_single_variance_shift_decrease_middle_978.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `ARI + Variance Shift` | `ari_single_variance_shift_decrease_beginning_779.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `ARI + Variance Shift` | `ari_single_variance_shift_increase_beginning_474.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `ARI + Variance Shift` | `ari_single_variance_shift_decrease_beginning_173.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `ARI + Variance Shift` | `ari_single_variance_shift_increase_end_931.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `ARIMA + Variance Shift` | `arima_single_variance_shift_increase_beginning_708.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `ARIMA + Variance Shift` | `arima_single_variance_shift_increase_beginning_747.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `ARIMA + Variance Shift` | `arima_single_variance_shift_decrease_middle_884.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `ARIMA + Variance Shift` | `arima_single_variance_shift_decrease_beginning_990.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `ARIMA + Variance Shift` | `arima_single_variance_shift_increase_middle_483.csv` | `stochastic_trend` | ~ PARTIAL |
| `ARIMA + Variance Shift` | `arima_single_variance_shift_decrease_middle_886.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `ARIMA + Variance Shift` | `arima_single_variance_shift_increase_middle_652.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `ARIMA + Variance Shift` | `arima_single_variance_shift_decrease_middle_4.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `ARIMA + Variance Shift` | `arima_single_variance_shift_decrease_beginning_601.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `ARIMA + Variance Shift` | `arima_multiple_variance_shifts_794.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `IMA + Variance Shift` | `ima_multiple_variance_shifts_813.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `IMA + Variance Shift` | `ima_single_variance_shift_increase_end_457.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `IMA + Variance Shift` | `ima_single_variance_shift_decrease_middle_577.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `IMA + Variance Shift` | `ima_single_variance_shift_decrease_end_910.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `IMA + Variance Shift` | `ima_single_variance_shift_decrease_middle_520.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `IMA + Variance Shift` | `ima_single_variance_shift_decrease_middle_429.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `IMA + Variance Shift` | `ima_single_variance_shift_decrease_middle_841.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `IMA + Variance Shift` | `ima_single_variance_shift_increase_end_974.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `IMA + Variance Shift` | `ima_multiple_variance_shifts_498.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `IMA + Variance Shift` | `ima_single_variance_shift_increase_end_563.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RW + Variance Shift` | `rw_single_variance_shift_increase_end_416.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RW + Variance Shift` | `rw_single_variance_shift_increase_end_362.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RW + Variance Shift` | `rw_multiple_variance_shifts_824.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RW + Variance Shift` | `rw_multiple_variance_shifts_545.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RW + Variance Shift` | `rw_single_variance_shift_decrease_middle_367.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RW + Variance Shift` | `rw_single_variance_shift_increase_end_968.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RW + Variance Shift` | `rw_single_variance_shift_decrease_end_80.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RW + Variance Shift` | `rw_single_variance_shift_increase_middle_600.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RW + Variance Shift` | `rw_multiple_variance_shifts_904.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RW + Variance Shift` | `rw_single_variance_shift_decrease_end_130.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RWD + Variance Shift` | `rwd_single_variance_shift_decrease_beginning_610.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RWD + Variance Shift` | `rwd_single_variance_shift_decrease_beginning_600.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RWD + Variance Shift` | `rwd_single_variance_shift_increase_beginning_452.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RWD + Variance Shift` | `rwd_single_variance_shift_decrease_middle_706.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RWD + Variance Shift` | `rwd_single_variance_shift_decrease_beginning_231.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RWD + Variance Shift` | `rwd_single_variance_shift_decrease_middle_509.csv` | `stochastic_trend` | ~ PARTIAL |
| `RWD + Variance Shift` | `rwd_single_variance_shift_decrease_beginning_551.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RWD + Variance Shift` | `rwd_single_variance_shift_decrease_end_351.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RWD + Variance Shift` | `rwd_single_variance_shift_decrease_middle_809.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RWD + Variance Shift` | `rwd_single_variance_shift_decrease_end_14.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
---

## Grup 36: vol+collective
**Beklenen:** `volatility + collective_anomaly`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `Volatility + Collective Anomaly` | `garch_single_collective_anomaly_middle_904.csv` | `volatility + collective_anomaly + trend_shift + variance_shift` | ✓ FULL |
| `Volatility + Collective Anomaly` | `garch_single_collective_anomaly_middle_95.csv` | `volatility` | ~ PARTIAL |
| `Volatility + Collective Anomaly` | `garch_single_collective_anomaly_middle_168.csv` | `volatility + collective_anomaly + point_anomaly` | ✓ FULL |
| `Volatility + Collective Anomaly` | `garch_single_collective_anomaly_middle_506.csv` | `volatility + collective_anomaly + point_anomaly` | ✓ FULL |
| `Volatility + Collective Anomaly` | `garch_single_collective_anomaly_middle_843.csv` | `volatility + collective_anomaly + point_anomaly` | ✓ FULL |
| `Volatility + Collective Anomaly` | `garch_single_collective_anomaly_middle_893.csv` | `volatility + collective_anomaly + variance_shift` | ✓ FULL |
| `Volatility + Collective Anomaly` | `garch_single_collective_anomaly_middle_888.csv` | `volatility + collective_anomaly + point_anomaly` | ✓ FULL |
| `Volatility + Collective Anomaly` | `garch_single_collective_anomaly_middle_605.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ✓ FULL |
| `Volatility + Collective Anomaly` | `garch_single_collective_anomaly_middle_189.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ✓ FULL |
| `Volatility + Collective Anomaly` | `garch_single_collective_anomaly_middle_144.csv` | `volatility + collective_anomaly` | ✓ FULL |
---

## Grup 37: vol+mean_shift
**Beklenen:** `volatility + mean_shift`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `Volatility + Mean Shift` | `garch_single_mean_shift_increase_middle_7.csv` | `volatility + mean_shift + variance_shift` | ✓ FULL |
| `Volatility + Mean Shift` | `garch_single_mean_shift_increase_middle_597.csv` | `volatility + mean_shift + point_anomaly` | ✓ FULL |
| `Volatility + Mean Shift` | `garch_single_mean_shift_increase_middle_87.csv` | `volatility + mean_shift + point_anomaly` | ✓ FULL |
| `Volatility + Mean Shift` | `garch_single_mean_shift_increase_middle_111.csv` | `volatility + mean_shift + point_anomaly` | ✓ FULL |
| `Volatility + Mean Shift` | `garch_single_mean_shift_increase_middle_992.csv` | `volatility + mean_shift + point_anomaly` | ✓ FULL |
| `Volatility + Mean Shift` | `garch_single_mean_shift_increase_middle_184.csv` | `volatility + mean_shift` | ✓ FULL |
| `Volatility + Mean Shift` | `garch_single_mean_shift_increase_middle_952.csv` | `volatility + collective_anomaly + mean_shift` | ✓ FULL |
| `Volatility + Mean Shift` | `garch_single_mean_shift_increase_middle_793.csv` | `volatility + collective_anomaly + mean_shift` | ✓ FULL |
| `Volatility + Mean Shift` | `garch_single_mean_shift_increase_middle_881.csv` | `volatility + collective_anomaly + mean_shift` | ✓ FULL |
| `Volatility + Mean Shift` | `garch_single_mean_shift_increase_middle_316.csv` | `volatility + collective_anomaly + mean_shift` | ✓ FULL |
---

## Grup 38: vol+point_anomaly
**Beklenen:** `volatility + point_anomaly`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `Volatility + Point Anomaly` | `garch_single_point_anomaly_middle_251.csv` | `volatility + point_anomaly + variance_shift` | ✓ FULL |
| `Volatility + Point Anomaly` | `garch_single_point_anomaly_middle_473.csv` | `volatility + collective_anomaly + point_anomaly` | ✓ FULL |
| `Volatility + Point Anomaly` | `garch_single_point_anomaly_middle_546.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ✓ FULL |
| `Volatility + Point Anomaly` | `garch_single_point_anomaly_middle_541.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ✓ FULL |
| `Volatility + Point Anomaly` | `garch_single_point_anomaly_middle_295.csv` | `volatility + collective_anomaly` | ~ PARTIAL |
| `Volatility + Point Anomaly` | `garch_single_point_anomaly_middle_896.csv` | `volatility + collective_anomaly + point_anomaly` | ✓ FULL |
| `Volatility + Point Anomaly` | `garch_single_point_anomaly_middle_468.csv` | `volatility + collective_anomaly + point_anomaly` | ✓ FULL |
| `Volatility + Point Anomaly` | `garch_single_point_anomaly_middle_930.csv` | `volatility + collective_anomaly + point_anomaly` | ✓ FULL |
| `Volatility + Point Anomaly` | `garch_single_point_anomaly_middle_152.csv` | `volatility + point_anomaly + variance_shift` | ✓ FULL |
| `Volatility + Point Anomaly` | `garch_single_point_anomaly_middle_25.csv` | `volatility + collective_anomaly` | ~ PARTIAL |
---

## Grup 39: vol+variance_shift
**Beklenen:** `volatility + variance_shift`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `Volatility + Variance Shift` | `garch_single_variance_shift_increase_middle_448.csv` | `volatility + variance_shift` | ✓ FULL |
| `Volatility + Variance Shift` | `garch_single_variance_shift_increase_middle_100.csv` | `volatility + point_anomaly + variance_shift` | ✓ FULL |
| `Volatility + Variance Shift` | `garch_single_variance_shift_increase_middle_458.csv` | `volatility + point_anomaly + variance_shift` | ✓ FULL |
| `Volatility + Variance Shift` | `garch_single_variance_shift_increase_middle_342.csv` | `stationary + collective_anomaly + variance_shift` | ~ PARTIAL |
| `Volatility + Variance Shift` | `garch_single_variance_shift_increase_middle_952.csv` | `volatility + collective_anomaly + variance_shift` | ✓ FULL |
| `Volatility + Variance Shift` | `garch_single_variance_shift_increase_middle_820.csv` | `volatility + variance_shift` | ✓ FULL |
| `Volatility + Variance Shift` | `garch_single_variance_shift_increase_middle_821.csv` | `volatility + variance_shift` | ✓ FULL |
| `Volatility + Variance Shift` | `garch_single_variance_shift_increase_middle_517.csv` | `volatility + variance_shift` | ✓ FULL |
| `Volatility + Variance Shift` | `garch_single_variance_shift_increase_middle_361.csv` | `volatility + point_anomaly + variance_shift` | ✓ FULL |
| `Volatility + Variance Shift` | `garch_single_variance_shift_increase_middle_489.csv` | `volatility + variance_shift` | ✓ FULL |

---

## Model Olasılıkları — Sadece Hatalı Örnekler

| Grup | CSV | stat | det | stoch | vol | coll | ctx | mean | point | trend | var | Sonuç |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cubic+mean_shift | `cubic_meanshift1_arma_091.csv` | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.09 | 0.00 | 0.00 | 1.00 | PARTIAL |
| cubic+mean_shift | `cubic_meanshift2_ma_017.csv` | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.26 | 0.00 | 0.00 | 0.99 | PARTIAL |
| damped+mean_shift | `damped_meanshift1_arma_044.csv` | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.25 | 0.00 | 0.00 | 1.00 | PARTIAL |
| damped+mean_shift | `damped_meanshift2_ar_120.csv` | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.49 | 0.00 | 0.00 | 0.84 | PARTIAL |
| damped+variance_shift | `damped_varshift_white_noise_104.csv` | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.98 | 0.00 | 0.00 | 0.19 | PARTIAL |
| quad+variance_shift | `quadratic_varshift_arma_205.csv` | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.71 | 0.01 | 0.00 | 0.23 | PARTIAL |
| stoch+mean_shift | `rwd_single_mean_shift_increase_middle_41.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.98 | 0.00 | 0.47 | 0.08 | 0.02 | 0.01 | PARTIAL |
| stoch+mean_shift | `rwd_single_mean_shift_increase_middle_640.csv` | 0.17 | 0.00 | 1.00 | 0.00 | 1.00 | 0.00 | 0.08 | 0.08 | 0.01 | 0.11 | PARTIAL |
| stoch+mean_shift | `rwd_single_mean_shift_increase_middle_609.csv` | 0.10 | 0.00 | 1.00 | 0.00 | 0.88 | 0.00 | 0.30 | 0.04 | 0.01 | 0.03 | PARTIAL |
| stoch+mean_shift | `rwd_single_mean_shift_increase_middle_104.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.15 | 0.01 | 0.00 | 0.00 | PARTIAL |
| stoch+point_anomaly | `rwd_single_point_anomaly_middle_402.csv` | 0.05 | 0.00 | 1.00 | 0.00 | 1.00 | 0.00 | 0.91 | 0.20 | 0.00 | 0.01 | PARTIAL |
| stoch+variance_shift | `arima_single_variance_shift_increase_middle_483.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.48 | PARTIAL |
| stoch+variance_shift | `rwd_single_variance_shift_decrease_middle_509.csv` | 0.47 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.07 | 0.05 | PARTIAL |
| vol+collective | `garch_single_collective_anomaly_middle_95.csv` | 0.79 | 0.00 | 0.00 | 1.00 | 0.27 | 0.00 | 0.37 | 0.32 | 0.14 | 0.13 | PARTIAL |
| vol+point_anomaly | `garch_single_point_anomaly_middle_295.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.93 | 0.00 | 0.02 | 0.34 | 0.07 | 0.41 | PARTIAL |
| vol+point_anomaly | `garch_single_point_anomaly_middle_25.csv` | 0.51 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.06 | 0.21 | 0.17 | 0.17 | PARTIAL |
| vol+variance_shift | `garch_single_variance_shift_increase_middle_342.csv` | 1.00 | 0.00 | 0.00 | 0.99 | 0.99 | 0.00 | 0.05 | 0.21 | 0.26 | 0.63 | PARTIAL |