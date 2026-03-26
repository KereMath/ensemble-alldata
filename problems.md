# Ensemble Modelinin Bilinen Sorunları, Kırılganlıkları ve Edge Case Analizi

Bu belge; ensemble modelinin manuelalldatatest (%59.8 FULL) ile manuelcombidatatest
(%95.9 FULL) arasındaki dramatik fark başta olmak üzere, tespit edilen tüm yapısal
zayıflıkları, tsfresh özellik uzayının getirdiği temel kısıtları ve henüz test
edilmemiş edge case'leri akademik düzeyde belgeler.

---

## 1. Temel Sorun: Neden Kombinasyon Testinde %95.9, Tüm Veri Testinde %59.8?

### 1.1 In-Distribution vs. Out-of-Distribution Açığı

Bu fark, tesadüfi değil; modelin eğitim dağılımı ile gerçek dağılım arasındaki
yapısal farklılığın doğrudan sonucudur.

**Kombinasyon testi (grup 11–39):**
Her anomali modelinin pozitif örnekleri tam olarak bu klasörlerden alındı.
`collective_anomaly` modeli "pozitif = combination/*/data/*.csv" ile eğitildi.
Test sırasında aynı klasörlerin farklı CSV'leri sunuluyor — model kendi
eğitim dağılımı içinde test ediliyor. Bu, machine learning literatüründe
*in-distribution generalization* olarak bilinir ve genellikle yüksek performans verir.

**Tüm veri testi (grup 1–10 + 11–39):**
Grup 1–10, anomali modellerinin **hiç görmediği** klasörlerdir. Bu klasörler
eğitim sırasında negatif örnek kaynağı olarak kullanılmış olabilir, ancak modelin
anomali dedektörü "bu seride anomali var mı?" sorusunu değil, dolaylı olarak
"bu serinin özellikleri benim pozitif eğitim örneklerime ne kadar benziyor?" sorusunu
yanıtlar. Saf (anomalisiz) serilerin doğal varyasyonu, zaman zaman anomali
imzasına benzer tsfresh özellikleri üretir.

**Sonuç:** %95.9 → %59.8 düşüşünün %36'lık bölümü neredeyse tamamen grup 1–10'dan,
yani *saf/single-type* serilerden kaynaklanmaktadır.

---

### 1.2 Eşik Kalibrasyonunun Asimetrik Etkisi

Anomali modelleri 0.5 eşiğiyle çalışır. Bu eşik, eğitim setinin sınıf dağılımına
göre optimize edilmiştir — yaklaşık %50 pozitif / %50 negatif. Ancak gerçek dünya
verisinde anomali sıklığı çok daha düşüktür (örn. %5–20).

Bayes teoremi çerçevesinde:

```
P(anomaly | features) ∝ P(features | anomaly) × P(anomaly)
```

Model yalnızca `P(features | anomaly)`'yi öğrenir; `P(anomaly)` (prior) sabit
0.5 olarak kabul edilir. Gerçek veri için prior düşükse, 0.5 eşiği sistematik
olarak **false positive üretir**. Bu, özellikle grup 1–4 (hiç anomali yok) için
yıkıcıdır: model anomali olmadığı hâlde anomali bildirir.

**Gözlemlenen etki:**
- Grup 1 (stationary, 120 örnek): %31 FULL, %43 PARTIAL
  → PARTIAL'ın neredeyse tamamı "doğru base, ekstra false positive anomali"
- Grup 3 (stochastic_trend, 150 örnek): %26 FULL, %69 PARTIAL
  → Seri kendisi variance_shift benzeri özellikler üretiyor
- Grup 4 (volatility, 120 örnek): %40 FULL, %59 PARTIAL
  → GARCH/ARCH sürecinin doğal spike'ları anomali olarak algılanıyor

---

## 2. Özellik Uzayı Çakışmaları (Feature Space Confounds)

Aşağıdaki her sorun, farklı zaman serisi patternlerinin tsfresh EfficientFCParameters
(777 özellik) uzayında birbirine yakın bölgelere düşmesinden kaynaklanır.
Bu, modelin hatası değil; seçilen özellik setinin bu ayrımı yapamadığının göstergesidir.

---

