# Manuel Test — Tüm Leaf Klasörlerden 1 Sample

Her kaynak grubun her leaf klasöründen 1 rastgele CSV alınıp ensemble ile sınıflandırılmıştır.

## Özet

| Metrik | Değer |
|---|---|
| Toplam test | 440 |
| Full match | 300 (68.2%) |
| Partial match | 99 (22.5%) |
| No match | 41 (9.3%) |

## Grup Bazlı Özet

| # | Grup | Beklenen | Leaf | Full | Partial | None |
|---|---|---|---|---|---|---|
| 1 | stationary | stationary | 12 | 4 | 8 | 0 |
| 2 | deterministic_trend | deterministic_trend | 72 | 24 | 21 | 27 |
| 3 | stochastic_trend | stochastic_trend | 15 | 4 | 8 | 3 |
| 4 | volatility | volatility | 12 | 5 | 6 | 1 |
| 5 | collective_anomaly | stationary + collective_anomaly | 48 | 30 | 16 | 2 |
| 6 | contextual_anomaly | stationary + contextual_anomaly | 48 | 48 | 0 | 0 |
| 7 | mean_shift | stationary + mean_shift | 48 | 41 | 6 | 1 |
| 8 | point_anomaly | stationary + point_anomaly | 48 | 31 | 13 | 4 |
| 9 | trend_shift | stationary + trend_shift | 48 | 43 | 5 | 0 |
| 10 | variance_shift | stationary + variance_shift | 48 | 31 | 14 | 3 |
| 11 | cubic+collective | deterministic_trend + collective_anomaly | 1 | 1 | 0 | 0 |
| 12 | cubic+mean_shift | deterministic_trend + mean_shift | 2 | 2 | 0 | 0 |
| 13 | cubic+point_anomaly | deterministic_trend + point_anomaly | 1 | 1 | 0 | 0 |
| 14 | cubic+variance_shift | deterministic_trend + variance_shift | 1 | 1 | 0 | 0 |
| 15 | damped+collective | deterministic_trend + collective_anomaly | 1 | 1 | 0 | 0 |
| 16 | damped+mean_shift | deterministic_trend + mean_shift | 2 | 2 | 0 | 0 |
| 17 | damped+point_anomaly | deterministic_trend + point_anomaly | 1 | 1 | 0 | 0 |
| 18 | damped+variance_shift | deterministic_trend + variance_shift | 1 | 1 | 0 | 0 |
| 19 | exp+collective | deterministic_trend + collective_anomaly | 1 | 1 | 0 | 0 |
| 20 | exp+mean_shift | deterministic_trend + mean_shift | 2 | 2 | 0 | 0 |
| 21 | exp+point_anomaly | deterministic_trend + point_anomaly | 1 | 1 | 0 | 0 |
| 22 | exp+variance_shift | deterministic_trend + variance_shift | 1 | 1 | 0 | 0 |
| 23 | linear+collective | deterministic_trend + collective_anomaly | 1 | 1 | 0 | 0 |
| 24 | linear+mean_shift | deterministic_trend + mean_shift | 2 | 2 | 0 | 0 |
| 25 | linear+point_anomaly | deterministic_trend + point_anomaly | 1 | 1 | 0 | 0 |
| 26 | linear+trend_shift | deterministic_trend + trend_shift | 3 | 3 | 0 | 0 |
| 27 | linear+variance_shift | deterministic_trend + variance_shift | 1 | 1 | 0 | 0 |
| 28 | quad+collective | deterministic_trend + collective_anomaly | 1 | 1 | 0 | 0 |
| 29 | quad+mean_shift | deterministic_trend + mean_shift | 2 | 2 | 0 | 0 |
| 30 | quad+point_anomaly | deterministic_trend + point_anomaly | 2 | 2 | 0 | 0 |
| 31 | quad+variance_shift | deterministic_trend + variance_shift | 1 | 1 | 0 | 0 |
| 32 | stoch+collective | stochastic_trend + collective_anomaly | 1 | 1 | 0 | 0 |
| 33 | stoch+mean_shift | stochastic_trend + mean_shift | 1 | 1 | 0 | 0 |
| 34 | stoch+point_anomaly | stochastic_trend + point_anomaly | 1 | 1 | 0 | 0 |
| 35 | stoch+variance_shift | stochastic_trend + variance_shift | 5 | 5 | 0 | 0 |
| 36 | vol+collective | volatility + collective_anomaly | 1 | 0 | 1 | 0 |
| 37 | vol+mean_shift | volatility + mean_shift | 1 | 0 | 1 | 0 |
| 38 | vol+point_anomaly | volatility + point_anomaly | 1 | 1 | 0 | 0 |
| 39 | vol+variance_shift | volatility + variance_shift | 1 | 1 | 0 | 0 |

---

## Grup 1: stationary
**Beklenen:** `stationary`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `ar_long` | `ar_28856.csv` | `stationary` | `stationary + point_anomaly` | ~ PARTIAL |
| `ar_medium` | `ar_13281.csv` | `stationary` | `stationary` | ✓ FULL |
| `ar_short` | `ar_10735.csv` | `stationary` | `stationary + collective_anomaly` | ~ PARTIAL |
| `arma_long` | `arma_31868.csv` | `stationary` | `stationary` | ✓ FULL |
| `arma_medium` | `arma_18109.csv` | `stationary` | `stationary + point_anomaly` | ~ PARTIAL |
| `arma_short` | `arma_1722.csv` | `stationary` | `stationary + collective_anomaly` | ~ PARTIAL |
| `ma_long` | `ma_16581.csv` | `stationary` | `stationary + point_anomaly` | ~ PARTIAL |
| `ma_medium` | `ma_14112.csv` | `stationary` | `stationary + point_anomaly` | ~ PARTIAL |
| `ma_short` | `ma_31717.csv` | `stationary` | `stationary + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `wn_long` | `wn_1302.csv` | `stationary` | `stationary` | ✓ FULL |
| `wn_medium` | `wn_29956.csv` | `stationary` | `stationary` | ✓ FULL |
| `wn_short` | `wn_31841.csv` | `stationary` | `stationary + collective_anomaly` | ~ PARTIAL |
---

## Grup 2: deterministic_trend
**Beklenen:** `deterministic_trend`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `long` | `ar_cubic_trend_920.csv` | `deterministic_trend` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ar_cubic_trend_600.csv` | `deterministic_trend` | `stochastic_trend + trend_shift` | ✗ NONE |
| `short` | `ar_cubic_trend_179.csv` | `deterministic_trend` | `stochastic_trend + trend_shift` | ✗ NONE |
| `long` | `ar_damped_trend_642.csv` | `deterministic_trend` | `deterministic_trend` | ✓ FULL |
| `medium` | `ar_damped_trend_488.csv` | `deterministic_trend` | `deterministic_trend` | ✓ FULL |
| `short` | `ar_damped_trend_127.csv` | `deterministic_trend` | `deterministic_trend` | ✓ FULL |
| `long` | `ar_exponential_trend_125.csv` | `deterministic_trend` | `deterministic_trend` | ✓ FULL |
| `medium` | `ar_exponential_trend_184.csv` | `deterministic_trend` | `stationary + trend_shift` | ✗ NONE |
| `short` | `ar_exponential_trend_3.csv` | `deterministic_trend` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `long` | `ar_linear_down_trend_312.csv` | `deterministic_trend` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `medium` | `ar_linear_down_trend_564.csv` | `deterministic_trend` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `short` | `ar_linear_down_trend_653.csv` | `deterministic_trend` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `long` | `ar_linear_up_trend_122.csv` | `deterministic_trend` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ar_linear_up_trend_615.csv` | `deterministic_trend` | `stochastic_trend + trend_shift` | ✗ NONE |
| `short` | `ar_linear_up_trend_281.csv` | `deterministic_trend` | `deterministic_trend + mean_shift + point_anomaly` | ~ PARTIAL |
| `long` | `ar_quadratic_trend_759.csv` | `deterministic_trend` | `deterministic_trend + collective_anomaly` | ~ PARTIAL |
| `medium` | `ar_quadratic_trend_698.csv` | `deterministic_trend` | `deterministic_trend + collective_anomaly` | ~ PARTIAL |
| `short` | `ar_quadratic_trend_745.csv` | `deterministic_trend` | `stationary` | ✗ NONE |
| `long` | `arma_cubic_trend_600.csv` | `deterministic_trend` | `stationary` | ✗ NONE |
| `medium` | `arma_cubic_trend_485.csv` | `deterministic_trend` | `stochastic_trend` | ✗ NONE |
| `short` | `arma_cubic_trend_300.csv` | `deterministic_trend` | `stochastic_trend` | ✗ NONE |
| `long` | `arma_damped_trend_511.csv` | `deterministic_trend` | `deterministic_trend` | ✓ FULL |
| `medium` | `arma_damped_trend_641.csv` | `deterministic_trend` | `deterministic_trend` | ✓ FULL |
| `short` | `arma_damped_trend_354.csv` | `deterministic_trend` | `deterministic_trend` | ✓ FULL |
| `long` | `arma_exponential_trend_844.csv` | `deterministic_trend` | `deterministic_trend` | ✓ FULL |
| `medium` | `arma_exponential_trend_90.csv` | `deterministic_trend` | `deterministic_trend` | ✓ FULL |
| `short` | `arma_exponential_trend_103.csv` | `deterministic_trend` | `deterministic_trend` | ✓ FULL |
| `long` | `arma_linear_down_trend_799.csv` | `deterministic_trend` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `medium` | `arma_linear_down_trend_841.csv` | `deterministic_trend` | `stationary + trend_shift` | ✗ NONE |
| `short` | `arma_linear_down_trend_245.csv` | `deterministic_trend` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `long` | `arma_linear_up_trend_741.csv` | `deterministic_trend` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `arma_linear_up_trend_488.csv` | `deterministic_trend` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `short` | `arma_linear_up_trend_411.csv` | `deterministic_trend` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `long` | `arma_quadratic_trend_354.csv` | `deterministic_trend` | `deterministic_trend + collective_anomaly` | ~ PARTIAL |
| `medium` | `arma_quadratic_trend_241.csv` | `deterministic_trend` | `deterministic_trend` | ✓ FULL |
| `short` | `arma_quadratic_trend_297.csv` | `deterministic_trend` | `deterministic_trend` | ✓ FULL |
| `long` | `ma_cubic_trend_981.csv` | `deterministic_trend` | `stationary` | ✗ NONE |
| `medium` | `ma_cubic_trend_801.csv` | `deterministic_trend` | `stationary + trend_shift` | ✗ NONE |
| `short` | `ma_cubic_trend_408.csv` | `deterministic_trend` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `long` | `ma_damped_trend_192.csv` | `deterministic_trend` | `deterministic_trend` | ✓ FULL |
| `medium` | `ma_damped_trend_183.csv` | `deterministic_trend` | `deterministic_trend` | ✓ FULL |
| `short` | `ma_damped_trend_449.csv` | `deterministic_trend` | `deterministic_trend` | ✓ FULL |
| `long` | `ma_exponential_trend_188.csv` | `deterministic_trend` | `deterministic_trend` | ✓ FULL |
| `medium` | `ma_exponential_trend_429.csv` | `deterministic_trend` | `stationary + trend_shift` | ✗ NONE |
| `short` | `ma_exponential_trend_88.csv` | `deterministic_trend` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `long` | `ma_linear_down_trend_415.csv` | `deterministic_trend` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ma_linear_down_trend_655.csv` | `deterministic_trend` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `short` | `ma_linear_down_trend_341.csv` | `deterministic_trend` | `stationary + trend_shift` | ✗ NONE |
| `long` | `ma_linear_up_trend_842.csv` | `deterministic_trend` | `stationary` | ✗ NONE |
| `medium` | `ma_linear_up_trend_138.csv` | `deterministic_trend` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `short` | `ma_linear_up_trend_771.csv` | `deterministic_trend` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `long` | `ma_quadratic_trend_521.csv` | `deterministic_trend` | `deterministic_trend + collective_anomaly` | ~ PARTIAL |
| `medium` | `ma_quadratic_trend_593.csv` | `deterministic_trend` | `deterministic_trend + collective_anomaly` | ~ PARTIAL |
| `short` | `ma_quadratic_trend_212.csv` | `deterministic_trend` | `stationary` | ✗ NONE |
| `long` | `white_noise_cubic_trend_996.csv` | `deterministic_trend` | `stationary` | ✗ NONE |
| `medium` | `white_noise_cubic_trend_949.csv` | `deterministic_trend` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `short` | `white_noise_cubic_trend_447.csv` | `deterministic_trend` | `stochastic_trend + trend_shift` | ✗ NONE |
| `long` | `white_noise_damped_trend_170.csv` | `deterministic_trend` | `deterministic_trend` | ✓ FULL |
| `medium` | `white_noise_damped_trend_607.csv` | `deterministic_trend` | `deterministic_trend` | ✓ FULL |
| `short` | `white_noise_damped_trend_369.csv` | `deterministic_trend` | `deterministic_trend` | ✓ FULL |
| `long` | `white_noise_exponential_trend_863.csv` | `deterministic_trend` | `deterministic_trend` | ✓ FULL |
| `medium` | `white_noise_exponential_trend_678.csv` | `deterministic_trend` | `deterministic_trend` | ✓ FULL |
| `short` | `white_noise_exponential_trend_669.csv` | `deterministic_trend` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `long` | `white_noise_linear_down_trend_914.csv` | `deterministic_trend` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `white_noise_linear_down_trend_893.csv` | `deterministic_trend` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `short` | `white_noise_linear_down_trend_431.csv` | `deterministic_trend` | `stationary + trend_shift` | ✗ NONE |
| `long` | `white_noise_linear_up_trend_630.csv` | `deterministic_trend` | `deterministic_trend` | ✓ FULL |
| `medium` | `white_noise_linear_up_trend_275.csv` | `deterministic_trend` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `short` | `white_noise_linear_up_trend_748.csv` | `deterministic_trend` | `stochastic_trend + trend_shift` | ✗ NONE |
| `long` | `white_noise_quadratic_trend_162.csv` | `deterministic_trend` | `stationary` | ✗ NONE |
| `medium` | `white_noise_quadratic_trend_14.csv` | `deterministic_trend` | `deterministic_trend` | ✓ FULL |
| `short` | `white_noise_quadratic_trend_708.csv` | `deterministic_trend` | `deterministic_trend` | ✓ FULL |
---

