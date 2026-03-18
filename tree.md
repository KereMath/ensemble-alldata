# Sampling Tree — ensemble-alldata

**N = 440 pozitif + 440 negatif per model**
**Her modelin pozitif/negatif kaynak gruplarından floor(440/grup_sayisi) ornek alinir.**
**Grup icindeki her leaf klasorden esit ornek (floor(grup_ornegi / leaf_sayisi)).**

GD   = C:\Users\user\Desktop\Generated Data
COMB = C:\Users\user\Desktop\Generated Data\Combinations

---

## Grup 1 — stationary
**Leaf: 12 | Toplam ornek: 195 | Leaf basina: 16**
Pozitif: stationary modeli (63/grup)
Negatif: diger 9 model (toplam 132 ornek bu gruptan)

```
GD\stationary\
   |- ar_long        [16]
   |- ar_medium      [16]
   |- ar_short       [16]
   |- arma_long      [16]
   |- arma_medium    [16]
   |- arma_short     [16]
   |- ma_long        [16]
   |- ma_medium      [16]
   |- ma_short       [16]
   |- wn_long        [16]
   |- wn_medium      [16]
   |- wn_short       [16]
```

---

## Grup 2 — deterministic_trend
**Leaf: 72 | Toplam ornek: 140 | Leaf basina: 2**
Pozitif: deterministic_trend modeli (20/grup)
Negatif: diger 9 model (toplam 120 ornek bu gruptan)

```
GD\deterministic_trend\
   |- AR\cubic\long          [2]
   |- AR\cubic\medium        [2]
   |- AR\cubic\short         [2]
   |- AR\damped\long         [2]
   |- AR\damped\medium       [2]
   |- AR\damped\short        [2]
   |- AR\exponential\long    [2]
   |- AR\exponential\medium  [2]
   |- AR\exponential\short   [2]
   |- AR\linear_down\long    [2]
   |- AR\linear_down\medium  [2]
   |- AR\linear_down\short   [2]
   |- AR\linear_up\long      [2]
   |- AR\linear_up\medium    [2]
   |- AR\linear_up\short     [2]
   |- AR\quadratic\long      [2]
   |- AR\quadratic\medium    [2]
   |- AR\quadratic\short     [2]
   |- ARMA\cubic\long        [2]
   |- ARMA\cubic\medium      [2]
   |- ARMA\cubic\short       [2]
   |- ARMA\damped\long       [2]
   |- ARMA\damped\medium     [2]
   |- ARMA\damped\short      [2]
   |- ARMA\exponential\long  [2]
   |- ARMA\exponential\medium[2]
   |- ARMA\exponential\short [2]
   |- ARMA\linear_down\long  [2]
   |- ARMA\linear_down\medium[2]
   |- ARMA\linear_down\short [2]
   |- ARMA\linear_up\long    [2]
   |- ARMA\linear_up\medium  [2]
   |- ARMA\linear_up\short   [2]
   |- ARMA\quadratic\long    [2]
   |- ARMA\quadratic\medium  [2]
   |- ARMA\quadratic\short   [2]
   |- MA\cubic\long          [2]
   |- MA\cubic\medium        [2]
   |- MA\cubic\short         [2]
   |- MA\damped\long         [2]
   |- MA\damped\medium       [2]
   |- MA\damped\short        [2]
   |- MA\exponential\long    [2]
   |- MA\exponential\medium  [2]
   |- MA\exponential\short   [2]
   |- MA\linear_down\long    [2]
   |- MA\linear_down\medium  [2]
   |- MA\linear_down\short   [2]
   |- MA\linear_up\long      [2]
   |- MA\linear_up\medium    [2]
   |- MA\linear_up\short     [2]
   |- MA\quadratic\long      [2]
   |- MA\quadratic\medium    [2]
   |- MA\quadratic\short     [2]
   |- White_Noise\cubic\long          [2]
   |- White_Noise\cubic\medium        [2]
   |- White_Noise\cubic\short         [2]
   |- White_Noise\damped\long         [2]
   |- White_Noise\damped\medium       [2]
   |- White_Noise\damped\short        [2]
   |- White_Noise\exponential\long    [2]
   |- White_Noise\exponential\medium  [2]
   |- White_Noise\exponential\short   [2]
   |- White_Noise\linear_down\long    [2]
   |- White_Noise\linear_down\medium  [2]
   |- White_Noise\linear_down\short   [2]
   |- White_Noise\linear_up\long      [2]
   |- White_Noise\linear_up\medium    [2]
   |- White_Noise\linear_up\short     [2]
   |- White_Noise\quadratic\long      [2]
   |- White_Noise\quadratic\medium    [2]
   |- White_Noise\quadratic\short     [2]
```