### 2.1 Mean Shift → Variance Shift False Positive (Yüksek Etki)

**Mekanizma:** Bir seriye mean shift eklendiğinde, shift noktasının öncesi ve sonrası
iki farklı ortalamaya sahip segment oluşur. tsfresh'in aşağıdaki özellikleri bu iki
segmenti **varyans farkı** olarak yorumlar:

- `change_quantile` (coeff_var, mean, variance üzerinden)
- `linear_trend` (slope, intercep — shift noktasında kırılma üretir)
- `agg_linear_trend` (segmentlerin ağırlıklı varyansı)
- `ratio_beyond_r_sigma` (shift sonrası değerler, global σ referansına göre aşırı)

Bu özellikler, mean shift varlığında `variance_shift` modelinin pozitif örnek
özellik profiliyle **örtüşen bir bölge** oluşturur.

**Kanıt (manuelcombidatatest):**
- Grup 12 (cubic+mean_shift): 20 örnekten 2'si PARTIAL (mean_shift kaçtı, variance_shift kaldı)
- Grup 33 (stoch+mean_shift): 10 örnekten 4'ü PARTIAL — en kötü kombinasyon grubu
- Grup 16 (damped+mean_shift): 20 örnekten 2'si PARTIAL

**Kanıt (manuelalldatatest, Grup 7 — stationary+mean_shift):**
480 örnekten yalnızca %64'ü FULL. PARTIAL örneklerin büyük bölümü
"mean_shift + variance_shift birlikte tahmin edildi" şeklinde.

**Yön:** Hem false positive (mean_shift yok ama variance_shift algılandı) hem de
label swap (mean_shift yerine variance_shift seçildi) formunda görünür.

---

### 2.2 Stochastic Trend ↔ Variance Shift Karışıklığı (Yüksek Etki)

**Mekanizma:** Random walk `x_t = x_{t-1} + ε_t` sürecinde varyans zamana göre
lineer büyür: `Var(x_t) = t·σ²`. Bu *heterokedastik* yapı, tsfresh'in
`augmented_dickey_fuller`, `agg_autocorrelation` ve özellikle `partial_autocorrelation`
özelliklerinde variance_shift imzasıyla örtüşür.

`variance_shift` modeli eğitim sırasında "varyansın ani değiştiği seriler = pozitif"
öğrenir. Random walk'ın kümülatif varyans artışı ani değildir; ancak serinin ilk
ve son yarısı karşılaştırıldığında ikinci yarının varyansı çok daha yüksektir —
bu, segment bazlı özellikler açısından variance_shift ile ayırt edilemez.

**Kanıt:**
- Grup 3 (stochastic_trend, 150 örnek): %26 FULL, %69 PARTIAL
  → PARTIAL'ın büyük çoğunluğu "stochastic_trend + variance_shift" tahmini
- Grup 35 (stoch+variance_shift): %96 FULL — gerçek variance_shift var ve bulunuyor ✓

---

### 2.3 Stationary → Anomali False Positive (Orta-Yüksek Etki)

**Mekanizma:** Yüksek AR katsayılı (`ar_coefficient` > 0.7) durağan seriler
uzun süreli belleğe sahiptir. Bu bellek:
- `mean_shift` benzeri: ardışık pozitif/negatif run'lar oluşturur
- `collective_anomaly` benzeri: belirli bir aralıkta konsantre kalan değerler
- `point_anomaly` benzeri: nadiren gelen uç değerler (AR(1) ile bile olası)

Özellikle `ar_medium` ve `ar_long` klasörlerinden gelen seriler bu sorundan
en çok etkileninenlerdir.

**Kanıt (manuelalldatatest, Grup 1):**
```
ar_medium/ar_26081.csv → stationary + collective_anomaly + mean_shift  (PARTIAL)
ar_medium/ar_7284.csv  → stationary + mean_shift + trend_shift         (PARTIAL)
ar_medium/ar_12561.csv → stationary + collective_anomaly               (PARTIAL)
ar_long/ar_28856.csv   → stationary + point_anomaly                    (PARTIAL)
```
Tüm bu seriler anomalisiz saf AR serisidir; model halüsinasyon üretiyor.

---

### 2.4 Volatility → False Positive Anomali (Orta Etki)

