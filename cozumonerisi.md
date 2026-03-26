# Ensemble Sisteminin Sorunları, Kök Nedenleri ve Çözüm Önerileri

Bu belge; mevcut iki ensemble sisteminin tespit edilen zayıflıklarını,
bu zayıflıkların kök nedenlerini, iki sistemin birbirini neden tamamladığını
ve üç farklı zorluk seviyesinde somut çözüm önerilerini kapsamlı biçimde belgeler.

---

## 1. Mevcut Durum: İki Ensemble, İki Farklı Güç Profili

Sistemde iki bağımsız tsfresh tabanlı ensemble mevcuttur:

### 1.1 Eski Ensemble (`tsfresh ensemble/`)

- **Mimari:** 9 bağımsız binary detector
- **Sınıflar:** `collective_anomaly`, `contextual_anomaly`, `deterministic_trend`,
  `mean_shift`, `point_anomaly`, `stochastic_trend`, `trend_shift`,
  `variance_shift`, `volatility`
- **Eğitim verisi:** Tekli etiketli seriler — her seri tek bir sınıfa ait
- **Güçlü olduğu yer:** "Bu seride mean_shift var mı?", "Bu seri deterministic_trend mi?"
  gibi tekli sorulara yüksek doğrulukla yanıt verebiliyor
- **Başarısız olduğu yer:** Kombinasyon verisi hiç görmedi. `base_type + anomali_type`
  yapısını çözemiyor. `stationary` sınıfı yok.

### 1.2 Yeni Ensemble (`ensemble-alldata/`)

- **Mimari:** 10 binary model (4 base type + 6 anomali type)
- **Sınıflar:** `stationary`, `deterministic_trend`, `stochastic_trend`, `volatility`
  (base) + `collective_anomaly`, `contextual_anomaly`, `mean_shift`, `point_anomaly`,
  `trend_shift`, `variance_shift` (anomali)
- **Eğitim verisi:** Kombinasyon klasörleri — `base_process + anomali` şeklinde sentezlenmiş
- **Güçlü olduğu yer:** Kombinasyon tespiti — `manuelcombidatatest` sonucu %95.9 FULL
- **Başarısız olduğu yer:** Tekli/saf serilerde false positive anomali üretiyor.
  `manuelalldatatest` genel sonucu %59.8 FULL; özellikle grup 1–4 %20–40 FULL.

---

## 2. Temel Sorun: Neden %95.9 → %59.8?

### 2.1 In-Distribution / Out-of-Distribution Açığı

Kombinasyon testinin (%95.9) yüksek çıkması modelin iyi genelleştiğini **değil**,
kendi eğitim dağılımında test edildiğini gösterir. Her anomali modelinin pozitif
örnekleri tam olarak aynı kombinasyon klasörlerinden alındı; test sırasında
aynı klasörlerin farklı CSV'leri sunuluyor — bu *in-distribution generalization*'dır.

Tüm veri testi (%59.8) ise grup 1–10'u içerir. Bu klasörler anomali modellerinin
hiç görmediği bağlamlardır. Model burada gerçek dünya koşullarını simüle eden
*out-of-distribution* (OOD) veriye maruz kalır.

### 2.2 Prior Mismatch: Bayes Perspektifinden Kök Neden

Anomali modelleri 0.5 eşiğiyle çalışır. Bu eşik, eğitim setinin yaklaşık %50
pozitif / %50 negatif sınıf dağılımına göre optimize edilmiştir. Bayes teoremi:

```
P(anomali | özellikler) ∝ P(özellikler | anomali) × P(anomali)
```

Model yalnızca `P(özellikler | anomali)` terimini öğrenir. Gerçek veri için
anomali prior'ı düşükse (anomalisiz saf seriler çoğunluksa), 0.5 eşiği
sistematik biçimde **false positive** üretir.

Grup 1–4 için bu yıkıcıdır: model anomali olmadığı hâlde anomali bildirir.

**Somut kanıt:**
```
Grup 1 (stationary, 120 örnek):   FULL %31, PARTIAL %43
Grup 3 (stochastic_trend, 150):   FULL %26, PARTIAL %69
Grup 4 (volatility, 120):          FULL %40, PARTIAL %59
```
PARTIAL örneklerin neredeyse tamamı "doğru base type, ekstra false positive anomali"
şeklindedir.