---

## Grup 3 — stochastic_trend
**Leaf: 15 | Toplam ornek: 221 | Leaf basina: 15**
Pozitif: stochastic_trend modeli (88/grup)
Negatif: diger 9 model (toplam 133 ornek)

```
GD\Stochastic Trend\
   |- ARI\stochastic_ari_long      [15]
   |- ARI\stochastic_ari_medium    [15]
   |- ARI\stochastic_ari_short     [15]
   |- ARIMA\stochastic_arima_long  [15]
   |- ARIMA\stochastic_arima_medium[15]
   |- ARIMA\stochastic_arima_short [15]
   |- IMA\stochastic_ima_long      [15]
   |- IMA\stochastic_ima_medium    [15]
   |- IMA\stochastic_ima_short     [15]
   |- RW\stochastic_rw_long        [15]
   |- RW\stochastic_rw_medium      [15]
   |- RW\stochastic_rw_short       [15]
   |- RWD\stochastic_rwd_long      [15]
   |- RWD\stochastic_rwd_medium    [15]
   |- RWD\stochastic_rwd_short     [15]
```

---

## Grup 4 — volatility
**Leaf: 12 | Toplam ornek: 221 | Leaf basina: 18**
Pozitif: volatility modeli (88/grup)
Negatif: diger 9 model (toplam 133 ornek)

```
GD\Volatility\
   |- APARCH\volatility_aparch_long    [18]
   |- APARCH\volatility_aparch_medium  [18]
   |- APARCH\volatility_aparch_short   [18]
   |- ARCH\volatility_arch_long        [18]
   |- ARCH\volatility_arch_medium      [18]
   |- ARCH\volatility_arch_short       [18]
   |- EGARCH\volatility_egarch_long    [18]
   |- EGARCH\volatility_egarch_medium  [18]
   |- EGARCH\volatility_egarch_short   [18]
   |- GARCH\volatility_garch_long      [18]
   |- GARCH\volatility_garch_medium    [18]
   |- GARCH\volatility_garch_short     [18]
```

---

## Grup 5 — collective_anomaly (tekli)
**Leaf: 48 | Toplam ornek: 236 | Leaf basina: 5**
Pozitif: stationary(63) + collective_anomaly(55) modelleri
Negatif: diger 8 model (toplam 118 ornek)

```
GD\collective_anomaly\
   |- AR\long\multiple              [5]
   |- AR\long\single\beginning      [5]
   |- AR\long\single\end            [5]
   |- AR\long\single\middle         [5]
   |- AR\medium\multiple            [5]
   |- AR\medium\single\beginning    [5]
   |- AR\medium\single\end          [5]
   |- AR\medium\single\middle       [5]
   |- AR\short\multiple             [5]
   |- AR\short\single\beginning     [5]
   |- AR\short\single\end           [5]
   |- AR\short\single\middle        [5]
   |- ARMA\long\multiple            [5]
   |- ARMA\long\single\beginning    [5]
   |- ARMA\long\single\end          [5]
   |- ARMA\long\single\middle       [5]
   |- ARMA\medium\multiple          [5]
   |- ARMA\medium\single\beginning  [5]
   |- ARMA\medium\single\end        [5]
   |- ARMA\medium\single\middle     [5]
   |- ARMA\short\multiple           [5]
   |- ARMA\short\single\beginning   [5]
   |- ARMA\short\single\end         [5]
   |- ARMA\short\single\middle      [5]
   |- MA\long\multiple              [5]
   |- MA\long\single\beginning      [5]
   |- MA\long\single\end            [5]
   |- MA\long\single\middle         [5]
   |- MA\medium\multiple            [5]
   |- MA\medium\single\beginning    [5]
   |- MA\medium\single\end          [5]
   |- MA\medium\single\middle       [5]
   |- MA\short\multiple             [5]
   |- MA\short\single\beginning     [5]
   |- MA\short\single\end           [5]
   |- MA\short\single\middle        [5]
   |- White_Noise\long\multiple             [5]
   |- White_Noise\long\single\beginning     [5]
   |- White_Noise\long\single\end           [5]
   |- White_Noise\long\single\middle        [5]
   |- White_Noise\medium\multiple           [5]
   |- White_Noise\medium\single\beginning   [5]
   |- White_Noise\medium\single\end         [5]
   |- White_Noise\medium\single\middle      [5]
   |- White_Noise\short\multiple            [5]
   |- White_Noise\short\single\beginning    [5]
   |- White_Noise\short\single\end          [5]
   |- White_Noise\short\single\middle       [5]
```