**Mekanizma:** GARCH/ARCH/EGARCH/APARCH süreçlerinde koşullu varyans
`σ²_t = α₀ + α₁ε²_{t-1} + β₁σ²_{t-1}` şeklinde kümelenir. Yüksek volatilite
dönemleri ardışık büyük değerler üretir → `collective_anomaly` sinyali.
Ani volatilite patlamaları tek büyük gözlem bırakır → `point_anomaly` sinyali.
Volatilite rejimleri arası geçiş → `variance_shift` sinyali.

GARCH doğası gereği anomali-benzeri özellikler üretir; ancak bu anomali değil,
sürecin kendisidir.

**Kanıt:**
- Grup 4 (volatility): %40 FULL, %59 PARTIAL
- Örnek: `garch_684.csv` → volatility: 1.00, collective: 0.89, point: 0.71

---

### 2.5 Deterministic Trend Tespiti: AR Gürültüsü Bastırma Problemi (Yüksek Etki)

**Mekanizma:** `linear_trend` ve `quadratic_trend` leaflerinde trend slope'u
düşük-orta olduğunda, yüksek AR katsayılı gürültü trend sinyalini bastırır.
tsfresh'in `linear_trend` özelliği OLS kullanır; gürültü artınca β_trend
istatistiksel olarak anlamsızlaşır ve sıfıra yaklaşır.

Bu durumda `deterministic_trend` modeli P≈0.00 verir; `argmax` base_type
olarak ya `stationary` ya da `stochastic_trend` seçer.

**Kanıt:**
- Grup 2 (deterministic_trend, 720 örnek): %31 FULL, %64 NONE
  → 458 NONE: base_type tamamen yanlış seçildi
- Özellikle `ar_linear_*`, `arma_linear_*`, `ma_linear_*` leafleri
- Örnek: `ar_linear_down_trend_312.csv` → det_trend: 0.00, stationary: 1.00

**Kombinasyon testinde neden görünmüyor?**
Kombinasyon klasörleri (`cubic+`, `damped+`, `exp+`, `linear+`, `quad+`) eğitim
setinin pozitif kısmıdır. Model bu klasörler için doğru çalışıyor çünkü eğitim
sırasında bunları deterministic olarak öğrendi. Sorun yalnızca "saf" grup 2
klasörlerinde ortaya çıkıyor.

---

## 3. Manuelalldatatest vs. Manuelcombidatatest: Farkın Tam Analizi

| Metrik       | Combi Test (11–39) | All-Data Test (1–39) |
|---|---|---|
| Toplam örnek | 410                | 4400                 |
| FULL         | 393 (%95.9)        | 2632 (%59.8)         |
| PARTIAL      | 17 (%4.1)          | 1083 (%24.6)         |
| NONE         | 0 (%0.0)           | 685 (%15.6)          |

All-data testindeki 685 NONE'un neredeyse tamamı grup 2 (deterministic_trend)
kaynaklıdır: 458 NONE tek başına. Grup 2 dışlandığında NONE oranı dramatik düşer.

All-data testindeki 1083 PARTIAL'ın bileşimi:
1. **Doğru base + ekstra anomali (false positive):** Grup 1, 3, 4 ağırlıklı
2. **Doğru base + yanlış anomali (label swap):** Grup 7 (mean_shift→variance_shift)
3. **Yanlış base + doğru anomali:** Nadiren; genellikle NONE olur

Combinasyon testinin başarısı **modelin iyi olduğunu göstermez**;
anomalileri tanıdığı bağlamda (anomalinin üzerine yerleştirildiği process)
iyi çalıştığını gösterir. Gerçek dünyada base process her zaman bilinmiyor.

---

## 4. Kısa Seri Performans Düşüşü

**Mekanizma:** tsfresh'in temel özelliklerinden birkaçı asgari timestep sayısı ister:

- `autocorrelation(lag=k)`: k+1 gözlem gerekir; `_short` serilerde yüksek lag hesaplanamaz
- `cwt_coefficients`: continuous wavelet transform için yeterli frekans çözünürlüğü yok
- `friedrich_coefficients`: Langevin fit için > ~100 gözlem önerilir
- `sample_entropy`: en az 200–300 gözlemde güvenilir