## Grup 3: stochastic_trend
**Beklenen:** `stochastic_trend`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `stochastic_ari_long` | `ari_308.csv` | `stochastic_trend` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_ari_medium` | `ari_810.csv` | `stochastic_trend` | `stationary + trend_shift` | ✗ NONE |
| `stochastic_ari_short` | `ari_365.csv` | `stochastic_trend` | `stochastic_trend + mean_shift` | ~ PARTIAL |
| `stochastic_arima_long` | `arima_171.csv` | `stochastic_trend` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_arima_medium` | `arima_887.csv` | `stochastic_trend` | `stationary + mean_shift + trend_shift` | ✗ NONE |
| `stochastic_arima_short` | `arima_312.csv` | `stochastic_trend` | `stationary + mean_shift` | ✗ NONE |
| `stochastic_ima_long` | `ima_898.csv` | `stochastic_trend` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_ima_medium` | `ima_191.csv` | `stochastic_trend` | `stochastic_trend + trend_shift` | ~ PARTIAL |
| `stochastic_ima_short` | `ima_449.csv` | `stochastic_trend` | `stochastic_trend` | ✓ FULL |
| `stochastic_rw_long` | `random_walk_354.csv` | `stochastic_trend` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_rw_medium` | `random_walk_516.csv` | `stochastic_trend` | `stochastic_trend` | ✓ FULL |
| `stochastic_rw_short` | `random_walk_684.csv` | `stochastic_trend` | `stochastic_trend + mean_shift` | ~ PARTIAL |
| `stochastic_rwd_long` | `random_walk_drift_868.csv` | `stochastic_trend` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_rwd_medium` | `random_walk_drift_434.csv` | `stochastic_trend` | `stochastic_trend` | ✓ FULL |
| `stochastic_rwd_short` | `random_walk_drift_248.csv` | `stochastic_trend` | `stochastic_trend` | ✓ FULL |
---

## Grup 4: volatility
**Beklenen:** `volatility`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `volatility_aparch_long` | `aparch_44.csv` | `volatility` | `volatility` | ✓ FULL |
| `volatility_aparch_medium` | `aparch_425.csv` | `volatility` | `volatility + point_anomaly` | ~ PARTIAL |
| `volatility_aparch_short` | `aparch_291.csv` | `volatility` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
| `volatility_arch_long` | `arch_716.csv` | `volatility` | `volatility` | ✓ FULL |
| `volatility_arch_medium` | `arch_344.csv` | `volatility` | `volatility + variance_shift` | ~ PARTIAL |
| `volatility_arch_short` | `arch_745.csv` | `volatility` | `volatility + variance_shift` | ~ PARTIAL |
| `volatility_egarch_long` | `egarch_962.csv` | `volatility` | `volatility` | ✓ FULL |
| `volatility_egarch_medium` | `egarch_728.csv` | `volatility` | `stationary + point_anomaly` | ✗ NONE |
| `volatility_egarch_short` | `egarch_696.csv` | `volatility` | `volatility + collective_anomaly` | ~ PARTIAL |
| `volatility_garch_long` | `garch_164.csv` | `volatility` | `volatility` | ✓ FULL |
| `volatility_garch_medium` | `garch_66.csv` | `volatility` | `volatility` | ✓ FULL |
| `volatility_garch_short` | `garch_684.csv` | `volatility` | `volatility + mean_shift + point_anomaly + variance_shift` | ~ PARTIAL |
---

## Grup 5: collective_anomaly
**Beklenen:** `stationary + collective_anomaly`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `multiple` | `ar_collective_anomaly_256.csv` | `stationary + collective_anomaly` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `beginning` | `ar_collective_anomaly_590.csv` | `stationary + collective_anomaly` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `end` | `ar_collective_anomaly_770.csv` | `stationary + collective_anomaly` | `stationary` | ~ PARTIAL |
| `middle` | `ar_collective_anomaly_323.csv` | `stationary + collective_anomaly` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `ar_collective_anomaly_249.csv` | `stationary + collective_anomaly` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `beginning` | `ar_collective_anomaly_524.csv` | `stationary + collective_anomaly` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `end` | `ar_collective_anomaly_448.csv` | `stationary + collective_anomaly` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `middle` | `ar_collective_anomaly_347.csv` | `stationary + collective_anomaly` | `stationary + collective_anomaly` | ✓ FULL |
| `multiple` | `ar_collective_anomaly_951.csv` | `stationary + collective_anomaly` | `stochastic_trend + point_anomaly` | ✗ NONE |
| `beginning` | `ar_collective_anomaly_689.csv` | `stationary + collective_anomaly` | `stationary` | ~ PARTIAL |
| `end` | `ar_collective_anomaly_732.csv` | `stationary + collective_anomaly` | `stationary + point_anomaly` | ~ PARTIAL |
| `middle` | `ar_collective_anomaly_611.csv` | `stationary + collective_anomaly` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `arma_collective_anomaly_30.csv` | `stationary + collective_anomaly` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `beginning` | `arma_collective_anomaly_73.csv` | `stationary + collective_anomaly` | `stationary + variance_shift` | ~ PARTIAL |
| `end` | `arma_collective_anomaly_398.csv` | `stationary + collective_anomaly` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `middle` | `arma_collective_anomaly_876.csv` | `stationary + collective_anomaly` | `stationary + collective_anomaly` | ✓ FULL |
| `multiple` | `arma_collective_anomaly_806.csv` | `stationary + collective_anomaly` | `stationary + collective_anomaly` | ✓ FULL |
| `beginning` | `arma_collective_anomaly_813.csv` | `stationary + collective_anomaly` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `end` | `arma_collective_anomaly_15.csv` | `stationary + collective_anomaly` | `stationary` | ~ PARTIAL |
| `middle` | `arma_collective_anomaly_309.csv` | `stationary + collective_anomaly` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `multiple` | `arma_collective_anomaly_856.csv` | `stationary + collective_anomaly` | `stationary + collective_anomaly` | ✓ FULL |
| `beginning` | `arma_collective_anomaly_127.csv` | `stationary + collective_anomaly` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `end` | `arma_collective_anomaly_840.csv` | `stationary + collective_anomaly` | `stochastic_trend + collective_anomaly + mean_shift` | ~ PARTIAL |
| `middle` | `arma_collective_anomaly_39.csv` | `stationary + collective_anomaly` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `ma_collective_anomaly_468.csv` | `stationary + collective_anomaly` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `beginning` | `ma_collective_anomaly_345.csv` | `stationary + collective_anomaly` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `end` | `ma_collective_anomaly_159.csv` | `stationary + collective_anomaly` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `middle` | `ma_collective_anomaly_293.csv` | `stationary + collective_anomaly` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `multiple` | `ma_collective_anomaly_940.csv` | `stationary + collective_anomaly` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `beginning` | `ma_collective_anomaly_968.csv` | `stationary + collective_anomaly` | `stationary + mean_shift` | ~ PARTIAL |
| `end` | `ma_collective_anomaly_620.csv` | `stationary + collective_anomaly` | `stationary + mean_shift` | ~ PARTIAL |
| `middle` | `ma_collective_anomaly_906.csv` | `stationary + collective_anomaly` | `stationary` | ~ PARTIAL |
| `multiple` | `ma_collective_anomaly_760.csv` | `stationary + collective_anomaly` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `beginning` | `ma_collective_anomaly_389.csv` | `stationary + collective_anomaly` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `end` | `ma_collective_anomaly_294.csv` | `stationary + collective_anomaly` | `volatility + collective_anomaly` | ~ PARTIAL |
| `middle` | `ma_collective_anomaly_702.csv` | `stationary + collective_anomaly` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `multiple` | `white_noise_collective_anomaly_559.csv` | `stationary + collective_anomaly` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `beginning` | `white_noise_collective_anomaly_463.csv` | `stationary + collective_anomaly` | `stationary + mean_shift + point_anomaly` | ~ PARTIAL |
| `end` | `white_noise_collective_anomaly_913.csv` | `stationary + collective_anomaly` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `middle` | `white_noise_collective_anomaly_941.csv` | `stationary + collective_anomaly` | `stationary + collective_anomaly` | ✓ FULL |
| `multiple` | `white_noise_collective_anomaly_691.csv` | `stationary + collective_anomaly` | `stationary + collective_anomaly` | ✓ FULL |
| `beginning` | `white_noise_collective_anomaly_520.csv` | `stationary + collective_anomaly` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `end` | `white_noise_collective_anomaly_23.csv` | `stationary + collective_anomaly` | `stationary + mean_shift` | ~ PARTIAL |
| `middle` | `white_noise_collective_anomaly_342.csv` | `stationary + collective_anomaly` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `multiple` | `white_noise_collective_anomaly_226.csv` | `stationary + collective_anomaly` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `beginning` | `white_noise_collective_anomaly_325.csv` | `stationary + collective_anomaly` | `stationary + collective_anomaly + mean_shift + trend_shift` | ✓ FULL |
| `end` | `white_noise_collective_anomaly_785.csv` | `stationary + collective_anomaly` | `volatility + collective_anomaly` | ~ PARTIAL |
| `middle` | `white_noise_collective_anomaly_615.csv` | `stationary + collective_anomaly` | `volatility + point_anomaly` | ✗ NONE |
---

## Grup 6: contextual_anomaly
**Beklenen:** `stationary + contextual_anomaly`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `multiple` | `ar_contextual_anomaly_multiple_595.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_long_beginning` | `ar_contextual_anomaly_beginning_340.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_long_end` | `ar_contextual_anomaly_end_787.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_long_middle` | `ar_contextual_anomaly_middle_637.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `ar_contextual_anomaly_multiple_493.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_medium_beginning` | `ar_contextual_anomaly_beginning_926.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_medium_end` | `ar_contextual_anomaly_end_636.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_medium_middle` | `ar_contextual_anomaly_middle_466.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `ar_contextual_anomaly_multiple_431.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_short_beginning` | `ar_contextual_anomaly_beginning_30.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_short_end` | `ar_contextual_anomaly_end_225.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_short_middle` | `ar_contextual_anomaly_middle_568.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `arma_contextual_anomaly_multiple_553.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_long_beginning` | `arma_contextual_anomaly_beginning_182.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_long_end` | `arma_contextual_anomaly_end_795.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_long_middle` | `arma_contextual_anomaly_middle_141.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `arma_contextual_anomaly_multiple_892.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_medium_beginning` | `arma_contextual_anomaly_beginning_2.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_medium_end` | `arma_contextual_anomaly_end_239.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_medium_middle` | `arma_contextual_anomaly_middle_677.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `arma_contextual_anomaly_multiple_245.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_short_beginning` | `arma_contextual_anomaly_beginning_829.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_short_end` | `arma_contextual_anomaly_end_725.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_short_middle` | `arma_contextual_anomaly_middle_488.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `ma_contextual_anomaly_multiple_648.csv` | `stationary + contextual_anomaly` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `MA_long_beginning` | `ma_contextual_anomaly_beginning_157.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_long_end` | `ma_contextual_anomaly_end_453.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_long_middle` | `ma_contextual_anomaly_middle_45.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `ma_contextual_anomaly_multiple_648.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_medium_beginning` | `ma_contextual_anomaly_beginning_53.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_medium_end` | `ma_contextual_anomaly_end_586.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_medium_middle` | `ma_contextual_anomaly_middle_33.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `ma_contextual_anomaly_multiple_994.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_short_beginning` | `ma_contextual_anomaly_beginning_608.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_short_end` | `ma_contextual_anomaly_end_892.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_short_middle` | `ma_contextual_anomaly_middle_968.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `white_noise_contextual_anomaly_multiple_108.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_long_beginning` | `white_noise_contextual_anomaly_beginning_725.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_long_end` | `white_noise_contextual_anomaly_end_763.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_long_middle` | `white_noise_contextual_anomaly_middle_203.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `white_noise_contextual_anomaly_multiple_727.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_medium_beginning` | `white_noise_contextual_anomaly_beginning_914.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_medium_end` | `white_noise_contextual_anomaly_end_593.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_medium_middle` | `white_noise_contextual_anomaly_middle_790.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `white_noise_contextual_anomaly_multiple_344.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_short_beginning` | `white_noise_contextual_anomaly_beginning_807.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_short_end` | `white_noise_contextual_anomaly_end_69.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_short_middle` | `white_noise_contextual_anomaly_middle_411.csv` | `stationary + contextual_anomaly` | `stationary + contextual_anomaly` | ✓ FULL |
---