---

## Grup 6 — contextual_anomaly (tekli)
**Leaf: 48 | Toplam ornek: 623 | Leaf basina: 13**
Pozitif: stationary(63) + contextual_anomaly(440) modelleri
Negatif: diger 8 model (toplam 120 ornek)

```
GD\contextual_anomaly\
   |- AR\long\multiple                              [13]
   |- AR\long\single\beginning\AR_long_beginning    [13]
   |- AR\long\single\end\AR_long_end                [13]
   |- AR\long\single\middle\AR_long_middle          [13]
   |- AR\medium\multiple                            [13]
   |- AR\medium\single\beginning\AR_medium_beginning[13]
   |- AR\medium\single\end\AR_medium_end            [13]
   |- AR\medium\single\middle\AR_medium_middle      [13]
   |- AR\short\multiple                             [13]
   |- AR\short\single\beginning\AR_short_beginning  [13]
   |- AR\short\single\end\AR_short_end              [13]
   |- AR\short\single\middle\AR_short_middle        [13]
   |- ARMA\...  (ayni yapi x12)                    [13]
   |- MA\...    (ayni yapi x12)                    [13]
   |- White_Noise\... (ayni yapi x12)              [13]
```

---

## Grup 7 — mean_shift (tekli)
**Leaf: 48 | Toplam ornek: 236 | Leaf basina: 5**
Pozitif: stationary(63) + mean_shift(55) modelleri
Negatif: diger 8 model

```
GD\mean_shift\
   |- AR\long\multiple           [5]
   |- AR\long\single\beginning   [5]
   |- AR\long\single\end         [5]
   |- AR\long\single\middle      [5]
   |- AR\medium\... (x4)         [5]
   |- AR\short\...  (x4)         [5]
   |- ARMA\...      (x12)        [5]
   |- MA\...        (x12)        [5]
   |- White_Noise\... (x12)      [5]
```

---

## Grup 8 — point_anomaly (tekli)
**Leaf: 48 | Toplam ornek: 236 | Leaf basina: 5**
Pozitif: stationary(63) + point_anomaly(55) modelleri
Negatif: diger 8 model

```
GD\point_anomaly\
   (Grup 5 ile ayni yapi — 48 leaf, her leaf [5])
```

---

## Grup 9 — trend_shift (tekli)
**Leaf: 48 | Toplam ornek: 403 | Leaf basina: 8**
Pozitif: stationary(63) + trend_shift(220) modelleri
Negatif: diger 8 model

```
GD\trend_shift\
   (48 leaf, her leaf [8])
```

---

## Grup 10 — variance_shift (tekli)
**Leaf: 48 | Toplam ornek: 236 | Leaf basina: 5**
Pozitif: stationary(63) + variance_shift(55) modelleri
Negatif: diger 8 model

```
GD\variance_shift\
   (48 leaf, her leaf [5])
```

---

## Grup 11 — cubic + collective_anomaly
**Leaf: 1 | Toplam ornek: 181 | Leaf basina: 181**
Pozitif: deterministic_trend(20) + collective_anomaly(55)
Negatif: 8 model (toplam 106)

```
COMB\Cubic Base\Cubic Base\cubic_collective_anomaly\
   |- data   [181]
```

---

## Grup 12 — cubic + mean_shift
**Leaf: 2 | Toplam ornek: 181 | Leaf basina: 90**
Pozitif: deterministic_trend(20) + mean_shift(55)
Negatif: 8 model (toplam 106)

```
COMB\Cubic Base\Cubic Base\Cubic + Mean Shift\
   |- cubic_mean_shift_1\data   [90]
   |- data                      [90]
```

---

## Grup 13 — cubic + point_anomaly
**Leaf: 1 | Toplam ornek: 181 | Leaf basina: 181**
Pozitif: deterministic_trend(20) + point_anomaly(55)

```
COMB\Cubic Base\Cubic Base\Cubic + Point Anomaly\
   |- data   [181]
```

---

## Grup 14 — cubic + variance_shift
**Leaf: 1 | Toplam ornek: 181 | Leaf basina: 181**
Pozitif: deterministic_trend(20) + variance_shift(55)

```
COMB\Cubic Base\Cubic Base\Cubic + Variance Shift\
   |- data   [181]
```

---