50–150 timestep aralığındaki seriler teknik olarak kabul edilse de (MIN_SERIES_LENGTH=50)
bu özellikler NaN döner, `impute` ile 0'a set edilir → bilgi kaybı → model
bu seriler için gürültüye yakın özellik vektörü alır.

**Etkilenen gruplar:** Tüm gruplardaki `_short` leaf klasörleri.

---

## 5. Yapısal Kör Noktalar: Eğitim Setinde Olmayan Kombinasyonlar

Aşağıdaki durumlar eğitim setinde hiç görülmemiştir. Modelin bu girişlerde
ne döndüreceği **tamamen bilinmemektedir** — ve büyük olasılıkla yanlış olacaktır.

### 5.1 Çoklu Anomali (base + 2+ anomali)

Eğitim seti yalnızca `base + 1 anomali` içerir. `mean_shift + variance_shift`
aynı anda gerçekleşse model muhtemelen her ikisini de algılar (çünkü her iki
modeli ayrı ayrı "tetikler"), ancak bu başarı değil rastlantı olur.
`point_anomaly + collective_anomaly + mean_shift` üçlüsünde ne olacağı belirsizdir.

**Tahmin:** Model büyük olasılıkla yalnızca en baskın anomaliyi (%P yüksek olan)
yakalar; diğerleri 0.5 eşiğinin altında kalabilir veya tüm anomali modelleri
birlikte aktive olabilir (false positive karmaşası).

### 5.2 Sinusoidal Deterministic Trend + Anomali

`sinusoidal` leaf klasörü sadece grup 2 (saf deterministic_trend) içinde var.
Kombinasyon klasörlerinde `sinusoidal + anomali` hiç oluşturulmamıştır.
Model `sinusoidal + mean_shift` ile karşılaşırsa:
- `deterministic_trend` algılar (muhtemelen evet — sinusoidal eğitimde görüldü)
- Anomaliyi algılar (belirsiz — bu bağlamda görülmedi)

### 5.3 Trend Shift: Eksik Base Kombinasyonları

Eğitim setinde `trend_shift` sadece `linear + trend_shift` kombinasyonuyla var
(grup 26). `cubic`, `damped`, `exponential`, `quadratic` base ile `trend_shift`
kombinasyonu hiç görülmedi. Bu baseler için model `trend_shift` anomalisini
tanıyamayabilir veya başka anomali olarak yorumlayabilir.

### 5.4 Contextual Anomaly + Non-Stationary Base

`contextual_anomaly` modeli yalnızca `stationary + contextual_anomaly` pozitif
örneklerle eğitildi (grup 6). `deterministic_trend + contextual_anomaly` veya
`stochastic_trend + contextual_anomaly` hiç görülmedi. Trend bağlamında
contextual anomaly, tsfresh özelliklerinde farklı bir iz bırakabilir — model
bunu kaçırabilir.

**Not:** Grup 6 (stationary+contextual_anomaly) all-data testinde %99 FULL ile
en iyi performans gösteren gruptur. Ancak bu başarı yalnızca stationary base
için geçerlidir.

### 5.5 Volatility + Trend Shift

Veri setinde `volatility + trend_shift` kombinasyon klasörü yoktur.
GARCH sürecinde regime değişimi ile deterministik trend kırılması benzer
tsfresh özellikleri üretir; model bunu ne base type ne de anomali olarak
doğru yorumlayamayacaktır.

### 5.6 Çok Uzun Seriler (5000+ Timestep)

`_long` leafler genellikle 500–2000 timestep içerir. 5000+ timestep:
- tsfresh özelliklerinin bazıları O(n²) veya O(n log n) karmaşıklığındadır
- `approximate_entropy`, `sample_entropy` çok uzun seride farklı yoğunluk
  dağılımı üretir
- Global istatistikler (mean, std) büyük n'de daha stabil → bazı özellikler
  normalize olur → model bu normalleşmeyi "anomali yok" olarak yorumlayabilir

Eğitim setinin dışına çıkan uzunluklarda model davranışı **belirsizdir**.

### 5.7 Çok Zayıf Anomali Sinyali