---

## 3. Özellik Uzayı Çakışmaları: Tsfresh'in Göremediği Ayrımlar

Aşağıdaki her sorun, farklı zaman serisi patternlerinin 777 boyutlu tsfresh
özellik uzayında birbirine çok yakın bölgelere düşmesinden kaynaklanır.
Bu modelin hatası değil; seçilen özellik setinin bu iki durumu birbirinden
ayırt etmek için yeterli bilgi içermediğinin göstergesidir.

### 3.1 Mean Shift → Variance Shift False Positive

**Mekanizma:** Mean shift (ortalama kayması) shift noktasının öncesi ve
sonrasında iki farklı ortalamaya sahip segment oluşturur. tsfresh'in
`change_quantile`, `agg_linear_trend` ve `ratio_beyond_r_sigma` özellikleri
bu iki segmenti **varyans farkı** olarak yorumlar — çünkü segmentlerin
referans alınan global ortalamadan sapmaları farklıdır.

Bu, `variance_shift` modelinin pozitif örnek profiliyle örtüşen bir bölge
yaratır; model her iki durumu da "variance_shift var" olarak yakalar.

**Kanıt:**
- Grup 12 (cubic+mean_shift): 20 örnekten 2 PARTIAL — mean_shift yerine variance_shift seçildi
- Grup 33 (stoch+mean_shift): 10 örnekten 4 PARTIAL — en kötü kombinasyon grubu
- Grup 7 (stationary+mean_shift, 480 örnek): yalnızca %64 FULL
- Örnek: `cubic_meanshift1_arma_091.csv` → tahmin: `deterministic_trend + variance_shift` (mean_shift kaçtı)

### 3.2 Stochastic Trend → Variance Shift False Positive

**Mekanizma:** Random walk `x_t = x_{t-1} + ε_t` sürecinde varyans zamana
göre lineer büyür: `Var(x_t) = t·σ²`. Bu heterokedastik yapı, tsfresh'in
segment bazlı özelliklerinde variance_shift ile neredeyse aynı sinyali üretir:
serinin ilk yarısının varyansı ile ikinci yarısının varyansı arasında büyük
bir fark gözlenir — ancak bu anomali değil, sürecin doğal özelliğidir.

**Kanıt:**
- Grup 3 (stochastic_trend, 150 örnek): %26 FULL, %69 PARTIAL
  → PARTIAL'ın büyük çoğunluğu "stochastic_trend + variance_shift" tahmini

### 3.3 Stationary AR Serileri → False Positive Anomali

**Mekanizma:** Yüksek AR katsayılı (> 0.7) durağan seriler uzun süreli belleğe
sahiptir. Bu bellek:
- Ardışık pozitif/negatif değer streak'leri → `mean_shift` veya `collective_anomaly` sinyali
- Belirli bir aralıkta konsantre kalan değerler → `collective_anomaly` sinyali
- Nadiren gelen uç değerler → `point_anomaly` sinyali

Seri tamamen anomalisiz olduğu hâlde anomali modelleri tetiklenir.

**Kanıt:**
```
ar_medium/ar_26081.csv → stationary + collective_anomaly + mean_shift  (PARTIAL)
ar_medium/ar_7284.csv  → stationary + mean_shift + trend_shift         (PARTIAL)
ar_long/ar_28856.csv   → stationary + point_anomaly                    (PARTIAL)
```

### 3.4 Volatility (GARCH/ARCH) → False Positive Anomali

**Mekanizma:** GARCH süreçlerinde koşullu varyans `σ²_t = α₀ + α₁ε²_{t-1} + β₁σ²_{t-1}`
kümelenir. Yüksek volatilite dönemleri ardışık büyük değerler üretir
(`collective_anomaly` sinyali); ani volatilite patlamaları tek büyük gözlem bırakır
(`point_anomaly` sinyali); volatilite rejimleri arası geçiş (`variance_shift` sinyali).
Bunların tamamı anomali değil, GARCH sürecinin doğal davranışıdır.

**Kanıt:**
- Grup 4 (volatility): %40 FULL, %59 PARTIAL
- `garch_684.csv` → volatility: 1.00, collective: 0.89, point: 0.71