## Grup 7: mean_shift
**Beklenen:** `stationary + mean_shift`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `multiple` | `ar_mean_shift_200.csv` | `stationary + mean_shift` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `ar_mean_shift_369.csv` | `stationary + mean_shift` | `stationary` | ~ PARTIAL |
| `end` | `ar_mean_shift_5.csv` | `stationary + mean_shift` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `ar_mean_shift_243.csv` | `stationary + mean_shift` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `ar_mean_shift_516.csv` | `stationary + mean_shift` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `ar_mean_shift_1000.csv` | `stationary + mean_shift` | `stationary + mean_shift` | ✓ FULL |
| `end` | `ar_mean_shift_978.csv` | `stationary + mean_shift` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `ar_mean_shift_764.csv` | `stationary + mean_shift` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `multiple` | `ar_mean_shift_905.csv` | `stationary + mean_shift` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `beginning` | `ar_mean_shift_761.csv` | `stationary + mean_shift` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `end` | `ar_mean_shift_340.csv` | `stationary + mean_shift` | `stationary + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `middle` | `ar_mean_shift_995.csv` | `stationary + mean_shift` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `multiple` | `arma_mean_shift_56.csv` | `stationary + mean_shift` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `arma_mean_shift_800.csv` | `stationary + mean_shift` | `stationary + mean_shift` | ✓ FULL |
| `end` | `arma_mean_shift_262.csv` | `stationary + mean_shift` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `arma_mean_shift_566.csv` | `stationary + mean_shift` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `arma_mean_shift_94.csv` | `stationary + mean_shift` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `beginning` | `arma_mean_shift_196.csv` | `stationary + mean_shift` | `stationary + mean_shift` | ✓ FULL |
| `end` | `arma_mean_shift_900.csv` | `stationary + mean_shift` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `arma_mean_shift_675.csv` | `stationary + mean_shift` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `arma_mean_shift_373.csv` | `stationary + mean_shift` | `stationary + collective_anomaly + point_anomaly + trend_shift` | ~ PARTIAL |
| `beginning` | `arma_mean_shift_874.csv` | `stationary + mean_shift` | `stationary + variance_shift` | ~ PARTIAL |
| `end` | `arma_mean_shift_688.csv` | `stationary + mean_shift` | `stochastic_trend` | ✗ NONE |
| `middle` | `arma_mean_shift_566.csv` | `stationary + mean_shift` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `ma_mean_shift_66.csv` | `stationary + mean_shift` | `stationary + mean_shift + variance_shift` | ✓ FULL |
| `beginning` | `ma_mean_shift_281.csv` | `stationary + mean_shift` | `stationary + mean_shift` | ✓ FULL |
| `end` | `ma_mean_shift_239.csv` | `stationary + mean_shift` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `ma_mean_shift_442.csv` | `stationary + mean_shift` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `ma_mean_shift_800.csv` | `stationary + mean_shift` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `ma_mean_shift_247.csv` | `stationary + mean_shift` | `stationary + collective_anomaly + mean_shift + point_anomaly` | ✓ FULL |
| `end` | `ma_mean_shift_596.csv` | `stationary + mean_shift` | `stationary + mean_shift + variance_shift` | ✓ FULL |
| `middle` | `ma_mean_shift_978.csv` | `stationary + mean_shift` | `stationary + mean_shift + variance_shift` | ✓ FULL |
| `multiple` | `ma_mean_shift_816.csv` | `stationary + mean_shift` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `beginning` | `ma_mean_shift_949.csv` | `stationary + mean_shift` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `end` | `ma_mean_shift_588.csv` | `stationary + mean_shift` | `volatility + mean_shift` | ~ PARTIAL |
| `middle` | `ma_mean_shift_945.csv` | `stationary + mean_shift` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `white_noise_mean_shift_1.csv` | `stationary + mean_shift` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `white_noise_mean_shift_650.csv` | `stationary + mean_shift` | `stationary + mean_shift` | ✓ FULL |
| `end` | `white_noise_mean_shift_397.csv` | `stationary + mean_shift` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `white_noise_mean_shift_549.csv` | `stationary + mean_shift` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `white_noise_mean_shift_115.csv` | `stationary + mean_shift` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `white_noise_mean_shift_200.csv` | `stationary + mean_shift` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `end` | `white_noise_mean_shift_955.csv` | `stationary + mean_shift` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `white_noise_mean_shift_432.csv` | `stationary + mean_shift` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `white_noise_mean_shift_908.csv` | `stationary + mean_shift` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `white_noise_mean_shift_865.csv` | `stationary + mean_shift` | `stationary` | ~ PARTIAL |
| `end` | `white_noise_mean_shift_842.csv` | `stationary + mean_shift` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `white_noise_mean_shift_381.csv` | `stationary + mean_shift` | `stationary + mean_shift + trend_shift` | ✓ FULL |
---

## Grup 8: point_anomaly
**Beklenen:** `stationary + point_anomaly`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `multiple` | `ar_point_anomaly_multiple_319.csv` | `stationary + point_anomaly` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `ar_point_anomaly_single_beginning_151.csv` | `stationary + point_anomaly` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `ar_point_anomaly_single_end_32.csv` | `stationary + point_anomaly` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `ar_point_anomaly_single_middle_908.csv` | `stationary + point_anomaly` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `ar_point_anomaly_multiple_620.csv` | `stationary + point_anomaly` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `beginning` | `ar_point_anomaly_single_beginning_971.csv` | `stationary + point_anomaly` | `stationary + collective_anomaly + mean_shift` | ~ PARTIAL |
| `end` | `ar_point_anomaly_single_end_170.csv` | `stationary + point_anomaly` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `ar_point_anomaly_single_middle_177.csv` | `stationary + point_anomaly` | `stationary + mean_shift` | ~ PARTIAL |
| `multiple` | `ar_point_anomaly_multiple_773.csv` | `stationary + point_anomaly` | `stationary + point_anomaly + trend_shift` | ✓ FULL |
| `beginning` | `ar_point_anomaly_single_beginning_546.csv` | `stationary + point_anomaly` | `stationary + collective_anomaly` | ~ PARTIAL |
| `end` | `ar_point_anomaly_single_end_850.csv` | `stationary + point_anomaly` | `volatility + collective_anomaly` | ✗ NONE |
| `middle` | `ar_point_anomaly_single_middle_161.csv` | `stationary + point_anomaly` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `arma_point_anomaly_multiple_8.csv` | `stationary + point_anomaly` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `arma_point_anomaly_single_beginning_59.csv` | `stationary + point_anomaly` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `arma_point_anomaly_single_end_804.csv` | `stationary + point_anomaly` | `stationary` | ~ PARTIAL |
| `middle` | `arma_point_anomaly_single_middle_213.csv` | `stationary + point_anomaly` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `arma_point_anomaly_multiple_216.csv` | `stationary + point_anomaly` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `beginning` | `arma_point_anomaly_single_beginning_706.csv` | `stationary + point_anomaly` | `stationary + collective_anomaly` | ~ PARTIAL |
| `end` | `arma_point_anomaly_single_end_536.csv` | `stationary + point_anomaly` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `arma_point_anomaly_single_middle_971.csv` | `stationary + point_anomaly` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `arma_point_anomaly_multiple_604.csv` | `stationary + point_anomaly` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `arma_point_anomaly_single_beginning_250.csv` | `stationary + point_anomaly` | `volatility + point_anomaly` | ~ PARTIAL |
| `end` | `arma_point_anomaly_single_end_342.csv` | `stationary + point_anomaly` | `stationary + collective_anomaly` | ~ PARTIAL |
| `middle` | `arma_point_anomaly_single_middle_585.csv` | `stationary + point_anomaly` | `stationary + mean_shift` | ~ PARTIAL |
| `multiple` | `ma_point_anomaly_multiple_902.csv` | `stationary + point_anomaly` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `ma_point_anomaly_single_beginning_658.csv` | `stationary + point_anomaly` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `ma_point_anomaly_single_end_489.csv` | `stationary + point_anomaly` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `ma_point_anomaly_single_middle_988.csv` | `stationary + point_anomaly` | `stationary` | ~ PARTIAL |
| `multiple` | `ma_point_anomaly_multiple_293.csv` | `stationary + point_anomaly` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `beginning` | `ma_point_anomaly_single_beginning_955.csv` | `stationary + point_anomaly` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `ma_point_anomaly_single_end_596.csv` | `stationary + point_anomaly` | `stationary` | ~ PARTIAL |
| `middle` | `ma_point_anomaly_single_middle_795.csv` | `stationary + point_anomaly` | `stationary + collective_anomaly` | ~ PARTIAL |
| `multiple` | `ma_point_anomaly_multiple_771.csv` | `stationary + point_anomaly` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `beginning` | `ma_point_anomaly_single_beginning_734.csv` | `stationary + point_anomaly` | `stationary + collective_anomaly` | ~ PARTIAL |
| `end` | `ma_point_anomaly_single_end_283.csv` | `stationary + point_anomaly` | `volatility + mean_shift` | ✗ NONE |
| `middle` | `ma_point_anomaly_single_middle_756.csv` | `stationary + point_anomaly` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `white_noise_point_anomaly_multiple_386.csv` | `stationary + point_anomaly` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `white_noise_point_anomaly_single_beginning_466.csv` | `stationary + point_anomaly` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `white_noise_point_anomaly_single_end_717.csv` | `stationary + point_anomaly` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `white_noise_point_anomaly_single_middle_698.csv` | `stationary + point_anomaly` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `white_noise_point_anomaly_multiple_442.csv` | `stationary + point_anomaly` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `white_noise_point_anomaly_single_beginning_501.csv` | `stationary + point_anomaly` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `white_noise_point_anomaly_single_end_928.csv` | `stationary + point_anomaly` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `white_noise_point_anomaly_single_middle_575.csv` | `stationary + point_anomaly` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `white_noise_point_anomaly_multiple_514.csv` | `stationary + point_anomaly` | `volatility + collective_anomaly + mean_shift + trend_shift` | ✗ NONE |
| `beginning` | `white_noise_point_anomaly_single_beginning_209.csv` | `stationary + point_anomaly` | `stationary + collective_anomaly + mean_shift + point_anomaly` | ✓ FULL |
| `end` | `white_noise_point_anomaly_single_end_326.csv` | `stationary + point_anomaly` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ~ PARTIAL |
| `middle` | `white_noise_point_anomaly_single_middle_305.csv` | `stationary + point_anomaly` | `volatility + collective_anomaly + mean_shift + trend_shift` | ✗ NONE |
---

## Grup 9: trend_shift
**Beklenen:** `stationary + trend_shift`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `multiple` | `ar_trend_shift_157.csv` | `stationary + trend_shift` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ar_trend_shift_41.csv` | `stationary + trend_shift` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ar_trend_shift_117.csv` | `stationary + trend_shift` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ar_trend_shift_640.csv` | `stationary + trend_shift` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ar_trend_shift_609.csv` | `stationary + trend_shift` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `beginning` | `ar_trend_shift_31.csv` | `stationary + trend_shift` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ar_trend_shift_640.csv` | `stationary + trend_shift` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ar_trend_shift_300.csv` | `stationary + trend_shift` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `multiple` | `ar_trend_shift_104.csv` | `stationary + trend_shift` | `stationary + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `beginning` | `ar_trend_shift_163.csv` | `stationary + trend_shift` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `end` | `ar_trend_shift_750.csv` | `stationary + trend_shift` | `stationary + collective_anomaly` | ~ PARTIAL |
| `middle` | `ar_trend_shift_680.csv` | `stationary + trend_shift` | `stochastic_trend + point_anomaly + trend_shift` | ~ PARTIAL |
| `multiple` | `arma_trend_shift_152.csv` | `stationary + trend_shift` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `arma_trend_shift_309.csv` | `stationary + trend_shift` | `stationary + trend_shift` | ✓ FULL |
| `end` | `arma_trend_shift_160.csv` | `stationary + trend_shift` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `arma_trend_shift_933.csv` | `stationary + trend_shift` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `arma_trend_shift_127.csv` | `stationary + trend_shift` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `arma_trend_shift_891.csv` | `stationary + trend_shift` | `stationary + trend_shift` | ✓ FULL |
| `end` | `arma_trend_shift_402.csv` | `stationary + trend_shift` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `arma_trend_shift_163.csv` | `stationary + trend_shift` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `multiple` | `arma_trend_shift_572.csv` | `stationary + trend_shift` | `stationary + point_anomaly + trend_shift` | ✓ FULL |
| `beginning` | `arma_trend_shift_317.csv` | `stationary + trend_shift` | `stationary + point_anomaly + trend_shift` | ✓ FULL |
| `end` | `arma_trend_shift_355.csv` | `stationary + trend_shift` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `middle` | `arma_trend_shift_715.csv` | `stationary + trend_shift` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ma_trend_shift_546.csv` | `stationary + trend_shift` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ma_trend_shift_296.csv` | `stationary + trend_shift` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ma_trend_shift_596.csv` | `stationary + trend_shift` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ma_trend_shift_22.csv` | `stationary + trend_shift` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ma_trend_shift_765.csv` | `stationary + trend_shift` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ma_trend_shift_960.csv` | `stationary + trend_shift` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ma_trend_shift_911.csv` | `stationary + trend_shift` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ma_trend_shift_624.csv` | `stationary + trend_shift` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ma_trend_shift_63.csv` | `stationary + trend_shift` | `stationary + mean_shift + point_anomaly + trend_shift` | ✓ FULL |
| `beginning` | `ma_trend_shift_534.csv` | `stationary + trend_shift` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ma_trend_shift_321.csv` | `stationary + trend_shift` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ma_trend_shift_821.csv` | `stationary + trend_shift` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `white_noise_trend_shift_534.csv` | `stationary + trend_shift` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `white_noise_trend_shift_842.csv` | `stationary + trend_shift` | `stationary + trend_shift` | ✓ FULL |
| `end` | `white_noise_trend_shift_473.csv` | `stationary + trend_shift` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `white_noise_trend_shift_273.csv` | `stationary + trend_shift` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `white_noise_trend_shift_185.csv` | `stationary + trend_shift` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `white_noise_trend_shift_188.csv` | `stationary + trend_shift` | `stationary + trend_shift` | ✓ FULL |
| `end` | `white_noise_trend_shift_705.csv` | `stationary + trend_shift` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `middle` | `white_noise_trend_shift_496.csv` | `stationary + trend_shift` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `white_noise_trend_shift_424.csv` | `stationary + trend_shift` | `stationary + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `beginning` | `white_noise_trend_shift_489.csv` | `stationary + trend_shift` | `stationary + trend_shift` | ✓ FULL |
| `end` | `white_noise_trend_shift_477.csv` | `stationary + trend_shift` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `middle` | `white_noise_trend_shift_529.csv` | `stationary + trend_shift` | `stationary + point_anomaly` | ~ PARTIAL |
---

