# Manuel All-Data Test

Her kaynak grubunun her leaf klasöründen en fazla 10 CSV alınarak
ensemble ile sınıflandırılmıştır.

## Özet

| Metrik | Değer |
|---|---|
| Toplam test | 4400 |
| Full match | 2632 (59.8%) |
| Partial match | 1083 (24.6%) |
| No match | 685 (15.6%) |

## Grup Bazlı Özet

| # | Grup | Beklenen | Örnek | Full | Partial | None | Full% |
|---|---|---|---|---|---|---|---|
| 1 | stationary | stationary | 120 | 37 | 52 | 31 | %31 |
| 2 | deterministic_trend | deterministic_trend | 720 | 221 | 41 | 458 | %31 |
| 3 | stochastic_trend | stochastic_trend | 150 | 39 | 103 | 8 | %26 |
| 4 | volatility | volatility | 120 | 48 | 71 | 1 | %40 |
| 5 | collective_anomaly | stationary + collective_anomaly | 480 | 257 | 212 | 11 | %54 |
| 6 | contextual_anomaly | stationary + contextual_anomaly | 480 | 476 | 4 | 0 | %99 |
| 7 | mean_shift | stationary + mean_shift | 480 | 307 | 130 | 43 | %64 |
| 8 | point_anomaly | stationary + point_anomaly | 480 | 249 | 176 | 55 | %52 |
| 9 | trend_shift | stationary + trend_shift | 480 | 354 | 102 | 24 | %74 |
| 10 | variance_shift | stationary + variance_shift | 480 | 243 | 183 | 54 | %51 |
| 11 | cubic+collective | deterministic_trend + collective_anomaly | 10 | 10 | 0 | 0 | %100 |
| 12 | cubic+mean_shift | deterministic_trend + mean_shift | 20 | 20 | 0 | 0 | %100 |
| 13 | cubic+point_anomaly | deterministic_trend + point_anomaly | 10 | 10 | 0 | 0 | %100 |
| 14 | cubic+variance_shift | deterministic_trend + variance_shift | 10 | 10 | 0 | 0 | %100 |
| 15 | damped+collective | deterministic_trend + collective_anomaly | 10 | 10 | 0 | 0 | %100 |
| 16 | damped+mean_shift | deterministic_trend + mean_shift | 20 | 20 | 0 | 0 | %100 |
| 17 | damped+point_anomaly | deterministic_trend + point_anomaly | 10 | 10 | 0 | 0 | %100 |
| 18 | damped+variance_shift | deterministic_trend + variance_shift | 10 | 10 | 0 | 0 | %100 |
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
| 33 | stoch+mean_shift | stochastic_trend + mean_shift | 10 | 8 | 2 | 0 | %80 |
| 34 | stoch+point_anomaly | stochastic_trend + point_anomaly | 10 | 10 | 0 | 0 | %100 |
| 35 | stoch+variance_shift | stochastic_trend + variance_shift | 50 | 48 | 2 | 0 | %96 |
| 36 | vol+collective | volatility + collective_anomaly | 10 | 9 | 1 | 0 | %90 |
| 37 | vol+mean_shift | volatility + mean_shift | 10 | 10 | 0 | 0 | %100 |
| 38 | vol+point_anomaly | volatility + point_anomaly | 10 | 9 | 1 | 0 | %90 |
| 39 | vol+variance_shift | volatility + variance_shift | 10 | 8 | 2 | 0 | %80 |

---

## Grup 1: stationary
**Beklenen:** `stationary`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `ar_long` | `ar_28856.csv` | `stationary + point_anomaly` | ~ PARTIAL |
| `ar_long` | `ar_13281.csv` | `stationary` | ✓ FULL |
| `ar_long` | `ar_10735.csv` | `stationary + point_anomaly` | ~ PARTIAL |
| `ar_long` | `ar_31868.csv` | `stationary + point_anomaly` | ~ PARTIAL |
| `ar_long` | `ar_18109.csv` | `stationary` | ✓ FULL |
| `ar_long` | `ar_1722.csv` | `stationary` | ✓ FULL |
| `ar_long` | `ar_16581.csv` | `stationary` | ✓ FULL |
| `ar_long` | `ar_14112.csv` | `stationary` | ✓ FULL |
| `ar_long` | `ar_31717.csv` | `stationary` | ✓ FULL |
| `ar_long` | `ar_1302.csv` | `stationary` | ✓ FULL |
| `ar_medium` | `ar_29956.csv` | `stationary` | ✓ FULL |
| `ar_medium` | `ar_31841.csv` | `stationary + point_anomaly` | ~ PARTIAL |
| `ar_medium` | `ar_7284.csv` | `stationary + mean_shift + trend_shift` | ~ PARTIAL |
| `ar_medium` | `ar_26081.csv` | `stationary + collective_anomaly + mean_shift` | ~ PARTIAL |
| `ar_medium` | `ar_12561.csv` | `stationary + collective_anomaly` | ~ PARTIAL |
| `ar_medium` | `ar_27412.csv` | `stationary + point_anomaly` | ~ PARTIAL |
| `ar_medium` | `ar_22440.csv` | `stationary + point_anomaly` | ~ PARTIAL |
| `ar_medium` | `ar_10935.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `ar_medium` | `ar_10877.csv` | `stationary` | ✓ FULL |
| `ar_medium` | `ar_12761.csv` | `stationary + variance_shift` | ~ PARTIAL |
| `ar_short` | `ar_16446.csv` | `volatility + collective_anomaly + point_anomaly + trend_shift` | ✗ NONE |
| `ar_short` | `ar_1686.csv` | `stochastic_trend + collective_anomaly + point_anomaly + trend_shift` | ✗ NONE |
| `ar_short` | `ar_24901.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly + trend_shift` | ✗ NONE |
| `ar_short` | `ar_27752.csv` | `volatility + collective_anomaly + point_anomaly + trend_shift` | ✗ NONE |
| `ar_short` | `ar_10780.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `ar_short` | `ar_2655.csv` | `stochastic_trend + mean_shift + point_anomaly + trend_shift` | ✗ NONE |
| `ar_short` | `ar_15862.csv` | `volatility + collective_anomaly + trend_shift` | ✗ NONE |
| `ar_short` | `ar_31113.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `ar_short` | `ar_29164.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `ar_short` | `ar_30681.csv` | `stationary + variance_shift` | ~ PARTIAL |
| `arma_long` | `arma_26069.csv` | `stationary + variance_shift` | ~ PARTIAL |
| `arma_long` | `arma_2237.csv` | `stationary + point_anomaly` | ~ PARTIAL |
| `arma_long` | `arma_165.csv` | `stationary` | ✓ FULL |
| `arma_long` | `arma_23245.csv` | `stationary + collective_anomaly` | ~ PARTIAL |
| `arma_long` | `arma_27377.csv` | `stationary + point_anomaly` | ~ PARTIAL |
| `arma_long` | `arma_18201.csv` | `stationary` | ✓ FULL |
| `arma_long` | `arma_4844.csv` | `stationary` | ✓ FULL |
| `arma_long` | `arma_661.csv` | `stationary` | ✓ FULL |
| `arma_long` | `arma_10189.csv` | `stationary + point_anomaly` | ~ PARTIAL |
| `arma_long` | `arma_3350.csv` | `stationary` | ✓ FULL |
| `arma_medium` | `arma_4738.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ✗ NONE |
| `arma_medium` | `arma_14706.csv` | `stationary + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `arma_medium` | `arma_30587.csv` | `stationary + point_anomaly` | ~ PARTIAL |
| `arma_medium` | `arma_22461.csv` | `stationary + point_anomaly` | ~ PARTIAL |
| `arma_medium` | `arma_20031.csv` | `stationary + point_anomaly + variance_shift` | ~ PARTIAL |
| `arma_medium` | `arma_18193.csv` | `stationary` | ✓ FULL |
| `arma_medium` | `arma_14583.csv` | `stationary + collective_anomaly + mean_shift` | ~ PARTIAL |
| `arma_medium` | `arma_16348.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `arma_medium` | `arma_9201.csv` | `stationary + variance_shift` | ~ PARTIAL |
| `arma_medium` | `arma_349.csv` | `stationary + collective_anomaly + mean_shift` | ~ PARTIAL |
| `arma_short` | `arma_19925.csv` | `stationary + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `arma_short` | `arma_13011.csv` | `stationary + collective_anomaly` | ~ PARTIAL |
| `arma_short` | `arma_12733.csv` | `volatility + collective_anomaly + point_anomaly + trend_shift` | ✗ NONE |
| `arma_short` | `arma_21201.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ✗ NONE |
| `arma_short` | `arma_12850.csv` | `stationary + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `arma_short` | `arma_20585.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `arma_short` | `arma_5967.csv` | `volatility + collective_anomaly + variance_shift` | ✗ NONE |
| `arma_short` | `arma_20140.csv` | `stationary + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `arma_short` | `arma_27802.csv` | `stationary + collective_anomaly` | ~ PARTIAL |
| `arma_short` | `arma_178.csv` | `stationary + collective_anomaly + variance_shift` | ~ PARTIAL |
| `ma_long` | `ma_4776.csv` | `stationary` | ✓ FULL |
| `ma_long` | `ma_11279.csv` | `stationary` | ✓ FULL |
| `ma_long` | `ma_31518.csv` | `stationary + point_anomaly` | ~ PARTIAL |
| `ma_long` | `ma_23547.csv` | `stationary` | ✓ FULL |
| `ma_long` | `ma_25812.csv` | `stationary` | ✓ FULL |
| `ma_long` | `ma_1368.csv` | `stationary` | ✓ FULL |
| `ma_long` | `ma_9672.csv` | `stationary` | ✓ FULL |
| `ma_long` | `ma_8172.csv` | `stationary` | ✓ FULL |
| `ma_long` | `ma_21160.csv` | `stationary` | ✓ FULL |
| `ma_long` | `ma_12321.csv` | `stationary` | ✓ FULL |
| `ma_medium` | `ma_26279.csv` | `stationary` | ✓ FULL |
| `ma_medium` | `ma_18644.csv` | `stationary + collective_anomaly + mean_shift` | ~ PARTIAL |
| `ma_medium` | `ma_5432.csv` | `stationary` | ✓ FULL |
| `ma_medium` | `ma_28538.csv` | `stationary` | ✓ FULL |
| `ma_medium` | `ma_28239.csv` | `stationary` | ✓ FULL |
| `ma_medium` | `ma_7086.csv` | `stationary` | ✓ FULL |
| `ma_medium` | `ma_6386.csv` | `stationary` | ✓ FULL |
| `ma_medium` | `ma_20663.csv` | `stationary` | ✓ FULL |
| `ma_medium` | `ma_27024.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `ma_medium` | `ma_15669.csv` | `stationary + point_anomaly` | ~ PARTIAL |
| `ma_short` | `ma_30777.csv` | `volatility + point_anomaly` | ✗ NONE |
| `ma_short` | `ma_12049.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `ma_short` | `ma_11349.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `ma_short` | `ma_2950.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `ma_short` | `ma_16719.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `ma_short` | `ma_3771.csv` | `stationary` | ✓ FULL |
| `ma_short` | `ma_18532.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `ma_short` | `ma_12350.csv` | `volatility + collective_anomaly + trend_shift` | ✗ NONE |
| `ma_short` | `ma_6198.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `ma_short` | `ma_16864.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `wn_long` | `wn_6526.csv` | `stationary + contextual_anomaly` | ~ PARTIAL |
| `wn_long` | `wn_12977.csv` | `stationary` | ✓ FULL |
| `wn_long` | `wn_21207.csv` | `stationary` | ✓ FULL |
| `wn_long` | `wn_18196.csv` | `stationary + contextual_anomaly` | ~ PARTIAL |
| `wn_long` | `wn_2337.csv` | `stationary + contextual_anomaly` | ~ PARTIAL |
| `wn_long` | `wn_28746.csv` | `stationary + contextual_anomaly` | ~ PARTIAL |
| `wn_long` | `wn_5572.csv` | `stationary` | ✓ FULL |
| `wn_long` | `wn_20757.csv` | `stationary` | ✓ FULL |
| `wn_long` | `wn_14795.csv` | `stationary + contextual_anomaly` | ~ PARTIAL |
| `wn_long` | `wn_20915.csv` | `stationary` | ✓ FULL |
| `wn_medium` | `wn_20475.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ~ PARTIAL |
| `wn_medium` | `wn_16177.csv` | `stationary + collective_anomaly + contextual_anomaly` | ~ PARTIAL |
| `wn_medium` | `wn_29763.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `wn_medium` | `wn_17872.csv` | `stationary + collective_anomaly` | ~ PARTIAL |
| `wn_medium` | `wn_30696.csv` | `stationary + collective_anomaly + contextual_anomaly` | ~ PARTIAL |
| `wn_medium` | `wn_8597.csv` | `stationary + collective_anomaly` | ~ PARTIAL |
| `wn_medium` | `wn_30156.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ~ PARTIAL |
| `wn_medium` | `wn_29109.csv` | `stationary + collective_anomaly + contextual_anomaly` | ~ PARTIAL |
| `wn_medium` | `wn_12102.csv` | `stationary + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `wn_medium` | `wn_27963.csv` | `stationary + collective_anomaly + contextual_anomaly` | ~ PARTIAL |
| `wn_short` | `wn_28724.csv` | `stationary + collective_anomaly + contextual_anomaly` | ~ PARTIAL |
| `wn_short` | `wn_15044.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `wn_short` | `wn_25750.csv` | `volatility + collective_anomaly + contextual_anomaly` | ✗ NONE |
| `wn_short` | `wn_31500.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `wn_short` | `wn_17217.csv` | `volatility + collective_anomaly + contextual_anomaly` | ✗ NONE |
| `wn_short` | `wn_14817.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `wn_short` | `wn_23630.csv` | `stationary + collective_anomaly + contextual_anomaly` | ~ PARTIAL |
| `wn_short` | `wn_21188.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `wn_short` | `wn_1796.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `wn_short` | `wn_8264.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ~ PARTIAL |
---

## Grup 2: deterministic_trend
**Beklenen:** `deterministic_trend`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `long` | `ar_cubic_trend_689.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ar_cubic_trend_732.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ar_cubic_trend_611.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ar_cubic_trend_30.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ar_cubic_trend_73.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ar_cubic_trend_398.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ar_cubic_trend_876.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ar_cubic_trend_806.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ar_cubic_trend_813.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ar_cubic_trend_15.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ar_cubic_trend_309.csv` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `medium` | `ar_cubic_trend_856.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ar_cubic_trend_127.csv` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `medium` | `ar_cubic_trend_840.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ar_cubic_trend_39.csv` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `medium` | `ar_cubic_trend_468.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ar_cubic_trend_345.csv` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `medium` | `ar_cubic_trend_159.csv` | `stationary` | ✗ NONE |
| `medium` | `ar_cubic_trend_293.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ar_cubic_trend_940.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `ar_cubic_trend_968.csv` | `stochastic_trend + point_anomaly` | ✗ NONE |
| `short` | `ar_cubic_trend_620.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `ar_cubic_trend_906.csv` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `short` | `ar_cubic_trend_760.csv` | `deterministic_trend + point_anomaly + trend_shift` | ~ PARTIAL |
| `short` | `ar_cubic_trend_389.csv` | `stochastic_trend` | ✗ NONE |
| `short` | `ar_cubic_trend_294.csv` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `short` | `ar_cubic_trend_702.csv` | `stochastic_trend + point_anomaly` | ✗ NONE |
| `short` | `ar_cubic_trend_559.csv` | `stochastic_trend` | ✗ NONE |
| `short` | `ar_cubic_trend_463.csv` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `short` | `ar_cubic_trend_913.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ar_damped_trend_941.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ar_damped_trend_691.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ar_damped_trend_520.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ar_damped_trend_23.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ar_damped_trend_342.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ar_damped_trend_226.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ar_damped_trend_325.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ar_damped_trend_785.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ar_damped_trend_615.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ar_damped_trend_595.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ar_damped_trend_340.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ar_damped_trend_787.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ar_damped_trend_637.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ar_damped_trend_493.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ar_damped_trend_926.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ar_damped_trend_636.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ar_damped_trend_466.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ar_damped_trend_431.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ar_damped_trend_30.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ar_damped_trend_225.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `ar_damped_trend_568.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `ar_damped_trend_553.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `ar_damped_trend_182.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `ar_damped_trend_795.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `ar_damped_trend_141.csv` | `deterministic_trend + point_anomaly` | ~ PARTIAL |
| `short` | `ar_damped_trend_892.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `ar_damped_trend_2.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `ar_damped_trend_239.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `ar_damped_trend_677.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `ar_damped_trend_245.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ar_exponential_trend_829.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `ar_exponential_trend_725.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ar_exponential_trend_488.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ar_exponential_trend_648.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ar_exponential_trend_157.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `ar_exponential_trend_453.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ar_exponential_trend_45.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ar_exponential_trend_53.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ar_exponential_trend_586.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ar_exponential_trend_33.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ar_exponential_trend_994.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ar_exponential_trend_608.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ar_exponential_trend_892.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ar_exponential_trend_968.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ar_exponential_trend_108.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ar_exponential_trend_725.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ar_exponential_trend_763.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ar_exponential_trend_203.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ar_exponential_trend_727.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ar_exponential_trend_914.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `ar_exponential_trend_593.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `ar_exponential_trend_790.csv` | `stochastic_trend + trend_shift` | ✗ NONE |
| `short` | `ar_exponential_trend_344.csv` | `stochastic_trend + trend_shift` | ✗ NONE |
| `short` | `ar_exponential_trend_807.csv` | `stochastic_trend + trend_shift` | ✗ NONE |
| `short` | `ar_exponential_trend_69.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `ar_exponential_trend_411.csv` | `stochastic_trend + trend_shift` | ✗ NONE |
| `short` | `ar_exponential_trend_200.csv` | `stochastic_trend + trend_shift` | ✗ NONE |
| `short` | `ar_exponential_trend_369.csv` | `stochastic_trend + trend_shift` | ✗ NONE |
| `short` | `ar_exponential_trend_5.csv` | `stochastic_trend + trend_shift` | ✗ NONE |
| `short` | `ar_exponential_trend_243.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ar_linear_down_trend_516.csv` | `stationary` | ✗ NONE |
| `long` | `ar_linear_down_trend_1000.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `ar_linear_down_trend_978.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `ar_linear_down_trend_764.csv` | `stationary + mean_shift` | ✗ NONE |
| `long` | `ar_linear_down_trend_905.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `ar_linear_down_trend_761.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `ar_linear_down_trend_340.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `ar_linear_down_trend_995.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `ar_linear_down_trend_56.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `ar_linear_down_trend_800.csv` | `stationary + mean_shift` | ✗ NONE |
| `medium` | `ar_linear_down_trend_262.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ar_linear_down_trend_566.csv` | `stationary + mean_shift + trend_shift` | ✗ NONE |
| `medium` | `ar_linear_down_trend_94.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ar_linear_down_trend_196.csv` | `stochastic_trend + trend_shift` | ✗ NONE |
| `medium` | `ar_linear_down_trend_900.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ar_linear_down_trend_675.csv` | `stationary + mean_shift + trend_shift` | ✗ NONE |
| `medium` | `ar_linear_down_trend_373.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ar_linear_down_trend_874.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ar_linear_down_trend_688.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ar_linear_down_trend_66.csv` | `stationary + trend_shift` | ✗ NONE |
| `short` | `ar_linear_down_trend_281.csv` | `stochastic_trend + trend_shift` | ✗ NONE |
| `short` | `ar_linear_down_trend_239.csv` | `stochastic_trend + trend_shift` | ✗ NONE |
| `short` | `ar_linear_down_trend_442.csv` | `stationary + trend_shift` | ✗ NONE |
| `short` | `ar_linear_down_trend_800.csv` | `stochastic_trend + point_anomaly + trend_shift` | ✗ NONE |
| `short` | `ar_linear_down_trend_247.csv` | `stationary + trend_shift` | ✗ NONE |
| `short` | `ar_linear_down_trend_596.csv` | `stochastic_trend + trend_shift` | ✗ NONE |
| `short` | `ar_linear_down_trend_978.csv` | `stochastic_trend + trend_shift` | ✗ NONE |
| `short` | `ar_linear_down_trend_816.csv` | `stochastic_trend + trend_shift` | ✗ NONE |
| `short` | `ar_linear_down_trend_949.csv` | `stochastic_trend + trend_shift` | ✗ NONE |
| `short` | `ar_linear_down_trend_588.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `ar_linear_up_trend_945.csv` | `stationary + mean_shift` | ✗ NONE |
| `long` | `ar_linear_up_trend_1.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `ar_linear_up_trend_650.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `ar_linear_up_trend_397.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `ar_linear_up_trend_549.csv` | `stationary` | ✗ NONE |
| `long` | `ar_linear_up_trend_115.csv` | `stationary` | ✗ NONE |
| `long` | `ar_linear_up_trend_200.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `ar_linear_up_trend_955.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `ar_linear_up_trend_432.csv` | `stationary` | ✗ NONE |
| `long` | `ar_linear_up_trend_908.csv` | `stationary` | ✗ NONE |
| `medium` | `ar_linear_up_trend_865.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ar_linear_up_trend_842.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ar_linear_up_trend_381.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ar_linear_up_trend_319.csv` | `stationary + mean_shift + trend_shift` | ✗ NONE |
| `medium` | `ar_linear_up_trend_151.csv` | `stationary + mean_shift + trend_shift` | ✗ NONE |
| `medium` | `ar_linear_up_trend_32.csv` | `stochastic_trend + trend_shift` | ✗ NONE |
| `medium` | `ar_linear_up_trend_908.csv` | `stationary + mean_shift + trend_shift` | ✗ NONE |
| `medium` | `ar_linear_up_trend_620.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ar_linear_up_trend_971.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ar_linear_up_trend_170.csv` | `stationary + trend_shift` | ✗ NONE |
| `short` | `ar_linear_up_trend_177.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `short` | `ar_linear_up_trend_773.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `short` | `ar_linear_up_trend_546.csv` | `volatility + mean_shift + trend_shift` | ✗ NONE |
| `short` | `ar_linear_up_trend_850.csv` | `stationary + mean_shift + trend_shift` | ✗ NONE |
| `short` | `ar_linear_up_trend_161.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `short` | `ar_linear_up_trend_8.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `short` | `ar_linear_up_trend_59.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `short` | `ar_linear_up_trend_804.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `short` | `ar_linear_up_trend_213.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `short` | `ar_linear_up_trend_216.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `long` | `ar_quadratic_trend_706.csv` | `stationary + point_anomaly` | ✗ NONE |
| `long` | `ar_quadratic_trend_536.csv` | `stationary + collective_anomaly` | ✗ NONE |
| `long` | `ar_quadratic_trend_971.csv` | `stationary` | ✗ NONE |
| `long` | `ar_quadratic_trend_604.csv` | `stationary + point_anomaly` | ✗ NONE |
| `long` | `ar_quadratic_trend_250.csv` | `stationary` | ✗ NONE |
| `long` | `ar_quadratic_trend_342.csv` | `stationary` | ✗ NONE |
| `long` | `ar_quadratic_trend_585.csv` | `stationary` | ✗ NONE |
| `long` | `ar_quadratic_trend_902.csv` | `stationary` | ✗ NONE |
| `long` | `ar_quadratic_trend_658.csv` | `stationary` | ✗ NONE |
| `long` | `ar_quadratic_trend_489.csv` | `stationary + point_anomaly` | ✗ NONE |
| `medium` | `ar_quadratic_trend_988.csv` | `stationary + collective_anomaly` | ✗ NONE |
| `medium` | `ar_quadratic_trend_293.csv` | `stationary + contextual_anomaly + point_anomaly` | ✗ NONE |
| `medium` | `ar_quadratic_trend_955.csv` | `stationary + collective_anomaly` | ✗ NONE |
| `medium` | `ar_quadratic_trend_596.csv` | `stationary + collective_anomaly` | ✗ NONE |
| `medium` | `ar_quadratic_trend_795.csv` | `stationary + point_anomaly` | ✗ NONE |
| `medium` | `ar_quadratic_trend_771.csv` | `stationary + collective_anomaly` | ✗ NONE |
| `medium` | `ar_quadratic_trend_734.csv` | `stationary + collective_anomaly` | ✗ NONE |
| `medium` | `ar_quadratic_trend_283.csv` | `stationary + point_anomaly` | ✗ NONE |
| `medium` | `ar_quadratic_trend_756.csv` | `deterministic_trend + collective_anomaly` | ~ PARTIAL |
| `medium` | `ar_quadratic_trend_386.csv` | `stationary + point_anomaly` | ✗ NONE |
| `short` | `ar_quadratic_trend_466.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✗ NONE |
| `short` | `ar_quadratic_trend_717.csv` | `stochastic_trend + contextual_anomaly + point_anomaly` | ✗ NONE |
| `short` | `ar_quadratic_trend_698.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly + trend_shift` | ✗ NONE |
| `short` | `ar_quadratic_trend_442.csv` | `stationary + contextual_anomaly + point_anomaly` | ✗ NONE |
| `short` | `ar_quadratic_trend_501.csv` | `stationary + point_anomaly` | ✗ NONE |
| `short` | `ar_quadratic_trend_928.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `short` | `ar_quadratic_trend_575.csv` | `stationary + collective_anomaly` | ✗ NONE |
| `short` | `ar_quadratic_trend_514.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✗ NONE |
| `short` | `ar_quadratic_trend_209.csv` | `stationary + contextual_anomaly + trend_shift` | ✗ NONE |
| `short` | `ar_quadratic_trend_326.csv` | `stationary` | ✗ NONE |
| `long` | `arma_cubic_trend_305.csv` | `stochastic_trend` | ✗ NONE |
| `long` | `arma_cubic_trend_157.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `arma_cubic_trend_41.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `arma_cubic_trend_117.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `arma_cubic_trend_640.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `arma_cubic_trend_609.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `arma_cubic_trend_31.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `arma_cubic_trend_300.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `arma_cubic_trend_104.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `arma_cubic_trend_163.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `arma_cubic_trend_750.csv` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `medium` | `arma_cubic_trend_680.csv` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `medium` | `arma_cubic_trend_152.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `arma_cubic_trend_309.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `arma_cubic_trend_160.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `arma_cubic_trend_933.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `arma_cubic_trend_127.csv` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `medium` | `arma_cubic_trend_891.csv` | `stochastic_trend` | ✗ NONE |
| `medium` | `arma_cubic_trend_402.csv` | `stationary` | ✗ NONE |
| `medium` | `arma_cubic_trend_163.csv` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `short` | `arma_cubic_trend_572.csv` | `stochastic_trend` | ✗ NONE |
| `short` | `arma_cubic_trend_317.csv` | `stochastic_trend` | ✗ NONE |
| `short` | `arma_cubic_trend_355.csv` | `stochastic_trend + point_anomaly + trend_shift` | ✗ NONE |
| `short` | `arma_cubic_trend_715.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `arma_cubic_trend_546.csv` | `stochastic_trend` | ✗ NONE |
| `short` | `arma_cubic_trend_296.csv` | `stochastic_trend` | ✗ NONE |
| `short` | `arma_cubic_trend_596.csv` | `stochastic_trend + point_anomaly` | ✗ NONE |
| `short` | `arma_cubic_trend_22.csv` | `stochastic_trend + point_anomaly` | ✗ NONE |
| `short` | `arma_cubic_trend_765.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `arma_cubic_trend_960.csv` | `stochastic_trend` | ✗ NONE |
| `long` | `arma_damped_trend_911.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `arma_damped_trend_624.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `arma_damped_trend_63.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `arma_damped_trend_534.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `arma_damped_trend_321.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `arma_damped_trend_821.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `arma_damped_trend_842.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `arma_damped_trend_473.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `arma_damped_trend_273.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `arma_damped_trend_185.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `arma_damped_trend_188.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `arma_damped_trend_705.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `arma_damped_trend_496.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `arma_damped_trend_424.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `arma_damped_trend_489.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `arma_damped_trend_477.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `arma_damped_trend_529.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `arma_damped_trend_895.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `arma_damped_trend_770.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `arma_damped_trend_148.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `arma_damped_trend_719.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `arma_damped_trend_700.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `arma_damped_trend_694.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `arma_damped_trend_189.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `arma_damped_trend_154.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `arma_damped_trend_47.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `arma_damped_trend_77.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `arma_damped_trend_410.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `arma_damped_trend_836.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `arma_damped_trend_893.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `arma_exponential_trend_199.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `arma_exponential_trend_327.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `arma_exponential_trend_275.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `arma_exponential_trend_273.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `arma_exponential_trend_593.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `arma_exponential_trend_511.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `arma_exponential_trend_227.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `arma_exponential_trend_488.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `arma_exponential_trend_267.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `arma_exponential_trend_355.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `arma_exponential_trend_524.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `arma_exponential_trend_328.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `arma_exponential_trend_904.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `arma_exponential_trend_95.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `arma_exponential_trend_168.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `arma_exponential_trend_506.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `arma_exponential_trend_843.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `arma_exponential_trend_893.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `arma_exponential_trend_888.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `arma_exponential_trend_605.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `arma_exponential_trend_189.csv` | `stochastic_trend + trend_shift` | ✗ NONE |
| `short` | `arma_exponential_trend_144.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `arma_exponential_trend_7.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `arma_exponential_trend_597.csv` | `stochastic_trend` | ✗ NONE |
| `short` | `arma_exponential_trend_87.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `arma_exponential_trend_111.csv` | `stochastic_trend + trend_shift` | ✗ NONE |
| `short` | `arma_exponential_trend_992.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `short` | `arma_exponential_trend_184.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `arma_exponential_trend_952.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `arma_exponential_trend_793.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `arma_linear_down_trend_881.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `arma_linear_down_trend_316.csv` | `stationary` | ✗ NONE |
| `long` | `arma_linear_down_trend_251.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `arma_linear_down_trend_473.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `arma_linear_down_trend_546.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `arma_linear_down_trend_541.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `arma_linear_down_trend_295.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `arma_linear_down_trend_896.csv` | `stationary` | ✗ NONE |
| `long` | `arma_linear_down_trend_468.csv` | `stationary` | ✗ NONE |
| `long` | `arma_linear_down_trend_930.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `arma_linear_down_trend_152.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `arma_linear_down_trend_25.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `arma_linear_down_trend_448.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `arma_linear_down_trend_100.csv` | `stationary + mean_shift + trend_shift` | ✗ NONE |
| `medium` | `arma_linear_down_trend_458.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `arma_linear_down_trend_342.csv` | `stationary + mean_shift` | ✗ NONE |
| `medium` | `arma_linear_down_trend_952.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `arma_linear_down_trend_820.csv` | `stochastic_trend + trend_shift` | ✗ NONE |
| `medium` | `arma_linear_down_trend_821.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `arma_linear_down_trend_517.csv` | `stationary + trend_shift` | ✗ NONE |
| `short` | `arma_linear_down_trend_361.csv` | `stochastic_trend + trend_shift` | ✗ NONE |
| `short` | `arma_linear_down_trend_489.csv` | `stochastic_trend + trend_shift` | ✗ NONE |
| `short` | `arma_linear_down_trend_740.csv` | `stochastic_trend + point_anomaly + trend_shift` | ✗ NONE |
| `short` | `arma_linear_down_trend_981.csv` | `stationary + trend_shift` | ✗ NONE |
| `short` | `arma_linear_down_trend_772.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `short` | `arma_linear_down_trend_820.csv` | `stationary + trend_shift` | ✗ NONE |
| `short` | `arma_linear_down_trend_610.csv` | `volatility + mean_shift + trend_shift` | ✗ NONE |
| `short` | `arma_linear_down_trend_708.csv` | `stochastic_trend + trend_shift` | ✗ NONE |
| `short` | `arma_linear_down_trend_760.csv` | `stochastic_trend + trend_shift` | ✗ NONE |
| `short` | `arma_linear_down_trend_547.csv` | `stochastic_trend + trend_shift` | ✗ NONE |
| `long` | `arma_linear_up_trend_240.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `arma_linear_up_trend_273.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `arma_linear_up_trend_371.csv` | `stationary` | ✗ NONE |
| `long` | `arma_linear_up_trend_299.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `arma_linear_up_trend_991.csv` | `stochastic_trend + trend_shift` | ✗ NONE |
| `long` | `arma_linear_up_trend_151.csv` | `stationary` | ✗ NONE |
| `long` | `arma_linear_up_trend_632.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `arma_linear_up_trend_777.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `arma_linear_up_trend_599.csv` | `stationary` | ✗ NONE |
| `long` | `arma_linear_up_trend_154.csv` | `stationary + mean_shift` | ✗ NONE |
| `medium` | `arma_linear_up_trend_788.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `arma_linear_up_trend_388.csv` | `stationary + mean_shift + trend_shift` | ✗ NONE |
| `medium` | `arma_linear_up_trend_150.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `arma_linear_up_trend_144.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `arma_linear_up_trend_637.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `arma_linear_up_trend_538.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `arma_linear_up_trend_561.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `arma_linear_up_trend_946.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `arma_linear_up_trend_885.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `arma_linear_up_trend_588.csv` | `stationary + mean_shift + variance_shift` | ✗ NONE |
| `short` | `arma_linear_up_trend_243.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `short` | `arma_linear_up_trend_150.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `short` | `arma_linear_up_trend_984.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `short` | `arma_linear_up_trend_567.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `short` | `arma_linear_up_trend_172.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `short` | `arma_linear_up_trend_883.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `short` | `arma_linear_up_trend_27.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `short` | `arma_linear_up_trend_161.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `short` | `arma_linear_up_trend_647.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `short` | `arma_linear_up_trend_160.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `long` | `arma_quadratic_trend_720.csv` | `stationary` | ✗ NONE |
| `long` | `arma_quadratic_trend_893.csv` | `stationary + point_anomaly` | ✗ NONE |
| `long` | `arma_quadratic_trend_314.csv` | `stationary` | ✗ NONE |
| `long` | `arma_quadratic_trend_470.csv` | `stationary` | ✗ NONE |
| `long` | `arma_quadratic_trend_208.csv` | `stationary` | ✗ NONE |
| `long` | `arma_quadratic_trend_967.csv` | `stationary` | ✗ NONE |
| `long` | `arma_quadratic_trend_919.csv` | `stationary` | ✗ NONE |
| `long` | `arma_quadratic_trend_623.csv` | `stationary + collective_anomaly` | ✗ NONE |
| `long` | `arma_quadratic_trend_325.csv` | `stationary` | ✗ NONE |
| `long` | `arma_quadratic_trend_631.csv` | `stationary` | ✗ NONE |
| `medium` | `arma_quadratic_trend_646.csv` | `stationary + collective_anomaly + point_anomaly` | ✗ NONE |
| `medium` | `arma_quadratic_trend_134.csv` | `stationary + collective_anomaly` | ✗ NONE |
| `medium` | `arma_quadratic_trend_67.csv` | `stationary + collective_anomaly + point_anomaly` | ✗ NONE |
| `medium` | `arma_quadratic_trend_173.csv` | `stationary + collective_anomaly` | ✗ NONE |
| `medium` | `arma_quadratic_trend_485.csv` | `stationary + collective_anomaly + point_anomaly` | ✗ NONE |
| `medium` | `arma_quadratic_trend_704.csv` | `deterministic_trend + point_anomaly` | ~ PARTIAL |
| `medium` | `arma_quadratic_trend_636.csv` | `stationary + contextual_anomaly + point_anomaly` | ✗ NONE |
| `medium` | `arma_quadratic_trend_619.csv` | `stationary + collective_anomaly` | ✗ NONE |
| `medium` | `arma_quadratic_trend_580.csv` | `stationary + collective_anomaly` | ✗ NONE |
| `medium` | `arma_quadratic_trend_39.csv` | `stationary + collective_anomaly` | ✗ NONE |
| `short` | `arma_quadratic_trend_960.csv` | `stationary + collective_anomaly + point_anomaly` | ✗ NONE |
| `short` | `arma_quadratic_trend_339.csv` | `stationary + collective_anomaly` | ✗ NONE |
| `short` | `arma_quadratic_trend_287.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `short` | `arma_quadratic_trend_715.csv` | `stationary + collective_anomaly` | ✗ NONE |
| `short` | `arma_quadratic_trend_759.csv` | `stationary + collective_anomaly` | ✗ NONE |
| `short` | `arma_quadratic_trend_388.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly + trend_shift` | ✗ NONE |
| `short` | `arma_quadratic_trend_318.csv` | `stationary` | ✗ NONE |
| `short` | `arma_quadratic_trend_342.csv` | `stationary + collective_anomaly` | ✗ NONE |
| `short` | `arma_quadratic_trend_463.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `short` | `arma_quadratic_trend_219.csv` | `stationary + point_anomaly` | ✗ NONE |
| `long` | `ma_cubic_trend_717.csv` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `long` | `ma_cubic_trend_693.csv` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `long` | `ma_cubic_trend_375.csv` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `long` | `ma_cubic_trend_52.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ma_cubic_trend_39.csv` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `long` | `ma_cubic_trend_955.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ma_cubic_trend_791.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ma_cubic_trend_961.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ma_cubic_trend_165.csv` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `long` | `ma_cubic_trend_106.csv` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `medium` | `ma_cubic_trend_520.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ma_cubic_trend_671.csv` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `medium` | `ma_cubic_trend_617.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ma_cubic_trend_190.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ma_cubic_trend_166.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ma_cubic_trend_594.csv` | `stochastic_trend` | ✗ NONE |
| `medium` | `ma_cubic_trend_295.csv` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `medium` | `ma_cubic_trend_565.csv` | `stationary` | ✗ NONE |
| `medium` | `ma_cubic_trend_342.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ma_cubic_trend_22.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `ma_cubic_trend_959.csv` | `stochastic_trend + point_anomaly` | ✗ NONE |
| `short` | `ma_cubic_trend_42.csv` | `stochastic_trend` | ✗ NONE |
| `short` | `ma_cubic_trend_910.csv` | `stochastic_trend` | ✗ NONE |
| `short` | `ma_cubic_trend_161.csv` | `stochastic_trend + trend_shift` | ✗ NONE |
| `short` | `ma_cubic_trend_909.csv` | `stochastic_trend + trend_shift` | ✗ NONE |
| `short` | `ma_cubic_trend_323.csv` | `stochastic_trend + point_anomaly` | ✗ NONE |
| `short` | `ma_cubic_trend_439.csv` | `stochastic_trend + point_anomaly` | ✗ NONE |
| `short` | `ma_cubic_trend_360.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `ma_cubic_trend_243.csv` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `short` | `ma_cubic_trend_501.csv` | `deterministic_trend + point_anomaly + trend_shift` | ~ PARTIAL |
| `long` | `ma_damped_trend_867.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ma_damped_trend_6.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ma_damped_trend_747.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ma_damped_trend_377.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ma_damped_trend_662.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ma_damped_trend_842.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ma_damped_trend_700.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ma_damped_trend_586.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ma_damped_trend_105.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ma_damped_trend_713.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ma_damped_trend_851.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ma_damped_trend_609.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ma_damped_trend_374.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ma_damped_trend_958.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ma_damped_trend_71.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ma_damped_trend_194.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ma_damped_trend_964.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ma_damped_trend_908.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ma_damped_trend_221.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ma_damped_trend_341.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `ma_damped_trend_204.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `ma_damped_trend_919.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `ma_damped_trend_197.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `ma_damped_trend_783.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `ma_damped_trend_608.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `ma_damped_trend_241.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `ma_damped_trend_349.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `ma_damped_trend_358.csv` | `stochastic_trend + point_anomaly` | ✗ NONE |
| `short` | `ma_damped_trend_656.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `ma_damped_trend_292.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ma_exponential_trend_76.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ma_exponential_trend_414.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ma_exponential_trend_286.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `ma_exponential_trend_731.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ma_exponential_trend_683.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `ma_exponential_trend_885.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ma_exponential_trend_341.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `ma_exponential_trend_564.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `ma_exponential_trend_549.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `ma_exponential_trend_33.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ma_exponential_trend_933.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ma_exponential_trend_935.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ma_exponential_trend_879.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ma_exponential_trend_145.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ma_exponential_trend_183.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ma_exponential_trend_683.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ma_exponential_trend_489.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `ma_exponential_trend_863.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ma_exponential_trend_353.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ma_exponential_trend_139.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `ma_exponential_trend_1000.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `ma_exponential_trend_405.csv` | `deterministic_trend + point_anomaly` | ~ PARTIAL |
| `short` | `ma_exponential_trend_809.csv` | `stochastic_trend + mean_shift` | ✗ NONE |
| `short` | `ma_exponential_trend_218.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `ma_exponential_trend_686.csv` | `stochastic_trend + trend_shift` | ✗ NONE |
| `short` | `ma_exponential_trend_34.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `ma_exponential_trend_247.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `ma_exponential_trend_782.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `short` | `ma_exponential_trend_505.csv` | `stochastic_trend + trend_shift` | ✗ NONE |
| `short` | `ma_exponential_trend_606.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ma_linear_down_trend_749.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `ma_linear_down_trend_492.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `ma_linear_down_trend_615.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `ma_linear_down_trend_106.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `ma_linear_down_trend_200.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `ma_linear_down_trend_168.csv` | `stationary` | ✗ NONE |
| `long` | `ma_linear_down_trend_97.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `ma_linear_down_trend_912.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `ma_linear_down_trend_735.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `ma_linear_down_trend_931.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ma_linear_down_trend_235.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ma_linear_down_trend_600.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ma_linear_down_trend_130.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ma_linear_down_trend_868.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ma_linear_down_trend_439.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ma_linear_down_trend_635.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ma_linear_down_trend_607.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ma_linear_down_trend_234.csv` | `stationary + mean_shift` | ✗ NONE |
| `medium` | `ma_linear_down_trend_495.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ma_linear_down_trend_215.csv` | `deterministic_trend + mean_shift` | ~ PARTIAL |
| `short` | `ma_linear_down_trend_136.csv` | `stationary + trend_shift` | ✗ NONE |
| `short` | `ma_linear_down_trend_382.csv` | `stochastic_trend` | ✗ NONE |
| `short` | `ma_linear_down_trend_434.csv` | `stochastic_trend` | ✗ NONE |
| `short` | `ma_linear_down_trend_927.csv` | `stochastic_trend` | ✗ NONE |
| `short` | `ma_linear_down_trend_959.csv` | `stationary + trend_shift` | ✗ NONE |
| `short` | `ma_linear_down_trend_832.csv` | `stationary + collective_anomaly + point_anomaly + trend_shift` | ✗ NONE |
| `short` | `ma_linear_down_trend_995.csv` | `stationary + trend_shift` | ✗ NONE |
| `short` | `ma_linear_down_trend_892.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `short` | `ma_linear_down_trend_134.csv` | `stationary + trend_shift` | ✗ NONE |
| `short` | `ma_linear_down_trend_428.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `ma_linear_up_trend_292.csv` | `stationary` | ✗ NONE |
| `long` | `ma_linear_up_trend_727.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `ma_linear_up_trend_328.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `ma_linear_up_trend_712.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `ma_linear_up_trend_193.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `ma_linear_up_trend_424.csv` | `stationary + mean_shift` | ✗ NONE |
| `long` | `ma_linear_up_trend_817.csv` | `stationary` | ✗ NONE |
| `long` | `ma_linear_up_trend_614.csv` | `stationary` | ✗ NONE |
| `long` | `ma_linear_up_trend_913.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `ma_linear_up_trend_904.csv` | `stationary` | ✗ NONE |
| `medium` | `ma_linear_up_trend_473.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ma_linear_up_trend_997.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ma_linear_up_trend_670.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ma_linear_up_trend_79.csv` | `stationary + mean_shift + trend_shift + variance_shift` | ✗ NONE |
| `medium` | `ma_linear_up_trend_240.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ma_linear_up_trend_951.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ma_linear_up_trend_956.csv` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `medium` | `ma_linear_up_trend_316.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ma_linear_up_trend_896.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `ma_linear_up_trend_248.csv` | `stationary + trend_shift` | ✗ NONE |
| `short` | `ma_linear_up_trend_999.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `short` | `ma_linear_up_trend_836.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `short` | `ma_linear_up_trend_846.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `short` | `ma_linear_up_trend_261.csv` | `stationary + mean_shift + point_anomaly + trend_shift` | ✗ NONE |
| `short` | `ma_linear_up_trend_910.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `short` | `ma_linear_up_trend_479.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `short` | `ma_linear_up_trend_120.csv` | `stochastic_trend + mean_shift` | ✗ NONE |
| `short` | `ma_linear_up_trend_263.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `short` | `ma_linear_up_trend_778.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `short` | `ma_linear_up_trend_950.csv` | `stochastic_trend + mean_shift + point_anomaly + trend_shift` | ✗ NONE |
| `long` | `ma_quadratic_trend_404.csv` | `stationary` | ✗ NONE |
| `long` | `ma_quadratic_trend_82.csv` | `stationary` | ✗ NONE |
| `long` | `ma_quadratic_trend_957.csv` | `stationary` | ✗ NONE |
| `long` | `ma_quadratic_trend_478.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `ma_quadratic_trend_838.csv` | `stationary` | ✗ NONE |
| `long` | `ma_quadratic_trend_715.csv` | `stationary` | ✗ NONE |
| `long` | `ma_quadratic_trend_895.csv` | `stationary` | ✗ NONE |
| `long` | `ma_quadratic_trend_776.csv` | `stationary + point_anomaly` | ✗ NONE |
| `long` | `ma_quadratic_trend_846.csv` | `stationary + point_anomaly` | ✗ NONE |
| `long` | `ma_quadratic_trend_327.csv` | `stationary` | ✗ NONE |
| `medium` | `ma_quadratic_trend_344.csv` | `stationary + collective_anomaly + point_anomaly` | ✗ NONE |
| `medium` | `ma_quadratic_trend_245.csv` | `stationary + collective_anomaly` | ✗ NONE |
| `medium` | `ma_quadratic_trend_824.csv` | `stationary + collective_anomaly` | ✗ NONE |
| `medium` | `ma_quadratic_trend_745.csv` | `stationary + collective_anomaly + point_anomaly + trend_shift` | ✗ NONE |
| `medium` | `ma_quadratic_trend_198.csv` | `stationary + collective_anomaly` | ✗ NONE |
| `medium` | `ma_quadratic_trend_450.csv` | `stationary + collective_anomaly` | ✗ NONE |
| `medium` | `ma_quadratic_trend_902.csv` | `stationary + collective_anomaly` | ✗ NONE |
| `medium` | `ma_quadratic_trend_133.csv` | `stationary + point_anomaly` | ✗ NONE |
| `medium` | `ma_quadratic_trend_890.csv` | `stationary + collective_anomaly` | ✗ NONE |
| `medium` | `ma_quadratic_trend_531.csv` | `stationary + collective_anomaly` | ✗ NONE |
| `short` | `ma_quadratic_trend_302.csv` | `stationary + collective_anomaly` | ✗ NONE |
| `short` | `ma_quadratic_trend_282.csv` | `volatility + collective_anomaly + trend_shift` | ✗ NONE |
| `short` | `ma_quadratic_trend_851.csv` | `stationary + collective_anomaly` | ✗ NONE |
| `short` | `ma_quadratic_trend_945.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `short` | `ma_quadratic_trend_522.csv` | `stationary` | ✗ NONE |
| `short` | `ma_quadratic_trend_420.csv` | `stationary` | ✗ NONE |
| `short` | `ma_quadratic_trend_38.csv` | `stationary + trend_shift` | ✗ NONE |
| `short` | `ma_quadratic_trend_855.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✗ NONE |
| `short` | `ma_quadratic_trend_831.csv` | `stationary` | ✗ NONE |
| `short` | `ma_quadratic_trend_901.csv` | `stationary + collective_anomaly` | ✗ NONE |
| `long` | `white_noise_cubic_trend_308.csv` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `long` | `white_noise_cubic_trend_303.csv` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `long` | `white_noise_cubic_trend_12.csv` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `long` | `white_noise_cubic_trend_706.csv` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `long` | `white_noise_cubic_trend_276.csv` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `long` | `white_noise_cubic_trend_466.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `white_noise_cubic_trend_400.csv` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `long` | `white_noise_cubic_trend_355.csv` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `long` | `white_noise_cubic_trend_896.csv` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `long` | `white_noise_cubic_trend_162.csv` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `medium` | `white_noise_cubic_trend_990.csv` | `stationary` | ✗ NONE |
| `medium` | `white_noise_cubic_trend_810.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `white_noise_cubic_trend_355.csv` | `stationary` | ✗ NONE |
| `medium` | `white_noise_cubic_trend_421.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `white_noise_cubic_trend_69.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `white_noise_cubic_trend_568.csv` | `deterministic_trend + mean_shift + trend_shift` | ~ PARTIAL |
| `medium` | `white_noise_cubic_trend_467.csv` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `medium` | `white_noise_cubic_trend_724.csv` | `stationary + mean_shift + trend_shift` | ✗ NONE |
| `medium` | `white_noise_cubic_trend_876.csv` | `stationary` | ✗ NONE |
| `medium` | `white_noise_cubic_trend_593.csv` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `short` | `white_noise_cubic_trend_403.csv` | `stochastic_trend + trend_shift` | ✗ NONE |
| `short` | `white_noise_cubic_trend_964.csv` | `deterministic_trend + point_anomaly + trend_shift` | ~ PARTIAL |
| `short` | `white_noise_cubic_trend_123.csv` | `stochastic_trend` | ✗ NONE |
| `short` | `white_noise_cubic_trend_204.csv` | `stationary + mean_shift + point_anomaly + trend_shift` | ✗ NONE |
| `short` | `white_noise_cubic_trend_907.csv` | `stochastic_trend + point_anomaly + trend_shift` | ✗ NONE |
| `short` | `white_noise_cubic_trend_993.csv` | `stochastic_trend + point_anomaly + trend_shift` | ✗ NONE |
| `short` | `white_noise_cubic_trend_339.csv` | `stochastic_trend + point_anomaly + trend_shift` | ✗ NONE |
| `short` | `white_noise_cubic_trend_262.csv` | `stochastic_trend + collective_anomaly + point_anomaly` | ✗ NONE |
| `short` | `white_noise_cubic_trend_633.csv` | `stochastic_trend + point_anomaly` | ✗ NONE |
| `short` | `white_noise_cubic_trend_986.csv` | `stochastic_trend + point_anomaly + trend_shift` | ✗ NONE |
| `long` | `white_noise_damped_trend_342.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `white_noise_damped_trend_133.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `white_noise_damped_trend_199.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `white_noise_damped_trend_648.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `white_noise_damped_trend_499.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `white_noise_damped_trend_416.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `white_noise_damped_trend_770.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `white_noise_damped_trend_823.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `white_noise_damped_trend_388.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `white_noise_damped_trend_50.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `white_noise_damped_trend_657.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `white_noise_damped_trend_57.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `white_noise_damped_trend_204.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `white_noise_damped_trend_453.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `white_noise_damped_trend_928.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `white_noise_damped_trend_63.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `white_noise_damped_trend_273.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `white_noise_damped_trend_332.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `white_noise_damped_trend_139.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `white_noise_damped_trend_751.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `white_noise_damped_trend_50.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `white_noise_damped_trend_10.csv` | `stochastic_trend` | ✗ NONE |
| `short` | `white_noise_damped_trend_578.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `white_noise_damped_trend_951.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `white_noise_damped_trend_841.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `white_noise_damped_trend_595.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `white_noise_damped_trend_731.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `white_noise_damped_trend_761.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `white_noise_damped_trend_965.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `white_noise_damped_trend_782.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `white_noise_exponential_trend_778.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `white_noise_exponential_trend_716.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `white_noise_exponential_trend_28.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `white_noise_exponential_trend_433.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `white_noise_exponential_trend_496.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `white_noise_exponential_trend_162.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `white_noise_exponential_trend_973.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `white_noise_exponential_trend_710.csv` | `deterministic_trend` | ✓ FULL |
| `long` | `white_noise_exponential_trend_947.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `white_noise_exponential_trend_402.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `white_noise_exponential_trend_673.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `white_noise_exponential_trend_388.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `white_noise_exponential_trend_71.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `white_noise_exponential_trend_880.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `white_noise_exponential_trend_212.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `white_noise_exponential_trend_762.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `white_noise_exponential_trend_928.csv` | `deterministic_trend` | ✓ FULL |
| `medium` | `white_noise_exponential_trend_375.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `white_noise_exponential_trend_566.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `white_noise_exponential_trend_383.csv` | `stationary + trend_shift` | ✗ NONE |
| `short` | `white_noise_exponential_trend_712.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `white_noise_exponential_trend_475.csv` | `stochastic_trend + trend_shift` | ✗ NONE |
| `short` | `white_noise_exponential_trend_4.csv` | `stochastic_trend` | ✗ NONE |
| `short` | `white_noise_exponential_trend_47.csv` | `stochastic_trend` | ✗ NONE |
| `short` | `white_noise_exponential_trend_740.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `short` | `white_noise_exponential_trend_370.csv` | `deterministic_trend` | ✓ FULL |
| `short` | `white_noise_exponential_trend_609.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `short` | `white_noise_exponential_trend_215.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `short` | `white_noise_exponential_trend_275.csv` | `stochastic_trend` | ✗ NONE |
| `short` | `white_noise_exponential_trend_486.csv` | `stochastic_trend + trend_shift` | ✗ NONE |
| `long` | `white_noise_linear_down_trend_710.csv` | `stationary + mean_shift` | ✗ NONE |
| `long` | `white_noise_linear_down_trend_965.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `white_noise_linear_down_trend_448.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `white_noise_linear_down_trend_722.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `white_noise_linear_down_trend_789.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `white_noise_linear_down_trend_930.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `white_noise_linear_down_trend_259.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `white_noise_linear_down_trend_666.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `white_noise_linear_down_trend_622.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `white_noise_linear_down_trend_376.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `white_noise_linear_down_trend_472.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `white_noise_linear_down_trend_603.csv` | `stationary + mean_shift + variance_shift` | ✗ NONE |
| `medium` | `white_noise_linear_down_trend_867.csv` | `stationary + mean_shift + trend_shift` | ✗ NONE |
| `medium` | `white_noise_linear_down_trend_1.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `white_noise_linear_down_trend_379.csv` | `stationary + mean_shift + trend_shift` | ✗ NONE |
| `medium` | `white_noise_linear_down_trend_362.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `white_noise_linear_down_trend_292.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `white_noise_linear_down_trend_495.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `white_noise_linear_down_trend_822.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `white_noise_linear_down_trend_632.csv` | `stationary + trend_shift` | ✗ NONE |
| `short` | `white_noise_linear_down_trend_658.csv` | `stationary + trend_shift` | ✗ NONE |
| `short` | `white_noise_linear_down_trend_701.csv` | `stochastic_trend + trend_shift` | ✗ NONE |
| `short` | `white_noise_linear_down_trend_395.csv` | `stochastic_trend + point_anomaly + trend_shift` | ✗ NONE |
| `short` | `white_noise_linear_down_trend_527.csv` | `stationary + trend_shift` | ✗ NONE |
| `short` | `white_noise_linear_down_trend_505.csv` | `stochastic_trend + collective_anomaly + trend_shift` | ✗ NONE |
| `short` | `white_noise_linear_down_trend_720.csv` | `stochastic_trend + trend_shift` | ✗ NONE |
| `short` | `white_noise_linear_down_trend_295.csv` | `stochastic_trend + trend_shift` | ✗ NONE |
| `short` | `white_noise_linear_down_trend_57.csv` | `stationary + trend_shift` | ✗ NONE |
| `short` | `white_noise_linear_down_trend_534.csv` | `stationary + trend_shift` | ✗ NONE |
| `short` | `white_noise_linear_down_trend_83.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `white_noise_linear_up_trend_929.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `white_noise_linear_up_trend_983.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `white_noise_linear_up_trend_832.csv` | `stationary + mean_shift` | ✗ NONE |
| `long` | `white_noise_linear_up_trend_777.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `white_noise_linear_up_trend_254.csv` | `stationary + mean_shift + variance_shift` | ✗ NONE |
| `long` | `white_noise_linear_up_trend_705.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `white_noise_linear_up_trend_176.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `white_noise_linear_up_trend_36.csv` | `stationary + mean_shift` | ✗ NONE |
| `long` | `white_noise_linear_up_trend_573.csv` | `stationary + trend_shift` | ✗ NONE |
| `long` | `white_noise_linear_up_trend_71.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `white_noise_linear_up_trend_682.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `white_noise_linear_up_trend_67.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `white_noise_linear_up_trend_407.csv` | `stationary + mean_shift + trend_shift` | ✗ NONE |
| `medium` | `white_noise_linear_up_trend_184.csv` | `stationary + mean_shift + trend_shift` | ✗ NONE |
| `medium` | `white_noise_linear_up_trend_853.csv` | `stationary + mean_shift + trend_shift` | ✗ NONE |
| `medium` | `white_noise_linear_up_trend_976.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `white_noise_linear_up_trend_791.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `white_noise_linear_up_trend_314.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `white_noise_linear_up_trend_718.csv` | `stationary + trend_shift` | ✗ NONE |
| `medium` | `white_noise_linear_up_trend_384.csv` | `stationary + trend_shift` | ✗ NONE |
| `short` | `white_noise_linear_up_trend_305.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `short` | `white_noise_linear_up_trend_841.csv` | `stationary + mean_shift + trend_shift` | ✗ NONE |
| `short` | `white_noise_linear_up_trend_281.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `short` | `white_noise_linear_up_trend_233.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `short` | `white_noise_linear_up_trend_120.csv` | `stationary + mean_shift + trend_shift` | ✗ NONE |
| `short` | `white_noise_linear_up_trend_140.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `short` | `white_noise_linear_up_trend_323.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `short` | `white_noise_linear_up_trend_536.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `short` | `white_noise_linear_up_trend_661.csv` | `stochastic_trend + collective_anomaly + mean_shift + trend_shift` | ✗ NONE |
| `short` | `white_noise_linear_up_trend_882.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `long` | `white_noise_quadratic_trend_806.csv` | `stationary` | ✗ NONE |
| `long` | `white_noise_quadratic_trend_165.csv` | `stationary` | ✗ NONE |
| `long` | `white_noise_quadratic_trend_518.csv` | `stationary + collective_anomaly` | ✗ NONE |
| `long` | `white_noise_quadratic_trend_480.csv` | `stationary + point_anomaly` | ✗ NONE |
| `long` | `white_noise_quadratic_trend_915.csv` | `stationary` | ✗ NONE |
| `long` | `white_noise_quadratic_trend_679.csv` | `stationary + point_anomaly` | ✗ NONE |
| `long` | `white_noise_quadratic_trend_629.csv` | `stationary` | ✗ NONE |
| `long` | `white_noise_quadratic_trend_278.csv` | `stationary` | ✗ NONE |
| `long` | `white_noise_quadratic_trend_760.csv` | `stationary` | ✗ NONE |
| `long` | `white_noise_quadratic_trend_740.csv` | `stationary + contextual_anomaly + point_anomaly` | ✗ NONE |
| `medium` | `white_noise_quadratic_trend_452.csv` | `stationary + contextual_anomaly + point_anomaly + trend_shift` | ✗ NONE |
| `medium` | `white_noise_quadratic_trend_554.csv` | `stationary + collective_anomaly + point_anomaly` | ✗ NONE |
| `medium` | `white_noise_quadratic_trend_467.csv` | `stationary + collective_anomaly` | ✗ NONE |
| `medium` | `white_noise_quadratic_trend_322.csv` | `stationary + contextual_anomaly + point_anomaly` | ✗ NONE |
| `medium` | `white_noise_quadratic_trend_234.csv` | `stationary + collective_anomaly` | ✗ NONE |
| `medium` | `white_noise_quadratic_trend_702.csv` | `stationary + collective_anomaly + point_anomaly` | ✗ NONE |
| `medium` | `white_noise_quadratic_trend_732.csv` | `stationary + contextual_anomaly + point_anomaly` | ✗ NONE |
| `medium` | `white_noise_quadratic_trend_102.csv` | `stationary + contextual_anomaly + point_anomaly` | ✗ NONE |
| `medium` | `white_noise_quadratic_trend_921.csv` | `stationary + collective_anomaly` | ✗ NONE |
| `medium` | `white_noise_quadratic_trend_790.csv` | `stationary + collective_anomaly` | ✗ NONE |
| `short` | `white_noise_quadratic_trend_892.csv` | `stationary + trend_shift` | ✗ NONE |
| `short` | `white_noise_quadratic_trend_808.csv` | `stationary + collective_anomaly + point_anomaly` | ✗ NONE |
| `short` | `white_noise_quadratic_trend_914.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✗ NONE |
| `short` | `white_noise_quadratic_trend_197.csv` | `stationary + collective_anomaly + point_anomaly` | ✗ NONE |
| `short` | `white_noise_quadratic_trend_816.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✗ NONE |
| `short` | `white_noise_quadratic_trend_490.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✗ NONE |
| `short` | `white_noise_quadratic_trend_30.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✗ NONE |
| `short` | `white_noise_quadratic_trend_260.csv` | `stationary + contextual_anomaly + point_anomaly` | ✗ NONE |
| `short` | `white_noise_quadratic_trend_84.csv` | `stationary + point_anomaly` | ✗ NONE |
| `short` | `white_noise_quadratic_trend_981.csv` | `stationary + collective_anomaly + point_anomaly` | ✗ NONE |
---

## Grup 3: stochastic_trend
**Beklenen:** `stochastic_trend`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `stochastic_ari_long` | `ari_74.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_ari_long` | `ari_576.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_ari_long` | `ari_526.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_ari_long` | `ari_144.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_ari_long` | `ari_611.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_ari_long` | `ari_328.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_ari_long` | `ari_944.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_ari_long` | `ari_880.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_ari_long` | `ari_21.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_ari_long` | `ari_519.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_ari_medium` | `ari_220.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_ari_medium` | `ari_837.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_ari_medium` | `ari_526.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_ari_medium` | `ari_713.csv` | `stationary + mean_shift + trend_shift` | ✗ NONE |
| `stochastic_ari_medium` | `ari_588.csv` | `stationary` | ✗ NONE |
| `stochastic_ari_medium` | `ari_613.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_ari_medium` | `ari_647.csv` | `stochastic_trend + mean_shift + trend_shift` | ~ PARTIAL |
| `stochastic_ari_medium` | `ari_390.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_ari_medium` | `ari_974.csv` | `stochastic_trend + trend_shift` | ~ PARTIAL |
| `stochastic_ari_medium` | `ari_795.csv` | `stationary + collective_anomaly + mean_shift` | ✗ NONE |
| `stochastic_ari_short` | `ari_92.csv` | `stochastic_trend + mean_shift` | ~ PARTIAL |
| `stochastic_ari_short` | `ari_506.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_ari_short` | `ari_663.csv` | `stochastic_trend + mean_shift` | ~ PARTIAL |
| `stochastic_ari_short` | `ari_85.csv` | `stochastic_trend + mean_shift` | ~ PARTIAL |
| `stochastic_ari_short` | `ari_761.csv` | `stochastic_trend + mean_shift` | ~ PARTIAL |
| `stochastic_ari_short` | `ari_920.csv` | `stochastic_trend + point_anomaly + trend_shift` | ~ PARTIAL |
| `stochastic_ari_short` | `ari_563.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_ari_short` | `ari_491.csv` | `stochastic_trend + mean_shift` | ~ PARTIAL |
| `stochastic_ari_short` | `ari_864.csv` | `stochastic_trend + trend_shift` | ~ PARTIAL |
| `stochastic_ari_short` | `ari_934.csv` | `stochastic_trend + mean_shift` | ~ PARTIAL |
| `stochastic_arima_long` | `arima_603.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_arima_long` | `arima_509.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_arima_long` | `arima_925.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_arima_long` | `arima_244.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_arima_long` | `arima_784.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_arima_long` | `arima_893.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_arima_long` | `arima_536.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_arima_long` | `arima_512.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_arima_long` | `arima_337.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_arima_long` | `arima_791.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_arima_medium` | `arima_326.csv` | `stochastic_trend + trend_shift` | ~ PARTIAL |
| `stochastic_arima_medium` | `arima_873.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_arima_medium` | `arima_686.csv` | `stationary + trend_shift` | ✗ NONE |
| `stochastic_arima_medium` | `arima_353.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_arima_medium` | `arima_804.csv` | `stochastic_trend + trend_shift` | ~ PARTIAL |
| `stochastic_arima_medium` | `arima_815.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_arima_medium` | `arima_579.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_arima_medium` | `arima_545.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_arima_medium` | `arima_676.csv` | `stationary + mean_shift` | ✗ NONE |
| `stochastic_arima_medium` | `arima_318.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_arima_short` | `arima_351.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_arima_short` | `arima_503.csv` | `stochastic_trend + mean_shift` | ~ PARTIAL |
| `stochastic_arima_short` | `arima_17.csv` | `stochastic_trend + point_anomaly + trend_shift` | ~ PARTIAL |
| `stochastic_arima_short` | `arima_756.csv` | `stochastic_trend + mean_shift + trend_shift` | ~ PARTIAL |
| `stochastic_arima_short` | `arima_361.csv` | `stochastic_trend + trend_shift` | ~ PARTIAL |
| `stochastic_arima_short` | `arima_314.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ~ PARTIAL |
| `stochastic_arima_short` | `arima_349.csv` | `stochastic_trend + mean_shift` | ~ PARTIAL |
| `stochastic_arima_short` | `arima_407.csv` | `stochastic_trend + collective_anomaly` | ~ PARTIAL |
| `stochastic_arima_short` | `arima_393.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_arima_short` | `arima_921.csv` | `stochastic_trend + mean_shift` | ~ PARTIAL |
| `stochastic_ima_long` | `ima_597.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_ima_long` | `ima_172.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_ima_long` | `ima_225.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_ima_long` | `ima_237.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_ima_long` | `ima_310.csv` | `stationary` | ✗ NONE |
| `stochastic_ima_long` | `ima_451.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_ima_long` | `ima_738.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_ima_long` | `ima_239.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_ima_long` | `ima_75.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_ima_long` | `ima_296.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_ima_medium` | `ima_157.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_ima_medium` | `ima_480.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_ima_medium` | `ima_474.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_ima_medium` | `ima_402.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_ima_medium` | `ima_599.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_ima_medium` | `ima_528.csv` | `stationary + mean_shift + point_anomaly + variance_shift` | ✗ NONE |
| `stochastic_ima_medium` | `ima_481.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_ima_medium` | `ima_155.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_ima_medium` | `ima_289.csv` | `stationary + mean_shift` | ✗ NONE |
| `stochastic_ima_medium` | `ima_866.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_ima_short` | `ima_486.csv` | `stochastic_trend + mean_shift` | ~ PARTIAL |
| `stochastic_ima_short` | `ima_457.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ~ PARTIAL |
| `stochastic_ima_short` | `ima_932.csv` | `stochastic_trend + mean_shift` | ~ PARTIAL |
| `stochastic_ima_short` | `ima_808.csv` | `stochastic_trend + trend_shift` | ~ PARTIAL |
| `stochastic_ima_short` | `ima_637.csv` | `stochastic_trend + collective_anomaly + mean_shift + point_anomaly` | ~ PARTIAL |
| `stochastic_ima_short` | `ima_970.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_ima_short` | `ima_74.csv` | `stochastic_trend + mean_shift` | ~ PARTIAL |
| `stochastic_ima_short` | `ima_116.csv` | `stochastic_trend + mean_shift` | ~ PARTIAL |
| `stochastic_ima_short` | `ima_889.csv` | `stochastic_trend + mean_shift` | ~ PARTIAL |
| `stochastic_ima_short` | `ima_91.csv` | `stochastic_trend + collective_anomaly` | ~ PARTIAL |
| `stochastic_rw_long` | `random_walk_803.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_rw_long` | `random_walk_629.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_rw_long` | `random_walk_449.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_rw_long` | `random_walk_538.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_rw_long` | `random_walk_103.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_rw_long` | `random_walk_968.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_rw_long` | `random_walk_422.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_rw_long` | `random_walk_373.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_rw_long` | `random_walk_793.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_rw_long` | `random_walk_458.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_rw_medium` | `random_walk_885.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_rw_medium` | `random_walk_920.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_rw_medium` | `random_walk_978.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_rw_medium` | `random_walk_869.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_rw_medium` | `random_walk_485.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_rw_medium` | `random_walk_595.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_rw_medium` | `random_walk_788.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_rw_medium` | `random_walk_776.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_rw_medium` | `random_walk_601.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_rw_medium` | `random_walk_836.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_rw_short` | `random_walk_654.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ~ PARTIAL |
| `stochastic_rw_short` | `random_walk_926.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ~ PARTIAL |
| `stochastic_rw_short` | `random_walk_300.csv` | `stochastic_trend + mean_shift` | ~ PARTIAL |
| `stochastic_rw_short` | `random_walk_548.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_rw_short` | `random_walk_30.csv` | `stochastic_trend + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `stochastic_rw_short` | `random_walk_35.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ~ PARTIAL |
| `stochastic_rw_short` | `random_walk_50.csv` | `stochastic_trend + collective_anomaly` | ~ PARTIAL |
| `stochastic_rw_short` | `random_walk_546.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ~ PARTIAL |
| `stochastic_rw_short` | `random_walk_124.csv` | `stochastic_trend + mean_shift` | ~ PARTIAL |
| `stochastic_rw_short` | `random_walk_457.csv` | `stochastic_trend + mean_shift` | ~ PARTIAL |
| `stochastic_rwd_long` | `random_walk_drift_408.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_rwd_long` | `random_walk_drift_714.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_rwd_long` | `random_walk_drift_724.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_rwd_long` | `random_walk_drift_834.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_rwd_long` | `random_walk_drift_471.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_rwd_long` | `random_walk_drift_766.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_rwd_long` | `random_walk_drift_250.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_rwd_long` | `random_walk_drift_873.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_rwd_long` | `random_walk_drift_529.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_rwd_long` | `random_walk_drift_946.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_rwd_medium` | `random_walk_drift_215.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_rwd_medium` | `random_walk_drift_672.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_rwd_medium` | `random_walk_drift_590.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_rwd_medium` | `random_walk_drift_122.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_rwd_medium` | `random_walk_drift_934.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_rwd_medium` | `random_walk_drift_461.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_rwd_medium` | `random_walk_drift_644.csv` | `stochastic_trend + collective_anomaly + mean_shift + variance_shift` | ~ PARTIAL |
| `stochastic_rwd_medium` | `random_walk_drift_618.csv` | `stochastic_trend` | ✓ FULL |
| `stochastic_rwd_medium` | `random_walk_drift_709.csv` | `stochastic_trend + collective_anomaly + mean_shift + variance_shift` | ~ PARTIAL |
| `stochastic_rwd_medium` | `random_walk_drift_175.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `stochastic_rwd_short` | `random_walk_drift_691.csv` | `stochastic_trend + collective_anomaly` | ~ PARTIAL |
| `stochastic_rwd_short` | `random_walk_drift_493.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ~ PARTIAL |
| `stochastic_rwd_short` | `random_walk_drift_222.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ~ PARTIAL |
| `stochastic_rwd_short` | `random_walk_drift_898.csv` | `stochastic_trend + mean_shift` | ~ PARTIAL |
| `stochastic_rwd_short` | `random_walk_drift_523.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ~ PARTIAL |
| `stochastic_rwd_short` | `random_walk_drift_266.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ~ PARTIAL |
| `stochastic_rwd_short` | `random_walk_drift_144.csv` | `stochastic_trend + mean_shift` | ~ PARTIAL |
| `stochastic_rwd_short` | `random_walk_drift_338.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ~ PARTIAL |
| `stochastic_rwd_short` | `random_walk_drift_448.csv` | `stochastic_trend + mean_shift` | ~ PARTIAL |
| `stochastic_rwd_short` | `random_walk_drift_40.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ~ PARTIAL |
---

## Grup 4: volatility
**Beklenen:** `volatility`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `volatility_aparch_long` | `aparch_293.csv` | `volatility` | ✓ FULL |
| `volatility_aparch_long` | `aparch_517.csv` | `volatility` | ✓ FULL |
| `volatility_aparch_long` | `aparch_4.csv` | `volatility` | ✓ FULL |
| `volatility_aparch_long` | `aparch_409.csv` | `volatility` | ✓ FULL |
| `volatility_aparch_long` | `aparch_80.csv` | `volatility` | ✓ FULL |
| `volatility_aparch_long` | `aparch_909.csv` | `volatility` | ✓ FULL |
| `volatility_aparch_long` | `aparch_448.csv` | `volatility` | ✓ FULL |
| `volatility_aparch_long` | `aparch_354.csv` | `volatility` | ✓ FULL |
| `volatility_aparch_long` | `aparch_792.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `volatility_aparch_long` | `aparch_976.csv` | `volatility` | ✓ FULL |
| `volatility_aparch_medium` | `aparch_865.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `volatility_aparch_medium` | `aparch_487.csv` | `volatility` | ✓ FULL |
| `volatility_aparch_medium` | `aparch_330.csv` | `volatility` | ✓ FULL |
| `volatility_aparch_medium` | `aparch_868.csv` | `stationary + point_anomaly + variance_shift` | ✗ NONE |
| `volatility_aparch_medium` | `aparch_173.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `volatility_aparch_medium` | `aparch_531.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `volatility_aparch_medium` | `aparch_115.csv` | `volatility` | ✓ FULL |
| `volatility_aparch_medium` | `aparch_79.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `volatility_aparch_medium` | `aparch_596.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `volatility_aparch_medium` | `aparch_146.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `volatility_aparch_short` | `aparch_976.csv` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
| `volatility_aparch_short` | `aparch_420.csv` | `volatility + collective_anomaly` | ~ PARTIAL |
| `volatility_aparch_short` | `aparch_304.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `volatility_aparch_short` | `aparch_698.csv` | `volatility + collective_anomaly` | ~ PARTIAL |
| `volatility_aparch_short` | `aparch_161.csv` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
| `volatility_aparch_short` | `aparch_818.csv` | `volatility + collective_anomaly + trend_shift` | ~ PARTIAL |
| `volatility_aparch_short` | `aparch_981.csv` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
| `volatility_aparch_short` | `aparch_7.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `volatility_aparch_short` | `aparch_135.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `volatility_aparch_short` | `aparch_794.csv` | `volatility + collective_anomaly` | ~ PARTIAL |
| `volatility_arch_long` | `arch_126.csv` | `volatility` | ✓ FULL |
| `volatility_arch_long` | `arch_974.csv` | `volatility` | ✓ FULL |
| `volatility_arch_long` | `arch_326.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `volatility_arch_long` | `arch_282.csv` | `volatility` | ✓ FULL |
| `volatility_arch_long` | `arch_872.csv` | `volatility` | ✓ FULL |
| `volatility_arch_long` | `arch_116.csv` | `volatility` | ✓ FULL |
| `volatility_arch_long` | `arch_671.csv` | `volatility` | ✓ FULL |
| `volatility_arch_long` | `arch_239.csv` | `volatility` | ✓ FULL |
| `volatility_arch_long` | `arch_318.csv` | `volatility` | ✓ FULL |
| `volatility_arch_long` | `arch_214.csv` | `volatility` | ✓ FULL |
| `volatility_arch_medium` | `arch_534.csv` | `volatility` | ✓ FULL |
| `volatility_arch_medium` | `arch_715.csv` | `volatility + mean_shift` | ~ PARTIAL |
| `volatility_arch_medium` | `arch_203.csv` | `volatility` | ✓ FULL |
| `volatility_arch_medium` | `arch_618.csv` | `volatility` | ✓ FULL |
| `volatility_arch_medium` | `arch_972.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `volatility_arch_medium` | `arch_3.csv` | `volatility` | ✓ FULL |
| `volatility_arch_medium` | `arch_527.csv` | `volatility` | ✓ FULL |
| `volatility_arch_medium` | `arch_743.csv` | `volatility` | ✓ FULL |
| `volatility_arch_medium` | `arch_334.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `volatility_arch_medium` | `arch_805.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `volatility_arch_short` | `arch_438.csv` | `volatility + point_anomaly` | ~ PARTIAL |
| `volatility_arch_short` | `arch_252.csv` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
| `volatility_arch_short` | `arch_657.csv` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
| `volatility_arch_short` | `arch_658.csv` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
| `volatility_arch_short` | `arch_987.csv` | `volatility + point_anomaly` | ~ PARTIAL |
| `volatility_arch_short` | `arch_788.csv` | `volatility + mean_shift + variance_shift` | ~ PARTIAL |
| `volatility_arch_short` | `arch_760.csv` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
| `volatility_arch_short` | `arch_203.csv` | `volatility + point_anomaly` | ~ PARTIAL |
| `volatility_arch_short` | `arch_815.csv` | `volatility + point_anomaly` | ~ PARTIAL |
| `volatility_arch_short` | `arch_853.csv` | `volatility + collective_anomaly` | ~ PARTIAL |
| `volatility_egarch_long` | `egarch_249.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `volatility_egarch_long` | `egarch_988.csv` | `volatility` | ✓ FULL |
| `volatility_egarch_long` | `egarch_385.csv` | `volatility` | ✓ FULL |
| `volatility_egarch_long` | `egarch_198.csv` | `volatility` | ✓ FULL |
| `volatility_egarch_long` | `egarch_631.csv` | `volatility` | ✓ FULL |
| `volatility_egarch_long` | `egarch_121.csv` | `volatility` | ✓ FULL |
| `volatility_egarch_long` | `egarch_955.csv` | `volatility` | ✓ FULL |
| `volatility_egarch_long` | `egarch_386.csv` | `volatility` | ✓ FULL |
| `volatility_egarch_long` | `egarch_629.csv` | `volatility` | ✓ FULL |
| `volatility_egarch_long` | `egarch_722.csv` | `volatility` | ✓ FULL |
| `volatility_egarch_medium` | `egarch_935.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `volatility_egarch_medium` | `egarch_982.csv` | `volatility` | ✓ FULL |
| `volatility_egarch_medium` | `egarch_444.csv` | `volatility` | ✓ FULL |
| `volatility_egarch_medium` | `egarch_464.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `volatility_egarch_medium` | `egarch_967.csv` | `volatility + collective_anomaly + mean_shift` | ~ PARTIAL |
| `volatility_egarch_medium` | `egarch_758.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `volatility_egarch_medium` | `egarch_281.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `volatility_egarch_medium` | `egarch_168.csv` | `volatility + point_anomaly` | ~ PARTIAL |
| `volatility_egarch_medium` | `egarch_644.csv` | `volatility + point_anomaly` | ~ PARTIAL |
| `volatility_egarch_medium` | `egarch_735.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `volatility_egarch_short` | `egarch_864.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `volatility_egarch_short` | `egarch_677.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `volatility_egarch_short` | `egarch_321.csv` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
| `volatility_egarch_short` | `egarch_192.csv` | `volatility + collective_anomaly + mean_shift` | ~ PARTIAL |
| `volatility_egarch_short` | `egarch_740.csv` | `volatility + collective_anomaly` | ~ PARTIAL |
| `volatility_egarch_short` | `egarch_810.csv` | `volatility + collective_anomaly` | ~ PARTIAL |
| `volatility_egarch_short` | `egarch_376.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `volatility_egarch_short` | `egarch_882.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly + variance_shift` | ~ PARTIAL |
| `volatility_egarch_short` | `egarch_729.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `volatility_egarch_short` | `egarch_651.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `volatility_garch_long` | `garch_840.csv` | `volatility` | ✓ FULL |
| `volatility_garch_long` | `garch_209.csv` | `volatility` | ✓ FULL |
| `volatility_garch_long` | `garch_832.csv` | `volatility` | ✓ FULL |
| `volatility_garch_long` | `garch_62.csv` | `volatility` | ✓ FULL |
| `volatility_garch_long` | `garch_82.csv` | `volatility` | ✓ FULL |
| `volatility_garch_long` | `garch_136.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `volatility_garch_long` | `garch_418.csv` | `volatility` | ✓ FULL |
| `volatility_garch_long` | `garch_59.csv` | `volatility` | ✓ FULL |
| `volatility_garch_long` | `garch_493.csv` | `volatility` | ✓ FULL |
| `volatility_garch_long` | `garch_708.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `volatility_garch_medium` | `garch_44.csv` | `volatility + mean_shift + variance_shift` | ~ PARTIAL |
| `volatility_garch_medium` | `garch_161.csv` | `volatility` | ✓ FULL |
| `volatility_garch_medium` | `garch_565.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `volatility_garch_medium` | `garch_696.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `volatility_garch_medium` | `garch_412.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `volatility_garch_medium` | `garch_109.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `volatility_garch_medium` | `garch_881.csv` | `volatility + point_anomaly` | ~ PARTIAL |
| `volatility_garch_medium` | `garch_486.csv` | `volatility` | ✓ FULL |
| `volatility_garch_medium` | `garch_857.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `volatility_garch_medium` | `garch_55.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `volatility_garch_short` | `garch_196.csv` | `volatility + point_anomaly + variance_shift` | ~ PARTIAL |
| `volatility_garch_short` | `garch_498.csv` | `volatility + collective_anomaly` | ~ PARTIAL |
| `volatility_garch_short` | `garch_984.csv` | `volatility + point_anomaly` | ~ PARTIAL |
| `volatility_garch_short` | `garch_431.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `volatility_garch_short` | `garch_684.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `volatility_garch_short` | `garch_92.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `volatility_garch_short` | `garch_862.csv` | `volatility + mean_shift + point_anomaly` | ~ PARTIAL |
| `volatility_garch_short` | `garch_521.csv` | `volatility + collective_anomaly + mean_shift` | ~ PARTIAL |
| `volatility_garch_short` | `garch_750.csv` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
| `volatility_garch_short` | `garch_239.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
---

## Grup 5: collective_anomaly
**Beklenen:** `stationary + collective_anomaly`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `multiple` | `ar_collective_anomaly_5.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `multiple` | `ar_collective_anomaly_260.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `multiple` | `ar_collective_anomaly_775.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `multiple` | `ar_collective_anomaly_58.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `multiple` | `ar_collective_anomaly_989.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `multiple` | `ar_collective_anomaly_699.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `multiple` | `ar_collective_anomaly_347.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `multiple` | `ar_collective_anomaly_666.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `multiple` | `ar_collective_anomaly_843.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `multiple` | `ar_collective_anomaly_946.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `beginning` | `ar_collective_anomaly_595.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `beginning` | `ar_collective_anomaly_812.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `beginning` | `ar_collective_anomaly_544.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `beginning` | `ar_collective_anomaly_527.csv` | `stationary` | ~ PARTIAL |
| `beginning` | `ar_collective_anomaly_50.csv` | `stationary` | ~ PARTIAL |
| `beginning` | `ar_collective_anomaly_86.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `beginning` | `ar_collective_anomaly_772.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `beginning` | `ar_collective_anomaly_644.csv` | `stationary + point_anomaly` | ~ PARTIAL |
| `beginning` | `ar_collective_anomaly_345.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `beginning` | `ar_collective_anomaly_396.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `end` | `ar_collective_anomaly_884.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `end` | `ar_collective_anomaly_324.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `end` | `ar_collective_anomaly_864.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `end` | `ar_collective_anomaly_960.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `end` | `ar_collective_anomaly_178.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `end` | `ar_collective_anomaly_355.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `end` | `ar_collective_anomaly_910.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `end` | `ar_collective_anomaly_513.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `end` | `ar_collective_anomaly_322.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `end` | `ar_collective_anomaly_790.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `middle` | `ar_collective_anomaly_526.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `ar_collective_anomaly_623.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `ar_collective_anomaly_660.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `ar_collective_anomaly_714.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `ar_collective_anomaly_448.csv` | `stationary` | ~ PARTIAL |
| `middle` | `ar_collective_anomaly_408.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `ar_collective_anomaly_124.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `ar_collective_anomaly_554.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `ar_collective_anomaly_883.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `ar_collective_anomaly_398.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `multiple` | `ar_collective_anomaly_266.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `multiple` | `ar_collective_anomaly_548.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `multiple` | `ar_collective_anomaly_294.csv` | `stationary + collective_anomaly + mean_shift + trend_shift` | ✓ FULL |
| `multiple` | `ar_collective_anomaly_425.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `multiple` | `ar_collective_anomaly_833.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `multiple` | `ar_collective_anomaly_336.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `multiple` | `ar_collective_anomaly_411.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `multiple` | `ar_collective_anomaly_356.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `multiple` | `ar_collective_anomaly_91.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `multiple` | `ar_collective_anomaly_648.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `beginning` | `ar_collective_anomaly_745.csv` | `stationary + collective_anomaly + mean_shift + point_anomaly` | ✓ FULL |
| `beginning` | `ar_collective_anomaly_91.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `beginning` | `ar_collective_anomaly_352.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `beginning` | `ar_collective_anomaly_610.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `beginning` | `ar_collective_anomaly_107.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `beginning` | `ar_collective_anomaly_575.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `beginning` | `ar_collective_anomaly_972.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `beginning` | `ar_collective_anomaly_274.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `beginning` | `ar_collective_anomaly_177.csv` | `stationary + point_anomaly` | ~ PARTIAL |
| `beginning` | `ar_collective_anomaly_320.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `end` | `ar_collective_anomaly_762.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `end` | `ar_collective_anomaly_473.csv` | `stationary + mean_shift + point_anomaly` | ~ PARTIAL |
| `end` | `ar_collective_anomaly_549.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `end` | `ar_collective_anomaly_61.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `end` | `ar_collective_anomaly_798.csv` | `stationary + mean_shift + point_anomaly + variance_shift` | ~ PARTIAL |
| `end` | `ar_collective_anomaly_32.csv` | `stationary + point_anomaly` | ~ PARTIAL |
| `end` | `ar_collective_anomaly_735.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `end` | `ar_collective_anomaly_537.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `end` | `ar_collective_anomaly_694.csv` | `stationary` | ~ PARTIAL |
| `end` | `ar_collective_anomaly_754.csv` | `stationary + collective_anomaly + variance_shift` | ✓ FULL |
| `middle` | `ar_collective_anomaly_550.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `middle` | `ar_collective_anomaly_510.csv` | `stationary + variance_shift` | ~ PARTIAL |
| `middle` | `ar_collective_anomaly_829.csv` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `middle` | `ar_collective_anomaly_113.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ~ PARTIAL |
| `middle` | `ar_collective_anomaly_184.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `middle` | `ar_collective_anomaly_37.csv` | `stationary + collective_anomaly + mean_shift + point_anomaly` | ✓ FULL |
| `middle` | `ar_collective_anomaly_301.csv` | `stationary + collective_anomaly + variance_shift` | ✓ FULL |
| `middle` | `ar_collective_anomaly_471.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `middle` | `ar_collective_anomaly_736.csv` | `stationary + point_anomaly + variance_shift` | ~ PARTIAL |
| `middle` | `ar_collective_anomaly_322.csv` | `stationary + point_anomaly` | ~ PARTIAL |
| `multiple` | `ar_collective_anomaly_380.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `multiple` | `ar_collective_anomaly_71.csv` | `volatility + collective_anomaly + trend_shift` | ~ PARTIAL |
| `multiple` | `ar_collective_anomaly_634.csv` | `stationary + collective_anomaly + variance_shift` | ✓ FULL |
| `multiple` | `ar_collective_anomaly_438.csv` | `volatility + mean_shift + trend_shift` | ✗ NONE |
| `multiple` | `ar_collective_anomaly_534.csv` | `volatility + collective_anomaly + mean_shift` | ~ PARTIAL |
| `multiple` | `ar_collective_anomaly_608.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ~ PARTIAL |
| `multiple` | `ar_collective_anomaly_588.csv` | `volatility + collective_anomaly + trend_shift` | ~ PARTIAL |
| `multiple` | `ar_collective_anomaly_415.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ~ PARTIAL |
| `multiple` | `ar_collective_anomaly_490.csv` | `volatility + collective_anomaly` | ~ PARTIAL |
| `multiple` | `ar_collective_anomaly_786.csv` | `volatility + collective_anomaly` | ~ PARTIAL |
| `beginning` | `ar_collective_anomaly_605.csv` | `volatility + collective_anomaly` | ~ PARTIAL |
| `beginning` | `ar_collective_anomaly_402.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `beginning` | `ar_collective_anomaly_422.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `beginning` | `ar_collective_anomaly_746.csv` | `volatility` | ✗ NONE |
| `beginning` | `ar_collective_anomaly_516.csv` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `beginning` | `ar_collective_anomaly_348.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `beginning` | `ar_collective_anomaly_380.csv` | `stochastic_trend + collective_anomaly + mean_shift + point_anomaly` | ~ PARTIAL |
| `beginning` | `ar_collective_anomaly_33.csv` | `volatility + point_anomaly` | ✗ NONE |
| `beginning` | `ar_collective_anomaly_310.csv` | `stationary + collective_anomaly + variance_shift` | ✓ FULL |
| `beginning` | `ar_collective_anomaly_209.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `end` | `ar_collective_anomaly_763.csv` | `stochastic_trend + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `end` | `ar_collective_anomaly_276.csv` | `stationary + collective_anomaly + mean_shift + point_anomaly + trend_shift` | ✓ FULL |
| `end` | `ar_collective_anomaly_39.csv` | `volatility + collective_anomaly` | ~ PARTIAL |
| `end` | `ar_collective_anomaly_208.csv` | `stochastic_trend + collective_anomaly` | ~ PARTIAL |
| `end` | `ar_collective_anomaly_783.csv` | `volatility + point_anomaly` | ✗ NONE |
| `end` | `ar_collective_anomaly_592.csv` | `stationary + mean_shift + trend_shift + variance_shift` | ~ PARTIAL |
| `end` | `ar_collective_anomaly_975.csv` | `volatility + collective_anomaly` | ~ PARTIAL |
| `end` | `ar_collective_anomaly_800.csv` | `stochastic_trend + collective_anomaly + mean_shift + point_anomaly + trend_shift` | ~ PARTIAL |
| `end` | `ar_collective_anomaly_734.csv` | `volatility + collective_anomaly` | ~ PARTIAL |
| `end` | `ar_collective_anomaly_269.csv` | `volatility + collective_anomaly + trend_shift` | ~ PARTIAL |
| `middle` | `ar_collective_anomaly_275.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `middle` | `ar_collective_anomaly_298.csv` | `volatility + collective_anomaly + point_anomaly + trend_shift` | ~ PARTIAL |
| `middle` | `ar_collective_anomaly_78.csv` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `middle` | `ar_collective_anomaly_544.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `middle` | `ar_collective_anomaly_353.csv` | `stationary + collective_anomaly + mean_shift + trend_shift` | ✓ FULL |
| `middle` | `ar_collective_anomaly_766.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `middle` | `ar_collective_anomaly_641.csv` | `stochastic_trend + collective_anomaly + mean_shift + point_anomaly` | ~ PARTIAL |
| `middle` | `ar_collective_anomaly_8.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `middle` | `ar_collective_anomaly_582.csv` | `stationary + collective_anomaly + variance_shift` | ✓ FULL |
| `middle` | `ar_collective_anomaly_649.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `multiple` | `arma_collective_anomaly_359.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `multiple` | `arma_collective_anomaly_190.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `multiple` | `arma_collective_anomaly_866.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `multiple` | `arma_collective_anomaly_277.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `multiple` | `arma_collective_anomaly_371.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `multiple` | `arma_collective_anomaly_307.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `multiple` | `arma_collective_anomaly_430.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `multiple` | `arma_collective_anomaly_263.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `multiple` | `arma_collective_anomaly_377.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `multiple` | `arma_collective_anomaly_110.csv` | `stationary` | ~ PARTIAL |
| `beginning` | `arma_collective_anomaly_751.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `beginning` | `arma_collective_anomaly_590.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `beginning` | `arma_collective_anomaly_214.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `beginning` | `arma_collective_anomaly_350.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `beginning` | `arma_collective_anomaly_14.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `beginning` | `arma_collective_anomaly_997.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `beginning` | `arma_collective_anomaly_148.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `beginning` | `arma_collective_anomaly_608.csv` | `stationary` | ~ PARTIAL |
| `beginning` | `arma_collective_anomaly_368.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `beginning` | `arma_collective_anomaly_741.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `end` | `arma_collective_anomaly_969.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `end` | `arma_collective_anomaly_214.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `end` | `arma_collective_anomaly_687.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `end` | `arma_collective_anomaly_9.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `end` | `arma_collective_anomaly_792.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `end` | `arma_collective_anomaly_550.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `end` | `arma_collective_anomaly_193.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `end` | `arma_collective_anomaly_902.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `end` | `arma_collective_anomaly_109.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `end` | `arma_collective_anomaly_627.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `middle` | `arma_collective_anomaly_360.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `arma_collective_anomaly_530.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `arma_collective_anomaly_54.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `arma_collective_anomaly_504.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `arma_collective_anomaly_411.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `arma_collective_anomaly_268.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `arma_collective_anomaly_989.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `arma_collective_anomaly_145.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `arma_collective_anomaly_330.csv` | `stationary` | ~ PARTIAL |
| `middle` | `arma_collective_anomaly_966.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `multiple` | `arma_collective_anomaly_893.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `multiple` | `arma_collective_anomaly_539.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `multiple` | `arma_collective_anomaly_202.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `multiple` | `arma_collective_anomaly_856.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `multiple` | `arma_collective_anomaly_158.csv` | `stochastic_trend + collective_anomaly + mean_shift + variance_shift` | ~ PARTIAL |
| `multiple` | `arma_collective_anomaly_468.csv` | `stationary + collective_anomaly + mean_shift + point_anomaly` | ✓ FULL |
| `multiple` | `arma_collective_anomaly_551.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `multiple` | `arma_collective_anomaly_166.csv` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `arma_collective_anomaly_63.csv` | `stationary + collective_anomaly + mean_shift + point_anomaly` | ✓ FULL |
| `multiple` | `arma_collective_anomaly_679.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `beginning` | `arma_collective_anomaly_730.csv` | `stationary + collective_anomaly + mean_shift + variance_shift` | ✓ FULL |
| `beginning` | `arma_collective_anomaly_147.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `beginning` | `arma_collective_anomaly_238.csv` | `stationary + mean_shift + point_anomaly` | ~ PARTIAL |
| `beginning` | `arma_collective_anomaly_235.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `beginning` | `arma_collective_anomaly_846.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `beginning` | `arma_collective_anomaly_617.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `beginning` | `arma_collective_anomaly_973.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `beginning` | `arma_collective_anomaly_379.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `beginning` | `arma_collective_anomaly_177.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `beginning` | `arma_collective_anomaly_327.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ~ PARTIAL |
| `end` | `arma_collective_anomaly_207.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `end` | `arma_collective_anomaly_612.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `end` | `arma_collective_anomaly_802.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `end` | `arma_collective_anomaly_482.csv` | `stationary + collective_anomaly + mean_shift + point_anomaly` | ✓ FULL |
| `end` | `arma_collective_anomaly_657.csv` | `stochastic_trend + collective_anomaly + mean_shift + variance_shift` | ~ PARTIAL |
| `end` | `arma_collective_anomaly_648.csv` | `stationary + collective_anomaly + mean_shift + variance_shift` | ✓ FULL |
| `end` | `arma_collective_anomaly_827.csv` | `stationary + collective_anomaly + variance_shift` | ✓ FULL |
| `end` | `arma_collective_anomaly_669.csv` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `end` | `arma_collective_anomaly_306.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `end` | `arma_collective_anomaly_813.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `middle` | `arma_collective_anomaly_580.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `arma_collective_anomaly_449.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `arma_collective_anomaly_513.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `middle` | `arma_collective_anomaly_936.csv` | `volatility + point_anomaly` | ✗ NONE |
| `middle` | `arma_collective_anomaly_506.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `middle` | `arma_collective_anomaly_372.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `arma_collective_anomaly_891.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `middle` | `arma_collective_anomaly_640.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `arma_collective_anomaly_494.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `middle` | `arma_collective_anomaly_38.csv` | `stochastic_trend + collective_anomaly + variance_shift` | ~ PARTIAL |
| `multiple` | `arma_collective_anomaly_622.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `multiple` | `arma_collective_anomaly_670.csv` | `volatility + collective_anomaly` | ~ PARTIAL |
| `multiple` | `arma_collective_anomaly_153.csv` | `stationary + collective_anomaly + trend_shift` | ✓ FULL |
| `multiple` | `arma_collective_anomaly_660.csv` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `arma_collective_anomaly_984.csv` | `volatility + collective_anomaly + mean_shift` | ~ PARTIAL |
| `multiple` | `arma_collective_anomaly_780.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly + trend_shift` | ~ PARTIAL |
| `multiple` | `arma_collective_anomaly_19.csv` | `stochastic_trend + collective_anomaly` | ~ PARTIAL |
| `multiple` | `arma_collective_anomaly_972.csv` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `arma_collective_anomaly_801.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `multiple` | `arma_collective_anomaly_29.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `beginning` | `arma_collective_anomaly_675.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ~ PARTIAL |
| `beginning` | `arma_collective_anomaly_293.csv` | `volatility + collective_anomaly + mean_shift` | ~ PARTIAL |
| `beginning` | `arma_collective_anomaly_341.csv` | `stationary + collective_anomaly + mean_shift + point_anomaly` | ✓ FULL |
| `beginning` | `arma_collective_anomaly_707.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `beginning` | `arma_collective_anomaly_173.csv` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `beginning` | `arma_collective_anomaly_242.csv` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `beginning` | `arma_collective_anomaly_319.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `beginning` | `arma_collective_anomaly_258.csv` | `volatility + collective_anomaly` | ~ PARTIAL |
| `beginning` | `arma_collective_anomaly_607.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `beginning` | `arma_collective_anomaly_167.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly + trend_shift` | ~ PARTIAL |
| `end` | `arma_collective_anomaly_242.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `end` | `arma_collective_anomaly_100.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly + trend_shift` | ~ PARTIAL |
| `end` | `arma_collective_anomaly_475.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `end` | `arma_collective_anomaly_513.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `end` | `arma_collective_anomaly_733.csv` | `volatility + collective_anomaly + trend_shift` | ~ PARTIAL |
| `end` | `arma_collective_anomaly_646.csv` | `volatility + collective_anomaly + mean_shift` | ~ PARTIAL |
| `end` | `arma_collective_anomaly_531.csv` | `stationary + variance_shift` | ~ PARTIAL |
| `end` | `arma_collective_anomaly_367.csv` | `volatility + collective_anomaly + trend_shift` | ~ PARTIAL |
| `end` | `arma_collective_anomaly_128.csv` | `stationary` | ~ PARTIAL |
| `end` | `arma_collective_anomaly_311.csv` | `stationary + variance_shift` | ~ PARTIAL |
| `middle` | `arma_collective_anomaly_364.csv` | `stationary + variance_shift` | ~ PARTIAL |
| `middle` | `arma_collective_anomaly_75.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `middle` | `arma_collective_anomaly_359.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly + variance_shift` | ~ PARTIAL |
| `middle` | `arma_collective_anomaly_746.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ~ PARTIAL |
| `middle` | `arma_collective_anomaly_891.csv` | `stationary + collective_anomaly + trend_shift` | ✓ FULL |
| `middle` | `arma_collective_anomaly_516.csv` | `stochastic_trend + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `middle` | `arma_collective_anomaly_163.csv` | `stationary + collective_anomaly + mean_shift + point_anomaly` | ✓ FULL |
| `middle` | `arma_collective_anomaly_731.csv` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
| `middle` | `arma_collective_anomaly_313.csv` | `volatility + collective_anomaly` | ~ PARTIAL |
| `middle` | `arma_collective_anomaly_950.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `multiple` | `ma_collective_anomaly_341.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `multiple` | `ma_collective_anomaly_824.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `multiple` | `ma_collective_anomaly_828.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `multiple` | `ma_collective_anomaly_675.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `multiple` | `ma_collective_anomaly_641.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `multiple` | `ma_collective_anomaly_708.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `multiple` | `ma_collective_anomaly_84.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `multiple` | `ma_collective_anomaly_96.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `multiple` | `ma_collective_anomaly_280.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `multiple` | `ma_collective_anomaly_490.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `beginning` | `ma_collective_anomaly_203.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `beginning` | `ma_collective_anomaly_60.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `beginning` | `ma_collective_anomaly_305.csv` | `stationary + point_anomaly` | ~ PARTIAL |
| `beginning` | `ma_collective_anomaly_696.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `beginning` | `ma_collective_anomaly_235.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `beginning` | `ma_collective_anomaly_936.csv` | `stationary` | ~ PARTIAL |
| `beginning` | `ma_collective_anomaly_343.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `beginning` | `ma_collective_anomaly_860.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `beginning` | `ma_collective_anomaly_229.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `beginning` | `ma_collective_anomaly_164.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `end` | `ma_collective_anomaly_153.csv` | `stationary` | ~ PARTIAL |
| `end` | `ma_collective_anomaly_250.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `end` | `ma_collective_anomaly_829.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `end` | `ma_collective_anomaly_381.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `end` | `ma_collective_anomaly_647.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `end` | `ma_collective_anomaly_789.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `end` | `ma_collective_anomaly_859.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `end` | `ma_collective_anomaly_622.csv` | `stationary` | ~ PARTIAL |
| `end` | `ma_collective_anomaly_948.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `end` | `ma_collective_anomaly_364.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `ma_collective_anomaly_502.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `ma_collective_anomaly_212.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `ma_collective_anomaly_53.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `ma_collective_anomaly_733.csv` | `stationary` | ~ PARTIAL |
| `middle` | `ma_collective_anomaly_379.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `ma_collective_anomaly_743.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `ma_collective_anomaly_47.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `ma_collective_anomaly_968.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `ma_collective_anomaly_349.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `ma_collective_anomaly_56.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `multiple` | `ma_collective_anomaly_596.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `multiple` | `ma_collective_anomaly_553.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `multiple` | `ma_collective_anomaly_501.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `multiple` | `ma_collective_anomaly_172.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `multiple` | `ma_collective_anomaly_65.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `multiple` | `ma_collective_anomaly_134.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `multiple` | `ma_collective_anomaly_918.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `multiple` | `ma_collective_anomaly_497.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `multiple` | `ma_collective_anomaly_776.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `multiple` | `ma_collective_anomaly_396.csv` | `deterministic_trend + mean_shift` | ✗ NONE |
| `beginning` | `ma_collective_anomaly_655.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `beginning` | `ma_collective_anomaly_329.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `beginning` | `ma_collective_anomaly_121.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `beginning` | `ma_collective_anomaly_182.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `beginning` | `ma_collective_anomaly_309.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `beginning` | `ma_collective_anomaly_985.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `beginning` | `ma_collective_anomaly_72.csv` | `stationary + collective_anomaly + mean_shift + point_anomaly` | ✓ FULL |
| `beginning` | `ma_collective_anomaly_87.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `beginning` | `ma_collective_anomaly_892.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `beginning` | `ma_collective_anomaly_629.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `end` | `ma_collective_anomaly_64.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `end` | `ma_collective_anomaly_975.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `end` | `ma_collective_anomaly_117.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `end` | `ma_collective_anomaly_803.csv` | `stationary + variance_shift` | ~ PARTIAL |
| `end` | `ma_collective_anomaly_718.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `end` | `ma_collective_anomaly_856.csv` | `stationary + collective_anomaly + mean_shift + variance_shift` | ✓ FULL |
| `end` | `ma_collective_anomaly_346.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `end` | `ma_collective_anomaly_63.csv` | `stationary` | ~ PARTIAL |
| `end` | `ma_collective_anomaly_135.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `end` | `ma_collective_anomaly_801.csv` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `middle` | `ma_collective_anomaly_796.csv` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `middle` | `ma_collective_anomaly_26.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `middle` | `ma_collective_anomaly_531.csv` | `stationary + collective_anomaly + mean_shift + point_anomaly` | ✓ FULL |
| `middle` | `ma_collective_anomaly_577.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `ma_collective_anomaly_7.csv` | `stationary + point_anomaly` | ~ PARTIAL |
| `middle` | `ma_collective_anomaly_505.csv` | `stationary` | ~ PARTIAL |
| `middle` | `ma_collective_anomaly_943.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `middle` | `ma_collective_anomaly_354.csv` | `stationary + collective_anomaly + variance_shift` | ✓ FULL |
| `middle` | `ma_collective_anomaly_265.csv` | `stationary + point_anomaly` | ~ PARTIAL |
| `middle` | `ma_collective_anomaly_638.csv` | `stationary` | ~ PARTIAL |
| `multiple` | `ma_collective_anomaly_50.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `multiple` | `ma_collective_anomaly_684.csv` | `volatility + collective_anomaly` | ~ PARTIAL |
| `multiple` | `ma_collective_anomaly_849.csv` | `volatility + collective_anomaly + point_anomaly + trend_shift` | ~ PARTIAL |
| `multiple` | `ma_collective_anomaly_551.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `multiple` | `ma_collective_anomaly_992.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `multiple` | `ma_collective_anomaly_182.csv` | `volatility` | ✗ NONE |
| `multiple` | `ma_collective_anomaly_531.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `multiple` | `ma_collective_anomaly_419.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `multiple` | `ma_collective_anomaly_475.csv` | `stationary + collective_anomaly + variance_shift` | ✓ FULL |
| `multiple` | `ma_collective_anomaly_405.csv` | `volatility + collective_anomaly` | ~ PARTIAL |
| `beginning` | `ma_collective_anomaly_394.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `beginning` | `ma_collective_anomaly_716.csv` | `volatility + collective_anomaly + mean_shift` | ~ PARTIAL |
| `beginning` | `ma_collective_anomaly_195.csv` | `volatility + collective_anomaly + point_anomaly + trend_shift` | ~ PARTIAL |
| `beginning` | `ma_collective_anomaly_89.csv` | `volatility + collective_anomaly` | ~ PARTIAL |
| `beginning` | `ma_collective_anomaly_246.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ~ PARTIAL |
| `beginning` | `ma_collective_anomaly_401.csv` | `stationary` | ~ PARTIAL |
| `beginning` | `ma_collective_anomaly_478.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `beginning` | `ma_collective_anomaly_738.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `beginning` | `ma_collective_anomaly_555.csv` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `beginning` | `ma_collective_anomaly_364.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `end` | `ma_collective_anomaly_709.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `end` | `ma_collective_anomaly_97.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `end` | `ma_collective_anomaly_468.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `end` | `ma_collective_anomaly_849.csv` | `volatility + collective_anomaly + mean_shift` | ~ PARTIAL |
| `end` | `ma_collective_anomaly_8.csv` | `volatility + collective_anomaly + trend_shift + variance_shift` | ~ PARTIAL |
| `end` | `ma_collective_anomaly_605.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `end` | `ma_collective_anomaly_131.csv` | `stationary + collective_anomaly + mean_shift + variance_shift` | ✓ FULL |
| `end` | `ma_collective_anomaly_517.csv` | `volatility + collective_anomaly` | ~ PARTIAL |
| `end` | `ma_collective_anomaly_18.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `end` | `ma_collective_anomaly_389.csv` | `stationary + collective_anomaly + mean_shift + point_anomaly` | ✓ FULL |
| `middle` | `ma_collective_anomaly_330.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `middle` | `ma_collective_anomaly_397.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly + trend_shift` | ~ PARTIAL |
| `middle` | `ma_collective_anomaly_204.csv` | `volatility + collective_anomaly + mean_shift` | ~ PARTIAL |
| `middle` | `ma_collective_anomaly_993.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `middle` | `ma_collective_anomaly_810.csv` | `stationary + collective_anomaly + mean_shift + trend_shift` | ✓ FULL |
| `middle` | `ma_collective_anomaly_470.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `middle` | `ma_collective_anomaly_896.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `middle` | `ma_collective_anomaly_572.csv` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `middle` | `ma_collective_anomaly_859.csv` | `volatility + collective_anomaly` | ~ PARTIAL |
| `middle` | `ma_collective_anomaly_10.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ~ PARTIAL |
| `multiple` | `white_noise_collective_anomaly_704.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `multiple` | `white_noise_collective_anomaly_90.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `multiple` | `white_noise_collective_anomaly_599.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `multiple` | `white_noise_collective_anomaly_524.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `multiple` | `white_noise_collective_anomaly_48.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `multiple` | `white_noise_collective_anomaly_148.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `multiple` | `white_noise_collective_anomaly_271.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `multiple` | `white_noise_collective_anomaly_576.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `multiple` | `white_noise_collective_anomaly_431.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `multiple` | `white_noise_collective_anomaly_672.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `beginning` | `white_noise_collective_anomaly_796.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `beginning` | `white_noise_collective_anomaly_558.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `beginning` | `white_noise_collective_anomaly_675.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `beginning` | `white_noise_collective_anomaly_505.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `beginning` | `white_noise_collective_anomaly_8.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `beginning` | `white_noise_collective_anomaly_145.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `beginning` | `white_noise_collective_anomaly_286.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `beginning` | `white_noise_collective_anomaly_344.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `beginning` | `white_noise_collective_anomaly_604.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `beginning` | `white_noise_collective_anomaly_219.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `end` | `white_noise_collective_anomaly_953.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `end` | `white_noise_collective_anomaly_363.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `end` | `white_noise_collective_anomaly_501.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `end` | `white_noise_collective_anomaly_91.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `end` | `white_noise_collective_anomaly_742.csv` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `end` | `white_noise_collective_anomaly_545.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `end` | `white_noise_collective_anomaly_21.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `end` | `white_noise_collective_anomaly_124.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `end` | `white_noise_collective_anomaly_996.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `end` | `white_noise_collective_anomaly_68.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `white_noise_collective_anomaly_66.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `white_noise_collective_anomaly_835.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `white_noise_collective_anomaly_319.csv` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `middle` | `white_noise_collective_anomaly_752.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `white_noise_collective_anomaly_244.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `white_noise_collective_anomaly_385.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `white_noise_collective_anomaly_606.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `white_noise_collective_anomaly_110.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `white_noise_collective_anomaly_607.csv` | `stationary` | ~ PARTIAL |
| `middle` | `white_noise_collective_anomaly_474.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `multiple` | `white_noise_collective_anomaly_184.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `multiple` | `white_noise_collective_anomaly_305.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `multiple` | `white_noise_collective_anomaly_874.csv` | `stationary` | ~ PARTIAL |
| `multiple` | `white_noise_collective_anomaly_94.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `multiple` | `white_noise_collective_anomaly_202.csv` | `stationary + point_anomaly` | ~ PARTIAL |
| `multiple` | `white_noise_collective_anomaly_523.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `multiple` | `white_noise_collective_anomaly_971.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `multiple` | `white_noise_collective_anomaly_206.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `multiple` | `white_noise_collective_anomaly_696.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `multiple` | `white_noise_collective_anomaly_866.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `beginning` | `white_noise_collective_anomaly_24.csv` | `stationary + mean_shift + point_anomaly` | ~ PARTIAL |
| `beginning` | `white_noise_collective_anomaly_558.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `beginning` | `white_noise_collective_anomaly_959.csv` | `stationary + point_anomaly` | ~ PARTIAL |
| `beginning` | `white_noise_collective_anomaly_759.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `beginning` | `white_noise_collective_anomaly_367.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `beginning` | `white_noise_collective_anomaly_568.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `beginning` | `white_noise_collective_anomaly_749.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `beginning` | `white_noise_collective_anomaly_35.csv` | `stationary + mean_shift + point_anomaly` | ~ PARTIAL |
| `beginning` | `white_noise_collective_anomaly_481.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `beginning` | `white_noise_collective_anomaly_868.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `end` | `white_noise_collective_anomaly_543.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `end` | `white_noise_collective_anomaly_533.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `end` | `white_noise_collective_anomaly_322.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `end` | `white_noise_collective_anomaly_519.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `end` | `white_noise_collective_anomaly_606.csv` | `stationary` | ~ PARTIAL |
| `end` | `white_noise_collective_anomaly_231.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `end` | `white_noise_collective_anomaly_451.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `end` | `white_noise_collective_anomaly_274.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `end` | `white_noise_collective_anomaly_948.csv` | `stationary` | ~ PARTIAL |
| `end` | `white_noise_collective_anomaly_650.csv` | `stationary + mean_shift + point_anomaly` | ~ PARTIAL |
| `middle` | `white_noise_collective_anomaly_567.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `middle` | `white_noise_collective_anomaly_787.csv` | `stationary + collective_anomaly` | ✓ FULL |
| `middle` | `white_noise_collective_anomaly_909.csv` | `volatility` | ✗ NONE |
| `middle` | `white_noise_collective_anomaly_223.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `middle` | `white_noise_collective_anomaly_895.csv` | `stationary` | ~ PARTIAL |
| `middle` | `white_noise_collective_anomaly_162.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `middle` | `white_noise_collective_anomaly_352.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `middle` | `white_noise_collective_anomaly_810.csv` | `stationary + collective_anomaly + variance_shift` | ✓ FULL |
| `middle` | `white_noise_collective_anomaly_826.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `middle` | `white_noise_collective_anomaly_886.csv` | `stationary + collective_anomaly + mean_shift + point_anomaly + variance_shift` | ✓ FULL |
| `multiple` | `white_noise_collective_anomaly_480.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly + trend_shift` | ~ PARTIAL |
| `multiple` | `white_noise_collective_anomaly_411.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `multiple` | `white_noise_collective_anomaly_96.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `multiple` | `white_noise_collective_anomaly_824.csv` | `volatility + collective_anomaly + mean_shift` | ~ PARTIAL |
| `multiple` | `white_noise_collective_anomaly_566.csv` | `volatility + collective_anomaly + trend_shift` | ~ PARTIAL |
| `multiple` | `white_noise_collective_anomaly_344.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `multiple` | `white_noise_collective_anomaly_855.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `multiple` | `white_noise_collective_anomaly_100.csv` | `volatility + point_anomaly` | ✗ NONE |
| `multiple` | `white_noise_collective_anomaly_359.csv` | `volatility + collective_anomaly + mean_shift` | ~ PARTIAL |
| `multiple` | `white_noise_collective_anomaly_768.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `beginning` | `white_noise_collective_anomaly_373.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ~ PARTIAL |
| `beginning` | `white_noise_collective_anomaly_870.csv` | `volatility + collective_anomaly` | ~ PARTIAL |
| `beginning` | `white_noise_collective_anomaly_64.csv` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
| `beginning` | `white_noise_collective_anomaly_632.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `beginning` | `white_noise_collective_anomaly_706.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `beginning` | `white_noise_collective_anomaly_55.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `beginning` | `white_noise_collective_anomaly_897.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `beginning` | `white_noise_collective_anomaly_235.csv` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
| `beginning` | `white_noise_collective_anomaly_51.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `beginning` | `white_noise_collective_anomaly_595.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ~ PARTIAL |
| `end` | `white_noise_collective_anomaly_544.csv` | `stationary + collective_anomaly + mean_shift + trend_shift` | ✓ FULL |
| `end` | `white_noise_collective_anomaly_416.csv` | `volatility + mean_shift + point_anomaly` | ✗ NONE |
| `end` | `white_noise_collective_anomaly_404.csv` | `volatility + collective_anomaly + mean_shift` | ~ PARTIAL |
| `end` | `white_noise_collective_anomaly_607.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `end` | `white_noise_collective_anomaly_801.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `end` | `white_noise_collective_anomaly_6.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `end` | `white_noise_collective_anomaly_446.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ~ PARTIAL |
| `end` | `white_noise_collective_anomaly_518.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `end` | `white_noise_collective_anomaly_959.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `end` | `white_noise_collective_anomaly_395.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `middle` | `white_noise_collective_anomaly_90.csv` | `volatility + collective_anomaly + trend_shift` | ~ PARTIAL |
| `middle` | `white_noise_collective_anomaly_272.csv` | `stationary + collective_anomaly + point_anomaly + trend_shift` | ✓ FULL |
| `middle` | `white_noise_collective_anomaly_741.csv` | `volatility + collective_anomaly` | ~ PARTIAL |
| `middle` | `white_noise_collective_anomaly_318.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ~ PARTIAL |
| `middle` | `white_noise_collective_anomaly_625.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `middle` | `white_noise_collective_anomaly_451.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `middle` | `white_noise_collective_anomaly_313.csv` | `volatility + point_anomaly + trend_shift` | ✗ NONE |
| `middle` | `white_noise_collective_anomaly_888.csv` | `volatility + collective_anomaly + point_anomaly + trend_shift` | ~ PARTIAL |
| `middle` | `white_noise_collective_anomaly_813.csv` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
| `middle` | `white_noise_collective_anomaly_477.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
---

## Grup 6: contextual_anomaly
**Beklenen:** `stationary + contextual_anomaly`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `multiple` | `ar_contextual_anomaly_multiple_138.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `ar_contextual_anomaly_multiple_391.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `ar_contextual_anomaly_multiple_785.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `ar_contextual_anomaly_multiple_534.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `ar_contextual_anomaly_multiple_749.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `ar_contextual_anomaly_multiple_940.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `ar_contextual_anomaly_multiple_846.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `ar_contextual_anomaly_multiple_45.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `ar_contextual_anomaly_multiple_454.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `ar_contextual_anomaly_multiple_71.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_long_beginning` | `ar_contextual_anomaly_beginning_829.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_long_beginning` | `ar_contextual_anomaly_beginning_855.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_long_beginning` | `ar_contextual_anomaly_beginning_7.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_long_beginning` | `ar_contextual_anomaly_beginning_238.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_long_beginning` | `ar_contextual_anomaly_beginning_555.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_long_beginning` | `ar_contextual_anomaly_beginning_988.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_long_beginning` | `ar_contextual_anomaly_beginning_131.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_long_beginning` | `ar_contextual_anomaly_beginning_214.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_long_beginning` | `ar_contextual_anomaly_beginning_561.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_long_beginning` | `ar_contextual_anomaly_beginning_989.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_long_end` | `ar_contextual_anomaly_end_642.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_long_end` | `ar_contextual_anomaly_end_403.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_long_end` | `ar_contextual_anomaly_end_90.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_long_end` | `ar_contextual_anomaly_end_190.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_long_end` | `ar_contextual_anomaly_end_904.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_long_end` | `ar_contextual_anomaly_end_878.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_long_end` | `ar_contextual_anomaly_end_503.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_long_end` | `ar_contextual_anomaly_end_583.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_long_end` | `ar_contextual_anomaly_end_938.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_long_end` | `ar_contextual_anomaly_end_519.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_long_middle` | `ar_contextual_anomaly_middle_111.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_long_middle` | `ar_contextual_anomaly_middle_764.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_long_middle` | `ar_contextual_anomaly_middle_230.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_long_middle` | `ar_contextual_anomaly_middle_476.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_long_middle` | `ar_contextual_anomaly_middle_900.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_long_middle` | `ar_contextual_anomaly_middle_701.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_long_middle` | `ar_contextual_anomaly_middle_993.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_long_middle` | `ar_contextual_anomaly_middle_240.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_long_middle` | `ar_contextual_anomaly_middle_167.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_long_middle` | `ar_contextual_anomaly_middle_530.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `ar_contextual_anomaly_multiple_819.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `multiple` | `ar_contextual_anomaly_multiple_992.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `ar_contextual_anomaly_multiple_342.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `multiple` | `ar_contextual_anomaly_multiple_41.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `ar_contextual_anomaly_multiple_673.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `ar_contextual_anomaly_multiple_737.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `multiple` | `ar_contextual_anomaly_multiple_465.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `ar_contextual_anomaly_multiple_698.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `ar_contextual_anomaly_multiple_172.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `multiple` | `ar_contextual_anomaly_multiple_884.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_medium_beginning` | `ar_contextual_anomaly_beginning_400.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `AR_medium_beginning` | `ar_contextual_anomaly_beginning_884.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_medium_beginning` | `ar_contextual_anomaly_beginning_72.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_medium_beginning` | `ar_contextual_anomaly_beginning_890.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_medium_beginning` | `ar_contextual_anomaly_beginning_590.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_medium_beginning` | `ar_contextual_anomaly_beginning_449.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_medium_beginning` | `ar_contextual_anomaly_beginning_979.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_medium_beginning` | `ar_contextual_anomaly_beginning_390.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_medium_beginning` | `ar_contextual_anomaly_beginning_676.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_medium_beginning` | `ar_contextual_anomaly_beginning_760.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_medium_end` | `ar_contextual_anomaly_end_916.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_medium_end` | `ar_contextual_anomaly_end_799.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_medium_end` | `ar_contextual_anomaly_end_548.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_medium_end` | `ar_contextual_anomaly_end_902.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_medium_end` | `ar_contextual_anomaly_end_598.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_medium_end` | `ar_contextual_anomaly_end_130.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_medium_end` | `ar_contextual_anomaly_end_668.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_medium_end` | `ar_contextual_anomaly_end_161.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `AR_medium_end` | `ar_contextual_anomaly_end_314.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `AR_medium_end` | `ar_contextual_anomaly_end_680.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_medium_middle` | `ar_contextual_anomaly_middle_729.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `AR_medium_middle` | `ar_contextual_anomaly_middle_948.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `AR_medium_middle` | `ar_contextual_anomaly_middle_363.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_medium_middle` | `ar_contextual_anomaly_middle_307.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_medium_middle` | `ar_contextual_anomaly_middle_787.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `AR_medium_middle` | `ar_contextual_anomaly_middle_181.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_medium_middle` | `ar_contextual_anomaly_middle_499.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_medium_middle` | `ar_contextual_anomaly_middle_189.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_medium_middle` | `ar_contextual_anomaly_middle_8.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `AR_medium_middle` | `ar_contextual_anomaly_middle_682.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `ar_contextual_anomaly_multiple_747.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `ar_contextual_anomaly_multiple_902.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `multiple` | `ar_contextual_anomaly_multiple_190.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `ar_contextual_anomaly_multiple_507.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `ar_contextual_anomaly_multiple_251.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `ar_contextual_anomaly_multiple_738.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `ar_contextual_anomaly_multiple_374.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `ar_contextual_anomaly_multiple_931.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `ar_contextual_anomaly_multiple_124.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `ar_contextual_anomaly_multiple_140.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `AR_short_beginning` | `ar_contextual_anomaly_beginning_398.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `AR_short_beginning` | `ar_contextual_anomaly_beginning_832.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `AR_short_beginning` | `ar_contextual_anomaly_beginning_15.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `AR_short_beginning` | `ar_contextual_anomaly_beginning_369.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `AR_short_beginning` | `ar_contextual_anomaly_beginning_429.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `AR_short_beginning` | `ar_contextual_anomaly_beginning_443.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `AR_short_beginning` | `ar_contextual_anomaly_beginning_496.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `AR_short_beginning` | `ar_contextual_anomaly_beginning_232.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `AR_short_beginning` | `ar_contextual_anomaly_beginning_323.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `AR_short_beginning` | `ar_contextual_anomaly_beginning_588.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `AR_short_end` | `ar_contextual_anomaly_end_478.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `AR_short_end` | `ar_contextual_anomaly_end_62.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `AR_short_end` | `ar_contextual_anomaly_end_727.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `AR_short_end` | `ar_contextual_anomaly_end_829.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `AR_short_end` | `ar_contextual_anomaly_end_264.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `AR_short_end` | `ar_contextual_anomaly_end_255.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `AR_short_end` | `ar_contextual_anomaly_end_26.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `AR_short_end` | `ar_contextual_anomaly_end_170.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `AR_short_end` | `ar_contextual_anomaly_end_660.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `AR_short_end` | `ar_contextual_anomaly_end_900.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `AR_short_middle` | `ar_contextual_anomaly_middle_450.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `AR_short_middle` | `ar_contextual_anomaly_middle_67.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `AR_short_middle` | `ar_contextual_anomaly_middle_728.csv` | `volatility + collective_anomaly + contextual_anomaly + point_anomaly` | ~ PARTIAL |
| `AR_short_middle` | `ar_contextual_anomaly_middle_32.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `AR_short_middle` | `ar_contextual_anomaly_middle_557.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `AR_short_middle` | `ar_contextual_anomaly_middle_94.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `AR_short_middle` | `ar_contextual_anomaly_middle_636.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `AR_short_middle` | `ar_contextual_anomaly_middle_23.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `AR_short_middle` | `ar_contextual_anomaly_middle_311.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `AR_short_middle` | `ar_contextual_anomaly_middle_523.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `multiple` | `arma_contextual_anomaly_multiple_687.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `arma_contextual_anomaly_multiple_332.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `multiple` | `arma_contextual_anomaly_multiple_521.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `arma_contextual_anomaly_multiple_333.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `arma_contextual_anomaly_multiple_712.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `arma_contextual_anomaly_multiple_106.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `arma_contextual_anomaly_multiple_927.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `arma_contextual_anomaly_multiple_84.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `arma_contextual_anomaly_multiple_527.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `arma_contextual_anomaly_multiple_929.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_long_beginning` | `arma_contextual_anomaly_beginning_363.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_long_beginning` | `arma_contextual_anomaly_beginning_722.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_long_beginning` | `arma_contextual_anomaly_beginning_601.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_long_beginning` | `arma_contextual_anomaly_beginning_243.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_long_beginning` | `arma_contextual_anomaly_beginning_166.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_long_beginning` | `arma_contextual_anomaly_beginning_505.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_long_beginning` | `arma_contextual_anomaly_beginning_97.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_long_beginning` | `arma_contextual_anomaly_beginning_416.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_long_beginning` | `arma_contextual_anomaly_beginning_64.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_long_beginning` | `arma_contextual_anomaly_beginning_374.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_long_end` | `arma_contextual_anomaly_end_688.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_long_end` | `arma_contextual_anomaly_end_986.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_long_end` | `arma_contextual_anomaly_end_49.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_long_end` | `arma_contextual_anomaly_end_734.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_long_end` | `arma_contextual_anomaly_end_329.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_long_end` | `arma_contextual_anomaly_end_519.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_long_end` | `arma_contextual_anomaly_end_878.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_long_end` | `arma_contextual_anomaly_end_377.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_long_end` | `arma_contextual_anomaly_end_281.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_long_end` | `arma_contextual_anomaly_end_452.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_long_middle` | `arma_contextual_anomaly_middle_885.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_long_middle` | `arma_contextual_anomaly_middle_543.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_long_middle` | `arma_contextual_anomaly_middle_197.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_long_middle` | `arma_contextual_anomaly_middle_316.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_long_middle` | `arma_contextual_anomaly_middle_45.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_long_middle` | `arma_contextual_anomaly_middle_625.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_long_middle` | `arma_contextual_anomaly_middle_429.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_long_middle` | `arma_contextual_anomaly_middle_628.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_long_middle` | `arma_contextual_anomaly_middle_370.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_long_middle` | `arma_contextual_anomaly_middle_743.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `arma_contextual_anomaly_multiple_370.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `multiple` | `arma_contextual_anomaly_multiple_118.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `arma_contextual_anomaly_multiple_863.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `multiple` | `arma_contextual_anomaly_multiple_705.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `arma_contextual_anomaly_multiple_463.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `multiple` | `arma_contextual_anomaly_multiple_351.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `multiple` | `arma_contextual_anomaly_multiple_105.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `multiple` | `arma_contextual_anomaly_multiple_62.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `arma_contextual_anomaly_multiple_896.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `arma_contextual_anomaly_multiple_730.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `ARMA_medium_beginning` | `arma_contextual_anomaly_beginning_815.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_medium_beginning` | `arma_contextual_anomaly_beginning_785.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_medium_beginning` | `arma_contextual_anomaly_beginning_996.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_medium_beginning` | `arma_contextual_anomaly_beginning_143.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_medium_beginning` | `arma_contextual_anomaly_beginning_938.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `ARMA_medium_beginning` | `arma_contextual_anomaly_beginning_657.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_medium_beginning` | `arma_contextual_anomaly_beginning_786.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_medium_beginning` | `arma_contextual_anomaly_beginning_556.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `ARMA_medium_beginning` | `arma_contextual_anomaly_beginning_866.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_medium_beginning` | `arma_contextual_anomaly_beginning_931.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_medium_end` | `arma_contextual_anomaly_end_930.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `ARMA_medium_end` | `arma_contextual_anomaly_end_362.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_medium_end` | `arma_contextual_anomaly_end_813.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_medium_end` | `arma_contextual_anomaly_end_835.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_medium_end` | `arma_contextual_anomaly_end_31.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_medium_end` | `arma_contextual_anomaly_end_658.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_medium_end` | `arma_contextual_anomaly_end_838.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_medium_end` | `arma_contextual_anomaly_end_422.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_medium_end` | `arma_contextual_anomaly_end_30.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_medium_end` | `arma_contextual_anomaly_end_685.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `ARMA_medium_middle` | `arma_contextual_anomaly_middle_273.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `ARMA_medium_middle` | `arma_contextual_anomaly_middle_670.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_medium_middle` | `arma_contextual_anomaly_middle_329.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `ARMA_medium_middle` | `arma_contextual_anomaly_middle_723.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_medium_middle` | `arma_contextual_anomaly_middle_795.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_medium_middle` | `arma_contextual_anomaly_middle_763.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `ARMA_medium_middle` | `arma_contextual_anomaly_middle_805.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `ARMA_medium_middle` | `arma_contextual_anomaly_middle_706.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_medium_middle` | `arma_contextual_anomaly_middle_726.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_medium_middle` | `arma_contextual_anomaly_middle_871.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `arma_contextual_anomaly_multiple_224.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `multiple` | `arma_contextual_anomaly_multiple_678.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `multiple` | `arma_contextual_anomaly_multiple_188.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `arma_contextual_anomaly_multiple_931.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `multiple` | `arma_contextual_anomaly_multiple_677.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `arma_contextual_anomaly_multiple_694.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `arma_contextual_anomaly_multiple_134.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `arma_contextual_anomaly_multiple_383.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `multiple` | `arma_contextual_anomaly_multiple_825.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `arma_contextual_anomaly_multiple_504.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `ARMA_short_beginning` | `arma_contextual_anomaly_beginning_129.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `ARMA_short_beginning` | `arma_contextual_anomaly_beginning_632.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `ARMA_short_beginning` | `arma_contextual_anomaly_beginning_434.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `ARMA_short_beginning` | `arma_contextual_anomaly_beginning_773.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `ARMA_short_beginning` | `arma_contextual_anomaly_beginning_219.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `ARMA_short_beginning` | `arma_contextual_anomaly_beginning_181.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `ARMA_short_beginning` | `arma_contextual_anomaly_beginning_937.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `ARMA_short_beginning` | `arma_contextual_anomaly_beginning_370.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `ARMA_short_beginning` | `arma_contextual_anomaly_beginning_4.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `ARMA_short_beginning` | `arma_contextual_anomaly_beginning_788.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `ARMA_short_end` | `arma_contextual_anomaly_end_481.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `ARMA_short_end` | `arma_contextual_anomaly_end_26.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `ARMA_short_end` | `arma_contextual_anomaly_end_283.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `ARMA_short_end` | `arma_contextual_anomaly_end_22.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `ARMA_short_end` | `arma_contextual_anomaly_end_823.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `ARMA_short_end` | `arma_contextual_anomaly_end_596.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `ARMA_short_end` | `arma_contextual_anomaly_end_906.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `ARMA_short_end` | `arma_contextual_anomaly_end_994.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `ARMA_short_end` | `arma_contextual_anomaly_end_435.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `ARMA_short_end` | `arma_contextual_anomaly_end_588.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `ARMA_short_middle` | `arma_contextual_anomaly_middle_560.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `ARMA_short_middle` | `arma_contextual_anomaly_middle_940.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `ARMA_short_middle` | `arma_contextual_anomaly_middle_35.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `ARMA_short_middle` | `arma_contextual_anomaly_middle_864.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `ARMA_short_middle` | `arma_contextual_anomaly_middle_25.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `ARMA_short_middle` | `arma_contextual_anomaly_middle_335.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `ARMA_short_middle` | `arma_contextual_anomaly_middle_859.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `ARMA_short_middle` | `arma_contextual_anomaly_middle_969.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `ARMA_short_middle` | `arma_contextual_anomaly_middle_542.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `ARMA_short_middle` | `arma_contextual_anomaly_middle_990.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `ma_contextual_anomaly_multiple_841.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `ma_contextual_anomaly_multiple_370.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `ma_contextual_anomaly_multiple_787.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `ma_contextual_anomaly_multiple_900.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `ma_contextual_anomaly_multiple_41.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `ma_contextual_anomaly_multiple_84.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `ma_contextual_anomaly_multiple_203.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `ma_contextual_anomaly_multiple_53.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `ma_contextual_anomaly_multiple_987.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `ma_contextual_anomaly_multiple_168.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_long_beginning` | `ma_contextual_anomaly_beginning_228.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_long_beginning` | `ma_contextual_anomaly_beginning_794.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_long_beginning` | `ma_contextual_anomaly_beginning_99.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_long_beginning` | `ma_contextual_anomaly_beginning_306.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_long_beginning` | `ma_contextual_anomaly_beginning_891.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_long_beginning` | `ma_contextual_anomaly_beginning_721.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_long_beginning` | `ma_contextual_anomaly_beginning_766.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_long_beginning` | `ma_contextual_anomaly_beginning_72.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_long_beginning` | `ma_contextual_anomaly_beginning_464.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_long_beginning` | `ma_contextual_anomaly_beginning_990.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_long_end` | `ma_contextual_anomaly_end_879.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_long_end` | `ma_contextual_anomaly_end_84.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_long_end` | `ma_contextual_anomaly_end_611.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_long_end` | `ma_contextual_anomaly_end_435.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_long_end` | `ma_contextual_anomaly_end_181.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_long_end` | `ma_contextual_anomaly_end_827.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_long_end` | `ma_contextual_anomaly_end_462.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_long_end` | `ma_contextual_anomaly_end_110.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_long_end` | `ma_contextual_anomaly_end_341.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_long_end` | `ma_contextual_anomaly_end_593.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_long_middle` | `ma_contextual_anomaly_middle_211.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_long_middle` | `ma_contextual_anomaly_middle_517.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_long_middle` | `ma_contextual_anomaly_middle_438.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_long_middle` | `ma_contextual_anomaly_middle_718.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_long_middle` | `ma_contextual_anomaly_middle_789.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_long_middle` | `ma_contextual_anomaly_middle_34.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_long_middle` | `ma_contextual_anomaly_middle_637.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_long_middle` | `ma_contextual_anomaly_middle_45.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_long_middle` | `ma_contextual_anomaly_middle_857.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_long_middle` | `ma_contextual_anomaly_middle_687.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `ma_contextual_anomaly_multiple_965.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `ma_contextual_anomaly_multiple_440.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `multiple` | `ma_contextual_anomaly_multiple_198.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `ma_contextual_anomaly_multiple_720.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `multiple` | `ma_contextual_anomaly_multiple_313.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `multiple` | `ma_contextual_anomaly_multiple_532.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `ma_contextual_anomaly_multiple_120.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `multiple` | `ma_contextual_anomaly_multiple_67.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `multiple` | `ma_contextual_anomaly_multiple_913.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `multiple` | `ma_contextual_anomaly_multiple_968.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_medium_beginning` | `ma_contextual_anomaly_beginning_615.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `MA_medium_beginning` | `ma_contextual_anomaly_beginning_40.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `MA_medium_beginning` | `ma_contextual_anomaly_beginning_942.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `MA_medium_beginning` | `ma_contextual_anomaly_beginning_660.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `MA_medium_beginning` | `ma_contextual_anomaly_beginning_301.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_medium_beginning` | `ma_contextual_anomaly_beginning_696.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_medium_beginning` | `ma_contextual_anomaly_beginning_156.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_medium_beginning` | `ma_contextual_anomaly_beginning_684.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `MA_medium_beginning` | `ma_contextual_anomaly_beginning_858.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_medium_beginning` | `ma_contextual_anomaly_beginning_526.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_medium_end` | `ma_contextual_anomaly_end_937.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_medium_end` | `ma_contextual_anomaly_end_744.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `MA_medium_end` | `ma_contextual_anomaly_end_377.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `MA_medium_end` | `ma_contextual_anomaly_end_697.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_medium_end` | `ma_contextual_anomaly_end_475.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_medium_end` | `ma_contextual_anomaly_end_205.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_medium_end` | `ma_contextual_anomaly_end_227.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_medium_end` | `ma_contextual_anomaly_end_14.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `MA_medium_end` | `ma_contextual_anomaly_end_970.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_medium_end` | `ma_contextual_anomaly_end_132.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `MA_medium_middle` | `ma_contextual_anomaly_middle_379.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_medium_middle` | `ma_contextual_anomaly_middle_552.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `MA_medium_middle` | `ma_contextual_anomaly_middle_204.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_medium_middle` | `ma_contextual_anomaly_middle_188.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_medium_middle` | `ma_contextual_anomaly_middle_314.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_medium_middle` | `ma_contextual_anomaly_middle_916.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `MA_medium_middle` | `ma_contextual_anomaly_middle_594.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `MA_medium_middle` | `ma_contextual_anomaly_middle_222.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `MA_medium_middle` | `ma_contextual_anomaly_middle_456.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `MA_medium_middle` | `ma_contextual_anomaly_middle_516.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `ma_contextual_anomaly_multiple_44.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `multiple` | `ma_contextual_anomaly_multiple_716.csv` | `volatility + collective_anomaly + contextual_anomaly + point_anomaly` | ~ PARTIAL |
| `multiple` | `ma_contextual_anomaly_multiple_974.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `ma_contextual_anomaly_multiple_783.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `ma_contextual_anomaly_multiple_740.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `ma_contextual_anomaly_multiple_970.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `ma_contextual_anomaly_multiple_597.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `ma_contextual_anomaly_multiple_485.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `multiple` | `ma_contextual_anomaly_multiple_64.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `ma_contextual_anomaly_multiple_769.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `MA_short_beginning` | `ma_contextual_anomaly_beginning_240.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `MA_short_beginning` | `ma_contextual_anomaly_beginning_914.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `MA_short_beginning` | `ma_contextual_anomaly_beginning_480.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `MA_short_beginning` | `ma_contextual_anomaly_beginning_701.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `MA_short_beginning` | `ma_contextual_anomaly_beginning_19.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `MA_short_beginning` | `ma_contextual_anomaly_beginning_867.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `MA_short_beginning` | `ma_contextual_anomaly_beginning_55.csv` | `volatility + collective_anomaly + contextual_anomaly + point_anomaly` | ~ PARTIAL |
| `MA_short_beginning` | `ma_contextual_anomaly_beginning_666.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `MA_short_beginning` | `ma_contextual_anomaly_beginning_474.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `MA_short_beginning` | `ma_contextual_anomaly_beginning_964.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `MA_short_end` | `ma_contextual_anomaly_end_976.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `MA_short_end` | `ma_contextual_anomaly_end_356.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `MA_short_end` | `ma_contextual_anomaly_end_128.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `MA_short_end` | `ma_contextual_anomaly_end_734.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `MA_short_end` | `ma_contextual_anomaly_end_44.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `MA_short_end` | `ma_contextual_anomaly_end_299.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `MA_short_end` | `ma_contextual_anomaly_end_507.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `MA_short_end` | `ma_contextual_anomaly_end_508.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `MA_short_end` | `ma_contextual_anomaly_end_975.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `MA_short_end` | `ma_contextual_anomaly_end_315.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `MA_short_middle` | `ma_contextual_anomaly_middle_887.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `MA_short_middle` | `ma_contextual_anomaly_middle_432.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `MA_short_middle` | `ma_contextual_anomaly_middle_19.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `MA_short_middle` | `ma_contextual_anomaly_middle_730.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `MA_short_middle` | `ma_contextual_anomaly_middle_437.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `MA_short_middle` | `ma_contextual_anomaly_middle_60.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `MA_short_middle` | `ma_contextual_anomaly_middle_93.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `MA_short_middle` | `ma_contextual_anomaly_middle_693.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `MA_short_middle` | `ma_contextual_anomaly_middle_429.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `MA_short_middle` | `ma_contextual_anomaly_middle_154.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `multiple` | `white_noise_contextual_anomaly_multiple_465.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `white_noise_contextual_anomaly_multiple_352.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `white_noise_contextual_anomaly_multiple_273.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `white_noise_contextual_anomaly_multiple_991.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `white_noise_contextual_anomaly_multiple_210.csv` | `stationary + contextual_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `white_noise_contextual_anomaly_multiple_973.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `white_noise_contextual_anomaly_multiple_880.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `white_noise_contextual_anomaly_multiple_858.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `white_noise_contextual_anomaly_multiple_517.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `white_noise_contextual_anomaly_multiple_182.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_long_beginning` | `white_noise_contextual_anomaly_beginning_709.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_long_beginning` | `white_noise_contextual_anomaly_beginning_294.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_long_beginning` | `white_noise_contextual_anomaly_beginning_690.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_long_beginning` | `white_noise_contextual_anomaly_beginning_688.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_long_beginning` | `white_noise_contextual_anomaly_beginning_649.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_long_beginning` | `white_noise_contextual_anomaly_beginning_994.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_long_beginning` | `white_noise_contextual_anomaly_beginning_117.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_long_beginning` | `white_noise_contextual_anomaly_beginning_144.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_long_beginning` | `white_noise_contextual_anomaly_beginning_823.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_long_beginning` | `white_noise_contextual_anomaly_beginning_405.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_long_end` | `white_noise_contextual_anomaly_end_322.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_long_end` | `white_noise_contextual_anomaly_end_213.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_long_end` | `white_noise_contextual_anomaly_end_823.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_long_end` | `white_noise_contextual_anomaly_end_619.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_long_end` | `white_noise_contextual_anomaly_end_288.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_long_end` | `white_noise_contextual_anomaly_end_161.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_long_end` | `white_noise_contextual_anomaly_end_863.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_long_end` | `white_noise_contextual_anomaly_end_803.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_long_end` | `white_noise_contextual_anomaly_end_609.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_long_end` | `white_noise_contextual_anomaly_end_29.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_long_middle` | `white_noise_contextual_anomaly_middle_639.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_long_middle` | `white_noise_contextual_anomaly_middle_298.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_long_middle` | `white_noise_contextual_anomaly_middle_848.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_long_middle` | `white_noise_contextual_anomaly_middle_90.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_long_middle` | `white_noise_contextual_anomaly_middle_312.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_long_middle` | `white_noise_contextual_anomaly_middle_400.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_long_middle` | `white_noise_contextual_anomaly_middle_811.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_long_middle` | `white_noise_contextual_anomaly_middle_234.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_long_middle` | `white_noise_contextual_anomaly_middle_825.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_long_middle` | `white_noise_contextual_anomaly_middle_929.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `white_noise_contextual_anomaly_multiple_648.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `white_noise_contextual_anomaly_multiple_100.csv` | `stationary + contextual_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `white_noise_contextual_anomaly_multiple_353.csv` | `stationary + contextual_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `white_noise_contextual_anomaly_multiple_890.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `white_noise_contextual_anomaly_multiple_231.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `white_noise_contextual_anomaly_multiple_218.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `multiple` | `white_noise_contextual_anomaly_multiple_597.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `white_noise_contextual_anomaly_multiple_329.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `white_noise_contextual_anomaly_multiple_834.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `multiple` | `white_noise_contextual_anomaly_multiple_259.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_medium_beginning` | `white_noise_contextual_anomaly_beginning_2.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_medium_beginning` | `white_noise_contextual_anomaly_beginning_707.csv` | `stationary + contextual_anomaly + point_anomaly` | ✓ FULL |
| `White_Noise_medium_beginning` | `white_noise_contextual_anomaly_beginning_898.csv` | `stationary + contextual_anomaly + point_anomaly` | ✓ FULL |
| `White_Noise_medium_beginning` | `white_noise_contextual_anomaly_beginning_121.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_medium_beginning` | `white_noise_contextual_anomaly_beginning_219.csv` | `stationary + contextual_anomaly + point_anomaly` | ✓ FULL |
| `White_Noise_medium_beginning` | `white_noise_contextual_anomaly_beginning_111.csv` | `stationary + contextual_anomaly + point_anomaly` | ✓ FULL |
| `White_Noise_medium_beginning` | `white_noise_contextual_anomaly_beginning_428.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `White_Noise_medium_beginning` | `white_noise_contextual_anomaly_beginning_826.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_medium_beginning` | `white_noise_contextual_anomaly_beginning_825.csv` | `stationary + contextual_anomaly + point_anomaly` | ✓ FULL |
| `White_Noise_medium_beginning` | `white_noise_contextual_anomaly_beginning_317.csv` | `stationary + contextual_anomaly + point_anomaly` | ✓ FULL |
| `White_Noise_medium_end` | `white_noise_contextual_anomaly_end_640.csv` | `stationary + contextual_anomaly + point_anomaly` | ✓ FULL |
| `White_Noise_medium_end` | `white_noise_contextual_anomaly_end_397.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `White_Noise_medium_end` | `white_noise_contextual_anomaly_end_112.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_medium_end` | `white_noise_contextual_anomaly_end_259.csv` | `stationary + contextual_anomaly + point_anomaly` | ✓ FULL |
| `White_Noise_medium_end` | `white_noise_contextual_anomaly_end_342.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_medium_end` | `white_noise_contextual_anomaly_end_146.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_medium_end` | `white_noise_contextual_anomaly_end_214.csv` | `stationary + contextual_anomaly + point_anomaly` | ✓ FULL |
| `White_Noise_medium_end` | `white_noise_contextual_anomaly_end_782.csv` | `stationary + contextual_anomaly + point_anomaly` | ✓ FULL |
| `White_Noise_medium_end` | `white_noise_contextual_anomaly_end_487.csv` | `stationary + contextual_anomaly + point_anomaly` | ✓ FULL |
| `White_Noise_medium_end` | `white_noise_contextual_anomaly_end_583.csv` | `stationary + contextual_anomaly + point_anomaly` | ✓ FULL |
| `White_Noise_medium_middle` | `white_noise_contextual_anomaly_middle_202.csv` | `stationary + contextual_anomaly + point_anomaly` | ✓ FULL |
| `White_Noise_medium_middle` | `white_noise_contextual_anomaly_middle_786.csv` | `stationary + contextual_anomaly + point_anomaly` | ✓ FULL |
| `White_Noise_medium_middle` | `white_noise_contextual_anomaly_middle_157.csv` | `stationary + contextual_anomaly + point_anomaly` | ✓ FULL |
| `White_Noise_medium_middle` | `white_noise_contextual_anomaly_middle_537.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_medium_middle` | `white_noise_contextual_anomaly_middle_511.csv` | `stationary + contextual_anomaly + point_anomaly` | ✓ FULL |
| `White_Noise_medium_middle` | `white_noise_contextual_anomaly_middle_815.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_medium_middle` | `white_noise_contextual_anomaly_middle_431.csv` | `stationary + contextual_anomaly + point_anomaly` | ✓ FULL |
| `White_Noise_medium_middle` | `white_noise_contextual_anomaly_middle_571.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_medium_middle` | `white_noise_contextual_anomaly_middle_645.csv` | `stationary + contextual_anomaly + point_anomaly` | ✓ FULL |
| `White_Noise_medium_middle` | `white_noise_contextual_anomaly_middle_199.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `multiple` | `white_noise_contextual_anomaly_multiple_514.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `white_noise_contextual_anomaly_multiple_562.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `white_noise_contextual_anomaly_multiple_301.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `multiple` | `white_noise_contextual_anomaly_multiple_970.csv` | `volatility + collective_anomaly + contextual_anomaly + point_anomaly` | ~ PARTIAL |
| `multiple` | `white_noise_contextual_anomaly_multiple_665.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `white_noise_contextual_anomaly_multiple_138.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `white_noise_contextual_anomaly_multiple_769.csv` | `stationary + contextual_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `white_noise_contextual_anomaly_multiple_820.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `white_noise_contextual_anomaly_multiple_936.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `white_noise_contextual_anomaly_multiple_898.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `White_Noise_short_beginning` | `white_noise_contextual_anomaly_beginning_705.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `White_Noise_short_beginning` | `white_noise_contextual_anomaly_beginning_579.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `White_Noise_short_beginning` | `white_noise_contextual_anomaly_beginning_376.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `White_Noise_short_beginning` | `white_noise_contextual_anomaly_beginning_520.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `White_Noise_short_beginning` | `white_noise_contextual_anomaly_beginning_691.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `White_Noise_short_beginning` | `white_noise_contextual_anomaly_beginning_988.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `White_Noise_short_beginning` | `white_noise_contextual_anomaly_beginning_126.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `White_Noise_short_beginning` | `white_noise_contextual_anomaly_beginning_154.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `White_Noise_short_beginning` | `white_noise_contextual_anomaly_beginning_54.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `White_Noise_short_beginning` | `white_noise_contextual_anomaly_beginning_88.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `White_Noise_short_end` | `white_noise_contextual_anomaly_end_469.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `White_Noise_short_end` | `white_noise_contextual_anomaly_end_491.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `White_Noise_short_end` | `white_noise_contextual_anomaly_end_730.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `White_Noise_short_end` | `white_noise_contextual_anomaly_end_198.csv` | `stationary + contextual_anomaly + point_anomaly` | ✓ FULL |
| `White_Noise_short_end` | `white_noise_contextual_anomaly_end_550.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `White_Noise_short_end` | `white_noise_contextual_anomaly_end_755.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `White_Noise_short_end` | `white_noise_contextual_anomaly_end_937.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `White_Noise_short_end` | `white_noise_contextual_anomaly_end_507.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `White_Noise_short_end` | `white_noise_contextual_anomaly_end_166.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `White_Noise_short_end` | `white_noise_contextual_anomaly_end_927.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `White_Noise_short_middle` | `white_noise_contextual_anomaly_middle_172.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `White_Noise_short_middle` | `white_noise_contextual_anomaly_middle_395.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `White_Noise_short_middle` | `white_noise_contextual_anomaly_middle_659.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `White_Noise_short_middle` | `white_noise_contextual_anomaly_middle_234.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `White_Noise_short_middle` | `white_noise_contextual_anomaly_middle_159.csv` | `stationary + contextual_anomaly` | ✓ FULL |
| `White_Noise_short_middle` | `white_noise_contextual_anomaly_middle_214.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `White_Noise_short_middle` | `white_noise_contextual_anomaly_middle_351.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
| `White_Noise_short_middle` | `white_noise_contextual_anomaly_middle_674.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `White_Noise_short_middle` | `white_noise_contextual_anomaly_middle_682.csv` | `stationary + collective_anomaly + contextual_anomaly` | ✓ FULL |
| `White_Noise_short_middle` | `white_noise_contextual_anomaly_middle_638.csv` | `stationary + collective_anomaly + contextual_anomaly + point_anomaly` | ✓ FULL |
---

## Grup 7: mean_shift
**Beklenen:** `stationary + mean_shift`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `multiple` | `ar_mean_shift_603.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `ar_mean_shift_755.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `ar_mean_shift_398.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `ar_mean_shift_45.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `ar_mean_shift_649.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `ar_mean_shift_588.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `ar_mean_shift_37.csv` | `stationary` | ~ PARTIAL |
| `multiple` | `ar_mean_shift_516.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `multiple` | `ar_mean_shift_564.csv` | `stationary` | ~ PARTIAL |
| `multiple` | `ar_mean_shift_656.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `ar_mean_shift_495.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `ar_mean_shift_19.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `ar_mean_shift_83.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `ar_mean_shift_745.csv` | `stationary + variance_shift` | ~ PARTIAL |
| `beginning` | `ar_mean_shift_203.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `ar_mean_shift_885.csv` | `stationary` | ~ PARTIAL |
| `beginning` | `ar_mean_shift_701.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `ar_mean_shift_699.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `ar_mean_shift_907.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `ar_mean_shift_807.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `end` | `ar_mean_shift_606.csv` | `stationary` | ~ PARTIAL |
| `end` | `ar_mean_shift_763.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `ar_mean_shift_897.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `ar_mean_shift_297.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `ar_mean_shift_495.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `ar_mean_shift_514.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `ar_mean_shift_917.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `ar_mean_shift_308.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `end` | `ar_mean_shift_48.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `ar_mean_shift_410.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `ar_mean_shift_861.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `ar_mean_shift_516.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `ar_mean_shift_466.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `ar_mean_shift_481.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `ar_mean_shift_771.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `ar_mean_shift_186.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `ar_mean_shift_387.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `ar_mean_shift_492.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `ar_mean_shift_711.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `ar_mean_shift_333.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `ar_mean_shift_443.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `multiple` | `ar_mean_shift_978.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `ar_mean_shift_239.csv` | `stationary + mean_shift + trend_shift + variance_shift` | ✓ FULL |
| `multiple` | `ar_mean_shift_731.csv` | `stationary + mean_shift + variance_shift` | ✓ FULL |
| `multiple` | `ar_mean_shift_95.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `ar_mean_shift_535.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `ar_mean_shift_16.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `ar_mean_shift_182.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `ar_mean_shift_865.csv` | `stationary + collective_anomaly + mean_shift + variance_shift` | ✓ FULL |
| `multiple` | `ar_mean_shift_177.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `ar_mean_shift_184.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `ar_mean_shift_497.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `ar_mean_shift_187.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `ar_mean_shift_785.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `beginning` | `ar_mean_shift_78.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `beginning` | `ar_mean_shift_441.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `ar_mean_shift_847.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `ar_mean_shift_218.csv` | `stationary + mean_shift + variance_shift` | ✓ FULL |
| `beginning` | `ar_mean_shift_610.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `beginning` | `ar_mean_shift_153.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `ar_mean_shift_639.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `ar_mean_shift_980.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `ar_mean_shift_616.csv` | `stationary` | ~ PARTIAL |
| `end` | `ar_mean_shift_401.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `ar_mean_shift_716.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `ar_mean_shift_210.csv` | `stationary + mean_shift + variance_shift` | ✓ FULL |
| `end` | `ar_mean_shift_477.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `end` | `ar_mean_shift_424.csv` | `stationary + mean_shift + variance_shift` | ✓ FULL |
| `end` | `ar_mean_shift_903.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `ar_mean_shift_711.csv` | `stationary + mean_shift + point_anomaly` | ✓ FULL |
| `middle` | `ar_mean_shift_966.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `middle` | `ar_mean_shift_790.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `ar_mean_shift_489.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `ar_mean_shift_899.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `middle` | `ar_mean_shift_942.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `middle` | `ar_mean_shift_763.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `ar_mean_shift_145.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `ar_mean_shift_991.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `middle` | `ar_mean_shift_363.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `ar_mean_shift_651.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `ar_mean_shift_386.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `multiple` | `ar_mean_shift_422.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `multiple` | `ar_mean_shift_194.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly + trend_shift` | ~ PARTIAL |
| `multiple` | `ar_mean_shift_630.csv` | `volatility + collective_anomaly + trend_shift` | ✗ NONE |
| `multiple` | `ar_mean_shift_566.csv` | `stationary + collective_anomaly + mean_shift + point_anomaly + variance_shift` | ✓ FULL |
| `multiple` | `ar_mean_shift_294.csv` | `volatility + collective_anomaly + mean_shift` | ~ PARTIAL |
| `multiple` | `ar_mean_shift_240.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `multiple` | `ar_mean_shift_703.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `multiple` | `ar_mean_shift_542.csv` | `stationary + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `multiple` | `ar_mean_shift_304.csv` | `stationary + collective_anomaly + mean_shift + point_anomaly` | ✓ FULL |
| `beginning` | `ar_mean_shift_88.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ~ PARTIAL |
| `beginning` | `ar_mean_shift_198.csv` | `volatility + collective_anomaly + mean_shift` | ~ PARTIAL |
| `beginning` | `ar_mean_shift_420.csv` | `stochastic_trend + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `beginning` | `ar_mean_shift_878.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ~ PARTIAL |
| `beginning` | `ar_mean_shift_610.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ~ PARTIAL |
| `beginning` | `ar_mean_shift_437.csv` | `volatility + mean_shift + trend_shift` | ~ PARTIAL |
| `beginning` | `ar_mean_shift_203.csv` | `volatility + collective_anomaly + mean_shift` | ~ PARTIAL |
| `beginning` | `ar_mean_shift_800.csv` | `volatility + collective_anomaly + point_anomaly + trend_shift` | ✗ NONE |
| `beginning` | `ar_mean_shift_355.csv` | `volatility + collective_anomaly + mean_shift` | ~ PARTIAL |
| `beginning` | `ar_mean_shift_627.csv` | `volatility + mean_shift + trend_shift` | ~ PARTIAL |
| `end` | `ar_mean_shift_306.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `end` | `ar_mean_shift_842.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `end` | `ar_mean_shift_494.csv` | `stationary + mean_shift + trend_shift + variance_shift` | ✓ FULL |
| `end` | `ar_mean_shift_878.csv` | `stationary + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `end` | `ar_mean_shift_615.csv` | `volatility + mean_shift + point_anomaly + trend_shift` | ~ PARTIAL |
| `end` | `ar_mean_shift_997.csv` | `volatility + collective_anomaly + variance_shift` | ✗ NONE |
| `end` | `ar_mean_shift_805.csv` | `volatility + collective_anomaly + trend_shift` | ✗ NONE |
| `end` | `ar_mean_shift_853.csv` | `stochastic_trend + mean_shift` | ~ PARTIAL |
| `end` | `ar_mean_shift_671.csv` | `volatility + collective_anomaly + mean_shift + trend_shift + variance_shift` | ~ PARTIAL |
| `end` | `ar_mean_shift_664.csv` | `stochastic_trend + mean_shift + point_anomaly + trend_shift` | ~ PARTIAL |
| `middle` | `ar_mean_shift_720.csv` | `stationary + collective_anomaly + mean_shift + trend_shift` | ✓ FULL |
| `middle` | `ar_mean_shift_691.csv` | `stochastic_trend + mean_shift` | ~ PARTIAL |
| `middle` | `ar_mean_shift_611.csv` | `stochastic_trend + mean_shift` | ~ PARTIAL |
| `middle` | `ar_mean_shift_121.csv` | `stationary + collective_anomaly + trend_shift + variance_shift` | ~ PARTIAL |
| `middle` | `ar_mean_shift_66.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ~ PARTIAL |
| `middle` | `ar_mean_shift_955.csv` | `volatility + mean_shift + trend_shift` | ~ PARTIAL |
| `middle` | `ar_mean_shift_704.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `middle` | `ar_mean_shift_863.csv` | `volatility + collective_anomaly + mean_shift` | ~ PARTIAL |
| `middle` | `ar_mean_shift_738.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ~ PARTIAL |
| `middle` | `ar_mean_shift_344.csv` | `stochastic_trend + collective_anomaly + mean_shift + point_anomaly` | ~ PARTIAL |
| `multiple` | `arma_mean_shift_124.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `arma_mean_shift_264.csv` | `stationary` | ~ PARTIAL |
| `multiple` | `arma_mean_shift_35.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `arma_mean_shift_746.csv` | `stationary + mean_shift + variance_shift` | ✓ FULL |
| `multiple` | `arma_mean_shift_800.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `arma_mean_shift_383.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `arma_mean_shift_948.csv` | `stationary + mean_shift + variance_shift` | ✓ FULL |
| `multiple` | `arma_mean_shift_410.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `arma_mean_shift_421.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `arma_mean_shift_103.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `arma_mean_shift_265.csv` | `stationary + collective_anomaly` | ~ PARTIAL |
| `beginning` | `arma_mean_shift_90.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `arma_mean_shift_23.csv` | `stationary` | ~ PARTIAL |
| `beginning` | `arma_mean_shift_62.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `arma_mean_shift_704.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `arma_mean_shift_468.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `arma_mean_shift_162.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `arma_mean_shift_229.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `arma_mean_shift_781.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `arma_mean_shift_682.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `arma_mean_shift_995.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `arma_mean_shift_126.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `arma_mean_shift_182.csv` | `stationary` | ~ PARTIAL |
| `end` | `arma_mean_shift_787.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `arma_mean_shift_588.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `arma_mean_shift_297.csv` | `stationary + point_anomaly` | ~ PARTIAL |
| `end` | `arma_mean_shift_445.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `arma_mean_shift_485.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `arma_mean_shift_516.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `arma_mean_shift_412.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `arma_mean_shift_243.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `arma_mean_shift_439.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `arma_mean_shift_386.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `arma_mean_shift_763.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `arma_mean_shift_398.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `arma_mean_shift_814.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `arma_mean_shift_967.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `arma_mean_shift_621.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `arma_mean_shift_648.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `arma_mean_shift_176.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `arma_mean_shift_912.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `arma_mean_shift_146.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `arma_mean_shift_241.csv` | `stationary + mean_shift + trend_shift + variance_shift` | ✓ FULL |
| `multiple` | `arma_mean_shift_243.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `arma_mean_shift_794.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `arma_mean_shift_668.csv` | `stationary + mean_shift + variance_shift` | ✓ FULL |
| `multiple` | `arma_mean_shift_143.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `arma_mean_shift_72.csv` | `stationary + mean_shift + variance_shift` | ✓ FULL |
| `multiple` | `arma_mean_shift_173.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `multiple` | `arma_mean_shift_349.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `arma_mean_shift_506.csv` | `deterministic_trend + mean_shift` | ~ PARTIAL |
| `beginning` | `arma_mean_shift_708.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `arma_mean_shift_49.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `beginning` | `arma_mean_shift_546.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `arma_mean_shift_658.csv` | `stationary + mean_shift + point_anomaly` | ✓ FULL |
| `beginning` | `arma_mean_shift_505.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `arma_mean_shift_480.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `arma_mean_shift_35.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `arma_mean_shift_297.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `arma_mean_shift_795.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `arma_mean_shift_570.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `arma_mean_shift_202.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `end` | `arma_mean_shift_416.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `arma_mean_shift_495.csv` | `stationary + mean_shift + variance_shift` | ✓ FULL |
| `end` | `arma_mean_shift_20.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `arma_mean_shift_36.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `arma_mean_shift_723.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `arma_mean_shift_645.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `arma_mean_shift_547.csv` | `stationary + mean_shift + variance_shift` | ✓ FULL |
| `end` | `arma_mean_shift_584.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `middle` | `arma_mean_shift_713.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `middle` | `arma_mean_shift_382.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `arma_mean_shift_14.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `arma_mean_shift_300.csv` | `stationary + mean_shift + variance_shift` | ✓ FULL |
| `middle` | `arma_mean_shift_462.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `middle` | `arma_mean_shift_650.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `arma_mean_shift_149.csv` | `stationary + mean_shift + point_anomaly` | ✓ FULL |
| `middle` | `arma_mean_shift_104.csv` | `stochastic_trend + mean_shift` | ~ PARTIAL |
| `middle` | `arma_mean_shift_287.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `arma_mean_shift_376.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `arma_mean_shift_970.csv` | `stationary + collective_anomaly + mean_shift + point_anomaly + trend_shift` | ✓ FULL |
| `multiple` | `arma_mean_shift_293.csv` | `volatility + mean_shift + trend_shift` | ~ PARTIAL |
| `multiple` | `arma_mean_shift_805.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `multiple` | `arma_mean_shift_224.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `multiple` | `arma_mean_shift_802.csv` | `stationary + mean_shift + point_anomaly + trend_shift` | ✓ FULL |
| `multiple` | `arma_mean_shift_333.csv` | `volatility + mean_shift + point_anomaly + variance_shift` | ~ PARTIAL |
| `multiple` | `arma_mean_shift_365.csv` | `volatility + collective_anomaly + mean_shift` | ~ PARTIAL |
| `multiple` | `arma_mean_shift_40.csv` | `stationary + mean_shift + point_anomaly + trend_shift` | ✓ FULL |
| `multiple` | `arma_mean_shift_208.csv` | `volatility + mean_shift + point_anomaly` | ~ PARTIAL |
| `multiple` | `arma_mean_shift_104.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `beginning` | `arma_mean_shift_557.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ~ PARTIAL |
| `beginning` | `arma_mean_shift_787.csv` | `volatility + collective_anomaly + mean_shift` | ~ PARTIAL |
| `beginning` | `arma_mean_shift_495.csv` | `stochastic_trend + collective_anomaly` | ✗ NONE |
| `beginning` | `arma_mean_shift_26.csv` | `volatility + mean_shift` | ~ PARTIAL |
| `beginning` | `arma_mean_shift_217.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly + trend_shift` | ~ PARTIAL |
| `beginning` | `arma_mean_shift_449.csv` | `volatility + collective_anomaly + mean_shift` | ~ PARTIAL |
| `beginning` | `arma_mean_shift_59.csv` | `volatility + collective_anomaly + mean_shift` | ~ PARTIAL |
| `beginning` | `arma_mean_shift_747.csv` | `volatility + mean_shift + trend_shift` | ~ PARTIAL |
| `beginning` | `arma_mean_shift_31.csv` | `volatility + mean_shift` | ~ PARTIAL |
| `beginning` | `arma_mean_shift_56.csv` | `volatility + mean_shift` | ~ PARTIAL |
| `end` | `arma_mean_shift_613.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `end` | `arma_mean_shift_867.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `end` | `arma_mean_shift_714.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ✗ NONE |
| `end` | `arma_mean_shift_841.csv` | `volatility + mean_shift + variance_shift` | ~ PARTIAL |
| `end` | `arma_mean_shift_424.csv` | `stochastic_trend + collective_anomaly` | ✗ NONE |
| `end` | `arma_mean_shift_164.csv` | `volatility + collective_anomaly + mean_shift` | ~ PARTIAL |
| `end` | `arma_mean_shift_464.csv` | `volatility + collective_anomaly + trend_shift` | ✗ NONE |
| `end` | `arma_mean_shift_893.csv` | `volatility + collective_anomaly + mean_shift + trend_shift + variance_shift` | ~ PARTIAL |
| `end` | `arma_mean_shift_782.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `end` | `arma_mean_shift_137.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `middle` | `arma_mean_shift_50.csv` | `stationary + collective_anomaly + mean_shift + point_anomaly + trend_shift` | ✓ FULL |
| `middle` | `arma_mean_shift_115.csv` | `stationary + collective_anomaly + point_anomaly + trend_shift` | ~ PARTIAL |
| `middle` | `arma_mean_shift_521.csv` | `volatility + collective_anomaly + mean_shift` | ~ PARTIAL |
| `middle` | `arma_mean_shift_948.csv` | `stochastic_trend + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `middle` | `arma_mean_shift_17.csv` | `volatility + collective_anomaly + trend_shift` | ✗ NONE |
| `middle` | `arma_mean_shift_893.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `middle` | `arma_mean_shift_387.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `middle` | `arma_mean_shift_629.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `middle` | `arma_mean_shift_494.csv` | `stochastic_trend + collective_anomaly` | ✗ NONE |
| `middle` | `arma_mean_shift_627.csv` | `volatility + collective_anomaly + mean_shift` | ~ PARTIAL |
| `multiple` | `ma_mean_shift_471.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `ma_mean_shift_752.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `ma_mean_shift_689.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `ma_mean_shift_483.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `ma_mean_shift_365.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `ma_mean_shift_203.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `multiple` | `ma_mean_shift_117.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `ma_mean_shift_99.csv` | `stochastic_trend + mean_shift` | ~ PARTIAL |
| `multiple` | `ma_mean_shift_398.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `ma_mean_shift_256.csv` | `stationary + mean_shift + variance_shift` | ✓ FULL |
| `beginning` | `ma_mean_shift_837.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `ma_mean_shift_972.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `ma_mean_shift_668.csv` | `stationary` | ~ PARTIAL |
| `beginning` | `ma_mean_shift_522.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `ma_mean_shift_865.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `ma_mean_shift_734.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `ma_mean_shift_946.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `ma_mean_shift_431.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `ma_mean_shift_18.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `ma_mean_shift_500.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `ma_mean_shift_877.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `ma_mean_shift_196.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `ma_mean_shift_322.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `ma_mean_shift_50.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `ma_mean_shift_641.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `ma_mean_shift_468.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `ma_mean_shift_581.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `ma_mean_shift_170.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `ma_mean_shift_463.csv` | `stationary` | ~ PARTIAL |
| `end` | `ma_mean_shift_900.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `ma_mean_shift_384.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `ma_mean_shift_786.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `ma_mean_shift_410.csv` | `stationary` | ~ PARTIAL |
| `middle` | `ma_mean_shift_301.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `ma_mean_shift_405.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `ma_mean_shift_816.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `ma_mean_shift_253.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `ma_mean_shift_169.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `ma_mean_shift_569.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `ma_mean_shift_682.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `ma_mean_shift_202.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `ma_mean_shift_588.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `ma_mean_shift_569.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `ma_mean_shift_277.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `ma_mean_shift_933.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `multiple` | `ma_mean_shift_813.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `multiple` | `ma_mean_shift_42.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `ma_mean_shift_421.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `ma_mean_shift_769.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `ma_mean_shift_982.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `ma_mean_shift_853.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `ma_mean_shift_693.csv` | `stationary + collective_anomaly` | ~ PARTIAL |
| `beginning` | `ma_mean_shift_85.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `ma_mean_shift_234.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `ma_mean_shift_315.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `ma_mean_shift_193.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `ma_mean_shift_232.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `ma_mean_shift_334.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `ma_mean_shift_280.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `ma_mean_shift_258.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `end` | `ma_mean_shift_653.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `ma_mean_shift_239.csv` | `stationary + collective_anomaly + mean_shift + point_anomaly` | ✓ FULL |
| `end` | `ma_mean_shift_8.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `end` | `ma_mean_shift_799.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `ma_mean_shift_702.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `ma_mean_shift_168.csv` | `stochastic_trend + mean_shift` | ~ PARTIAL |
| `end` | `ma_mean_shift_261.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `ma_mean_shift_976.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `ma_mean_shift_810.csv` | `stationary` | ~ PARTIAL |
| `end` | `ma_mean_shift_678.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `ma_mean_shift_553.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `ma_mean_shift_526.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `ma_mean_shift_794.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `ma_mean_shift_618.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `ma_mean_shift_8.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `ma_mean_shift_632.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `middle` | `ma_mean_shift_511.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `ma_mean_shift_726.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `ma_mean_shift_950.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `ma_mean_shift_911.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `ma_mean_shift_619.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ~ PARTIAL |
| `multiple` | `ma_mean_shift_691.csv` | `stochastic_trend + collective_anomaly + point_anomaly + trend_shift` | ✗ NONE |
| `multiple` | `ma_mean_shift_684.csv` | `volatility + collective_anomaly + mean_shift + trend_shift + variance_shift` | ~ PARTIAL |
| `multiple` | `ma_mean_shift_674.csv` | `volatility + mean_shift` | ~ PARTIAL |
| `multiple` | `ma_mean_shift_396.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ~ PARTIAL |
| `multiple` | `ma_mean_shift_895.csv` | `volatility + mean_shift + trend_shift` | ~ PARTIAL |
| `multiple` | `ma_mean_shift_994.csv` | `volatility + collective_anomaly + trend_shift` | ✗ NONE |
| `multiple` | `ma_mean_shift_677.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `multiple` | `ma_mean_shift_39.csv` | `volatility + collective_anomaly + mean_shift + trend_shift + variance_shift` | ~ PARTIAL |
| `multiple` | `ma_mean_shift_237.csv` | `volatility + mean_shift + trend_shift` | ~ PARTIAL |
| `beginning` | `ma_mean_shift_503.csv` | `stationary + collective_anomaly + trend_shift` | ~ PARTIAL |
| `beginning` | `ma_mean_shift_160.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `beginning` | `ma_mean_shift_530.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `beginning` | `ma_mean_shift_505.csv` | `volatility + collective_anomaly + mean_shift` | ~ PARTIAL |
| `beginning` | `ma_mean_shift_680.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `beginning` | `ma_mean_shift_378.csv` | `volatility + collective_anomaly + point_anomaly + trend_shift` | ✗ NONE |
| `beginning` | `ma_mean_shift_832.csv` | `volatility + collective_anomaly + mean_shift` | ~ PARTIAL |
| `beginning` | `ma_mean_shift_351.csv` | `volatility + collective_anomaly + mean_shift` | ~ PARTIAL |
| `beginning` | `ma_mean_shift_643.csv` | `volatility + collective_anomaly + mean_shift` | ~ PARTIAL |
| `beginning` | `ma_mean_shift_15.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `end` | `ma_mean_shift_422.csv` | `volatility + collective_anomaly + mean_shift` | ~ PARTIAL |
| `end` | `ma_mean_shift_566.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `end` | `ma_mean_shift_166.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ~ PARTIAL |
| `end` | `ma_mean_shift_384.csv` | `stochastic_trend + mean_shift` | ~ PARTIAL |
| `end` | `ma_mean_shift_523.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `end` | `ma_mean_shift_514.csv` | `volatility + collective_anomaly + mean_shift + trend_shift + variance_shift` | ~ PARTIAL |
| `end` | `ma_mean_shift_132.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `end` | `ma_mean_shift_150.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ✗ NONE |
| `end` | `ma_mean_shift_438.csv` | `stochastic_trend + collective_anomaly + mean_shift + point_anomaly + trend_shift` | ~ PARTIAL |
| `end` | `ma_mean_shift_865.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ~ PARTIAL |
| `middle` | `ma_mean_shift_362.csv` | `volatility + mean_shift` | ~ PARTIAL |
| `middle` | `ma_mean_shift_169.csv` | `stochastic_trend + collective_anomaly + mean_shift + point_anomaly + trend_shift` | ~ PARTIAL |
| `middle` | `ma_mean_shift_693.csv` | `volatility + collective_anomaly + mean_shift + variance_shift` | ~ PARTIAL |
| `middle` | `ma_mean_shift_895.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `middle` | `ma_mean_shift_887.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly + trend_shift` | ~ PARTIAL |
| `middle` | `ma_mean_shift_181.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ~ PARTIAL |
| `middle` | `ma_mean_shift_665.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `middle` | `ma_mean_shift_646.csv` | `volatility + mean_shift + trend_shift` | ~ PARTIAL |
| `middle` | `ma_mean_shift_566.csv` | `volatility + collective_anomaly + mean_shift` | ~ PARTIAL |
| `middle` | `ma_mean_shift_452.csv` | `volatility + mean_shift + variance_shift` | ~ PARTIAL |
| `multiple` | `white_noise_mean_shift_524.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `white_noise_mean_shift_633.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `white_noise_mean_shift_609.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `white_noise_mean_shift_979.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `white_noise_mean_shift_828.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `white_noise_mean_shift_78.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `white_noise_mean_shift_924.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `white_noise_mean_shift_136.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `white_noise_mean_shift_512.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `white_noise_mean_shift_936.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `white_noise_mean_shift_845.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `white_noise_mean_shift_625.csv` | `stationary` | ~ PARTIAL |
| `beginning` | `white_noise_mean_shift_7.csv` | `stationary` | ~ PARTIAL |
| `beginning` | `white_noise_mean_shift_271.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `white_noise_mean_shift_395.csv` | `stationary` | ~ PARTIAL |
| `beginning` | `white_noise_mean_shift_656.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `white_noise_mean_shift_537.csv` | `stationary` | ~ PARTIAL |
| `beginning` | `white_noise_mean_shift_560.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `white_noise_mean_shift_237.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `white_noise_mean_shift_981.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `white_noise_mean_shift_155.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `white_noise_mean_shift_513.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `white_noise_mean_shift_193.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `white_noise_mean_shift_846.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `white_noise_mean_shift_927.csv` | `stationary` | ~ PARTIAL |
| `end` | `white_noise_mean_shift_870.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `white_noise_mean_shift_414.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `white_noise_mean_shift_757.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `white_noise_mean_shift_176.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `white_noise_mean_shift_563.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `white_noise_mean_shift_694.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `white_noise_mean_shift_257.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `white_noise_mean_shift_134.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `white_noise_mean_shift_326.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `white_noise_mean_shift_750.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `white_noise_mean_shift_501.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `white_noise_mean_shift_502.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `white_noise_mean_shift_581.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `white_noise_mean_shift_580.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `white_noise_mean_shift_660.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `white_noise_mean_shift_244.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `white_noise_mean_shift_433.csv` | `stationary + mean_shift + variance_shift` | ✓ FULL |
| `multiple` | `white_noise_mean_shift_441.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `white_noise_mean_shift_944.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `white_noise_mean_shift_359.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `white_noise_mean_shift_455.csv` | `stationary + mean_shift + variance_shift` | ✓ FULL |
| `multiple` | `white_noise_mean_shift_475.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `white_noise_mean_shift_812.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `multiple` | `white_noise_mean_shift_41.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
| `multiple` | `white_noise_mean_shift_724.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `white_noise_mean_shift_65.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `white_noise_mean_shift_146.csv` | `stationary + mean_shift + point_anomaly` | ✓ FULL |
| `beginning` | `white_noise_mean_shift_826.csv` | `stationary + mean_shift + point_anomaly` | ✓ FULL |
| `beginning` | `white_noise_mean_shift_680.csv` | `stationary + mean_shift + point_anomaly` | ✓ FULL |
| `beginning` | `white_noise_mean_shift_695.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `white_noise_mean_shift_406.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `white_noise_mean_shift_159.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `white_noise_mean_shift_401.csv` | `stationary + mean_shift + point_anomaly` | ✓ FULL |
| `beginning` | `white_noise_mean_shift_185.csv` | `stationary + mean_shift` | ✓ FULL |
| `beginning` | `white_noise_mean_shift_612.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `white_noise_mean_shift_723.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `white_noise_mean_shift_454.csv` | `stationary + mean_shift + variance_shift` | ✓ FULL |
| `end` | `white_noise_mean_shift_36.csv` | `stationary` | ~ PARTIAL |
| `end` | `white_noise_mean_shift_330.csv` | `stationary + mean_shift + trend_shift + variance_shift` | ✓ FULL |
| `end` | `white_noise_mean_shift_766.csv` | `stationary` | ~ PARTIAL |
| `end` | `white_noise_mean_shift_884.csv` | `stationary + mean_shift + variance_shift` | ✓ FULL |
| `end` | `white_noise_mean_shift_703.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `white_noise_mean_shift_988.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `white_noise_mean_shift_934.csv` | `stationary + mean_shift` | ✓ FULL |
| `end` | `white_noise_mean_shift_654.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `white_noise_mean_shift_903.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `white_noise_mean_shift_236.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `white_noise_mean_shift_405.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `white_noise_mean_shift_173.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `white_noise_mean_shift_635.csv` | `stationary + mean_shift + variance_shift` | ✓ FULL |
| `middle` | `white_noise_mean_shift_71.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `white_noise_mean_shift_228.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `white_noise_mean_shift_943.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `white_noise_mean_shift_420.csv` | `stationary + mean_shift` | ✓ FULL |
| `middle` | `white_noise_mean_shift_384.csv` | `stationary + mean_shift` | ✓ FULL |
| `multiple` | `white_noise_mean_shift_990.csv` | `volatility + collective_anomaly + mean_shift` | ~ PARTIAL |
| `multiple` | `white_noise_mean_shift_702.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `multiple` | `white_noise_mean_shift_742.csv` | `volatility + mean_shift + trend_shift + variance_shift` | ~ PARTIAL |
| `multiple` | `white_noise_mean_shift_709.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ~ PARTIAL |
| `multiple` | `white_noise_mean_shift_46.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `multiple` | `white_noise_mean_shift_217.csv` | `volatility + point_anomaly + trend_shift` | ✗ NONE |
| `multiple` | `white_noise_mean_shift_647.csv` | `volatility + mean_shift + point_anomaly` | ~ PARTIAL |
| `multiple` | `white_noise_mean_shift_751.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `multiple` | `white_noise_mean_shift_963.csv` | `volatility + mean_shift + trend_shift` | ~ PARTIAL |
| `multiple` | `white_noise_mean_shift_176.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `beginning` | `white_noise_mean_shift_384.csv` | `volatility + mean_shift + trend_shift` | ~ PARTIAL |
| `beginning` | `white_noise_mean_shift_613.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly + variance_shift` | ~ PARTIAL |
| `beginning` | `white_noise_mean_shift_445.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `beginning` | `white_noise_mean_shift_691.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `beginning` | `white_noise_mean_shift_828.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `beginning` | `white_noise_mean_shift_400.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ~ PARTIAL |
| `beginning` | `white_noise_mean_shift_848.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly + trend_shift` | ~ PARTIAL |
| `beginning` | `white_noise_mean_shift_215.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `beginning` | `white_noise_mean_shift_716.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `beginning` | `white_noise_mean_shift_746.csv` | `volatility + mean_shift + point_anomaly` | ~ PARTIAL |
| `end` | `white_noise_mean_shift_862.csv` | `volatility + collective_anomaly + mean_shift + variance_shift` | ~ PARTIAL |
| `end` | `white_noise_mean_shift_971.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `end` | `white_noise_mean_shift_78.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `end` | `white_noise_mean_shift_73.csv` | `stationary + collective_anomaly + mean_shift + trend_shift` | ✓ FULL |
| `end` | `white_noise_mean_shift_94.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ~ PARTIAL |
| `end` | `white_noise_mean_shift_584.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `end` | `white_noise_mean_shift_184.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `end` | `white_noise_mean_shift_694.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ~ PARTIAL |
| `end` | `white_noise_mean_shift_716.csv` | `volatility + mean_shift + trend_shift` | ~ PARTIAL |
| `end` | `white_noise_mean_shift_489.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `middle` | `white_noise_mean_shift_567.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ✗ NONE |
| `middle` | `white_noise_mean_shift_431.csv` | `volatility + mean_shift` | ~ PARTIAL |
| `middle` | `white_noise_mean_shift_114.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `middle` | `white_noise_mean_shift_432.csv` | `volatility + mean_shift + trend_shift` | ~ PARTIAL |
| `middle` | `white_noise_mean_shift_383.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly + trend_shift` | ~ PARTIAL |
| `middle` | `white_noise_mean_shift_264.csv` | `volatility + mean_shift + trend_shift` | ~ PARTIAL |
| `middle` | `white_noise_mean_shift_975.csv` | `volatility + mean_shift + trend_shift` | ~ PARTIAL |
| `middle` | `white_noise_mean_shift_296.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `middle` | `white_noise_mean_shift_412.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `middle` | `white_noise_mean_shift_972.csv` | `stationary + collective_anomaly + mean_shift` | ✓ FULL |
---

## Grup 8: point_anomaly
**Beklenen:** `stationary + point_anomaly`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `multiple` | `ar_point_anomaly_multiple_804.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `ar_point_anomaly_multiple_546.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `ar_point_anomaly_multiple_275.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `ar_point_anomaly_multiple_306.csv` | `stationary` | ~ PARTIAL |
| `multiple` | `ar_point_anomaly_multiple_224.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `ar_point_anomaly_multiple_240.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `ar_point_anomaly_multiple_17.csv` | `stationary` | ~ PARTIAL |
| `multiple` | `ar_point_anomaly_multiple_370.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `ar_point_anomaly_multiple_877.csv` | `stationary` | ~ PARTIAL |
| `multiple` | `ar_point_anomaly_multiple_825.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `ar_point_anomaly_single_beginning_191.csv` | `stationary + collective_anomaly` | ~ PARTIAL |
| `beginning` | `ar_point_anomaly_single_beginning_566.csv` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `beginning` | `ar_point_anomaly_single_beginning_809.csv` | `stationary` | ~ PARTIAL |
| `beginning` | `ar_point_anomaly_single_beginning_596.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `beginning` | `ar_point_anomaly_single_beginning_869.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `ar_point_anomaly_single_beginning_78.csv` | `stationary` | ~ PARTIAL |
| `beginning` | `ar_point_anomaly_single_beginning_912.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `ar_point_anomaly_single_beginning_584.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `ar_point_anomaly_single_beginning_132.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `ar_point_anomaly_single_beginning_708.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `ar_point_anomaly_single_end_408.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `ar_point_anomaly_single_end_906.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `ar_point_anomaly_single_end_804.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `ar_point_anomaly_single_end_668.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `ar_point_anomaly_single_end_219.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `ar_point_anomaly_single_end_649.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `ar_point_anomaly_single_end_445.csv` | `stationary` | ~ PARTIAL |
| `end` | `ar_point_anomaly_single_end_24.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `ar_point_anomaly_single_end_248.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `ar_point_anomaly_single_end_265.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `ar_point_anomaly_single_middle_865.csv` | `stationary + collective_anomaly` | ~ PARTIAL |
| `middle` | `ar_point_anomaly_single_middle_737.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `ar_point_anomaly_single_middle_809.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `ar_point_anomaly_single_middle_674.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `ar_point_anomaly_single_middle_844.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `ar_point_anomaly_single_middle_930.csv` | `stationary + collective_anomaly` | ~ PARTIAL |
| `middle` | `ar_point_anomaly_single_middle_250.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `middle` | `ar_point_anomaly_single_middle_763.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `ar_point_anomaly_single_middle_501.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `ar_point_anomaly_single_middle_138.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `ar_point_anomaly_multiple_477.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `ar_point_anomaly_multiple_434.csv` | `stationary + collective_anomaly` | ~ PARTIAL |
| `multiple` | `ar_point_anomaly_multiple_721.csv` | `stationary` | ~ PARTIAL |
| `multiple` | `ar_point_anomaly_multiple_761.csv` | `stationary + mean_shift + point_anomaly + variance_shift` | ✓ FULL |
| `multiple` | `ar_point_anomaly_multiple_317.csv` | `stationary + collective_anomaly + mean_shift` | ~ PARTIAL |
| `multiple` | `ar_point_anomaly_multiple_992.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `ar_point_anomaly_multiple_507.csv` | `stationary + collective_anomaly + mean_shift + point_anomaly` | ✓ FULL |
| `multiple` | `ar_point_anomaly_multiple_661.csv` | `stationary + collective_anomaly + mean_shift` | ~ PARTIAL |
| `multiple` | `ar_point_anomaly_multiple_360.csv` | `stationary + collective_anomaly + variance_shift` | ~ PARTIAL |
| `multiple` | `ar_point_anomaly_multiple_792.csv` | `stationary + mean_shift + point_anomaly + variance_shift` | ✓ FULL |
| `beginning` | `ar_point_anomaly_single_beginning_789.csv` | `stationary` | ~ PARTIAL |
| `beginning` | `ar_point_anomaly_single_beginning_820.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `beginning` | `ar_point_anomaly_single_beginning_511.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `ar_point_anomaly_single_beginning_313.csv` | `stationary + variance_shift` | ~ PARTIAL |
| `beginning` | `ar_point_anomaly_single_beginning_590.csv` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `beginning` | `ar_point_anomaly_single_beginning_318.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `ar_point_anomaly_single_beginning_383.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `ar_point_anomaly_single_beginning_989.csv` | `stationary` | ~ PARTIAL |
| `beginning` | `ar_point_anomaly_single_beginning_844.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `beginning` | `ar_point_anomaly_single_beginning_821.csv` | `stationary + variance_shift` | ~ PARTIAL |
| `end` | `ar_point_anomaly_single_end_530.csv` | `stationary + collective_anomaly + mean_shift + point_anomaly` | ✓ FULL |
| `end` | `ar_point_anomaly_single_end_931.csv` | `stationary + variance_shift` | ~ PARTIAL |
| `end` | `ar_point_anomaly_single_end_869.csv` | `stationary + mean_shift + point_anomaly` | ✓ FULL |
| `end` | `ar_point_anomaly_single_end_277.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `ar_point_anomaly_single_end_437.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `end` | `ar_point_anomaly_single_end_723.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `end` | `ar_point_anomaly_single_end_971.csv` | `stationary + variance_shift` | ~ PARTIAL |
| `end` | `ar_point_anomaly_single_end_624.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `ar_point_anomaly_single_end_504.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `ar_point_anomaly_single_end_523.csv` | `stationary + collective_anomaly + mean_shift + point_anomaly + variance_shift` | ✓ FULL |
| `middle` | `ar_point_anomaly_single_middle_807.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `ar_point_anomaly_single_middle_358.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `ar_point_anomaly_single_middle_815.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `middle` | `ar_point_anomaly_single_middle_450.csv` | `stationary + variance_shift` | ~ PARTIAL |
| `middle` | `ar_point_anomaly_single_middle_561.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `ar_point_anomaly_single_middle_585.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `ar_point_anomaly_single_middle_484.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `ar_point_anomaly_single_middle_99.csv` | `stationary` | ~ PARTIAL |
| `middle` | `ar_point_anomaly_single_middle_247.csv` | `stationary + mean_shift + variance_shift` | ~ PARTIAL |
| `middle` | `ar_point_anomaly_single_middle_851.csv` | `stationary + variance_shift` | ~ PARTIAL |
| `multiple` | `ar_point_anomaly_multiple_282.csv` | `volatility + collective_anomaly + mean_shift` | ✗ NONE |
| `multiple` | `ar_point_anomaly_multiple_837.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `multiple` | `ar_point_anomaly_multiple_656.csv` | `volatility + collective_anomaly + variance_shift` | ✗ NONE |
| `multiple` | `ar_point_anomaly_multiple_225.csv` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `ar_point_anomaly_multiple_902.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `multiple` | `ar_point_anomaly_multiple_329.csv` | `volatility + collective_anomaly + point_anomaly + trend_shift` | ~ PARTIAL |
| `multiple` | `ar_point_anomaly_multiple_146.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `multiple` | `ar_point_anomaly_multiple_69.csv` | `volatility + collective_anomaly + mean_shift` | ✗ NONE |
| `multiple` | `ar_point_anomaly_multiple_541.csv` | `volatility + collective_anomaly + point_anomaly + trend_shift` | ~ PARTIAL |
| `multiple` | `ar_point_anomaly_multiple_904.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `beginning` | `ar_point_anomaly_single_beginning_440.csv` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `beginning` | `ar_point_anomaly_single_beginning_609.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `beginning` | `ar_point_anomaly_single_beginning_96.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `beginning` | `ar_point_anomaly_single_beginning_193.csv` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `beginning` | `ar_point_anomaly_single_beginning_754.csv` | `volatility + collective_anomaly + mean_shift` | ✗ NONE |
| `beginning` | `ar_point_anomaly_single_beginning_879.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `ar_point_anomaly_single_beginning_574.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `beginning` | `ar_point_anomaly_single_beginning_883.csv` | `stationary + variance_shift` | ~ PARTIAL |
| `beginning` | `ar_point_anomaly_single_beginning_212.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `beginning` | `ar_point_anomaly_single_beginning_360.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `end` | `ar_point_anomaly_single_end_175.csv` | `volatility + collective_anomaly + mean_shift` | ✗ NONE |
| `end` | `ar_point_anomaly_single_end_801.csv` | `volatility + variance_shift` | ✗ NONE |
| `end` | `ar_point_anomaly_single_end_246.csv` | `stationary + collective_anomaly + point_anomaly + variance_shift` | ✓ FULL |
| `end` | `ar_point_anomaly_single_end_35.csv` | `stochastic_trend + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `end` | `ar_point_anomaly_single_end_512.csv` | `volatility + mean_shift` | ✗ NONE |
| `end` | `ar_point_anomaly_single_end_933.csv` | `volatility + collective_anomaly + variance_shift` | ✗ NONE |
| `end` | `ar_point_anomaly_single_end_571.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `end` | `ar_point_anomaly_single_end_233.csv` | `volatility + collective_anomaly + point_anomaly + trend_shift` | ~ PARTIAL |
| `end` | `ar_point_anomaly_single_end_864.csv` | `stochastic_trend + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `end` | `ar_point_anomaly_single_end_500.csv` | `stationary + collective_anomaly + trend_shift` | ~ PARTIAL |
| `middle` | `ar_point_anomaly_single_middle_182.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `middle` | `ar_point_anomaly_single_middle_971.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `middle` | `ar_point_anomaly_single_middle_938.csv` | `volatility + collective_anomaly + point_anomaly + trend_shift + variance_shift` | ~ PARTIAL |
| `middle` | `ar_point_anomaly_single_middle_302.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `middle` | `ar_point_anomaly_single_middle_851.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ~ PARTIAL |
| `middle` | `ar_point_anomaly_single_middle_513.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ~ PARTIAL |
| `middle` | `ar_point_anomaly_single_middle_913.csv` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `middle` | `ar_point_anomaly_single_middle_42.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `middle` | `ar_point_anomaly_single_middle_956.csv` | `volatility + point_anomaly` | ~ PARTIAL |
| `middle` | `ar_point_anomaly_single_middle_122.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `multiple` | `arma_point_anomaly_multiple_480.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `arma_point_anomaly_multiple_147.csv` | `stationary` | ~ PARTIAL |
| `multiple` | `arma_point_anomaly_multiple_463.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `arma_point_anomaly_multiple_561.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `arma_point_anomaly_multiple_442.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `multiple` | `arma_point_anomaly_multiple_315.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `arma_point_anomaly_multiple_454.csv` | `stationary` | ~ PARTIAL |
| `multiple` | `arma_point_anomaly_multiple_173.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `arma_point_anomaly_multiple_443.csv` | `stationary` | ~ PARTIAL |
| `multiple` | `arma_point_anomaly_multiple_304.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `arma_point_anomaly_single_beginning_123.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `arma_point_anomaly_single_beginning_392.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `arma_point_anomaly_single_beginning_957.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `arma_point_anomaly_single_beginning_19.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `arma_point_anomaly_single_beginning_872.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `arma_point_anomaly_single_beginning_757.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `arma_point_anomaly_single_beginning_698.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `arma_point_anomaly_single_beginning_407.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `beginning` | `arma_point_anomaly_single_beginning_828.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `arma_point_anomaly_single_beginning_232.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `arma_point_anomaly_single_end_224.csv` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `end` | `arma_point_anomaly_single_end_133.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `arma_point_anomaly_single_end_362.csv` | `stationary` | ~ PARTIAL |
| `end` | `arma_point_anomaly_single_end_944.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `arma_point_anomaly_single_end_863.csv` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `end` | `arma_point_anomaly_single_end_533.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `arma_point_anomaly_single_end_74.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `arma_point_anomaly_single_end_865.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `arma_point_anomaly_single_end_226.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `arma_point_anomaly_single_end_799.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `arma_point_anomaly_single_middle_749.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `arma_point_anomaly_single_middle_530.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `arma_point_anomaly_single_middle_511.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `arma_point_anomaly_single_middle_666.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `arma_point_anomaly_single_middle_102.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `arma_point_anomaly_single_middle_933.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `arma_point_anomaly_single_middle_171.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `arma_point_anomaly_single_middle_115.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `arma_point_anomaly_single_middle_334.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `arma_point_anomaly_single_middle_297.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `arma_point_anomaly_multiple_869.csv` | `stationary` | ~ PARTIAL |
| `multiple` | `arma_point_anomaly_multiple_236.csv` | `stationary` | ~ PARTIAL |
| `multiple` | `arma_point_anomaly_multiple_603.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `arma_point_anomaly_multiple_965.csv` | `stationary + collective_anomaly + mean_shift + point_anomaly + variance_shift` | ✓ FULL |
| `multiple` | `arma_point_anomaly_multiple_769.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `arma_point_anomaly_multiple_66.csv` | `volatility` | ✗ NONE |
| `multiple` | `arma_point_anomaly_multiple_585.csv` | `stationary + collective_anomaly + mean_shift` | ~ PARTIAL |
| `multiple` | `arma_point_anomaly_multiple_489.csv` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `arma_point_anomaly_multiple_20.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `multiple` | `arma_point_anomaly_multiple_813.csv` | `stationary` | ~ PARTIAL |
| `beginning` | `arma_point_anomaly_single_beginning_364.csv` | `stationary + collective_anomaly` | ~ PARTIAL |
| `beginning` | `arma_point_anomaly_single_beginning_317.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `arma_point_anomaly_single_beginning_376.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `beginning` | `arma_point_anomaly_single_beginning_21.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `arma_point_anomaly_single_beginning_141.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `beginning` | `arma_point_anomaly_single_beginning_318.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `beginning` | `arma_point_anomaly_single_beginning_485.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `arma_point_anomaly_single_beginning_688.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `arma_point_anomaly_single_beginning_83.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `arma_point_anomaly_single_beginning_672.csv` | `stationary + collective_anomaly` | ~ PARTIAL |
| `end` | `arma_point_anomaly_single_end_52.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `arma_point_anomaly_single_end_156.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `end` | `arma_point_anomaly_single_end_20.csv` | `stationary + collective_anomaly + variance_shift` | ~ PARTIAL |
| `end` | `arma_point_anomaly_single_end_87.csv` | `stochastic_trend + mean_shift` | ✗ NONE |
| `end` | `arma_point_anomaly_single_end_932.csv` | `stationary + variance_shift` | ~ PARTIAL |
| `end` | `arma_point_anomaly_single_end_559.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `end` | `arma_point_anomaly_single_end_649.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `end` | `arma_point_anomaly_single_end_592.csv` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `end` | `arma_point_anomaly_single_end_112.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `arma_point_anomaly_single_end_681.csv` | `stationary + collective_anomaly` | ~ PARTIAL |
| `middle` | `arma_point_anomaly_single_middle_573.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `arma_point_anomaly_single_middle_628.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `arma_point_anomaly_single_middle_320.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `arma_point_anomaly_single_middle_760.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `arma_point_anomaly_single_middle_230.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `arma_point_anomaly_single_middle_367.csv` | `stationary + variance_shift` | ~ PARTIAL |
| `middle` | `arma_point_anomaly_single_middle_494.csv` | `stationary + mean_shift + point_anomaly` | ✓ FULL |
| `middle` | `arma_point_anomaly_single_middle_10.csv` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `middle` | `arma_point_anomaly_single_middle_665.csv` | `stationary + collective_anomaly + mean_shift` | ~ PARTIAL |
| `middle` | `arma_point_anomaly_single_middle_423.csv` | `stationary + collective_anomaly + mean_shift + point_anomaly` | ✓ FULL |
| `multiple` | `arma_point_anomaly_multiple_32.csv` | `volatility + collective_anomaly + variance_shift` | ✗ NONE |
| `multiple` | `arma_point_anomaly_multiple_624.csv` | `volatility + variance_shift` | ✗ NONE |
| `multiple` | `arma_point_anomaly_multiple_482.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `multiple` | `arma_point_anomaly_multiple_270.csv` | `volatility + point_anomaly + variance_shift` | ~ PARTIAL |
| `multiple` | `arma_point_anomaly_multiple_710.csv` | `volatility + mean_shift` | ✗ NONE |
| `multiple` | `arma_point_anomaly_multiple_714.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `multiple` | `arma_point_anomaly_multiple_177.csv` | `stationary` | ~ PARTIAL |
| `multiple` | `arma_point_anomaly_multiple_581.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `multiple` | `arma_point_anomaly_multiple_998.csv` | `volatility + mean_shift + variance_shift` | ✗ NONE |
| `multiple` | `arma_point_anomaly_multiple_430.csv` | `stochastic_trend + point_anomaly` | ~ PARTIAL |
| `beginning` | `arma_point_anomaly_single_beginning_160.csv` | `volatility + collective_anomaly + trend_shift` | ✗ NONE |
| `beginning` | `arma_point_anomaly_single_beginning_978.csv` | `volatility + point_anomaly` | ~ PARTIAL |
| `beginning` | `arma_point_anomaly_single_beginning_583.csv` | `volatility` | ✗ NONE |
| `beginning` | `arma_point_anomaly_single_beginning_60.csv` | `stationary + collective_anomaly + point_anomaly + variance_shift` | ✓ FULL |
| `beginning` | `arma_point_anomaly_single_beginning_566.csv` | `volatility + collective_anomaly + mean_shift` | ✗ NONE |
| `beginning` | `arma_point_anomaly_single_beginning_823.csv` | `stochastic_trend + collective_anomaly` | ✗ NONE |
| `beginning` | `arma_point_anomaly_single_beginning_609.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `beginning` | `arma_point_anomaly_single_beginning_116.csv` | `volatility + mean_shift + point_anomaly` | ~ PARTIAL |
| `beginning` | `arma_point_anomaly_single_beginning_458.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `beginning` | `arma_point_anomaly_single_beginning_903.csv` | `volatility + point_anomaly` | ~ PARTIAL |
| `end` | `arma_point_anomaly_single_end_531.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `arma_point_anomaly_single_end_138.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `end` | `arma_point_anomaly_single_end_684.csv` | `stationary + variance_shift` | ~ PARTIAL |
| `end` | `arma_point_anomaly_single_end_455.csv` | `volatility + collective_anomaly + mean_shift + variance_shift` | ✗ NONE |
| `end` | `arma_point_anomaly_single_end_442.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `end` | `arma_point_anomaly_single_end_331.csv` | `volatility + point_anomaly` | ~ PARTIAL |
| `end` | `arma_point_anomaly_single_end_788.csv` | `stationary + collective_anomaly` | ~ PARTIAL |
| `end` | `arma_point_anomaly_single_end_112.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `end` | `arma_point_anomaly_single_end_427.csv` | `volatility + collective_anomaly + variance_shift` | ✗ NONE |
| `end` | `arma_point_anomaly_single_end_825.csv` | `volatility + collective_anomaly + mean_shift` | ✗ NONE |
| `middle` | `arma_point_anomaly_single_middle_160.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `middle` | `arma_point_anomaly_single_middle_416.csv` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `middle` | `arma_point_anomaly_single_middle_32.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `middle` | `arma_point_anomaly_single_middle_774.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `middle` | `arma_point_anomaly_single_middle_703.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `middle` | `arma_point_anomaly_single_middle_678.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `middle` | `arma_point_anomaly_single_middle_194.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `middle` | `arma_point_anomaly_single_middle_81.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `middle` | `arma_point_anomaly_single_middle_634.csv` | `stationary + collective_anomaly + point_anomaly + trend_shift + variance_shift` | ✓ FULL |
| `middle` | `arma_point_anomaly_single_middle_776.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `multiple` | `ma_point_anomaly_multiple_796.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `ma_point_anomaly_multiple_404.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `ma_point_anomaly_multiple_220.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `ma_point_anomaly_multiple_139.csv` | `stationary` | ~ PARTIAL |
| `multiple` | `ma_point_anomaly_multiple_422.csv` | `stationary` | ~ PARTIAL |
| `multiple` | `ma_point_anomaly_multiple_601.csv` | `stationary` | ~ PARTIAL |
| `multiple` | `ma_point_anomaly_multiple_41.csv` | `stationary` | ~ PARTIAL |
| `multiple` | `ma_point_anomaly_multiple_849.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `ma_point_anomaly_multiple_691.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `ma_point_anomaly_multiple_26.csv` | `stationary` | ~ PARTIAL |
| `beginning` | `ma_point_anomaly_single_beginning_864.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `ma_point_anomaly_single_beginning_816.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `ma_point_anomaly_single_beginning_73.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `ma_point_anomaly_single_beginning_526.csv` | `stationary` | ~ PARTIAL |
| `beginning` | `ma_point_anomaly_single_beginning_74.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `ma_point_anomaly_single_beginning_54.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `ma_point_anomaly_single_beginning_680.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `ma_point_anomaly_single_beginning_266.csv` | `stationary` | ~ PARTIAL |
| `beginning` | `ma_point_anomaly_single_beginning_846.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `ma_point_anomaly_single_beginning_222.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `ma_point_anomaly_single_end_156.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `ma_point_anomaly_single_end_759.csv` | `stationary` | ~ PARTIAL |
| `end` | `ma_point_anomaly_single_end_813.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `ma_point_anomaly_single_end_969.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `ma_point_anomaly_single_end_52.csv` | `stationary` | ~ PARTIAL |
| `end` | `ma_point_anomaly_single_end_131.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `ma_point_anomaly_single_end_369.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `ma_point_anomaly_single_end_284.csv` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `end` | `ma_point_anomaly_single_end_138.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `ma_point_anomaly_single_end_828.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `ma_point_anomaly_single_middle_282.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `ma_point_anomaly_single_middle_915.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `ma_point_anomaly_single_middle_136.csv` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `middle` | `ma_point_anomaly_single_middle_39.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `ma_point_anomaly_single_middle_959.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `ma_point_anomaly_single_middle_384.csv` | `stationary` | ~ PARTIAL |
| `middle` | `ma_point_anomaly_single_middle_573.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `ma_point_anomaly_single_middle_465.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `ma_point_anomaly_single_middle_85.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `ma_point_anomaly_single_middle_6.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `ma_point_anomaly_multiple_534.csv` | `stationary` | ~ PARTIAL |
| `multiple` | `ma_point_anomaly_multiple_331.csv` | `stationary` | ~ PARTIAL |
| `multiple` | `ma_point_anomaly_multiple_131.csv` | `stationary` | ~ PARTIAL |
| `multiple` | `ma_point_anomaly_multiple_793.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `ma_point_anomaly_multiple_695.csv` | `stationary + collective_anomaly + point_anomaly + variance_shift` | ✓ FULL |
| `multiple` | `ma_point_anomaly_multiple_274.csv` | `volatility + mean_shift` | ✗ NONE |
| `multiple` | `ma_point_anomaly_multiple_361.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `ma_point_anomaly_multiple_427.csv` | `stationary + collective_anomaly` | ~ PARTIAL |
| `multiple` | `ma_point_anomaly_multiple_893.csv` | `stationary + variance_shift` | ~ PARTIAL |
| `multiple` | `ma_point_anomaly_multiple_818.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `ma_point_anomaly_single_beginning_141.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `ma_point_anomaly_single_beginning_897.csv` | `stationary + variance_shift` | ~ PARTIAL |
| `beginning` | `ma_point_anomaly_single_beginning_702.csv` | `stationary + collective_anomaly + mean_shift` | ~ PARTIAL |
| `beginning` | `ma_point_anomaly_single_beginning_403.csv` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `beginning` | `ma_point_anomaly_single_beginning_35.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `beginning` | `ma_point_anomaly_single_beginning_212.csv` | `stationary + mean_shift + point_anomaly` | ✓ FULL |
| `beginning` | `ma_point_anomaly_single_beginning_835.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `ma_point_anomaly_single_beginning_437.csv` | `stationary` | ~ PARTIAL |
| `beginning` | `ma_point_anomaly_single_beginning_500.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `ma_point_anomaly_single_beginning_918.csv` | `volatility + point_anomaly + variance_shift` | ~ PARTIAL |
| `end` | `ma_point_anomaly_single_end_467.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `end` | `ma_point_anomaly_single_end_784.csv` | `stationary + collective_anomaly + mean_shift` | ~ PARTIAL |
| `end` | `ma_point_anomaly_single_end_503.csv` | `stationary + collective_anomaly + mean_shift` | ~ PARTIAL |
| `end` | `ma_point_anomaly_single_end_923.csv` | `stationary + collective_anomaly + point_anomaly + variance_shift` | ✓ FULL |
| `end` | `ma_point_anomaly_single_end_980.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `ma_point_anomaly_single_end_454.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `ma_point_anomaly_single_end_410.csv` | `stationary + collective_anomaly` | ~ PARTIAL |
| `end` | `ma_point_anomaly_single_end_997.csv` | `stationary + mean_shift + point_anomaly` | ✓ FULL |
| `end` | `ma_point_anomaly_single_end_270.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `end` | `ma_point_anomaly_single_end_556.csv` | `stationary + variance_shift` | ~ PARTIAL |
| `middle` | `ma_point_anomaly_single_middle_736.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `ma_point_anomaly_single_middle_557.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `ma_point_anomaly_single_middle_437.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `ma_point_anomaly_single_middle_950.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `ma_point_anomaly_single_middle_833.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `ma_point_anomaly_single_middle_577.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `ma_point_anomaly_single_middle_344.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `ma_point_anomaly_single_middle_837.csv` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `middle` | `ma_point_anomaly_single_middle_174.csv` | `stationary + collective_anomaly + mean_shift + point_anomaly` | ✓ FULL |
| `middle` | `ma_point_anomaly_single_middle_769.csv` | `stationary` | ~ PARTIAL |
| `multiple` | `ma_point_anomaly_multiple_49.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `multiple` | `ma_point_anomaly_multiple_170.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ~ PARTIAL |
| `multiple` | `ma_point_anomaly_multiple_495.csv` | `volatility + collective_anomaly + variance_shift` | ✗ NONE |
| `multiple` | `ma_point_anomaly_multiple_653.csv` | `volatility + point_anomaly` | ~ PARTIAL |
| `multiple` | `ma_point_anomaly_multiple_857.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ~ PARTIAL |
| `multiple` | `ma_point_anomaly_multiple_264.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `multiple` | `ma_point_anomaly_multiple_600.csv` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `ma_point_anomaly_multiple_369.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `multiple` | `ma_point_anomaly_multiple_394.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `multiple` | `ma_point_anomaly_multiple_193.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `beginning` | `ma_point_anomaly_single_beginning_171.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `beginning` | `ma_point_anomaly_single_beginning_40.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `beginning` | `ma_point_anomaly_single_beginning_707.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `beginning` | `ma_point_anomaly_single_beginning_370.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `beginning` | `ma_point_anomaly_single_beginning_380.csv` | `volatility + mean_shift` | ✗ NONE |
| `beginning` | `ma_point_anomaly_single_beginning_509.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `beginning` | `ma_point_anomaly_single_beginning_654.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `beginning` | `ma_point_anomaly_single_beginning_76.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `beginning` | `ma_point_anomaly_single_beginning_491.csv` | `volatility + collective_anomaly + mean_shift` | ✗ NONE |
| `beginning` | `ma_point_anomaly_single_beginning_251.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `end` | `ma_point_anomaly_single_end_734.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `end` | `ma_point_anomaly_single_end_507.csv` | `volatility + collective_anomaly + mean_shift` | ✗ NONE |
| `end` | `ma_point_anomaly_single_end_421.csv` | `volatility + collective_anomaly + mean_shift` | ✗ NONE |
| `end` | `ma_point_anomaly_single_end_51.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ~ PARTIAL |
| `end` | `ma_point_anomaly_single_end_137.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `end` | `ma_point_anomaly_single_end_769.csv` | `volatility + collective_anomaly + mean_shift` | ✗ NONE |
| `end` | `ma_point_anomaly_single_end_90.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `end` | `ma_point_anomaly_single_end_939.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `end` | `ma_point_anomaly_single_end_423.csv` | `volatility + collective_anomaly + trend_shift + variance_shift` | ✗ NONE |
| `end` | `ma_point_anomaly_single_end_665.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `middle` | `ma_point_anomaly_single_middle_5.csv` | `stationary + collective_anomaly + point_anomaly + variance_shift` | ✓ FULL |
| `middle` | `ma_point_anomaly_single_middle_351.csv` | `volatility + point_anomaly` | ~ PARTIAL |
| `middle` | `ma_point_anomaly_single_middle_688.csv` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `middle` | `ma_point_anomaly_single_middle_828.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ~ PARTIAL |
| `middle` | `ma_point_anomaly_single_middle_972.csv` | `volatility + collective_anomaly + point_anomaly + trend_shift` | ~ PARTIAL |
| `middle` | `ma_point_anomaly_single_middle_150.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `middle` | `ma_point_anomaly_single_middle_167.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `middle` | `ma_point_anomaly_single_middle_717.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `middle` | `ma_point_anomaly_single_middle_686.csv` | `volatility + point_anomaly + variance_shift` | ~ PARTIAL |
| `middle` | `ma_point_anomaly_single_middle_472.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ~ PARTIAL |
| `multiple` | `white_noise_point_anomaly_multiple_433.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `white_noise_point_anomaly_multiple_571.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `white_noise_point_anomaly_multiple_837.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `white_noise_point_anomaly_multiple_79.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `white_noise_point_anomaly_multiple_724.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `white_noise_point_anomaly_multiple_245.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `white_noise_point_anomaly_multiple_977.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `white_noise_point_anomaly_multiple_126.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `white_noise_point_anomaly_multiple_23.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `white_noise_point_anomaly_multiple_881.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `white_noise_point_anomaly_single_beginning_659.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `white_noise_point_anomaly_single_beginning_723.csv` | `stationary` | ~ PARTIAL |
| `beginning` | `white_noise_point_anomaly_single_beginning_819.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `white_noise_point_anomaly_single_beginning_501.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `white_noise_point_anomaly_single_beginning_13.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `white_noise_point_anomaly_single_beginning_214.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `white_noise_point_anomaly_single_beginning_16.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `white_noise_point_anomaly_single_beginning_315.csv` | `stationary` | ~ PARTIAL |
| `beginning` | `white_noise_point_anomaly_single_beginning_816.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `white_noise_point_anomaly_single_beginning_693.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `white_noise_point_anomaly_single_end_436.csv` | `stationary` | ~ PARTIAL |
| `end` | `white_noise_point_anomaly_single_end_431.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `white_noise_point_anomaly_single_end_451.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `white_noise_point_anomaly_single_end_974.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `white_noise_point_anomaly_single_end_620.csv` | `stationary` | ~ PARTIAL |
| `end` | `white_noise_point_anomaly_single_end_128.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `white_noise_point_anomaly_single_end_656.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `white_noise_point_anomaly_single_end_24.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `white_noise_point_anomaly_single_end_724.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `white_noise_point_anomaly_single_end_512.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `white_noise_point_anomaly_single_middle_973.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `white_noise_point_anomaly_single_middle_44.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `white_noise_point_anomaly_single_middle_440.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `white_noise_point_anomaly_single_middle_507.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `white_noise_point_anomaly_single_middle_801.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `white_noise_point_anomaly_single_middle_169.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `white_noise_point_anomaly_single_middle_627.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `white_noise_point_anomaly_single_middle_224.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `white_noise_point_anomaly_single_middle_587.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `white_noise_point_anomaly_single_middle_436.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `white_noise_point_anomaly_multiple_465.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `white_noise_point_anomaly_multiple_388.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `white_noise_point_anomaly_multiple_698.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `white_noise_point_anomaly_multiple_355.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `white_noise_point_anomaly_multiple_328.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `white_noise_point_anomaly_multiple_984.csv` | `stationary + variance_shift` | ~ PARTIAL |
| `multiple` | `white_noise_point_anomaly_multiple_202.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `white_noise_point_anomaly_multiple_121.csv` | `stationary + mean_shift + point_anomaly` | ✓ FULL |
| `multiple` | `white_noise_point_anomaly_multiple_777.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `white_noise_point_anomaly_multiple_27.csv` | `volatility + point_anomaly` | ~ PARTIAL |
| `beginning` | `white_noise_point_anomaly_single_beginning_559.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `beginning` | `white_noise_point_anomaly_single_beginning_576.csv` | `stationary` | ~ PARTIAL |
| `beginning` | `white_noise_point_anomaly_single_beginning_455.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `white_noise_point_anomaly_single_beginning_940.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `white_noise_point_anomaly_single_beginning_616.csv` | `stationary + mean_shift + point_anomaly` | ✓ FULL |
| `beginning` | `white_noise_point_anomaly_single_beginning_206.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `white_noise_point_anomaly_single_beginning_34.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `white_noise_point_anomaly_single_beginning_812.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `beginning` | `white_noise_point_anomaly_single_beginning_338.csv` | `stationary + point_anomaly` | ✓ FULL |
| `beginning` | `white_noise_point_anomaly_single_beginning_747.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `white_noise_point_anomaly_single_end_509.csv` | `stationary + mean_shift + point_anomaly` | ✓ FULL |
| `end` | `white_noise_point_anomaly_single_end_296.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `white_noise_point_anomaly_single_end_662.csv` | `stationary` | ~ PARTIAL |
| `end` | `white_noise_point_anomaly_single_end_361.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `white_noise_point_anomaly_single_end_738.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `white_noise_point_anomaly_single_end_943.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `white_noise_point_anomaly_single_end_550.csv` | `volatility + point_anomaly` | ~ PARTIAL |
| `end` | `white_noise_point_anomaly_single_end_282.csv` | `stationary + point_anomaly` | ✓ FULL |
| `end` | `white_noise_point_anomaly_single_end_210.csv` | `stationary + mean_shift + point_anomaly` | ✓ FULL |
| `end` | `white_noise_point_anomaly_single_end_222.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `white_noise_point_anomaly_single_middle_885.csv` | `volatility + point_anomaly` | ~ PARTIAL |
| `middle` | `white_noise_point_anomaly_single_middle_166.csv` | `volatility + point_anomaly` | ~ PARTIAL |
| `middle` | `white_noise_point_anomaly_single_middle_514.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `white_noise_point_anomaly_single_middle_257.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `white_noise_point_anomaly_single_middle_927.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `middle` | `white_noise_point_anomaly_single_middle_756.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `white_noise_point_anomaly_single_middle_508.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `white_noise_point_anomaly_single_middle_179.csv` | `stationary + point_anomaly` | ✓ FULL |
| `middle` | `white_noise_point_anomaly_single_middle_845.csv` | `stationary + mean_shift + point_anomaly` | ✓ FULL |
| `middle` | `white_noise_point_anomaly_single_middle_727.csv` | `stationary + point_anomaly` | ✓ FULL |
| `multiple` | `white_noise_point_anomaly_multiple_990.csv` | `volatility + collective_anomaly + variance_shift` | ✗ NONE |
| `multiple` | `white_noise_point_anomaly_multiple_878.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `multiple` | `white_noise_point_anomaly_multiple_393.csv` | `stationary + collective_anomaly + point_anomaly` | ✓ FULL |
| `multiple` | `white_noise_point_anomaly_multiple_713.csv` | `volatility + collective_anomaly + point_anomaly + trend_shift` | ~ PARTIAL |
| `multiple` | `white_noise_point_anomaly_multiple_418.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `multiple` | `white_noise_point_anomaly_multiple_752.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `multiple` | `white_noise_point_anomaly_multiple_158.csv` | `volatility + collective_anomaly + trend_shift` | ✗ NONE |
| `multiple` | `white_noise_point_anomaly_multiple_605.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `multiple` | `white_noise_point_anomaly_multiple_599.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `multiple` | `white_noise_point_anomaly_multiple_366.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `beginning` | `white_noise_point_anomaly_single_beginning_92.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `beginning` | `white_noise_point_anomaly_single_beginning_375.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `beginning` | `white_noise_point_anomaly_single_beginning_883.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `beginning` | `white_noise_point_anomaly_single_beginning_243.csv` | `volatility + collective_anomaly + mean_shift` | ✗ NONE |
| `beginning` | `white_noise_point_anomaly_single_beginning_754.csv` | `volatility + point_anomaly` | ~ PARTIAL |
| `beginning` | `white_noise_point_anomaly_single_beginning_752.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `beginning` | `white_noise_point_anomaly_single_beginning_953.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `beginning` | `white_noise_point_anomaly_single_beginning_744.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `beginning` | `white_noise_point_anomaly_single_beginning_687.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `beginning` | `white_noise_point_anomaly_single_beginning_259.csv` | `volatility + point_anomaly` | ~ PARTIAL |
| `end` | `white_noise_point_anomaly_single_end_83.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `end` | `white_noise_point_anomaly_single_end_431.csv` | `volatility + mean_shift + variance_shift` | ✗ NONE |
| `end` | `white_noise_point_anomaly_single_end_567.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `end` | `white_noise_point_anomaly_single_end_304.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `end` | `white_noise_point_anomaly_single_end_21.csv` | `volatility` | ✗ NONE |
| `end` | `white_noise_point_anomaly_single_end_283.csv` | `volatility + collective_anomaly + point_anomaly + trend_shift` | ~ PARTIAL |
| `end` | `white_noise_point_anomaly_single_end_829.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `end` | `white_noise_point_anomaly_single_end_226.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `end` | `white_noise_point_anomaly_single_end_316.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `end` | `white_noise_point_anomaly_single_end_827.csv` | `volatility + collective_anomaly + variance_shift` | ✗ NONE |
| `middle` | `white_noise_point_anomaly_single_middle_553.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `middle` | `white_noise_point_anomaly_single_middle_121.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ~ PARTIAL |
| `middle` | `white_noise_point_anomaly_single_middle_430.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `middle` | `white_noise_point_anomaly_single_middle_609.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `middle` | `white_noise_point_anomaly_single_middle_626.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `middle` | `white_noise_point_anomaly_single_middle_438.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `middle` | `white_noise_point_anomaly_single_middle_529.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `middle` | `white_noise_point_anomaly_single_middle_839.csv` | `volatility + collective_anomaly + mean_shift` | ✗ NONE |
| `middle` | `white_noise_point_anomaly_single_middle_606.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `middle` | `white_noise_point_anomaly_single_middle_217.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ~ PARTIAL |
---

## Grup 9: trend_shift
**Beklenen:** `stationary + trend_shift`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `multiple` | `ar_trend_shift_662.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ar_trend_shift_913.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ar_trend_shift_178.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ar_trend_shift_159.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ar_trend_shift_383.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ar_trend_shift_465.csv` | `stochastic_trend + trend_shift` | ~ PARTIAL |
| `multiple` | `ar_trend_shift_76.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ar_trend_shift_761.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ar_trend_shift_54.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ar_trend_shift_583.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ar_trend_shift_477.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ar_trend_shift_807.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ar_trend_shift_476.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ar_trend_shift_858.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ar_trend_shift_628.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ar_trend_shift_166.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ar_trend_shift_213.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ar_trend_shift_995.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ar_trend_shift_390.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ar_trend_shift_690.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ar_trend_shift_166.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ar_trend_shift_512.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ar_trend_shift_528.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ar_trend_shift_725.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ar_trend_shift_575.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ar_trend_shift_415.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ar_trend_shift_216.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ar_trend_shift_908.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ar_trend_shift_862.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ar_trend_shift_817.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ar_trend_shift_606.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ar_trend_shift_689.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ar_trend_shift_64.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ar_trend_shift_266.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ar_trend_shift_806.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ar_trend_shift_99.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ar_trend_shift_217.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ar_trend_shift_498.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ar_trend_shift_561.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ar_trend_shift_938.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ar_trend_shift_9.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ar_trend_shift_149.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ar_trend_shift_865.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ar_trend_shift_212.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ar_trend_shift_576.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ar_trend_shift_239.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ar_trend_shift_379.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ar_trend_shift_25.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `multiple` | `ar_trend_shift_247.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ar_trend_shift_396.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ar_trend_shift_960.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ar_trend_shift_752.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ar_trend_shift_305.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ar_trend_shift_417.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ar_trend_shift_972.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `beginning` | `ar_trend_shift_966.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ar_trend_shift_577.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ar_trend_shift_923.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ar_trend_shift_36.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ar_trend_shift_879.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ar_trend_shift_170.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `end` | `ar_trend_shift_329.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ar_trend_shift_28.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ar_trend_shift_684.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ar_trend_shift_980.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `end` | `ar_trend_shift_606.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ar_trend_shift_351.csv` | `stationary + mean_shift + variance_shift` | ~ PARTIAL |
| `end` | `ar_trend_shift_213.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `end` | `ar_trend_shift_675.csv` | `stationary + mean_shift + trend_shift + variance_shift` | ✓ FULL |
| `end` | `ar_trend_shift_378.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ar_trend_shift_665.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `middle` | `ar_trend_shift_590.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ar_trend_shift_184.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ar_trend_shift_561.csv` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `middle` | `ar_trend_shift_69.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ar_trend_shift_253.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ar_trend_shift_644.csv` | `deterministic_trend + trend_shift` | ~ PARTIAL |
| `middle` | `ar_trend_shift_967.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ar_trend_shift_633.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ar_trend_shift_24.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `multiple` | `ar_trend_shift_256.csv` | `stochastic_trend + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `multiple` | `ar_trend_shift_705.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ar_trend_shift_674.csv` | `volatility + collective_anomaly + mean_shift` | ✗ NONE |
| `multiple` | `ar_trend_shift_762.csv` | `stochastic_trend + mean_shift + trend_shift` | ~ PARTIAL |
| `multiple` | `ar_trend_shift_93.csv` | `stochastic_trend + mean_shift + trend_shift` | ~ PARTIAL |
| `multiple` | `ar_trend_shift_656.csv` | `stochastic_trend + mean_shift + trend_shift` | ~ PARTIAL |
| `multiple` | `ar_trend_shift_409.csv` | `stochastic_trend + mean_shift + trend_shift` | ~ PARTIAL |
| `multiple` | `ar_trend_shift_875.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `multiple` | `ar_trend_shift_950.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly + trend_shift` | ~ PARTIAL |
| `multiple` | `ar_trend_shift_618.csv` | `volatility + mean_shift + trend_shift` | ~ PARTIAL |
| `beginning` | `ar_trend_shift_136.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ar_trend_shift_86.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `beginning` | `ar_trend_shift_895.csv` | `stochastic_trend + mean_shift + trend_shift` | ~ PARTIAL |
| `beginning` | `ar_trend_shift_124.csv` | `stochastic_trend + trend_shift` | ~ PARTIAL |
| `beginning` | `ar_trend_shift_173.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `beginning` | `ar_trend_shift_14.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ar_trend_shift_973.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ✗ NONE |
| `beginning` | `ar_trend_shift_69.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ar_trend_shift_809.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `beginning` | `ar_trend_shift_63.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `end` | `ar_trend_shift_342.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `end` | `ar_trend_shift_699.csv` | `stochastic_trend + point_anomaly + trend_shift` | ~ PARTIAL |
| `end` | `ar_trend_shift_292.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `end` | `ar_trend_shift_805.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ar_trend_shift_625.csv` | `stochastic_trend + mean_shift + point_anomaly + trend_shift` | ~ PARTIAL |
| `end` | `ar_trend_shift_482.csv` | `stochastic_trend + trend_shift + variance_shift` | ~ PARTIAL |
| `end` | `ar_trend_shift_668.csv` | `volatility + collective_anomaly + mean_shift` | ✗ NONE |
| `end` | `ar_trend_shift_688.csv` | `volatility + collective_anomaly + mean_shift` | ✗ NONE |
| `end` | `ar_trend_shift_126.csv` | `volatility + collective_anomaly + mean_shift` | ✗ NONE |
| `end` | `ar_trend_shift_557.csv` | `stochastic_trend + point_anomaly + trend_shift` | ~ PARTIAL |
| `middle` | `ar_trend_shift_918.csv` | `stochastic_trend + collective_anomaly + mean_shift + point_anomaly + trend_shift` | ~ PARTIAL |
| `middle` | `ar_trend_shift_677.csv` | `stationary + collective_anomaly + mean_shift` | ~ PARTIAL |
| `middle` | `ar_trend_shift_600.csv` | `stationary + mean_shift + point_anomaly + trend_shift` | ✓ FULL |
| `middle` | `ar_trend_shift_365.csv` | `stochastic_trend + mean_shift + trend_shift` | ~ PARTIAL |
| `middle` | `ar_trend_shift_690.csv` | `stochastic_trend + trend_shift` | ~ PARTIAL |
| `middle` | `ar_trend_shift_980.csv` | `stochastic_trend + mean_shift + point_anomaly + trend_shift` | ~ PARTIAL |
| `middle` | `ar_trend_shift_377.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `middle` | `ar_trend_shift_543.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ✗ NONE |
| `middle` | `ar_trend_shift_323.csv` | `stochastic_trend + mean_shift + trend_shift` | ~ PARTIAL |
| `middle` | `ar_trend_shift_840.csv` | `stochastic_trend + mean_shift + point_anomaly + trend_shift` | ~ PARTIAL |
| `multiple` | `arma_trend_shift_842.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `arma_trend_shift_73.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `arma_trend_shift_472.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `arma_trend_shift_372.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `arma_trend_shift_516.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `arma_trend_shift_165.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `arma_trend_shift_733.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `arma_trend_shift_153.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `arma_trend_shift_243.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `arma_trend_shift_503.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `arma_trend_shift_481.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `arma_trend_shift_544.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `arma_trend_shift_526.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `arma_trend_shift_286.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `arma_trend_shift_411.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `arma_trend_shift_658.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `arma_trend_shift_230.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `arma_trend_shift_387.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `arma_trend_shift_893.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `arma_trend_shift_760.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `arma_trend_shift_392.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `arma_trend_shift_775.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `arma_trend_shift_892.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `arma_trend_shift_416.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `arma_trend_shift_998.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `arma_trend_shift_466.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `arma_trend_shift_218.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `end` | `arma_trend_shift_8.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `arma_trend_shift_44.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `arma_trend_shift_573.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `arma_trend_shift_616.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `arma_trend_shift_196.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `arma_trend_shift_392.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `arma_trend_shift_320.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `arma_trend_shift_528.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `arma_trend_shift_210.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `arma_trend_shift_344.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `arma_trend_shift_512.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `arma_trend_shift_326.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `arma_trend_shift_228.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `arma_trend_shift_188.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `arma_trend_shift_144.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `arma_trend_shift_366.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `arma_trend_shift_970.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `multiple` | `arma_trend_shift_452.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `arma_trend_shift_895.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `arma_trend_shift_666.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `arma_trend_shift_484.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `arma_trend_shift_327.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `arma_trend_shift_986.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `arma_trend_shift_897.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `arma_trend_shift_93.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `arma_trend_shift_245.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `arma_trend_shift_849.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `arma_trend_shift_40.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `arma_trend_shift_96.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `arma_trend_shift_630.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `arma_trend_shift_763.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `arma_trend_shift_387.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `arma_trend_shift_273.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `arma_trend_shift_801.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `end` | `arma_trend_shift_245.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `arma_trend_shift_558.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `arma_trend_shift_573.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `arma_trend_shift_529.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `arma_trend_shift_909.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `arma_trend_shift_382.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `arma_trend_shift_557.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `arma_trend_shift_119.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `arma_trend_shift_181.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `arma_trend_shift_97.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `middle` | `arma_trend_shift_460.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `arma_trend_shift_564.csv` | `stationary + mean_shift + variance_shift` | ~ PARTIAL |
| `middle` | `arma_trend_shift_52.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `arma_trend_shift_99.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `arma_trend_shift_32.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `arma_trend_shift_297.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `arma_trend_shift_636.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `arma_trend_shift_423.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `arma_trend_shift_142.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `multiple` | `arma_trend_shift_144.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `multiple` | `arma_trend_shift_358.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `multiple` | `arma_trend_shift_554.csv` | `stochastic_trend + point_anomaly + variance_shift` | ✗ NONE |
| `multiple` | `arma_trend_shift_649.csv` | `stochastic_trend + mean_shift + trend_shift` | ~ PARTIAL |
| `multiple` | `arma_trend_shift_911.csv` | `stochastic_trend + trend_shift` | ~ PARTIAL |
| `multiple` | `arma_trend_shift_876.csv` | `volatility + mean_shift + trend_shift` | ~ PARTIAL |
| `multiple` | `arma_trend_shift_700.csv` | `volatility + collective_anomaly + mean_shift` | ✗ NONE |
| `multiple` | `arma_trend_shift_718.csv` | `stochastic_trend + point_anomaly + trend_shift` | ~ PARTIAL |
| `multiple` | `arma_trend_shift_531.csv` | `stochastic_trend + collective_anomaly + point_anomaly` | ✗ NONE |
| `multiple` | `arma_trend_shift_361.csv` | `stochastic_trend + mean_shift + trend_shift` | ~ PARTIAL |
| `beginning` | `arma_trend_shift_593.csv` | `stochastic_trend + mean_shift + trend_shift` | ~ PARTIAL |
| `beginning` | `arma_trend_shift_105.csv` | `stochastic_trend + mean_shift + trend_shift` | ~ PARTIAL |
| `beginning` | `arma_trend_shift_88.csv` | `stationary + mean_shift + trend_shift + variance_shift` | ✓ FULL |
| `beginning` | `arma_trend_shift_198.csv` | `stochastic_trend + point_anomaly + trend_shift` | ~ PARTIAL |
| `beginning` | `arma_trend_shift_496.csv` | `volatility + collective_anomaly + mean_shift` | ✗ NONE |
| `beginning` | `arma_trend_shift_221.csv` | `stochastic_trend + mean_shift + trend_shift` | ~ PARTIAL |
| `beginning` | `arma_trend_shift_911.csv` | `stochastic_trend + mean_shift + trend_shift` | ~ PARTIAL |
| `beginning` | `arma_trend_shift_341.csv` | `stochastic_trend + mean_shift + trend_shift` | ~ PARTIAL |
| `beginning` | `arma_trend_shift_769.csv` | `stochastic_trend + mean_shift + trend_shift` | ~ PARTIAL |
| `beginning` | `arma_trend_shift_435.csv` | `stochastic_trend + point_anomaly + trend_shift` | ~ PARTIAL |
| `end` | `arma_trend_shift_802.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `end` | `arma_trend_shift_47.csv` | `volatility + variance_shift` | ✗ NONE |
| `end` | `arma_trend_shift_435.csv` | `stochastic_trend + collective_anomaly` | ✗ NONE |
| `end` | `arma_trend_shift_14.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `end` | `arma_trend_shift_468.csv` | `stochastic_trend + mean_shift + trend_shift` | ~ PARTIAL |
| `end` | `arma_trend_shift_145.csv` | `volatility + mean_shift` | ✗ NONE |
| `end` | `arma_trend_shift_623.csv` | `stationary + collective_anomaly + mean_shift + point_anomaly + trend_shift` | ✓ FULL |
| `end` | `arma_trend_shift_616.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `end` | `arma_trend_shift_278.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `end` | `arma_trend_shift_432.csv` | `volatility + mean_shift + trend_shift` | ~ PARTIAL |
| `middle` | `arma_trend_shift_608.csv` | `volatility + collective_anomaly + trend_shift` | ~ PARTIAL |
| `middle` | `arma_trend_shift_364.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `middle` | `arma_trend_shift_166.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `middle` | `arma_trend_shift_454.csv` | `stochastic_trend + mean_shift + trend_shift` | ~ PARTIAL |
| `middle` | `arma_trend_shift_563.csv` | `stochastic_trend + point_anomaly + trend_shift` | ~ PARTIAL |
| `middle` | `arma_trend_shift_513.csv` | `volatility + mean_shift + trend_shift` | ~ PARTIAL |
| `middle` | `arma_trend_shift_802.csv` | `stationary + point_anomaly + trend_shift` | ✓ FULL |
| `middle` | `arma_trend_shift_605.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `middle` | `arma_trend_shift_356.csv` | `volatility + mean_shift + trend_shift` | ~ PARTIAL |
| `middle` | `arma_trend_shift_86.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `multiple` | `ma_trend_shift_673.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ma_trend_shift_725.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ma_trend_shift_661.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ma_trend_shift_207.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ma_trend_shift_216.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ma_trend_shift_998.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ma_trend_shift_188.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ma_trend_shift_461.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ma_trend_shift_442.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ma_trend_shift_830.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ma_trend_shift_410.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ma_trend_shift_612.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ma_trend_shift_964.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ma_trend_shift_435.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ma_trend_shift_795.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ma_trend_shift_230.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ma_trend_shift_281.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ma_trend_shift_653.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ma_trend_shift_568.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ma_trend_shift_469.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ma_trend_shift_56.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ma_trend_shift_135.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ma_trend_shift_14.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ma_trend_shift_133.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ma_trend_shift_224.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ma_trend_shift_756.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ma_trend_shift_405.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ma_trend_shift_84.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ma_trend_shift_535.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ma_trend_shift_577.csv` | `deterministic_trend` | ✗ NONE |
| `middle` | `ma_trend_shift_519.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ma_trend_shift_235.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ma_trend_shift_657.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ma_trend_shift_921.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ma_trend_shift_573.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ma_trend_shift_227.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ma_trend_shift_40.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ma_trend_shift_957.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ma_trend_shift_663.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ma_trend_shift_392.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ma_trend_shift_248.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ma_trend_shift_460.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ma_trend_shift_667.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ma_trend_shift_780.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ma_trend_shift_875.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ma_trend_shift_374.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ma_trend_shift_645.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ma_trend_shift_408.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ma_trend_shift_566.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ma_trend_shift_862.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `beginning` | `ma_trend_shift_568.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ma_trend_shift_59.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ma_trend_shift_55.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ma_trend_shift_751.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ma_trend_shift_617.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ma_trend_shift_374.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ma_trend_shift_536.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ma_trend_shift_850.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `beginning` | `ma_trend_shift_113.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `ma_trend_shift_438.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ma_trend_shift_403.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ma_trend_shift_719.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ma_trend_shift_2.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ma_trend_shift_482.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ma_trend_shift_636.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ma_trend_shift_382.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `end` | `ma_trend_shift_832.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `end` | `ma_trend_shift_927.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ma_trend_shift_767.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ma_trend_shift_902.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ma_trend_shift_732.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ma_trend_shift_679.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ma_trend_shift_122.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `middle` | `ma_trend_shift_649.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ma_trend_shift_535.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ma_trend_shift_342.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `middle` | `ma_trend_shift_990.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `middle` | `ma_trend_shift_702.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ma_trend_shift_82.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ma_trend_shift_995.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `ma_trend_shift_813.csv` | `stationary + collective_anomaly + mean_shift + trend_shift` | ✓ FULL |
| `multiple` | `ma_trend_shift_631.csv` | `stochastic_trend + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `multiple` | `ma_trend_shift_630.csv` | `stationary + mean_shift + trend_shift + variance_shift` | ✓ FULL |
| `multiple` | `ma_trend_shift_308.csv` | `volatility + collective_anomaly + trend_shift` | ~ PARTIAL |
| `multiple` | `ma_trend_shift_763.csv` | `stochastic_trend + mean_shift + trend_shift` | ~ PARTIAL |
| `multiple` | `ma_trend_shift_145.csv` | `stochastic_trend + mean_shift + trend_shift` | ~ PARTIAL |
| `multiple` | `ma_trend_shift_636.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `multiple` | `ma_trend_shift_540.csv` | `volatility + collective_anomaly + mean_shift` | ✗ NONE |
| `multiple` | `ma_trend_shift_255.csv` | `stochastic_trend + mean_shift + trend_shift` | ~ PARTIAL |
| `multiple` | `ma_trend_shift_581.csv` | `volatility + collective_anomaly + trend_shift` | ~ PARTIAL |
| `beginning` | `ma_trend_shift_679.csv` | `stochastic_trend + point_anomaly + trend_shift` | ~ PARTIAL |
| `beginning` | `ma_trend_shift_763.csv` | `stochastic_trend + mean_shift + trend_shift` | ~ PARTIAL |
| `beginning` | `ma_trend_shift_67.csv` | `stochastic_trend + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `beginning` | `ma_trend_shift_812.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `beginning` | `ma_trend_shift_874.csv` | `stationary + trend_shift + variance_shift` | ✓ FULL |
| `beginning` | `ma_trend_shift_449.csv` | `stochastic_trend + point_anomaly + trend_shift` | ~ PARTIAL |
| `beginning` | `ma_trend_shift_234.csv` | `volatility + mean_shift + trend_shift` | ~ PARTIAL |
| `beginning` | `ma_trend_shift_856.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `beginning` | `ma_trend_shift_726.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `beginning` | `ma_trend_shift_321.csv` | `stochastic_trend + mean_shift + trend_shift` | ~ PARTIAL |
| `end` | `ma_trend_shift_127.csv` | `stochastic_trend + mean_shift + trend_shift` | ~ PARTIAL |
| `end` | `ma_trend_shift_626.csv` | `stochastic_trend + mean_shift + trend_shift` | ~ PARTIAL |
| `end` | `ma_trend_shift_972.csv` | `stationary + point_anomaly + trend_shift` | ✓ FULL |
| `end` | `ma_trend_shift_744.csv` | `stochastic_trend + trend_shift` | ~ PARTIAL |
| `end` | `ma_trend_shift_2.csv` | `stationary + collective_anomaly + mean_shift + trend_shift` | ✓ FULL |
| `end` | `ma_trend_shift_274.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `end` | `ma_trend_shift_115.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `end` | `ma_trend_shift_504.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `ma_trend_shift_388.csv` | `volatility + mean_shift + trend_shift` | ~ PARTIAL |
| `end` | `ma_trend_shift_484.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `middle` | `ma_trend_shift_238.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly + trend_shift` | ~ PARTIAL |
| `middle` | `ma_trend_shift_479.csv` | `stationary + point_anomaly + trend_shift` | ✓ FULL |
| `middle` | `ma_trend_shift_735.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `middle` | `ma_trend_shift_286.csv` | `volatility + collective_anomaly + point_anomaly + trend_shift` | ~ PARTIAL |
| `middle` | `ma_trend_shift_477.csv` | `volatility + collective_anomaly + mean_shift` | ✗ NONE |
| `middle` | `ma_trend_shift_560.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `middle` | `ma_trend_shift_812.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `middle` | `ma_trend_shift_662.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `ma_trend_shift_947.csv` | `stochastic_trend + point_anomaly + trend_shift` | ~ PARTIAL |
| `middle` | `ma_trend_shift_532.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly + trend_shift` | ~ PARTIAL |
| `multiple` | `white_noise_trend_shift_902.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `white_noise_trend_shift_880.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `white_noise_trend_shift_777.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `white_noise_trend_shift_769.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `multiple` | `white_noise_trend_shift_155.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `white_noise_trend_shift_749.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `white_noise_trend_shift_225.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `white_noise_trend_shift_577.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `white_noise_trend_shift_29.csv` | `stationary + trend_shift + variance_shift` | ✓ FULL |
| `multiple` | `white_noise_trend_shift_615.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `white_noise_trend_shift_398.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `white_noise_trend_shift_709.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `white_noise_trend_shift_539.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `white_noise_trend_shift_583.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `white_noise_trend_shift_445.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `white_noise_trend_shift_388.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `white_noise_trend_shift_980.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `white_noise_trend_shift_258.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `white_noise_trend_shift_521.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `white_noise_trend_shift_94.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `white_noise_trend_shift_59.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `white_noise_trend_shift_413.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `white_noise_trend_shift_601.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `white_noise_trend_shift_424.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `white_noise_trend_shift_721.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `white_noise_trend_shift_81.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `white_noise_trend_shift_899.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `white_noise_trend_shift_763.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `white_noise_trend_shift_726.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `white_noise_trend_shift_691.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `white_noise_trend_shift_839.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `white_noise_trend_shift_737.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `white_noise_trend_shift_341.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `white_noise_trend_shift_660.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `white_noise_trend_shift_544.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `white_noise_trend_shift_275.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `white_noise_trend_shift_981.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `white_noise_trend_shift_325.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `white_noise_trend_shift_355.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `middle` | `white_noise_trend_shift_612.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `white_noise_trend_shift_373.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `white_noise_trend_shift_305.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `white_noise_trend_shift_967.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `white_noise_trend_shift_996.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `white_noise_trend_shift_372.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `white_noise_trend_shift_809.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `white_noise_trend_shift_364.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `white_noise_trend_shift_748.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `white_noise_trend_shift_29.csv` | `stationary + trend_shift` | ✓ FULL |
| `multiple` | `white_noise_trend_shift_734.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `white_noise_trend_shift_748.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `white_noise_trend_shift_549.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `white_noise_trend_shift_390.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `white_noise_trend_shift_540.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `white_noise_trend_shift_42.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `white_noise_trend_shift_614.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `white_noise_trend_shift_96.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `white_noise_trend_shift_831.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `white_noise_trend_shift_763.csv` | `stationary + trend_shift` | ✓ FULL |
| `beginning` | `white_noise_trend_shift_350.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `white_noise_trend_shift_363.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `white_noise_trend_shift_21.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `white_noise_trend_shift_627.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `white_noise_trend_shift_721.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `white_noise_trend_shift_6.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `white_noise_trend_shift_448.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `white_noise_trend_shift_924.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `white_noise_trend_shift_462.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `white_noise_trend_shift_853.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `white_noise_trend_shift_416.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `white_noise_trend_shift_979.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `white_noise_trend_shift_810.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `middle` | `white_noise_trend_shift_84.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `white_noise_trend_shift_232.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `white_noise_trend_shift_366.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `white_noise_trend_shift_137.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `white_noise_trend_shift_363.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `white_noise_trend_shift_98.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `middle` | `white_noise_trend_shift_757.csv` | `stationary + trend_shift` | ✓ FULL |
| `middle` | `white_noise_trend_shift_170.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `multiple` | `white_noise_trend_shift_417.csv` | `stationary + mean_shift + point_anomaly + trend_shift` | ✓ FULL |
| `multiple` | `white_noise_trend_shift_950.csv` | `stochastic_trend + trend_shift` | ~ PARTIAL |
| `multiple` | `white_noise_trend_shift_505.csv` | `stochastic_trend + mean_shift + trend_shift` | ~ PARTIAL |
| `multiple` | `white_noise_trend_shift_702.csv` | `stochastic_trend + collective_anomaly + trend_shift + variance_shift` | ~ PARTIAL |
| `multiple` | `white_noise_trend_shift_334.csv` | `stationary + collective_anomaly + mean_shift + trend_shift` | ✓ FULL |
| `multiple` | `white_noise_trend_shift_788.csv` | `volatility + collective_anomaly + mean_shift + trend_shift + variance_shift` | ~ PARTIAL |
| `multiple` | `white_noise_trend_shift_54.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly + trend_shift` | ~ PARTIAL |
| `multiple` | `white_noise_trend_shift_296.csv` | `volatility + collective_anomaly + trend_shift` | ~ PARTIAL |
| `multiple` | `white_noise_trend_shift_284.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `multiple` | `white_noise_trend_shift_861.csv` | `stochastic_trend + mean_shift + point_anomaly + trend_shift` | ~ PARTIAL |
| `beginning` | `white_noise_trend_shift_595.csv` | `stationary + mean_shift + point_anomaly + trend_shift` | ✓ FULL |
| `beginning` | `white_noise_trend_shift_348.csv` | `volatility + mean_shift + trend_shift` | ~ PARTIAL |
| `beginning` | `white_noise_trend_shift_959.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `beginning` | `white_noise_trend_shift_616.csv` | `volatility + collective_anomaly + mean_shift` | ✗ NONE |
| `beginning` | `white_noise_trend_shift_74.csv` | `stochastic_trend + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `beginning` | `white_noise_trend_shift_349.csv` | `stochastic_trend + mean_shift + trend_shift` | ~ PARTIAL |
| `beginning` | `white_noise_trend_shift_224.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `beginning` | `white_noise_trend_shift_199.csv` | `stochastic_trend + point_anomaly + trend_shift` | ~ PARTIAL |
| `beginning` | `white_noise_trend_shift_666.csv` | `stationary + trend_shift + variance_shift` | ✓ FULL |
| `beginning` | `white_noise_trend_shift_781.csv` | `stochastic_trend + mean_shift + trend_shift` | ~ PARTIAL |
| `end` | `white_noise_trend_shift_639.csv` | `stochastic_trend + trend_shift` | ~ PARTIAL |
| `end` | `white_noise_trend_shift_319.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `end` | `white_noise_trend_shift_321.csv` | `stationary + mean_shift + trend_shift` | ✓ FULL |
| `end` | `white_noise_trend_shift_144.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `white_noise_trend_shift_715.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `end` | `white_noise_trend_shift_932.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `end` | `white_noise_trend_shift_588.csv` | `volatility + mean_shift + point_anomaly + trend_shift` | ~ PARTIAL |
| `end` | `white_noise_trend_shift_306.csv` | `stationary + trend_shift` | ✓ FULL |
| `end` | `white_noise_trend_shift_687.csv` | `volatility + collective_anomaly + mean_shift` | ✗ NONE |
| `end` | `white_noise_trend_shift_312.csv` | `volatility + mean_shift + trend_shift` | ~ PARTIAL |
| `middle` | `white_noise_trend_shift_146.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ✗ NONE |
| `middle` | `white_noise_trend_shift_190.csv` | `stochastic_trend + mean_shift + trend_shift` | ~ PARTIAL |
| `middle` | `white_noise_trend_shift_48.csv` | `volatility + mean_shift` | ✗ NONE |
| `middle` | `white_noise_trend_shift_402.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ~ PARTIAL |
| `middle` | `white_noise_trend_shift_76.csv` | `stationary + point_anomaly + trend_shift` | ✓ FULL |
| `middle` | `white_noise_trend_shift_533.csv` | `volatility + mean_shift + trend_shift` | ~ PARTIAL |
| `middle` | `white_noise_trend_shift_726.csv` | `stationary + point_anomaly + trend_shift` | ✓ FULL |
| `middle` | `white_noise_trend_shift_809.csv` | `stochastic_trend + point_anomaly + trend_shift` | ~ PARTIAL |
| `middle` | `white_noise_trend_shift_224.csv` | `volatility + collective_anomaly + point_anomaly + trend_shift` | ~ PARTIAL |
| `middle` | `white_noise_trend_shift_102.csv` | `stochastic_trend + mean_shift + point_anomaly + trend_shift` | ~ PARTIAL |
---

## Grup 10: variance_shift
**Beklenen:** `stationary + variance_shift`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `multiple` | `ar_variance_shift_988.csv` | `stationary + point_anomaly` | ~ PARTIAL |
| `multiple` | `ar_variance_shift_605.csv` | `stationary` | ~ PARTIAL |
| `multiple` | `ar_variance_shift_955.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `ar_variance_shift_243.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `ar_variance_shift_473.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `ar_variance_shift_70.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `ar_variance_shift_960.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `ar_variance_shift_91.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `ar_variance_shift_908.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `ar_variance_shift_537.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `ar_variance_shift_538.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `ar_variance_shift_699.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `ar_variance_shift_282.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `ar_variance_shift_796.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `ar_variance_shift_988.csv` | `stationary` | ~ PARTIAL |
| `beginning` | `ar_variance_shift_363.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `ar_variance_shift_394.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `ar_variance_shift_361.csv` | `stationary + point_anomaly` | ~ PARTIAL |
| `beginning` | `ar_variance_shift_694.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `ar_variance_shift_152.csv` | `stationary + variance_shift` | ✓ FULL |
| `end` | `ar_variance_shift_935.csv` | `stationary + variance_shift` | ✓ FULL |
| `end` | `ar_variance_shift_807.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `end` | `ar_variance_shift_180.csv` | `stationary + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `end` | `ar_variance_shift_7.csv` | `stationary + point_anomaly` | ~ PARTIAL |
| `end` | `ar_variance_shift_627.csv` | `stationary + variance_shift` | ✓ FULL |
| `end` | `ar_variance_shift_311.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `end` | `ar_variance_shift_591.csv` | `stationary` | ~ PARTIAL |
| `end` | `ar_variance_shift_78.csv` | `stationary + variance_shift` | ✓ FULL |
| `end` | `ar_variance_shift_765.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `end` | `ar_variance_shift_882.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `ar_variance_shift_962.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `ar_variance_shift_132.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `ar_variance_shift_940.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `ar_variance_shift_948.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `ar_variance_shift_26.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `ar_variance_shift_483.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `ar_variance_shift_911.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `middle` | `ar_variance_shift_870.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `ar_variance_shift_260.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `ar_variance_shift_96.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `ar_variance_shift_946.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `multiple` | `ar_variance_shift_131.csv` | `stationary + collective_anomaly + point_anomaly + variance_shift` | ✓ FULL |
| `multiple` | `ar_variance_shift_87.csv` | `stationary + mean_shift + variance_shift` | ✓ FULL |
| `multiple` | `ar_variance_shift_464.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `ar_variance_shift_824.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `multiple` | `ar_variance_shift_555.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `ar_variance_shift_27.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `multiple` | `ar_variance_shift_962.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `ar_variance_shift_789.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `ar_variance_shift_986.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `ar_variance_shift_902.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `ar_variance_shift_952.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `beginning` | `ar_variance_shift_365.csv` | `stationary + collective_anomaly + variance_shift` | ✓ FULL |
| `beginning` | `ar_variance_shift_906.csv` | `stationary + mean_shift + variance_shift` | ✓ FULL |
| `beginning` | `ar_variance_shift_132.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `ar_variance_shift_106.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `beginning` | `ar_variance_shift_373.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `beginning` | `ar_variance_shift_621.csv` | `stationary + collective_anomaly + point_anomaly + variance_shift` | ✓ FULL |
| `beginning` | `ar_variance_shift_654.csv` | `stationary + mean_shift + variance_shift` | ✓ FULL |
| `beginning` | `ar_variance_shift_197.csv` | `stationary + variance_shift` | ✓ FULL |
| `end` | `ar_variance_shift_954.csv` | `stationary` | ~ PARTIAL |
| `end` | `ar_variance_shift_407.csv` | `stationary + mean_shift + point_anomaly + variance_shift` | ✓ FULL |
| `end` | `ar_variance_shift_360.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `end` | `ar_variance_shift_517.csv` | `stationary + mean_shift` | ~ PARTIAL |
| `end` | `ar_variance_shift_69.csv` | `stationary + mean_shift + variance_shift` | ✓ FULL |
| `end` | `ar_variance_shift_6.csv` | `stationary + collective_anomaly + variance_shift` | ✓ FULL |
| `end` | `ar_variance_shift_581.csv` | `stationary + variance_shift` | ✓ FULL |
| `end` | `ar_variance_shift_553.csv` | `stationary + variance_shift` | ✓ FULL |
| `end` | `ar_variance_shift_918.csv` | `volatility + mean_shift + variance_shift` | ~ PARTIAL |
| `end` | `ar_variance_shift_964.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `middle` | `ar_variance_shift_221.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `middle` | `ar_variance_shift_883.csv` | `stochastic_trend + variance_shift` | ~ PARTIAL |
| `middle` | `ar_variance_shift_563.csv` | `stationary + mean_shift + variance_shift` | ✓ FULL |
| `middle` | `ar_variance_shift_53.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `ar_variance_shift_35.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `ar_variance_shift_276.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `ar_variance_shift_844.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `ar_variance_shift_201.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `middle` | `ar_variance_shift_402.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `ar_variance_shift_248.csv` | `stationary + collective_anomaly + variance_shift` | ✓ FULL |
| `multiple` | `ar_variance_shift_772.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `multiple` | `ar_variance_shift_520.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `multiple` | `ar_variance_shift_696.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `multiple` | `ar_variance_shift_335.csv` | `stochastic_trend + collective_anomaly + point_anomaly` | ✗ NONE |
| `multiple` | `ar_variance_shift_760.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `multiple` | `ar_variance_shift_27.csv` | `volatility + collective_anomaly + mean_shift` | ✗ NONE |
| `multiple` | `ar_variance_shift_110.csv` | `stochastic_trend + point_anomaly` | ✗ NONE |
| `multiple` | `ar_variance_shift_778.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `multiple` | `ar_variance_shift_409.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `multiple` | `ar_variance_shift_827.csv` | `volatility + mean_shift + point_anomaly` | ✗ NONE |
| `beginning` | `ar_variance_shift_370.csv` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
| `beginning` | `ar_variance_shift_621.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `beginning` | `ar_variance_shift_72.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `ar_variance_shift_797.csv` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
| `beginning` | `ar_variance_shift_276.csv` | `volatility + point_anomaly + variance_shift` | ~ PARTIAL |
| `beginning` | `ar_variance_shift_26.csv` | `stationary + collective_anomaly + mean_shift + point_anomaly` | ~ PARTIAL |
| `beginning` | `ar_variance_shift_661.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `beginning` | `ar_variance_shift_888.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `beginning` | `ar_variance_shift_688.csv` | `volatility + mean_shift + point_anomaly + variance_shift` | ~ PARTIAL |
| `beginning` | `ar_variance_shift_925.csv` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
| `end` | `ar_variance_shift_472.csv` | `stationary + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `end` | `ar_variance_shift_860.csv` | `stochastic_trend + mean_shift + trend_shift` | ✗ NONE |
| `end` | `ar_variance_shift_492.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `end` | `ar_variance_shift_573.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ✗ NONE |
| `end` | `ar_variance_shift_40.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `end` | `ar_variance_shift_178.csv` | `volatility + collective_anomaly + mean_shift` | ✗ NONE |
| `end` | `ar_variance_shift_468.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `end` | `ar_variance_shift_715.csv` | `stationary + collective_anomaly + mean_shift` | ~ PARTIAL |
| `end` | `ar_variance_shift_186.csv` | `stationary + variance_shift` | ✓ FULL |
| `end` | `ar_variance_shift_269.csv` | `stationary + collective_anomaly + point_anomaly + variance_shift` | ✓ FULL |
| `middle` | `ar_variance_shift_227.csv` | `volatility + point_anomaly + variance_shift` | ~ PARTIAL |
| `middle` | `ar_variance_shift_538.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `middle` | `ar_variance_shift_397.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `middle` | `ar_variance_shift_961.csv` | `volatility + point_anomaly + variance_shift` | ~ PARTIAL |
| `middle` | `ar_variance_shift_327.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `middle` | `ar_variance_shift_103.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `middle` | `ar_variance_shift_339.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ✗ NONE |
| `middle` | `ar_variance_shift_451.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly + variance_shift` | ~ PARTIAL |
| `middle` | `ar_variance_shift_315.csv` | `volatility + collective_anomaly + point_anomaly + trend_shift + variance_shift` | ~ PARTIAL |
| `middle` | `ar_variance_shift_51.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `multiple` | `arma_variance_shift_793.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `arma_variance_shift_344.csv` | `stationary` | ~ PARTIAL |
| `multiple` | `arma_variance_shift_978.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `arma_variance_shift_401.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `arma_variance_shift_377.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `arma_variance_shift_635.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `arma_variance_shift_765.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `arma_variance_shift_626.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `arma_variance_shift_108.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `arma_variance_shift_339.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `arma_variance_shift_700.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `arma_variance_shift_43.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `arma_variance_shift_737.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `arma_variance_shift_315.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `beginning` | `arma_variance_shift_155.csv` | `stationary + collective_anomaly + variance_shift` | ✓ FULL |
| `beginning` | `arma_variance_shift_713.csv` | `stationary + collective_anomaly + variance_shift` | ✓ FULL |
| `beginning` | `arma_variance_shift_207.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `beginning` | `arma_variance_shift_527.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `arma_variance_shift_381.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `arma_variance_shift_245.csv` | `stationary + variance_shift` | ✓ FULL |
| `end` | `arma_variance_shift_472.csv` | `stationary + variance_shift` | ✓ FULL |
| `end` | `arma_variance_shift_730.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `end` | `arma_variance_shift_561.csv` | `stationary + variance_shift` | ✓ FULL |
| `end` | `arma_variance_shift_95.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `end` | `arma_variance_shift_923.csv` | `stationary + variance_shift` | ✓ FULL |
| `end` | `arma_variance_shift_917.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `end` | `arma_variance_shift_747.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `end` | `arma_variance_shift_808.csv` | `stationary + variance_shift` | ✓ FULL |
| `end` | `arma_variance_shift_385.csv` | `stationary + variance_shift` | ✓ FULL |
| `end` | `arma_variance_shift_734.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `arma_variance_shift_206.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `arma_variance_shift_688.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `arma_variance_shift_943.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `arma_variance_shift_966.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `arma_variance_shift_370.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `arma_variance_shift_437.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `arma_variance_shift_665.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `arma_variance_shift_301.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `arma_variance_shift_30.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `arma_variance_shift_981.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `arma_variance_shift_220.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `multiple` | `arma_variance_shift_539.csv` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
| `multiple` | `arma_variance_shift_239.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `arma_variance_shift_517.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `arma_variance_shift_788.csv` | `stationary + mean_shift + variance_shift` | ✓ FULL |
| `multiple` | `arma_variance_shift_657.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `arma_variance_shift_442.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `arma_variance_shift_481.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `arma_variance_shift_745.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `multiple` | `arma_variance_shift_604.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `arma_variance_shift_94.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `arma_variance_shift_532.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `beginning` | `arma_variance_shift_797.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `beginning` | `arma_variance_shift_594.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `beginning` | `arma_variance_shift_838.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `arma_variance_shift_710.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `arma_variance_shift_86.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `arma_variance_shift_3.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `arma_variance_shift_800.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `arma_variance_shift_326.csv` | `stationary + variance_shift` | ✓ FULL |
| `end` | `arma_variance_shift_725.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `end` | `arma_variance_shift_794.csv` | `stationary + collective_anomaly + point_anomaly + variance_shift` | ✓ FULL |
| `end` | `arma_variance_shift_648.csv` | `stationary + mean_shift + variance_shift` | ✓ FULL |
| `end` | `arma_variance_shift_903.csv` | `stationary + mean_shift + variance_shift` | ✓ FULL |
| `end` | `arma_variance_shift_824.csv` | `volatility + point_anomaly + variance_shift` | ~ PARTIAL |
| `end` | `arma_variance_shift_173.csv` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
| `end` | `arma_variance_shift_583.csv` | `stationary + variance_shift` | ✓ FULL |
| `end` | `arma_variance_shift_51.csv` | `stationary + variance_shift` | ✓ FULL |
| `end` | `arma_variance_shift_585.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `end` | `arma_variance_shift_747.csv` | `stationary + collective_anomaly + point_anomaly + variance_shift` | ✓ FULL |
| `middle` | `arma_variance_shift_431.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `arma_variance_shift_17.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `arma_variance_shift_944.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `arma_variance_shift_618.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `arma_variance_shift_200.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `arma_variance_shift_155.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `arma_variance_shift_862.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `middle` | `arma_variance_shift_602.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `arma_variance_shift_930.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `middle` | `arma_variance_shift_564.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `arma_variance_shift_285.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `multiple` | `arma_variance_shift_626.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `multiple` | `arma_variance_shift_593.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `multiple` | `arma_variance_shift_236.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `multiple` | `arma_variance_shift_25.csv` | `volatility + mean_shift + point_anomaly` | ✗ NONE |
| `multiple` | `arma_variance_shift_40.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `arma_variance_shift_886.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `multiple` | `arma_variance_shift_578.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ✗ NONE |
| `multiple` | `arma_variance_shift_505.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ✗ NONE |
| `multiple` | `arma_variance_shift_205.csv` | `stochastic_trend + mean_shift` | ✗ NONE |
| `beginning` | `arma_variance_shift_725.csv` | `volatility + point_anomaly + variance_shift` | ~ PARTIAL |
| `beginning` | `arma_variance_shift_288.csv` | `stationary + collective_anomaly` | ~ PARTIAL |
| `beginning` | `arma_variance_shift_76.csv` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
| `beginning` | `arma_variance_shift_636.csv` | `stochastic_trend + collective_anomaly` | ✗ NONE |
| `beginning` | `arma_variance_shift_549.csv` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
| `beginning` | `arma_variance_shift_182.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `beginning` | `arma_variance_shift_927.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `beginning` | `arma_variance_shift_569.csv` | `stationary + collective_anomaly` | ~ PARTIAL |
| `beginning` | `arma_variance_shift_509.csv` | `stochastic_trend + collective_anomaly + mean_shift + point_anomaly` | ✗ NONE |
| `beginning` | `arma_variance_shift_844.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `end` | `arma_variance_shift_149.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `end` | `arma_variance_shift_516.csv` | `stationary + collective_anomaly + variance_shift` | ✓ FULL |
| `end` | `arma_variance_shift_22.csv` | `volatility + mean_shift + variance_shift` | ~ PARTIAL |
| `end` | `arma_variance_shift_571.csv` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
| `end` | `arma_variance_shift_481.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ✗ NONE |
| `end` | `arma_variance_shift_519.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ✗ NONE |
| `end` | `arma_variance_shift_618.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `end` | `arma_variance_shift_151.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `end` | `arma_variance_shift_613.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `end` | `arma_variance_shift_524.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `middle` | `arma_variance_shift_718.csv` | `stochastic_trend + collective_anomaly + point_anomaly` | ✗ NONE |
| `middle` | `arma_variance_shift_842.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `middle` | `arma_variance_shift_382.csv` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
| `middle` | `arma_variance_shift_765.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `arma_variance_shift_118.csv` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
| `middle` | `arma_variance_shift_463.csv` | `stationary + collective_anomaly + variance_shift` | ✓ FULL |
| `middle` | `arma_variance_shift_332.csv` | `volatility + point_anomaly + variance_shift` | ~ PARTIAL |
| `middle` | `arma_variance_shift_851.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `middle` | `arma_variance_shift_1000.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `middle` | `arma_variance_shift_786.csv` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
| `multiple` | `ma_variance_shift_3.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `ma_variance_shift_631.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `ma_variance_shift_165.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `ma_variance_shift_14.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `ma_variance_shift_489.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `ma_variance_shift_415.csv` | `stationary` | ~ PARTIAL |
| `multiple` | `ma_variance_shift_744.csv` | `stationary + collective_anomaly + variance_shift` | ✓ FULL |
| `multiple` | `ma_variance_shift_157.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `ma_variance_shift_598.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `ma_variance_shift_153.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `ma_variance_shift_960.csv` | `stationary + point_anomaly` | ~ PARTIAL |
| `beginning` | `ma_variance_shift_922.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `ma_variance_shift_161.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `ma_variance_shift_96.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `ma_variance_shift_533.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `ma_variance_shift_127.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `ma_variance_shift_362.csv` | `stationary + mean_shift + variance_shift` | ✓ FULL |
| `beginning` | `ma_variance_shift_475.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `ma_variance_shift_264.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `ma_variance_shift_807.csv` | `stationary` | ~ PARTIAL |
| `end` | `ma_variance_shift_222.csv` | `stationary + variance_shift` | ✓ FULL |
| `end` | `ma_variance_shift_804.csv` | `stationary + variance_shift` | ✓ FULL |
| `end` | `ma_variance_shift_69.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `end` | `ma_variance_shift_770.csv` | `stationary + variance_shift` | ✓ FULL |
| `end` | `ma_variance_shift_694.csv` | `stationary + variance_shift` | ✓ FULL |
| `end` | `ma_variance_shift_987.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `end` | `ma_variance_shift_486.csv` | `stationary + variance_shift` | ✓ FULL |
| `end` | `ma_variance_shift_443.csv` | `stationary + variance_shift` | ✓ FULL |
| `end` | `ma_variance_shift_92.csv` | `stationary + point_anomaly` | ~ PARTIAL |
| `end` | `ma_variance_shift_450.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `ma_variance_shift_511.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `ma_variance_shift_90.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `ma_variance_shift_944.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `ma_variance_shift_934.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `ma_variance_shift_446.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `ma_variance_shift_444.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `ma_variance_shift_172.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `ma_variance_shift_728.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `ma_variance_shift_988.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `ma_variance_shift_708.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `ma_variance_shift_904.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `ma_variance_shift_596.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `multiple` | `ma_variance_shift_220.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `ma_variance_shift_700.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `ma_variance_shift_891.csv` | `stationary + mean_shift + variance_shift` | ✓ FULL |
| `multiple` | `ma_variance_shift_419.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `multiple` | `ma_variance_shift_207.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `multiple` | `ma_variance_shift_262.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `ma_variance_shift_594.csv` | `volatility + point_anomaly + variance_shift` | ~ PARTIAL |
| `multiple` | `ma_variance_shift_460.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `beginning` | `ma_variance_shift_586.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `ma_variance_shift_215.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `ma_variance_shift_77.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `ma_variance_shift_303.csv` | `stationary` | ~ PARTIAL |
| `beginning` | `ma_variance_shift_868.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `ma_variance_shift_1000.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `ma_variance_shift_796.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `ma_variance_shift_119.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `ma_variance_shift_373.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `ma_variance_shift_525.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `end` | `ma_variance_shift_719.csv` | `stationary + variance_shift` | ✓ FULL |
| `end` | `ma_variance_shift_761.csv` | `stationary + mean_shift + variance_shift` | ✓ FULL |
| `end` | `ma_variance_shift_60.csv` | `stationary + variance_shift` | ✓ FULL |
| `end` | `ma_variance_shift_49.csv` | `stationary + mean_shift + variance_shift` | ✓ FULL |
| `end` | `ma_variance_shift_589.csv` | `stationary + collective_anomaly + point_anomaly + variance_shift` | ✓ FULL |
| `end` | `ma_variance_shift_448.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `end` | `ma_variance_shift_858.csv` | `stationary + variance_shift` | ✓ FULL |
| `end` | `ma_variance_shift_31.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `end` | `ma_variance_shift_326.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `end` | `ma_variance_shift_522.csv` | `stationary + collective_anomaly + point_anomaly + variance_shift` | ✓ FULL |
| `middle` | `ma_variance_shift_417.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `middle` | `ma_variance_shift_240.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `ma_variance_shift_352.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `middle` | `ma_variance_shift_272.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `middle` | `ma_variance_shift_962.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `middle` | `ma_variance_shift_905.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `middle` | `ma_variance_shift_767.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `middle` | `ma_variance_shift_803.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `middle` | `ma_variance_shift_201.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `middle` | `ma_variance_shift_127.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `ma_variance_shift_844.csv` | `stationary + collective_anomaly` | ~ PARTIAL |
| `multiple` | `ma_variance_shift_707.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `multiple` | `ma_variance_shift_485.csv` | `stochastic_trend + mean_shift + point_anomaly` | ✗ NONE |
| `multiple` | `ma_variance_shift_665.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `multiple` | `ma_variance_shift_804.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `multiple` | `ma_variance_shift_961.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `multiple` | `ma_variance_shift_912.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `multiple` | `ma_variance_shift_918.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `multiple` | `ma_variance_shift_112.csv` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
| `multiple` | `ma_variance_shift_32.csv` | `stochastic_trend + collective_anomaly + variance_shift` | ~ PARTIAL |
| `beginning` | `ma_variance_shift_289.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `beginning` | `ma_variance_shift_16.csv` | `volatility + collective_anomaly + mean_shift` | ✗ NONE |
| `beginning` | `ma_variance_shift_191.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `beginning` | `ma_variance_shift_646.csv` | `volatility + point_anomaly + variance_shift` | ~ PARTIAL |
| `beginning` | `ma_variance_shift_129.csv` | `stationary + collective_anomaly` | ~ PARTIAL |
| `beginning` | `ma_variance_shift_51.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `beginning` | `ma_variance_shift_65.csv` | `stationary + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `beginning` | `ma_variance_shift_718.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `beginning` | `ma_variance_shift_747.csv` | `volatility + point_anomaly + variance_shift` | ~ PARTIAL |
| `beginning` | `ma_variance_shift_902.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `end` | `ma_variance_shift_142.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `end` | `ma_variance_shift_323.csv` | `volatility + point_anomaly + variance_shift` | ~ PARTIAL |
| `end` | `ma_variance_shift_781.csv` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
| `end` | `ma_variance_shift_139.csv` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
| `end` | `ma_variance_shift_469.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `end` | `ma_variance_shift_502.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `end` | `ma_variance_shift_313.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `end` | `ma_variance_shift_596.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `end` | `ma_variance_shift_299.csv` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
| `end` | `ma_variance_shift_794.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `middle` | `ma_variance_shift_895.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `middle` | `ma_variance_shift_813.csv` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
| `middle` | `ma_variance_shift_15.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `middle` | `ma_variance_shift_227.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `middle` | `ma_variance_shift_562.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `middle` | `ma_variance_shift_365.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `middle` | `ma_variance_shift_313.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `middle` | `ma_variance_shift_850.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `middle` | `ma_variance_shift_943.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `middle` | `ma_variance_shift_773.csv` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
| `multiple` | `white_noise_variance_shift_629.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `white_noise_variance_shift_392.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `white_noise_variance_shift_630.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `multiple` | `white_noise_variance_shift_65.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `white_noise_variance_shift_810.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `white_noise_variance_shift_718.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `white_noise_variance_shift_853.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `white_noise_variance_shift_394.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `white_noise_variance_shift_316.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `white_noise_variance_shift_377.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `white_noise_variance_shift_906.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `white_noise_variance_shift_23.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `white_noise_variance_shift_707.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `white_noise_variance_shift_579.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `white_noise_variance_shift_301.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `white_noise_variance_shift_48.csv` | `stationary + point_anomaly` | ~ PARTIAL |
| `beginning` | `white_noise_variance_shift_375.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `white_noise_variance_shift_351.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `white_noise_variance_shift_154.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `beginning` | `white_noise_variance_shift_611.csv` | `stationary + variance_shift` | ✓ FULL |
| `end` | `white_noise_variance_shift_973.csv` | `stationary + variance_shift` | ✓ FULL |
| `end` | `white_noise_variance_shift_643.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `end` | `white_noise_variance_shift_909.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `end` | `white_noise_variance_shift_776.csv` | `stationary + point_anomaly` | ~ PARTIAL |
| `end` | `white_noise_variance_shift_939.csv` | `stationary + variance_shift` | ✓ FULL |
| `end` | `white_noise_variance_shift_26.csv` | `stationary + variance_shift` | ✓ FULL |
| `end` | `white_noise_variance_shift_676.csv` | `stationary + variance_shift` | ✓ FULL |
| `end` | `white_noise_variance_shift_724.csv` | `stationary + variance_shift` | ✓ FULL |
| `end` | `white_noise_variance_shift_492.csv` | `stationary + variance_shift` | ✓ FULL |
| `end` | `white_noise_variance_shift_610.csv` | `stationary + point_anomaly` | ~ PARTIAL |
| `middle` | `white_noise_variance_shift_555.csv` | `stationary + point_anomaly + variance_shift` | ✓ FULL |
| `middle` | `white_noise_variance_shift_141.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `white_noise_variance_shift_995.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `middle` | `white_noise_variance_shift_415.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `white_noise_variance_shift_967.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `white_noise_variance_shift_691.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `white_noise_variance_shift_717.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `white_noise_variance_shift_45.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `white_noise_variance_shift_822.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `white_noise_variance_shift_582.csv` | `stationary + variance_shift` | ✓ FULL |
| `multiple` | `white_noise_variance_shift_392.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `multiple` | `white_noise_variance_shift_740.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `multiple` | `white_noise_variance_shift_482.csv` | `stationary + mean_shift + variance_shift` | ✓ FULL |
| `multiple` | `white_noise_variance_shift_475.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `multiple` | `white_noise_variance_shift_235.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `multiple` | `white_noise_variance_shift_375.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `multiple` | `white_noise_variance_shift_445.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `multiple` | `white_noise_variance_shift_268.csv` | `volatility` | ✗ NONE |
| `multiple` | `white_noise_variance_shift_794.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `multiple` | `white_noise_variance_shift_594.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `white_noise_variance_shift_534.csv` | `stationary + mean_shift + variance_shift` | ✓ FULL |
| `beginning` | `white_noise_variance_shift_32.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `white_noise_variance_shift_881.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `white_noise_variance_shift_305.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `beginning` | `white_noise_variance_shift_375.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `beginning` | `white_noise_variance_shift_89.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `white_noise_variance_shift_750.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `beginning` | `white_noise_variance_shift_230.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `beginning` | `white_noise_variance_shift_841.csv` | `stationary + variance_shift` | ✓ FULL |
| `beginning` | `white_noise_variance_shift_525.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `end` | `white_noise_variance_shift_941.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `end` | `white_noise_variance_shift_151.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `end` | `white_noise_variance_shift_616.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `end` | `white_noise_variance_shift_479.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `end` | `white_noise_variance_shift_991.csv` | `volatility + point_anomaly + variance_shift` | ~ PARTIAL |
| `end` | `white_noise_variance_shift_482.csv` | `volatility + point_anomaly + variance_shift` | ~ PARTIAL |
| `end` | `white_noise_variance_shift_611.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `end` | `white_noise_variance_shift_587.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `end` | `white_noise_variance_shift_221.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `end` | `white_noise_variance_shift_456.csv` | `volatility + point_anomaly + variance_shift` | ~ PARTIAL |
| `middle` | `white_noise_variance_shift_321.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `middle` | `white_noise_variance_shift_333.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `middle` | `white_noise_variance_shift_286.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `middle` | `white_noise_variance_shift_402.csv` | `stationary + variance_shift` | ✓ FULL |
| `middle` | `white_noise_variance_shift_695.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `middle` | `white_noise_variance_shift_170.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `middle` | `white_noise_variance_shift_949.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `middle` | `white_noise_variance_shift_512.csv` | `volatility + mean_shift + variance_shift` | ~ PARTIAL |
| `middle` | `white_noise_variance_shift_88.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `middle` | `white_noise_variance_shift_44.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `multiple` | `white_noise_variance_shift_183.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `multiple` | `white_noise_variance_shift_592.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ✗ NONE |
| `multiple` | `white_noise_variance_shift_766.csv` | `volatility + mean_shift` | ✗ NONE |
| `multiple` | `white_noise_variance_shift_863.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `multiple` | `white_noise_variance_shift_274.csv` | `volatility + collective_anomaly + mean_shift` | ✗ NONE |
| `multiple` | `white_noise_variance_shift_145.csv` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
| `multiple` | `white_noise_variance_shift_345.csv` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
| `multiple` | `white_noise_variance_shift_446.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `multiple` | `white_noise_variance_shift_719.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `multiple` | `white_noise_variance_shift_656.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `beginning` | `white_noise_variance_shift_654.csv` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
| `beginning` | `white_noise_variance_shift_134.csv` | `volatility + collective_anomaly + mean_shift + variance_shift` | ~ PARTIAL |
| `beginning` | `white_noise_variance_shift_903.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `beginning` | `white_noise_variance_shift_165.csv` | `volatility + mean_shift + variance_shift` | ~ PARTIAL |
| `beginning` | `white_noise_variance_shift_271.csv` | `volatility + mean_shift + point_anomaly` | ✗ NONE |
| `beginning` | `white_noise_variance_shift_84.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `beginning` | `white_noise_variance_shift_80.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `beginning` | `white_noise_variance_shift_64.csv` | `volatility + collective_anomaly + mean_shift` | ✗ NONE |
| `beginning` | `white_noise_variance_shift_766.csv` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
| `beginning` | `white_noise_variance_shift_717.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `end` | `white_noise_variance_shift_613.csv` | `volatility + collective_anomaly + mean_shift` | ✗ NONE |
| `end` | `white_noise_variance_shift_299.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `end` | `white_noise_variance_shift_54.csv` | `volatility + point_anomaly + variance_shift` | ~ PARTIAL |
| `end` | `white_noise_variance_shift_290.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `end` | `white_noise_variance_shift_90.csv` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
| `end` | `white_noise_variance_shift_934.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `end` | `white_noise_variance_shift_404.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `end` | `white_noise_variance_shift_378.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `end` | `white_noise_variance_shift_980.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `end` | `white_noise_variance_shift_936.csv` | `volatility + point_anomaly` | ✗ NONE |
| `middle` | `white_noise_variance_shift_111.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `middle` | `white_noise_variance_shift_293.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `middle` | `white_noise_variance_shift_962.csv` | `volatility + mean_shift + point_anomaly` | ✗ NONE |
| `middle` | `white_noise_variance_shift_273.csv` | `volatility + collective_anomaly` | ✗ NONE |
| `middle` | `white_noise_variance_shift_986.csv` | `volatility + collective_anomaly + point_anomaly` | ✗ NONE |
| `middle` | `white_noise_variance_shift_782.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly + trend_shift` | ✗ NONE |
| `middle` | `white_noise_variance_shift_206.csv` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
| `middle` | `white_noise_variance_shift_787.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `middle` | `white_noise_variance_shift_794.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ~ PARTIAL |
| `middle` | `white_noise_variance_shift_54.csv` | `volatility + collective_anomaly + variance_shift` | ~ PARTIAL |
---

## Grup 11: cubic+collective
**Beklenen:** `deterministic_trend + collective_anomaly`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `cubic_collective_white_noise_186.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `cubic_collective_arma_248.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `cubic_collective_ma_212.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `cubic_collective_ma_118.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `cubic_collective_ma_220.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `cubic_collective_arma_209.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `cubic_collective_ar_156.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `cubic_collective_white_noise_187.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `cubic_collective_arma_245.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `cubic_collective_ma_065.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
---

## Grup 12: cubic+mean_shift
**Beklenen:** `deterministic_trend + mean_shift`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `cubic_meanshift1_ar_074.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `cubic_meanshift1_white_noise_038.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `cubic_meanshift1_ar_034.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `cubic_meanshift1_ar_134.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `cubic_meanshift1_ar_222.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `cubic_meanshift1_ma_041.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `cubic_meanshift1_ma_159.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `cubic_meanshift1_ar_112.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `cubic_meanshift1_ar_060.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `cubic_meanshift1_ar_012.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `cubic_meanshift2_ar_118.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `cubic_meanshift2_ma_025.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `cubic_meanshift2_white_noise_153.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `cubic_meanshift2_ma_009.csv` | `deterministic_trend + mean_shift + point_anomaly` | ✓ FULL |
| `data` | `cubic_meanshift2_ar_227.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `cubic_meanshift2_arma_100.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `cubic_meanshift2_white_noise_072.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `cubic_meanshift2_ma_239.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `cubic_meanshift2_ar_230.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `cubic_meanshift2_white_noise_029.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
---

## Grup 13: cubic+point_anomaly
**Beklenen:** `deterministic_trend + point_anomaly`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `cubic_point_white_noise_109.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `cubic_point_ar_077.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `cubic_point_white_noise_186.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `cubic_point_arma_208.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `cubic_point_ar_129.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `cubic_point_ar_070.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `cubic_point_ar_173.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `cubic_point_arma_046.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `cubic_point_ma_076.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `cubic_point_white_noise_134.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
---

## Grup 14: cubic+variance_shift
**Beklenen:** `deterministic_trend + variance_shift`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `cubic_varshift_arma_226.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `cubic_varshift_white_noise_009.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `cubic_varshift_arma_149.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `cubic_varshift_arma_016.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `cubic_varshift_ar_017.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `cubic_varshift_ma_066.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `cubic_varshift_white_noise_207.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `cubic_varshift_ma_098.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `cubic_varshift_ma_093.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `cubic_varshift_ma_237.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
---

## Grup 15: damped+collective
**Beklenen:** `deterministic_trend + collective_anomaly`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `damped_collective_ar_177.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `damped_collective_ar_052.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `damped_collective_arma_156.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `damped_collective_arma_200.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `damped_collective_ar_087.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `damped_collective_arma_235.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `damped_collective_ar_138.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `damped_collective_ma_083.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `damped_collective_white_noise_103.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `damped_collective_ar_001.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
---

## Grup 16: damped+mean_shift
**Beklenen:** `deterministic_trend + mean_shift`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `damped_meanshift1_ma_011.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `damped_meanshift1_ma_063.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `damped_meanshift1_ma_170.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `damped_meanshift1_white_noise_216.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `damped_meanshift1_ma_201.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `damped_meanshift1_ar_095.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `damped_meanshift1_ar_013.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `damped_meanshift1_white_noise_031.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `damped_meanshift1_white_noise_091.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `damped_meanshift1_ma_000.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `damped_meanshift2_white_noise_239.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `damped_meanshift2_ma_240.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `damped_meanshift2_ma_157.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `damped_meanshift2_white_noise_007.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `damped_meanshift2_ma_002.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `damped_meanshift2_ar_221.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `damped_meanshift2_arma_172.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `damped_meanshift2_white_noise_000.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `damped_meanshift2_white_noise_064.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `damped_meanshift2_ar_110.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
---

## Grup 17: damped+point_anomaly
**Beklenen:** `deterministic_trend + point_anomaly`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `damped_point_arma_173.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `damped_point_arma_143.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `damped_point_ma_237.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `damped_point_ma_059.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `damped_point_ma_000.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `damped_point_arma_188.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `damped_point_white_noise_188.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `damped_point_white_noise_160.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `damped_point_ma_055.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `damped_point_ma_157.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
---

## Grup 18: damped+variance_shift
**Beklenen:** `deterministic_trend + variance_shift`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `damped_varshift_white_noise_230.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `damped_varshift_arma_060.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `damped_varshift_ma_036.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `damped_varshift_arma_034.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `damped_varshift_white_noise_109.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `damped_varshift_white_noise_117.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `damped_varshift_arma_076.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `damped_varshift_white_noise_217.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `damped_varshift_white_noise_087.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `damped_varshift_ma_184.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
---

## Grup 19: exp+collective
**Beklenen:** `deterministic_trend + collective_anomaly`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `exp_collective_arma_049.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `exp_collective_white_noise_032.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `exp_collective_arma_006.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `exp_collective_ar_172.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `exp_collective_arma_140.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `exp_collective_white_noise_112.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `exp_collective_ma_145.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `exp_collective_arma_236.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `exp_collective_arma_069.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `exp_collective_ma_224.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
---

## Grup 20: exp+mean_shift
**Beklenen:** `deterministic_trend + mean_shift`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `exp_meanshift1_arma_154.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `exp_meanshift1_arma_009.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `exp_meanshift1_arma_223.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `exp_meanshift1_ma_017.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `exp_meanshift1_ar_216.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `exp_meanshift1_ar_132.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `exp_meanshift1_arma_061.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `exp_meanshift1_ma_132.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `exp_meanshift1_ma_153.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `exp_meanshift1_ma_182.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `exp_meanshift2_white_noise_206.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `exp_meanshift2_ma_131.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `exp_meanshift2_white_noise_184.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `exp_meanshift2_ar_244.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `exp_meanshift2_ma_175.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `exp_meanshift2_ar_249.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `exp_meanshift2_arma_016.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `exp_meanshift2_arma_006.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `exp_meanshift2_ma_044.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `exp_meanshift2_ma_064.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
---

## Grup 21: exp+point_anomaly
**Beklenen:** `deterministic_trend + point_anomaly`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `exp_point_ar_171.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `exp_point_arma_012.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `exp_point_arma_017.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `exp_point_ma_042.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `exp_point_ma_239.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `exp_point_ar_031.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `exp_point_ma_048.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `exp_point_ar_043.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `exp_point_ma_014.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `exp_point_white_noise_082.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
---

## Grup 22: exp+variance_shift
**Beklenen:** `deterministic_trend + variance_shift`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `exp_varshift_ma_214.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `exp_varshift_ma_190.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `exp_varshift_ar_190.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `exp_varshift_white_noise_075.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `exp_varshift_white_noise_212.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `exp_varshift_white_noise_181.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `exp_varshift_arma_183.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `exp_varshift_arma_109.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `exp_varshift_white_noise_190.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `exp_varshift_arma_098.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
---

## Grup 23: linear+collective
**Beklenen:** `deterministic_trend + collective_anomaly`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `linear_collective_ma_down_073.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `linear_collective_arma_up_054.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `linear_collective_arma_up_243.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `linear_collective_arma_up_143.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `linear_collective_ma_up_019.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `linear_collective_ma_down_078.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `linear_collective_ar_down_016.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `linear_collective_white_noise_down_169.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `linear_collective_ar_down_225.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `linear_collective_ar_down_047.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
---

## Grup 24: linear+mean_shift
**Beklenen:** `deterministic_trend + mean_shift`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `linear_meanshift1_white_noise_down_064.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `linear_meanshift1_ar_up_031.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `linear_meanshift1_arma_down_080.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `linear_meanshift1_ar_up_007.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `linear_meanshift1_white_noise_up_107.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `linear_meanshift1_ar_up_040.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `linear_meanshift1_ar_up_095.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `linear_meanshift1_ma_down_078.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `linear_meanshift1_arma_up_124.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `linear_meanshift1_ma_up_088.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `linear_meanshift2_arma_up_106.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `linear_meanshift2_ar_down_057.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `linear_meanshift2_ma_up_075.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `linear_meanshift2_white_noise_down_097.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `linear_meanshift2_white_noise_down_118.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `linear_meanshift2_arma_down_082.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `linear_meanshift2_ma_up_044.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `linear_meanshift2_white_noise_up_003.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `linear_meanshift2_ma_up_040.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `linear_meanshift2_white_noise_down_027.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
---

## Grup 25: linear+point_anomaly
**Beklenen:** `deterministic_trend + point_anomaly`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `linear_point_arma_down_064.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `linear_point_arma_down_191.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `linear_point_ar_up_080.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `linear_point_ar_up_026.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `linear_point_ar_up_022.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `linear_point_ma_down_131.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `linear_point_ar_up_224.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `linear_point_arma_down_114.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `linear_point_ma_up_054.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `linear_point_arma_down_019.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
---

## Grup 26: linear+trend_shift
**Beklenen:** `deterministic_trend + trend_shift`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `trendshift_direction_and_magnitude_change_ma_up_094.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_and_magnitude_change_arma_up_050.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_and_magnitude_change_arma_down_084.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_and_magnitude_change_ma_down_011.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_and_magnitude_change_white_noise_down_115.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_and_magnitude_change_ar_up_069.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_and_magnitude_change_ma_up_035.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_and_magnitude_change_white_noise_down_053.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_and_magnitude_change_ar_down_089.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_and_magnitude_change_ma_down_079.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_change_white_noise_up_003.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_change_white_noise_up_122.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_change_arma_down_097.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_change_white_noise_up_041.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_change_ma_down_040.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_change_white_noise_up_066.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_change_arma_down_043.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_change_arma_up_110.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_change_arma_up_091.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_direction_change_white_noise_up_047.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_magnitude_change_white_noise_up_013.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_magnitude_change_ma_up_083.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_magnitude_change_white_noise_up_033.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_magnitude_change_ma_down_080.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_magnitude_change_ar_up_111.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_magnitude_change_ar_down_027.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_magnitude_change_arma_down_047.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_magnitude_change_white_noise_up_071.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_magnitude_change_arma_down_076.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
| `data` | `trendshift_magnitude_change_ma_up_075.csv` | `deterministic_trend + trend_shift` | ✓ FULL |
---

## Grup 27: linear+variance_shift
**Beklenen:** `deterministic_trend + variance_shift`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `linear_varshift1_white_noise_up_071.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `linear_varshift1_ar_down_037.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `linear_varshift1_white_noise_up_044.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `linear_varshift1_ma_down_055.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `linear_varshift1_ma_down_076.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `linear_varshift1_ma_up_047.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `linear_varshift1_arma_down_033.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `linear_varshift1_arma_up_058.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `linear_varshift1_white_noise_up_075.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `linear_varshift1_white_noise_down_119.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
---

## Grup 28: quad+collective
**Beklenen:** `deterministic_trend + collective_anomaly`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `quadratic_collective_ar_072.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `quadratic_collective_arma_016.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `quadratic_collective_white_noise_234.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `quadratic_collective_arma_212.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `quadratic_collective_ma_101.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `quadratic_collective_arma_147.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `quadratic_collective_white_noise_020.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `quadratic_collective_white_noise_090.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `quadratic_collective_ma_229.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
| `data` | `quadratic_collective_ar_157.csv` | `deterministic_trend + collective_anomaly` | ✓ FULL |
---

## Grup 29: quad+mean_shift
**Beklenen:** `deterministic_trend + mean_shift`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `quadratic_meanshift1_white_noise_201.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `quadratic_meanshift1_arma_078.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `quadratic_meanshift1_ar_056.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `quadratic_meanshift1_arma_166.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `quadratic_meanshift1_ma_077.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `quadratic_meanshift1_arma_246.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `quadratic_meanshift1_ma_080.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `quadratic_meanshift1_white_noise_104.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `quadratic_meanshift1_white_noise_119.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `quadratic_meanshift1_ar_148.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `quadratic_meanshift2_ma_193.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `quadratic_meanshift2_white_noise_168.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `quadratic_meanshift2_ma_053.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `quadratic_meanshift2_ar_089.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `quadratic_meanshift2_ar_143.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `quadratic_meanshift2_white_noise_023.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `quadratic_meanshift2_white_noise_007.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `quadratic_meanshift2_arma_143.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `quadratic_meanshift2_white_noise_059.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
| `data` | `quadratic_meanshift2_ma_205.csv` | `deterministic_trend + mean_shift` | ✓ FULL |
---

## Grup 30: quad+point_anomaly
**Beklenen:** `deterministic_trend + point_anomaly`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `quadratic_point_ma_241.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_arma_080.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_ma_012.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_white_noise_013.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_white_noise_247.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_ar_104.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_arma_054.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_arma_100.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_ar_197.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_arma_237.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_white_noise_108.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_arma_077.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_ar_098.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_ma_119.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_white_noise_037.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_ma_128.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_white_noise_227.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_ma_109.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_ar_156.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
| `data` | `quadratic_point_white_noise_242.csv` | `deterministic_trend + point_anomaly` | ✓ FULL |
---

## Grup 31: quad+variance_shift
**Beklenen:** `deterministic_trend + variance_shift`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `data` | `quadratic_varshift_white_noise_042.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `quadratic_varshift_ar_084.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `quadratic_varshift_arma_030.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `quadratic_varshift_ma_149.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `quadratic_varshift_ar_029.csv` | `deterministic_trend + mean_shift` | ~ PARTIAL |
| `data` | `quadratic_varshift_white_noise_052.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `quadratic_varshift_ar_211.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `quadratic_varshift_ma_002.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
| `data` | `quadratic_varshift_arma_233.csv` | `deterministic_trend + variance_shift` | ✓ FULL |
| `data` | `quadratic_varshift_ar_114.csv` | `deterministic_trend + mean_shift + variance_shift` | ✓ FULL |
---

## Grup 32: stoch+collective
**Beklenen:** `stochastic_trend + collective_anomaly`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `Stochastic Trend + Collective Anomaly` | `rwd_single_collective_anomaly_middle_608.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ✓ FULL |
| `Stochastic Trend + Collective Anomaly` | `rwd_single_collective_anomaly_middle_966.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ✓ FULL |
| `Stochastic Trend + Collective Anomaly` | `rwd_single_collective_anomaly_middle_444.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ✓ FULL |
| `Stochastic Trend + Collective Anomaly` | `rwd_single_collective_anomaly_middle_497.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ✓ FULL |
| `Stochastic Trend + Collective Anomaly` | `rwd_single_collective_anomaly_middle_27.csv` | `stochastic_trend + collective_anomaly` | ✓ FULL |
| `Stochastic Trend + Collective Anomaly` | `rwd_single_collective_anomaly_middle_725.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ✓ FULL |
| `Stochastic Trend + Collective Anomaly` | `rwd_single_collective_anomaly_middle_638.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ✓ FULL |
| `Stochastic Trend + Collective Anomaly` | `rwd_single_collective_anomaly_middle_707.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ✓ FULL |
| `Stochastic Trend + Collective Anomaly` | `rwd_single_collective_anomaly_middle_449.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ✓ FULL |
| `Stochastic Trend + Collective Anomaly` | `rwd_single_collective_anomaly_middle_177.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ✓ FULL |
---

## Grup 33: stoch+mean_shift
**Beklenen:** `stochastic_trend + mean_shift`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `Stochastic Trend + Mean Shift` | `rwd_single_mean_shift_increase_middle_81.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ✓ FULL |
| `Stochastic Trend + Mean Shift` | `rwd_single_mean_shift_increase_middle_669.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ✓ FULL |
| `Stochastic Trend + Mean Shift` | `rwd_single_mean_shift_increase_middle_370.csv` | `stochastic_trend + mean_shift` | ✓ FULL |
| `Stochastic Trend + Mean Shift` | `rwd_single_mean_shift_increase_middle_834.csv` | `stochastic_trend + mean_shift` | ✓ FULL |
| `Stochastic Trend + Mean Shift` | `rwd_single_mean_shift_increase_middle_325.csv` | `stochastic_trend + collective_anomaly` | ~ PARTIAL |
| `Stochastic Trend + Mean Shift` | `rwd_single_mean_shift_increase_middle_756.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ✓ FULL |
| `Stochastic Trend + Mean Shift` | `rwd_single_mean_shift_increase_middle_166.csv` | `stochastic_trend + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `Stochastic Trend + Mean Shift` | `rwd_single_mean_shift_increase_middle_174.csv` | `stochastic_trend + mean_shift` | ✓ FULL |
| `Stochastic Trend + Mean Shift` | `rwd_single_mean_shift_increase_middle_345.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ✓ FULL |
| `Stochastic Trend + Mean Shift` | `rwd_single_mean_shift_increase_middle_24.csv` | `stochastic_trend + collective_anomaly + mean_shift` | ✓ FULL |
---

## Grup 34: stoch+point_anomaly
**Beklenen:** `stochastic_trend + point_anomaly`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `Stochastic Trend + Point Anomaly` | `rwd_single_point_anomaly_middle_449.csv` | `stochastic_trend + mean_shift + point_anomaly` | ✓ FULL |
| `Stochastic Trend + Point Anomaly` | `rwd_single_point_anomaly_middle_754.csv` | `stochastic_trend + point_anomaly` | ✓ FULL |
| `Stochastic Trend + Point Anomaly` | `rwd_single_point_anomaly_middle_820.csv` | `stochastic_trend + point_anomaly` | ✓ FULL |
| `Stochastic Trend + Point Anomaly` | `rwd_single_point_anomaly_middle_683.csv` | `stochastic_trend + point_anomaly` | ✓ FULL |
| `Stochastic Trend + Point Anomaly` | `rwd_single_point_anomaly_middle_24.csv` | `stochastic_trend + point_anomaly` | ✓ FULL |
| `Stochastic Trend + Point Anomaly` | `rwd_single_point_anomaly_middle_780.csv` | `stochastic_trend + mean_shift + point_anomaly` | ✓ FULL |
| `Stochastic Trend + Point Anomaly` | `rwd_single_point_anomaly_middle_457.csv` | `stochastic_trend + mean_shift + point_anomaly` | ✓ FULL |
| `Stochastic Trend + Point Anomaly` | `rwd_single_point_anomaly_middle_390.csv` | `stochastic_trend + point_anomaly` | ✓ FULL |
| `Stochastic Trend + Point Anomaly` | `rwd_single_point_anomaly_middle_430.csv` | `stochastic_trend + point_anomaly` | ✓ FULL |
| `Stochastic Trend + Point Anomaly` | `rwd_single_point_anomaly_middle_197.csv` | `stochastic_trend + collective_anomaly + mean_shift + point_anomaly` | ✓ FULL |
---

## Grup 35: stoch+variance_shift
**Beklenen:** `stochastic_trend + variance_shift`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `ARI + Variance Shift` | `ari_multiple_variance_shifts_773.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `ARI + Variance Shift` | `ari_multiple_variance_shifts_136.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `ARI + Variance Shift` | `ari_single_variance_shift_decrease_end_571.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `ARI + Variance Shift` | `ari_single_variance_shift_decrease_middle_678.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `ARI + Variance Shift` | `ari_single_variance_shift_decrease_end_952.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `ARI + Variance Shift` | `ari_single_variance_shift_increase_middle_310.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `ARI + Variance Shift` | `ari_single_variance_shift_decrease_end_287.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `ARI + Variance Shift` | `ari_multiple_variance_shifts_852.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `ARI + Variance Shift` | `ari_single_variance_shift_decrease_beginning_175.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `ARI + Variance Shift` | `ari_multiple_variance_shifts_742.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `ARIMA + Variance Shift` | `arima_single_variance_shift_decrease_beginning_580.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `ARIMA + Variance Shift` | `arima_single_variance_shift_decrease_middle_576.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `ARIMA + Variance Shift` | `arima_single_variance_shift_decrease_middle_707.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `ARIMA + Variance Shift` | `arima_single_variance_shift_increase_beginning_604.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `ARIMA + Variance Shift` | `arima_single_variance_shift_increase_beginning_589.csv` | `stochastic_trend + trend_shift + variance_shift` | ✓ FULL |
| `ARIMA + Variance Shift` | `arima_single_variance_shift_increase_beginning_276.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `ARIMA + Variance Shift` | `arima_single_variance_shift_decrease_middle_406.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `ARIMA + Variance Shift` | `arima_multiple_variance_shifts_860.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `ARIMA + Variance Shift` | `arima_multiple_variance_shifts_292.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `ARIMA + Variance Shift` | `arima_multiple_variance_shifts_76.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `IMA + Variance Shift` | `ima_single_variance_shift_decrease_end_908.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `IMA + Variance Shift` | `ima_single_variance_shift_increase_beginning_585.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `IMA + Variance Shift` | `ima_multiple_variance_shifts_785.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `IMA + Variance Shift` | `ima_single_variance_shift_increase_beginning_90.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `IMA + Variance Shift` | `ima_single_variance_shift_increase_beginning_908.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `IMA + Variance Shift` | `ima_single_variance_shift_increase_middle_482.csv` | `stationary + variance_shift` | ~ PARTIAL |
| `IMA + Variance Shift` | `ima_single_variance_shift_decrease_end_690.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `IMA + Variance Shift` | `ima_single_variance_shift_decrease_middle_238.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `IMA + Variance Shift` | `ima_multiple_variance_shifts_19.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `IMA + Variance Shift` | `ima_single_variance_shift_decrease_end_45.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RW + Variance Shift` | `rw_single_variance_shift_decrease_middle_449.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RW + Variance Shift` | `rw_single_variance_shift_decrease_middle_257.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RW + Variance Shift` | `rw_single_variance_shift_increase_middle_442.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RW + Variance Shift` | `rw_multiple_variance_shifts_722.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RW + Variance Shift` | `rw_single_variance_shift_increase_end_942.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RW + Variance Shift` | `rw_single_variance_shift_increase_beginning_623.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RW + Variance Shift` | `rw_single_variance_shift_decrease_beginning_989.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RW + Variance Shift` | `rw_single_variance_shift_increase_beginning_715.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RW + Variance Shift` | `rw_single_variance_shift_increase_beginning_34.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RW + Variance Shift` | `rw_single_variance_shift_decrease_beginning_449.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RWD + Variance Shift` | `rwd_single_variance_shift_increase_end_651.csv` | `stochastic_trend + mean_shift + variance_shift` | ✓ FULL |
| `RWD + Variance Shift` | `rwd_single_variance_shift_decrease_middle_204.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RWD + Variance Shift` | `rwd_single_variance_shift_decrease_beginning_448.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RWD + Variance Shift` | `rwd_single_variance_shift_decrease_beginning_221.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RWD + Variance Shift` | `rwd_single_variance_shift_decrease_end_280.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RWD + Variance Shift` | `rwd_single_variance_shift_decrease_end_518.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RWD + Variance Shift` | `rwd_single_variance_shift_decrease_end_277.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RWD + Variance Shift` | `rwd_single_variance_shift_increase_beginning_133.csv` | `stochastic_trend` | ~ PARTIAL |
| `RWD + Variance Shift` | `rwd_single_variance_shift_decrease_beginning_274.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
| `RWD + Variance Shift` | `rwd_multiple_variance_shifts_565.csv` | `stochastic_trend + variance_shift` | ✓ FULL |
---

## Grup 36: vol+collective
**Beklenen:** `volatility + collective_anomaly`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `Volatility + Collective Anomaly` | `garch_single_collective_anomaly_middle_252.csv` | `volatility + collective_anomaly + point_anomaly` | ✓ FULL |
| `Volatility + Collective Anomaly` | `garch_single_collective_anomaly_middle_5.csv` | `volatility + collective_anomaly + point_anomaly` | ✓ FULL |
| `Volatility + Collective Anomaly` | `garch_single_collective_anomaly_middle_352.csv` | `volatility + collective_anomaly + variance_shift` | ✓ FULL |
| `Volatility + Collective Anomaly` | `garch_single_collective_anomaly_middle_487.csv` | `volatility + collective_anomaly` | ✓ FULL |
| `Volatility + Collective Anomaly` | `garch_single_collective_anomaly_middle_374.csv` | `volatility + variance_shift` | ~ PARTIAL |
| `Volatility + Collective Anomaly` | `garch_single_collective_anomaly_middle_544.csv` | `volatility + collective_anomaly` | ✓ FULL |
| `Volatility + Collective Anomaly` | `garch_single_collective_anomaly_middle_82.csv` | `volatility + collective_anomaly + point_anomaly` | ✓ FULL |
| `Volatility + Collective Anomaly` | `garch_single_collective_anomaly_middle_169.csv` | `volatility + collective_anomaly` | ✓ FULL |
| `Volatility + Collective Anomaly` | `garch_single_collective_anomaly_middle_430.csv` | `volatility + collective_anomaly` | ✓ FULL |
| `Volatility + Collective Anomaly` | `garch_single_collective_anomaly_middle_33.csv` | `volatility + collective_anomaly + point_anomaly` | ✓ FULL |
---

## Grup 37: vol+mean_shift
**Beklenen:** `volatility + mean_shift`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `Volatility + Mean Shift` | `garch_single_mean_shift_increase_middle_969.csv` | `volatility + mean_shift + variance_shift` | ✓ FULL |
| `Volatility + Mean Shift` | `garch_single_mean_shift_increase_middle_325.csv` | `volatility + collective_anomaly + mean_shift + point_anomaly` | ✓ FULL |
| `Volatility + Mean Shift` | `garch_single_mean_shift_increase_middle_763.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ✓ FULL |
| `Volatility + Mean Shift` | `garch_single_mean_shift_increase_middle_675.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ✓ FULL |
| `Volatility + Mean Shift` | `garch_single_mean_shift_increase_middle_555.csv` | `volatility + mean_shift + point_anomaly + trend_shift` | ✓ FULL |
| `Volatility + Mean Shift` | `garch_single_mean_shift_increase_middle_646.csv` | `volatility + collective_anomaly + mean_shift` | ✓ FULL |
| `Volatility + Mean Shift` | `garch_single_mean_shift_increase_middle_667.csv` | `volatility + collective_anomaly + mean_shift + trend_shift` | ✓ FULL |
| `Volatility + Mean Shift` | `garch_single_mean_shift_increase_middle_279.csv` | `volatility + mean_shift + trend_shift` | ✓ FULL |
| `Volatility + Mean Shift` | `garch_single_mean_shift_increase_middle_52.csv` | `volatility + mean_shift + point_anomaly` | ✓ FULL |
| `Volatility + Mean Shift` | `garch_single_mean_shift_increase_middle_197.csv` | `volatility + mean_shift` | ✓ FULL |
---

## Grup 38: vol+point_anomaly
**Beklenen:** `volatility + point_anomaly`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `Volatility + Point Anomaly` | `garch_single_point_anomaly_middle_222.csv` | `volatility + collective_anomaly + point_anomaly` | ✓ FULL |
| `Volatility + Point Anomaly` | `garch_single_point_anomaly_middle_379.csv` | `volatility + mean_shift + point_anomaly + trend_shift + variance_shift` | ✓ FULL |
| `Volatility + Point Anomaly` | `garch_single_point_anomaly_middle_103.csv` | `volatility + point_anomaly` | ✓ FULL |
| `Volatility + Point Anomaly` | `garch_single_point_anomaly_middle_973.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ✓ FULL |
| `Volatility + Point Anomaly` | `garch_single_point_anomaly_middle_463.csv` | `volatility` | ~ PARTIAL |
| `Volatility + Point Anomaly` | `garch_single_point_anomaly_middle_404.csv` | `volatility + collective_anomaly + point_anomaly` | ✓ FULL |
| `Volatility + Point Anomaly` | `garch_single_point_anomaly_middle_874.csv` | `volatility + collective_anomaly + point_anomaly` | ✓ FULL |
| `Volatility + Point Anomaly` | `garch_single_point_anomaly_middle_670.csv` | `volatility + collective_anomaly + point_anomaly` | ✓ FULL |
| `Volatility + Point Anomaly` | `garch_single_point_anomaly_middle_449.csv` | `volatility + point_anomaly + variance_shift` | ✓ FULL |
| `Volatility + Point Anomaly` | `garch_single_point_anomaly_middle_84.csv` | `volatility + collective_anomaly + point_anomaly` | ✓ FULL |
---

## Grup 39: vol+variance_shift
**Beklenen:** `volatility + variance_shift`

| Leaf | CSV | Tahmin | Sonuç |
|---|---|---|---|
| `Volatility + Variance Shift` | `garch_single_variance_shift_increase_middle_893.csv` | `volatility + point_anomaly + variance_shift` | ✓ FULL |
| `Volatility + Variance Shift` | `garch_single_variance_shift_increase_middle_401.csv` | `volatility + collective_anomaly + variance_shift` | ✓ FULL |
| `Volatility + Variance Shift` | `garch_single_variance_shift_increase_middle_503.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ✓ FULL |
| `Volatility + Variance Shift` | `garch_single_variance_shift_increase_middle_406.csv` | `volatility + collective_anomaly + point_anomaly` | ~ PARTIAL |
| `Volatility + Variance Shift` | `garch_single_variance_shift_increase_middle_495.csv` | `volatility + variance_shift` | ✓ FULL |
| `Volatility + Variance Shift` | `garch_single_variance_shift_increase_middle_850.csv` | `volatility + point_anomaly` | ~ PARTIAL |
| `Volatility + Variance Shift` | `garch_single_variance_shift_increase_middle_858.csv` | `volatility + collective_anomaly + variance_shift` | ✓ FULL |
| `Volatility + Variance Shift` | `garch_single_variance_shift_increase_middle_891.csv` | `volatility + collective_anomaly + variance_shift` | ✓ FULL |
| `Volatility + Variance Shift` | `garch_single_variance_shift_increase_middle_699.csv` | `volatility + collective_anomaly + variance_shift` | ✓ FULL |
| `Volatility + Variance Shift` | `garch_single_variance_shift_increase_middle_997.csv` | `volatility + collective_anomaly + point_anomaly + variance_shift` | ✓ FULL |

---

## Model Olasılıkları — Sadece Hatalı Örnekler

| Grup | CSV | stat | det | stoch | vol | coll | ctx | mean | point | trend | var | Sonuç |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| stationary | `ar_28856.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.32 | 0.00 | 0.03 | 0.61 | 0.00 | 0.01 | PARTIAL |
| stationary | `ar_10735.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.16 | 0.65 | 0.00 | 0.01 | PARTIAL |
| stationary | `ar_31868.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.56 | 0.00 | 0.01 | PARTIAL |
| stationary | `ar_31841.csv` | 1.00 | 0.00 | 0.00 | 0.16 | 0.22 | 0.00 | 0.06 | 0.90 | 0.00 | 0.44 | PARTIAL |
| stationary | `ar_7284.csv` | 1.00 | 0.00 | 0.72 | 0.00 | 0.11 | 0.00 | 0.99 | 0.04 | 0.68 | 0.04 | PARTIAL |
| stationary | `ar_26081.csv` | 1.00 | 0.00 | 0.00 | 0.07 | 0.83 | 0.00 | 0.53 | 0.29 | 0.03 | 0.27 | PARTIAL |
| stationary | `ar_12561.csv` | 1.00 | 0.00 | 0.00 | 0.12 | 0.95 | 0.00 | 0.50 | 0.20 | 0.01 | 0.05 | PARTIAL |
| stationary | `ar_27412.csv` | 1.00 | 0.00 | 0.00 | 0.01 | 0.13 | 0.00 | 0.31 | 0.60 | 0.05 | 0.42 | PARTIAL |
| stationary | `ar_22440.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.26 | 0.59 | 0.00 | 0.11 | PARTIAL |
| stationary | `ar_10935.csv` | 1.00 | 0.00 | 0.00 | 0.08 | 0.31 | 0.00 | 0.98 | 0.36 | 0.04 | 0.04 | PARTIAL |
| stationary | `ar_12761.csv` | 1.00 | 0.51 | 0.00 | 0.01 | 0.00 | 0.00 | 0.01 | 0.14 | 0.00 | 1.00 | PARTIAL |
| stationary | `ar_16446.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.43 | 0.78 | 0.88 | 0.01 | NONE |
| stationary | `ar_1686.csv` | 0.98 | 0.00 | 1.00 | 0.00 | 0.79 | 0.00 | 0.29 | 0.67 | 0.65 | 0.05 | NONE |
| stationary | `ar_24901.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.83 | 0.68 | 0.66 | 0.02 | NONE |
| stationary | `ar_27752.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.73 | 0.00 | 0.48 | 0.55 | 0.85 | 0.07 | NONE |
| stationary | `ar_10780.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.97 | 0.00 | 0.10 | 0.06 | 0.42 | 0.07 | NONE |
| stationary | `ar_2655.csv` | 0.92 | 0.00 | 1.00 | 0.00 | 0.21 | 0.00 | 0.87 | 0.67 | 0.67 | 0.01 | NONE |
| stationary | `ar_15862.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.11 | 0.12 | 0.71 | 0.07 | NONE |
| stationary | `ar_31113.csv` | 0.97 | 0.00 | 1.00 | 0.00 | 0.44 | 0.00 | 0.93 | 0.08 | 0.80 | 0.01 | NONE |
| stationary | `ar_29164.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.92 | 0.00 | 0.05 | 0.60 | 0.04 | 0.09 | NONE |
| stationary | `ar_30681.csv` | 1.00 | 0.00 | 0.00 | 0.02 | 0.13 | 0.00 | 0.05 | 0.24 | 0.25 | 0.86 | PARTIAL |
| stationary | `arma_26069.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.35 | 0.00 | 0.96 | PARTIAL |
| stationary | `arma_2237.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.57 | 0.00 | 0.02 | PARTIAL |
| stationary | `arma_23245.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.97 | 0.00 | 0.06 | 0.33 | 0.00 | 0.02 | PARTIAL |
| stationary | `arma_27377.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.70 | 0.00 | 0.01 | PARTIAL |
| stationary | `arma_10189.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.69 | 0.00 | 0.00 | PARTIAL |
| stationary | `arma_4738.csv` | 0.99 | 0.00 | 1.00 | 0.00 | 0.90 | 0.00 | 0.79 | 0.01 | 0.01 | 0.29 | NONE |
| stationary | `arma_14706.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.60 | 0.00 | 0.02 | 0.80 | 0.01 | 0.61 | PARTIAL |
| stationary | `arma_30587.csv` | 1.00 | 0.00 | 0.00 | 0.51 | 0.18 | 0.00 | 0.04 | 0.55 | 0.00 | 0.38 | PARTIAL |
| stationary | `arma_22461.csv` | 1.00 | 0.00 | 0.00 | 0.77 | 0.17 | 0.00 | 0.03 | 0.62 | 0.00 | 0.23 | PARTIAL |
| stationary | `arma_20031.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.31 | 0.00 | 0.01 | 0.67 | 0.02 | 0.81 | PARTIAL |
| stationary | `arma_14583.csv` | 1.00 | 0.00 | 1.00 | 0.00 | 0.66 | 0.00 | 0.92 | 0.44 | 0.00 | 0.12 | PARTIAL |
| stationary | `arma_16348.csv` | 1.00 | 0.00 | 1.00 | 0.00 | 0.36 | 0.00 | 0.96 | 0.38 | 0.00 | 0.12 | PARTIAL |
| stationary | `arma_9201.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.26 | 0.00 | 0.02 | 0.07 | 0.01 | 0.77 | PARTIAL |
| stationary | `arma_349.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.63 | 0.00 | 0.93 | 0.44 | 0.00 | 0.13 | PARTIAL |
| stationary | `arma_19925.csv` | 1.00 | 0.00 | 0.00 | 0.78 | 0.95 | 0.00 | 0.03 | 0.67 | 0.06 | 0.06 | PARTIAL |
| stationary | `arma_13011.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.82 | 0.00 | 0.14 | 0.30 | 0.03 | 0.20 | PARTIAL |
| stationary | `arma_12733.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.14 | 0.81 | 0.65 | 0.19 | NONE |
| stationary | `arma_21201.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.97 | 0.00 | 0.03 | 0.58 | 0.12 | 0.77 | NONE |
| stationary | `arma_12850.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.84 | 0.00 | 0.03 | 0.57 | 0.01 | 0.18 | PARTIAL |
| stationary | `arma_20585.csv` | 0.85 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.43 | 0.60 | 0.19 | 0.02 | NONE |
| stationary | `arma_5967.csv` | 0.43 | 0.00 | 0.01 | 1.00 | 0.94 | 0.00 | 0.09 | 0.08 | 0.01 | 0.93 | NONE |
| stationary | `arma_20140.csv` | 1.00 | 0.00 | 0.00 | 0.97 | 0.62 | 0.00 | 0.42 | 0.85 | 0.31 | 0.42 | PARTIAL |
| stationary | `arma_27802.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.79 | 0.00 | 0.03 | 0.27 | 0.01 | 0.09 | PARTIAL |
| stationary | `arma_178.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.76 | 0.00 | 0.08 | 0.09 | 0.05 | 0.79 | PARTIAL |
| stationary | `ma_31518.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.06 | 0.63 | 0.00 | 0.04 | PARTIAL |
| stationary | `ma_18644.csv` | 1.00 | 0.00 | 0.30 | 0.02 | 0.86 | 0.00 | 0.86 | 0.23 | 0.00 | 0.32 | PARTIAL |
| stationary | `ma_27024.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.58 | 0.20 | 0.01 | 0.08 | PARTIAL |
| stationary | `ma_15669.csv` | 1.00 | 0.00 | 0.00 | 0.14 | 0.49 | 0.00 | 0.16 | 0.64 | 0.00 | 0.10 | PARTIAL |
| stationary | `ma_30777.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.28 | 0.00 | 0.04 | 0.67 | 0.01 | 0.23 | NONE |
| stationary | `ma_12049.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.92 | 0.00 | 0.04 | 0.81 | 0.09 | 0.07 | NONE |
| stationary | `ma_11349.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.86 | 0.00 | 0.04 | 0.09 | 0.14 | 0.20 | NONE |
| stationary | `ma_2950.csv` | 0.83 | 0.00 | 0.00 | 1.00 | 0.92 | 0.00 | 0.13 | 0.49 | 0.04 | 0.26 | NONE |
| stationary | `ma_16719.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.93 | 0.00 | 0.12 | 0.58 | 0.12 | 0.01 | NONE |
| stationary | `ma_18532.csv` | 0.95 | 0.00 | 0.00 | 1.00 | 0.96 | 0.00 | 0.02 | 0.28 | 0.26 | 0.17 | NONE |
| stationary | `ma_12350.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.63 | 0.00 | 0.37 | 0.26 | 0.73 | 0.01 | NONE |
| stationary | `ma_6198.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.87 | 0.00 | 0.10 | 0.53 | 0.05 | 0.03 | NONE |
| stationary | `ma_16864.csv` | 0.95 | 0.00 | 0.00 | 1.00 | 0.84 | 0.00 | 0.08 | 0.56 | 0.04 | 0.16 | NONE |
| stationary | `wn_6526.csv` | 1.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.55 | 0.00 | 0.02 | 0.00 | 0.00 | PARTIAL |
| stationary | `wn_18196.csv` | 1.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.98 | 0.00 | 0.02 | 0.00 | 0.00 | PARTIAL |
| stationary | `wn_2337.csv` | 1.00 | 0.00 | 0.00 | 0.04 | 0.00 | 0.99 | 0.00 | 0.02 | 0.00 | 0.00 | PARTIAL |
| stationary | `wn_28746.csv` | 1.00 | 0.00 | 0.00 | 0.04 | 0.00 | 0.99 | 0.00 | 0.10 | 0.00 | 0.00 | PARTIAL |
| stationary | `wn_14795.csv` | 1.00 | 0.00 | 0.00 | 0.03 | 0.00 | 1.00 | 0.00 | 0.01 | 0.00 | 0.00 | PARTIAL |
| stationary | `wn_20475.csv` | 1.00 | 0.00 | 0.00 | 0.03 | 0.95 | 0.65 | 0.01 | 0.64 | 0.01 | 0.00 | PARTIAL |
| stationary | `wn_16177.csv` | 1.00 | 0.00 | 0.00 | 0.53 | 0.99 | 0.99 | 0.01 | 0.09 | 0.01 | 0.00 | PARTIAL |
| stationary | `wn_29763.csv` | 0.77 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.01 | 0.02 | 0.01 | 0.02 | NONE |
| stationary | `wn_17872.csv` | 1.00 | 0.00 | 0.00 | 0.56 | 0.67 | 0.00 | 0.09 | 0.28 | 0.02 | 0.00 | PARTIAL |
| stationary | `wn_30696.csv` | 1.00 | 0.35 | 0.00 | 0.01 | 0.99 | 0.98 | 0.01 | 0.09 | 0.00 | 0.02 | PARTIAL |
| stationary | `wn_8597.csv` | 1.00 | 0.00 | 0.00 | 0.81 | 0.81 | 0.04 | 0.01 | 0.34 | 0.02 | 0.03 | PARTIAL |
| stationary | `wn_30156.csv` | 1.00 | 0.00 | 0.00 | 0.11 | 0.82 | 0.94 | 0.01 | 0.61 | 0.02 | 0.00 | PARTIAL |
| stationary | `wn_29109.csv` | 1.00 | 0.00 | 0.00 | 0.71 | 1.00 | 0.88 | 0.01 | 0.22 | 0.02 | 0.01 | PARTIAL |
| stationary | `wn_12102.csv` | 1.00 | 0.00 | 0.00 | 0.04 | 0.98 | 0.35 | 0.01 | 0.73 | 0.01 | 0.01 | PARTIAL |
| stationary | `wn_27963.csv` | 1.00 | 0.00 | 0.00 | 0.05 | 0.98 | 0.99 | 0.01 | 0.19 | 0.00 | 0.01 | PARTIAL |
| stationary | `wn_28724.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.99 | 1.00 | 0.04 | 0.29 | 0.03 | 0.02 | PARTIAL |
| stationary | `wn_15044.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.93 | 0.00 | 0.02 | 0.27 | 0.03 | 0.00 | NONE |
| stationary | `wn_25750.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.95 | 1.00 | 0.01 | 0.25 | 0.04 | 0.00 | NONE |
| stationary | `wn_31500.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.02 | 0.26 | 0.10 | 0.01 | NONE |
| stationary | `wn_17217.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.95 | 1.00 | 0.02 | 0.35 | 0.03 | 0.01 | NONE |
| stationary | `wn_14817.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.63 | 0.10 | 0.01 | 0.37 | 0.10 | 0.01 | NONE |
| stationary | `wn_23630.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.97 | 0.99 | 0.00 | 0.23 | 0.05 | 0.00 | PARTIAL |
| stationary | `wn_21188.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.94 | 0.00 | 0.02 | 0.32 | 0.24 | 0.00 | NONE |
| stationary | `wn_1796.csv` | 0.02 | 0.00 | 0.00 | 1.00 | 0.88 | 0.00 | 0.01 | 0.26 | 0.02 | 0.13 | NONE |
| stationary | `wn_8264.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.97 | 1.00 | 0.01 | 0.54 | 0.03 | 0.01 | PARTIAL |
| deterministic_trend | `ar_cubic_trend_309.csv` | 0.14 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.02 | 0.88 | 0.00 | PARTIAL |
| deterministic_trend | `ar_cubic_trend_856.csv` | 0.29 | 0.05 | 0.00 | 0.00 | 0.00 | 0.00 | 0.06 | 0.11 | 0.66 | 0.00 | NONE |
| deterministic_trend | `ar_cubic_trend_127.csv` | 0.01 | 1.00 | 0.48 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.87 | 0.03 | PARTIAL |
| deterministic_trend | `ar_cubic_trend_39.csv` | 0.08 | 0.97 | 0.00 | 0.00 | 0.01 | 0.00 | 0.01 | 0.06 | 0.55 | 0.00 | PARTIAL |
| deterministic_trend | `ar_cubic_trend_345.csv` | 0.04 | 0.99 | 0.69 | 0.00 | 0.00 | 0.00 | 0.01 | 0.02 | 0.83 | 0.00 | PARTIAL |
| deterministic_trend | `ar_cubic_trend_159.csv` | 0.86 | 0.39 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.04 | 0.00 | NONE |
| deterministic_trend | `ar_cubic_trend_968.csv` | 0.00 | 0.90 | 1.00 | 0.00 | 0.02 | 0.00 | 0.08 | 0.63 | 0.07 | 0.00 | NONE |
| deterministic_trend | `ar_cubic_trend_906.csv` | 0.00 | 0.21 | 0.02 | 0.00 | 0.11 | 0.00 | 0.08 | 0.33 | 0.66 | 0.00 | PARTIAL |
| deterministic_trend | `ar_cubic_trend_760.csv` | 0.01 | 0.02 | 0.00 | 0.00 | 0.05 | 0.00 | 0.08 | 0.53 | 0.58 | 0.00 | PARTIAL |
| deterministic_trend | `ar_cubic_trend_389.csv` | 0.00 | 0.01 | 1.00 | 0.00 | 0.05 | 0.00 | 0.45 | 0.07 | 0.01 | 0.00 | NONE |
| deterministic_trend | `ar_cubic_trend_294.csv` | 0.01 | 0.01 | 0.00 | 0.00 | 0.06 | 0.00 | 0.14 | 0.11 | 0.55 | 0.01 | PARTIAL |
| deterministic_trend | `ar_cubic_trend_702.csv` | 0.01 | 0.00 | 1.00 | 0.00 | 0.04 | 0.00 | 0.05 | 0.88 | 0.10 | 0.00 | NONE |
| deterministic_trend | `ar_cubic_trend_559.csv` | 0.00 | 0.02 | 1.00 | 0.00 | 0.01 | 0.00 | 0.10 | 0.44 | 0.28 | 0.00 | NONE |
| deterministic_trend | `ar_cubic_trend_463.csv` | 0.01 | 0.99 | 0.00 | 0.00 | 0.01 | 0.00 | 0.03 | 0.23 | 0.57 | 0.00 | PARTIAL |
| deterministic_trend | `ar_damped_trend_141.csv` | 0.00 | 0.55 | 0.36 | 0.00 | 0.00 | 0.00 | 0.17 | 0.52 | 0.01 | 0.02 | PARTIAL |
| deterministic_trend | `ar_exponential_trend_829.csv` | 0.98 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.89 | 0.01 | NONE |
| deterministic_trend | `ar_exponential_trend_157.csv` | 0.86 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.76 | 0.22 | NONE |
| deterministic_trend | `ar_exponential_trend_33.csv` | 1.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.93 | 0.00 | NONE |
| deterministic_trend | `ar_exponential_trend_608.csv` | 1.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.99 | 0.02 | NONE |
| deterministic_trend | `ar_exponential_trend_892.csv` | 0.98 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.98 | 0.00 | NONE |
| deterministic_trend | `ar_exponential_trend_968.csv` | 1.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 1.00 | 0.00 | NONE |
| deterministic_trend | `ar_exponential_trend_108.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 1.00 | 0.01 | NONE |
| deterministic_trend | `ar_exponential_trend_727.csv` | 0.48 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.97 | 0.02 | NONE |
| deterministic_trend | `ar_exponential_trend_790.csv` | 0.01 | 0.00 | 0.72 | 0.00 | 0.01 | 0.00 | 0.30 | 0.08 | 0.53 | 0.01 | NONE |
| deterministic_trend | `ar_exponential_trend_344.csv` | 0.18 | 0.00 | 0.97 | 0.00 | 0.00 | 0.00 | 0.39 | 0.12 | 0.89 | 0.01 | NONE |
| deterministic_trend | `ar_exponential_trend_807.csv` | 0.05 | 0.00 | 0.57 | 0.00 | 0.00 | 0.00 | 0.36 | 0.07 | 0.89 | 0.01 | NONE |
| deterministic_trend | `ar_exponential_trend_411.csv` | 0.06 | 0.00 | 0.66 | 0.00 | 0.00 | 0.00 | 0.46 | 0.08 | 0.77 | 0.01 | NONE |
| deterministic_trend | `ar_exponential_trend_200.csv` | 0.06 | 0.00 | 0.81 | 0.00 | 0.01 | 0.00 | 0.40 | 0.10 | 0.90 | 0.00 | NONE |
| deterministic_trend | `ar_exponential_trend_369.csv` | 0.06 | 0.00 | 0.47 | 0.00 | 0.00 | 0.00 | 0.39 | 0.09 | 0.72 | 0.01 | NONE |
| deterministic_trend | `ar_exponential_trend_5.csv` | 0.01 | 0.00 | 1.00 | 0.00 | 0.01 | 0.00 | 0.36 | 0.08 | 0.51 | 0.01 | NONE |
| deterministic_trend | `ar_linear_down_trend_516.csv` | 0.48 | 0.12 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.02 | 0.28 | 0.02 | NONE |
| deterministic_trend | `ar_linear_down_trend_1000.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.92 | 0.01 | NONE |
| deterministic_trend | `ar_linear_down_trend_978.csv` | 0.87 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.76 | 0.03 | NONE |
| deterministic_trend | `ar_linear_down_trend_764.csv` | 0.98 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.75 | 0.01 | 0.00 | 0.02 | NONE |
| deterministic_trend | `ar_linear_down_trend_905.csv` | 0.73 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.01 | 0.92 | 0.02 | NONE |
| deterministic_trend | `ar_linear_down_trend_761.csv` | 0.99 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.54 | 0.01 | NONE |
| deterministic_trend | `ar_linear_down_trend_340.csv` | 0.66 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.86 | 0.02 | NONE |
| deterministic_trend | `ar_linear_down_trend_995.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.98 | 0.01 | NONE |
| deterministic_trend | `ar_linear_down_trend_56.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.98 | 0.01 | NONE |
| deterministic_trend | `ar_linear_down_trend_800.csv` | 0.69 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.80 | 0.01 | 0.02 | 0.01 | NONE |
| deterministic_trend | `ar_linear_down_trend_262.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.20 | 0.97 | 0.00 | NONE |
| deterministic_trend | `ar_linear_down_trend_566.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.73 | 0.06 | 0.53 | 0.02 | NONE |
| deterministic_trend | `ar_linear_down_trend_94.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.10 | 1.00 | 0.00 | NONE |
| deterministic_trend | `ar_linear_down_trend_196.csv` | 0.59 | 0.00 | 0.98 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.95 | 0.00 | NONE |
| deterministic_trend | `ar_linear_down_trend_900.csv` | 0.94 | 0.00 | 0.84 | 0.00 | 0.00 | 0.00 | 0.01 | 0.17 | 0.79 | 0.00 | NONE |
| deterministic_trend | `ar_linear_down_trend_675.csv` | 0.95 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.71 | 0.04 | 0.92 | 0.10 | NONE |
| deterministic_trend | `ar_linear_down_trend_373.csv` | 0.99 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.22 | 1.00 | 0.00 | NONE |
| deterministic_trend | `ar_linear_down_trend_874.csv` | 0.96 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.21 | 0.99 | 0.00 | NONE |
| deterministic_trend | `ar_linear_down_trend_688.csv` | 1.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.21 | 1.00 | 0.00 | NONE |
| deterministic_trend | `ar_linear_down_trend_66.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.16 | 0.99 | 0.00 | NONE |
| deterministic_trend | `ar_linear_down_trend_281.csv` | 0.03 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.18 | 0.81 | 0.00 | NONE |
| deterministic_trend | `ar_linear_down_trend_239.csv` | 0.23 | 0.00 | 1.00 | 0.00 | 0.03 | 0.00 | 0.16 | 0.17 | 0.76 | 0.00 | NONE |
| deterministic_trend | `ar_linear_down_trend_442.csv` | 0.69 | 0.00 | 0.13 | 0.00 | 0.00 | 0.00 | 0.11 | 0.21 | 0.99 | 0.02 | NONE |
| deterministic_trend | `ar_linear_down_trend_800.csv` | 0.95 | 0.00 | 1.00 | 0.00 | 0.04 | 0.00 | 0.31 | 0.86 | 0.93 | 0.01 | NONE |
| deterministic_trend | `ar_linear_down_trend_247.csv` | 0.18 | 0.01 | 0.03 | 0.00 | 0.00 | 0.00 | 0.13 | 0.36 | 0.82 | 0.01 | NONE |
| deterministic_trend | `ar_linear_down_trend_596.csv` | 0.26 | 0.00 | 0.85 | 0.00 | 0.00 | 0.00 | 0.09 | 0.15 | 0.74 | 0.00 | NONE |
| deterministic_trend | `ar_linear_down_trend_978.csv` | 0.04 | 0.01 | 0.04 | 0.00 | 0.00 | 0.00 | 0.05 | 0.22 | 0.85 | 0.00 | NONE |
| deterministic_trend | `ar_linear_down_trend_816.csv` | 0.08 | 0.01 | 0.41 | 0.00 | 0.00 | 0.00 | 0.06 | 0.10 | 0.85 | 0.00 | NONE |
| deterministic_trend | `ar_linear_down_trend_949.csv` | 0.02 | 0.00 | 0.17 | 0.00 | 0.00 | 0.00 | 0.10 | 0.09 | 0.59 | 0.00 | NONE |
| deterministic_trend | `ar_linear_down_trend_588.csv` | 0.85 | 0.00 | 0.05 | 0.00 | 0.00 | 0.00 | 0.11 | 0.06 | 0.87 | 0.01 | NONE |
| deterministic_trend | `ar_linear_up_trend_945.csv` | 0.94 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.62 | 0.00 | 0.02 | 0.04 | NONE |
| deterministic_trend | `ar_linear_up_trend_1.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.92 | 0.01 | NONE |
| deterministic_trend | `ar_linear_up_trend_650.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.74 | 0.00 | NONE |
| deterministic_trend | `ar_linear_up_trend_397.csv` | 0.96 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.91 | 0.01 | NONE |
| deterministic_trend | `ar_linear_up_trend_549.csv` | 0.59 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.01 | 0.08 | 0.01 | NONE |
| deterministic_trend | `ar_linear_up_trend_115.csv` | 0.75 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.35 | 0.01 | 0.02 | 0.02 | NONE |
| deterministic_trend | `ar_linear_up_trend_200.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.92 | 0.01 | NONE |
| deterministic_trend | `ar_linear_up_trend_955.csv` | 1.00 | 0.00 | 0.75 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.86 | 0.01 | NONE |
| deterministic_trend | `ar_linear_up_trend_432.csv` | 0.51 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.02 | 0.25 | 0.02 | NONE |
| deterministic_trend | `ar_linear_up_trend_908.csv` | 0.98 | 0.00 | 0.91 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.39 | 0.01 | NONE |
| deterministic_trend | `ar_linear_up_trend_865.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.08 | 1.00 | 0.00 | NONE |
| deterministic_trend | `ar_linear_up_trend_842.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.14 | 0.99 | 0.00 | NONE |
| deterministic_trend | `ar_linear_up_trend_381.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.12 | 0.99 | 0.00 | NONE |
| deterministic_trend | `ar_linear_up_trend_319.csv` | 0.99 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.53 | 0.05 | 0.99 | 0.00 | NONE |
| deterministic_trend | `ar_linear_up_trend_151.csv` | 1.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.81 | 0.05 | 0.99 | 0.01 | NONE |
| deterministic_trend | `ar_linear_up_trend_32.csv` | 0.83 | 0.00 | 0.97 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.98 | 0.00 | NONE |
| deterministic_trend | `ar_linear_up_trend_908.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.99 | 0.02 | 0.54 | 0.00 | NONE |
| deterministic_trend | `ar_linear_up_trend_620.csv` | 0.97 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.13 | 0.63 | 0.00 | NONE |
| deterministic_trend | `ar_linear_up_trend_971.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.06 | 1.00 | 0.00 | NONE |
| deterministic_trend | `ar_linear_up_trend_170.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.09 | 1.00 | 0.00 | NONE |
| deterministic_trend | `ar_linear_up_trend_177.csv` | 0.56 | 0.00 | 0.69 | 0.00 | 0.00 | 0.00 | 0.83 | 0.22 | 0.94 | 0.00 | NONE |
| deterministic_trend | `ar_linear_up_trend_773.csv` | 0.05 | 0.00 | 1.00 | 0.00 | 0.01 | 0.00 | 0.82 | 0.06 | 0.78 | 0.00 | NONE |
| deterministic_trend | `ar_linear_up_trend_546.csv` | 0.20 | 0.00 | 0.15 | 1.00 | 0.03 | 0.00 | 0.98 | 0.14 | 1.00 | 0.11 | NONE |
| deterministic_trend | `ar_linear_up_trend_850.csv` | 0.98 | 0.00 | 0.39 | 0.98 | 0.16 | 0.00 | 0.94 | 0.08 | 1.00 | 0.03 | NONE |
| deterministic_trend | `ar_linear_up_trend_161.csv` | 0.43 | 0.00 | 0.85 | 0.00 | 0.00 | 0.00 | 0.88 | 0.23 | 0.98 | 0.00 | NONE |
| deterministic_trend | `ar_linear_up_trend_8.csv` | 0.51 | 0.00 | 1.00 | 0.00 | 0.11 | 0.00 | 0.71 | 0.38 | 0.99 | 0.00 | NONE |
| deterministic_trend | `ar_linear_up_trend_59.csv` | 0.44 | 0.00 | 0.99 | 0.00 | 0.15 | 0.00 | 0.84 | 0.23 | 0.97 | 0.00 | NONE |
| deterministic_trend | `ar_linear_up_trend_804.csv` | 0.07 | 0.00 | 0.83 | 0.00 | 0.00 | 0.00 | 0.87 | 0.09 | 0.75 | 0.00 | NONE |
| deterministic_trend | `ar_linear_up_trend_213.csv` | 0.97 | 0.00 | 1.00 | 0.00 | 0.03 | 0.00 | 0.94 | 0.39 | 0.99 | 0.00 | NONE |
| deterministic_trend | `ar_linear_up_trend_216.csv` | 0.49 | 0.00 | 0.98 | 0.00 | 0.03 | 0.00 | 0.86 | 0.37 | 0.95 | 0.00 | NONE |
| deterministic_trend | `ar_quadratic_trend_706.csv` | 0.98 | 0.00 | 0.01 | 0.00 | 0.00 | 0.20 | 0.00 | 0.66 | 0.00 | 0.01 | NONE |
| deterministic_trend | `ar_quadratic_trend_536.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.01 | NONE |
| deterministic_trend | `ar_quadratic_trend_971.csv` | 0.60 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.03 | 0.00 | 0.01 | NONE |
| deterministic_trend | `ar_quadratic_trend_604.csv` | 0.74 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.57 | 0.00 | 0.01 | NONE |
| deterministic_trend | `ar_quadratic_trend_250.csv` | 0.56 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.02 | 0.00 | 0.00 | NONE |
| deterministic_trend | `ar_quadratic_trend_342.csv` | 0.15 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | NONE |
| deterministic_trend | `ar_quadratic_trend_585.csv` | 0.98 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.02 | 0.00 | 0.00 | NONE |
| deterministic_trend | `ar_quadratic_trend_902.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.18 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | NONE |
| deterministic_trend | `ar_quadratic_trend_658.csv` | 0.84 | 0.00 | 0.00 | 0.00 | 0.00 | 0.44 | 0.01 | 0.03 | 0.01 | 0.01 | NONE |
| deterministic_trend | `ar_quadratic_trend_489.csv` | 0.98 | 0.00 | 0.00 | 0.00 | 0.00 | 0.18 | 0.01 | 0.54 | 0.00 | 0.01 | NONE |
| deterministic_trend | `ar_quadratic_trend_988.csv` | 0.29 | 0.13 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.02 | 0.02 | 0.00 | NONE |
| deterministic_trend | `ar_quadratic_trend_293.csv` | 0.60 | 0.00 | 0.00 | 0.00 | 0.19 | 0.51 | 0.01 | 0.88 | 0.18 | 0.00 | NONE |
| deterministic_trend | `ar_quadratic_trend_955.csv` | 0.04 | 0.02 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.02 | 0.02 | 0.01 | NONE |
| deterministic_trend | `ar_quadratic_trend_596.csv` | 0.91 | 0.02 | 0.03 | 0.00 | 1.00 | 0.00 | 0.01 | 0.02 | 0.24 | 0.00 | NONE |
| deterministic_trend | `ar_quadratic_trend_795.csv` | 0.86 | 0.00 | 0.00 | 0.00 | 0.03 | 0.33 | 0.01 | 0.94 | 0.39 | 0.00 | NONE |
| deterministic_trend | `ar_quadratic_trend_771.csv` | 0.27 | 0.07 | 0.00 | 0.00 | 0.98 | 0.00 | 0.00 | 0.03 | 0.23 | 0.01 | NONE |
| deterministic_trend | `ar_quadratic_trend_734.csv` | 0.54 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 | 0.01 | 0.09 | 0.11 | 0.01 | NONE |
| deterministic_trend | `ar_quadratic_trend_283.csv` | 0.21 | 0.00 | 0.00 | 0.00 | 0.20 | 0.00 | 0.01 | 0.87 | 0.05 | 0.00 | NONE |
| deterministic_trend | `ar_quadratic_trend_756.csv` | 0.05 | 0.13 | 0.00 | 0.00 | 0.98 | 0.00 | 0.00 | 0.08 | 0.09 | 0.01 | PARTIAL |
| deterministic_trend | `ar_quadratic_trend_386.csv` | 0.68 | 0.03 | 0.00 | 0.00 | 0.16 | 0.00 | 0.00 | 0.88 | 0.03 | 0.01 | NONE |
| deterministic_trend | `ar_quadratic_trend_466.csv` | 0.36 | 0.00 | 0.01 | 0.00 | 0.51 | 1.00 | 0.01 | 0.13 | 0.38 | 0.00 | NONE |
| deterministic_trend | `ar_quadratic_trend_717.csv` | 0.92 | 0.00 | 0.95 | 0.00 | 0.21 | 1.00 | 0.01 | 0.80 | 0.11 | 0.00 | NONE |
| deterministic_trend | `ar_quadratic_trend_698.csv` | 0.97 | 0.01 | 0.05 | 0.01 | 0.65 | 1.00 | 0.00 | 0.88 | 0.54 | 0.00 | NONE |
| deterministic_trend | `ar_quadratic_trend_442.csv` | 0.88 | 0.02 | 0.01 | 0.01 | 0.35 | 1.00 | 0.00 | 0.87 | 0.41 | 0.00 | NONE |
| deterministic_trend | `ar_quadratic_trend_501.csv` | 0.94 | 0.00 | 0.00 | 0.00 | 0.21 | 0.00 | 0.01 | 0.91 | 0.18 | 0.00 | NONE |
| deterministic_trend | `ar_quadratic_trend_928.csv` | 0.11 | 0.00 | 0.00 | 0.11 | 0.55 | 0.00 | 0.01 | 0.08 | 0.13 | 0.01 | NONE |
| deterministic_trend | `ar_quadratic_trend_575.csv` | 0.84 | 0.00 | 0.00 | 0.07 | 0.51 | 0.00 | 0.01 | 0.04 | 0.08 | 0.00 | NONE |
| deterministic_trend | `ar_quadratic_trend_514.csv` | 0.99 | 0.00 | 0.00 | 0.00 | 0.56 | 0.89 | 0.00 | 0.09 | 0.47 | 0.00 | NONE |
| deterministic_trend | `ar_quadratic_trend_209.csv` | 0.99 | 0.00 | 0.00 | 0.01 | 0.49 | 1.00 | 0.01 | 0.05 | 0.72 | 0.02 | NONE |
| deterministic_trend | `ar_quadratic_trend_326.csv` | 0.82 | 0.00 | 0.00 | 0.79 | 0.22 | 0.00 | 0.01 | 0.08 | 0.46 | 0.01 | NONE |
| deterministic_trend | `arma_cubic_trend_305.csv` | 0.02 | 0.14 | 1.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.30 | NONE |
| deterministic_trend | `arma_cubic_trend_750.csv` | 0.24 | 0.99 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.86 | 0.00 | PARTIAL |
| deterministic_trend | `arma_cubic_trend_680.csv` | 0.31 | 0.99 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.02 | 0.99 | 0.01 | PARTIAL |
| deterministic_trend | `arma_cubic_trend_127.csv` | 0.09 | 0.85 | 0.39 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.65 | 0.00 | PARTIAL |
| deterministic_trend | `arma_cubic_trend_891.csv` | 0.15 | 0.34 | 1.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.04 | 0.00 | 0.02 | NONE |
| deterministic_trend | `arma_cubic_trend_402.csv` | 0.79 | 0.51 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.05 | 0.36 | 0.00 | NONE |
| deterministic_trend | `arma_cubic_trend_163.csv` | 0.53 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.03 | 1.00 | 0.01 | PARTIAL |
| deterministic_trend | `arma_cubic_trend_572.csv` | 0.00 | 0.07 | 1.00 | 0.00 | 0.02 | 0.00 | 0.19 | 0.06 | 0.02 | 0.00 | NONE |
| deterministic_trend | `arma_cubic_trend_317.csv` | 0.00 | 0.95 | 1.00 | 0.00 | 0.00 | 0.00 | 0.32 | 0.01 | 0.01 | 0.01 | NONE |
| deterministic_trend | `arma_cubic_trend_355.csv` | 0.00 | 0.00 | 0.01 | 0.00 | 0.17 | 0.00 | 0.29 | 0.53 | 0.77 | 0.00 | NONE |
| deterministic_trend | `arma_cubic_trend_546.csv` | 0.00 | 0.09 | 0.97 | 0.00 | 0.01 | 0.00 | 0.12 | 0.04 | 0.27 | 0.00 | NONE |
| deterministic_trend | `arma_cubic_trend_296.csv` | 0.00 | 0.00 | 0.01 | 0.00 | 0.07 | 0.00 | 0.50 | 0.25 | 0.34 | 0.01 | NONE |
| deterministic_trend | `arma_cubic_trend_596.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.16 | 0.00 | 0.16 | 0.89 | 0.10 | 0.00 | NONE |
| deterministic_trend | `arma_cubic_trend_22.csv` | 0.01 | 0.30 | 0.99 | 0.00 | 0.06 | 0.00 | 0.12 | 0.74 | 0.36 | 0.00 | NONE |
| deterministic_trend | `arma_cubic_trend_960.csv` | 0.00 | 0.31 | 0.99 | 0.00 | 0.06 | 0.00 | 0.05 | 0.29 | 0.23 | 0.00 | NONE |
| deterministic_trend | `arma_exponential_trend_327.csv` | 0.98 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.84 | 0.05 | NONE |
| deterministic_trend | `arma_exponential_trend_593.csv` | 0.99 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.84 | 0.01 | NONE |
| deterministic_trend | `arma_exponential_trend_524.csv` | 0.40 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.97 | 0.02 | NONE |
| deterministic_trend | `arma_exponential_trend_328.csv` | 0.78 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.98 | 0.01 | NONE |
| deterministic_trend | `arma_exponential_trend_904.csv` | 0.52 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.98 | 0.01 | NONE |
| deterministic_trend | `arma_exponential_trend_168.csv` | 0.42 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.98 | 0.03 | NONE |
| deterministic_trend | `arma_exponential_trend_843.csv` | 0.54 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.96 | 0.02 | NONE |
| deterministic_trend | `arma_exponential_trend_893.csv` | 0.77 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.96 | 0.01 | NONE |
| deterministic_trend | `arma_exponential_trend_888.csv` | 0.92 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.99 | 0.01 | NONE |
| deterministic_trend | `arma_exponential_trend_189.csv` | 0.03 | 0.00 | 0.71 | 0.00 | 0.00 | 0.00 | 0.40 | 0.07 | 0.88 | 0.01 | NONE |
| deterministic_trend | `arma_exponential_trend_597.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.01 | 0.00 | 0.34 | 0.07 | 0.24 | 0.01 | NONE |
| deterministic_trend | `arma_exponential_trend_111.csv` | 0.02 | 0.00 | 0.81 | 0.00 | 0.00 | 0.00 | 0.37 | 0.08 | 0.69 | 0.01 | NONE |
| deterministic_trend | `arma_exponential_trend_992.csv` | 0.08 | 0.00 | 0.62 | 0.00 | 0.01 | 0.00 | 0.58 | 0.11 | 0.82 | 0.00 | NONE |
| deterministic_trend | `arma_linear_down_trend_881.csv` | 0.99 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.70 | 0.02 | NONE |
| deterministic_trend | `arma_linear_down_trend_316.csv` | 0.42 | 0.12 | 0.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.02 | 0.08 | 0.01 | NONE |
| deterministic_trend | `arma_linear_down_trend_251.csv` | 0.97 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.89 | 0.01 | NONE |
| deterministic_trend | `arma_linear_down_trend_546.csv` | 0.99 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.02 | 0.77 | 0.13 | NONE |
| deterministic_trend | `arma_linear_down_trend_541.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.99 | 0.00 | NONE |
| deterministic_trend | `arma_linear_down_trend_295.csv` | 0.96 | 0.01 | 0.17 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.84 | 0.01 | NONE |
| deterministic_trend | `arma_linear_down_trend_896.csv` | 0.35 | 0.05 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.02 | 0.19 | 0.01 | NONE |
| deterministic_trend | `arma_linear_down_trend_468.csv` | 0.92 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.15 | 0.01 | NONE |
| deterministic_trend | `arma_linear_down_trend_930.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 1.00 | 0.00 | NONE |
| deterministic_trend | `arma_linear_down_trend_152.csv` | 0.98 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.19 | 0.99 | 0.00 | NONE |
| deterministic_trend | `arma_linear_down_trend_25.csv` | 0.96 | 0.00 | 0.43 | 0.00 | 0.00 | 0.00 | 0.00 | 0.09 | 0.96 | 0.00 | NONE |
| deterministic_trend | `arma_linear_down_trend_448.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.08 | 1.00 | 0.00 | NONE |
| deterministic_trend | `arma_linear_down_trend_100.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.50 | 0.20 | 0.94 | 0.00 | NONE |
| deterministic_trend | `arma_linear_down_trend_458.csv` | 0.99 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.08 | 1.00 | 0.00 | NONE |
| deterministic_trend | `arma_linear_down_trend_342.csv` | 0.99 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.95 | 0.02 | 0.25 | 0.06 | NONE |
| deterministic_trend | `arma_linear_down_trend_952.csv` | 0.87 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.24 | 0.93 | 0.00 | NONE |
| deterministic_trend | `arma_linear_down_trend_820.csv` | 0.45 | 0.00 | 0.65 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.82 | 0.00 | NONE |
| deterministic_trend | `arma_linear_down_trend_821.csv` | 0.99 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.12 | 0.99 | 0.00 | NONE |
| deterministic_trend | `arma_linear_down_trend_517.csv` | 0.96 | 0.00 | 0.22 | 0.00 | 0.00 | 0.00 | 0.16 | 0.09 | 0.70 | 0.00 | NONE |
| deterministic_trend | `arma_linear_down_trend_361.csv` | 0.03 | 0.01 | 0.76 | 0.00 | 0.00 | 0.00 | 0.18 | 0.11 | 0.76 | 0.00 | NONE |
| deterministic_trend | `arma_linear_down_trend_489.csv` | 0.41 | 0.01 | 0.44 | 0.00 | 0.00 | 0.00 | 0.07 | 0.36 | 0.97 | 0.00 | NONE |
| deterministic_trend | `arma_linear_down_trend_740.csv` | 0.13 | 0.01 | 1.00 | 0.00 | 0.30 | 0.00 | 0.23 | 0.52 | 0.64 | 0.00 | NONE |
| deterministic_trend | `arma_linear_down_trend_981.csv` | 0.93 | 0.00 | 0.81 | 0.00 | 0.00 | 0.00 | 0.14 | 0.25 | 0.99 | 0.02 | NONE |
| deterministic_trend | `arma_linear_down_trend_772.csv` | 0.07 | 0.00 | 0.16 | 0.00 | 0.01 | 0.00 | 0.56 | 0.04 | 0.50 | 0.00 | NONE |
| deterministic_trend | `arma_linear_down_trend_820.csv` | 0.20 | 0.01 | 0.18 | 0.00 | 0.00 | 0.00 | 0.08 | 0.28 | 0.76 | 0.01 | NONE |
| deterministic_trend | `arma_linear_down_trend_610.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.03 | 0.00 | 0.87 | 0.16 | 0.99 | 0.11 | NONE |
| deterministic_trend | `arma_linear_down_trend_708.csv` | 0.48 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.19 | 0.80 | 0.00 | NONE |
| deterministic_trend | `arma_linear_down_trend_760.csv` | 0.09 | 0.00 | 0.70 | 0.00 | 0.00 | 0.00 | 0.34 | 0.30 | 0.61 | 0.00 | NONE |
| deterministic_trend | `arma_linear_down_trend_547.csv` | 0.37 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.22 | 0.37 | 0.76 | 0.00 | NONE |
| deterministic_trend | `arma_linear_up_trend_240.csv` | 0.98 | 0.00 | 0.82 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.88 | 0.00 | NONE |
| deterministic_trend | `arma_linear_up_trend_273.csv` | 0.49 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.67 | 0.02 | NONE |
| deterministic_trend | `arma_linear_up_trend_371.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.29 | 0.01 | 0.03 | 0.03 | NONE |
| deterministic_trend | `arma_linear_up_trend_299.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.90 | 0.00 | NONE |
| deterministic_trend | `arma_linear_up_trend_991.csv` | 0.83 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.54 | 0.02 | NONE |
| deterministic_trend | `arma_linear_up_trend_151.csv` | 0.45 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.01 | 0.15 | 0.02 | NONE |
| deterministic_trend | `arma_linear_up_trend_632.csv` | 0.99 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.52 | 0.01 | NONE |
| deterministic_trend | `arma_linear_up_trend_777.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.86 | 0.01 | NONE |
| deterministic_trend | `arma_linear_up_trend_599.csv` | 0.94 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.13 | 0.01 | NONE |
| deterministic_trend | `arma_linear_up_trend_154.csv` | 0.99 | 0.00 | 0.08 | 0.00 | 0.00 | 0.00 | 0.79 | 0.00 | 0.01 | 0.04 | NONE |
| deterministic_trend | `arma_linear_up_trend_788.csv` | 0.96 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 1.00 | 0.00 | NONE |
| deterministic_trend | `arma_linear_up_trend_388.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.56 | 0.02 | 1.00 | 0.00 | NONE |
| deterministic_trend | `arma_linear_up_trend_150.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.06 | 1.00 | 0.00 | NONE |
| deterministic_trend | `arma_linear_up_trend_144.csv` | 0.96 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.14 | 0.98 | 0.00 | NONE |
| deterministic_trend | `arma_linear_up_trend_637.csv` | 1.00 | 0.00 | 0.19 | 0.00 | 0.00 | 0.00 | 0.01 | 0.05 | 0.98 | 0.00 | NONE |
| deterministic_trend | `arma_linear_up_trend_538.csv` | 0.91 | 0.00 | 0.53 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.81 | 0.00 | NONE |
| deterministic_trend | `arma_linear_up_trend_561.csv` | 1.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.01 | 0.08 | 0.99 | 0.00 | NONE |
| deterministic_trend | `arma_linear_up_trend_946.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 1.00 | 0.00 | NONE |
| deterministic_trend | `arma_linear_up_trend_885.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.99 | 0.00 | NONE |
| deterministic_trend | `arma_linear_up_trend_588.csv` | 0.99 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.88 | 0.00 | 0.31 | 0.95 | NONE |
| deterministic_trend | `arma_linear_up_trend_243.csv` | 0.02 | 0.00 | 0.57 | 0.00 | 0.00 | 0.00 | 0.91 | 0.08 | 0.80 | 0.00 | NONE |
| deterministic_trend | `arma_linear_up_trend_150.csv` | 0.05 | 0.00 | 0.41 | 0.00 | 0.00 | 0.00 | 0.76 | 0.12 | 0.78 | 0.00 | NONE |
| deterministic_trend | `arma_linear_up_trend_984.csv` | 0.80 | 0.00 | 1.00 | 0.00 | 0.04 | 0.00 | 0.74 | 0.18 | 0.97 | 0.01 | NONE |
| deterministic_trend | `arma_linear_up_trend_567.csv` | 0.02 | 0.00 | 1.00 | 0.00 | 0.04 | 0.00 | 0.85 | 0.04 | 0.57 | 0.00 | NONE |
| deterministic_trend | `arma_linear_up_trend_172.csv` | 0.32 | 0.00 | 0.57 | 0.00 | 0.00 | 0.00 | 0.68 | 0.08 | 0.90 | 0.00 | NONE |
| deterministic_trend | `arma_linear_up_trend_883.csv` | 0.24 | 0.00 | 0.98 | 0.00 | 0.00 | 0.00 | 0.75 | 0.34 | 0.95 | 0.00 | NONE |
| deterministic_trend | `arma_linear_up_trend_27.csv` | 0.52 | 0.00 | 0.53 | 0.00 | 0.02 | 0.00 | 0.85 | 0.39 | 0.96 | 0.00 | NONE |
| deterministic_trend | `arma_linear_up_trend_161.csv` | 0.45 | 0.00 | 1.00 | 0.00 | 0.02 | 0.00 | 0.89 | 0.38 | 0.92 | 0.00 | NONE |
| deterministic_trend | `arma_linear_up_trend_647.csv` | 0.97 | 0.00 | 1.00 | 0.00 | 0.03 | 0.00 | 0.82 | 0.34 | 1.00 | 0.00 | NONE |
| deterministic_trend | `arma_linear_up_trend_160.csv` | 0.20 | 0.00 | 0.99 | 0.00 | 0.03 | 0.00 | 0.89 | 0.18 | 0.89 | 0.00 | NONE |
| deterministic_trend | `arma_quadratic_trend_720.csv` | 0.70 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | NONE |
| deterministic_trend | `arma_quadratic_trend_893.csv` | 0.02 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.66 | 0.00 | 0.14 | NONE |
| deterministic_trend | `arma_quadratic_trend_314.csv` | 0.94 | 0.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.01 | 0.03 | 0.01 | 0.00 | NONE |
| deterministic_trend | `arma_quadratic_trend_470.csv` | 0.32 | 0.01 | 0.00 | 0.00 | 0.01 | 0.00 | 0.01 | 0.02 | 0.00 | 0.02 | NONE |
| deterministic_trend | `arma_quadratic_trend_208.csv` | 0.94 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.11 | NONE |
| deterministic_trend | `arma_quadratic_trend_967.csv` | 0.82 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.01 | 0.03 | 0.01 | 0.00 | NONE |
| deterministic_trend | `arma_quadratic_trend_919.csv` | 0.64 | 0.00 | 0.00 | 0.00 | 0.32 | 0.00 | 0.01 | 0.00 | 0.00 | 0.01 | NONE |
| deterministic_trend | `arma_quadratic_trend_623.csv` | 0.89 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.01 | NONE |
| deterministic_trend | `arma_quadratic_trend_325.csv` | 0.79 | 0.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.01 | 0.02 | 0.00 | 0.01 | NONE |
| deterministic_trend | `arma_quadratic_trend_631.csv` | 0.84 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | NONE |
| deterministic_trend | `arma_quadratic_trend_646.csv` | 0.70 | 0.00 | 0.00 | 0.00 | 0.98 | 0.00 | 0.01 | 0.88 | 0.25 | 0.00 | NONE |
| deterministic_trend | `arma_quadratic_trend_134.csv` | 0.88 | 0.02 | 0.00 | 0.00 | 1.00 | 0.04 | 0.01 | 0.03 | 0.39 | 0.00 | NONE |
| deterministic_trend | `arma_quadratic_trend_67.csv` | 0.85 | 0.00 | 0.00 | 0.00 | 0.97 | 0.01 | 0.01 | 0.73 | 0.12 | 0.01 | NONE |
| deterministic_trend | `arma_quadratic_trend_173.csv` | 0.23 | 0.06 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | NONE |
| deterministic_trend | `arma_quadratic_trend_485.csv` | 0.84 | 0.00 | 0.00 | 0.00 | 0.91 | 0.00 | 0.01 | 0.89 | 0.01 | 0.01 | NONE |
| deterministic_trend | `arma_quadratic_trend_704.csv` | 0.27 | 1.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.98 | 0.01 | 0.00 | PARTIAL |
| deterministic_trend | `arma_quadratic_trend_636.csv` | 0.60 | 0.02 | 0.00 | 0.00 | 0.12 | 0.54 | 0.00 | 0.81 | 0.36 | 0.00 | NONE |
| deterministic_trend | `arma_quadratic_trend_619.csv` | 0.04 | 0.01 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.02 | 0.02 | 0.01 | NONE |
| deterministic_trend | `arma_quadratic_trend_580.csv` | 0.50 | 0.07 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.01 | 0.20 | 0.01 | NONE |
| deterministic_trend | `arma_quadratic_trend_39.csv` | 0.97 | 0.00 | 0.00 | 0.00 | 1.00 | 0.30 | 0.01 | 0.03 | 0.04 | 0.01 | NONE |
| deterministic_trend | `arma_quadratic_trend_960.csv` | 0.81 | 0.04 | 0.00 | 0.02 | 0.60 | 0.12 | 0.00 | 0.84 | 0.10 | 0.00 | NONE |
| deterministic_trend | `arma_quadratic_trend_339.csv` | 0.15 | 0.00 | 0.00 | 0.00 | 0.61 | 0.00 | 0.01 | 0.08 | 0.48 | 0.00 | NONE |
| deterministic_trend | `arma_quadratic_trend_287.csv` | 0.53 | 0.00 | 0.00 | 0.90 | 0.50 | 0.00 | 0.00 | 0.05 | 0.14 | 0.01 | NONE |
| deterministic_trend | `arma_quadratic_trend_715.csv` | 0.94 | 0.01 | 0.01 | 0.00 | 0.87 | 0.01 | 0.01 | 0.05 | 0.06 | 0.01 | NONE |
| deterministic_trend | `arma_quadratic_trend_759.csv` | 0.80 | 0.00 | 0.00 | 0.01 | 0.51 | 0.00 | 0.00 | 0.08 | 0.48 | 0.01 | NONE |
| deterministic_trend | `arma_quadratic_trend_388.csv` | 0.98 | 0.00 | 0.00 | 0.00 | 0.86 | 1.00 | 0.01 | 0.90 | 0.75 | 0.00 | NONE |
| deterministic_trend | `arma_quadratic_trend_318.csv` | 0.52 | 0.00 | 0.02 | 0.00 | 0.18 | 0.00 | 0.00 | 0.13 | 0.47 | 0.00 | NONE |
| deterministic_trend | `arma_quadratic_trend_342.csv` | 0.10 | 0.00 | 0.02 | 0.02 | 0.79 | 0.00 | 0.00 | 0.04 | 0.02 | 0.00 | NONE |
| deterministic_trend | `arma_quadratic_trend_463.csv` | 0.77 | 0.00 | 0.00 | 0.93 | 0.51 | 0.00 | 0.01 | 0.05 | 0.07 | 0.00 | NONE |
| deterministic_trend | `arma_quadratic_trend_219.csv` | 0.95 | 0.03 | 0.00 | 0.00 | 0.28 | 0.09 | 0.00 | 0.91 | 0.15 | 0.01 | NONE |
| deterministic_trend | `ma_cubic_trend_717.csv` | 0.01 | 0.99 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.92 | 0.00 | PARTIAL |
| deterministic_trend | `ma_cubic_trend_693.csv` | 0.13 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.96 | 0.00 | PARTIAL |
| deterministic_trend | `ma_cubic_trend_375.csv` | 0.04 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.82 | 0.00 | PARTIAL |
| deterministic_trend | `ma_cubic_trend_39.csv` | 0.01 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.85 | 0.00 | PARTIAL |
| deterministic_trend | `ma_cubic_trend_165.csv` | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.63 | 0.00 | PARTIAL |
| deterministic_trend | `ma_cubic_trend_106.csv` | 0.01 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.76 | 0.00 | PARTIAL |
| deterministic_trend | `ma_cubic_trend_520.csv` | 0.74 | 0.55 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.14 | 0.66 | 0.00 | NONE |
| deterministic_trend | `ma_cubic_trend_671.csv` | 0.09 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.02 | 0.81 | 0.00 | PARTIAL |
| deterministic_trend | `ma_cubic_trend_594.csv` | 0.03 | 0.06 | 0.22 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.07 | 0.00 | NONE |
| deterministic_trend | `ma_cubic_trend_295.csv` | 0.05 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.02 | 0.97 | 0.00 | PARTIAL |
| deterministic_trend | `ma_cubic_trend_565.csv` | 0.73 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.23 | 0.18 | 0.00 | NONE |
| deterministic_trend | `ma_cubic_trend_959.csv` | 0.01 | 0.68 | 1.00 | 0.00 | 0.03 | 0.00 | 0.04 | 0.82 | 0.47 | 0.00 | NONE |
| deterministic_trend | `ma_cubic_trend_42.csv` | 0.00 | 0.12 | 1.00 | 0.00 | 0.01 | 0.00 | 0.48 | 0.01 | 0.00 | 0.01 | NONE |
| deterministic_trend | `ma_cubic_trend_910.csv` | 0.15 | 0.10 | 0.95 | 0.00 | 0.05 | 0.00 | 0.10 | 0.46 | 0.17 | 0.02 | NONE |
| deterministic_trend | `ma_cubic_trend_161.csv` | 0.00 | 0.01 | 0.01 | 0.00 | 0.17 | 0.00 | 0.03 | 0.34 | 0.85 | 0.00 | NONE |
| deterministic_trend | `ma_cubic_trend_909.csv` | 0.01 | 0.19 | 0.20 | 0.00 | 0.01 | 0.00 | 0.19 | 0.26 | 0.58 | 0.00 | NONE |
| deterministic_trend | `ma_cubic_trend_323.csv` | 0.26 | 0.25 | 0.81 | 0.00 | 0.03 | 0.00 | 0.03 | 0.66 | 0.30 | 0.00 | NONE |
| deterministic_trend | `ma_cubic_trend_439.csv` | 0.03 | 0.07 | 1.00 | 0.00 | 0.05 | 0.00 | 0.07 | 0.53 | 0.29 | 0.00 | NONE |
| deterministic_trend | `ma_cubic_trend_243.csv` | 0.00 | 0.89 | 0.00 | 0.00 | 0.14 | 0.00 | 0.09 | 0.45 | 0.54 | 0.00 | PARTIAL |
| deterministic_trend | `ma_cubic_trend_501.csv` | 0.14 | 0.49 | 0.01 | 0.00 | 0.11 | 0.00 | 0.08 | 0.54 | 0.66 | 0.00 | PARTIAL |
| deterministic_trend | `ma_damped_trend_358.csv` | 0.00 | 0.79 | 0.90 | 0.00 | 0.00 | 0.00 | 0.19 | 0.56 | 0.01 | 0.01 | NONE |
| deterministic_trend | `ma_exponential_trend_286.csv` | 0.99 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.94 | 0.03 | NONE |
| deterministic_trend | `ma_exponential_trend_683.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.94 | 0.00 | NONE |
| deterministic_trend | `ma_exponential_trend_341.csv` | 0.98 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.73 | 0.03 | NONE |
| deterministic_trend | `ma_exponential_trend_564.csv` | 0.99 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.97 | 0.01 | NONE |
| deterministic_trend | `ma_exponential_trend_549.csv` | 0.98 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.88 | 0.01 | NONE |
| deterministic_trend | `ma_exponential_trend_933.csv` | 0.97 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.98 | 0.00 | NONE |
| deterministic_trend | `ma_exponential_trend_183.csv` | 0.95 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.98 | 0.02 | NONE |
| deterministic_trend | `ma_exponential_trend_863.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 1.00 | 0.00 | NONE |
| deterministic_trend | `ma_exponential_trend_353.csv` | 0.99 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.99 | 0.00 | NONE |
| deterministic_trend | `ma_exponential_trend_405.csv` | 0.00 | 1.00 | 0.84 | 0.00 | 0.00 | 0.00 | 0.05 | 0.55 | 0.03 | 0.01 | PARTIAL |
| deterministic_trend | `ma_exponential_trend_809.csv` | 0.00 | 0.00 | 0.97 | 0.00 | 0.00 | 0.00 | 0.58 | 0.23 | 0.33 | 0.01 | NONE |
| deterministic_trend | `ma_exponential_trend_686.csv` | 0.01 | 0.00 | 0.96 | 0.00 | 0.01 | 0.00 | 0.22 | 0.09 | 0.62 | 0.01 | NONE |
| deterministic_trend | `ma_exponential_trend_782.csv` | 0.25 | 0.00 | 0.62 | 0.00 | 0.01 | 0.00 | 0.59 | 0.07 | 0.91 | 0.00 | NONE |
| deterministic_trend | `ma_exponential_trend_505.csv` | 0.01 | 0.00 | 0.52 | 0.00 | 0.01 | 0.00 | 0.41 | 0.08 | 0.85 | 0.01 | NONE |
| deterministic_trend | `ma_linear_down_trend_749.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.88 | 0.00 | NONE |
| deterministic_trend | `ma_linear_down_trend_492.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.98 | 0.01 | NONE |
| deterministic_trend | `ma_linear_down_trend_615.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.92 | 0.01 | NONE |
| deterministic_trend | `ma_linear_down_trend_106.csv` | 0.99 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.98 | 0.01 | NONE |
| deterministic_trend | `ma_linear_down_trend_200.csv` | 0.99 | 0.44 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.97 | 0.00 | NONE |
| deterministic_trend | `ma_linear_down_trend_168.csv` | 0.62 | 0.20 | 0.00 | 0.00 | 0.00 | 0.00 | 0.50 | 0.02 | 0.01 | 0.02 | NONE |
| deterministic_trend | `ma_linear_down_trend_97.csv` | 0.84 | 0.51 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.78 | 0.01 | NONE |
| deterministic_trend | `ma_linear_down_trend_912.csv` | 0.97 | 0.25 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.02 | 0.87 | 0.00 | NONE |
| deterministic_trend | `ma_linear_down_trend_735.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.91 | 0.01 | NONE |
| deterministic_trend | `ma_linear_down_trend_931.csv` | 0.94 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.57 | 0.01 | NONE |
| deterministic_trend | `ma_linear_down_trend_235.csv` | 0.97 | 0.00 | 0.62 | 0.00 | 0.00 | 0.00 | 0.02 | 0.07 | 0.99 | 0.00 | NONE |
| deterministic_trend | `ma_linear_down_trend_600.csv` | 0.99 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.15 | 0.99 | 0.00 | NONE |
| deterministic_trend | `ma_linear_down_trend_130.csv` | 0.99 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.12 | 1.00 | 0.00 | NONE |
| deterministic_trend | `ma_linear_down_trend_868.csv` | 0.97 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.16 | 1.00 | 0.00 | NONE |
| deterministic_trend | `ma_linear_down_trend_439.csv` | 0.97 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.08 | 1.00 | 0.00 | NONE |
| deterministic_trend | `ma_linear_down_trend_635.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.18 | 1.00 | 0.00 | NONE |
| deterministic_trend | `ma_linear_down_trend_607.csv` | 0.99 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.11 | 0.98 | 0.00 | NONE |
| deterministic_trend | `ma_linear_down_trend_234.csv` | 0.99 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.96 | 0.04 | 0.33 | 0.01 | NONE |
| deterministic_trend | `ma_linear_down_trend_495.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.18 | 1.00 | 0.00 | NONE |
| deterministic_trend | `ma_linear_down_trend_215.csv` | 0.94 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.98 | 0.05 | 0.02 | 0.04 | PARTIAL |
| deterministic_trend | `ma_linear_down_trend_136.csv` | 0.41 | 0.00 | 0.21 | 0.00 | 0.01 | 0.00 | 0.16 | 0.17 | 0.90 | 0.00 | NONE |
| deterministic_trend | `ma_linear_down_trend_382.csv` | 0.04 | 0.00 | 0.29 | 0.00 | 0.00 | 0.00 | 0.16 | 0.09 | 0.47 | 0.01 | NONE |
| deterministic_trend | `ma_linear_down_trend_434.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.11 | 0.18 | 0.33 | 0.00 | NONE |
| deterministic_trend | `ma_linear_down_trend_927.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.09 | 0.11 | 0.21 | 0.00 | NONE |
| deterministic_trend | `ma_linear_down_trend_959.csv` | 0.67 | 0.00 | 0.25 | 0.00 | 0.01 | 0.00 | 0.10 | 0.14 | 0.89 | 0.00 | NONE |
| deterministic_trend | `ma_linear_down_trend_832.csv` | 0.97 | 0.00 | 0.85 | 0.00 | 0.75 | 0.00 | 0.37 | 0.80 | 0.87 | 0.02 | NONE |
| deterministic_trend | `ma_linear_down_trend_995.csv` | 0.75 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.11 | 0.33 | 0.96 | 0.00 | NONE |
| deterministic_trend | `ma_linear_down_trend_892.csv` | 0.17 | 0.00 | 1.00 | 0.00 | 0.11 | 0.00 | 0.54 | 0.36 | 0.97 | 0.00 | NONE |
| deterministic_trend | `ma_linear_down_trend_134.csv` | 0.69 | 0.00 | 0.12 | 0.00 | 0.00 | 0.00 | 0.11 | 0.14 | 0.73 | 0.00 | NONE |
| deterministic_trend | `ma_linear_down_trend_428.csv` | 0.40 | 0.00 | 0.13 | 0.00 | 0.00 | 0.00 | 0.28 | 0.14 | 0.65 | 0.01 | NONE |
| deterministic_trend | `ma_linear_up_trend_292.csv` | 0.74 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.06 | 0.00 | 0.21 | 0.05 | NONE |
| deterministic_trend | `ma_linear_up_trend_727.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.89 | 0.00 | NONE |
| deterministic_trend | `ma_linear_up_trend_328.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.92 | 0.00 | NONE |
| deterministic_trend | `ma_linear_up_trend_712.csv` | 1.00 | 0.00 | 0.88 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.85 | 0.01 | NONE |
| deterministic_trend | `ma_linear_up_trend_193.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.98 | 0.01 | NONE |
| deterministic_trend | `ma_linear_up_trend_424.csv` | 0.91 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.69 | 0.00 | 0.02 | 0.03 | NONE |
| deterministic_trend | `ma_linear_up_trend_817.csv` | 0.95 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.25 | 0.01 | NONE |
| deterministic_trend | `ma_linear_up_trend_614.csv` | 0.96 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.26 | 0.00 | 0.07 | 0.02 | NONE |
| deterministic_trend | `ma_linear_up_trend_913.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.98 | 0.01 | NONE |
| deterministic_trend | `ma_linear_up_trend_904.csv` | 0.81 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.01 | 0.21 | 0.02 | NONE |
| deterministic_trend | `ma_linear_up_trend_473.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 1.00 | 0.00 | NONE |
| deterministic_trend | `ma_linear_up_trend_997.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.99 | 0.00 | NONE |
| deterministic_trend | `ma_linear_up_trend_670.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.05 | 1.00 | 0.00 | NONE |
| deterministic_trend | `ma_linear_up_trend_79.csv` | 0.94 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.55 | 0.00 | 0.53 | 0.97 | NONE |
| deterministic_trend | `ma_linear_up_trend_240.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.04 | 0.98 | 0.00 | NONE |
| deterministic_trend | `ma_linear_up_trend_951.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.13 | 0.99 | 0.00 | NONE |
| deterministic_trend | `ma_linear_up_trend_956.csv` | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.15 | 0.98 | 0.00 | PARTIAL |
| deterministic_trend | `ma_linear_up_trend_316.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.11 | 1.00 | 0.00 | NONE |
| deterministic_trend | `ma_linear_up_trend_896.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.12 | 0.99 | 0.00 | NONE |
| deterministic_trend | `ma_linear_up_trend_248.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 1.00 | 0.00 | NONE |
| deterministic_trend | `ma_linear_up_trend_999.csv` | 0.31 | 0.00 | 0.97 | 0.00 | 0.00 | 0.00 | 0.84 | 0.17 | 0.87 | 0.00 | NONE |
| deterministic_trend | `ma_linear_up_trend_836.csv` | 0.47 | 0.00 | 0.86 | 0.00 | 0.04 | 0.00 | 0.87 | 0.25 | 0.98 | 0.00 | NONE |
| deterministic_trend | `ma_linear_up_trend_846.csv` | 0.49 | 0.00 | 1.00 | 0.00 | 0.23 | 0.00 | 0.92 | 0.18 | 0.98 | 0.00 | NONE |
| deterministic_trend | `ma_linear_up_trend_261.csv` | 0.93 | 0.00 | 0.36 | 0.00 | 0.01 | 0.00 | 0.86 | 0.51 | 0.98 | 0.00 | NONE |
| deterministic_trend | `ma_linear_up_trend_910.csv` | 0.67 | 0.00 | 1.00 | 0.00 | 0.35 | 0.00 | 0.87 | 0.16 | 0.97 | 0.01 | NONE |
| deterministic_trend | `ma_linear_up_trend_479.csv` | 0.55 | 0.00 | 1.00 | 0.00 | 0.04 | 0.00 | 0.75 | 0.26 | 0.99 | 0.00 | NONE |
| deterministic_trend | `ma_linear_up_trend_120.csv` | 0.01 | 0.00 | 1.00 | 0.00 | 0.02 | 0.00 | 0.96 | 0.07 | 0.36 | 0.00 | NONE |
| deterministic_trend | `ma_linear_up_trend_263.csv` | 0.72 | 0.00 | 1.00 | 0.00 | 0.38 | 0.00 | 0.81 | 0.31 | 0.97 | 0.00 | NONE |
| deterministic_trend | `ma_linear_up_trend_778.csv` | 0.05 | 0.00 | 1.00 | 0.00 | 0.02 | 0.00 | 0.94 | 0.10 | 0.66 | 0.00 | NONE |
| deterministic_trend | `ma_linear_up_trend_950.csv` | 0.46 | 0.00 | 1.00 | 0.00 | 0.17 | 0.00 | 0.82 | 0.68 | 0.92 | 0.00 | NONE |
| deterministic_trend | `ma_quadratic_trend_404.csv` | 0.24 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.04 | 0.00 | 0.00 | NONE |
| deterministic_trend | `ma_quadratic_trend_82.csv` | 0.94 | 0.00 | 0.00 | 0.00 | 0.00 | 0.43 | 0.02 | 0.01 | 0.01 | 0.00 | NONE |
| deterministic_trend | `ma_quadratic_trend_957.csv` | 0.86 | 0.00 | 0.00 | 0.00 | 0.05 | 0.00 | 0.01 | 0.01 | 0.00 | 0.01 | NONE |
| deterministic_trend | `ma_quadratic_trend_838.csv` | 0.56 | 0.12 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.01 | NONE |
| deterministic_trend | `ma_quadratic_trend_715.csv` | 0.81 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.01 | 0.02 | 0.01 | 0.00 | NONE |
| deterministic_trend | `ma_quadratic_trend_895.csv` | 0.75 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.04 | 0.00 | 0.01 | NONE |
| deterministic_trend | `ma_quadratic_trend_776.csv` | 0.85 | 0.23 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.73 | 0.00 | 0.01 | NONE |
| deterministic_trend | `ma_quadratic_trend_846.csv` | 0.92 | 0.00 | 0.00 | 0.00 | 0.00 | 0.42 | 0.01 | 0.64 | 0.02 | 0.01 | NONE |
| deterministic_trend | `ma_quadratic_trend_327.csv` | 0.58 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.02 | 0.00 | 0.01 | NONE |
| deterministic_trend | `ma_quadratic_trend_344.csv` | 0.67 | 0.00 | 0.00 | 0.00 | 0.97 | 0.41 | 0.01 | 0.91 | 0.25 | 0.01 | NONE |
| deterministic_trend | `ma_quadratic_trend_245.csv` | 0.60 | 0.00 | 0.00 | 0.00 | 0.96 | 0.00 | 0.01 | 0.12 | 0.05 | 0.01 | NONE |
| deterministic_trend | `ma_quadratic_trend_824.csv` | 0.34 | 0.04 | 0.00 | 0.00 | 1.00 | 0.00 | 0.01 | 0.01 | 0.13 | 0.00 | NONE |
| deterministic_trend | `ma_quadratic_trend_745.csv` | 0.86 | 0.05 | 0.00 | 0.00 | 0.97 | 0.15 | 0.00 | 0.91 | 0.62 | 0.01 | NONE |
| deterministic_trend | `ma_quadratic_trend_198.csv` | 0.75 | 0.09 | 0.00 | 0.00 | 0.98 | 0.05 | 0.01 | 0.06 | 0.31 | 0.01 | NONE |
| deterministic_trend | `ma_quadratic_trend_450.csv` | 0.87 | 0.00 | 0.00 | 0.00 | 1.00 | 0.03 | 0.01 | 0.01 | 0.40 | 0.00 | NONE |
| deterministic_trend | `ma_quadratic_trend_902.csv` | 0.93 | 0.01 | 0.00 | 0.00 | 1.00 | 0.03 | 0.01 | 0.03 | 0.30 | 0.01 | NONE |
| deterministic_trend | `ma_quadratic_trend_133.csv` | 0.39 | 0.00 | 0.00 | 0.00 | 0.08 | 0.00 | 0.01 | 0.90 | 0.14 | 0.00 | NONE |
| deterministic_trend | `ma_quadratic_trend_890.csv` | 0.42 | 0.01 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.01 | 0.06 | 0.02 | NONE |
| deterministic_trend | `ma_quadratic_trend_531.csv` | 0.39 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.01 | 0.43 | 0.00 | NONE |
| deterministic_trend | `ma_quadratic_trend_302.csv` | 0.98 | 0.00 | 0.00 | 0.27 | 0.56 | 0.01 | 0.01 | 0.05 | 0.02 | 0.01 | NONE |
| deterministic_trend | `ma_quadratic_trend_282.csv` | 0.57 | 0.00 | 0.00 | 0.99 | 0.65 | 0.00 | 0.00 | 0.07 | 0.73 | 0.00 | NONE |
| deterministic_trend | `ma_quadratic_trend_851.csv` | 0.84 | 0.00 | 0.54 | 0.00 | 0.68 | 0.00 | 0.00 | 0.04 | 0.25 | 0.01 | NONE |
| deterministic_trend | `ma_quadratic_trend_945.csv` | 0.85 | 0.00 | 0.00 | 1.00 | 0.75 | 0.00 | 0.00 | 0.03 | 0.21 | 0.01 | NONE |
| deterministic_trend | `ma_quadratic_trend_522.csv` | 0.78 | 0.00 | 0.00 | 0.09 | 0.35 | 0.00 | 0.01 | 0.04 | 0.17 | 0.00 | NONE |
| deterministic_trend | `ma_quadratic_trend_420.csv` | 0.56 | 0.00 | 0.05 | 0.01 | 0.22 | 0.00 | 0.00 | 0.08 | 0.20 | 0.01 | NONE |
| deterministic_trend | `ma_quadratic_trend_38.csv` | 0.67 | 0.00 | 0.00 | 0.46 | 0.36 | 0.00 | 0.00 | 0.04 | 0.78 | 0.02 | NONE |
| deterministic_trend | `ma_quadratic_trend_855.csv` | 0.92 | 0.00 | 0.00 | 0.02 | 0.58 | 1.00 | 0.01 | 0.82 | 0.24 | 0.00 | NONE |
| deterministic_trend | `ma_quadratic_trend_831.csv` | 0.29 | 0.00 | 0.01 | 0.05 | 0.37 | 0.00 | 0.00 | 0.06 | 0.08 | 0.05 | NONE |
| deterministic_trend | `ma_quadratic_trend_901.csv` | 0.10 | 0.00 | 0.01 | 0.00 | 0.54 | 0.00 | 0.01 | 0.03 | 0.04 | 0.01 | NONE |
| deterministic_trend | `white_noise_cubic_trend_308.csv` | 0.05 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.93 | 0.00 | PARTIAL |
| deterministic_trend | `white_noise_cubic_trend_303.csv` | 0.03 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.95 | 0.00 | PARTIAL |
| deterministic_trend | `white_noise_cubic_trend_12.csv` | 0.01 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.62 | 0.01 | PARTIAL |
| deterministic_trend | `white_noise_cubic_trend_706.csv` | 0.04 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.98 | 0.00 | PARTIAL |
| deterministic_trend | `white_noise_cubic_trend_276.csv` | 0.10 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.62 | 0.00 | PARTIAL |
| deterministic_trend | `white_noise_cubic_trend_400.csv` | 0.10 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.73 | 0.00 | PARTIAL |
| deterministic_trend | `white_noise_cubic_trend_355.csv` | 0.01 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.98 | 0.00 | PARTIAL |
| deterministic_trend | `white_noise_cubic_trend_896.csv` | 0.02 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.58 | 0.00 | PARTIAL |
| deterministic_trend | `white_noise_cubic_trend_162.csv` | 0.04 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.76 | 0.00 | PARTIAL |
| deterministic_trend | `white_noise_cubic_trend_990.csv` | 0.62 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.09 | 0.14 | 0.27 | 0.00 | NONE |
| deterministic_trend | `white_noise_cubic_trend_810.csv` | 0.99 | 0.43 | 0.00 | 0.00 | 0.01 | 0.00 | 0.01 | 0.06 | 0.61 | 0.00 | NONE |
| deterministic_trend | `white_noise_cubic_trend_355.csv` | 0.65 | 0.05 | 0.00 | 0.00 | 0.00 | 0.00 | 0.24 | 0.17 | 0.50 | 0.00 | NONE |
| deterministic_trend | `white_noise_cubic_trend_421.csv` | 0.26 | 0.08 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.11 | 0.76 | 0.00 | NONE |
| deterministic_trend | `white_noise_cubic_trend_69.csv` | 0.89 | 0.48 | 0.00 | 0.00 | 0.00 | 0.00 | 0.13 | 0.05 | 0.89 | 0.00 | NONE |
| deterministic_trend | `white_noise_cubic_trend_568.csv` | 0.26 | 0.44 | 0.00 | 0.00 | 0.00 | 0.00 | 0.92 | 0.03 | 0.99 | 0.00 | PARTIAL |
| deterministic_trend | `white_noise_cubic_trend_467.csv` | 0.58 | 0.60 | 0.01 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.98 | 0.00 | PARTIAL |
| deterministic_trend | `white_noise_cubic_trend_724.csv` | 0.97 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.69 | 0.08 | 0.64 | 0.00 | NONE |
| deterministic_trend | `white_noise_cubic_trend_876.csv` | 0.38 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.35 | 0.07 | 0.33 | 0.00 | NONE |
| deterministic_trend | `white_noise_cubic_trend_593.csv` | 0.60 | 0.92 | 0.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.02 | 0.98 | 0.01 | PARTIAL |
| deterministic_trend | `white_noise_cubic_trend_403.csv` | 0.82 | 0.34 | 0.99 | 0.00 | 0.10 | 0.00 | 0.33 | 0.16 | 0.94 | 0.00 | NONE |
| deterministic_trend | `white_noise_cubic_trend_964.csv` | 0.00 | 0.76 | 0.00 | 0.00 | 0.06 | 0.00 | 0.03 | 0.63 | 0.75 | 0.00 | PARTIAL |
| deterministic_trend | `white_noise_cubic_trend_123.csv` | 0.60 | 0.00 | 0.99 | 0.00 | 0.03 | 0.00 | 0.11 | 0.28 | 0.19 | 0.00 | NONE |
| deterministic_trend | `white_noise_cubic_trend_204.csv` | 0.93 | 0.01 | 0.84 | 0.00 | 0.03 | 0.00 | 0.74 | 0.59 | 0.67 | 0.00 | NONE |
| deterministic_trend | `white_noise_cubic_trend_907.csv` | 0.04 | 0.00 | 0.91 | 0.00 | 0.41 | 0.00 | 0.08 | 0.66 | 0.88 | 0.00 | NONE |
| deterministic_trend | `white_noise_cubic_trend_993.csv` | 0.04 | 0.00 | 1.00 | 0.00 | 0.10 | 0.00 | 0.12 | 0.85 | 0.89 | 0.00 | NONE |
| deterministic_trend | `white_noise_cubic_trend_339.csv` | 0.17 | 0.17 | 0.93 | 0.00 | 0.01 | 0.00 | 0.17 | 0.58 | 0.79 | 0.00 | NONE |
| deterministic_trend | `white_noise_cubic_trend_262.csv` | 0.00 | 0.01 | 1.00 | 0.00 | 0.57 | 0.00 | 0.02 | 0.68 | 0.48 | 0.00 | NONE |
| deterministic_trend | `white_noise_cubic_trend_633.csv` | 0.00 | 0.02 | 0.98 | 0.00 | 0.13 | 0.00 | 0.06 | 0.57 | 0.28 | 0.00 | NONE |
| deterministic_trend | `white_noise_cubic_trend_986.csv` | 0.99 | 0.00 | 1.00 | 0.00 | 0.21 | 0.00 | 0.31 | 0.75 | 0.70 | 0.01 | NONE |
| deterministic_trend | `white_noise_damped_trend_10.csv` | 0.00 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.15 | 0.26 | 0.02 | 0.01 | NONE |
| deterministic_trend | `white_noise_exponential_trend_716.csv` | 0.99 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.95 | 0.00 | NONE |
| deterministic_trend | `white_noise_exponential_trend_28.csv` | 0.98 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.92 | 0.01 | NONE |
| deterministic_trend | `white_noise_exponential_trend_496.csv` | 0.98 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.81 | 0.01 | NONE |
| deterministic_trend | `white_noise_exponential_trend_947.csv` | 0.98 | 0.90 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.97 | 0.00 | NONE |
| deterministic_trend | `white_noise_exponential_trend_388.csv` | 0.96 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.98 | 0.01 | NONE |
| deterministic_trend | `white_noise_exponential_trend_71.csv` | 0.98 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.98 | 0.01 | NONE |
| deterministic_trend | `white_noise_exponential_trend_880.csv` | 1.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.01 | 0.05 | 0.99 | 0.00 | NONE |
| deterministic_trend | `white_noise_exponential_trend_375.csv` | 0.98 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.06 | 0.99 | 0.00 | NONE |
| deterministic_trend | `white_noise_exponential_trend_566.csv` | 0.63 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.98 | 0.02 | NONE |
| deterministic_trend | `white_noise_exponential_trend_383.csv` | 0.95 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.94 | 0.02 | NONE |
| deterministic_trend | `white_noise_exponential_trend_475.csv` | 0.35 | 0.00 | 0.63 | 0.00 | 0.00 | 0.00 | 0.46 | 0.10 | 0.95 | 0.01 | NONE |
| deterministic_trend | `white_noise_exponential_trend_4.csv` | 0.02 | 0.00 | 1.00 | 0.00 | 0.01 | 0.00 | 0.49 | 0.13 | 0.36 | 0.01 | NONE |
| deterministic_trend | `white_noise_exponential_trend_47.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.01 | 0.00 | 0.34 | 0.08 | 0.30 | 0.01 | NONE |
| deterministic_trend | `white_noise_exponential_trend_740.csv` | 0.05 | 0.00 | 0.73 | 0.00 | 0.00 | 0.00 | 0.60 | 0.10 | 0.85 | 0.01 | NONE |
| deterministic_trend | `white_noise_exponential_trend_609.csv` | 0.15 | 0.00 | 0.97 | 0.00 | 0.01 | 0.00 | 0.54 | 0.07 | 0.85 | 0.00 | NONE |
| deterministic_trend | `white_noise_exponential_trend_215.csv` | 0.03 | 0.00 | 0.96 | 0.00 | 0.01 | 0.00 | 0.52 | 0.09 | 0.56 | 0.00 | NONE |
| deterministic_trend | `white_noise_exponential_trend_275.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.01 | 0.00 | 0.39 | 0.08 | 0.32 | 0.01 | NONE |
| deterministic_trend | `white_noise_exponential_trend_486.csv` | 0.04 | 0.00 | 0.66 | 0.00 | 0.00 | 0.00 | 0.41 | 0.11 | 0.77 | 0.00 | NONE |
| deterministic_trend | `white_noise_linear_down_trend_710.csv` | 0.50 | 0.01 | 0.04 | 0.00 | 0.00 | 0.00 | 0.74 | 0.01 | 0.01 | 0.03 | NONE |
| deterministic_trend | `white_noise_linear_down_trend_965.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.98 | 0.01 | NONE |
| deterministic_trend | `white_noise_linear_down_trend_448.csv` | 0.99 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.98 | 0.01 | NONE |
| deterministic_trend | `white_noise_linear_down_trend_722.csv` | 0.99 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.97 | 0.02 | NONE |
| deterministic_trend | `white_noise_linear_down_trend_789.csv` | 0.98 | 0.08 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.93 | 0.01 | NONE |
| deterministic_trend | `white_noise_linear_down_trend_930.csv` | 0.89 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.96 | 0.01 | NONE |
| deterministic_trend | `white_noise_linear_down_trend_259.csv` | 0.98 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.95 | 0.01 | NONE |
| deterministic_trend | `white_noise_linear_down_trend_666.csv` | 0.99 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.89 | 0.01 | NONE |
| deterministic_trend | `white_noise_linear_down_trend_622.csv` | 0.99 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.98 | 0.01 | NONE |
| deterministic_trend | `white_noise_linear_down_trend_376.csv` | 0.71 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.68 | 0.02 | NONE |
| deterministic_trend | `white_noise_linear_down_trend_472.csv` | 0.98 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.15 | 1.00 | 0.00 | NONE |
| deterministic_trend | `white_noise_linear_down_trend_603.csv` | 0.98 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.88 | 0.04 | 0.49 | 0.95 | NONE |
| deterministic_trend | `white_noise_linear_down_trend_867.csv` | 0.99 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.81 | 0.08 | 0.98 | 0.00 | NONE |
| deterministic_trend | `white_noise_linear_down_trend_1.csv` | 0.98 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.13 | 1.00 | 0.00 | NONE |
| deterministic_trend | `white_noise_linear_down_trend_379.csv` | 0.89 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.52 | 0.10 | 0.98 | 0.00 | NONE |
| deterministic_trend | `white_noise_linear_down_trend_362.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.16 | 1.00 | 0.00 | NONE |
| deterministic_trend | `white_noise_linear_down_trend_292.csv` | 0.99 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.18 | 1.00 | 0.00 | NONE |
| deterministic_trend | `white_noise_linear_down_trend_495.csv` | 0.99 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.13 | 1.00 | 0.00 | NONE |
| deterministic_trend | `white_noise_linear_down_trend_822.csv` | 0.94 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.09 | 0.99 | 0.00 | NONE |
| deterministic_trend | `white_noise_linear_down_trend_632.csv` | 0.95 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.09 | 0.99 | 0.02 | NONE |
| deterministic_trend | `white_noise_linear_down_trend_658.csv` | 0.69 | 0.00 | 0.04 | 0.00 | 0.00 | 0.00 | 0.21 | 0.33 | 0.98 | 0.00 | NONE |
| deterministic_trend | `white_noise_linear_down_trend_701.csv` | 0.84 | 0.00 | 0.98 | 0.00 | 0.00 | 0.00 | 0.36 | 0.50 | 0.99 | 0.00 | NONE |
| deterministic_trend | `white_noise_linear_down_trend_395.csv` | 0.02 | 0.00 | 1.00 | 0.00 | 0.05 | 0.00 | 0.27 | 0.51 | 0.96 | 0.01 | NONE |
| deterministic_trend | `white_noise_linear_down_trend_527.csv` | 0.55 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.18 | 0.13 | 0.86 | 0.00 | NONE |
| deterministic_trend | `white_noise_linear_down_trend_505.csv` | 0.53 | 0.00 | 0.85 | 0.00 | 0.72 | 0.00 | 0.35 | 0.38 | 0.83 | 0.00 | NONE |
| deterministic_trend | `white_noise_linear_down_trend_720.csv` | 0.25 | 0.00 | 0.30 | 0.00 | 0.01 | 0.00 | 0.21 | 0.12 | 0.66 | 0.00 | NONE |
| deterministic_trend | `white_noise_linear_down_trend_295.csv` | 0.04 | 0.01 | 0.98 | 0.00 | 0.00 | 0.00 | 0.06 | 0.23 | 0.73 | 0.00 | NONE |
| deterministic_trend | `white_noise_linear_down_trend_57.csv` | 0.98 | 0.00 | 0.97 | 0.00 | 0.00 | 0.00 | 0.14 | 0.40 | 1.00 | 0.00 | NONE |
| deterministic_trend | `white_noise_linear_down_trend_534.csv` | 1.00 | 0.00 | 0.15 | 0.00 | 0.01 | 0.00 | 0.46 | 0.27 | 1.00 | 0.01 | NONE |
| deterministic_trend | `white_noise_linear_down_trend_83.csv` | 0.04 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.42 | 0.07 | 0.64 | 0.00 | NONE |
| deterministic_trend | `white_noise_linear_up_trend_929.csv` | 0.44 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.56 | 0.01 | NONE |
| deterministic_trend | `white_noise_linear_up_trend_983.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.99 | 0.00 | NONE |
| deterministic_trend | `white_noise_linear_up_trend_832.csv` | 0.96 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.63 | 0.00 | 0.01 | 0.06 | NONE |
| deterministic_trend | `white_noise_linear_up_trend_777.csv` | 0.64 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.92 | 0.01 | NONE |
| deterministic_trend | `white_noise_linear_up_trend_254.csv` | 0.98 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.88 | 0.00 | 0.00 | 0.55 | NONE |
| deterministic_trend | `white_noise_linear_up_trend_705.csv` | 0.99 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.95 | 0.01 | NONE |
| deterministic_trend | `white_noise_linear_up_trend_176.csv` | 0.99 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.93 | 0.01 | NONE |
| deterministic_trend | `white_noise_linear_up_trend_36.csv` | 0.94 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.74 | 0.01 | 0.05 | 0.02 | NONE |
| deterministic_trend | `white_noise_linear_up_trend_573.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.96 | 0.01 | NONE |
| deterministic_trend | `white_noise_linear_up_trend_71.csv` | 0.76 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.80 | 0.03 | NONE |
| deterministic_trend | `white_noise_linear_up_trend_682.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.05 | 1.00 | 0.00 | NONE |
| deterministic_trend | `white_noise_linear_up_trend_67.csv` | 1.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.02 | 0.06 | 1.00 | 0.01 | NONE |
| deterministic_trend | `white_noise_linear_up_trend_407.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.87 | 0.05 | 0.95 | 0.00 | NONE |
| deterministic_trend | `white_noise_linear_up_trend_184.csv` | 1.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.67 | 0.04 | 0.99 | 0.01 | NONE |
| deterministic_trend | `white_noise_linear_up_trend_853.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.92 | 0.01 | 0.96 | 0.03 | NONE |
| deterministic_trend | `white_noise_linear_up_trend_976.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.08 | 1.00 | 0.00 | NONE |
| deterministic_trend | `white_noise_linear_up_trend_791.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.05 | 1.00 | 0.00 | NONE |
| deterministic_trend | `white_noise_linear_up_trend_314.csv` | 1.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.01 | 0.04 | 1.00 | 0.00 | NONE |
| deterministic_trend | `white_noise_linear_up_trend_718.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.06 | 1.00 | 0.00 | NONE |
| deterministic_trend | `white_noise_linear_up_trend_384.csv` | 0.94 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.05 | 0.99 | 0.00 | NONE |
| deterministic_trend | `white_noise_linear_up_trend_305.csv` | 0.01 | 0.00 | 0.50 | 0.00 | 0.02 | 0.00 | 0.94 | 0.15 | 0.88 | 0.00 | NONE |
| deterministic_trend | `white_noise_linear_up_trend_841.csv` | 0.48 | 0.00 | 0.33 | 0.00 | 0.02 | 0.00 | 0.77 | 0.19 | 0.98 | 0.00 | NONE |
| deterministic_trend | `white_noise_linear_up_trend_281.csv` | 0.30 | 0.00 | 0.87 | 0.00 | 0.00 | 0.00 | 0.80 | 0.36 | 0.95 | 0.00 | NONE |
| deterministic_trend | `white_noise_linear_up_trend_233.csv` | 0.42 | 0.00 | 1.00 | 0.00 | 0.14 | 0.00 | 0.81 | 0.45 | 0.97 | 0.00 | NONE |
| deterministic_trend | `white_noise_linear_up_trend_120.csv` | 0.94 | 0.00 | 0.60 | 0.00 | 0.01 | 0.00 | 0.81 | 0.36 | 0.98 | 0.00 | NONE |
| deterministic_trend | `white_noise_linear_up_trend_140.csv` | 0.85 | 0.00 | 0.94 | 0.00 | 0.01 | 0.00 | 0.79 | 0.30 | 0.99 | 0.00 | NONE |
| deterministic_trend | `white_noise_linear_up_trend_323.csv` | 0.34 | 0.00 | 0.40 | 0.00 | 0.00 | 0.00 | 0.84 | 0.21 | 0.92 | 0.00 | NONE |
| deterministic_trend | `white_noise_linear_up_trend_536.csv` | 0.17 | 0.00 | 0.99 | 0.00 | 0.03 | 0.00 | 0.87 | 0.30 | 0.85 | 0.00 | NONE |
| deterministic_trend | `white_noise_linear_up_trend_661.csv` | 0.81 | 0.00 | 1.00 | 0.00 | 0.73 | 0.00 | 0.94 | 0.17 | 0.95 | 0.00 | NONE |
| deterministic_trend | `white_noise_linear_up_trend_882.csv` | 0.94 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.95 | 0.20 | 0.99 | 0.00 | NONE |
| deterministic_trend | `white_noise_quadratic_trend_806.csv` | 0.31 | 0.00 | 0.00 | 0.00 | 0.22 | 0.00 | 0.01 | 0.02 | 0.00 | 0.00 | NONE |
| deterministic_trend | `white_noise_quadratic_trend_165.csv` | 0.65 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | NONE |
| deterministic_trend | `white_noise_quadratic_trend_518.csv` | 0.80 | 0.00 | 0.00 | 0.00 | 0.91 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | NONE |
| deterministic_trend | `white_noise_quadratic_trend_480.csv` | 0.22 | 0.12 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.58 | 0.00 | 0.01 | NONE |
| deterministic_trend | `white_noise_quadratic_trend_915.csv` | 0.19 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | NONE |
| deterministic_trend | `white_noise_quadratic_trend_679.csv` | 0.65 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.72 | 0.00 | 0.01 | NONE |
| deterministic_trend | `white_noise_quadratic_trend_629.csv` | 0.99 | 0.00 | 0.00 | 0.00 | 0.23 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | NONE |
| deterministic_trend | `white_noise_quadratic_trend_278.csv` | 0.38 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | NONE |
| deterministic_trend | `white_noise_quadratic_trend_760.csv` | 0.46 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.03 | 0.00 | 0.01 | NONE |
| deterministic_trend | `white_noise_quadratic_trend_740.csv` | 0.67 | 0.00 | 0.00 | 0.00 | 0.01 | 0.93 | 0.01 | 0.63 | 0.01 | 0.01 | NONE |
| deterministic_trend | `white_noise_quadratic_trend_452.csv` | 0.60 | 0.03 | 0.00 | 0.00 | 0.05 | 0.91 | 0.00 | 0.94 | 0.55 | 0.00 | NONE |
| deterministic_trend | `white_noise_quadratic_trend_554.csv` | 0.82 | 0.06 | 0.00 | 0.00 | 0.99 | 0.28 | 0.00 | 0.81 | 0.42 | 0.00 | NONE |
| deterministic_trend | `white_noise_quadratic_trend_467.csv` | 0.91 | 0.00 | 0.00 | 0.00 | 1.00 | 0.17 | 0.00 | 0.01 | 0.05 | 0.00 | NONE |
| deterministic_trend | `white_noise_quadratic_trend_322.csv` | 0.61 | 0.02 | 0.00 | 0.00 | 0.06 | 0.94 | 0.01 | 0.71 | 0.11 | 0.01 | NONE |
| deterministic_trend | `white_noise_quadratic_trend_234.csv` | 0.63 | 0.01 | 0.00 | 0.00 | 1.00 | 0.00 | 0.01 | 0.00 | 0.01 | 0.00 | NONE |
| deterministic_trend | `white_noise_quadratic_trend_702.csv` | 0.39 | 0.00 | 0.00 | 0.00 | 0.99 | 0.00 | 0.01 | 0.62 | 0.04 | 0.01 | NONE |
| deterministic_trend | `white_noise_quadratic_trend_732.csv` | 0.45 | 0.03 | 0.00 | 0.00 | 0.31 | 0.92 | 0.01 | 0.74 | 0.19 | 0.00 | NONE |
| deterministic_trend | `white_noise_quadratic_trend_102.csv` | 0.88 | 0.06 | 0.00 | 0.00 | 0.04 | 0.76 | 0.00 | 0.95 | 0.44 | 0.00 | NONE |
| deterministic_trend | `white_noise_quadratic_trend_921.csv` | 0.43 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 | 0.02 | 0.03 | 0.12 | 0.01 | NONE |
| deterministic_trend | `white_noise_quadratic_trend_790.csv` | 0.30 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 | 0.01 | 0.10 | 0.13 | 0.00 | NONE |
| deterministic_trend | `white_noise_quadratic_trend_892.csv` | 0.52 | 0.00 | 0.00 | 0.00 | 0.29 | 0.00 | 0.00 | 0.10 | 0.61 | 0.00 | NONE |
| deterministic_trend | `white_noise_quadratic_trend_808.csv` | 0.87 | 0.02 | 0.00 | 0.01 | 0.51 | 0.01 | 0.00 | 0.92 | 0.10 | 0.00 | NONE |
| deterministic_trend | `white_noise_quadratic_trend_914.csv` | 0.99 | 0.00 | 0.00 | 0.63 | 0.72 | 1.00 | 0.01 | 0.05 | 0.19 | 0.03 | NONE |
| deterministic_trend | `white_noise_quadratic_trend_197.csv` | 0.94 | 0.09 | 0.00 | 0.00 | 0.95 | 0.02 | 0.00 | 0.89 | 0.02 | 0.00 | NONE |
| deterministic_trend | `white_noise_quadratic_trend_816.csv` | 0.99 | 0.00 | 0.00 | 0.77 | 0.58 | 1.00 | 0.00 | 0.11 | 0.21 | 0.00 | NONE |
| deterministic_trend | `white_noise_quadratic_trend_490.csv` | 0.99 | 0.00 | 0.00 | 0.04 | 0.57 | 1.00 | 0.01 | 0.04 | 0.36 | 0.01 | NONE |
| deterministic_trend | `white_noise_quadratic_trend_30.csv` | 0.99 | 0.00 | 0.00 | 0.00 | 0.65 | 1.00 | 0.01 | 0.14 | 0.39 | 0.01 | NONE |
| deterministic_trend | `white_noise_quadratic_trend_260.csv` | 0.60 | 0.00 | 0.00 | 0.02 | 0.43 | 1.00 | 0.01 | 0.82 | 0.36 | 0.00 | NONE |
| deterministic_trend | `white_noise_quadratic_trend_84.csv` | 0.79 | 0.00 | 0.00 | 0.01 | 0.34 | 0.09 | 0.01 | 0.81 | 0.13 | 0.00 | NONE |
| deterministic_trend | `white_noise_quadratic_trend_981.csv` | 1.00 | 0.01 | 0.00 | 0.01 | 0.74 | 0.15 | 0.01 | 0.81 | 0.09 | 0.00 | NONE |
| stochastic_trend | `ari_74.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.98 | PARTIAL |
| stochastic_trend | `ari_576.csv` | 0.01 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.14 | 0.92 | PARTIAL |
| stochastic_trend | `ari_526.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.91 | PARTIAL |
| stochastic_trend | `ari_144.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.78 | PARTIAL |
| stochastic_trend | `ari_611.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.55 | PARTIAL |
| stochastic_trend | `ari_328.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.98 | PARTIAL |
| stochastic_trend | `ari_944.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.74 | PARTIAL |
| stochastic_trend | `ari_880.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.87 | PARTIAL |
| stochastic_trend | `ari_21.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.79 | PARTIAL |
| stochastic_trend | `ari_519.csv` | 0.01 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.83 | PARTIAL |
| stochastic_trend | `ari_713.csv` | 0.98 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.86 | 0.01 | 0.67 | 0.03 | NONE |
| stochastic_trend | `ari_588.csv` | 0.88 | 0.00 | 0.78 | 0.00 | 0.00 | 0.00 | 0.02 | 0.03 | 0.22 | 0.00 | NONE |
| stochastic_trend | `ari_647.csv` | 0.94 | 0.00 | 1.00 | 0.00 | 0.10 | 0.00 | 0.76 | 0.12 | 0.79 | 0.01 | PARTIAL |
| stochastic_trend | `ari_974.csv` | 0.79 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.04 | 0.80 | 0.04 | PARTIAL |
| stochastic_trend | `ari_795.csv` | 1.00 | 0.00 | 0.97 | 0.00 | 0.63 | 0.00 | 0.99 | 0.02 | 0.28 | 0.02 | NONE |
| stochastic_trend | `ari_92.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.72 | 0.01 | 0.21 | 0.00 | PARTIAL |
| stochastic_trend | `ari_663.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.79 | 0.01 | 0.02 | 0.01 | PARTIAL |
| stochastic_trend | `ari_85.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.77 | 0.01 | 0.04 | 0.00 | PARTIAL |
| stochastic_trend | `ari_761.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.01 | 0.00 | 0.92 | 0.00 | 0.01 | 0.01 | PARTIAL |
| stochastic_trend | `ari_920.csv` | 0.29 | 0.00 | 0.99 | 0.00 | 0.44 | 0.00 | 0.05 | 0.80 | 0.67 | 0.02 | PARTIAL |
| stochastic_trend | `ari_491.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.01 | 0.00 | 0.85 | 0.01 | 0.00 | 0.02 | PARTIAL |
| stochastic_trend | `ari_864.csv` | 0.16 | 0.00 | 1.00 | 0.00 | 0.02 | 0.00 | 0.08 | 0.41 | 0.66 | 0.02 | PARTIAL |
| stochastic_trend | `ari_934.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.01 | 0.00 | 0.76 | 0.00 | 0.01 | 0.01 | PARTIAL |
| stochastic_trend | `arima_509.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.80 | PARTIAL |
| stochastic_trend | `arima_925.csv` | 0.01 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.01 | 0.81 | PARTIAL |
| stochastic_trend | `arima_244.csv` | 0.01 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.10 | 0.77 | PARTIAL |
| stochastic_trend | `arima_784.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.92 | PARTIAL |
| stochastic_trend | `arima_893.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.89 | PARTIAL |
| stochastic_trend | `arima_536.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.85 | PARTIAL |
| stochastic_trend | `arima_337.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.92 | PARTIAL |
| stochastic_trend | `arima_791.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.90 | PARTIAL |
| stochastic_trend | `arima_326.csv` | 0.01 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.71 | 0.11 | PARTIAL |
| stochastic_trend | `arima_686.csv` | 0.94 | 0.00 | 0.57 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.01 | NONE |
| stochastic_trend | `arima_353.csv` | 0.28 | 0.00 | 1.00 | 0.00 | 0.19 | 0.00 | 0.15 | 0.05 | 0.01 | 0.55 | PARTIAL |
| stochastic_trend | `arima_804.csv` | 0.01 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.99 | 0.03 | PARTIAL |
| stochastic_trend | `arima_676.csv` | 0.90 | 0.00 | 0.89 | 0.00 | 0.01 | 0.00 | 0.73 | 0.03 | 0.09 | 0.02 | NONE |
| stochastic_trend | `arima_503.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.10 | 0.00 | 0.91 | 0.13 | 0.08 | 0.00 | PARTIAL |
| stochastic_trend | `arima_17.csv` | 0.82 | 0.00 | 1.00 | 0.00 | 0.28 | 0.00 | 0.45 | 0.83 | 0.77 | 0.01 | PARTIAL |
| stochastic_trend | `arima_756.csv` | 0.01 | 0.00 | 1.00 | 0.00 | 0.01 | 0.00 | 0.55 | 0.02 | 0.51 | 0.02 | PARTIAL |
| stochastic_trend | `arima_361.csv` | 0.17 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.01 | 0.82 | 0.02 | PARTIAL |
| stochastic_trend | `arima_314.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.93 | 0.00 | 0.93 | 0.01 | 0.01 | 0.04 | PARTIAL |
| stochastic_trend | `arima_349.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.17 | 0.00 | 0.88 | 0.01 | 0.01 | 0.00 | PARTIAL |
| stochastic_trend | `arima_407.csv` | 0.08 | 0.00 | 1.00 | 0.00 | 0.96 | 0.00 | 0.23 | 0.35 | 0.05 | 0.01 | PARTIAL |
| stochastic_trend | `arima_921.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.01 | 0.00 | 0.64 | 0.01 | 0.02 | 0.01 | PARTIAL |
| stochastic_trend | `ima_597.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.96 | PARTIAL |
| stochastic_trend | `ima_172.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.84 | PARTIAL |
| stochastic_trend | `ima_225.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.94 | PARTIAL |
| stochastic_trend | `ima_237.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.91 | PARTIAL |
| stochastic_trend | `ima_310.csv` | 0.98 | 0.00 | 0.95 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.24 | 0.37 | NONE |
| stochastic_trend | `ima_451.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.97 | PARTIAL |
| stochastic_trend | `ima_239.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.66 | PARTIAL |
| stochastic_trend | `ima_75.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.85 | PARTIAL |
| stochastic_trend | `ima_296.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.90 | PARTIAL |
| stochastic_trend | `ima_157.csv` | 0.01 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.78 | PARTIAL |
| stochastic_trend | `ima_528.csv` | 1.00 | 0.00 | 0.00 | 0.71 | 0.34 | 0.00 | 0.95 | 0.88 | 0.00 | 0.76 | NONE |
| stochastic_trend | `ima_289.csv` | 1.00 | 0.00 | 0.00 | 0.99 | 0.30 | 0.00 | 0.95 | 0.34 | 0.02 | 0.18 | NONE |
| stochastic_trend | `ima_486.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.01 | 0.00 | 0.67 | 0.00 | 0.12 | 0.00 | PARTIAL |
| stochastic_trend | `ima_457.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.50 | 0.00 | 0.68 | 0.05 | 0.00 | 0.02 | PARTIAL |
| stochastic_trend | `ima_932.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.01 | 0.00 | 0.86 | 0.01 | 0.03 | 0.01 | PARTIAL |
| stochastic_trend | `ima_808.csv` | 0.03 | 0.02 | 1.00 | 0.00 | 0.00 | 0.00 | 0.10 | 0.02 | 0.50 | 0.00 | PARTIAL |
| stochastic_trend | `ima_637.csv` | 0.18 | 0.00 | 1.00 | 0.00 | 0.70 | 0.00 | 0.80 | 0.56 | 0.01 | 0.04 | PARTIAL |
| stochastic_trend | `ima_74.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.43 | 0.00 | 0.82 | 0.01 | 0.01 | 0.04 | PARTIAL |
| stochastic_trend | `ima_116.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.42 | 0.00 | 0.78 | 0.41 | 0.35 | 0.03 | PARTIAL |
| stochastic_trend | `ima_889.csv` | 0.01 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.62 | 0.00 | 0.05 | 0.01 | PARTIAL |
| stochastic_trend | `ima_91.csv` | 0.39 | 0.00 | 1.00 | 0.00 | 0.98 | 0.00 | 0.29 | 0.21 | 0.03 | 0.03 | PARTIAL |
| stochastic_trend | `random_walk_803.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.95 | PARTIAL |
| stochastic_trend | `random_walk_629.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.92 | PARTIAL |
| stochastic_trend | `random_walk_449.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.94 | PARTIAL |
| stochastic_trend | `random_walk_538.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.97 | PARTIAL |
| stochastic_trend | `random_walk_103.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.96 | PARTIAL |
| stochastic_trend | `random_walk_968.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.87 | PARTIAL |
| stochastic_trend | `random_walk_422.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.98 | PARTIAL |
| stochastic_trend | `random_walk_373.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.86 | PARTIAL |
| stochastic_trend | `random_walk_793.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.92 | PARTIAL |
| stochastic_trend | `random_walk_458.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.98 | PARTIAL |
| stochastic_trend | `random_walk_595.csv` | 0.35 | 0.00 | 1.00 | 0.00 | 0.02 | 0.00 | 0.01 | 0.01 | 0.09 | 0.62 | PARTIAL |
| stochastic_trend | `random_walk_788.csv` | 0.12 | 0.00 | 1.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.66 | PARTIAL |
| stochastic_trend | `random_walk_601.csv` | 0.03 | 0.00 | 1.00 | 0.00 | 0.18 | 0.00 | 0.07 | 0.01 | 0.00 | 0.57 | PARTIAL |
| stochastic_trend | `random_walk_654.csv` | 0.01 | 0.00 | 1.00 | 0.00 | 0.99 | 0.00 | 0.67 | 0.06 | 0.02 | 0.01 | PARTIAL |
| stochastic_trend | `random_walk_926.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.66 | 0.00 | 0.58 | 0.02 | 0.00 | 0.00 | PARTIAL |
| stochastic_trend | `random_walk_300.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.13 | 0.00 | 0.52 | 0.01 | 0.00 | 0.00 | PARTIAL |
| stochastic_trend | `random_walk_30.csv` | 0.01 | 0.00 | 1.00 | 0.00 | 0.99 | 0.00 | 0.26 | 0.59 | 0.00 | 0.00 | PARTIAL |
| stochastic_trend | `random_walk_35.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.98 | 0.00 | 0.89 | 0.48 | 0.00 | 0.01 | PARTIAL |
| stochastic_trend | `random_walk_50.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.99 | 0.00 | 0.46 | 0.12 | 0.00 | 0.01 | PARTIAL |
| stochastic_trend | `random_walk_546.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.94 | 0.00 | 0.98 | 0.00 | 0.00 | 0.02 | PARTIAL |
| stochastic_trend | `random_walk_124.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.40 | 0.00 | 0.88 | 0.01 | 0.01 | 0.02 | PARTIAL |
| stochastic_trend | `random_walk_457.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.04 | 0.00 | 0.90 | 0.03 | 0.01 | 0.00 | PARTIAL |
| stochastic_trend | `random_walk_drift_408.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.83 | PARTIAL |
| stochastic_trend | `random_walk_drift_714.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.88 | PARTIAL |
| stochastic_trend | `random_walk_drift_724.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.93 | PARTIAL |
| stochastic_trend | `random_walk_drift_834.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.90 | PARTIAL |
| stochastic_trend | `random_walk_drift_471.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.88 | PARTIAL |
| stochastic_trend | `random_walk_drift_766.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.97 | PARTIAL |
| stochastic_trend | `random_walk_drift_250.csv` | 0.02 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.94 | PARTIAL |
| stochastic_trend | `random_walk_drift_873.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.89 | PARTIAL |
| stochastic_trend | `random_walk_drift_529.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.89 | PARTIAL |
| stochastic_trend | `random_walk_drift_946.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.95 | PARTIAL |
| stochastic_trend | `random_walk_drift_461.csv` | 0.08 | 0.00 | 1.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.77 | PARTIAL |
| stochastic_trend | `random_walk_drift_644.csv` | 0.04 | 0.00 | 1.00 | 0.00 | 0.76 | 0.00 | 0.63 | 0.00 | 0.01 | 0.78 | PARTIAL |
| stochastic_trend | `random_walk_drift_709.csv` | 0.83 | 0.00 | 1.00 | 0.00 | 0.71 | 0.00 | 0.96 | 0.02 | 0.00 | 0.68 | PARTIAL |
| stochastic_trend | `random_walk_drift_175.csv` | 0.05 | 0.00 | 1.00 | 0.00 | 0.19 | 0.00 | 0.07 | 0.01 | 0.01 | 0.60 | PARTIAL |
| stochastic_trend | `random_walk_drift_691.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.97 | 0.00 | 0.48 | 0.08 | 0.00 | 0.01 | PARTIAL |
| stochastic_trend | `random_walk_drift_493.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.73 | 0.00 | 0.69 | 0.03 | 0.00 | 0.01 | PARTIAL |
| stochastic_trend | `random_walk_drift_222.csv` | 0.03 | 0.00 | 1.00 | 0.00 | 0.96 | 0.00 | 0.87 | 0.03 | 0.00 | 0.00 | PARTIAL |
| stochastic_trend | `random_walk_drift_898.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.02 | 0.00 | 0.98 | 0.03 | 0.00 | 0.00 | PARTIAL |
| stochastic_trend | `random_walk_drift_523.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.81 | 0.00 | 0.96 | 0.01 | 0.00 | 0.00 | PARTIAL |
| stochastic_trend | `random_walk_drift_266.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.99 | 0.00 | 0.83 | 0.15 | 0.01 | 0.01 | PARTIAL |
| stochastic_trend | `random_walk_drift_144.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.11 | 0.00 | 0.98 | 0.01 | 0.01 | 0.00 | PARTIAL |
| stochastic_trend | `random_walk_drift_338.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.51 | 0.00 | 0.91 | 0.07 | 0.24 | 0.00 | PARTIAL |
| stochastic_trend | `random_walk_drift_448.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.45 | 0.00 | 0.97 | 0.01 | 0.00 | 0.00 | PARTIAL |
| stochastic_trend | `random_walk_drift_40.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.88 | 0.00 | 0.95 | 0.01 | 0.01 | 0.01 | PARTIAL |
| volatility | `aparch_792.csv` | 0.01 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.95 | PARTIAL |
| volatility | `aparch_865.csv` | 0.54 | 0.00 | 0.00 | 1.00 | 0.01 | 0.00 | 0.02 | 0.09 | 0.00 | 0.94 | PARTIAL |
| volatility | `aparch_868.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.17 | 0.00 | 0.48 | 0.56 | 0.00 | 0.92 | NONE |
| volatility | `aparch_173.csv` | 0.93 | 0.00 | 0.00 | 1.00 | 0.02 | 0.00 | 0.11 | 0.23 | 0.01 | 0.51 | PARTIAL |
| volatility | `aparch_531.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.23 | 0.00 | 0.04 | 0.29 | 0.00 | 0.86 | PARTIAL |
| volatility | `aparch_79.csv` | 0.80 | 0.00 | 0.00 | 1.00 | 0.02 | 0.00 | 0.00 | 0.25 | 0.00 | 0.95 | PARTIAL |
| volatility | `aparch_596.csv` | 0.70 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 1.00 | PARTIAL |
| volatility | `aparch_146.csv` | 0.40 | 0.00 | 0.00 | 1.00 | 0.01 | 0.00 | 0.02 | 0.06 | 0.00 | 0.92 | PARTIAL |
| volatility | `aparch_976.csv` | 0.93 | 0.00 | 0.00 | 1.00 | 0.88 | 0.00 | 0.02 | 0.08 | 0.02 | 0.90 | PARTIAL |
| volatility | `aparch_420.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 1.00 | 0.00 | 0.16 | 0.31 | 0.06 | 0.28 | PARTIAL |
| volatility | `aparch_304.csv` | 0.02 | 0.00 | 0.00 | 1.00 | 0.67 | 0.00 | 0.44 | 0.57 | 0.01 | 0.10 | PARTIAL |
| volatility | `aparch_698.csv` | 0.94 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.06 | 0.48 | 0.24 | 0.09 | PARTIAL |
| volatility | `aparch_161.csv` | 0.60 | 0.00 | 0.00 | 1.00 | 0.57 | 0.00 | 0.11 | 0.36 | 0.13 | 0.66 | PARTIAL |
| volatility | `aparch_818.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.93 | 0.00 | 0.37 | 0.42 | 0.71 | 0.02 | PARTIAL |
| volatility | `aparch_981.csv` | 0.26 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.03 | 0.08 | 0.32 | 0.93 | PARTIAL |
| volatility | `aparch_7.csv` | 0.90 | 0.00 | 0.00 | 1.00 | 0.83 | 0.00 | 0.03 | 0.95 | 0.02 | 0.17 | PARTIAL |
| volatility | `aparch_135.csv` | 0.89 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.03 | 0.62 | 0.05 | 0.03 | PARTIAL |
| volatility | `aparch_794.csv` | 0.61 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.19 | 0.34 | 0.31 | 0.02 | PARTIAL |
| volatility | `arch_326.csv` | 0.82 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.68 | PARTIAL |
| volatility | `arch_715.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.03 | 0.00 | 0.84 | 0.06 | 0.01 | 0.36 | PARTIAL |
| volatility | `arch_972.csv` | 0.80 | 0.00 | 0.00 | 1.00 | 0.02 | 0.00 | 0.00 | 0.01 | 0.01 | 0.97 | PARTIAL |
| volatility | `arch_334.csv` | 0.39 | 0.00 | 0.00 | 1.00 | 0.02 | 0.00 | 0.01 | 0.05 | 0.00 | 0.95 | PARTIAL |
| volatility | `arch_805.csv` | 0.81 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.01 | 0.02 | 0.00 | 0.55 | PARTIAL |
| volatility | `arch_438.csv` | 0.49 | 0.00 | 0.00 | 1.00 | 0.15 | 0.00 | 0.22 | 0.75 | 0.00 | 0.03 | PARTIAL |
| volatility | `arch_252.csv` | 0.64 | 0.00 | 0.00 | 1.00 | 0.93 | 0.00 | 0.00 | 0.39 | 0.00 | 0.56 | PARTIAL |
| volatility | `arch_657.csv` | 0.01 | 0.00 | 0.00 | 1.00 | 0.73 | 0.00 | 0.03 | 0.47 | 0.00 | 0.68 | PARTIAL |
| volatility | `arch_658.csv` | 0.59 | 0.00 | 0.00 | 1.00 | 0.97 | 0.00 | 0.09 | 0.40 | 0.02 | 0.74 | PARTIAL |
| volatility | `arch_987.csv` | 0.43 | 0.00 | 0.00 | 1.00 | 0.47 | 0.00 | 0.03 | 0.94 | 0.00 | 0.13 | PARTIAL |
| volatility | `arch_788.csv` | 0.00 | 0.00 | 0.02 | 1.00 | 0.06 | 0.00 | 0.74 | 0.28 | 0.02 | 0.88 | PARTIAL |
| volatility | `arch_760.csv` | 0.12 | 0.00 | 0.00 | 1.00 | 0.85 | 0.00 | 0.08 | 0.45 | 0.00 | 0.80 | PARTIAL |
| volatility | `arch_203.csv` | 0.29 | 0.00 | 0.00 | 1.00 | 0.46 | 0.00 | 0.01 | 0.93 | 0.00 | 0.45 | PARTIAL |
| volatility | `arch_815.csv` | 0.00 | 0.00 | 0.00 | 1.00 | 0.50 | 0.00 | 0.03 | 0.97 | 0.00 | 0.24 | PARTIAL |
| volatility | `arch_853.csv` | 0.17 | 0.00 | 0.00 | 1.00 | 0.56 | 0.00 | 0.04 | 0.46 | 0.01 | 0.37 | PARTIAL |
| volatility | `egarch_249.csv` | 0.98 | 0.00 | 0.00 | 0.99 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.59 | PARTIAL |
| volatility | `egarch_935.csv` | 0.94 | 0.00 | 0.00 | 1.00 | 0.02 | 0.00 | 0.03 | 0.08 | 0.00 | 0.99 | PARTIAL |
| volatility | `egarch_464.csv` | 0.76 | 0.00 | 0.00 | 1.00 | 0.02 | 0.00 | 0.00 | 0.13 | 0.00 | 0.55 | PARTIAL |
| volatility | `egarch_967.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.56 | 0.00 | 0.97 | 0.31 | 0.00 | 0.26 | PARTIAL |
| volatility | `egarch_758.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.02 | 0.00 | 0.00 | 0.09 | 0.00 | 0.64 | PARTIAL |
| volatility | `egarch_281.csv` | 0.71 | 0.00 | 0.00 | 1.00 | 0.02 | 0.00 | 0.01 | 0.21 | 0.00 | 0.97 | PARTIAL |
| volatility | `egarch_168.csv` | 0.86 | 0.00 | 0.00 | 1.00 | 0.01 | 0.00 | 0.01 | 0.62 | 0.00 | 0.16 | PARTIAL |
| volatility | `egarch_644.csv` | 0.90 | 0.00 | 0.00 | 1.00 | 0.01 | 0.00 | 0.02 | 0.71 | 0.00 | 0.21 | PARTIAL |
| volatility | `egarch_735.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.03 | 0.00 | 0.03 | 0.06 | 0.00 | 0.85 | PARTIAL |
| volatility | `egarch_864.csv` | 0.00 | 0.00 | 0.00 | 1.00 | 0.95 | 0.00 | 0.01 | 0.72 | 0.00 | 0.39 | PARTIAL |
| volatility | `egarch_677.csv` | 0.86 | 0.00 | 0.00 | 1.00 | 0.82 | 0.00 | 0.05 | 0.69 | 0.00 | 0.75 | PARTIAL |
| volatility | `egarch_321.csv` | 0.03 | 0.00 | 0.00 | 1.00 | 0.81 | 0.00 | 0.25 | 0.37 | 0.01 | 0.98 | PARTIAL |
| volatility | `egarch_192.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 1.00 | 0.00 | 0.65 | 0.19 | 0.25 | 0.04 | PARTIAL |
| volatility | `egarch_740.csv` | 0.74 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.20 | 0.23 | 0.07 | 0.15 | PARTIAL |
| volatility | `egarch_810.csv` | 0.65 | 0.00 | 0.00 | 1.00 | 0.71 | 0.00 | 0.02 | 0.30 | 0.02 | 0.09 | PARTIAL |
| volatility | `egarch_376.csv` | 0.00 | 0.00 | 0.00 | 1.00 | 0.17 | 0.00 | 0.03 | 0.33 | 0.00 | 0.99 | PARTIAL |
| volatility | `egarch_882.csv` | 0.05 | 0.00 | 0.00 | 1.00 | 0.53 | 0.00 | 0.98 | 0.66 | 0.00 | 0.76 | PARTIAL |
| volatility | `egarch_729.csv` | 0.40 | 0.00 | 0.00 | 1.00 | 0.89 | 0.00 | 0.01 | 0.98 | 0.01 | 0.07 | PARTIAL |
| volatility | `egarch_651.csv` | 0.00 | 0.00 | 0.00 | 1.00 | 0.18 | 0.00 | 0.35 | 0.30 | 0.01 | 0.86 | PARTIAL |
| volatility | `garch_136.csv` | 0.85 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.96 | PARTIAL |
| volatility | `garch_708.csv` | 0.03 | 0.00 | 0.00 | 0.99 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.98 | PARTIAL |
| volatility | `garch_44.csv` | 0.94 | 0.00 | 0.00 | 1.00 | 0.01 | 0.00 | 0.61 | 0.32 | 0.00 | 0.63 | PARTIAL |
| volatility | `garch_565.csv` | 0.65 | 0.00 | 0.00 | 1.00 | 0.01 | 0.00 | 0.02 | 0.28 | 0.00 | 0.78 | PARTIAL |
| volatility | `garch_696.csv` | 0.65 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.98 | PARTIAL |
| volatility | `garch_412.csv` | 0.63 | 0.00 | 0.00 | 1.00 | 0.01 | 0.00 | 0.03 | 0.11 | 0.00 | 0.97 | PARTIAL |
| volatility | `garch_109.csv` | 0.49 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.01 | 0.08 | 0.00 | 0.76 | PARTIAL |
| volatility | `garch_881.csv` | 0.37 | 0.00 | 0.00 | 1.00 | 0.01 | 0.00 | 0.18 | 0.63 | 0.00 | 0.26 | PARTIAL |
| volatility | `garch_857.csv` | 0.43 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.01 | 0.98 | PARTIAL |
| volatility | `garch_55.csv` | 0.42 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.00 | 0.98 | PARTIAL |
| volatility | `garch_196.csv` | 0.13 | 0.00 | 0.00 | 1.00 | 0.37 | 0.00 | 0.10 | 0.84 | 0.00 | 0.78 | PARTIAL |
| volatility | `garch_498.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.96 | 0.00 | 0.18 | 0.15 | 0.45 | 0.12 | PARTIAL |
| volatility | `garch_984.csv` | 0.15 | 0.00 | 0.00 | 1.00 | 0.26 | 0.00 | 0.03 | 0.99 | 0.00 | 0.19 | PARTIAL |
| volatility | `garch_431.csv` | 0.30 | 0.00 | 0.00 | 1.00 | 0.96 | 0.00 | 0.30 | 0.93 | 0.01 | 0.10 | PARTIAL |
| volatility | `garch_684.csv` | 0.01 | 0.00 | 0.00 | 1.00 | 0.80 | 0.00 | 0.43 | 0.79 | 0.00 | 0.33 | PARTIAL |
| volatility | `garch_92.csv` | 0.00 | 0.00 | 0.00 | 1.00 | 0.10 | 0.00 | 0.04 | 0.18 | 0.00 | 0.99 | PARTIAL |
| volatility | `garch_862.csv` | 0.00 | 0.00 | 0.00 | 1.00 | 0.20 | 0.00 | 0.98 | 0.61 | 0.00 | 0.09 | PARTIAL |
| volatility | `garch_521.csv` | 0.59 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.93 | 0.09 | 0.03 | 0.12 | PARTIAL |
| volatility | `garch_750.csv` | 0.65 | 0.00 | 0.00 | 1.00 | 0.82 | 0.00 | 0.32 | 0.21 | 0.15 | 0.97 | PARTIAL |
| volatility | `garch_239.csv` | 0.24 | 0.00 | 0.00 | 1.00 | 0.84 | 0.00 | 0.07 | 0.75 | 0.01 | 0.03 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_775.csv` | 1.00 | 0.00 | 0.01 | 0.00 | 0.28 | 0.00 | 0.80 | 0.00 | 0.00 | 0.02 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_989.csv` | 0.99 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.52 | 0.00 | 0.02 | 0.07 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_946.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.08 | 0.00 | 0.98 | 0.00 | 0.00 | 0.01 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_527.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.08 | 0.00 | 0.02 | 0.22 | 0.00 | 0.01 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_50.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.10 | 0.00 | 0.26 | 0.01 | 0.00 | 0.01 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_86.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.17 | 0.00 | 0.79 | 0.01 | 0.00 | 0.04 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_644.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.01 | 0.69 | 0.00 | 0.05 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_178.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.46 | 0.00 | 0.83 | 0.00 | 0.00 | 0.01 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_448.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.26 | 0.00 | 0.06 | 0.06 | 0.00 | 0.00 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_833.csv` | 1.00 | 0.00 | 0.00 | 0.12 | 0.37 | 0.00 | 0.50 | 0.50 | 0.03 | 0.06 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_336.csv` | 0.98 | 0.00 | 0.34 | 0.00 | 0.01 | 0.00 | 0.96 | 0.01 | 0.23 | 0.15 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_356.csv` | 1.00 | 0.00 | 0.20 | 0.00 | 0.04 | 0.00 | 0.99 | 0.03 | 0.00 | 0.08 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_610.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.35 | 0.00 | 0.98 | 0.13 | 0.05 | 0.15 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_107.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.34 | 0.00 | 0.72 | 0.19 | 0.00 | 0.03 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_274.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.22 | 0.00 | 0.97 | 0.05 | 0.00 | 0.06 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_177.csv` | 0.99 | 0.00 | 0.00 | 0.98 | 0.17 | 0.00 | 0.15 | 0.64 | 0.00 | 0.03 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_473.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.32 | 0.00 | 0.91 | 0.67 | 0.02 | 0.22 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_549.csv` | 0.99 | 0.00 | 0.00 | 0.93 | 0.03 | 0.00 | 0.75 | 0.38 | 0.01 | 0.25 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_798.csv` | 1.00 | 0.00 | 0.00 | 0.18 | 0.15 | 0.00 | 0.96 | 0.63 | 0.02 | 0.68 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_32.csv` | 1.00 | 0.00 | 0.00 | 0.05 | 0.33 | 0.00 | 0.07 | 0.54 | 0.06 | 0.31 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_735.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 1.00 | 0.03 | 0.06 | 0.02 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_694.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.04 | 0.44 | 0.00 | 0.10 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_510.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.28 | 0.00 | 0.01 | 0.31 | 0.03 | 0.88 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_113.csv` | 1.00 | 0.00 | 1.00 | 0.00 | 0.72 | 0.00 | 0.59 | 0.08 | 0.04 | 0.05 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_471.csv` | 1.00 | 0.00 | 0.00 | 0.01 | 0.43 | 0.00 | 0.61 | 0.30 | 0.02 | 0.03 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_736.csv` | 1.00 | 0.00 | 0.00 | 0.10 | 0.09 | 0.00 | 0.16 | 0.58 | 0.00 | 0.92 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_322.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.28 | 0.00 | 0.46 | 0.57 | 0.03 | 0.34 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_380.csv` | 0.62 | 0.00 | 0.96 | 1.00 | 0.93 | 0.00 | 0.25 | 0.57 | 0.01 | 0.73 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_71.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.09 | 0.22 | 0.51 | 0.02 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_438.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.05 | 0.00 | 0.99 | 0.04 | 0.93 | 0.15 | NONE |
| collective_anomaly | `ar_collective_anomaly_534.csv` | 0.93 | 0.00 | 1.00 | 1.00 | 0.74 | 0.00 | 0.99 | 0.29 | 0.02 | 0.01 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_608.csv` | 0.79 | 0.00 | 1.00 | 1.00 | 0.82 | 0.00 | 0.99 | 0.15 | 0.03 | 0.00 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_588.csv` | 0.94 | 0.00 | 0.00 | 1.00 | 0.50 | 0.00 | 0.06 | 0.36 | 0.55 | 0.25 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_415.csv` | 0.99 | 0.00 | 1.00 | 0.89 | 1.00 | 0.00 | 0.60 | 0.23 | 0.07 | 0.42 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_490.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.96 | 0.00 | 0.16 | 0.35 | 0.20 | 0.22 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_786.csv` | 0.01 | 0.00 | 0.00 | 1.00 | 0.63 | 0.00 | 0.15 | 0.43 | 0.02 | 0.10 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_605.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.32 | 0.23 | 0.09 | 0.06 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_402.csv` | 0.95 | 0.00 | 0.00 | 1.00 | 0.71 | 0.00 | 0.12 | 0.53 | 0.01 | 0.27 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_422.csv` | 0.89 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.04 | 0.68 | 0.01 | 0.25 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_746.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.43 | 0.00 | 0.03 | 0.45 | 0.07 | 0.23 | NONE |
| collective_anomaly | `ar_collective_anomaly_348.csv` | 0.96 | 0.00 | 0.00 | 1.00 | 0.81 | 0.00 | 0.12 | 0.82 | 0.01 | 0.30 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_380.csv` | 0.30 | 0.00 | 1.00 | 0.00 | 0.96 | 0.00 | 0.82 | 0.50 | 0.04 | 0.04 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_33.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.29 | 0.00 | 0.03 | 0.65 | 0.05 | 0.19 | NONE |
| collective_anomaly | `ar_collective_anomaly_209.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.14 | 0.76 | 0.35 | 0.14 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_763.csv` | 0.57 | 0.00 | 1.00 | 0.00 | 0.93 | 0.00 | 0.14 | 0.52 | 0.11 | 0.32 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_39.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 1.00 | 0.00 | 0.10 | 0.04 | 0.01 | 0.11 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_208.csv` | 0.15 | 0.00 | 1.00 | 0.00 | 0.98 | 0.00 | 0.03 | 0.26 | 0.01 | 0.01 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_783.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.27 | 0.00 | 0.01 | 0.50 | 0.20 | 0.28 | NONE |
| collective_anomaly | `ar_collective_anomaly_592.csv` | 1.00 | 0.00 | 0.40 | 0.92 | 0.14 | 0.00 | 0.55 | 0.21 | 0.98 | 0.52 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_975.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.10 | 0.39 | 0.05 | 0.10 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_800.csv` | 0.99 | 0.00 | 1.00 | 0.00 | 0.85 | 0.00 | 0.73 | 0.68 | 0.61 | 0.02 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_734.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.11 | 0.12 | 0.37 | 0.14 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_269.csv` | 0.95 | 0.00 | 0.00 | 1.00 | 1.00 | 0.00 | 0.33 | 0.26 | 0.83 | 0.06 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_275.csv` | 0.56 | 0.00 | 0.00 | 1.00 | 0.89 | 0.00 | 0.10 | 0.86 | 0.23 | 0.06 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_298.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.72 | 0.00 | 0.30 | 0.75 | 0.58 | 0.08 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_544.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.22 | 0.89 | 0.13 | 0.12 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_766.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.95 | 0.00 | 0.91 | 0.33 | 0.69 | 0.01 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_641.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.99 | 0.00 | 0.89 | 0.50 | 0.00 | 0.02 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_8.csv` | 0.93 | 0.00 | 0.00 | 1.00 | 0.95 | 0.00 | 0.21 | 0.51 | 0.03 | 0.09 | PARTIAL |
| collective_anomaly | `ar_collective_anomaly_649.csv` | 0.95 | 0.00 | 0.00 | 1.00 | 0.97 | 0.00 | 0.06 | 0.78 | 0.01 | 0.45 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_110.csv` | 0.95 | 0.00 | 0.82 | 0.00 | 0.19 | 0.00 | 0.06 | 0.01 | 0.00 | 0.09 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_608.csv` | 0.99 | 0.00 | 0.03 | 0.00 | 0.06 | 0.00 | 0.05 | 0.01 | 0.00 | 0.09 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_330.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.43 | 0.00 | 0.18 | 0.02 | 0.00 | 0.06 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_539.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.25 | 0.00 | 0.80 | 0.08 | 0.01 | 0.06 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_158.csv` | 1.00 | 0.00 | 1.00 | 0.00 | 0.83 | 0.00 | 0.91 | 0.02 | 0.00 | 0.54 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_238.csv` | 1.00 | 0.77 | 0.00 | 0.00 | 0.15 | 0.00 | 0.59 | 0.70 | 0.00 | 0.17 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_379.csv` | 1.00 | 0.00 | 0.00 | 0.02 | 0.16 | 0.00 | 0.93 | 0.40 | 0.02 | 0.19 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_327.csv` | 1.00 | 0.00 | 1.00 | 0.00 | 0.98 | 0.00 | 0.94 | 0.01 | 0.00 | 0.12 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_612.csv` | 1.00 | 0.00 | 0.00 | 0.13 | 0.26 | 0.00 | 0.96 | 0.18 | 0.00 | 0.07 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_657.csv` | 0.99 | 0.00 | 1.00 | 0.00 | 0.93 | 0.00 | 0.78 | 0.03 | 0.00 | 0.64 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_306.csv` | 1.00 | 0.00 | 0.00 | 0.99 | 0.29 | 0.00 | 0.85 | 0.20 | 0.02 | 0.22 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_813.csv` | 1.00 | 0.00 | 0.00 | 0.04 | 0.19 | 0.00 | 0.97 | 0.42 | 0.01 | 0.13 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_936.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.12 | 0.00 | 0.32 | 0.80 | 0.01 | 0.29 | NONE |
| collective_anomaly | `arma_collective_anomaly_38.csv` | 0.91 | 0.00 | 1.00 | 0.00 | 0.92 | 0.00 | 0.22 | 0.01 | 0.00 | 0.74 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_622.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.89 | 0.00 | 0.05 | 0.72 | 0.21 | 0.11 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_670.csv` | 0.95 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.09 | 0.40 | 0.04 | 0.44 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_984.csv` | 0.26 | 0.00 | 0.00 | 1.00 | 0.95 | 0.00 | 0.99 | 0.18 | 0.01 | 0.05 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_780.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.74 | 0.00 | 0.67 | 0.79 | 0.62 | 0.04 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_19.csv` | 0.03 | 0.00 | 0.99 | 0.45 | 1.00 | 0.00 | 0.07 | 0.48 | 0.00 | 0.24 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_29.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.06 | 0.69 | 0.00 | 0.54 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_675.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.67 | 0.53 | 0.04 | 0.30 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_293.csv` | 0.90 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.74 | 0.20 | 0.39 | 0.20 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_707.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.87 | 0.00 | 0.97 | 0.37 | 0.91 | 0.01 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_319.csv` | 0.94 | 0.00 | 0.00 | 1.00 | 0.92 | 0.00 | 0.16 | 0.64 | 0.02 | 0.04 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_258.csv` | 0.92 | 0.00 | 0.94 | 1.00 | 0.99 | 0.00 | 0.19 | 0.12 | 0.01 | 0.20 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_167.csv` | 0.92 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.84 | 0.61 | 0.55 | 0.08 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_242.csv` | 0.93 | 0.00 | 0.01 | 0.97 | 0.85 | 0.00 | 0.86 | 0.17 | 0.52 | 0.03 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_100.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.77 | 0.00 | 0.94 | 0.58 | 0.64 | 0.01 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_733.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.97 | 0.00 | 0.01 | 0.39 | 0.94 | 0.09 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_646.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.90 | 0.00 | 0.68 | 0.25 | 0.11 | 0.15 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_531.csv` | 1.00 | 0.00 | 0.00 | 0.14 | 0.50 | 0.00 | 0.06 | 0.15 | 0.34 | 0.87 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_367.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.94 | 0.00 | 0.14 | 0.27 | 0.65 | 0.02 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_128.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.41 | 0.00 | 0.02 | 0.23 | 0.08 | 0.09 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_311.csv` | 1.00 | 0.00 | 0.00 | 0.97 | 0.37 | 0.00 | 0.07 | 0.34 | 0.01 | 0.96 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_364.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.31 | 0.00 | 0.04 | 0.12 | 0.02 | 0.97 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_75.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.18 | 0.91 | 0.01 | 0.23 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_359.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.67 | 0.00 | 0.86 | 0.67 | 0.24 | 0.72 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_746.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.87 | 0.00 | 0.94 | 0.68 | 0.21 | 0.05 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_516.csv` | 0.99 | 0.00 | 0.99 | 0.87 | 0.83 | 0.00 | 0.09 | 0.91 | 0.07 | 0.58 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_731.csv` | 0.96 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.02 | 0.11 | 0.42 | 0.59 | PARTIAL |
| collective_anomaly | `arma_collective_anomaly_313.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.23 | 0.44 | 0.02 | 0.15 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_305.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.10 | 0.00 | 0.02 | 0.76 | 0.00 | 0.01 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_936.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.37 | 0.00 | 0.20 | 0.01 | 0.00 | 0.01 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_153.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.00 | 0.27 | 0.02 | 0.00 | 0.01 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_859.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.09 | 0.00 | 0.94 | 0.01 | 0.00 | 0.01 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_622.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.29 | 0.00 | 0.39 | 0.01 | 0.00 | 0.00 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_733.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.44 | 0.00 | 0.12 | 0.02 | 0.00 | 0.06 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_56.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.22 | 0.00 | 0.78 | 0.05 | 0.00 | 0.07 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_172.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.18 | 0.00 | 1.00 | 0.03 | 0.20 | 0.07 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_65.csv` | 1.00 | 0.00 | 0.00 | 0.22 | 0.28 | 0.00 | 1.00 | 0.03 | 0.02 | 0.06 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_134.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.20 | 0.00 | 0.99 | 0.07 | 0.11 | 0.04 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_497.csv` | 1.00 | 0.00 | 0.00 | 0.01 | 0.18 | 0.00 | 0.99 | 0.03 | 0.02 | 0.03 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_396.csv` | 0.03 | 1.00 | 0.00 | 0.00 | 0.30 | 0.00 | 0.55 | 0.14 | 0.00 | 0.32 | NONE |
| collective_anomaly | `ma_collective_anomaly_329.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.12 | 0.00 | 0.94 | 0.33 | 0.01 | 0.09 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_803.csv` | 1.00 | 0.00 | 0.00 | 0.95 | 0.47 | 0.00 | 0.34 | 0.23 | 0.08 | 0.58 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_718.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.45 | 0.00 | 0.96 | 0.33 | 0.03 | 0.05 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_63.csv` | 1.00 | 0.00 | 0.00 | 0.28 | 0.22 | 0.00 | 0.14 | 0.24 | 0.01 | 0.22 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_135.csv` | 1.00 | 0.00 | 0.00 | 0.17 | 0.34 | 0.00 | 0.97 | 0.06 | 0.15 | 0.21 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_26.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.43 | 0.00 | 0.71 | 0.06 | 0.02 | 0.11 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_7.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.39 | 0.00 | 0.20 | 0.74 | 0.00 | 0.14 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_505.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.43 | 0.00 | 0.45 | 0.20 | 0.00 | 0.08 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_265.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.06 | 0.00 | 0.35 | 0.82 | 0.00 | 0.08 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_638.csv` | 1.00 | 0.00 | 0.00 | 0.02 | 0.11 | 0.00 | 0.46 | 0.17 | 0.00 | 0.10 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_50.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.88 | 0.00 | 0.38 | 0.58 | 0.04 | 0.71 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_684.csv` | 0.93 | 0.00 | 0.00 | 1.00 | 1.00 | 0.00 | 0.16 | 0.20 | 0.05 | 0.04 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_849.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.96 | 0.00 | 0.21 | 0.75 | 0.53 | 0.03 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_551.csv` | 0.43 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.03 | 0.61 | 0.01 | 0.23 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_992.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.82 | 0.00 | 0.03 | 0.57 | 0.00 | 0.14 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_182.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.11 | 0.00 | 0.10 | 0.12 | 0.01 | 0.43 | NONE |
| collective_anomaly | `ma_collective_anomaly_531.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.88 | 0.00 | 0.98 | 0.22 | 0.53 | 0.03 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_419.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.89 | 0.00 | 0.04 | 0.71 | 0.04 | 0.05 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_405.csv` | 0.73 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.13 | 0.36 | 0.05 | 0.23 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_716.csv` | 0.98 | 0.00 | 0.99 | 1.00 | 0.90 | 0.00 | 0.88 | 0.22 | 0.04 | 0.04 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_195.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.96 | 0.00 | 0.42 | 0.81 | 0.85 | 0.01 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_89.csv` | 0.96 | 0.00 | 0.00 | 1.00 | 0.96 | 0.00 | 0.22 | 0.11 | 0.22 | 0.02 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_246.csv` | 0.96 | 0.00 | 0.00 | 1.00 | 0.95 | 0.00 | 0.51 | 0.63 | 0.07 | 0.24 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_401.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.38 | 0.00 | 0.05 | 0.12 | 0.01 | 0.06 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_478.csv` | 0.91 | 0.00 | 0.00 | 1.00 | 0.93 | 0.00 | 0.19 | 0.92 | 0.02 | 0.14 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_738.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 1.00 | 0.00 | 0.84 | 0.31 | 0.61 | 0.02 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_364.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.93 | 0.00 | 0.11 | 0.68 | 0.03 | 0.42 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_709.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.90 | 0.00 | 0.93 | 0.10 | 0.65 | 0.05 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_97.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.97 | 0.00 | 0.08 | 0.78 | 0.10 | 0.05 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_468.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.80 | 0.00 | 0.02 | 0.94 | 0.01 | 0.60 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_849.csv` | 0.91 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.98 | 0.14 | 0.19 | 0.01 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_8.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.90 | 0.00 | 0.41 | 0.40 | 0.57 | 0.58 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_605.csv` | 0.11 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.05 | 0.79 | 0.01 | 0.17 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_517.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.88 | 0.00 | 0.43 | 0.40 | 0.03 | 0.06 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_330.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.53 | 0.00 | 0.33 | 0.67 | 0.01 | 0.16 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_397.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.89 | 0.00 | 0.88 | 0.82 | 0.86 | 0.05 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_204.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.54 | 0.33 | 0.08 | 0.22 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_993.csv` | 0.88 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.03 | 0.69 | 0.06 | 0.05 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_470.csv` | 0.85 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.07 | 0.89 | 0.25 | 0.20 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_896.csv` | 0.96 | 0.00 | 0.00 | 1.00 | 0.91 | 0.00 | 0.06 | 0.83 | 0.15 | 0.55 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_859.csv` | 0.72 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.32 | 0.33 | 0.28 | 0.02 | PARTIAL |
| collective_anomaly | `ma_collective_anomaly_10.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.89 | 0.00 | 0.67 | 0.75 | 0.08 | 0.01 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_607.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.22 | 0.00 | 0.33 | 0.03 | 0.00 | 0.01 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_184.csv` | 1.00 | 0.00 | 0.00 | 0.07 | 0.30 | 0.00 | 0.96 | 0.42 | 0.00 | 0.10 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_305.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.44 | 0.00 | 1.00 | 0.05 | 0.16 | 0.02 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_874.csv` | 0.99 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.50 | 0.12 | 0.02 | 0.47 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_94.csv` | 1.00 | 0.00 | 0.00 | 0.25 | 0.17 | 0.00 | 0.95 | 0.15 | 0.04 | 0.02 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_202.csv` | 1.00 | 0.00 | 0.00 | 0.01 | 0.05 | 0.00 | 0.26 | 0.66 | 0.01 | 0.16 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_971.csv` | 1.00 | 0.00 | 0.00 | 0.05 | 0.03 | 0.00 | 0.99 | 0.34 | 0.04 | 0.04 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_866.csv` | 0.99 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 1.00 | 0.01 | 0.09 | 0.12 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_24.csv` | 1.00 | 0.00 | 0.00 | 0.16 | 0.03 | 0.00 | 0.99 | 0.74 | 0.01 | 0.01 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_558.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.98 | 0.12 | 0.03 | 0.02 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_959.csv` | 0.97 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.43 | 0.68 | 0.00 | 0.12 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_759.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.20 | 0.00 | 0.97 | 0.02 | 0.00 | 0.28 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_367.csv` | 1.00 | 0.00 | 0.00 | 0.03 | 0.02 | 0.00 | 0.99 | 0.07 | 0.00 | 0.23 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_568.csv` | 1.00 | 0.00 | 0.00 | 0.57 | 0.34 | 0.00 | 0.72 | 0.39 | 0.01 | 0.25 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_749.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.17 | 0.00 | 0.98 | 0.20 | 0.01 | 0.02 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_35.csv` | 1.00 | 0.00 | 0.00 | 0.16 | 0.04 | 0.00 | 0.86 | 0.58 | 0.04 | 0.10 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_481.csv` | 1.00 | 0.00 | 0.00 | 0.01 | 0.36 | 0.00 | 0.75 | 0.08 | 0.00 | 0.41 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_868.csv` | 1.00 | 0.00 | 0.00 | 0.98 | 0.18 | 0.00 | 0.97 | 0.30 | 0.01 | 0.12 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_533.csv` | 1.00 | 0.00 | 0.00 | 0.10 | 0.02 | 0.00 | 0.98 | 0.17 | 0.01 | 0.28 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_322.csv` | 1.00 | 0.00 | 0.00 | 0.12 | 0.35 | 0.00 | 0.99 | 0.20 | 0.04 | 0.16 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_519.csv` | 0.95 | 0.00 | 0.00 | 0.01 | 0.18 | 0.00 | 0.99 | 0.06 | 0.02 | 0.23 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_606.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.09 | 0.28 | 0.01 | 0.07 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_231.csv` | 0.99 | 0.00 | 0.00 | 0.99 | 0.01 | 0.00 | 0.77 | 0.40 | 0.02 | 0.03 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_274.csv` | 0.99 | 0.00 | 0.00 | 0.00 | 0.09 | 0.00 | 0.85 | 0.16 | 0.00 | 0.05 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_948.csv` | 0.99 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.12 | 0.18 | 0.00 | 0.14 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_650.csv` | 1.00 | 0.00 | 0.00 | 0.08 | 0.03 | 0.00 | 0.88 | 0.54 | 0.02 | 0.15 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_909.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.13 | 0.00 | 0.35 | 0.23 | 0.01 | 0.12 | NONE |
| collective_anomaly | `white_noise_collective_anomaly_223.csv` | 1.00 | 0.00 | 0.00 | 0.96 | 0.48 | 0.00 | 0.89 | 0.14 | 0.06 | 0.01 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_895.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.24 | 0.42 | 0.01 | 0.12 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_826.csv` | 1.00 | 0.00 | 0.00 | 0.01 | 0.16 | 0.00 | 0.66 | 0.11 | 0.01 | 0.21 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_480.csv` | 0.96 | 0.00 | 0.00 | 1.00 | 0.67 | 0.00 | 0.95 | 0.94 | 0.59 | 0.01 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_411.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.70 | 0.00 | 0.99 | 0.12 | 0.85 | 0.02 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_96.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.05 | 0.62 | 0.26 | 0.03 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_824.csv` | 0.41 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.51 | 0.43 | 0.17 | 0.02 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_566.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.32 | 0.48 | 0.87 | 0.06 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_344.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 1.00 | 0.00 | 0.08 | 0.58 | 0.03 | 0.03 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_855.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.16 | 0.58 | 0.42 | 0.01 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_100.csv` | 0.70 | 0.00 | 0.00 | 1.00 | 0.36 | 0.00 | 0.06 | 0.95 | 0.01 | 0.03 | NONE |
| collective_anomaly | `white_noise_collective_anomaly_359.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.96 | 0.00 | 1.00 | 0.19 | 0.11 | 0.10 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_768.csv` | 0.90 | 0.00 | 0.00 | 1.00 | 0.97 | 0.00 | 0.93 | 0.15 | 0.74 | 0.17 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_373.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.96 | 0.00 | 0.59 | 0.70 | 0.28 | 0.06 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_870.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.08 | 0.49 | 0.35 | 0.13 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_64.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.52 | 0.00 | 0.02 | 0.24 | 0.19 | 0.80 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_632.csv` | 0.67 | 0.00 | 0.00 | 1.00 | 0.67 | 0.00 | 0.06 | 0.69 | 0.02 | 0.07 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_706.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.95 | 0.00 | 0.98 | 0.13 | 0.56 | 0.00 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_55.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.95 | 0.00 | 0.14 | 0.96 | 0.08 | 0.44 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_897.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.18 | 0.57 | 0.06 | 0.17 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_235.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.31 | 0.26 | 0.30 | 0.95 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_51.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.97 | 0.00 | 0.10 | 0.87 | 0.07 | 0.29 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_595.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.71 | 0.67 | 0.28 | 0.07 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_416.csv` | 0.95 | 0.00 | 0.00 | 1.00 | 0.06 | 0.00 | 0.98 | 0.62 | 0.06 | 0.00 | NONE |
| collective_anomaly | `white_noise_collective_anomaly_404.csv` | 0.62 | 0.00 | 0.00 | 1.00 | 0.57 | 0.00 | 0.99 | 0.06 | 0.36 | 0.00 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_607.csv` | 0.72 | 0.00 | 0.00 | 1.00 | 0.96 | 0.00 | 0.10 | 0.56 | 0.03 | 0.24 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_801.csv` | 0.75 | 0.00 | 0.00 | 1.00 | 0.86 | 0.00 | 0.95 | 0.10 | 0.55 | 0.07 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_6.csv` | 0.83 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.13 | 0.58 | 0.34 | 0.06 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_446.csv` | 0.60 | 0.00 | 0.00 | 1.00 | 0.96 | 0.00 | 0.59 | 0.58 | 0.09 | 0.13 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_518.csv` | 0.73 | 0.00 | 0.00 | 1.00 | 0.96 | 0.00 | 0.21 | 0.70 | 0.23 | 0.05 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_959.csv` | 0.01 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.03 | 0.75 | 0.01 | 0.12 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_395.csv` | 0.86 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.04 | 0.58 | 0.06 | 0.01 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_90.csv` | 0.93 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.44 | 0.30 | 0.68 | 0.02 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_741.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.07 | 0.40 | 0.07 | 0.14 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_318.csv` | 0.27 | 0.00 | 0.00 | 1.00 | 0.93 | 0.00 | 0.99 | 0.62 | 0.07 | 0.01 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_625.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.86 | 0.00 | 0.22 | 0.54 | 0.31 | 0.27 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_451.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.97 | 0.00 | 0.15 | 0.72 | 0.18 | 0.47 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_313.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.44 | 0.00 | 0.35 | 0.85 | 0.58 | 0.36 | NONE |
| collective_anomaly | `white_noise_collective_anomaly_888.csv` | 0.96 | 0.00 | 0.00 | 1.00 | 1.00 | 0.00 | 0.17 | 0.65 | 0.53 | 0.02 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_813.csv` | 0.70 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.41 | 0.25 | 0.22 | 0.67 | PARTIAL |
| collective_anomaly | `white_noise_collective_anomaly_477.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.95 | 0.00 | 0.43 | 0.80 | 0.12 | 0.10 | PARTIAL |
| contextual_anomaly | `ar_contextual_anomaly_middle_728.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.98 | 1.00 | 0.01 | 0.99 | 0.03 | 0.01 | PARTIAL |
| contextual_anomaly | `ma_contextual_anomaly_multiple_716.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.99 | 1.00 | 0.01 | 1.00 | 0.02 | 0.00 | PARTIAL |
| contextual_anomaly | `ma_contextual_anomaly_beginning_55.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 1.00 | 1.00 | 0.13 | 0.75 | 0.05 | 0.04 | PARTIAL |
| contextual_anomaly | `white_noise_contextual_anomaly_multiple_970.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.97 | 1.00 | 0.00 | 0.58 | 0.01 | 0.02 | PARTIAL |
| mean_shift | `ar_mean_shift_37.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.08 | 0.00 | 0.19 | 0.01 | 0.00 | 0.01 | PARTIAL |
| mean_shift | `ar_mean_shift_564.csv` | 0.96 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.02 | PARTIAL |
| mean_shift | `ar_mean_shift_745.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.17 | 0.00 | 0.00 | 0.75 | PARTIAL |
| mean_shift | `ar_mean_shift_885.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.24 | 0.05 | 0.00 | 0.25 | PARTIAL |
| mean_shift | `ar_mean_shift_606.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.22 | 0.02 | 0.00 | 0.00 | PARTIAL |
| mean_shift | `ar_mean_shift_616.csv` | 1.00 | 0.00 | 0.00 | 0.83 | 0.26 | 0.00 | 0.49 | 0.39 | 0.01 | 0.02 | PARTIAL |
| mean_shift | `ar_mean_shift_386.csv` | 0.81 | 0.00 | 0.00 | 1.00 | 0.80 | 0.00 | 0.98 | 0.24 | 0.64 | 0.01 | PARTIAL |
| mean_shift | `ar_mean_shift_194.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.97 | 0.00 | 0.54 | 0.90 | 0.85 | 0.01 | PARTIAL |
| mean_shift | `ar_mean_shift_630.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.70 | 0.00 | 0.27 | 0.21 | 0.89 | 0.13 | NONE |
| mean_shift | `ar_mean_shift_294.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.94 | 0.38 | 0.31 | 0.01 | PARTIAL |
| mean_shift | `ar_mean_shift_240.csv` | 0.34 | 0.00 | 0.00 | 1.00 | 1.00 | 0.00 | 0.17 | 0.02 | 0.01 | 0.07 | NONE |
| mean_shift | `ar_mean_shift_703.csv` | 0.94 | 0.00 | 0.00 | 1.00 | 1.00 | 0.00 | 0.11 | 0.07 | 0.05 | 0.20 | NONE |
| mean_shift | `ar_mean_shift_542.csv` | 1.00 | 0.00 | 0.74 | 0.99 | 0.99 | 0.00 | 0.16 | 0.94 | 0.06 | 0.04 | PARTIAL |
| mean_shift | `ar_mean_shift_88.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.97 | 0.00 | 0.89 | 0.68 | 0.17 | 0.08 | PARTIAL |
| mean_shift | `ar_mean_shift_198.csv` | 0.16 | 0.00 | 0.95 | 1.00 | 0.95 | 0.00 | 1.00 | 0.07 | 0.18 | 0.09 | PARTIAL |
| mean_shift | `ar_mean_shift_420.csv` | 0.91 | 0.00 | 1.00 | 0.00 | 0.86 | 0.00 | 0.98 | 0.38 | 0.62 | 0.01 | PARTIAL |
| mean_shift | `ar_mean_shift_878.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.96 | 0.00 | 0.67 | 0.77 | 0.02 | 0.02 | PARTIAL |
| mean_shift | `ar_mean_shift_610.csv` | 0.94 | 0.00 | 0.01 | 1.00 | 0.96 | 0.00 | 0.56 | 0.75 | 0.04 | 0.44 | PARTIAL |
| mean_shift | `ar_mean_shift_437.csv` | 0.94 | 0.00 | 0.00 | 1.00 | 0.03 | 0.00 | 0.79 | 0.37 | 0.78 | 0.18 | PARTIAL |
| mean_shift | `ar_mean_shift_203.csv` | 0.81 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.80 | 0.42 | 0.02 | 0.08 | PARTIAL |
| mean_shift | `ar_mean_shift_800.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.53 | 0.00 | 0.16 | 0.73 | 0.81 | 0.23 | NONE |
| mean_shift | `ar_mean_shift_355.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.87 | 0.00 | 0.87 | 0.30 | 0.32 | 0.11 | PARTIAL |
| mean_shift | `ar_mean_shift_627.csv` | 0.84 | 0.00 | 0.07 | 1.00 | 0.05 | 0.00 | 0.99 | 0.11 | 0.99 | 0.01 | PARTIAL |
| mean_shift | `ar_mean_shift_306.csv` | 0.90 | 0.00 | 0.08 | 1.00 | 1.00 | 0.00 | 0.50 | 0.95 | 0.02 | 0.02 | NONE |
| mean_shift | `ar_mean_shift_842.csv` | 0.95 | 0.00 | 0.02 | 1.00 | 0.99 | 0.00 | 0.39 | 0.78 | 0.02 | 0.03 | NONE |
| mean_shift | `ar_mean_shift_878.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.16 | 0.95 | 0.02 | 0.13 | PARTIAL |
| mean_shift | `ar_mean_shift_615.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.19 | 0.00 | 0.88 | 0.85 | 0.97 | 0.01 | PARTIAL |
| mean_shift | `ar_mean_shift_997.csv` | 0.84 | 0.00 | 0.00 | 1.00 | 0.83 | 0.00 | 0.26 | 0.49 | 0.02 | 0.83 | NONE |
| mean_shift | `ar_mean_shift_805.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.15 | 0.27 | 0.69 | 0.07 | NONE |
| mean_shift | `ar_mean_shift_853.csv` | 0.06 | 0.00 | 1.00 | 0.00 | 0.15 | 0.00 | 0.75 | 0.39 | 0.27 | 0.01 | PARTIAL |
| mean_shift | `ar_mean_shift_671.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.75 | 0.00 | 0.95 | 0.08 | 0.55 | 0.53 | PARTIAL |
| mean_shift | `ar_mean_shift_664.csv` | 0.91 | 0.00 | 1.00 | 0.25 | 0.14 | 0.00 | 0.93 | 0.82 | 0.80 | 0.01 | PARTIAL |
| mean_shift | `ar_mean_shift_691.csv` | 0.93 | 0.00 | 1.00 | 0.00 | 0.45 | 0.00 | 0.96 | 0.08 | 0.09 | 0.07 | PARTIAL |
| mean_shift | `ar_mean_shift_611.csv` | 0.16 | 0.00 | 1.00 | 0.00 | 0.10 | 0.00 | 0.76 | 0.22 | 0.31 | 0.01 | PARTIAL |
| mean_shift | `ar_mean_shift_121.csv` | 1.00 | 0.00 | 0.00 | 0.29 | 0.78 | 0.00 | 0.32 | 0.14 | 0.52 | 0.85 | PARTIAL |
| mean_shift | `ar_mean_shift_66.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.94 | 0.00 | 0.75 | 0.86 | 0.13 | 0.10 | PARTIAL |
| mean_shift | `ar_mean_shift_955.csv` | 0.19 | 0.00 | 0.00 | 1.00 | 0.03 | 0.00 | 0.96 | 0.09 | 0.91 | 0.33 | PARTIAL |
| mean_shift | `ar_mean_shift_704.csv` | 0.61 | 0.00 | 0.00 | 1.00 | 0.56 | 0.00 | 1.00 | 0.04 | 0.93 | 0.01 | PARTIAL |
| mean_shift | `ar_mean_shift_863.csv` | 0.15 | 0.00 | 0.00 | 1.00 | 0.90 | 0.00 | 0.98 | 0.26 | 0.29 | 0.03 | PARTIAL |
| mean_shift | `ar_mean_shift_738.csv` | 0.29 | 0.00 | 0.00 | 1.00 | 0.56 | 0.00 | 0.72 | 0.83 | 0.14 | 0.03 | PARTIAL |
| mean_shift | `ar_mean_shift_344.csv` | 0.63 | 0.00 | 1.00 | 0.03 | 0.89 | 0.00 | 0.97 | 0.67 | 0.01 | 0.03 | PARTIAL |
| mean_shift | `arma_mean_shift_264.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.41 | 0.00 | 0.01 | 0.23 | PARTIAL |
| mean_shift | `arma_mean_shift_265.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.65 | 0.00 | 0.09 | 0.08 | 0.00 | 0.07 | PARTIAL |
| mean_shift | `arma_mean_shift_23.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.34 | 0.00 | 0.38 | 0.14 | 0.00 | 0.00 | PARTIAL |
| mean_shift | `arma_mean_shift_182.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.20 | 0.00 | 0.31 | 0.42 | 0.00 | 0.00 | PARTIAL |
| mean_shift | `arma_mean_shift_297.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.16 | 0.60 | 0.00 | 0.03 | PARTIAL |
| mean_shift | `arma_mean_shift_506.csv` | 0.93 | 1.00 | 0.00 | 0.00 | 0.42 | 0.00 | 0.95 | 0.01 | 0.00 | 0.02 | PARTIAL |
| mean_shift | `arma_mean_shift_104.csv` | 0.99 | 0.00 | 1.00 | 0.00 | 0.07 | 0.00 | 0.67 | 0.02 | 0.39 | 0.32 | PARTIAL |
| mean_shift | `arma_mean_shift_293.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.03 | 0.00 | 1.00 | 0.47 | 0.54 | 0.01 | PARTIAL |
| mean_shift | `arma_mean_shift_805.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.97 | 0.00 | 0.49 | 0.86 | 0.37 | 0.02 | NONE |
| mean_shift | `arma_mean_shift_224.csv` | 0.94 | 0.00 | 0.00 | 1.00 | 0.86 | 0.00 | 0.67 | 0.22 | 0.52 | 0.43 | PARTIAL |
| mean_shift | `arma_mean_shift_333.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.41 | 0.00 | 0.78 | 0.64 | 0.44 | 0.76 | PARTIAL |
| mean_shift | `arma_mean_shift_365.csv` | 0.17 | 0.00 | 0.00 | 1.00 | 0.86 | 0.00 | 0.98 | 0.19 | 0.47 | 0.02 | PARTIAL |
| mean_shift | `arma_mean_shift_208.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.43 | 0.00 | 0.84 | 0.73 | 0.24 | 0.17 | PARTIAL |
| mean_shift | `arma_mean_shift_557.csv` | 0.95 | 0.00 | 0.00 | 1.00 | 0.89 | 0.00 | 0.95 | 0.69 | 0.07 | 0.33 | PARTIAL |
| mean_shift | `arma_mean_shift_787.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.83 | 0.00 | 0.98 | 0.35 | 0.37 | 0.02 | PARTIAL |
| mean_shift | `arma_mean_shift_495.csv` | 0.80 | 0.00 | 1.00 | 0.07 | 0.52 | 0.00 | 0.03 | 0.49 | 0.02 | 0.19 | NONE |
| mean_shift | `arma_mean_shift_26.csv` | 0.05 | 0.00 | 0.00 | 1.00 | 0.40 | 0.00 | 0.97 | 0.36 | 0.13 | 0.21 | PARTIAL |
| mean_shift | `arma_mean_shift_217.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.82 | 0.62 | 0.75 | 0.02 | PARTIAL |
| mean_shift | `arma_mean_shift_449.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.80 | 0.00 | 0.93 | 0.46 | 0.13 | 0.01 | PARTIAL |
| mean_shift | `arma_mean_shift_59.csv` | 0.36 | 0.00 | 0.00 | 0.99 | 0.97 | 0.00 | 0.97 | 0.48 | 0.04 | 0.49 | PARTIAL |
| mean_shift | `arma_mean_shift_747.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.29 | 0.00 | 1.00 | 0.07 | 0.51 | 0.25 | PARTIAL |
| mean_shift | `arma_mean_shift_31.csv` | 0.89 | 0.00 | 0.00 | 1.00 | 0.35 | 0.00 | 0.98 | 0.16 | 0.09 | 0.02 | PARTIAL |
| mean_shift | `arma_mean_shift_56.csv` | 0.19 | 0.00 | 0.00 | 1.00 | 0.20 | 0.00 | 0.99 | 0.10 | 0.05 | 0.02 | PARTIAL |
| mean_shift | `arma_mean_shift_613.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.12 | 0.36 | 0.05 | 0.03 | NONE |
| mean_shift | `arma_mean_shift_867.csv` | 0.75 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.05 | 0.81 | 0.43 | 0.38 | NONE |
| mean_shift | `arma_mean_shift_714.csv` | 0.54 | 0.00 | 0.00 | 1.00 | 0.97 | 0.00 | 0.12 | 0.56 | 0.24 | 0.66 | NONE |
| mean_shift | `arma_mean_shift_841.csv` | 0.95 | 0.00 | 0.00 | 1.00 | 0.15 | 0.00 | 0.65 | 0.17 | 0.03 | 0.70 | PARTIAL |
| mean_shift | `arma_mean_shift_424.csv` | 0.36 | 0.00 | 1.00 | 0.96 | 0.99 | 0.00 | 0.27 | 0.16 | 0.03 | 0.42 | NONE |
| mean_shift | `arma_mean_shift_164.csv` | 0.86 | 0.00 | 0.00 | 1.00 | 0.63 | 0.00 | 0.90 | 0.29 | 0.48 | 0.01 | PARTIAL |
| mean_shift | `arma_mean_shift_464.csv` | 0.94 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.25 | 0.10 | 0.69 | 0.04 | NONE |
| mean_shift | `arma_mean_shift_893.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.87 | 0.00 | 0.92 | 0.09 | 0.88 | 0.71 | PARTIAL |
| mean_shift | `arma_mean_shift_782.csv` | 0.93 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.04 | 0.39 | 0.20 | 0.23 | NONE |
| mean_shift | `arma_mean_shift_137.csv` | 0.16 | 0.00 | 0.00 | 1.00 | 0.96 | 0.00 | 0.14 | 0.96 | 0.19 | 0.06 | NONE |
| mean_shift | `arma_mean_shift_115.csv` | 1.00 | 0.00 | 0.00 | 0.96 | 0.93 | 0.00 | 0.39 | 0.79 | 0.78 | 0.16 | PARTIAL |
| mean_shift | `arma_mean_shift_521.csv` | 0.95 | 0.00 | 0.00 | 1.00 | 0.80 | 0.00 | 0.87 | 0.48 | 0.07 | 0.06 | PARTIAL |
| mean_shift | `arma_mean_shift_948.csv` | 0.97 | 0.00 | 1.00 | 0.01 | 0.73 | 0.00 | 0.88 | 0.37 | 0.70 | 0.03 | PARTIAL |
| mean_shift | `arma_mean_shift_17.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.94 | 0.00 | 0.04 | 0.47 | 0.76 | 0.06 | NONE |
| mean_shift | `arma_mean_shift_893.csv` | 0.94 | 0.00 | 0.00 | 1.00 | 0.67 | 0.00 | 0.83 | 0.40 | 0.95 | 0.01 | PARTIAL |
| mean_shift | `arma_mean_shift_629.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.93 | 0.00 | 0.30 | 0.71 | 0.27 | 0.02 | NONE |
| mean_shift | `arma_mean_shift_494.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.81 | 0.00 | 0.50 | 0.11 | 0.00 | 0.01 | NONE |
| mean_shift | `arma_mean_shift_627.csv` | 0.91 | 0.00 | 0.94 | 1.00 | 0.74 | 0.00 | 0.98 | 0.11 | 0.09 | 0.01 | PARTIAL |
| mean_shift | `ma_mean_shift_99.csv` | 0.35 | 0.06 | 0.86 | 0.00 | 0.01 | 0.00 | 0.66 | 0.00 | 0.00 | 0.05 | PARTIAL |
| mean_shift | `ma_mean_shift_668.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.37 | 0.06 | 0.00 | 0.01 | PARTIAL |
| mean_shift | `ma_mean_shift_463.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.00 | 0.03 | 0.09 | 0.00 | 0.01 | PARTIAL |
| mean_shift | `ma_mean_shift_410.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.10 | 0.25 | 0.00 | 0.01 | PARTIAL |
| mean_shift | `ma_mean_shift_693.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.97 | 0.00 | 0.15 | 0.30 | 0.03 | 0.35 | PARTIAL |
| mean_shift | `ma_mean_shift_168.csv` | 0.96 | 0.00 | 1.00 | 0.00 | 0.19 | 0.00 | 0.98 | 0.03 | 0.04 | 0.11 | PARTIAL |
| mean_shift | `ma_mean_shift_810.csv` | 1.00 | 0.00 | 0.00 | 0.36 | 0.22 | 0.00 | 0.38 | 0.41 | 0.01 | 0.33 | PARTIAL |
| mean_shift | `ma_mean_shift_619.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.79 | 0.00 | 0.77 | 0.72 | 0.39 | 0.10 | PARTIAL |
| mean_shift | `ma_mean_shift_691.csv` | 0.99 | 0.00 | 1.00 | 0.00 | 0.80 | 0.00 | 0.34 | 0.83 | 0.67 | 0.01 | NONE |
| mean_shift | `ma_mean_shift_684.csv` | 0.79 | 0.00 | 0.00 | 1.00 | 0.86 | 0.00 | 0.88 | 0.49 | 0.76 | 0.84 | PARTIAL |
| mean_shift | `ma_mean_shift_674.csv` | 0.96 | 0.00 | 0.00 | 1.00 | 0.29 | 0.00 | 1.00 | 0.23 | 0.16 | 0.03 | PARTIAL |
| mean_shift | `ma_mean_shift_396.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.97 | 0.00 | 0.54 | 0.92 | 0.05 | 0.03 | PARTIAL |
| mean_shift | `ma_mean_shift_895.csv` | 0.96 | 0.00 | 0.00 | 1.00 | 0.05 | 0.00 | 0.94 | 0.49 | 0.98 | 0.05 | PARTIAL |
| mean_shift | `ma_mean_shift_994.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.09 | 0.15 | 0.53 | 0.42 | NONE |
| mean_shift | `ma_mean_shift_677.csv` | 0.79 | 0.00 | 0.01 | 1.00 | 0.93 | 0.00 | 0.10 | 0.75 | 0.02 | 0.04 | NONE |
| mean_shift | `ma_mean_shift_39.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.89 | 0.00 | 0.81 | 0.20 | 0.98 | 0.69 | PARTIAL |
| mean_shift | `ma_mean_shift_237.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.23 | 0.00 | 0.99 | 0.03 | 0.99 | 0.03 | PARTIAL |
| mean_shift | `ma_mean_shift_503.csv` | 1.00 | 0.00 | 0.00 | 0.96 | 0.99 | 0.00 | 0.17 | 0.33 | 0.51 | 0.16 | PARTIAL |
| mean_shift | `ma_mean_shift_160.csv` | 0.88 | 0.00 | 0.00 | 1.00 | 0.67 | 0.00 | 1.00 | 0.03 | 0.53 | 0.02 | PARTIAL |
| mean_shift | `ma_mean_shift_530.csv` | 0.67 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.14 | 0.11 | 0.13 | 0.14 | NONE |
| mean_shift | `ma_mean_shift_505.csv` | 0.80 | 0.00 | 0.00 | 1.00 | 0.77 | 0.00 | 0.98 | 0.27 | 0.13 | 0.13 | PARTIAL |
| mean_shift | `ma_mean_shift_680.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.61 | 0.00 | 0.03 | 0.66 | 0.10 | 0.06 | NONE |
| mean_shift | `ma_mean_shift_378.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.86 | 0.00 | 0.46 | 0.53 | 0.60 | 0.03 | NONE |
| mean_shift | `ma_mean_shift_832.csv` | 0.96 | 0.00 | 0.00 | 1.00 | 0.71 | 0.00 | 0.51 | 0.06 | 0.44 | 0.18 | PARTIAL |
| mean_shift | `ma_mean_shift_351.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.69 | 0.39 | 0.10 | 0.29 | PARTIAL |
| mean_shift | `ma_mean_shift_643.csv` | 0.78 | 0.00 | 0.05 | 1.00 | 0.82 | 0.00 | 0.96 | 0.03 | 0.19 | 0.01 | PARTIAL |
| mean_shift | `ma_mean_shift_15.csv` | 0.94 | 0.00 | 0.00 | 1.00 | 0.57 | 0.00 | 0.69 | 0.21 | 0.87 | 0.05 | PARTIAL |
| mean_shift | `ma_mean_shift_422.csv` | 0.87 | 0.00 | 0.00 | 1.00 | 0.96 | 0.00 | 0.96 | 0.22 | 0.09 | 0.02 | PARTIAL |
| mean_shift | `ma_mean_shift_566.csv` | 0.89 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.20 | 0.13 | 0.39 | 0.02 | NONE |
| mean_shift | `ma_mean_shift_166.csv` | 0.85 | 0.00 | 1.00 | 0.01 | 1.00 | 0.00 | 0.97 | 0.13 | 0.03 | 0.02 | PARTIAL |
| mean_shift | `ma_mean_shift_384.csv` | 0.96 | 0.00 | 1.00 | 0.53 | 0.28 | 0.00 | 1.00 | 0.04 | 0.17 | 0.02 | PARTIAL |
| mean_shift | `ma_mean_shift_514.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.52 | 0.00 | 0.51 | 0.34 | 0.82 | 0.83 | PARTIAL |
| mean_shift | `ma_mean_shift_132.csv` | 0.94 | 0.00 | 0.00 | 1.00 | 0.92 | 0.00 | 1.00 | 0.09 | 0.97 | 0.01 | PARTIAL |
| mean_shift | `ma_mean_shift_150.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.61 | 0.00 | 0.02 | 0.56 | 0.02 | 0.62 | NONE |
| mean_shift | `ma_mean_shift_438.csv` | 0.96 | 0.00 | 1.00 | 0.00 | 0.59 | 0.00 | 0.87 | 0.70 | 0.82 | 0.01 | PARTIAL |
| mean_shift | `ma_mean_shift_865.csv` | 0.02 | 0.00 | 1.00 | 1.00 | 0.97 | 0.00 | 0.91 | 0.55 | 0.01 | 0.03 | PARTIAL |
| mean_shift | `ma_mean_shift_362.csv` | 0.56 | 0.00 | 0.00 | 1.00 | 0.33 | 0.00 | 0.98 | 0.17 | 0.11 | 0.02 | PARTIAL |
| mean_shift | `ma_mean_shift_169.csv` | 0.93 | 0.00 | 1.00 | 0.00 | 0.59 | 0.00 | 0.61 | 0.66 | 0.77 | 0.01 | PARTIAL |
| mean_shift | `ma_mean_shift_693.csv` | 0.72 | 0.00 | 0.15 | 1.00 | 0.98 | 0.00 | 0.80 | 0.37 | 0.07 | 0.57 | PARTIAL |
| mean_shift | `ma_mean_shift_895.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.83 | 0.00 | 0.99 | 0.09 | 0.98 | 0.01 | PARTIAL |
| mean_shift | `ma_mean_shift_887.csv` | 0.98 | 0.00 | 0.81 | 1.00 | 0.96 | 0.00 | 0.65 | 0.82 | 0.83 | 0.04 | PARTIAL |
| mean_shift | `ma_mean_shift_181.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.78 | 0.00 | 0.99 | 0.57 | 0.06 | 0.06 | PARTIAL |
| mean_shift | `ma_mean_shift_665.csv` | 0.98 | 0.00 | 0.03 | 0.99 | 0.86 | 0.00 | 1.00 | 0.24 | 0.66 | 0.01 | PARTIAL |
| mean_shift | `ma_mean_shift_646.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.23 | 0.00 | 0.97 | 0.12 | 0.71 | 0.04 | PARTIAL |
| mean_shift | `ma_mean_shift_566.csv` | 0.67 | 0.00 | 0.00 | 1.00 | 0.84 | 0.00 | 0.99 | 0.25 | 0.03 | 0.01 | PARTIAL |
| mean_shift | `ma_mean_shift_452.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.03 | 0.00 | 0.99 | 0.07 | 0.49 | 0.80 | PARTIAL |
| mean_shift | `white_noise_mean_shift_625.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.33 | 0.03 | 0.00 | 0.00 | PARTIAL |
| mean_shift | `white_noise_mean_shift_7.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.09 | 0.00 | 0.28 | 0.30 | 0.00 | 0.00 | PARTIAL |
| mean_shift | `white_noise_mean_shift_395.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.31 | 0.02 | 0.00 | 0.00 | PARTIAL |
| mean_shift | `white_noise_mean_shift_537.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.08 | 0.00 | 0.35 | 0.02 | 0.00 | 0.02 | PARTIAL |
| mean_shift | `white_noise_mean_shift_927.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.17 | 0.05 | 0.00 | 0.01 | PARTIAL |
| mean_shift | `white_noise_mean_shift_36.csv` | 1.00 | 0.00 | 0.00 | 0.97 | 0.04 | 0.00 | 0.11 | 0.38 | 0.01 | 0.07 | PARTIAL |
| mean_shift | `white_noise_mean_shift_766.csv` | 1.00 | 0.00 | 0.00 | 0.86 | 0.07 | 0.00 | 0.05 | 0.32 | 0.01 | 0.44 | PARTIAL |
| mean_shift | `white_noise_mean_shift_990.csv` | 0.33 | 0.00 | 0.00 | 1.00 | 0.91 | 0.00 | 1.00 | 0.03 | 0.23 | 0.00 | PARTIAL |
| mean_shift | `white_noise_mean_shift_702.csv` | 0.43 | 0.00 | 0.00 | 1.00 | 0.85 | 0.00 | 0.09 | 0.09 | 0.49 | 0.45 | NONE |
| mean_shift | `white_noise_mean_shift_742.csv` | 0.94 | 0.00 | 0.00 | 1.00 | 0.01 | 0.00 | 0.99 | 0.08 | 0.75 | 0.61 | PARTIAL |
| mean_shift | `white_noise_mean_shift_709.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.80 | 0.00 | 0.58 | 0.61 | 0.22 | 0.08 | PARTIAL |
| mean_shift | `white_noise_mean_shift_46.csv` | 0.94 | 0.00 | 0.00 | 1.00 | 0.73 | 0.00 | 0.52 | 0.42 | 0.81 | 0.02 | PARTIAL |
| mean_shift | `white_noise_mean_shift_217.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.32 | 0.00 | 0.19 | 0.68 | 0.94 | 0.43 | NONE |
| mean_shift | `white_noise_mean_shift_647.csv` | 0.69 | 0.00 | 0.00 | 1.00 | 0.17 | 0.00 | 0.72 | 0.60 | 0.16 | 0.07 | PARTIAL |
| mean_shift | `white_noise_mean_shift_751.csv` | 0.82 | 0.00 | 0.00 | 1.00 | 0.95 | 0.00 | 0.03 | 0.74 | 0.12 | 0.31 | NONE |
| mean_shift | `white_noise_mean_shift_963.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.08 | 0.00 | 1.00 | 0.09 | 0.97 | 0.00 | PARTIAL |
| mean_shift | `white_noise_mean_shift_176.csv` | 0.88 | 0.00 | 0.00 | 1.00 | 0.50 | 0.00 | 0.98 | 0.02 | 1.00 | 0.01 | PARTIAL |
| mean_shift | `white_noise_mean_shift_384.csv` | 0.96 | 0.00 | 0.00 | 1.00 | 0.25 | 0.00 | 0.94 | 0.40 | 0.95 | 0.11 | PARTIAL |
| mean_shift | `white_noise_mean_shift_613.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.73 | 0.00 | 0.62 | 0.65 | 0.38 | 0.87 | PARTIAL |
| mean_shift | `white_noise_mean_shift_445.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.05 | 0.79 | 0.04 | 0.33 | NONE |
| mean_shift | `white_noise_mean_shift_691.csv` | 0.95 | 0.00 | 0.00 | 1.00 | 0.97 | 0.00 | 0.14 | 0.50 | 0.37 | 0.18 | NONE |
| mean_shift | `white_noise_mean_shift_828.csv` | 0.89 | 0.00 | 0.00 | 0.99 | 0.78 | 0.00 | 0.88 | 0.42 | 0.87 | 0.13 | PARTIAL |
| mean_shift | `white_noise_mean_shift_400.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.83 | 0.59 | 0.26 | 0.04 | PARTIAL |
| mean_shift | `white_noise_mean_shift_848.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.92 | 0.00 | 0.96 | 0.69 | 0.65 | 0.14 | PARTIAL |
| mean_shift | `white_noise_mean_shift_215.csv` | 0.75 | 0.00 | 0.00 | 1.00 | 1.00 | 0.00 | 0.04 | 0.72 | 0.08 | 0.03 | NONE |
| mean_shift | `white_noise_mean_shift_716.csv` | 0.75 | 0.00 | 0.00 | 1.00 | 0.97 | 0.00 | 0.10 | 0.17 | 0.22 | 0.10 | NONE |
| mean_shift | `white_noise_mean_shift_746.csv` | 0.53 | 0.00 | 0.00 | 1.00 | 0.09 | 0.00 | 0.88 | 0.55 | 0.00 | 0.44 | PARTIAL |
| mean_shift | `white_noise_mean_shift_862.csv` | 0.90 | 0.00 | 0.00 | 1.00 | 0.88 | 0.00 | 0.54 | 0.18 | 0.02 | 0.89 | PARTIAL |
| mean_shift | `white_noise_mean_shift_971.csv` | 0.93 | 0.00 | 0.00 | 1.00 | 0.94 | 0.00 | 0.60 | 0.49 | 0.83 | 0.21 | PARTIAL |
| mean_shift | `white_noise_mean_shift_78.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.85 | 0.00 | 0.06 | 0.66 | 0.07 | 0.06 | NONE |
| mean_shift | `white_noise_mean_shift_94.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.71 | 0.00 | 0.93 | 0.64 | 0.42 | 0.26 | PARTIAL |
| mean_shift | `white_noise_mean_shift_584.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 1.00 | 0.00 | 0.02 | 0.37 | 0.19 | 0.32 | NONE |
| mean_shift | `white_noise_mean_shift_184.csv` | 0.95 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.28 | 0.15 | 0.05 | 0.35 | NONE |
| mean_shift | `white_noise_mean_shift_694.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.93 | 0.66 | 0.47 | 0.08 | PARTIAL |
| mean_shift | `white_noise_mean_shift_716.csv` | 0.51 | 0.00 | 0.00 | 1.00 | 0.28 | 0.00 | 0.99 | 0.05 | 0.61 | 0.01 | PARTIAL |
| mean_shift | `white_noise_mean_shift_489.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.87 | 0.00 | 0.06 | 0.22 | 0.36 | 0.05 | NONE |
| mean_shift | `white_noise_mean_shift_567.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.06 | 0.53 | 0.47 | 0.64 | NONE |
| mean_shift | `white_noise_mean_shift_431.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.05 | 0.00 | 1.00 | 0.10 | 0.35 | 0.02 | PARTIAL |
| mean_shift | `white_noise_mean_shift_114.csv` | 0.88 | 0.00 | 0.00 | 1.00 | 1.00 | 0.00 | 0.19 | 0.50 | 0.07 | 0.20 | NONE |
| mean_shift | `white_noise_mean_shift_432.csv` | 0.86 | 0.00 | 0.00 | 1.00 | 0.15 | 0.00 | 0.98 | 0.09 | 0.77 | 0.41 | PARTIAL |
| mean_shift | `white_noise_mean_shift_383.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.75 | 0.00 | 1.00 | 0.66 | 0.76 | 0.02 | PARTIAL |
| mean_shift | `white_noise_mean_shift_264.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.31 | 0.00 | 1.00 | 0.35 | 0.71 | 0.00 | PARTIAL |
| mean_shift | `white_noise_mean_shift_975.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.22 | 0.00 | 1.00 | 0.03 | 0.90 | 0.02 | PARTIAL |
| mean_shift | `white_noise_mean_shift_296.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.87 | 0.00 | 0.37 | 0.82 | 0.06 | 0.03 | NONE |
| mean_shift | `white_noise_mean_shift_412.csv` | 0.47 | 0.00 | 0.00 | 1.00 | 0.87 | 0.00 | 0.27 | 0.16 | 0.39 | 0.03 | NONE |
| point_anomaly | `ar_point_anomaly_multiple_306.csv` | 1.00 | 0.00 | 0.01 | 0.00 | 0.01 | 0.00 | 0.14 | 0.01 | 0.00 | 0.06 | PARTIAL |
| point_anomaly | `ar_point_anomaly_multiple_17.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.07 | 0.09 | 0.00 | 0.01 | PARTIAL |
| point_anomaly | `ar_point_anomaly_multiple_877.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.39 | 0.00 | 0.01 | PARTIAL |
| point_anomaly | `ar_point_anomaly_single_beginning_191.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.77 | 0.00 | 0.02 | 0.03 | 0.00 | 0.01 | PARTIAL |
| point_anomaly | `ar_point_anomaly_single_beginning_809.csv` | 1.00 | 0.00 | 0.00 | 0.01 | 0.04 | 0.00 | 0.01 | 0.44 | 0.00 | 0.00 | PARTIAL |
| point_anomaly | `ar_point_anomaly_single_beginning_78.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.02 | 0.50 | 0.00 | 0.01 | PARTIAL |
| point_anomaly | `ar_point_anomaly_single_end_445.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.04 | 0.47 | 0.00 | 0.01 | PARTIAL |
| point_anomaly | `ar_point_anomaly_single_middle_865.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.71 | 0.00 | 0.01 | 0.45 | 0.00 | 0.00 | PARTIAL |
| point_anomaly | `ar_point_anomaly_single_middle_930.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.96 | 0.00 | 0.16 | 0.01 | 0.00 | 0.00 | PARTIAL |
| point_anomaly | `ar_point_anomaly_multiple_434.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.56 | 0.00 | 0.04 | 0.16 | 0.06 | 0.36 | PARTIAL |
| point_anomaly | `ar_point_anomaly_multiple_721.csv` | 1.00 | 0.00 | 0.00 | 0.57 | 0.03 | 0.00 | 0.18 | 0.19 | 0.01 | 0.04 | PARTIAL |
| point_anomaly | `ar_point_anomaly_multiple_317.csv` | 1.00 | 0.00 | 0.00 | 0.02 | 0.81 | 0.00 | 0.71 | 0.30 | 0.00 | 0.09 | PARTIAL |
| point_anomaly | `ar_point_anomaly_multiple_661.csv` | 1.00 | 0.00 | 0.21 | 0.00 | 0.63 | 0.00 | 0.54 | 0.11 | 0.34 | 0.16 | PARTIAL |
| point_anomaly | `ar_point_anomaly_multiple_360.csv` | 1.00 | 0.00 | 0.22 | 0.00 | 0.92 | 0.00 | 0.07 | 0.35 | 0.00 | 0.73 | PARTIAL |
| point_anomaly | `ar_point_anomaly_single_beginning_789.csv` | 0.99 | 0.00 | 0.00 | 0.15 | 0.01 | 0.00 | 0.09 | 0.32 | 0.00 | 0.10 | PARTIAL |
| point_anomaly | `ar_point_anomaly_single_beginning_313.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.20 | 0.00 | 0.02 | 0.25 | 0.00 | 0.90 | PARTIAL |
| point_anomaly | `ar_point_anomaly_single_beginning_989.csv` | 1.00 | 0.00 | 0.00 | 0.15 | 0.04 | 0.00 | 0.03 | 0.35 | 0.00 | 0.29 | PARTIAL |
| point_anomaly | `ar_point_anomaly_single_beginning_844.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.46 | 0.00 | 0.97 | 0.03 | 0.00 | 0.12 | PARTIAL |
| point_anomaly | `ar_point_anomaly_single_beginning_821.csv` | 1.00 | 0.00 | 0.00 | 0.62 | 0.08 | 0.00 | 0.05 | 0.42 | 0.00 | 0.57 | PARTIAL |
| point_anomaly | `ar_point_anomaly_single_end_931.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.12 | 0.00 | 0.01 | 0.31 | 0.02 | 0.99 | PARTIAL |
| point_anomaly | `ar_point_anomaly_single_end_971.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.02 | 0.05 | 0.01 | 1.00 | PARTIAL |
| point_anomaly | `ar_point_anomaly_single_middle_450.csv` | 1.00 | 0.00 | 0.00 | 0.01 | 0.04 | 0.00 | 0.15 | 0.37 | 0.01 | 0.62 | PARTIAL |
| point_anomaly | `ar_point_anomaly_single_middle_99.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.05 | 0.46 | 0.00 | 0.06 | PARTIAL |
| point_anomaly | `ar_point_anomaly_single_middle_247.csv` | 1.00 | 0.00 | 0.00 | 0.01 | 0.28 | 0.00 | 0.93 | 0.15 | 0.03 | 0.98 | PARTIAL |
| point_anomaly | `ar_point_anomaly_single_middle_851.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.06 | 0.00 | 0.00 | 0.30 | 0.01 | 0.98 | PARTIAL |
| point_anomaly | `ar_point_anomaly_multiple_282.csv` | 0.81 | 0.00 | 0.00 | 1.00 | 0.95 | 0.00 | 0.98 | 0.16 | 0.18 | 0.03 | NONE |
| point_anomaly | `ar_point_anomaly_multiple_837.csv` | 0.37 | 0.00 | 0.00 | 1.00 | 0.97 | 0.00 | 0.01 | 0.33 | 0.01 | 0.16 | NONE |
| point_anomaly | `ar_point_anomaly_multiple_656.csv` | 0.25 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.04 | 0.45 | 0.03 | 0.78 | NONE |
| point_anomaly | `ar_point_anomaly_multiple_902.csv` | 0.96 | 0.00 | 0.00 | 1.00 | 0.88 | 0.00 | 0.03 | 0.52 | 0.03 | 0.77 | PARTIAL |
| point_anomaly | `ar_point_anomaly_multiple_329.csv` | 0.14 | 0.00 | 0.00 | 1.00 | 0.80 | 0.00 | 0.34 | 0.87 | 0.53 | 0.07 | PARTIAL |
| point_anomaly | `ar_point_anomaly_multiple_146.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.96 | 0.00 | 0.11 | 0.64 | 0.48 | 0.11 | PARTIAL |
| point_anomaly | `ar_point_anomaly_multiple_69.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.53 | 0.00 | 0.98 | 0.43 | 0.08 | 0.00 | NONE |
| point_anomaly | `ar_point_anomaly_multiple_541.csv` | 0.87 | 0.00 | 0.00 | 1.00 | 0.93 | 0.00 | 0.05 | 0.96 | 0.63 | 0.06 | PARTIAL |
| point_anomaly | `ar_point_anomaly_multiple_904.csv` | 0.52 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.29 | 0.86 | 0.02 | 0.40 | PARTIAL |
| point_anomaly | `ar_point_anomaly_single_beginning_609.csv` | 0.10 | 0.00 | 0.00 | 1.00 | 0.95 | 0.00 | 0.11 | 0.38 | 0.03 | 0.25 | NONE |
| point_anomaly | `ar_point_anomaly_single_beginning_96.csv` | 0.08 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.22 | 0.47 | 0.01 | 0.40 | NONE |
| point_anomaly | `ar_point_anomaly_single_beginning_754.csv` | 0.34 | 0.00 | 0.00 | 1.00 | 0.97 | 0.00 | 0.84 | 0.46 | 0.04 | 0.07 | NONE |
| point_anomaly | `ar_point_anomaly_single_beginning_574.csv` | 0.77 | 0.00 | 0.00 | 1.00 | 0.86 | 0.00 | 0.08 | 0.66 | 0.00 | 0.40 | PARTIAL |
| point_anomaly | `ar_point_anomaly_single_beginning_883.csv` | 1.00 | 0.00 | 0.26 | 0.99 | 0.13 | 0.00 | 0.02 | 0.25 | 0.02 | 0.94 | PARTIAL |
| point_anomaly | `ar_point_anomaly_single_beginning_212.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.08 | 0.19 | 0.16 | 0.10 | NONE |
| point_anomaly | `ar_point_anomaly_single_beginning_360.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.92 | 0.00 | 0.13 | 0.82 | 0.08 | 0.01 | PARTIAL |
| point_anomaly | `ar_point_anomaly_single_end_175.csv` | 0.37 | 0.00 | 0.00 | 1.00 | 0.96 | 0.00 | 0.90 | 0.16 | 0.04 | 0.03 | NONE |
| point_anomaly | `ar_point_anomaly_single_end_801.csv` | 0.82 | 0.00 | 0.00 | 1.00 | 0.26 | 0.00 | 0.02 | 0.42 | 0.00 | 0.90 | NONE |
| point_anomaly | `ar_point_anomaly_single_end_35.csv` | 1.00 | 0.00 | 1.00 | 0.00 | 0.94 | 0.00 | 0.34 | 0.68 | 0.01 | 0.08 | PARTIAL |
| point_anomaly | `ar_point_anomaly_single_end_512.csv` | 0.80 | 0.00 | 0.00 | 1.00 | 0.05 | 0.00 | 0.96 | 0.12 | 0.10 | 0.46 | NONE |
| point_anomaly | `ar_point_anomaly_single_end_933.csv` | 0.94 | 0.00 | 0.00 | 1.00 | 0.70 | 0.00 | 0.03 | 0.44 | 0.02 | 0.76 | NONE |
| point_anomaly | `ar_point_anomaly_single_end_571.csv` | 0.86 | 0.00 | 0.00 | 1.00 | 1.00 | 0.00 | 0.09 | 0.83 | 0.03 | 0.04 | PARTIAL |
| point_anomaly | `ar_point_anomaly_single_end_233.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.94 | 0.00 | 0.12 | 0.60 | 0.98 | 0.02 | PARTIAL |
| point_anomaly | `ar_point_anomaly_single_end_864.csv` | 0.94 | 0.00 | 0.95 | 0.53 | 0.82 | 0.00 | 0.44 | 0.80 | 0.00 | 0.21 | PARTIAL |
| point_anomaly | `ar_point_anomaly_single_end_500.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.95 | 0.00 | 0.04 | 0.20 | 0.94 | 0.05 | PARTIAL |
| point_anomaly | `ar_point_anomaly_single_middle_182.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.95 | 0.00 | 0.10 | 0.95 | 0.01 | 0.74 | PARTIAL |
| point_anomaly | `ar_point_anomaly_single_middle_971.csv` | 0.93 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.06 | 0.76 | 0.09 | 0.03 | PARTIAL |
| point_anomaly | `ar_point_anomaly_single_middle_938.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.09 | 0.54 | 0.59 | 0.90 | PARTIAL |
| point_anomaly | `ar_point_anomaly_single_middle_302.csv` | 0.96 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.16 | 0.56 | 0.35 | 0.04 | PARTIAL |
| point_anomaly | `ar_point_anomaly_single_middle_851.csv` | 0.96 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.91 | 0.63 | 0.05 | 0.02 | PARTIAL |
| point_anomaly | `ar_point_anomaly_single_middle_513.csv` | 0.66 | 0.00 | 0.00 | 1.00 | 0.91 | 0.00 | 0.97 | 0.73 | 0.11 | 0.04 | PARTIAL |
| point_anomaly | `ar_point_anomaly_single_middle_42.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.19 | 0.47 | 0.12 | 0.03 | NONE |
| point_anomaly | `ar_point_anomaly_single_middle_956.csv` | 0.33 | 0.00 | 0.00 | 1.00 | 0.06 | 0.00 | 0.04 | 0.86 | 0.01 | 0.06 | PARTIAL |
| point_anomaly | `ar_point_anomaly_single_middle_122.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.54 | 0.00 | 0.17 | 0.93 | 0.00 | 0.15 | PARTIAL |
| point_anomaly | `arma_point_anomaly_multiple_147.csv` | 1.00 | 0.00 | 0.72 | 0.00 | 0.11 | 0.00 | 0.01 | 0.04 | 0.00 | 0.11 | PARTIAL |
| point_anomaly | `arma_point_anomaly_multiple_454.csv` | 1.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.45 | 0.00 | 0.04 | PARTIAL |
| point_anomaly | `arma_point_anomaly_multiple_443.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.18 | 0.00 | 0.39 | PARTIAL |
| point_anomaly | `arma_point_anomaly_single_end_362.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.00 | 0.00 | 0.31 | 0.00 | 0.01 | PARTIAL |
| point_anomaly | `arma_point_anomaly_multiple_869.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.36 | 0.00 | 0.14 | 0.36 | 0.00 | 0.06 | PARTIAL |
| point_anomaly | `arma_point_anomaly_multiple_236.csv` | 1.00 | 0.00 | 0.00 | 0.16 | 0.17 | 0.00 | 0.01 | 0.37 | 0.01 | 0.37 | PARTIAL |
| point_anomaly | `arma_point_anomaly_multiple_66.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.01 | 0.00 | 0.13 | 0.40 | 0.00 | 0.41 | NONE |
| point_anomaly | `arma_point_anomaly_multiple_585.csv` | 1.00 | 0.00 | 0.00 | 0.80 | 0.54 | 0.00 | 1.00 | 0.09 | 0.03 | 0.22 | PARTIAL |
| point_anomaly | `arma_point_anomaly_multiple_20.csv` | 1.00 | 0.00 | 0.83 | 0.00 | 0.40 | 0.00 | 0.76 | 0.12 | 0.00 | 0.09 | PARTIAL |
| point_anomaly | `arma_point_anomaly_multiple_813.csv` | 1.00 | 0.00 | 0.00 | 0.31 | 0.46 | 0.00 | 0.45 | 0.28 | 0.04 | 0.03 | PARTIAL |
| point_anomaly | `arma_point_anomaly_single_beginning_364.csv` | 1.00 | 0.00 | 0.48 | 0.06 | 0.61 | 0.00 | 0.22 | 0.38 | 0.00 | 0.43 | PARTIAL |
| point_anomaly | `arma_point_anomaly_single_beginning_376.csv` | 1.00 | 0.00 | 0.00 | 0.11 | 0.17 | 0.00 | 0.59 | 0.33 | 0.00 | 0.08 | PARTIAL |
| point_anomaly | `arma_point_anomaly_single_beginning_318.csv` | 1.00 | 0.76 | 0.00 | 0.00 | 0.18 | 0.00 | 0.91 | 0.25 | 0.00 | 0.15 | PARTIAL |
| point_anomaly | `arma_point_anomaly_single_beginning_672.csv` | 1.00 | 0.00 | 0.00 | 0.02 | 0.79 | 0.00 | 0.05 | 0.49 | 0.01 | 0.19 | PARTIAL |
| point_anomaly | `arma_point_anomaly_single_end_156.csv` | 1.00 | 0.00 | 0.64 | 0.00 | 0.19 | 0.00 | 0.92 | 0.35 | 0.00 | 0.05 | PARTIAL |
| point_anomaly | `arma_point_anomaly_single_end_20.csv` | 1.00 | 0.00 | 0.00 | 0.02 | 0.70 | 0.00 | 0.29 | 0.38 | 0.01 | 0.74 | PARTIAL |
| point_anomaly | `arma_point_anomaly_single_end_87.csv` | 1.00 | 0.00 | 1.00 | 0.00 | 0.17 | 0.00 | 0.84 | 0.08 | 0.21 | 0.03 | NONE |
| point_anomaly | `arma_point_anomaly_single_end_932.csv` | 1.00 | 0.00 | 0.00 | 0.06 | 0.02 | 0.00 | 0.16 | 0.44 | 0.05 | 0.67 | PARTIAL |
| point_anomaly | `arma_point_anomaly_single_end_681.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.66 | 0.00 | 0.02 | 0.12 | 0.14 | 0.20 | PARTIAL |
| point_anomaly | `arma_point_anomaly_single_middle_367.csv` | 1.00 | 0.00 | 0.00 | 0.02 | 0.06 | 0.00 | 0.00 | 0.50 | 0.02 | 0.95 | PARTIAL |
| point_anomaly | `arma_point_anomaly_single_middle_665.csv` | 1.00 | 0.00 | 0.90 | 0.00 | 0.90 | 0.00 | 0.80 | 0.47 | 0.00 | 0.20 | PARTIAL |
| point_anomaly | `arma_point_anomaly_multiple_32.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.62 | 0.00 | 0.01 | 0.21 | 0.01 | 0.98 | NONE |
| point_anomaly | `arma_point_anomaly_multiple_624.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.07 | 0.00 | 0.02 | 0.30 | 0.00 | 0.99 | NONE |
| point_anomaly | `arma_point_anomaly_multiple_482.csv` | 0.61 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.13 | 0.95 | 0.11 | 0.04 | PARTIAL |
| point_anomaly | `arma_point_anomaly_multiple_270.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.22 | 0.00 | 0.15 | 0.92 | 0.00 | 0.56 | PARTIAL |
| point_anomaly | `arma_point_anomaly_multiple_710.csv` | 0.93 | 0.00 | 0.99 | 1.00 | 0.23 | 0.00 | 1.00 | 0.07 | 0.01 | 0.17 | NONE |
| point_anomaly | `arma_point_anomaly_multiple_714.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.96 | 0.00 | 0.13 | 0.75 | 0.08 | 0.04 | PARTIAL |
| point_anomaly | `arma_point_anomaly_multiple_177.csv` | 1.00 | 0.00 | 0.00 | 0.30 | 0.39 | 0.00 | 0.06 | 0.22 | 0.09 | 0.42 | PARTIAL |
| point_anomaly | `arma_point_anomaly_multiple_581.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.75 | 0.00 | 0.21 | 0.17 | 0.36 | 0.19 | NONE |
| point_anomaly | `arma_point_anomaly_multiple_998.csv` | 0.39 | 0.00 | 0.00 | 1.00 | 0.45 | 0.00 | 0.83 | 0.03 | 0.05 | 0.84 | NONE |
| point_anomaly | `arma_point_anomaly_multiple_430.csv` | 0.01 | 0.00 | 1.00 | 0.00 | 0.46 | 0.00 | 0.13 | 0.94 | 0.09 | 0.05 | PARTIAL |
| point_anomaly | `arma_point_anomaly_single_beginning_160.csv` | 0.96 | 0.00 | 0.00 | 1.00 | 0.96 | 0.00 | 0.12 | 0.46 | 0.84 | 0.06 | NONE |
| point_anomaly | `arma_point_anomaly_single_beginning_978.csv` | 0.89 | 0.00 | 0.00 | 1.00 | 0.26 | 0.00 | 0.30 | 0.53 | 0.13 | 0.31 | PARTIAL |
| point_anomaly | `arma_point_anomaly_single_beginning_583.csv` | 0.94 | 0.00 | 0.00 | 1.00 | 0.39 | 0.00 | 0.14 | 0.43 | 0.00 | 0.14 | NONE |
| point_anomaly | `arma_point_anomaly_single_beginning_566.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.53 | 0.00 | 0.97 | 0.15 | 0.08 | 0.04 | NONE |
| point_anomaly | `arma_point_anomaly_single_beginning_823.csv` | 0.94 | 0.00 | 1.00 | 0.00 | 0.98 | 0.00 | 0.13 | 0.35 | 0.01 | 0.02 | NONE |
| point_anomaly | `arma_point_anomaly_single_beginning_609.csv` | 0.49 | 0.00 | 0.00 | 1.00 | 0.95 | 0.00 | 0.16 | 0.65 | 0.25 | 0.06 | PARTIAL |
| point_anomaly | `arma_point_anomaly_single_beginning_116.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.45 | 0.00 | 0.86 | 0.78 | 0.01 | 0.26 | PARTIAL |
| point_anomaly | `arma_point_anomaly_single_beginning_458.csv` | 0.79 | 0.00 | 0.00 | 1.00 | 0.90 | 0.00 | 0.18 | 0.39 | 0.27 | 0.02 | NONE |
| point_anomaly | `arma_point_anomaly_single_beginning_903.csv` | 0.35 | 0.00 | 0.00 | 1.00 | 0.36 | 0.00 | 0.06 | 0.90 | 0.00 | 0.39 | PARTIAL |
| point_anomaly | `arma_point_anomaly_single_end_138.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.77 | 0.00 | 0.21 | 0.23 | 0.05 | 0.23 | NONE |
| point_anomaly | `arma_point_anomaly_single_end_684.csv` | 1.00 | 0.00 | 0.00 | 0.99 | 0.17 | 0.00 | 0.03 | 0.18 | 0.16 | 0.99 | PARTIAL |
| point_anomaly | `arma_point_anomaly_single_end_455.csv` | 0.84 | 0.00 | 0.00 | 1.00 | 0.55 | 0.00 | 0.77 | 0.09 | 0.08 | 0.81 | NONE |
| point_anomaly | `arma_point_anomaly_single_end_442.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.83 | 0.00 | 0.05 | 0.77 | 0.03 | 0.28 | PARTIAL |
| point_anomaly | `arma_point_anomaly_single_end_331.csv` | 0.83 | 0.00 | 0.00 | 1.00 | 0.37 | 0.00 | 0.03 | 0.61 | 0.01 | 0.13 | PARTIAL |
| point_anomaly | `arma_point_anomaly_single_end_788.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.94 | 0.00 | 0.12 | 0.42 | 0.30 | 0.02 | PARTIAL |
| point_anomaly | `arma_point_anomaly_single_end_112.csv` | 0.94 | 0.00 | 0.00 | 1.00 | 1.00 | 0.00 | 0.02 | 0.64 | 0.10 | 0.02 | PARTIAL |
| point_anomaly | `arma_point_anomaly_single_end_427.csv` | 0.86 | 0.00 | 0.00 | 0.99 | 0.84 | 0.00 | 0.04 | 0.14 | 0.04 | 0.98 | NONE |
| point_anomaly | `arma_point_anomaly_single_end_825.csv` | 0.18 | 0.00 | 0.00 | 1.00 | 0.67 | 0.00 | 0.97 | 0.16 | 0.06 | 0.03 | NONE |
| point_anomaly | `arma_point_anomaly_single_middle_160.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.20 | 0.92 | 0.01 | 0.51 | PARTIAL |
| point_anomaly | `arma_point_anomaly_single_middle_32.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.77 | 0.00 | 0.14 | 0.71 | 0.01 | 0.62 | PARTIAL |
| point_anomaly | `arma_point_anomaly_single_middle_774.csv` | 0.61 | 0.00 | 0.00 | 1.00 | 0.85 | 0.00 | 0.01 | 0.78 | 0.02 | 0.12 | PARTIAL |
| point_anomaly | `arma_point_anomaly_single_middle_678.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.75 | 0.00 | 0.01 | 0.64 | 0.14 | 0.95 | PARTIAL |
| point_anomaly | `arma_point_anomaly_single_middle_194.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.09 | 0.94 | 0.04 | 0.08 | PARTIAL |
| point_anomaly | `arma_point_anomaly_single_middle_81.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 1.00 | 0.00 | 0.05 | 0.46 | 0.49 | 0.14 | NONE |
| point_anomaly | `arma_point_anomaly_single_middle_776.csv` | 0.96 | 0.00 | 0.00 | 0.97 | 0.59 | 0.00 | 0.43 | 0.86 | 0.29 | 0.01 | PARTIAL |
| point_anomaly | `ma_point_anomaly_multiple_139.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.36 | 0.00 | 0.03 | PARTIAL |
| point_anomaly | `ma_point_anomaly_multiple_422.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.14 | 0.00 | 0.02 | 0.42 | 0.00 | 0.02 | PARTIAL |
| point_anomaly | `ma_point_anomaly_multiple_601.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.48 | 0.00 | 0.04 | PARTIAL |
| point_anomaly | `ma_point_anomaly_multiple_41.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.09 | 0.00 | 0.01 | 0.42 | 0.00 | 0.01 | PARTIAL |
| point_anomaly | `ma_point_anomaly_multiple_26.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.25 | 0.00 | 0.00 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_beginning_526.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.02 | 0.31 | 0.00 | 0.01 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_beginning_266.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.00 | 0.05 | 0.50 | 0.00 | 0.00 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_end_759.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.19 | 0.00 | 0.01 | 0.13 | 0.00 | 0.02 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_end_52.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.01 | 0.12 | 0.00 | 0.00 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_middle_384.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.29 | 0.00 | 0.01 | PARTIAL |
| point_anomaly | `ma_point_anomaly_multiple_534.csv` | 1.00 | 0.00 | 0.00 | 0.27 | 0.01 | 0.00 | 0.06 | 0.29 | 0.03 | 0.07 | PARTIAL |
| point_anomaly | `ma_point_anomaly_multiple_331.csv` | 1.00 | 0.00 | 0.00 | 0.04 | 0.10 | 0.00 | 0.20 | 0.43 | 0.00 | 0.22 | PARTIAL |
| point_anomaly | `ma_point_anomaly_multiple_131.csv` | 1.00 | 0.00 | 0.00 | 0.64 | 0.37 | 0.00 | 0.05 | 0.37 | 0.01 | 0.11 | PARTIAL |
| point_anomaly | `ma_point_anomaly_multiple_274.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.06 | 0.00 | 0.94 | 0.28 | 0.00 | 0.38 | NONE |
| point_anomaly | `ma_point_anomaly_multiple_427.csv` | 1.00 | 0.00 | 0.00 | 0.81 | 0.60 | 0.00 | 0.41 | 0.11 | 0.01 | 0.43 | PARTIAL |
| point_anomaly | `ma_point_anomaly_multiple_893.csv` | 1.00 | 0.00 | 0.00 | 0.17 | 0.11 | 0.00 | 0.02 | 0.39 | 0.01 | 0.65 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_beginning_897.csv` | 1.00 | 0.00 | 0.00 | 0.94 | 0.05 | 0.00 | 0.01 | 0.30 | 0.00 | 0.91 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_beginning_702.csv` | 1.00 | 0.00 | 0.30 | 0.00 | 0.89 | 0.00 | 0.98 | 0.19 | 0.00 | 0.05 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_beginning_35.csv` | 1.00 | 0.00 | 0.00 | 0.57 | 0.27 | 0.00 | 0.64 | 0.37 | 0.03 | 0.11 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_beginning_437.csv` | 1.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.04 | 0.42 | 0.00 | 0.04 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_beginning_918.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.04 | 0.76 | 0.00 | 0.94 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_end_784.csv` | 1.00 | 0.00 | 0.76 | 0.00 | 0.98 | 0.00 | 0.53 | 0.43 | 0.00 | 0.13 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_end_503.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.86 | 0.00 | 0.64 | 0.32 | 0.01 | 0.05 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_end_410.csv` | 1.00 | 0.00 | 0.00 | 0.06 | 0.95 | 0.00 | 0.21 | 0.15 | 0.00 | 0.25 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_end_556.csv` | 0.99 | 0.00 | 0.00 | 0.90 | 0.02 | 0.00 | 0.28 | 0.31 | 0.00 | 0.94 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_middle_769.csv` | 1.00 | 0.00 | 0.00 | 0.01 | 0.25 | 0.00 | 0.01 | 0.46 | 0.01 | 0.26 | PARTIAL |
| point_anomaly | `ma_point_anomaly_multiple_49.csv` | 0.85 | 0.00 | 0.00 | 1.00 | 0.63 | 0.00 | 0.11 | 0.59 | 0.20 | 0.03 | PARTIAL |
| point_anomaly | `ma_point_anomaly_multiple_170.csv` | 0.08 | 0.00 | 0.00 | 1.00 | 0.93 | 0.00 | 0.99 | 0.76 | 0.06 | 0.19 | PARTIAL |
| point_anomaly | `ma_point_anomaly_multiple_495.csv` | 0.93 | 0.00 | 0.00 | 1.00 | 0.91 | 0.00 | 0.12 | 0.13 | 0.05 | 0.84 | NONE |
| point_anomaly | `ma_point_anomaly_multiple_653.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.39 | 0.00 | 0.01 | 0.92 | 0.02 | 0.45 | PARTIAL |
| point_anomaly | `ma_point_anomaly_multiple_857.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.86 | 0.00 | 0.82 | 0.69 | 0.02 | 0.17 | PARTIAL |
| point_anomaly | `ma_point_anomaly_multiple_264.csv` | 0.00 | 0.00 | 0.00 | 1.00 | 0.96 | 0.00 | 0.02 | 0.98 | 0.00 | 0.87 | PARTIAL |
| point_anomaly | `ma_point_anomaly_multiple_369.csv` | 0.87 | 0.00 | 0.00 | 1.00 | 0.85 | 0.00 | 0.44 | 0.74 | 0.00 | 0.09 | PARTIAL |
| point_anomaly | `ma_point_anomaly_multiple_394.csv` | 0.92 | 0.00 | 0.00 | 1.00 | 0.95 | 0.00 | 0.12 | 0.87 | 0.03 | 0.91 | PARTIAL |
| point_anomaly | `ma_point_anomaly_multiple_193.csv` | 0.33 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.27 | 0.51 | 0.26 | 0.24 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_beginning_171.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.72 | 0.00 | 0.02 | 0.95 | 0.04 | 0.57 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_beginning_40.csv` | 0.88 | 0.00 | 0.00 | 1.00 | 0.86 | 0.00 | 0.20 | 0.23 | 0.01 | 0.40 | NONE |
| point_anomaly | `ma_point_anomaly_single_beginning_707.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.89 | 0.00 | 0.03 | 0.76 | 0.04 | 0.06 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_beginning_370.csv` | 0.95 | 0.00 | 0.00 | 1.00 | 0.91 | 0.00 | 0.04 | 0.33 | 0.02 | 0.26 | NONE |
| point_anomaly | `ma_point_anomaly_single_beginning_380.csv` | 0.90 | 0.00 | 0.13 | 1.00 | 0.41 | 0.00 | 0.92 | 0.33 | 0.10 | 0.11 | NONE |
| point_anomaly | `ma_point_anomaly_single_beginning_509.csv` | 0.69 | 0.00 | 0.00 | 1.00 | 0.66 | 0.00 | 0.11 | 0.46 | 0.11 | 0.48 | NONE |
| point_anomaly | `ma_point_anomaly_single_beginning_654.csv` | 0.00 | 0.00 | 0.00 | 1.00 | 0.97 | 0.00 | 0.05 | 0.98 | 0.02 | 0.12 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_beginning_76.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.65 | 0.00 | 0.15 | 0.72 | 0.13 | 0.14 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_beginning_491.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.82 | 0.00 | 0.82 | 0.47 | 0.16 | 0.01 | NONE |
| point_anomaly | `ma_point_anomaly_single_beginning_251.csv` | 0.14 | 0.00 | 0.00 | 1.00 | 0.52 | 0.00 | 0.02 | 0.90 | 0.00 | 0.41 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_end_734.csv` | 0.85 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.02 | 0.91 | 0.03 | 0.72 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_end_507.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.69 | 0.24 | 0.40 | 0.01 | NONE |
| point_anomaly | `ma_point_anomaly_single_end_421.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.95 | 0.00 | 0.95 | 0.39 | 0.35 | 0.01 | NONE |
| point_anomaly | `ma_point_anomaly_single_end_51.csv` | 0.33 | 0.00 | 0.00 | 1.00 | 0.94 | 0.00 | 0.99 | 0.51 | 0.46 | 0.05 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_end_137.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.96 | 0.00 | 0.04 | 0.52 | 0.03 | 0.67 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_end_769.csv` | 0.94 | 0.00 | 0.99 | 1.00 | 0.88 | 0.00 | 0.99 | 0.40 | 0.12 | 0.05 | NONE |
| point_anomaly | `ma_point_anomaly_single_end_90.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 1.00 | 0.00 | 0.13 | 0.71 | 0.16 | 0.37 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_end_939.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.92 | 0.00 | 0.04 | 0.72 | 0.43 | 0.05 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_end_423.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.82 | 0.00 | 0.29 | 0.37 | 0.68 | 0.63 | NONE |
| point_anomaly | `ma_point_anomaly_single_end_665.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.77 | 0.00 | 0.02 | 0.79 | 0.01 | 0.87 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_middle_351.csv` | 0.50 | 0.00 | 0.00 | 1.00 | 0.39 | 0.00 | 0.09 | 0.78 | 0.00 | 0.06 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_middle_828.csv` | 0.91 | 0.00 | 0.00 | 1.00 | 0.95 | 0.00 | 0.79 | 0.95 | 0.10 | 0.01 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_middle_972.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.04 | 0.75 | 0.51 | 0.11 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_middle_150.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.85 | 0.00 | 0.02 | 0.94 | 0.01 | 0.55 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_middle_167.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.77 | 0.00 | 0.01 | 0.91 | 0.02 | 0.04 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_middle_717.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.76 | 0.00 | 0.12 | 0.81 | 0.23 | 0.16 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_middle_686.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.23 | 0.00 | 0.10 | 0.84 | 0.05 | 0.87 | PARTIAL |
| point_anomaly | `ma_point_anomaly_single_middle_472.csv` | 0.35 | 0.00 | 0.00 | 1.00 | 0.91 | 0.00 | 0.65 | 0.86 | 0.41 | 0.05 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_single_beginning_723.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.01 | 0.29 | 0.00 | 0.01 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_single_beginning_315.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.01 | 0.05 | 0.00 | 0.01 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_single_end_436.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.05 | 0.48 | 0.00 | 0.01 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_single_end_620.csv` | 1.00 | 0.00 | 0.00 | 0.03 | 0.02 | 0.00 | 0.03 | 0.49 | 0.00 | 0.01 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_multiple_984.csv` | 1.00 | 0.00 | 0.00 | 0.99 | 0.05 | 0.00 | 0.02 | 0.24 | 0.00 | 0.64 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_multiple_27.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.07 | 0.00 | 0.09 | 0.83 | 0.00 | 0.49 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_single_beginning_559.csv` | 1.00 | 0.00 | 0.00 | 0.58 | 0.43 | 0.00 | 0.59 | 0.46 | 0.01 | 0.23 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_single_beginning_576.csv` | 1.00 | 0.00 | 0.00 | 0.39 | 0.02 | 0.00 | 0.14 | 0.20 | 0.01 | 0.21 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_single_beginning_812.csv` | 0.99 | 0.00 | 0.00 | 0.88 | 0.05 | 0.00 | 0.52 | 0.49 | 0.01 | 0.20 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_single_end_662.csv` | 1.00 | 0.00 | 0.00 | 0.84 | 0.07 | 0.00 | 0.05 | 0.10 | 0.00 | 0.32 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_single_end_550.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.15 | 0.00 | 0.29 | 0.93 | 0.00 | 0.01 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_single_middle_885.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.04 | 0.00 | 0.37 | 0.72 | 0.00 | 0.07 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_single_middle_166.csv` | 0.94 | 0.00 | 0.00 | 1.00 | 0.09 | 0.00 | 0.04 | 0.72 | 0.00 | 0.27 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_single_middle_927.csv` | 1.00 | 0.00 | 0.00 | 0.01 | 0.02 | 0.00 | 0.89 | 0.37 | 0.02 | 0.01 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_multiple_990.csv` | 0.46 | 0.00 | 0.00 | 1.00 | 1.00 | 0.00 | 0.02 | 0.30 | 0.14 | 0.96 | NONE |
| point_anomaly | `white_noise_point_anomaly_multiple_878.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.97 | 0.00 | 0.11 | 0.68 | 0.17 | 0.02 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_multiple_713.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.87 | 0.00 | 0.11 | 0.71 | 0.64 | 0.37 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_multiple_418.csv` | 0.84 | 0.00 | 0.00 | 1.00 | 0.65 | 0.00 | 0.37 | 0.92 | 0.03 | 0.11 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_multiple_752.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.10 | 0.58 | 0.24 | 0.04 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_multiple_158.csv` | 0.94 | 0.00 | 0.00 | 1.00 | 0.91 | 0.00 | 0.23 | 0.39 | 0.89 | 0.18 | NONE |
| point_anomaly | `white_noise_point_anomaly_multiple_605.csv` | 0.64 | 0.00 | 0.00 | 1.00 | 0.96 | 0.00 | 0.06 | 0.56 | 0.05 | 0.06 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_multiple_599.csv` | 0.87 | 0.00 | 0.00 | 1.00 | 1.00 | 0.00 | 0.02 | 0.77 | 0.08 | 0.72 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_multiple_366.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.87 | 0.00 | 0.00 | 0.88 | 0.01 | 0.48 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_single_beginning_92.csv` | 0.91 | 0.00 | 0.00 | 1.00 | 0.81 | 0.00 | 0.24 | 0.33 | 0.04 | 0.13 | NONE |
| point_anomaly | `white_noise_point_anomaly_single_beginning_375.csv` | 0.18 | 0.00 | 0.00 | 1.00 | 0.80 | 0.00 | 0.26 | 0.77 | 0.02 | 0.23 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_single_beginning_883.csv` | 0.93 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.09 | 0.33 | 0.05 | 0.06 | NONE |
| point_anomaly | `white_noise_point_anomaly_single_beginning_243.csv` | 0.88 | 0.00 | 0.00 | 1.00 | 0.93 | 0.00 | 0.98 | 0.35 | 0.10 | 0.05 | NONE |
| point_anomaly | `white_noise_point_anomaly_single_beginning_754.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.24 | 0.00 | 0.12 | 0.67 | 0.02 | 0.48 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_single_beginning_752.csv` | 0.96 | 0.00 | 0.00 | 1.00 | 0.68 | 0.00 | 0.02 | 0.42 | 0.17 | 0.03 | NONE |
| point_anomaly | `white_noise_point_anomaly_single_beginning_953.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.68 | 0.00 | 0.17 | 0.66 | 0.05 | 0.01 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_single_beginning_744.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.75 | 0.00 | 0.02 | 0.82 | 0.00 | 0.46 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_single_beginning_687.csv` | 0.67 | 0.00 | 0.00 | 1.00 | 1.00 | 0.00 | 0.03 | 0.91 | 0.00 | 0.78 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_single_beginning_259.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.47 | 0.00 | 0.16 | 0.51 | 0.00 | 0.22 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_single_end_83.csv` | 0.56 | 0.00 | 0.00 | 1.00 | 0.67 | 0.00 | 0.13 | 0.17 | 0.02 | 0.36 | NONE |
| point_anomaly | `white_noise_point_anomaly_single_end_431.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.46 | 0.00 | 0.88 | 0.08 | 0.16 | 0.93 | NONE |
| point_anomaly | `white_noise_point_anomaly_single_end_567.csv` | 0.48 | 0.00 | 0.00 | 1.00 | 0.87 | 0.00 | 0.11 | 0.73 | 0.49 | 0.02 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_single_end_304.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 1.00 | 0.00 | 0.02 | 0.65 | 0.19 | 0.14 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_single_end_21.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.38 | 0.00 | 0.03 | 0.23 | 0.01 | 0.12 | NONE |
| point_anomaly | `white_noise_point_anomaly_single_end_283.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.94 | 0.00 | 0.09 | 0.63 | 0.58 | 0.05 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_single_end_829.csv` | 0.82 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.07 | 0.28 | 0.04 | 0.06 | NONE |
| point_anomaly | `white_noise_point_anomaly_single_end_226.csv` | 0.45 | 0.00 | 0.00 | 1.00 | 0.90 | 0.00 | 0.04 | 0.43 | 0.03 | 0.18 | NONE |
| point_anomaly | `white_noise_point_anomaly_single_end_316.csv` | 0.18 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.04 | 0.17 | 0.04 | 0.08 | NONE |
| point_anomaly | `white_noise_point_anomaly_single_end_827.csv` | 0.95 | 0.00 | 0.00 | 1.00 | 1.00 | 0.00 | 0.03 | 0.25 | 0.19 | 0.54 | NONE |
| point_anomaly | `white_noise_point_anomaly_single_middle_553.csv` | 0.94 | 0.00 | 0.00 | 1.00 | 0.60 | 0.00 | 0.04 | 0.95 | 0.00 | 0.29 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_single_middle_121.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.97 | 0.00 | 0.95 | 0.92 | 0.11 | 0.07 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_single_middle_430.csv` | 0.01 | 0.00 | 0.00 | 1.00 | 0.63 | 0.00 | 0.01 | 0.73 | 0.00 | 0.37 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_single_middle_609.csv` | 0.89 | 0.00 | 0.00 | 1.00 | 0.85 | 0.00 | 0.41 | 0.73 | 0.02 | 0.10 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_single_middle_626.csv` | 0.51 | 0.00 | 0.00 | 1.00 | 0.96 | 0.00 | 0.10 | 0.87 | 0.01 | 0.40 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_single_middle_438.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 1.00 | 0.00 | 0.11 | 0.55 | 0.18 | 0.03 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_single_middle_529.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.07 | 0.96 | 0.05 | 0.19 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_single_middle_839.csv` | 0.85 | 0.00 | 0.00 | 1.00 | 0.55 | 0.00 | 0.99 | 0.19 | 0.14 | 0.05 | NONE |
| point_anomaly | `white_noise_point_anomaly_single_middle_606.csv` | 0.94 | 0.00 | 0.00 | 1.00 | 0.95 | 0.00 | 0.10 | 0.87 | 0.26 | 0.06 | PARTIAL |
| point_anomaly | `white_noise_point_anomaly_single_middle_217.csv` | 0.07 | 0.00 | 0.00 | 1.00 | 0.96 | 0.00 | 0.97 | 0.97 | 0.00 | 0.08 | PARTIAL |
| trend_shift | `ar_trend_shift_465.csv` | 0.82 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.98 | 0.02 | PARTIAL |
| trend_shift | `ar_trend_shift_351.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.99 | 0.01 | 0.05 | 0.51 | PARTIAL |
| trend_shift | `ar_trend_shift_561.csv` | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.04 | 0.91 | 0.00 | PARTIAL |
| trend_shift | `ar_trend_shift_644.csv` | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.16 | 0.01 | 0.90 | 0.00 | PARTIAL |
| trend_shift | `ar_trend_shift_256.csv` | 0.65 | 0.00 | 1.00 | 0.02 | 0.59 | 0.00 | 0.89 | 0.21 | 0.97 | 0.02 | PARTIAL |
| trend_shift | `ar_trend_shift_674.csv` | 0.94 | 0.00 | 0.00 | 1.00 | 0.84 | 0.00 | 0.98 | 0.40 | 0.16 | 0.02 | NONE |
| trend_shift | `ar_trend_shift_762.csv` | 0.42 | 0.00 | 1.00 | 0.00 | 0.01 | 0.00 | 0.66 | 0.10 | 0.97 | 0.01 | PARTIAL |
| trend_shift | `ar_trend_shift_93.csv` | 0.32 | 0.00 | 1.00 | 0.00 | 0.07 | 0.00 | 0.64 | 0.19 | 0.97 | 0.00 | PARTIAL |
| trend_shift | `ar_trend_shift_656.csv` | 1.00 | 0.00 | 1.00 | 0.00 | 0.05 | 0.00 | 0.86 | 0.09 | 0.99 | 0.01 | PARTIAL |
| trend_shift | `ar_trend_shift_409.csv` | 0.81 | 0.00 | 1.00 | 0.00 | 0.03 | 0.00 | 0.83 | 0.27 | 0.99 | 0.01 | PARTIAL |
| trend_shift | `ar_trend_shift_950.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.58 | 0.00 | 0.77 | 0.90 | 0.84 | 0.06 | PARTIAL |
| trend_shift | `ar_trend_shift_618.csv` | 0.73 | 0.00 | 0.00 | 1.00 | 0.01 | 0.00 | 1.00 | 0.16 | 0.94 | 0.03 | PARTIAL |
| trend_shift | `ar_trend_shift_86.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.53 | 0.00 | 1.00 | 0.12 | 0.90 | 0.01 | PARTIAL |
| trend_shift | `ar_trend_shift_895.csv` | 0.99 | 0.00 | 1.00 | 0.00 | 0.03 | 0.00 | 0.70 | 0.25 | 0.99 | 0.00 | PARTIAL |
| trend_shift | `ar_trend_shift_124.csv` | 0.73 | 0.00 | 0.75 | 0.00 | 0.00 | 0.00 | 0.08 | 0.33 | 0.96 | 0.00 | PARTIAL |
| trend_shift | `ar_trend_shift_973.csv` | 0.43 | 0.00 | 1.00 | 0.00 | 0.74 | 0.00 | 0.88 | 0.19 | 0.20 | 0.08 | NONE |
| trend_shift | `ar_trend_shift_699.csv` | 0.93 | 0.00 | 1.00 | 0.00 | 0.01 | 0.00 | 0.14 | 0.58 | 0.98 | 0.01 | PARTIAL |
| trend_shift | `ar_trend_shift_625.csv` | 0.76 | 0.00 | 1.00 | 0.00 | 0.02 | 0.00 | 0.79 | 0.53 | 1.00 | 0.01 | PARTIAL |
| trend_shift | `ar_trend_shift_482.csv` | 0.95 | 0.00 | 1.00 | 0.00 | 0.13 | 0.00 | 0.16 | 0.31 | 0.90 | 0.57 | PARTIAL |
| trend_shift | `ar_trend_shift_668.csv` | 0.83 | 0.00 | 0.00 | 1.00 | 0.84 | 0.00 | 1.00 | 0.13 | 0.12 | 0.00 | NONE |
| trend_shift | `ar_trend_shift_688.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.96 | 0.00 | 0.95 | 0.34 | 0.35 | 0.06 | NONE |
| trend_shift | `ar_trend_shift_126.csv` | 0.78 | 0.00 | 0.00 | 1.00 | 0.85 | 0.00 | 0.97 | 0.24 | 0.27 | 0.13 | NONE |
| trend_shift | `ar_trend_shift_557.csv` | 0.97 | 0.00 | 1.00 | 0.00 | 0.02 | 0.00 | 0.20 | 0.60 | 0.99 | 0.01 | PARTIAL |
| trend_shift | `ar_trend_shift_918.csv` | 0.31 | 0.00 | 1.00 | 0.80 | 0.81 | 0.00 | 0.91 | 0.90 | 0.81 | 0.24 | PARTIAL |
| trend_shift | `ar_trend_shift_677.csv` | 1.00 | 0.00 | 0.00 | 0.99 | 0.99 | 0.00 | 0.73 | 0.04 | 0.38 | 0.07 | PARTIAL |
| trend_shift | `ar_trend_shift_365.csv` | 0.93 | 0.00 | 0.99 | 0.00 | 0.01 | 0.00 | 0.84 | 0.39 | 0.99 | 0.00 | PARTIAL |
| trend_shift | `ar_trend_shift_690.csv` | 0.65 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.18 | 0.41 | 0.93 | 0.01 | PARTIAL |
| trend_shift | `ar_trend_shift_980.csv` | 0.85 | 0.00 | 1.00 | 0.00 | 0.20 | 0.00 | 0.98 | 0.69 | 0.99 | 0.00 | PARTIAL |
| trend_shift | `ar_trend_shift_377.csv` | 0.38 | 0.00 | 0.00 | 1.00 | 0.97 | 0.00 | 0.06 | 0.25 | 0.06 | 0.04 | NONE |
| trend_shift | `ar_trend_shift_543.csv` | 0.94 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.60 | 0.85 | 0.38 | 0.04 | NONE |
| trend_shift | `ar_trend_shift_323.csv` | 0.96 | 0.00 | 1.00 | 0.00 | 0.28 | 0.00 | 0.94 | 0.15 | 0.98 | 0.00 | PARTIAL |
| trend_shift | `ar_trend_shift_840.csv` | 0.99 | 0.00 | 1.00 | 0.00 | 0.20 | 0.00 | 0.50 | 0.57 | 1.00 | 0.01 | PARTIAL |
| trend_shift | `arma_trend_shift_218.csv` | 0.94 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.55 | 0.01 | 0.18 | 0.01 | PARTIAL |
| trend_shift | `arma_trend_shift_564.csv` | 0.99 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.98 | 0.01 | 0.44 | 0.77 | PARTIAL |
| trend_shift | `arma_trend_shift_144.csv` | 0.89 | 0.00 | 0.00 | 1.00 | 0.54 | 0.00 | 1.00 | 0.06 | 0.96 | 0.01 | PARTIAL |
| trend_shift | `arma_trend_shift_358.csv` | 0.32 | 0.00 | 0.00 | 1.00 | 0.91 | 0.00 | 0.64 | 0.37 | 0.70 | 0.10 | PARTIAL |
| trend_shift | `arma_trend_shift_554.csv` | 0.16 | 0.00 | 1.00 | 0.04 | 0.36 | 0.00 | 0.02 | 0.54 | 0.38 | 0.89 | NONE |
| trend_shift | `arma_trend_shift_649.csv` | 0.17 | 0.00 | 1.00 | 0.18 | 0.11 | 0.00 | 0.98 | 0.05 | 0.97 | 0.18 | PARTIAL |
| trend_shift | `arma_trend_shift_911.csv` | 0.91 | 0.00 | 0.97 | 0.89 | 0.13 | 0.00 | 0.21 | 0.16 | 1.00 | 0.18 | PARTIAL |
| trend_shift | `arma_trend_shift_876.csv` | 0.54 | 0.00 | 0.00 | 1.00 | 0.02 | 0.00 | 0.99 | 0.21 | 0.95 | 0.19 | PARTIAL |
| trend_shift | `arma_trend_shift_700.csv` | 0.11 | 0.00 | 0.00 | 1.00 | 0.66 | 0.00 | 0.96 | 0.05 | 0.48 | 0.40 | NONE |
| trend_shift | `arma_trend_shift_718.csv` | 0.96 | 0.00 | 1.00 | 0.00 | 0.03 | 0.00 | 0.18 | 0.74 | 0.99 | 0.00 | PARTIAL |
| trend_shift | `arma_trend_shift_531.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.89 | 0.00 | 0.45 | 0.70 | 0.14 | 0.01 | NONE |
| trend_shift | `arma_trend_shift_361.csv` | 0.05 | 0.00 | 1.00 | 0.00 | 0.05 | 0.00 | 0.78 | 0.28 | 0.72 | 0.00 | PARTIAL |
| trend_shift | `arma_trend_shift_593.csv` | 0.96 | 0.00 | 1.00 | 0.00 | 0.06 | 0.00 | 0.53 | 0.28 | 0.98 | 0.00 | PARTIAL |
| trend_shift | `arma_trend_shift_105.csv` | 0.97 | 0.00 | 1.00 | 0.00 | 0.05 | 0.00 | 0.89 | 0.11 | 1.00 | 0.00 | PARTIAL |
| trend_shift | `arma_trend_shift_198.csv` | 0.81 | 0.02 | 0.98 | 0.00 | 0.00 | 0.00 | 0.06 | 0.65 | 0.98 | 0.00 | PARTIAL |
| trend_shift | `arma_trend_shift_496.csv` | 0.07 | 0.00 | 0.00 | 1.00 | 0.92 | 0.00 | 1.00 | 0.31 | 0.06 | 0.04 | NONE |
| trend_shift | `arma_trend_shift_221.csv` | 0.35 | 0.00 | 0.99 | 0.00 | 0.00 | 0.00 | 0.87 | 0.33 | 0.97 | 0.00 | PARTIAL |
| trend_shift | `arma_trend_shift_911.csv` | 0.87 | 0.00 | 0.90 | 0.00 | 0.04 | 0.00 | 0.61 | 0.17 | 0.99 | 0.16 | PARTIAL |
| trend_shift | `arma_trend_shift_341.csv` | 0.94 | 0.00 | 1.00 | 0.00 | 0.06 | 0.00 | 0.52 | 0.17 | 0.99 | 0.01 | PARTIAL |
| trend_shift | `arma_trend_shift_769.csv` | 0.99 | 0.00 | 1.00 | 0.00 | 0.01 | 0.00 | 0.75 | 0.38 | 1.00 | 0.01 | PARTIAL |
| trend_shift | `arma_trend_shift_435.csv` | 0.40 | 0.00 | 0.95 | 0.00 | 0.00 | 0.00 | 0.10 | 0.65 | 0.99 | 0.00 | PARTIAL |
| trend_shift | `arma_trend_shift_802.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.89 | 0.00 | 0.96 | 0.34 | 0.96 | 0.05 | PARTIAL |
| trend_shift | `arma_trend_shift_47.csv` | 0.13 | 0.00 | 0.00 | 1.00 | 0.36 | 0.00 | 0.03 | 0.43 | 0.01 | 0.59 | NONE |
| trend_shift | `arma_trend_shift_435.csv` | 0.02 | 0.00 | 1.00 | 0.00 | 0.98 | 0.00 | 0.46 | 0.05 | 0.07 | 0.03 | NONE |
| trend_shift | `arma_trend_shift_468.csv` | 0.47 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.93 | 0.16 | 0.97 | 0.01 | PARTIAL |
| trend_shift | `arma_trend_shift_145.csv` | 0.57 | 0.00 | 0.00 | 1.00 | 0.06 | 0.00 | 0.99 | 0.22 | 0.12 | 0.06 | NONE |
| trend_shift | `arma_trend_shift_278.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.87 | 0.00 | 0.98 | 0.14 | 0.63 | 0.19 | PARTIAL |
| trend_shift | `arma_trend_shift_432.csv` | 0.94 | 0.00 | 0.00 | 1.00 | 0.26 | 0.00 | 0.99 | 0.01 | 0.96 | 0.09 | PARTIAL |
| trend_shift | `arma_trend_shift_608.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.93 | 0.00 | 0.17 | 0.27 | 0.88 | 0.03 | PARTIAL |
| trend_shift | `arma_trend_shift_454.csv` | 0.83 | 0.00 | 1.00 | 0.00 | 0.08 | 0.00 | 0.88 | 0.31 | 0.99 | 0.00 | PARTIAL |
| trend_shift | `arma_trend_shift_563.csv` | 0.96 | 0.00 | 1.00 | 0.00 | 0.15 | 0.00 | 0.05 | 0.81 | 0.99 | 0.00 | PARTIAL |
| trend_shift | `arma_trend_shift_513.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.13 | 0.00 | 1.00 | 0.09 | 1.00 | 0.02 | PARTIAL |
| trend_shift | `arma_trend_shift_605.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.70 | 0.08 | 0.81 | 0.29 | PARTIAL |
| trend_shift | `arma_trend_shift_356.csv` | 0.86 | 0.00 | 0.00 | 1.00 | 0.16 | 0.00 | 0.97 | 0.17 | 0.94 | 0.39 | PARTIAL |
| trend_shift | `ma_trend_shift_577.csv` | 0.04 | 0.37 | 0.00 | 0.00 | 0.00 | 0.00 | 0.27 | 0.00 | 0.19 | 0.03 | NONE |
| trend_shift | `ma_trend_shift_631.csv` | 0.02 | 0.00 | 1.00 | 0.00 | 0.52 | 0.00 | 0.73 | 0.14 | 0.77 | 0.01 | PARTIAL |
| trend_shift | `ma_trend_shift_308.csv` | 0.58 | 0.00 | 0.00 | 1.00 | 0.63 | 0.00 | 0.29 | 0.18 | 0.99 | 0.11 | PARTIAL |
| trend_shift | `ma_trend_shift_763.csv` | 0.03 | 0.00 | 1.00 | 0.00 | 0.01 | 0.00 | 0.54 | 0.11 | 0.81 | 0.00 | PARTIAL |
| trend_shift | `ma_trend_shift_145.csv` | 0.59 | 0.00 | 1.00 | 0.00 | 0.04 | 0.00 | 0.96 | 0.26 | 0.99 | 0.00 | PARTIAL |
| trend_shift | `ma_trend_shift_636.csv` | 0.51 | 0.00 | 0.19 | 1.00 | 0.82 | 0.00 | 0.99 | 0.15 | 0.60 | 0.02 | PARTIAL |
| trend_shift | `ma_trend_shift_540.csv` | 0.55 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.85 | 0.07 | 0.32 | 0.07 | NONE |
| trend_shift | `ma_trend_shift_255.csv` | 0.98 | 0.00 | 1.00 | 0.00 | 0.08 | 0.00 | 0.95 | 0.30 | 0.99 | 0.00 | PARTIAL |
| trend_shift | `ma_trend_shift_581.csv` | 0.74 | 0.00 | 0.00 | 1.00 | 0.97 | 0.00 | 0.40 | 0.43 | 0.86 | 0.04 | PARTIAL |
| trend_shift | `ma_trend_shift_679.csv` | 0.90 | 0.00 | 0.99 | 0.00 | 0.01 | 0.00 | 0.15 | 0.57 | 0.99 | 0.00 | PARTIAL |
| trend_shift | `ma_trend_shift_763.csv` | 0.98 | 0.00 | 1.00 | 0.00 | 0.12 | 0.00 | 0.89 | 0.30 | 1.00 | 0.00 | PARTIAL |
| trend_shift | `ma_trend_shift_67.csv` | 0.74 | 0.00 | 1.00 | 0.00 | 0.76 | 0.00 | 0.98 | 0.04 | 0.82 | 0.01 | PARTIAL |
| trend_shift | `ma_trend_shift_812.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.80 | 0.00 | 0.91 | 0.24 | 0.95 | 0.12 | PARTIAL |
| trend_shift | `ma_trend_shift_449.csv` | 0.94 | 0.00 | 1.00 | 0.00 | 0.01 | 0.00 | 0.21 | 0.59 | 0.99 | 0.00 | PARTIAL |
| trend_shift | `ma_trend_shift_234.csv` | 0.91 | 0.00 | 0.00 | 1.00 | 0.23 | 0.00 | 0.99 | 0.06 | 0.99 | 0.03 | PARTIAL |
| trend_shift | `ma_trend_shift_321.csv` | 0.82 | 0.00 | 0.99 | 0.00 | 0.02 | 0.00 | 0.89 | 0.23 | 0.93 | 0.00 | PARTIAL |
| trend_shift | `ma_trend_shift_127.csv` | 0.96 | 0.00 | 1.00 | 0.00 | 0.13 | 0.00 | 0.98 | 0.28 | 0.98 | 0.01 | PARTIAL |
| trend_shift | `ma_trend_shift_626.csv` | 0.44 | 0.00 | 1.00 | 0.97 | 0.34 | 0.00 | 0.97 | 0.08 | 0.98 | 0.02 | PARTIAL |
| trend_shift | `ma_trend_shift_744.csv` | 0.54 | 0.00 | 0.99 | 0.00 | 0.03 | 0.00 | 0.16 | 0.25 | 0.99 | 0.01 | PARTIAL |
| trend_shift | `ma_trend_shift_274.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.96 | 0.00 | 0.82 | 0.18 | 0.82 | 0.03 | PARTIAL |
| trend_shift | `ma_trend_shift_388.csv` | 0.93 | 0.00 | 0.00 | 1.00 | 0.14 | 0.00 | 0.98 | 0.05 | 0.97 | 0.47 | PARTIAL |
| trend_shift | `ma_trend_shift_238.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 1.00 | 0.00 | 0.51 | 0.71 | 0.99 | 0.01 | PARTIAL |
| trend_shift | `ma_trend_shift_735.csv` | 0.74 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.23 | 0.68 | 0.13 | 0.09 | NONE |
| trend_shift | `ma_trend_shift_286.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.51 | 0.00 | 0.47 | 0.83 | 0.98 | 0.05 | PARTIAL |
| trend_shift | `ma_trend_shift_477.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 1.00 | 0.00 | 0.77 | 0.14 | 0.46 | 0.01 | NONE |
| trend_shift | `ma_trend_shift_560.csv` | 0.44 | 0.00 | 0.00 | 1.00 | 0.97 | 0.00 | 0.91 | 0.14 | 0.87 | 0.06 | PARTIAL |
| trend_shift | `ma_trend_shift_812.csv` | 0.91 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.62 | 0.20 | 0.72 | 0.04 | PARTIAL |
| trend_shift | `ma_trend_shift_947.csv` | 0.99 | 0.00 | 1.00 | 0.00 | 0.02 | 0.00 | 0.14 | 0.64 | 0.99 | 0.00 | PARTIAL |
| trend_shift | `ma_trend_shift_532.csv` | 0.93 | 0.00 | 0.00 | 1.00 | 0.97 | 0.00 | 0.84 | 0.84 | 0.94 | 0.03 | PARTIAL |
| trend_shift | `white_noise_trend_shift_769.csv` | 0.57 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.72 | 0.01 | 0.11 | 0.03 | PARTIAL |
| trend_shift | `white_noise_trend_shift_950.csv` | 0.72 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.13 | 0.86 | 0.01 | PARTIAL |
| trend_shift | `white_noise_trend_shift_505.csv` | 0.01 | 0.00 | 1.00 | 0.00 | 0.03 | 0.00 | 0.54 | 0.15 | 0.93 | 0.03 | PARTIAL |
| trend_shift | `white_noise_trend_shift_702.csv` | 0.38 | 0.00 | 1.00 | 0.04 | 0.77 | 0.00 | 0.49 | 0.37 | 0.78 | 0.63 | PARTIAL |
| trend_shift | `white_noise_trend_shift_788.csv` | 0.63 | 0.00 | 0.00 | 1.00 | 0.78 | 0.00 | 0.88 | 0.34 | 0.81 | 0.58 | PARTIAL |
| trend_shift | `white_noise_trend_shift_54.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.73 | 0.00 | 0.95 | 0.89 | 0.96 | 0.01 | PARTIAL |
| trend_shift | `white_noise_trend_shift_296.csv` | 0.94 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.07 | 0.32 | 0.53 | 0.19 | PARTIAL |
| trend_shift | `white_noise_trend_shift_284.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.08 | 0.49 | 0.43 | 0.39 | NONE |
| trend_shift | `white_noise_trend_shift_861.csv` | 0.10 | 0.00 | 1.00 | 0.00 | 0.25 | 0.00 | 0.82 | 0.70 | 0.98 | 0.00 | PARTIAL |
| trend_shift | `white_noise_trend_shift_348.csv` | 0.69 | 0.00 | 0.00 | 0.98 | 0.18 | 0.00 | 0.96 | 0.02 | 0.97 | 0.28 | PARTIAL |
| trend_shift | `white_noise_trend_shift_959.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.88 | 0.00 | 0.62 | 0.27 | 0.93 | 0.01 | PARTIAL |
| trend_shift | `white_noise_trend_shift_616.csv` | 0.98 | 0.00 | 0.00 | 0.99 | 0.62 | 0.00 | 0.87 | 0.48 | 0.48 | 0.09 | NONE |
| trend_shift | `white_noise_trend_shift_74.csv` | 0.50 | 0.00 | 0.92 | 0.00 | 0.62 | 0.00 | 0.96 | 0.13 | 0.82 | 0.01 | PARTIAL |
| trend_shift | `white_noise_trend_shift_349.csv` | 0.97 | 0.00 | 1.00 | 0.00 | 0.01 | 0.00 | 0.91 | 0.39 | 1.00 | 0.00 | PARTIAL |
| trend_shift | `white_noise_trend_shift_199.csv` | 0.73 | 0.00 | 0.97 | 0.00 | 0.09 | 0.00 | 0.35 | 0.80 | 0.97 | 0.05 | PARTIAL |
| trend_shift | `white_noise_trend_shift_781.csv` | 0.89 | 0.00 | 1.00 | 0.00 | 0.02 | 0.00 | 0.84 | 0.49 | 0.95 | 0.00 | PARTIAL |
| trend_shift | `white_noise_trend_shift_639.csv` | 0.94 | 0.00 | 1.00 | 0.00 | 0.08 | 0.00 | 0.12 | 0.18 | 0.94 | 0.02 | PARTIAL |
| trend_shift | `white_noise_trend_shift_319.csv` | 0.89 | 0.00 | 0.00 | 1.00 | 0.95 | 0.00 | 1.00 | 0.04 | 0.70 | 0.01 | PARTIAL |
| trend_shift | `white_noise_trend_shift_715.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.75 | 0.00 | 0.93 | 0.40 | 0.67 | 0.07 | PARTIAL |
| trend_shift | `white_noise_trend_shift_932.csv` | 0.84 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.15 | 0.73 | 0.10 | 0.02 | NONE |
| trend_shift | `white_noise_trend_shift_588.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.11 | 0.00 | 0.84 | 0.67 | 0.91 | 0.05 | PARTIAL |
| trend_shift | `white_noise_trend_shift_687.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.85 | 0.00 | 0.82 | 0.32 | 0.47 | 0.09 | NONE |
| trend_shift | `white_noise_trend_shift_312.csv` | 0.71 | 0.00 | 1.00 | 1.00 | 0.06 | 0.00 | 0.99 | 0.02 | 0.79 | 0.35 | PARTIAL |
| trend_shift | `white_noise_trend_shift_146.csv` | 0.81 | 0.00 | 0.00 | 1.00 | 0.97 | 0.00 | 0.98 | 0.96 | 0.08 | 0.03 | NONE |
| trend_shift | `white_noise_trend_shift_190.csv` | 0.85 | 0.00 | 1.00 | 0.00 | 0.06 | 0.00 | 0.91 | 0.35 | 0.99 | 0.00 | PARTIAL |
| trend_shift | `white_noise_trend_shift_48.csv` | 0.80 | 0.00 | 0.00 | 1.00 | 0.49 | 0.00 | 1.00 | 0.04 | 0.38 | 0.02 | NONE |
| trend_shift | `white_noise_trend_shift_402.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.94 | 0.00 | 0.98 | 0.12 | 0.96 | 0.10 | PARTIAL |
| trend_shift | `white_noise_trend_shift_533.csv` | 0.93 | 0.00 | 0.01 | 1.00 | 0.23 | 0.00 | 0.99 | 0.12 | 0.98 | 0.01 | PARTIAL |
| trend_shift | `white_noise_trend_shift_809.csv` | 0.81 | 0.00 | 1.00 | 0.00 | 0.23 | 0.00 | 0.20 | 0.87 | 0.73 | 0.00 | PARTIAL |
| trend_shift | `white_noise_trend_shift_224.csv` | 0.95 | 0.00 | 0.17 | 1.00 | 0.95 | 0.00 | 0.44 | 0.86 | 0.99 | 0.07 | PARTIAL |
| trend_shift | `white_noise_trend_shift_102.csv` | 0.99 | 0.00 | 1.00 | 0.00 | 0.15 | 0.00 | 0.61 | 0.93 | 0.99 | 0.00 | PARTIAL |
| variance_shift | `ar_variance_shift_988.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.78 | 0.00 | 0.08 | PARTIAL |
| variance_shift | `ar_variance_shift_605.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.39 | PARTIAL |
| variance_shift | `ar_variance_shift_988.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.03 | 0.24 | 0.00 | 0.47 | PARTIAL |
| variance_shift | `ar_variance_shift_361.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.83 | 0.00 | 0.27 | PARTIAL |
| variance_shift | `ar_variance_shift_180.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.52 | 0.00 | 0.02 | 0.57 | 0.00 | 0.39 | PARTIAL |
| variance_shift | `ar_variance_shift_7.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.78 | 0.00 | 0.03 | PARTIAL |
| variance_shift | `ar_variance_shift_591.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.21 | 0.00 | 0.01 | 0.11 | 0.00 | 0.16 | PARTIAL |
| variance_shift | `ar_variance_shift_824.csv` | 0.87 | 0.00 | 0.00 | 0.99 | 0.01 | 0.00 | 0.09 | 0.18 | 0.00 | 0.94 | PARTIAL |
| variance_shift | `ar_variance_shift_27.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.10 | 0.00 | 0.01 | 0.06 | 0.01 | 1.00 | PARTIAL |
| variance_shift | `ar_variance_shift_106.csv` | 0.95 | 0.00 | 0.00 | 1.00 | 0.15 | 0.00 | 0.19 | 0.37 | 0.00 | 0.95 | PARTIAL |
| variance_shift | `ar_variance_shift_373.csv` | 0.99 | 0.00 | 0.00 | 0.99 | 0.01 | 0.00 | 0.01 | 0.04 | 0.00 | 0.99 | PARTIAL |
| variance_shift | `ar_variance_shift_954.csv` | 1.00 | 0.00 | 0.00 | 0.69 | 0.23 | 0.00 | 0.11 | 0.48 | 0.01 | 0.39 | PARTIAL |
| variance_shift | `ar_variance_shift_360.csv` | 0.91 | 0.00 | 0.00 | 1.00 | 0.22 | 0.00 | 0.02 | 0.06 | 0.17 | 1.00 | PARTIAL |
| variance_shift | `ar_variance_shift_517.csv` | 1.00 | 0.00 | 0.13 | 0.00 | 0.09 | 0.00 | 0.99 | 0.11 | 0.47 | 0.25 | PARTIAL |
| variance_shift | `ar_variance_shift_918.csv` | 0.96 | 0.00 | 0.00 | 0.97 | 0.09 | 0.00 | 0.84 | 0.16 | 0.02 | 0.98 | PARTIAL |
| variance_shift | `ar_variance_shift_964.csv` | 0.72 | 0.00 | 0.00 | 1.00 | 0.01 | 0.00 | 0.01 | 0.02 | 0.00 | 0.99 | PARTIAL |
| variance_shift | `ar_variance_shift_221.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.06 | 0.00 | 0.02 | 0.46 | 0.00 | 1.00 | PARTIAL |
| variance_shift | `ar_variance_shift_883.csv` | 1.00 | 0.00 | 1.00 | 0.00 | 0.43 | 0.00 | 0.21 | 0.21 | 0.00 | 0.68 | PARTIAL |
| variance_shift | `ar_variance_shift_201.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 1.00 | PARTIAL |
| variance_shift | `ar_variance_shift_772.csv` | 0.51 | 0.00 | 0.00 | 1.00 | 0.51 | 0.00 | 0.09 | 0.95 | 0.00 | 0.69 | PARTIAL |
| variance_shift | `ar_variance_shift_520.csv` | 0.08 | 0.00 | 0.00 | 1.00 | 0.95 | 0.00 | 0.09 | 0.38 | 0.02 | 0.18 | NONE |
| variance_shift | `ar_variance_shift_696.csv` | 0.77 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.39 | 0.26 | 0.06 | 0.10 | NONE |
| variance_shift | `ar_variance_shift_335.csv` | 0.79 | 0.00 | 0.99 | 0.05 | 0.92 | 0.00 | 0.05 | 0.93 | 0.01 | 0.41 | NONE |
| variance_shift | `ar_variance_shift_760.csv` | 0.03 | 0.00 | 0.00 | 1.00 | 0.86 | 0.00 | 0.03 | 0.56 | 0.00 | 0.87 | PARTIAL |
| variance_shift | `ar_variance_shift_27.csv` | 0.73 | 0.00 | 0.03 | 1.00 | 0.83 | 0.00 | 0.88 | 0.09 | 0.05 | 0.46 | NONE |
| variance_shift | `ar_variance_shift_110.csv` | 0.23 | 0.00 | 1.00 | 0.00 | 0.27 | 0.00 | 0.03 | 0.69 | 0.47 | 0.11 | NONE |
| variance_shift | `ar_variance_shift_778.csv` | 0.95 | 0.00 | 0.00 | 1.00 | 0.78 | 0.00 | 0.08 | 0.79 | 0.03 | 0.71 | PARTIAL |
| variance_shift | `ar_variance_shift_409.csv` | 0.87 | 0.00 | 0.00 | 1.00 | 0.75 | 0.00 | 0.38 | 0.38 | 0.25 | 0.07 | NONE |
| variance_shift | `ar_variance_shift_827.csv` | 0.66 | 0.00 | 0.00 | 1.00 | 0.17 | 0.00 | 0.80 | 0.88 | 0.30 | 0.18 | NONE |
| variance_shift | `ar_variance_shift_370.csv` | 0.78 | 0.00 | 0.00 | 1.00 | 0.72 | 0.00 | 0.10 | 0.49 | 0.02 | 0.76 | PARTIAL |
| variance_shift | `ar_variance_shift_621.csv` | 0.84 | 0.00 | 0.00 | 1.00 | 0.97 | 0.00 | 0.09 | 0.65 | 0.12 | 0.12 | NONE |
| variance_shift | `ar_variance_shift_797.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.62 | 0.00 | 0.02 | 0.22 | 0.05 | 0.98 | PARTIAL |
| variance_shift | `ar_variance_shift_276.csv` | 0.00 | 0.00 | 0.00 | 1.00 | 0.40 | 0.00 | 0.00 | 0.96 | 0.00 | 0.95 | PARTIAL |
| variance_shift | `ar_variance_shift_26.csv` | 1.00 | 0.00 | 0.00 | 0.14 | 0.77 | 0.00 | 0.78 | 0.53 | 0.24 | 0.10 | PARTIAL |
| variance_shift | `ar_variance_shift_661.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.36 | 0.00 | 0.02 | 0.34 | 0.01 | 0.87 | PARTIAL |
| variance_shift | `ar_variance_shift_888.csv` | 0.61 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.04 | 0.22 | 0.03 | 0.43 | NONE |
| variance_shift | `ar_variance_shift_688.csv` | 0.88 | 0.00 | 0.00 | 1.00 | 0.20 | 0.00 | 0.52 | 0.84 | 0.01 | 0.68 | PARTIAL |
| variance_shift | `ar_variance_shift_925.csv` | 0.09 | 0.00 | 0.00 | 1.00 | 0.92 | 0.00 | 0.02 | 0.44 | 0.05 | 0.99 | PARTIAL |
| variance_shift | `ar_variance_shift_472.csv` | 1.00 | 0.00 | 0.00 | 0.99 | 1.00 | 0.00 | 0.16 | 0.63 | 0.02 | 0.18 | PARTIAL |
| variance_shift | `ar_variance_shift_860.csv` | 0.14 | 0.00 | 1.00 | 0.00 | 0.35 | 0.00 | 0.76 | 0.45 | 0.88 | 0.02 | NONE |
| variance_shift | `ar_variance_shift_492.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.55 | 0.00 | 0.05 | 0.59 | 0.00 | 0.14 | NONE |
| variance_shift | `ar_variance_shift_573.csv` | 0.33 | 0.00 | 0.00 | 1.00 | 0.94 | 0.00 | 0.86 | 0.40 | 0.78 | 0.10 | NONE |
| variance_shift | `ar_variance_shift_40.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.87 | 0.00 | 0.10 | 0.58 | 0.23 | 0.10 | NONE |
| variance_shift | `ar_variance_shift_178.csv` | 0.16 | 0.00 | 0.00 | 1.00 | 0.87 | 0.00 | 0.95 | 0.33 | 0.02 | 0.09 | NONE |
| variance_shift | `ar_variance_shift_468.csv` | 0.17 | 0.00 | 0.00 | 1.00 | 0.04 | 0.00 | 0.05 | 0.08 | 0.02 | 0.99 | PARTIAL |
| variance_shift | `ar_variance_shift_715.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.70 | 0.00 | 0.97 | 0.25 | 0.39 | 0.01 | PARTIAL |
| variance_shift | `ar_variance_shift_227.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.41 | 0.00 | 0.04 | 0.80 | 0.01 | 0.79 | PARTIAL |
| variance_shift | `ar_variance_shift_538.csv` | 0.22 | 0.00 | 0.00 | 1.00 | 0.05 | 0.00 | 0.01 | 0.03 | 0.01 | 1.00 | PARTIAL |
| variance_shift | `ar_variance_shift_397.csv` | 0.93 | 0.00 | 0.00 | 1.00 | 0.06 | 0.00 | 0.00 | 0.04 | 0.00 | 1.00 | PARTIAL |
| variance_shift | `ar_variance_shift_961.csv` | 0.01 | 0.00 | 0.00 | 1.00 | 0.19 | 0.00 | 0.05 | 0.91 | 0.01 | 1.00 | PARTIAL |
| variance_shift | `ar_variance_shift_327.csv` | 0.94 | 0.00 | 0.00 | 1.00 | 0.92 | 0.00 | 0.05 | 0.97 | 0.00 | 0.54 | PARTIAL |
| variance_shift | `ar_variance_shift_103.csv` | 0.83 | 0.00 | 0.00 | 1.00 | 1.00 | 0.00 | 0.43 | 0.45 | 0.01 | 0.38 | NONE |
| variance_shift | `ar_variance_shift_339.csv` | 0.82 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.97 | 0.66 | 0.34 | 0.25 | NONE |
| variance_shift | `ar_variance_shift_451.csv` | 0.38 | 0.00 | 0.00 | 1.00 | 0.92 | 0.00 | 0.71 | 0.68 | 0.00 | 0.51 | PARTIAL |
| variance_shift | `ar_variance_shift_315.csv` | 0.89 | 0.00 | 0.00 | 0.99 | 0.72 | 0.00 | 0.05 | 0.56 | 0.84 | 0.82 | PARTIAL |
| variance_shift | `ar_variance_shift_51.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.08 | 0.00 | 0.01 | 0.24 | 0.03 | 0.99 | PARTIAL |
| variance_shift | `arma_variance_shift_344.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.27 | PARTIAL |
| variance_shift | `arma_variance_shift_220.csv` | 0.94 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 1.00 | PARTIAL |
| variance_shift | `arma_variance_shift_539.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.57 | 0.00 | 0.04 | 0.07 | 0.00 | 0.99 | PARTIAL |
| variance_shift | `arma_variance_shift_745.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.16 | 0.00 | 0.00 | 0.06 | 0.00 | 0.90 | PARTIAL |
| variance_shift | `arma_variance_shift_725.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.01 | 0.00 | 0.00 | 0.04 | 0.01 | 1.00 | PARTIAL |
| variance_shift | `arma_variance_shift_824.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.11 | 0.00 | 0.09 | 0.56 | 0.00 | 0.81 | PARTIAL |
| variance_shift | `arma_variance_shift_173.csv` | 0.96 | 0.00 | 0.00 | 1.00 | 0.57 | 0.00 | 0.02 | 0.02 | 0.02 | 0.99 | PARTIAL |
| variance_shift | `arma_variance_shift_585.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.03 | 0.00 | 0.00 | 0.06 | 0.00 | 1.00 | PARTIAL |
| variance_shift | `arma_variance_shift_862.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.03 | 0.00 | 0.01 | 0.14 | 0.00 | 0.98 | PARTIAL |
| variance_shift | `arma_variance_shift_930.csv` | 0.94 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 1.00 | PARTIAL |
| variance_shift | `arma_variance_shift_285.csv` | 0.23 | 0.00 | 0.00 | 1.00 | 0.84 | 0.00 | 0.04 | 0.76 | 0.00 | 0.14 | NONE |
| variance_shift | `arma_variance_shift_626.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.30 | 0.00 | 0.03 | 0.33 | 0.00 | 0.88 | PARTIAL |
| variance_shift | `arma_variance_shift_593.csv` | 0.96 | 0.00 | 0.00 | 1.00 | 0.96 | 0.00 | 0.01 | 0.51 | 0.02 | 0.96 | PARTIAL |
| variance_shift | `arma_variance_shift_236.csv` | 0.77 | 0.00 | 0.00 | 1.00 | 0.60 | 0.00 | 0.06 | 0.87 | 0.01 | 0.90 | PARTIAL |
| variance_shift | `arma_variance_shift_25.csv` | 0.95 | 0.00 | 0.51 | 1.00 | 0.26 | 0.00 | 0.99 | 0.53 | 0.01 | 0.03 | NONE |
| variance_shift | `arma_variance_shift_886.csv` | 0.02 | 0.00 | 0.00 | 1.00 | 0.83 | 0.00 | 0.15 | 0.56 | 0.00 | 0.62 | PARTIAL |
| variance_shift | `arma_variance_shift_578.csv` | 0.01 | 0.00 | 1.00 | 0.00 | 0.99 | 0.00 | 0.83 | 0.18 | 0.00 | 0.01 | NONE |
| variance_shift | `arma_variance_shift_505.csv` | 0.20 | 0.00 | 0.00 | 1.00 | 0.56 | 0.00 | 0.67 | 0.92 | 0.01 | 0.19 | NONE |
| variance_shift | `arma_variance_shift_205.csv` | 0.01 | 0.00 | 1.00 | 0.00 | 0.49 | 0.00 | 0.80 | 0.13 | 0.00 | 0.01 | NONE |
| variance_shift | `arma_variance_shift_725.csv` | 0.95 | 0.00 | 0.00 | 1.00 | 0.27 | 0.00 | 0.05 | 0.51 | 0.00 | 0.50 | PARTIAL |
| variance_shift | `arma_variance_shift_288.csv` | 1.00 | 0.00 | 0.00 | 0.95 | 0.85 | 0.00 | 0.34 | 0.06 | 0.29 | 0.43 | PARTIAL |
| variance_shift | `arma_variance_shift_76.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.81 | 0.00 | 0.05 | 0.36 | 0.03 | 0.93 | PARTIAL |
| variance_shift | `arma_variance_shift_636.csv` | 0.98 | 0.00 | 1.00 | 0.02 | 0.91 | 0.00 | 0.27 | 0.16 | 0.01 | 0.02 | NONE |
| variance_shift | `arma_variance_shift_549.csv` | 0.84 | 0.00 | 0.00 | 1.00 | 0.52 | 0.00 | 0.02 | 0.20 | 0.01 | 1.00 | PARTIAL |
| variance_shift | `arma_variance_shift_182.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.26 | 0.00 | 0.10 | 0.26 | 0.04 | 0.84 | PARTIAL |
| variance_shift | `arma_variance_shift_927.csv` | 0.29 | 0.00 | 0.00 | 1.00 | 0.46 | 0.00 | 0.38 | 0.11 | 0.01 | 0.97 | PARTIAL |
| variance_shift | `arma_variance_shift_569.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.11 | 0.20 | 0.05 | 0.17 | PARTIAL |
| variance_shift | `arma_variance_shift_509.csv` | 0.01 | 0.00 | 1.00 | 0.00 | 0.88 | 0.00 | 0.72 | 0.94 | 0.02 | 0.00 | NONE |
| variance_shift | `arma_variance_shift_844.csv` | 0.06 | 0.00 | 0.00 | 1.00 | 0.87 | 0.00 | 0.15 | 0.78 | 0.00 | 0.41 | NONE |
| variance_shift | `arma_variance_shift_149.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.11 | 0.00 | 0.01 | 0.37 | 0.01 | 0.99 | PARTIAL |
| variance_shift | `arma_variance_shift_22.csv` | 0.12 | 0.00 | 0.00 | 1.00 | 0.03 | 0.00 | 0.97 | 0.24 | 0.01 | 0.83 | PARTIAL |
| variance_shift | `arma_variance_shift_571.csv` | 0.11 | 0.00 | 0.00 | 1.00 | 0.81 | 0.00 | 0.04 | 0.17 | 0.01 | 0.97 | PARTIAL |
| variance_shift | `arma_variance_shift_481.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.96 | 0.00 | 0.64 | 0.89 | 0.23 | 0.12 | NONE |
| variance_shift | `arma_variance_shift_519.csv` | 0.84 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.62 | 0.12 | 0.67 | 0.03 | NONE |
| variance_shift | `arma_variance_shift_618.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.66 | 0.00 | 0.05 | 0.78 | 0.11 | 0.38 | NONE |
| variance_shift | `arma_variance_shift_151.csv` | 0.47 | 0.00 | 0.00 | 1.00 | 0.97 | 0.00 | 0.30 | 0.29 | 0.04 | 0.07 | NONE |
| variance_shift | `arma_variance_shift_613.csv` | 0.34 | 0.00 | 0.40 | 1.00 | 1.00 | 0.00 | 0.05 | 0.74 | 0.01 | 0.18 | NONE |
| variance_shift | `arma_variance_shift_524.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.31 | 0.00 | 0.03 | 0.27 | 0.00 | 1.00 | PARTIAL |
| variance_shift | `arma_variance_shift_718.csv` | 0.02 | 0.00 | 1.00 | 0.02 | 0.88 | 0.00 | 0.38 | 0.59 | 0.01 | 0.44 | NONE |
| variance_shift | `arma_variance_shift_382.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.55 | 0.00 | 0.07 | 0.38 | 0.07 | 0.99 | PARTIAL |
| variance_shift | `arma_variance_shift_118.csv` | 0.30 | 0.00 | 0.00 | 1.00 | 0.86 | 0.00 | 0.02 | 0.21 | 0.02 | 0.96 | PARTIAL |
| variance_shift | `arma_variance_shift_332.csv` | 0.91 | 0.00 | 0.00 | 1.00 | 0.19 | 0.00 | 0.02 | 0.91 | 0.00 | 0.94 | PARTIAL |
| variance_shift | `arma_variance_shift_851.csv` | 0.62 | 0.00 | 0.00 | 1.00 | 0.15 | 0.00 | 0.04 | 0.05 | 0.00 | 0.99 | PARTIAL |
| variance_shift | `arma_variance_shift_1000.csv` | 0.14 | 0.00 | 0.00 | 1.00 | 0.16 | 0.00 | 0.03 | 0.23 | 0.01 | 1.00 | PARTIAL |
| variance_shift | `arma_variance_shift_786.csv` | 0.91 | 0.00 | 0.00 | 1.00 | 0.95 | 0.00 | 0.10 | 0.24 | 0.08 | 0.97 | PARTIAL |
| variance_shift | `ma_variance_shift_415.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.13 | 0.00 | 0.04 | PARTIAL |
| variance_shift | `ma_variance_shift_960.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.57 | 0.00 | 0.29 | PARTIAL |
| variance_shift | `ma_variance_shift_807.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.49 | 0.00 | 0.39 | PARTIAL |
| variance_shift | `ma_variance_shift_92.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.96 | 0.00 | 0.06 | PARTIAL |
| variance_shift | `ma_variance_shift_596.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.01 | 0.00 | 0.00 | 0.02 | 0.02 | 1.00 | PARTIAL |
| variance_shift | `ma_variance_shift_419.csv` | 0.90 | 0.00 | 0.00 | 1.00 | 0.03 | 0.00 | 0.00 | 0.01 | 0.01 | 1.00 | PARTIAL |
| variance_shift | `ma_variance_shift_594.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.03 | 0.00 | 0.05 | 0.55 | 0.00 | 0.97 | PARTIAL |
| variance_shift | `ma_variance_shift_460.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.02 | 0.00 | 0.01 | 0.05 | 0.00 | 0.92 | PARTIAL |
| variance_shift | `ma_variance_shift_303.csv` | 1.00 | 0.00 | 0.00 | 0.01 | 0.04 | 0.00 | 0.07 | 0.43 | 0.02 | 0.05 | PARTIAL |
| variance_shift | `ma_variance_shift_525.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.01 | 0.22 | 0.00 | 0.99 | PARTIAL |
| variance_shift | `ma_variance_shift_448.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.01 | 0.00 | 0.00 | 0.07 | 0.01 | 1.00 | PARTIAL |
| variance_shift | `ma_variance_shift_31.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.10 | 0.00 | 0.00 | 0.03 | 0.09 | 1.00 | PARTIAL |
| variance_shift | `ma_variance_shift_326.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.03 | 0.00 | 0.02 | 0.12 | 0.00 | 0.87 | PARTIAL |
| variance_shift | `ma_variance_shift_417.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.01 | 0.00 | 0.03 | 0.10 | 0.00 | 0.98 | PARTIAL |
| variance_shift | `ma_variance_shift_352.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 1.00 | PARTIAL |
| variance_shift | `ma_variance_shift_962.csv` | 0.66 | 0.00 | 0.00 | 0.99 | 0.00 | 0.00 | 0.00 | 0.36 | 0.00 | 1.00 | PARTIAL |
| variance_shift | `ma_variance_shift_767.csv` | 0.98 | 0.00 | 0.00 | 0.99 | 0.01 | 0.00 | 0.07 | 0.27 | 0.00 | 0.97 | PARTIAL |
| variance_shift | `ma_variance_shift_803.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.04 | 0.00 | 0.00 | 0.05 | 0.00 | 1.00 | PARTIAL |
| variance_shift | `ma_variance_shift_844.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.97 | 0.00 | 0.16 | 0.33 | 0.25 | 0.08 | PARTIAL |
| variance_shift | `ma_variance_shift_707.csv` | 0.20 | 0.00 | 0.92 | 1.00 | 0.70 | 0.00 | 0.05 | 0.55 | 0.00 | 0.36 | NONE |
| variance_shift | `ma_variance_shift_485.csv` | 0.34 | 0.00 | 1.00 | 0.04 | 0.08 | 0.00 | 0.69 | 0.85 | 0.01 | 0.18 | NONE |
| variance_shift | `ma_variance_shift_665.csv` | 0.17 | 0.00 | 0.00 | 1.00 | 0.06 | 0.00 | 0.01 | 0.17 | 0.00 | 1.00 | PARTIAL |
| variance_shift | `ma_variance_shift_804.csv` | 0.59 | 0.00 | 0.00 | 1.00 | 0.21 | 0.00 | 0.01 | 0.04 | 0.01 | 1.00 | PARTIAL |
| variance_shift | `ma_variance_shift_961.csv` | 0.02 | 0.00 | 0.00 | 1.00 | 0.79 | 0.00 | 0.08 | 0.89 | 0.00 | 0.76 | PARTIAL |
| variance_shift | `ma_variance_shift_912.csv` | 0.07 | 0.00 | 0.00 | 1.00 | 0.87 | 0.00 | 0.03 | 0.93 | 0.00 | 0.17 | NONE |
| variance_shift | `ma_variance_shift_918.csv` | 0.01 | 0.00 | 0.00 | 1.00 | 0.29 | 0.00 | 0.01 | 0.13 | 0.00 | 1.00 | PARTIAL |
| variance_shift | `ma_variance_shift_112.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.97 | 0.00 | 0.05 | 0.19 | 0.02 | 0.55 | PARTIAL |
| variance_shift | `ma_variance_shift_32.csv` | 0.28 | 0.00 | 1.00 | 0.67 | 0.52 | 0.00 | 0.01 | 0.30 | 0.01 | 0.92 | PARTIAL |
| variance_shift | `ma_variance_shift_289.csv` | 0.66 | 0.00 | 0.00 | 1.00 | 0.46 | 0.00 | 0.10 | 0.38 | 0.43 | 0.67 | PARTIAL |
| variance_shift | `ma_variance_shift_16.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.83 | 0.00 | 0.97 | 0.34 | 0.07 | 0.32 | NONE |
| variance_shift | `ma_variance_shift_191.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.86 | 0.00 | 0.11 | 0.79 | 0.13 | 0.01 | NONE |
| variance_shift | `ma_variance_shift_646.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.38 | 0.00 | 0.23 | 0.81 | 0.01 | 0.64 | PARTIAL |
| variance_shift | `ma_variance_shift_129.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.90 | 0.00 | 0.04 | 0.17 | 0.36 | 0.04 | PARTIAL |
| variance_shift | `ma_variance_shift_51.csv` | 0.68 | 0.00 | 0.00 | 1.00 | 0.11 | 0.00 | 0.01 | 0.21 | 0.03 | 0.99 | PARTIAL |
| variance_shift | `ma_variance_shift_65.csv` | 0.99 | 0.00 | 0.00 | 0.98 | 1.00 | 0.00 | 0.12 | 0.52 | 0.41 | 0.13 | PARTIAL |
| variance_shift | `ma_variance_shift_718.csv` | 0.67 | 0.00 | 0.00 | 1.00 | 0.84 | 0.00 | 0.29 | 0.20 | 0.01 | 0.07 | NONE |
| variance_shift | `ma_variance_shift_747.csv` | 0.06 | 0.00 | 0.00 | 1.00 | 0.20 | 0.00 | 0.07 | 0.55 | 0.00 | 0.83 | PARTIAL |
| variance_shift | `ma_variance_shift_902.csv` | 0.78 | 0.00 | 0.00 | 1.00 | 0.92 | 0.00 | 0.07 | 0.82 | 0.33 | 0.38 | NONE |
| variance_shift | `ma_variance_shift_142.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.96 | 0.00 | 0.03 | 0.79 | 0.24 | 0.84 | PARTIAL |
| variance_shift | `ma_variance_shift_323.csv` | 0.00 | 0.00 | 0.00 | 1.00 | 0.16 | 0.00 | 0.00 | 0.71 | 0.01 | 0.99 | PARTIAL |
| variance_shift | `ma_variance_shift_781.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.61 | 0.00 | 0.14 | 0.44 | 0.28 | 0.80 | PARTIAL |
| variance_shift | `ma_variance_shift_139.csv` | 0.88 | 0.00 | 0.00 | 1.00 | 0.96 | 0.00 | 0.05 | 0.49 | 0.04 | 0.99 | PARTIAL |
| variance_shift | `ma_variance_shift_469.csv` | 0.06 | 0.00 | 0.00 | 1.00 | 1.00 | 0.00 | 0.04 | 0.90 | 0.00 | 0.61 | PARTIAL |
| variance_shift | `ma_variance_shift_502.csv` | 0.28 | 0.00 | 0.00 | 1.00 | 0.41 | 0.00 | 0.00 | 0.50 | 0.02 | 1.00 | PARTIAL |
| variance_shift | `ma_variance_shift_313.csv` | 0.01 | 0.00 | 0.00 | 1.00 | 0.37 | 0.00 | 0.01 | 0.19 | 0.02 | 1.00 | PARTIAL |
| variance_shift | `ma_variance_shift_596.csv` | 0.82 | 0.00 | 0.00 | 1.00 | 0.60 | 0.00 | 0.02 | 0.70 | 0.03 | 0.99 | PARTIAL |
| variance_shift | `ma_variance_shift_299.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.75 | 0.00 | 0.01 | 0.09 | 0.10 | 0.99 | PARTIAL |
| variance_shift | `ma_variance_shift_794.csv` | 0.94 | 0.00 | 0.00 | 1.00 | 0.91 | 0.00 | 0.18 | 0.75 | 0.24 | 0.00 | NONE |
| variance_shift | `ma_variance_shift_895.csv` | 0.08 | 0.00 | 0.00 | 1.00 | 0.95 | 0.00 | 0.02 | 0.96 | 0.00 | 0.99 | PARTIAL |
| variance_shift | `ma_variance_shift_813.csv` | 0.88 | 0.00 | 0.02 | 1.00 | 0.79 | 0.00 | 0.08 | 0.22 | 0.01 | 0.85 | PARTIAL |
| variance_shift | `ma_variance_shift_15.csv` | 0.10 | 0.00 | 0.00 | 1.00 | 0.96 | 0.00 | 0.04 | 0.81 | 0.02 | 0.87 | PARTIAL |
| variance_shift | `ma_variance_shift_227.csv` | 0.08 | 0.00 | 0.00 | 1.00 | 0.64 | 0.00 | 0.01 | 0.69 | 0.01 | 0.99 | PARTIAL |
| variance_shift | `ma_variance_shift_562.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.56 | 0.00 | 0.04 | 0.80 | 0.01 | 0.33 | NONE |
| variance_shift | `ma_variance_shift_365.csv` | 0.16 | 0.00 | 0.00 | 1.00 | 1.00 | 0.00 | 0.05 | 0.98 | 0.03 | 0.76 | PARTIAL |
| variance_shift | `ma_variance_shift_313.csv` | 0.95 | 0.00 | 0.00 | 1.00 | 0.96 | 0.00 | 0.04 | 0.86 | 0.03 | 0.98 | PARTIAL |
| variance_shift | `ma_variance_shift_850.csv` | 0.81 | 0.00 | 0.00 | 1.00 | 0.93 | 0.00 | 0.03 | 0.96 | 0.01 | 0.47 | NONE |
| variance_shift | `ma_variance_shift_943.csv` | 0.21 | 0.00 | 0.00 | 1.00 | 0.86 | 0.00 | 0.19 | 0.60 | 0.01 | 0.63 | PARTIAL |
| variance_shift | `ma_variance_shift_773.csv` | 0.11 | 0.00 | 0.00 | 1.00 | 0.58 | 0.00 | 0.01 | 0.06 | 0.03 | 0.99 | PARTIAL |
| variance_shift | `white_noise_variance_shift_630.csv` | 0.98 | 0.00 | 0.00 | 0.99 | 0.00 | 0.00 | 0.01 | 0.06 | 0.00 | 0.68 | PARTIAL |
| variance_shift | `white_noise_variance_shift_48.csv` | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.61 | 0.00 | 0.43 | PARTIAL |
| variance_shift | `white_noise_variance_shift_909.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.10 | 0.00 | 0.99 | PARTIAL |
| variance_shift | `white_noise_variance_shift_776.csv` | 1.00 | 0.00 | 0.00 | 0.90 | 0.00 | 0.00 | 0.00 | 0.67 | 0.00 | 0.21 | PARTIAL |
| variance_shift | `white_noise_variance_shift_610.csv` | 1.00 | 0.00 | 0.00 | 0.25 | 0.01 | 0.00 | 0.00 | 0.61 | 0.00 | 0.09 | PARTIAL |
| variance_shift | `white_noise_variance_shift_995.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.93 | PARTIAL |
| variance_shift | `white_noise_variance_shift_392.csv` | 0.90 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.01 | 1.00 | PARTIAL |
| variance_shift | `white_noise_variance_shift_740.csv` | 0.95 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.02 | 0.03 | 0.00 | 0.97 | PARTIAL |
| variance_shift | `white_noise_variance_shift_475.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 1.00 | PARTIAL |
| variance_shift | `white_noise_variance_shift_235.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.18 | 0.00 | 0.10 | 0.06 | 0.00 | 0.79 | PARTIAL |
| variance_shift | `white_noise_variance_shift_375.csv` | 0.87 | 0.00 | 0.00 | 1.00 | 0.01 | 0.00 | 0.01 | 0.06 | 0.00 | 0.80 | PARTIAL |
| variance_shift | `white_noise_variance_shift_445.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.01 | 0.00 | 0.01 | 0.11 | 0.00 | 0.92 | PARTIAL |
| variance_shift | `white_noise_variance_shift_268.csv` | 0.58 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.01 | 0.02 | 0.00 | 0.32 | NONE |
| variance_shift | `white_noise_variance_shift_794.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.14 | 0.00 | 0.02 | 0.22 | 0.00 | 0.59 | PARTIAL |
| variance_shift | `white_noise_variance_shift_305.csv` | 0.98 | 0.00 | 0.00 | 0.99 | 0.01 | 0.00 | 0.46 | 0.02 | 0.00 | 0.97 | PARTIAL |
| variance_shift | `white_noise_variance_shift_375.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.01 | 0.28 | 0.00 | 0.99 | PARTIAL |
| variance_shift | `white_noise_variance_shift_750.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 1.00 | PARTIAL |
| variance_shift | `white_noise_variance_shift_230.csv` | 0.96 | 0.00 | 0.00 | 1.00 | 0.07 | 0.00 | 0.01 | 0.02 | 0.01 | 1.00 | PARTIAL |
| variance_shift | `white_noise_variance_shift_525.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.04 | 0.00 | 0.34 | 0.35 | 0.00 | 0.95 | PARTIAL |
| variance_shift | `white_noise_variance_shift_941.csv` | 0.94 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.14 | 0.00 | 0.99 | PARTIAL |
| variance_shift | `white_noise_variance_shift_151.csv` | 0.70 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 1.00 | PARTIAL |
| variance_shift | `white_noise_variance_shift_616.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.01 | 0.00 | 0.04 | 0.13 | 0.00 | 0.99 | PARTIAL |
| variance_shift | `white_noise_variance_shift_479.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.01 | 0.11 | 0.00 | 0.99 | PARTIAL |
| variance_shift | `white_noise_variance_shift_991.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.01 | 0.00 | 0.03 | 0.79 | 0.01 | 0.99 | PARTIAL |
| variance_shift | `white_noise_variance_shift_482.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.12 | 0.00 | 0.11 | 0.54 | 0.00 | 0.73 | PARTIAL |
| variance_shift | `white_noise_variance_shift_611.csv` | 0.94 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.01 | 1.00 | PARTIAL |
| variance_shift | `white_noise_variance_shift_587.csv` | 0.97 | 0.00 | 0.00 | 0.99 | 0.04 | 0.00 | 0.28 | 0.19 | 0.01 | 0.99 | PARTIAL |
| variance_shift | `white_noise_variance_shift_221.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 1.00 | PARTIAL |
| variance_shift | `white_noise_variance_shift_456.csv` | 0.90 | 0.00 | 0.00 | 1.00 | 0.03 | 0.00 | 0.16 | 0.56 | 0.00 | 0.99 | PARTIAL |
| variance_shift | `white_noise_variance_shift_321.csv` | 0.96 | 0.00 | 0.00 | 1.00 | 0.01 | 0.00 | 0.01 | 0.42 | 0.00 | 1.00 | PARTIAL |
| variance_shift | `white_noise_variance_shift_333.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.01 | 0.00 | 0.11 | 0.11 | 0.00 | 0.99 | PARTIAL |
| variance_shift | `white_noise_variance_shift_286.csv` | 0.84 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 1.00 | PARTIAL |
| variance_shift | `white_noise_variance_shift_695.csv` | 0.96 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.01 | 0.03 | 0.00 | 1.00 | PARTIAL |
| variance_shift | `white_noise_variance_shift_170.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.02 | 0.00 | 0.01 | 0.05 | 0.00 | 0.98 | PARTIAL |
| variance_shift | `white_noise_variance_shift_949.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.02 | 0.00 | 0.01 | 0.04 | 0.01 | 0.99 | PARTIAL |
| variance_shift | `white_noise_variance_shift_512.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.01 | 0.00 | 0.52 | 0.05 | 0.00 | 0.98 | PARTIAL |
| variance_shift | `white_noise_variance_shift_88.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.15 | 0.00 | 0.10 | 0.15 | 0.00 | 0.98 | PARTIAL |
| variance_shift | `white_noise_variance_shift_44.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.02 | 0.00 | 0.21 | 0.01 | 0.00 | 0.97 | PARTIAL |
| variance_shift | `white_noise_variance_shift_183.csv` | 0.22 | 0.00 | 0.00 | 1.00 | 0.46 | 0.00 | 0.04 | 0.40 | 0.00 | 0.92 | PARTIAL |
| variance_shift | `white_noise_variance_shift_592.csv` | 0.36 | 0.00 | 0.00 | 1.00 | 0.77 | 0.00 | 0.58 | 0.94 | 0.02 | 0.08 | NONE |
| variance_shift | `white_noise_variance_shift_766.csv` | 0.00 | 0.00 | 0.00 | 1.00 | 0.21 | 0.00 | 0.98 | 0.50 | 0.01 | 0.09 | NONE |
| variance_shift | `white_noise_variance_shift_863.csv` | 0.48 | 0.00 | 0.00 | 1.00 | 0.21 | 0.00 | 0.01 | 0.14 | 0.00 | 0.99 | PARTIAL |
| variance_shift | `white_noise_variance_shift_274.csv` | 0.78 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.92 | 0.19 | 0.06 | 0.07 | NONE |
| variance_shift | `white_noise_variance_shift_145.csv` | 0.00 | 0.00 | 0.00 | 1.00 | 0.78 | 0.00 | 0.01 | 0.40 | 0.03 | 1.00 | PARTIAL |
| variance_shift | `white_noise_variance_shift_345.csv` | 0.02 | 0.00 | 0.00 | 1.00 | 0.56 | 0.00 | 0.01 | 0.41 | 0.00 | 0.99 | PARTIAL |
| variance_shift | `white_noise_variance_shift_446.csv` | 0.00 | 0.00 | 0.00 | 1.00 | 0.15 | 0.00 | 0.01 | 0.02 | 0.01 | 1.00 | PARTIAL |
| variance_shift | `white_noise_variance_shift_719.csv` | 0.09 | 0.00 | 0.00 | 1.00 | 0.66 | 0.00 | 0.19 | 0.68 | 0.01 | 0.63 | PARTIAL |
| variance_shift | `white_noise_variance_shift_656.csv` | 0.03 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.07 | 0.92 | 0.01 | 0.12 | NONE |
| variance_shift | `white_noise_variance_shift_654.csv` | 0.74 | 0.00 | 0.00 | 1.00 | 0.69 | 0.00 | 0.02 | 0.21 | 0.01 | 0.98 | PARTIAL |
| variance_shift | `white_noise_variance_shift_134.csv` | 0.86 | 0.00 | 0.00 | 1.00 | 0.91 | 0.00 | 0.95 | 0.11 | 0.34 | 0.56 | PARTIAL |
| variance_shift | `white_noise_variance_shift_903.csv` | 0.96 | 0.00 | 0.00 | 1.00 | 0.82 | 0.00 | 0.01 | 0.68 | 0.02 | 0.90 | PARTIAL |
| variance_shift | `white_noise_variance_shift_165.csv` | 0.64 | 0.00 | 0.00 | 1.00 | 0.23 | 0.00 | 0.58 | 0.43 | 0.00 | 0.92 | PARTIAL |
| variance_shift | `white_noise_variance_shift_271.csv` | 0.99 | 0.00 | 0.00 | 1.00 | 0.28 | 0.00 | 0.95 | 0.66 | 0.02 | 0.12 | NONE |
| variance_shift | `white_noise_variance_shift_84.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.99 | 0.00 | 0.03 | 0.63 | 0.09 | 0.73 | PARTIAL |
| variance_shift | `white_noise_variance_shift_80.csv` | 0.34 | 0.00 | 0.00 | 1.00 | 0.72 | 0.00 | 0.11 | 0.70 | 0.02 | 0.59 | PARTIAL |
| variance_shift | `white_noise_variance_shift_64.csv` | 0.02 | 0.00 | 0.00 | 1.00 | 0.88 | 0.00 | 0.96 | 0.44 | 0.00 | 0.05 | NONE |
| variance_shift | `white_noise_variance_shift_766.csv` | 0.90 | 0.00 | 0.00 | 0.98 | 1.00 | 0.00 | 0.14 | 0.16 | 0.09 | 0.50 | PARTIAL |
| variance_shift | `white_noise_variance_shift_717.csv` | 0.97 | 0.00 | 0.00 | 1.00 | 0.51 | 0.00 | 0.03 | 0.59 | 0.02 | 0.85 | PARTIAL |
| variance_shift | `white_noise_variance_shift_613.csv` | 0.00 | 0.00 | 0.00 | 1.00 | 0.69 | 0.00 | 0.98 | 0.41 | 0.21 | 0.03 | NONE |
| variance_shift | `white_noise_variance_shift_299.csv` | 0.12 | 0.00 | 0.00 | 1.00 | 0.84 | 0.00 | 0.14 | 0.79 | 0.00 | 0.63 | PARTIAL |
| variance_shift | `white_noise_variance_shift_54.csv` | 0.71 | 0.00 | 0.00 | 1.00 | 0.43 | 0.00 | 0.03 | 0.52 | 0.05 | 0.98 | PARTIAL |
| variance_shift | `white_noise_variance_shift_290.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 0.28 | 0.00 | 0.03 | 0.38 | 0.01 | 0.98 | PARTIAL |
| variance_shift | `white_noise_variance_shift_90.csv` | 0.08 | 0.00 | 0.00 | 1.00 | 0.57 | 0.00 | 0.02 | 0.43 | 0.00 | 0.99 | PARTIAL |
| variance_shift | `white_noise_variance_shift_934.csv` | 0.58 | 0.00 | 0.00 | 1.00 | 0.80 | 0.00 | 0.20 | 0.56 | 0.03 | 0.09 | NONE |
| variance_shift | `white_noise_variance_shift_404.csv` | 0.26 | 0.00 | 0.00 | 1.00 | 0.45 | 0.00 | 0.08 | 0.23 | 0.02 | 0.99 | PARTIAL |
| variance_shift | `white_noise_variance_shift_378.csv` | 0.03 | 0.00 | 0.00 | 1.00 | 0.05 | 0.00 | 0.01 | 0.10 | 0.00 | 1.00 | PARTIAL |
| variance_shift | `white_noise_variance_shift_980.csv` | 0.27 | 0.00 | 0.00 | 1.00 | 0.86 | 0.00 | 0.02 | 0.54 | 0.10 | 0.99 | PARTIAL |
| variance_shift | `white_noise_variance_shift_936.csv` | 1.00 | 0.00 | 0.00 | 1.00 | 0.30 | 0.00 | 0.20 | 0.55 | 0.00 | 0.34 | NONE |
| variance_shift | `white_noise_variance_shift_111.csv` | 0.00 | 0.00 | 0.00 | 1.00 | 0.47 | 0.00 | 0.02 | 0.20 | 0.01 | 0.99 | PARTIAL |
| variance_shift | `white_noise_variance_shift_293.csv` | 0.58 | 0.00 | 0.00 | 1.00 | 0.07 | 0.00 | 0.05 | 0.22 | 0.01 | 0.93 | PARTIAL |
| variance_shift | `white_noise_variance_shift_962.csv` | 0.92 | 0.00 | 0.00 | 1.00 | 0.17 | 0.00 | 0.85 | 0.96 | 0.00 | 0.20 | NONE |
| variance_shift | `white_noise_variance_shift_273.csv` | 0.85 | 0.00 | 0.00 | 1.00 | 0.79 | 0.00 | 0.01 | 0.45 | 0.05 | 0.39 | NONE |
| variance_shift | `white_noise_variance_shift_986.csv` | 0.96 | 0.00 | 0.00 | 1.00 | 0.95 | 0.00 | 0.06 | 0.70 | 0.00 | 0.29 | NONE |
| variance_shift | `white_noise_variance_shift_782.csv` | 0.98 | 0.00 | 0.00 | 1.00 | 1.00 | 0.00 | 0.58 | 0.52 | 0.84 | 0.01 | NONE |
| variance_shift | `white_noise_variance_shift_206.csv` | 0.92 | 0.00 | 0.00 | 1.00 | 0.63 | 0.00 | 0.02 | 0.23 | 0.18 | 0.95 | PARTIAL |
| variance_shift | `white_noise_variance_shift_787.csv` | 0.66 | 0.00 | 0.00 | 1.00 | 0.07 | 0.00 | 0.07 | 0.40 | 0.01 | 0.98 | PARTIAL |
| variance_shift | `white_noise_variance_shift_794.csv` | 0.85 | 0.00 | 0.00 | 1.00 | 0.87 | 0.00 | 0.05 | 0.86 | 0.02 | 0.99 | PARTIAL |
| variance_shift | `white_noise_variance_shift_54.csv` | 0.44 | 0.00 | 0.00 | 1.00 | 0.98 | 0.00 | 0.01 | 0.21 | 0.01 | 1.00 | PARTIAL |
| quad+variance_shift | `quadratic_varshift_ar_029.csv` | 0.00 | 1.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.97 | 0.00 | 0.00 | 0.34 | PARTIAL |
| stoch+mean_shift | `rwd_single_mean_shift_increase_middle_325.csv` | 0.16 | 0.00 | 1.00 | 0.00 | 0.99 | 0.00 | 0.37 | 0.32 | 0.01 | 0.00 | PARTIAL |
| stoch+mean_shift | `rwd_single_mean_shift_increase_middle_166.csv` | 0.00 | 0.00 | 1.00 | 0.00 | 0.90 | 0.00 | 0.06 | 0.57 | 0.01 | 0.01 | PARTIAL |
| stoch+variance_shift | `ima_single_variance_shift_increase_middle_482.csv` | 0.99 | 0.00 | 0.00 | 0.00 | 0.12 | 0.00 | 0.33 | 0.00 | 0.00 | 0.91 | PARTIAL |
| stoch+variance_shift | `rwd_single_variance_shift_increase_beginning_133.csv` | 0.01 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.25 | PARTIAL |
| vol+collective | `garch_single_collective_anomaly_middle_374.csv` | 0.03 | 0.00 | 0.00 | 1.00 | 0.19 | 0.00 | 0.11 | 0.03 | 0.00 | 0.99 | PARTIAL |
| vol+point_anomaly | `garch_single_point_anomaly_middle_463.csv` | 0.00 | 0.00 | 0.00 | 1.00 | 0.50 | 0.00 | 0.44 | 0.38 | 0.01 | 0.02 | PARTIAL |
| vol+variance_shift | `garch_single_variance_shift_increase_middle_406.csv` | 0.00 | 0.00 | 0.00 | 1.00 | 0.86 | 0.00 | 0.02 | 0.98 | 0.00 | 0.46 | PARTIAL |
| vol+variance_shift | `garch_single_variance_shift_increase_middle_850.csv` | 0.00 | 0.00 | 0.00 | 1.00 | 0.45 | 0.00 | 0.02 | 0.92 | 0.00 | 0.48 | PARTIAL |