### 3.5 Deterministic Trend: AR Gürültüsü Bastırma Problemi

**Mekanizma:** `linear_trend` ve `quadratic_trend` leaflerinde yüksek AR
katsayılı gürültü trend slope'unu istatistiksel olarak anlamsızlaştırır.
tsfresh'in `linear_trend` özelliği OLS kullanır; gürültü baskın olunca
β_trend ≈ 0 çıkar ve `deterministic_trend` modeli P ≈ 0.00 verir.
`argmax` base type olarak `stationary` veya `stochastic_trend` seçer.

**Kanıt:**
- Grup 2 (deterministic_trend, 720 örnek): %31 FULL, %64 NONE
- 458 adet NONE: base type tamamen yanlış seçildi
- Örnek: `ar_linear_down_trend_312.csv` → det_trend: 0.00, stationary: 1.00

**Neden kombinasyon testinde görünmüyor?** Kombinasyon klasörleri (cubic, damped, exp, linear,
quad) eğitim setinin pozitif kısmıdır; model bu leafler için deterministik sinyal
öğrendi. Sorun yalnızca grup 2'nin "saf" leaflerinde (özellikle `ar_linear_*`,
`arma_linear_*`) ortaya çıkıyor — bunlar kombinasyon eğitiminde kullanılmadı.

---

## 4. Ölçüm Sorunları: İki Test Arasındaki Farkın Tam Analizi

| Metrik       | Combi Test (11–39) | All-Data Test (1–39) |
|---|---|---|
| Toplam örnek | 410                | 4400                 |
| FULL         | 393 (%95.9)        | 2632 (%59.8)         |
| PARTIAL      | 17 (%4.1)          | 1083 (%24.6)         |
| NONE         | 0 (%0.0)           | 685 (%15.6)          |

**All-data testindeki 685 NONE'un dağılımı:**
Neredeyse tamamı grup 2 kaynaklı: 458 NONE tek başına (det_trend sorundan,
bkz. §3.5). Grup 2 dışlandığında NONE oranı %4'e düşer.

**All-data testindeki 1083 PARTIAL'ın üç kategorisi:**
1. Doğru base + ekstra false positive anomali → Grup 1, 3, 4 ağırlıklı (§2.2)
2. Doğru base + yanlış anomali (label swap) → Grup 7 mean_shift→variance_shift (§3.1)
3. Yanlış base + doğru anomali → Nadir; genellikle NONE olur

**Grup bazlı özet:**

| Grup Kategorisi | FULL% | Başarısızlık Modu |
|---|---|---|
| Saf base type (1–4) | %20–40 | FP anomali + det_trend kaçırma |
| Stationary + anomali (5–10) | %51–99 | variance_shift FP, point FP; contextual %99 |
| Kombi: det_trend + anomali (11–31) | %90–100 | Sadece mean_shift grubunda variance_shift |
| Kombi: stoch_trend + anomali (32–35) | %60–100 | stoch+mean_shift en kötü (%60) |
| Kombi: volatility + anomali (36–39) | %80–100 | point ve variance_shift tespiti zayıf |

---

## 5. Yapısal Kör Noktalar: Eğitim Setinde Hiç Görülmemiş Durumlar

Aşağıdaki durumlar için modelin davranışı **tamamen bilinmemektedir**.

| Durum | Neden Yok | Beklenen Davranış |
|---|---|---|
| base + 2 anomali aynı anda | Eğitim seti sadece base + 1 anomali | Baskın anomali yakalanır, diğeri kaçar |
| Sinusoidal + anomali | Kombinasyon klasöründe sinusoidal leaf yok | base_type belirsiz, anomali kaçabilir |
| cubic/damped + trend_shift | Sadece linear + trend_shift kombinasyonu var | trend_shift tanınmayabilir |
| det_trend veya stoch_trend + contextual_anomaly | Sadece stationary + contextual var | Anomali kaçar (base context yabancı) |
| volatility + trend_shift | Bu kombinasyon hiç oluşturulmadı | İkisi de regime change üretir, karışıklık garantili |
| 5000+ timestep seri | _long leafler 500–2000 timestep | tsfresh özellikleri normalize olabilir |
| Çok zayıf anomali genliği | Standart genlik kullanıldı | P(anomaly) < 0.5 → kaçırılır |
| Multiple mean_shift | Kombinasyon klasöründe multiple leaf yok | Tek shift yakalanır, diğerleri kaçar |