## Grup 10: variance_shift
**Beklenen:** `stationary + variance_shift`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `multiple` | `ar_variance_shift_895.csv` | `stationary + variance_shift` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `ar_variance_shift_770.csv` | `stationary + variance_shift` | `stationary + variance_shift` | ✓ FULL |
| `end` | `ar_variance_shift_148.csv` | `stationary + variance_shift` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `ar_variance_shift_719.csv` | `stationary + variance_shift` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `ar_variance_shift_700.csv` | `stationary + variance_shift` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `ar_variance_shift_694.csv` | `stationary + variance_shift` | `stationary + variance_shift` | ✓ FULL |
| `end` | `ar_variance_shift_189.csv` | `stationary + variance_shift` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `ar_variance_shift_154.csv` | `stationary + variance_shift` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `ar_variance_shift_47.csv` | `stationary + variance_shift` | `volatility + variance_shift` | ~ PARTIAL |
| `beginning` | `ar_variance_shift_77.csv` | `stationary + variance_shift` | `stationary + collective_anomaly` | ~ PARTIAL |
| `end` | `ar_variance_shift_410.csv` | `stationary + variance_shift` | `volatility + point_anomaly` | ✗ NONE |
| `middle` | `ar_variance_shift_836.csv` | `stationary + variance_shift` | `stationary + mean_shift + variance_shift` | ✓ FULL |
| `multiple` | `arma_variance_shift_893.csv` | `stationary + variance_shift` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `arma_variance_shift_199.csv` | `stationary + variance_shift` | `stationary + variance_shift` | ✓ FULL |
| `end` | `arma_variance_shift_327.csv` | `stationary + variance_shift` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `arma_variance_shift_275.csv` | `stationary + variance_shift` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `arma_variance_shift_273.csv` | `stationary + variance_shift` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `arma_variance_shift_593.csv` | `stationary + variance_shift` | `stationary + variance_shift` | ✓ FULL |
| `end` | `arma_variance_shift_511.csv` | `stationary + variance_shift` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `arma_variance_shift_227.csv` | `stationary + variance_shift` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `arma_variance_shift_488.csv` | `stationary + variance_shift` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `arma_variance_shift_267.csv` | `stationary + variance_shift` | `stationary + collective_anomaly + point_anomaly + variance_shift` | ✓ FULL |
| `end` | `arma_variance_shift_355.csv` | `stationary + variance_shift` | `volatility + variance_shift` | ~ PARTIAL |
| `middle` | `arma_variance_shift_524.csv` | `stationary + variance_shift` | `volatility + variance_shift` | ~ PARTIAL |
| `multiple` | `ma_variance_shift_328.csv` | `stationary + variance_shift` | `stationary + collective_anomaly + mean_shift + variance_shift` | ✓ FULL |
| `beginning` | `ma_variance_shift_904.csv` | `stationary + variance_shift` | `stationary` | ~ PARTIAL |
| `end` | `ma_variance_shift_95.csv` | `stationary + variance_shift` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `middle` | `ma_variance_shift_168.csv` | `stationary + variance_shift` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `ma_variance_shift_506.csv` | `stationary + variance_shift` | `stationary + collective_anomaly` | ~ PARTIAL |
| `beginning` | `ma_variance_shift_843.csv` | `stationary + variance_shift` | `stationary + variance_shift` | ✓ FULL |
| `end` | `ma_variance_shift_893.csv` | `stationary + variance_shift` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `middle` | `ma_variance_shift_888.csv` | `stationary + variance_shift` | `volatility + variance_shift` | ~ PARTIAL |
| `multiple` | `ma_variance_shift_605.csv` | `stationary + variance_shift` | `volatility + variance_shift` | ~ PARTIAL |
| `beginning` | `ma_variance_shift_189.csv` | `stationary + variance_shift` | `volatility + collective_anomaly` | ✗ NONE |
| `end` | `ma_variance_shift_144.csv` | `stationary + variance_shift` | `stationary + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `middle` | `ma_variance_shift_7.csv` | `stationary + variance_shift` | `stationary + mean_shift + variance_shift` | ✓ FULL |
| `multiple` | `white_noise_variance_shift_597.csv` | `stationary + variance_shift` | `volatility + variance_shift` | ~ PARTIAL |
| `beginning` | `white_noise_variance_shift_87.csv` | `stationary + variance_shift` | `stationary + variance_shift` | ✓ FULL |
| `end` | `white_noise_variance_shift_111.csv` | `stationary + variance_shift` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `white_noise_variance_shift_992.csv` | `stationary + variance_shift` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `white_noise_variance_shift_184.csv` | `stationary + variance_shift` | `stationary + mean_shift` | ~ PARTIAL |
| `beginning` | `white_noise_variance_shift_952.csv` | `stationary + variance_shift` | `stationary + variance_shift` | ✓ FULL |
| `end` | `white_noise_variance_shift_793.csv` | `stationary + variance_shift` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `white_noise_variance_shift_881.csv` | `stationary + variance_shift` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `white_noise_variance_shift_316.csv` | `stationary + variance_shift` | `volatility + variance_shift` | ~ PARTIAL |
| `beginning` | `white_noise_variance_shift_251.csv` | `stationary + variance_shift` | `volatility + point_anomaly + variance_shift` | ~ PARTIAL |
| `end` | `white_noise_variance_shift_473.csv` | `stationary + variance_shift` | `volatility + collective_anomaly` | ✗ NONE |
| `middle` | `white_noise_variance_shift_546.csv` | `stationary + variance_shift` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
---

## Grup 11: cubic+collective
**Beklenen:** `deterministic_trend + collective_anomaly`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `data` | `cubic_collective_ar_242.csv` | `deterministic_trend + collective_anomaly` | `deterministic_trend + collective_anomaly` | ✓ FULL |
---

## Grup 12: cubic+mean_shift
**Beklenen:** `deterministic_trend + mean_shift`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `data` | `cubic_meanshift1_arma_213.csv` | `deterministic_trend + mean_shift` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `cubic_meanshift2_white_noise_135.csv` | `deterministic_trend + mean_shift` | `deterministic_trend + mean_shift` | ✓ FULL |
---

## Grup 13: cubic+point_anomaly
**Beklenen:** `deterministic_trend + point_anomaly`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `data` | `cubic_point_ar_160.csv` | `deterministic_trend + point_anomaly` | `deterministic_trend + point_anomaly` | ✓ FULL |
---

## Grup 14: cubic+variance_shift
**Beklenen:** `deterministic_trend + variance_shift`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `data` | `cubic_varshift_white_noise_174.csv` | `deterministic_trend + variance_shift` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
---

## Grup 15: damped+collective
**Beklenen:** `deterministic_trend + collective_anomaly`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `data` | `damped_collective_arma_060.csv` | `deterministic_trend + collective_anomaly` | `deterministic_trend + collective_anomaly` | ✓ FULL |
---

## Grup 16: damped+mean_shift
**Beklenen:** `deterministic_trend + mean_shift`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `data` | `damped_meanshift1_arma_168.csv` | `deterministic_trend + mean_shift` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `damped_meanshift2_ar_138.csv` | `deterministic_trend + mean_shift` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
---

## Grup 17: damped+point_anomaly
**Beklenen:** `deterministic_trend + point_anomaly`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `data` | `damped_point_arma_002.csv` | `deterministic_trend + point_anomaly` | `deterministic_trend + point_anomaly` | ✓ FULL |
---

## Grup 18: damped+variance_shift
**Beklenen:** `deterministic_trend + variance_shift`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `data` | `damped_varshift_ar_149.csv` | `deterministic_trend + variance_shift` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
---

## Grup 19: exp+collective
**Beklenen:** `deterministic_trend + collective_anomaly`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `data` | `exp_collective_ar_021.csv` | `deterministic_trend + collective_anomaly` | `deterministic_trend + collective_anomaly` | ✓ FULL |
---

## Grup 20: exp+mean_shift
**Beklenen:** `deterministic_trend + mean_shift`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `data` | `exp_meanshift1_white_noise_198.csv` | `deterministic_trend + mean_shift` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `exp_meanshift2_white_noise_052.csv` | `deterministic_trend + mean_shift` | `deterministic_trend + mean_shift` | ✓ FULL |
---

## Grup 21: exp+point_anomaly
**Beklenen:** `deterministic_trend + point_anomaly`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `data` | `exp_point_white_noise_053.csv` | `deterministic_trend + point_anomaly` | `deterministic_trend + point_anomaly` | ✓ FULL |
---

## Grup 22: exp+variance_shift
**Beklenen:** `deterministic_trend + variance_shift`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `data` | `exp_varshift_ar_215.csv` | `deterministic_trend + variance_shift` | `deterministic_trend + variance_shift` | ✓ FULL |
---

## Grup 23: linear+collective
**Beklenen:** `deterministic_trend + collective_anomaly`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `data` | `linear_collective_ar_down_084.csv` | `deterministic_trend + collective_anomaly` | `deterministic_trend + collective_anomaly` | ✓ FULL |
---

## Grup 24: linear+mean_shift
**Beklenen:** `deterministic_trend + mean_shift`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `data` | `linear_meanshift1_ar_up_058.csv` | `deterministic_trend + mean_shift` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `linear_meanshift2_ma_up_088.csv` | `deterministic_trend + mean_shift` | `deterministic_trend + mean_shift` | ✓ FULL |
---

## Grup 25: linear+point_anomaly
**Beklenen:** `deterministic_trend + point_anomaly`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `data` | `linear_point_white_noise_up_210.csv` | `deterministic_trend + point_anomaly` | `deterministic_trend + point_anomaly` | ✓ FULL |
---

## Grup 26: linear+trend_shift
**Beklenen:** `deterministic_trend + trend_shift`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `data` | `trendshift_direction_and_magnitude_change_ma_up_123.csv` | `deterministic_trend + trend_shift` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_change_white_noise_down_052.csv` | `deterministic_trend + trend_shift` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_magnitude_change_ma_down_069.csv` | `deterministic_trend + trend_shift` | `deterministic_trend + trend_shift` | ✓ FULL |
---

## Grup 27: linear+variance_shift
**Beklenen:** `deterministic_trend + variance_shift`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `data` | `linear_varshift1_ma_up_051.csv` | `deterministic_trend + variance_shift` | `deterministic_trend + variance_shift` | ✓ FULL |
---

## Grup 28: quad+collective
**Beklenen:** `deterministic_trend + collective_anomaly`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `data` | `quadratic_collective_ma_235.csv` | `deterministic_trend + collective_anomaly` | `deterministic_trend + collective_anomaly` | ✓ FULL |
---

## Grup 29: quad+mean_shift
**Beklenen:** `deterministic_trend + mean_shift`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `data` | `quadratic_meanshift1_ar_248.csv` | `deterministic_trend + mean_shift` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `quadratic_meanshift2_arma_158.csv` | `deterministic_trend + mean_shift` | `deterministic_trend + mean_shift` | ✓ FULL |
---

## Grup 30: quad+point_anomaly
**Beklenen:** `deterministic_trend + point_anomaly`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `data` | `quadratic_point_arma_194.csv` | `deterministic_trend + point_anomaly` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_ar_053.csv` | `deterministic_trend + point_anomaly` | `deterministic_trend + point_anomaly` | ✓ FULL |
---