## Grup 15 — damped + collective_anomaly
**Leaf: 1 | Toplam ornek: 181 | Leaf basina: 181**
Pozitif: deterministic_trend(20) + collective_anomaly(55)

```
COMB\Damped Base\Damped Base\Damped + Collective Anomaly\
   |- data   [181]
```

---

## Grup 16 — damped + mean_shift
**Leaf: 2 | Toplam ornek: 181 | Leaf basina: 90**
Pozitif: deterministic_trend(20) + mean_shift(55)

```
COMB\Damped Base\Damped Base\Damped + Mean Shift\
   |- data (1. klasor)   [90]
   |- data (2. klasor)   [90]
```

---

## Grup 17 — damped + point_anomaly
**Leaf: 1 | Toplam ornek: 181 | Leaf basina: 181**

```
COMB\Damped Base\Damped Base\Damped + Point Anomaly\
   |- data   [181]
```

---

## Grup 18 — damped + variance_shift
**Leaf: 1 | Toplam ornek: 181 | Leaf basina: 181**

```
COMB\Damped Base\Damped Base\Damped + Variance Shift\
   |- data   [181]
```

---

## Grup 19 — exponential + collective_anomaly
**Leaf: 1 | Toplam ornek: 181 | Leaf basina: 181**
Pozitif: deterministic_trend(20) + collective_anomaly(55)

```
COMB\Exponential Base\Exponential Base\exponential_collective_anomaly\
   |- data   [181]
```

---

## Grup 20 — exponential + mean_shift
**Leaf: 2 | Toplam ornek: 181 | Leaf basina: 90**
Pozitif: deterministic_trend(20) + mean_shift(55)

```
COMB\Exponential Base\Exponential Base\Exponential + Mean Shift\
   |- data (1. klasor)   [90]
   |- data (2. klasor)   [90]
```

---

## Grup 21 — exponential + point_anomaly
**Leaf: 1 | Toplam ornek: 181 | Leaf basina: 181**

```
COMB\Exponential Base\Exponential Base\exponential_point_anomaly\
   |- data   [181]
```

---

## Grup 22 — exponential + variance_shift
**Leaf: 1 | Toplam ornek: 181 | Leaf basina: 181**

```
COMB\Exponential Base\Exponential Base\exponential_variance_shift\
   |- data   [181]
```

---

## Grup 23 — linear + collective_anomaly
**Leaf: 1 | Toplam ornek: 181 | Leaf basina: 181**
Pozitif: deterministic_trend(20) + collective_anomaly(55)

```
COMB\Linear Base\Linear Base\Linear + Collective Anomaly\
   |- data   [181]   (2000 CSV mevcut)
```

---

## Grup 24 — linear + mean_shift
**Leaf: 2 | Toplam ornek: 181 | Leaf basina: 90**
Pozitif: deterministic_trend(20) + mean_shift(55)

```
COMB\Linear Base\Linear Base\Linear + Mean Shift\
   |- data (1. klasor)   [90]
   |- data (2. klasor)   [90]
```

---

## Grup 25 — linear + point_anomaly
**Leaf: 1 | Toplam ornek: 181 | Leaf basina: 181**
Pozitif: deterministic_trend(20) + point_anomaly(55)

```
COMB\Linear Base\Linear Base\Linear + Point Anomaly\
   |- data   [181]   (2000 CSV mevcut)
```

---

## Grup 26 — linear + trend_shift
**Leaf: 3 | Toplam ornek: 348 | Leaf basina: 116**
Pozitif: deterministic_trend(20) + trend_shift(220)
Negatif: 8 model (toplam 108)

```
COMB\Linear Base\Linear Base\Linear + Trend Shift\
   |- data (1. klasor)   [116]
   |- data (2. klasor)   [116]
   |- data (3. klasor)   [116]
```

---

## Grup 27 — linear + variance_shift
**Leaf: 1 | Toplam ornek: 181 | Leaf basina: 181**
Pozitif: deterministic_trend(20) + variance_shift(55)

```
COMB\Linear Base\Linear Base\Linear + Variance Shift\
   |- data   [181]
```

---

## Grup 28 — quadratic + collective_anomaly
**Leaf: 1 | Toplam ornek: 181 | Leaf basina: 181**
Pozitif: deterministic_trend(20) + collective_anomaly(55)

```
COMB\Quadratic Base\Quadratic Base\Quadratic + Collective anomaly\
   |- data   [181]
```

---

## Grup 29 — quadratic + mean_shift
**Leaf: 2 | Toplam ornek: 181 | Leaf basina: 90**
Pozitif: deterministic_trend(20) + mean_shift(55)