---

## 6. Çözüm Önerileri

Üç farklı çaba / kazanım seviyesinde çözüm önerilmektedir. Bunlar birbirini
dışlamaz; sırayla uygulanabilir.

---

### Çözüm A — Dinamik Eşik Kalibrasyonu (Hızlı, Sıfır Risk)

**Fikir:** `decode` fonksiyonunda, argmax sonucu seçilen base_type'a göre
anomali eşiğini dinamik olarak ayarla. Ek model eğitimi gerekmez.

**Gerekçe:** False positive sorunların büyük kısmı belirli base_type /
anomali kombinasyonlarına özgüdür (§3.1–§3.4). Bu kombinasyonlar için
eşiği yükseltmek FP oranını bastırır.

**Önerilen eşik tablosu:**

| Bağlam | Mevcut Eşik | Önerilen Eşik | Gerekçe |
|---|---|---|---|
| base = volatility → tüm anomaliler | 0.50 | 0.70 | GARCH FP bastırma |
| base = stochastic → variance_shift | 0.50 | 0.65 | Kümülatif varyans artışı |
| mean_shift tahmininde → variance_shift | 0.50 | 0.65 | Segment varyans çakışması |
| base = stationary, anomali yok beklentisi | 0.50 | 0.60 | Prior mismatch azaltma |
| Diğer tüm durumlar | 0.50 | 0.50 | Değişmez |

**Pseudocode:**
```python
def decode(probs):
    base = max({m: probs[m] for m in BASE_MODELS}, key=lambda k: probs[k])

    thresholds = {m: 0.50 for m in ANOMALY_MODELS}
    if base == "volatility":
        for m in ANOMALY_MODELS:
            thresholds[m] = 0.70
    elif base == "stochastic_trend":
        thresholds["variance_shift"] = 0.65
    if probs.get("mean_shift", 0) >= 0.50:
        thresholds["variance_shift"] = max(thresholds["variance_shift"], 0.65)

    anomalies = [m for m in ANOMALY_MODELS if probs[m] >= thresholds[m]]
    return base, anomalies
```

**Beklenen kazanım:** Grup 1, 3, 4 PARTIAL oranlarında düşüş. Grup 7'deki
variance_shift FP'lerin büyük kısmı temizlenir.
**Sınır:** Grup 2 NONE sorunu (det_trend kaçırma) çözülmez — bu özellik
eksikliğidir, eşik meselesi değil.

---

### Çözüm B — İki Aşamalı Yönlendirmeli Ensemble Mimarisi (Orta Çaba, Yüksek Kazanım)

**Fikir:** İki ensemble'ı birleştiren bir router katmanı ekle. Router "bu seri
tekli mi, kombinasyon mu?" sorusunu yanıtlar; yanıta göre ilgili ensemble'a yönlendirir.

```
                     Zaman Serisi (ham)
                            │
                   tsfresh feature extraction
                     (777 özellik, bir kez)
                            │
                 ┌──────────▼──────────┐
                 │   STAGE 1: ROUTER   │
                 │  "Tekli mi, çoklu   │
                 │   (kombinasyon) mu?"│
                 └──────┬──────┬───────┘
                        │      │
            P(combo) < θ│      │P(combo) ≥ θ
                        │      │
           ┌────────────▼──┐  ┌▼────────────────────┐
           │  STAGE 2A     │  │  STAGE 2B            │
           │  ESKİ ENSEMBLE│  │  YENİ ENSEMBLE       │
           │  (9 binary    │  │  (4 base + 6 anomali │
           │   detector)   │  │   binary model)      │
           └───────┬───────┘  └──────────┬───────────┘
                   │                     │
           "mean_shift"         "stochastic_trend +
           "deterministic_trend" collective_anomaly"
           "volatility" ...      vb.
```

#### Stage 1: Router Modeli

**Görev:** Binary sınıflandırıcı — "saf/tekli seri" mi, "base + anomali kombinasyonu" mu?