## Grup 31: quad+variance_shift
**Beklenen:** `deterministic_trend + variance_shift`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `data` | `quadratic_varshift_arma_222.csv` | `deterministic_trend + variance_shift` | `deterministic_trend + variance_shift` | ✓ FULL |
---

## Grup 32: stoch+collective
**Beklenen:** `stochastic_trend + collective_anomaly`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `Stochastic Trend + Collective Anomaly` | `rwd_single_collective_anomaly_middle_991.csv` | `stochastic_trend + collective_anomaly` | `stochastic_trend + collective_anomaly + mean_shift` | ✓ FULL |
---

## Grup 33: stoch+mean_shift
**Beklenen:** `stochastic_trend + mean_shift`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `Stochastic Trend + Mean Shift` | `rwd_single_mean_shift_increase_middle_151.csv` | `stochastic_trend + mean_shift` | `stochastic_trend + mean_shift` | ✓ FULL |
---

## Grup 34: stoch+point_anomaly
**Beklenen:** `stochastic_trend + point_anomaly`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `Stochastic Trend + Point Anomaly` | `rwd_single_point_anomaly_middle_632.csv` | `stochastic_trend + point_anomaly` | `stochastic_trend + collective_anomaly + point_anomaly` | ✓ FULL |
---

## Grup 35: stoch+variance_shift
**Beklenen:** `stochastic_trend + variance_shift`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `ARI + Variance Shift` | `ari_single_variance_shift_increase_middle_122.csv` | `stochastic_trend + variance_shift` | `stochastic_trend + variance_shift` | ✓ FULL |
| `ARIMA + Variance Shift` | `arima_single_variance_shift_increase_beginning_496.csv` | `stochastic_trend + variance_shift` | `stochastic_trend + variance_shift` | ✓ FULL |
| `IMA + Variance Shift` | `ima_multiple_variance_shifts_548.csv` | `stochastic_trend + variance_shift` | `stochastic_trend + trend_shift + variance_shift` | ✓ FULL |
| `RW + Variance Shift` | `rw_single_variance_shift_increase_middle_212.csv` | `stochastic_trend + variance_shift` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RWD + Variance Shift` | `rwd_single_variance_shift_decrease_end_610.csv` | `stochastic_trend + variance_shift` | `stochastic_trend + variance_shift` | ✓ FULL |
---

## Grup 36: vol+collective
**Beklenen:** `volatility + collective_anomaly`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `Volatility + Collective Anomaly` | `garch_single_collective_anomaly_middle_150.csv` | `volatility + collective_anomaly` | `stationary + collective_anomaly + variance_shift` | ~ PARTIAL |
---

## Grup 37: vol+mean_shift
**Beklenen:** `volatility + mean_shift`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `Volatility + Mean Shift` | `garch_single_mean_shift_increase_middle_144.csv` | `volatility + mean_shift` | `stationary + mean_shift` | ~ PARTIAL |
---

## Grup 38: vol+point_anomaly
**Beklenen:** `volatility + point_anomaly`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `Volatility + Point Anomaly` | `garch_single_point_anomaly_middle_637.csv` | `volatility + point_anomaly` | `volatility + collective_anomaly + point_anomaly` | ✓ FULL |
---

## Grup 39: vol+variance_shift
**Beklenen:** `volatility + variance_shift`

| Leaf Klasör | CSV | Beklenen | Tahmin | Sonuç |
|---|---|---|---|---|
| `Volatility + Variance Shift` | `garch_single_variance_shift_increase_middle_538.csv` | `volatility + variance_shift` | `volatility + variance_shift` | ✓ FULL |

---

## Model Olasılıkları — Sadece Hatalı Örnekler

| Grup | CSV | stationary | det_trend | stoch_trend | volatility | collective | contextual | mean_shift | point | trend_shift | var_shift | Sonuç |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| stationary | `ar_28856.csv` | 1.00 | 0.00 | 0.00 | 0.01 | 0.04 | 0.00 | 0.07 | 0.97 | 0.00 | 0.01 | PARTIAL |
| stationary | `ar_10735.csv` | 1.00 | 0.00 | 0.01 | 0.36 | 0.86 | 0.00 | 0.27 | 0.08 | 0.01 | 0.15 | PARTIAL |
| stationary | `arma_18109.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.36 | 0.00 | 0.00 | 0.88 | 0.00 | 0.08 | PARTIAL |
| stationary | `arma_1722.csv` | 0.99 | 0.00 | 0.04 | 0.03 | 0.76 | 0.00 | 0.00 | 0.07 | 0.00 | 0.20 | PARTIAL |
| stationary | `ma_16581.csv` | 1.00 | 0.00 | 0.00 | 0.02 | 0.06 | 0.00 | 0.08 | 0.85 | 0.00 | 0.00 | PARTIAL |
| stationary | `ma_14112.csv` | 1.00 | 0.00 | 0.00 | 0.02 | 0.16 | 0.00 | 0.01 | 0.71 | 0.00 | 0.04 | PARTIAL |
| stationary | `ma_31717.csv` | 0.93 | 0.00 | 0.25 | 0.16 | 0.90 | 0.00 | 0.04 | 0.79 | 0.00 | 0.04 | PARTIAL |
| stationary | `wn_31841.csv` | 0.99 | 0.00 | 0.00 | 0.93 | 0.64 | 0.00 | 0.00 | 0.38 | 0.00 | 0.01 | PARTIAL |
| deterministic_trend | `ar_cubic_trend_920.csv` | 0.98 | 0.11 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.99 | 0.01 | NONE |
| deterministic_trend | `ar_cubic_trend_600.csv` | 0.19 | 0.00 | 0.80 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.98 | 0.00 | NONE |
| deterministic_trend | `ar_cubic_trend_179.csv` | 0.00 | 0.01 | 0.01 | 0.00 | 0.05 | 0.00 | 0.46 | 0.08 | 0.80 | 0.00 | NONE |
| deterministic_trend | `ar_exponential_trend_184.csv` | 0.90 | 0.78 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 | NONE |
| deterministic_trend | `ar_exponential_trend_3.csv` | 0.01 | 0.82 | 0.00 | 0.00 | 0.04 | 0.00 | 0.04 | 0.00 | 0.54 | 0.00 | PARTIAL |
| deterministic_trend | `ar_linear_down_trend_312.csv` | 0.91 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.63 | 0.02 | PARTIAL |
| deterministic_trend | `ar_linear_down_trend_564.csv` | 0.69 | 0.01 | 0.97 | 0.00 | 0.00 | 0.00 | 0.90 | 0.00 | 0.66 | 0.00 | NONE |
| deterministic_trend | `ar_linear_down_trend_653.csv` | 0.02 | 0.94 | 0.00 | 0.00 | 0.01 | 0.00 | 0.10 | 0.00 | 0.97 | 0.00 | PARTIAL |
| deterministic_trend | `ar_linear_up_trend_122.csv` | 0.80 | 0.59 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.86 | 0.05 | NONE |
| deterministic_trend | `ar_linear_up_trend_615.csv` | 0.29 | 0.03 | 0.90 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.97 | 0.00 | NONE |
| deterministic_trend | `ar_linear_up_trend_281.csv` | 0.00 | 0.35 | 0.01 | 0.00 | 0.01 | 0.00 | 0.82 | 0.74 | 0.27 | 0.00 | PARTIAL |
| deterministic_trend | `ar_quadratic_trend_759.csv` | 0.06 | 1.00 | 0.00 | 0.00 | 0.76 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | PARTIAL |
| deterministic_trend | `ar_quadratic_trend_698.csv` | 0.61 | 0.99 | 0.00 | 0.00 | 0.63 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | PARTIAL |
| deterministic_trend | `ar_quadratic_trend_745.csv` | 0.93 | 0.02 | 0.00 | 0.05 | 0.14 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | NONE |
| deterministic_trend | `arma_cubic_trend_600.csv` | 0.89 | 0.66 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.03 | 0.49 | 0.05 | NONE |
| deterministic_trend | `arma_cubic_trend_485.csv` | 0.50 | 0.60 | 1.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.02 | 0.00 | 0.01 | NONE |
| deterministic_trend | `arma_cubic_trend_300.csv` | 0.01 | 0.00 | 1.00 | 0.00 | 0.05 | 0.00 | 0.12 | 0.03 | 0.00 | 0.00 | NONE |
| deterministic_trend | `arma_linear_down_trend_799.csv` | 0.52 | 0.77 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.97 | 0.03 | PARTIAL |
| deterministic_trend | `arma_linear_down_trend_841.csv` | 0.82 | 0.63 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 | NONE |
| deterministic_trend | `arma_linear_down_trend_245.csv` | 0.06 | 0.65 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.98 | 0.01 | PARTIAL |
| deterministic_trend | `arma_linear_up_trend_741.csv` | 0.99 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 | NONE |
| deterministic_trend | `arma_linear_up_trend_488.csv` | 0.49 | 0.99 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 1.00 | 0.00 | PARTIAL |
| deterministic_trend | `arma_linear_up_trend_411.csv` | 0.05 | 0.48 | 0.01 | 0.00 | 0.01 | 0.00 | 0.12 | 0.18 | 0.87 | 0.00 | PARTIAL |
| deterministic_trend | `arma_quadratic_trend_354.csv` | 0.82 | 1.00 | 0.00 | 0.00 | 0.53 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | PARTIAL |
| deterministic_trend | `ma_cubic_trend_981.csv` | 0.91 | 0.71 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.01 | 0.10 | NONE |
| deterministic_trend | `ma_cubic_trend_801.csv` | 0.09 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.75 | 0.00 | NONE |
| deterministic_trend | `ma_cubic_trend_408.csv` | 0.01 | 0.00 | 0.45 | 0.00 | 0.05 | 0.00 | 0.91 | 0.02 | 0.84 | 0.00 | NONE |
| deterministic_trend | `ma_exponential_trend_429.csv` | 0.98 | 0.59 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 | NONE |
| deterministic_trend | `ma_exponential_trend_88.csv` | 0.01 | 0.96 | 0.26 | 0.00 | 0.07 | 0.00 | 0.01 | 0.00 | 0.86 | 0.00 | PARTIAL |
| deterministic_trend | `ma_linear_down_trend_415.csv` | 0.96 | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.99 | 0.02 | NONE |
| deterministic_trend | `ma_linear_down_trend_655.csv` | 0.19 | 0.99 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 | PARTIAL |
| deterministic_trend | `ma_linear_down_trend_341.csv` | 0.75 | 0.66 | 0.00 | 0.00 | 0.01 | 0.00 | 0.17 | 0.00 | 1.00 | 0.00 | NONE |
| deterministic_trend | `ma_linear_up_trend_842.csv` | 0.60 | 0.36 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.23 | NONE |
| deterministic_trend | `ma_linear_up_trend_138.csv` | 0.61 | 0.99 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 1.00 | 0.00 | PARTIAL |
| deterministic_trend | `ma_linear_up_trend_771.csv` | 0.05 | 0.24 | 0.00 | 0.00 | 0.02 | 0.00 | 0.24 | 0.17 | 1.00 | 0.00 | PARTIAL |
| deterministic_trend | `ma_quadratic_trend_521.csv` | 0.09 | 0.21 | 0.00 | 0.00 | 0.50 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | PARTIAL |
| deterministic_trend | `ma_quadratic_trend_593.csv` | 0.01 | 0.97 | 0.00 | 0.00 | 0.68 | 0.00 | 0.00 | 0.50 | 0.00 | 0.00 | PARTIAL |
| deterministic_trend | `ma_quadratic_trend_212.csv` | 0.98 | 0.01 | 0.00 | 0.07 | 0.38 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | NONE |
| deterministic_trend | `white_noise_cubic_trend_996.csv` | 0.91 | 0.62 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.07 | 0.06 | NONE |
| deterministic_trend | `white_noise_cubic_trend_949.csv` | 0.39 | 0.69 | 0.12 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.97 | 0.00 | PARTIAL |
| deterministic_trend | `white_noise_cubic_trend_447.csv` | 0.38 | 0.03 | 0.99 | 0.00 | 0.04 | 0.00 | 0.32 | 0.48 | 1.00 | 0.01 | NONE |
| deterministic_trend | `white_noise_exponential_trend_669.csv` | 0.00 | 0.96 | 0.43 | 0.00 | 0.09 | 0.00 | 0.02 | 0.00 | 0.51 | 0.00 | PARTIAL |
| deterministic_trend | `white_noise_linear_down_trend_914.csv` | 0.95 | 0.70 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.01 | NONE |
| deterministic_trend | `white_noise_linear_down_trend_893.csv` | 0.60 | 0.99 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 | PARTIAL |
| deterministic_trend | `white_noise_linear_down_trend_431.csv` | 0.82 | 0.49 | 0.00 | 0.00 | 0.01 | 0.00 | 0.14 | 0.13 | 1.00 | 0.00 | NONE |
| deterministic_trend | `white_noise_linear_up_trend_275.csv` | 0.07 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.20 | 0.99 | 0.02 | PARTIAL |
| deterministic_trend | `white_noise_linear_up_trend_748.csv` | 0.33 | 0.00 | 0.97 | 0.00 | 0.10 | 0.00 | 0.43 | 0.07 | 1.00 | 0.00 | NONE |
| deterministic_trend | `white_noise_quadratic_trend_162.csv` | 0.77 | 0.04 | 0.00 | 0.00 | 0.09 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | NONE |
| stochastic_trend | `ari_308.csv` | 0.02 | 0.00 | 0.99 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.69 | PARTIAL |
| stochastic_trend | `ari_810.csv` | 0.96 | 0.06 | 0.14 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.99 | 0.00 | NONE |
| stochastic_trend | `ari_365.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.24 | 0.00 | 0.85 | 0.00 | 0.00 | 0.01 | PARTIAL |
| stochastic_trend | `arima_171.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.98 | PARTIAL |
| stochastic_trend | `arima_887.csv` | 0.92 | 0.04 | 0.00 | 0.00 | 0.02 | 0.00 | 0.97 | 0.00 | 0.97 | 0.00 | NONE |
| stochastic_trend | `arima_312.csv` | 0.97 | 0.00 | 0.00 | 0.49 | 0.47 | 0.00 | 0.58 | 0.01 | 0.12 | 0.04 | NONE |
| stochastic_trend | `ima_898.csv` | 0.03 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.73 | PARTIAL |
| stochastic_trend | `ima_191.csv` | 0.96 | 0.00 | 1.00 | 0.00 | 0.14 | 0.00 | 0.16 | 0.00 | 0.81 | 0.28 | PARTIAL |
| stochastic_trend | `random_walk_354.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.93 | PARTIAL |
| stochastic_trend | `random_walk_684.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.07 | 0.00 | 0.77 | 0.03 | 0.00 | 0.00 | PARTIAL |
| stochastic_trend | `random_walk_drift_868.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.55 | PARTIAL |
| volatility | `aparch_425.csv` | 0.75 | 0.00 | 0.00 | 0.96 | 0.08 | 0.00 | 0.00 | 0.50 | 0.00 | 0.02 | PARTIAL |
| volatility | `aparch_291.csv` | 0.01 | 0.00 | 0.00 | 1.00 | 0.69 | 0.00 | 0.02 | 0.17 | 0.00 | 0.97 | PARTIAL |
| volatility | `arch_344.csv` | 0.18 | 0.00 | 0.00 | 1.00 | 0.01 | 0.00 | 0.00 | 0.09 | 0.00 | 0.81 | PARTIAL |
| volatility | `arch_745.csv` | 0.00 | 0.00 | 0.00 | 1.00 | 0.09 | 0.00 | 0.00 | 0.15 | 0.00 | 1.00 | PARTIAL |
| volatility | `egarch_728.csv` | 0.96 | 0.00 | 0.00 | 0.93 | 0.16 | 0.00 | 0.01 | 0.79 | 0.00 | 0.05 | NONE |
| volatility | `egarch_696.csv` | 0.23 | 0.00 | 0.00 | 0.99 | 0.58 | 0.00 | 0.01 | 0.15 | 0.06 | 0.08 | PARTIAL |
| volatility | `garch_684.csv` | 0.01 | 0.00 | 0.00 | 1.00 | 0.37 | 0.00 | 0.67 | 0.88 | 0.00 | 0.59 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_770.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.23 | 0.00 | 0.03 | 0.30 | 0.00 | 0.01 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_951.csv` | 0.96 | 0.00 | 1.00 | 0.02 | 0.43 | 0.00 | 0.42 | 0.99 | 0.00 | 0.01 | NONE |
| collective_anomaly | `ar_collective_anomaly_689.csv` | 1.00 | 0.00 | 0.00 | 0.24 | 0.27 | 0.00 | 0.07 | 0.08 | 0.00 | 0.48 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_732.csv` | 1.00 | 0.00 | 0.00 | 0.04 | 0.09 | 0.00 | 0.05 | 0.98 | 0.00 | 0.33 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_73.csv` | 1.00 | 0.00 | 0.00 | 0.02 | 0.27 | 0.00 | 0.34 | 0.10 | 0.00 | 0.82 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_15.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.17 | 0.00 | 0.01 | 0.25 | 0.00 | 0.06 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_840.csv` | 0.02 | 0.00 | 1.00 | 0.00 | 0.82 | 0.00 | 0.82 | 0.18 | 0.00 | 0.01 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_968.csv` | 1.00 | 0.00 | 0.00 | 0.01 | 0.32 | 0.00 | 0.84 | 0.03 | 0.00 | 0.02 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_620.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.26 | 0.00 | 0.90 | 0.03 | 0.00 | 0.03 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_906.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.33 | 0.00 | 0.00 | 0.06 | 0.00 | 0.13 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_760.csv` | 0.70 | 0.00 | 0.00 | 1.00 | 0.94 | 0.00 | 0.02 | 0.78 | 0.01 | 0.65 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_389.csv` | 0.95 | 0.00 | 0.00 | 0.98 | 0.64 | 0.00 | 0.02 | 0.94 | 0.12 | 0.12 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_294.csv` | 0.90 | 0.00 | 0.00 | 0.99 | 0.80 | 0.00 | 0.00 | 0.36 | 0.00 | 0.03 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_702.csv` | 0.95 | 0.00 | 0.00 | 0.98 | 0.94 | 0.00 | 0.06 | 0.58 | 0.00 | 0.01 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_463.csv` | 1.00 | 0.00 | 0.00 | 0.01 | 0.15 | 0.00 | 0.82 | 0.69 | 0.00 | 0.01 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_23.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.40 | 0.00 | 1.00 | 0.00 | 0.00 | 0.02 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_785.csv` | 0.71 | 0.00 | 0.00 | 0.99 | 0.70 | 0.00 | 0.00 | 0.09 | 0.01 | 0.02 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_615.csv` | 0.41 | 0.00 | 0.00 | 1.00 | 0.12 | 0.00 | 0.01 | 0.97 | 0.03 | 0.24 | NONE |
| mean_shift | `ar_mean_shift_369.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.00 | 0.37 | 0.06 | 0.00 | 0.01 | PARTIAL |
| mean_shift | `ar_mean_shift_340.csv` | 0.99 | 0.00 | 0.00 | 0.89 | 0.72 | 0.00 | 0.02 | 0.75 | 0.00 | 0.03 | PARTIAL |
| mean_shift | `arma_mean_shift_373.csv` | 1.00 | 0.00 | 0.00 | 0.70 | 0.68 | 0.00 | 0.04 | 0.98 | 0.73 | 0.01 | PARTIAL |
| mean_shift | `arma_mean_shift_874.csv` | 1.00 | 0.00 | 0.00 | 0.27 | 0.16 | 0.00 | 0.23 | 0.04 | 0.00 | 0.60 | PARTIAL |
| mean_shift | `arma_mean_shift_688.csv` | 1.00 | 0.00 | 1.00 | 0.18 | 0.43 | 0.00 | 0.11 | 0.34 | 0.02 | 0.28 | NONE |
| mean_shift | `ma_mean_shift_588.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.34 | 0.00 | 0.92 | 0.09 | 0.01 | 0.01 | PARTIAL |
| mean_shift | `white_noise_mean_shift_865.csv` | 1.00 | 0.00 | 0.00 | 0.94 | 0.32 | 0.00 | 0.36 | 0.47 | 0.03 | 0.38 | PARTIAL |
| point_anomaly | `ar_point_anomaly_single_beginning_971.csv` | 1.00 | 0.00 | 0.00 | 0.03 | 0.82 | 0.00 | 0.64 | 0.34 | 0.00 | 0.08 | PARTIAL |
| point_anomaly | `ar_point_anomaly_single_middle_177.csv` | 1.00 | 0.00 | 0.00 | 0.01 | 0.31 | 0.00 | 0.72 | 0.21 | 0.00 | 0.49 | PARTIAL |
| point_anomaly | `ar_point_anomaly_single_beginning_546.csv` | 0.99 | 0.00 | 0.00 | 0.85 | 0.78 | 0.00 | 0.01 | 0.08 | 0.00 | 0.24 | PARTIAL |
| point_anomaly | `ar_point_anomaly_single_end_850.csv` | 0.98 | 0.00 | 0.00 | 0.99 | 0.78 | 0.00 | 0.01 | 0.31 | 0.00 | 0.14 | NONE |
| point_anomaly | `arma_point_anomaly_single_end_804.csv` | 0.93 | 0.00 | 0.39 | 0.00 | 0.01 | 0.00 | 0.01 | 0.00 | 0.00 | 0.41 | PARTIAL |
| point_anomaly | `arma_point_anomaly_single_beginning_706.csv` | 1.00 | 0.00 | 0.00 | 0.01 | 0.88 | 0.00 | 0.04 | 0.38 | 0.00 | 0.05 | PARTIAL |
| point_anomaly | `arma_point_anomaly_single_beginning_250.csv` | 0.88 | 0.00 | 0.00 | 1.00 | 0.20 | 0.00 | 0.03 | 0.71 | 0.01 | 0.40 | PARTIAL |
| point_anomaly | `arma_point_anomaly_single_end_342.csv` | 1.00 | 0.00 | 0.00 | 0.50 | 0.65 | 0.00 | 0.26 | 0.09 | 0.00 | 0.46 | PARTIAL |
| point_anomaly | `arma_point_anomaly_single_middle_585.csv` | 1.00 | 0.00 | 0.01 | 0.72 | 0.23 | 0.00 | 0.90 | 0.28 | 0.29 | 0.05 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_middle_988.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.06 | 0.00 | 0.00 | 0.40 | 0.00 | 0.06 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_end_596.csv` | 1.00 | 0.00 | 0.00 | 0.07 | 0.06 | 0.00 | 0.02 | 0.14 | 0.00 | 0.03 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_middle_795.csv` | 1.00 | 0.00 | 0.00 | 0.02 | 0.65 | 0.00 | 0.00 | 0.20 | 0.00 | 0.06 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_beginning_734.csv` | 1.00 | 0.00 | 0.06 | 0.29 | 0.69 | 0.00 | 0.01 | 0.13 | 0.00 | 0.10 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_end_283.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.36 | 0.00 | 0.67 | 0.31 | 0.00 | 0.03 | NONE |
| point_anomaly | `white_noise_point_anomaly_multiple_514.csv` | 0.93 | 0.00 | 0.00 | 0.99 | 0.67 | 0.00 | 0.97 | 0.18 | 0.73 | 0.03 | NONE |
| point_anomaly | `white_noise_point_anomaly_single_end_326.csv` | 0.62 | 0.00 | 0.00 | 0.99 | 0.58 | 0.00 | 0.73 | 0.98 | 0.01 | 0.14 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_single_middle_305.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.69 | 0.00 | 0.96 | 0.03 | 0.75 | 0.19 | NONE |
| trend_shift | `ar_trend_shift_104.csv` | 1.00 | 0.00 | 0.00 | 0.98 | 0.95 | 0.00 | 0.16 | 0.65 | 0.00 | 0.05 | PARTIAL |
| trend_shift | `ar_trend_shift_750.csv` | 1.00 | 0.00 | 0.00 | 0.97 | 0.91 | 0.00 | 0.01 | 0.18 | 0.03 | 0.47 | PARTIAL |
| trend_shift | `ar_trend_shift_680.csv` | 0.47 | 0.00 | 1.00 | 0.00 | 0.01 | 0.00 | 0.02 | 0.54 | 1.00 | 0.00 | PARTIAL |
| trend_shift | `white_noise_trend_shift_424.csv` | 0.99 | 0.00 | 0.00 | 0.88 | 0.85 | 0.00 | 0.01 | 0.77 | 0.13 | 0.45 | PARTIAL |
| trend_shift | `white_noise_trend_shift_529.csv` | 1.00 | 0.00 | 0.00 | 0.74 | 0.23 | 0.00 | 0.05 | 0.70 | 0.00 | 0.01 | PARTIAL |
| variance_shift | `ar_variance_shift_47.csv` | 0.57 | 0.00 | 0.00 | 0.99 | 0.11 | 0.00 | 0.00 | 0.13 | 0.00 | 0.92 | PARTIAL |
| variance_shift | `ar_variance_shift_77.csv` | 0.99 | 0.00 | 0.00 | 0.13 | 0.53 | 0.00 | 0.28 | 0.40 | 0.24 | 0.04 | PARTIAL |
| variance_shift | `ar_variance_shift_410.csv` | 0.08 | 0.00 | 0.00 | 0.98 | 0.39 | 0.00 | 0.01 | 0.90 | 0.00 | 0.15 | NONE |
| variance_shift | `arma_variance_shift_355.csv` | 0.53 | 0.00 | 0.00 | 1.00 | 0.35 | 0.00 | 0.03 | 0.00 | 0.00 | 0.97 | PARTIAL |
| variance_shift | `arma_variance_shift_524.csv` | 0.56 | 0.00 | 0.00 | 0.99 | 0.06 | 0.00 | 0.00 | 0.02 | 0.00 | 0.98 | PARTIAL |
| variance_shift | `ma_variance_shift_904.csv` | 1.00 | 0.00 | 0.00 | 0.01 | 0.04 | 0.00 | 0.01 | 0.16 | 0.00 | 0.31 | PARTIAL |
| variance_shift | `ma_variance_shift_506.csv` | 1.00 | 0.00 | 0.00 | 0.53 | 0.64 | 0.00 | 0.00 | 0.48 | 0.00 | 0.01 | PARTIAL |
| variance_shift | `ma_variance_shift_888.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 | PARTIAL |
| variance_shift | `ma_variance_shift_605.csv` | 0.95 | 0.00 | 0.01 | 0.97 | 0.48 | 0.00 | 0.01 | 0.01 | 0.00 | 0.88 | PARTIAL |
| variance_shift | `ma_variance_shift_189.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.50 | 0.00 | 0.00 | 0.06 | 0.00 | 0.13 | NONE |
| variance_shift | `ma_variance_shift_144.csv` | 0.98 | 0.00 | 0.00 | 0.36 | 0.88 | 0.00 | 0.17 | 0.52 | 0.00 | 0.29 | PARTIAL |
| variance_shift | `white_noise_variance_shift_597.csv` | 0.17 | 0.00 | 0.00 | 0.25 | 0.43 | 0.00 | 0.00 | 0.03 | 0.00 | 0.97 | PARTIAL |
| variance_shift | `white_noise_variance_shift_184.csv` | 1.00 | 0.00 | 0.00 | 0.02 | 0.09 | 0.00 | 0.73 | 0.21 | 0.00 | 0.05 | PARTIAL |
| variance_shift | `white_noise_variance_shift_316.csv` | 0.10 | 0.00 | 0.00 | 1.00 | 0.13 | 0.00 | 0.00 | 0.03 | 0.00 | 1.00 | PARTIAL |
| variance_shift | `white_noise_variance_shift_251.csv` | 0.75 | 0.00 | 0.00 | 1.00 | 0.23 | 0.00 | 0.01 | 0.92 | 0.00 | 0.64 | PARTIAL |
| variance_shift | `white_noise_variance_shift_473.csv` | 0.98 | 0.00 | 0.00 | 0.99 | 0.89 | 0.00 | 0.13 | 0.08 | 0.01 | 0.33 | NONE |
| variance_shift | `white_noise_variance_shift_546.csv` | 0.25 | 0.00 | 0.00 | 1.00 | 0.78 | 0.00 | 0.40 | 0.64 | 0.00 | 0.86 | PARTIAL |
| vol+collective | `garch_single_collective_anomaly_middle_150.csv` | 1.00 | 0.00 | 0.00 | 0.92 | 0.55 | 0.00 | 0.01 | 0.11 | 0.02 | 0.79 | PARTIAL |
| vol+mean_shift | `garch_single_mean_shift_increase_middle_144.csv` | 0.99 | 0.00 | 0.00 | 0.98 | 0.49 | 0.00 | 1.00 | 0.03 | 0.01 | 0.11 | PARTIAL |