```
COMB\Quadratic Base\Quadratic Base\Quadratic + Mean Shift\
   |- data (1. klasor)   [90]
   |- data (2. klasor)   [90]
```

---

## Grup 30 — quadratic + point_anomaly
**Leaf: 2 | Toplam ornek: 181 | Leaf basina: 90**
Pozitif: deterministic_trend(20) + point_anomaly(55)

```
COMB\Quadratic Base\Quadratic Base\Quadratic + Point Anomaly\
   |- data (1. klasor)   [90]
   |- data (2. klasor)   [90]
```

---

## Grup 31 — quadratic + variance_shift
**Leaf: 1 | Toplam ornek: 181 | Leaf basina: 181**
Pozitif: deterministic_trend(20) + variance_shift(55)

```
COMB\Quadratic Base\Quadratic Base\Quadratic + Variance Shift\
   |- data   [181]
```

---

## Grup 32 — stochastic + collective_anomaly
**Leaf: 1 | Toplam ornek: 262 | Leaf basina: 262**
Pozitif: stochastic_trend(88) + collective_anomaly(55)
Negatif: 8 model (toplam 119)

```
COMB\Stochastic Trend + Collective Anomaly\
   |- Stochastic Trend + Collective Anomaly   [262]
```

---

## Grup 33 — stochastic + mean_shift
**Leaf: 1 | Toplam ornek: 262 | Leaf basina: 262**
Pozitif: stochastic_trend(88) + mean_shift(55)

```
COMB\Stochastic Trend + Mean Shift\
   |- Stochastic Trend + Mean Shift   [262]
```

---

## Grup 34 — stochastic + point_anomaly
**Leaf: 1 | Toplam ornek: 262 | Leaf basina: 262**
Pozitif: stochastic_trend(88) + point_anomaly(55)

```
COMB\Stochastic Trend + Point Anomaly\
   |- Stochastic Trend + Point Anomaly   [262]
```

---

## Grup 35 — stochastic + variance_shift
**Leaf: 5 | Toplam ornek: 262 | Leaf basina: 52**
Pozitif: stochastic_trend(88) + variance_shift(55)
Negatif: 8 model (toplam 119)

```
COMB\Stochastic Trend + Variance Shift\Stochastic Trend + Variance Shift\
   |- ARI + Variance Shift    [52]
   |- ARIMA + Variance Shift  [52]
   |- IMA + Variance Shift    [52]
   |- RW + Variance Shift     [52]
   |- RWD + Variance Shift    [52]
```

---

## Grup 36 — volatility + collective_anomaly
**Leaf: 1 | Toplam ornek: 262 | Leaf basina: 262**
Pozitif: volatility(88) + collective_anomaly(55)

```
COMB\Volatility + Collective Anomaly\
   |- Volatility + Collective Anomaly   [262]
```

---

## Grup 37 — volatility + mean_shift
**Leaf: 1 | Toplam ornek: 262 | Leaf basina: 262**
Pozitif: volatility(88) + mean_shift(55)

```
COMB\Volatility + Mean Shift\
   |- Volatility + Mean Shift   [262]
```

---

## Grup 38 — volatility + point_anomaly
**Leaf: 1 | Toplam ornek: 262 | Leaf basina: 262**
Pozitif: volatility(88) + point_anomaly(55)

```
COMB\Volatility + Point Anomaly\
   |- Volatility + Point Anomaly   [262]
```

---

## Grup 39 — volatility + variance_shift
**Leaf: 1 | Toplam ornek: 262 | Leaf basina: 262**
Pozitif: volatility(88) + variance_shift(55)

```
COMB\Volatility + Variance Shift\
   |- Volatility + Variance Shift   [262]
```

---

## Ozet: Dikkat Edilecek Noktalar

| Durum | Gruplar | Leaf basina |
|---|---|---|
| Cok leaf, az ornek (risk: 1-2/leaf) | Grup 2 (det_trend saf, 72 leaf) | **2** |
| Az leaf, cok ornek | Grup 32-39 (stoch/vol kombolar) | **262** |
| En dengeli | Grup 3,4 (stoch/vol saf) | 15-18 |
| Sadece pozitif olarak goren | Grup 6 (contextual, tek grup) | 13 |

> Grup 2 icin leaf basina 2 ornek cok az gorunebilir ama 72 leaf x 2 = 144 ornek
> grubu temsil etmeye yeterlidir; det_trend modelinin 22 grubu var ve her grubun
> esit agirligi olmasi icin bu deger bu sekilde cikiyor.