**Eğitim verisi:**
- Pozitif (combo = 1): Grup 11–39 klasörlerindeki CSV'ler
- Negatif (single = 0): Grup 1–4 klasörlerindeki CSV'ler

**Grup 5–10 nereye?**
Grup 5–10 teknik olarak kombinasyondur (stationary base + anomali). Eski
ensemble `stationary` sınıfına sahip olmadığından bu grupları Stage 2A'ya
göndermek sağlıklı değil. **Önerilen:** Grup 5–10 → pozitif (combo) → Stage 2B.
Yeni ensemble bu grupları zaten %51–99 FULL ile çözüyor.

**Model:** Aynı 777 tsfresh özelliği üzerinde XGBoost binary classifier.
Ek feature extraction gerekmez — feature vektörü zaten mevcut.

**Threshold θ kalibrasyonu:** Validation seti üzerinde precision-recall eğrisi
ile θ belirlenir. Tip II hatayı (combo → single yönlendirilmesi) minimize edecek
yönde ayarlanır (bkz. §6.2 hata analizi).

#### Stage 2A: Eski Ensemble — Tekli Seriler

Eski ensemble'ın 9 binary detector'ı tekli pattern'larda yüksek doğrulukla
çalışıyor. Ancak kritik bir eksik var:

**`stationary` sınıfı yok.**

Eski ensemble'ın 9 sınıfı: collective_anomaly, contextual_anomaly,
deterministic_trend, mean_shift, point_anomaly, stochastic_trend, trend_shift,
variance_shift, volatility. Stationary yoktur.

Stage 2A'ya yönlendirilmiş bir saf stationary seri için 9 detector'ın hiçbiri
güçlü tetiklenmez; argmax belirsiz bir sonuç döndürür.

**İki çözüm yolu:**
1. Eski ensemble'a yeni bir `stationary` binary detector ekle (yeni
   ensemble'ın stationary modeliyle aynı mimaride eğitilebilir)
2. Fallback kural: 9 detector'ın tümü 0.5 altında kalırsa → "stationary" raporla

Seçenek 2 hızlı uygulanabilir ve makul: gerçekten stationary olan seriler
hiçbir anomali/trend sinyali üretmez, dolayısıyla tüm detector'lar düşük
kalır.

#### Stage 2B: Yeni Ensemble — Kombinasyon Seriler

Mevcut `ensemble-alldata` modeli. Base type (argmax 4 model) + anomali
(eşik ≥ θ). Kombinasyon verilerinde %95.9 FULL. Bu aşamada Çözüm A'daki
dinamik eşik de uygulanabilir.

#### Router Hata Analizi

İki hata türü vardır; etkileri asimetrik:

**Tip I — False Combo (Tekli → Stage 2B):**
Stage 2B saf/tekli seriyi alır, anomali yokken anomali üretir.
→ Mevcut sistemin zaten yaptığı şey. Ek zarar marjinal.

**Tip II — False Single (Combo → Stage 2A):**
Stage 2A kombinasyonu alır, base+anomali yapısını görünce yanlış tek
etiket döndürür; anomali ya kaçar ya da yanlış sınıflandırılır.
→ Grup 11–39 için önemli regresyon.

**Sonuç:** Router θ'yu conservative tut — "combo" diyeceksen emin ol,
şüpheli ise combo de, Stage 2B'ye gönder. Tip II > Tip I zararı.

#### Özellik Uyumluluğu

Her iki ensemble da aynı tsfresh EfficientFCParameters (777 özellik) kullanır.
Ancak eğitim verilerinin istatistik dağılımı farklı olduğundan scaler'lar
farklıdır. Bu sorun değil: tek bir `tsfresh.extract` çağrısı yapılır,
ham özellik vektörü Stage 1, 2A ve 2B'ye iletilir; her model kendi scaler'ını bağımsız uygular.

#### Birleşik Pipeline Pseudocode