0.5 eşiği, eğitim setindeki ortalama anomali gücüne göre ayarlanmıştır.
Anomali genliği küçük olursa (örn. mean shift miktarı = 0.2σ), model
P(anomaly) ≈ 0.3–0.4 döndürür ve anomaliyi kaçırır. Eşik duyarlılığı
hiç test edilmemiştir.

### 5.8 Birden Fazla Mean Shift

`mean_shift` leaf klasöründe `multiple` alt klasörler var (iki veya daha fazla
shift noktası). Kombinasyon klasörlerinde `base + multiple_mean_shift` yok.
Modelin böyle bir seride:
1. mean_shift'i fark edip etmeyeceği
2. Aynı zamanda variance_shift false positive üretip üretmeyeceği
bilinmiyor.

---

## 6. Eşik Optimizasyonu: Bağlam-Bağımlı Kalibrasyon Gerekliliği

Mevcut model sabit eşik (THRESHOLD = 0.5) kullanır. Ancak:

| Bağlam | Optimal Eşik | Gerekçe |
|---|---|---|
| Genel kullanım | 0.5 | Dengeli prior varsayımı |
| Volatility base seçildiğinde | 0.70–0.80 | GARCH false positive bastırma |
| Mean_shift bağlamında variance_shift | 0.65 | Segment varyans çakışması |
| Stochastic base seçildiğinde variance_shift | 0.65 | Kümülatif varyans artışı |
| Stationary base + anomali yok beklentisi | 0.60 | False positive bastırma |

Bağlam-bağımlı eşik (`decode` fonksiyonunda seçilen base_type'a göre anomali
eşiğini dinamik olarak ayarlamak) en doğrudan iyileştirme yoludur.

---

## 7. Önerilen İyileştirmeler

| # | Sorun | Öneri | Zorluk |
|---|---|---|---|
| 1 | variance_shift FP on mean_shift | Bağlam-bağımlı eşik: mean_shift grubunda variance_shift eşiğini 0.65'e çıkar | Düşük |
| 2 | Volatility anomali FP | base=volatility ise tüm anomali eşiklerini 0.70'e çıkar | Düşük |
| 3 | Stochastic trend → variance_shift FP | base=stochastic ise variance_shift eşiğini 0.65'e çıkar | Düşük |
| 4 | Stationary false positive anomali | Anomali modellerine negatif örnek olarak saf stationary ağırlığını artır | Orta |
| 5 | Linear/quadratic trend tespiti | Eğitim setinde ar_linear/arma_linear leaflerini ağırlıklandır; veya `weak_trend` yardımcı özelliği ekle | Orta |
| 6 | Kısa seri | MIN_SERIES_LENGTH'i 100–150'ye çıkar veya kısa seriler için ayrı özellik seti | Orta |
| 7 | In-distribution test şişirmesi | Gerçek OOD test seti: eğitimde hiç görülmeyen process parametrelerinden yeni CSV üret | Yüksek |
| 8 | Çoklu anomali desteği | `base + 2 anomali` kombinasyonlarıyla yeni eğitim verisi ekle | Yüksek |
| 9 | Threshold kalibrasyonu | Val seti üzerinde ROC eğrisi ile anomali başına optimal eşik bul | Orta |

---

## 8. Özet: Performans Matrisi

| Grup Kategorisi | FULL% | Temel Başarısızlık Modu |
|---|---|---|
| Saf base type (1–4) | %20–40 | False positive anomali; det_trend kaçırmak |
| Stationary + anomali (5–10) | %51–99 | variance_shift FP, point_anomaly FP; contextual %99 aykırı |
| Kombinasyon: det_trend + anomali (11–31) | %90–100 | Yalnızca mean_shift grubunda variance_shift çakışması |
| Kombinasyon: stoch_trend + anomali (32–35) | %60–100 | stoch+mean_shift en kötü (%60) |
| Kombinasyon: volatility + anomali (36–39) | %80–100 | point_anomaly ve variance_shift tespiti zayıf |

**Kritik çıkarım:** Model, *anomali varlığını tespit etme* konusunda güçlüdür
(`contextual_anomaly` %99, `trend_shift` %74, kombinasyon ortalaması %95.9).
Asıl zayıflık **anomali yokken sessiz kalmak** (false positive bastırma) ve
**zayıf trend sinyalini gürültüden ayırmak**tır.