```python
X = tsfresh_extract(series)          # bir kez, tüm aşamalar paylaşır

p_combo = router.predict_proba(scaler_router.transform(X))[0, 1]

if p_combo >= theta:                 # Stage 2B
    X_s = scaler_new.transform(X)
    probs = {name: model.predict_proba(X_s)[0,1]
             for name, model in new_ensemble.items()}
    base, anomalies = decode_with_dynamic_threshold(probs)
else:                                # Stage 2A
    X_s = scaler_old.transform(X)
    probs = {name: model.predict_proba(X_s)[0,1]
             for name, model in old_ensemble.items()}
    label = argmax_with_stationary_fallback(probs)
```

#### Beklenen Kazanımlar

| Grup | Mevcut FULL% | Beklenen FULL% | Mekanizma |
|---|---|---|---|
| 1 (stationary) | %31 | %70–85 | Stage 2A: FP anomali yok, fallback ile stationary doğru |
| 2 (det_trend) | %31 | %50–65 | Stage 2A: eski ensemble bu leaf'leri daha iyi biliyor |
| 3 (stoch_trend) | %26 | %65–80 | Stage 2A: variance_shift FP yok |
| 4 (volatility) | %40 | %70–85 | Stage 2A: GARCH FP yok |
| 5–10 (stat+anom) | %51–99 | Değişmez | Stage 2B devam |
| 11–39 (kombi) | %95.9 | %95–97 | Stage 2B + dinamik eşik |

**Not:** Tahminler gösterge niteliğindedir; router doğruluğuna bağlıdır.

---

### Çözüm C — OOD Veriyle Yeniden Eğitim (Uzun Vadeli, Kalıcı)

**Fikir:** Mevcut ensemble'ların başarısızlığının kök nedeni, eğitim verisinin
gerçek dağılımı temsil etmemesidir. Kalıcı çözüm yeni veri üretimidir.

**Gerekli yeni eğitim verisi:**
- Saf stationary serilerden anomali modellerine **negatif** örnek ağırlığı artırılması
- `ar_linear_*`, `arma_linear_*` leaflerinden `deterministic_trend` modeline
  **pozitif** örnek ağırlığı artırılması (AR gürültülü trend sorunu, §3.5)
- `base + 2 anomali` kombinasyonları (çoklu anomali desteği)
- Kombinasyon klasörlerine sinusoidal, cubic, damped base ile trend_shift
- `contextual_anomaly` için non-stationary base kombinasyonları

**Beklenen etki:** Özellik uzayı çakışmalarının büyük kısmı eğitim seti
genişletilerek sınıflandırıcıya öğretilebilir. Threshold kalibrasyonuna
gerek azalır. OOD performansı %59.8'den %80+'a çıkabilir.

**Zorluk:** En fazla efor. Yeni sentez kodu ve eğitim döngüsü gerektirir.

---

## 7. Önerilen Uygulama Sırası

| Adım | Çözüm | Efor | Beklenen Kazanım |
|---|---|---|---|
| 1 | Dinamik eşik (Çözüm A) | 1–2 saat | Grup 1, 3, 4 PARTIAL azalır; %59.8 → %65–68 tahmini |
| 2 | Router mimarisi (Çözüm B) | 2–4 gün | Grup 1–4 dramatik düzelme; %65 → %75–80 tahmini |
| 3 | OOD yeniden eğitim (Çözüm C) | 1–2 hafta | Kalıcı genelleşme; %80+ hedef |

Her adım bir öncekinden bağımsız uygulanabilir ve her adım sonunda
`manuelalldatatest.py` ile aynı 4400 örnekli karşılaştırmalı ölçüm yapılmalıdır.

---

## 8. Özet

**Sistemin güçlü olduğu şey:**
Anomali *varlığını* tespit etmek — özellikle base process ile birlikte
sunulduğunda. Kombinasyon testinde %95.9 FULL bu yeteneği kanıtlıyor.

**Sistemin zayıf olduğu şey:**
- Anomali *yokken sessiz kalmak* (false positive bastırma)
- Zayıf trend sinyalini yüksek AR gürültüsünden ayırt etmek
- OOD genelleşme: eğitim dışı bağlamlarda prior mismatch

**İki ensemble'ın tamamlayıcılığı:**
Eski ensemble tekli pattern tespitinde, yeni ensemble kombinasyon tespitinde
güçlüdür. Router mimarisi bu tamamlayıcılığı sistematik biçimde kullanır ve
her ensemble'ı kendi güçlü olduğu bağlamda çalıştırır.
