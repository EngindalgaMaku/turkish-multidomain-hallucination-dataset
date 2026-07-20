# Turkish Multidomain Hallucination Dataset — Canonical v17

Türkçe bağlam–soru–iddia üçlüleri üzerinde kaynak-temelli doğrulama için hazırlanmış dört sınıflı çok alanlı veri setidir. Aktif sürüm yalnızca tıp, finans ve hukuk alanlarındaki kanonik eğitim, geliştirme ve test dosyalarını içerir.

## Aktif dosyalar

| Bölüm | Dosya | Örnek |
|---|---|---:|
| Train | `data/train_6150.jsonl` | 6.150 |
| Dev | `data/dev_600.jsonl` | 600 |
| Test | `data/test_600.jsonl` | 600 |
| Challenge | `data/challenge/fresh_150_v2_4class.jsonl` | 150 |

## Etiketler

- `supported`: İddiadaki bütün atomik önermeler bağlam tarafından desteklenir.
- `partially_supported`: En az bir atom desteklenir; en az bir atom desteklenmez veya çelişir.
- `contradicted`: Desteklenen merkezi önerme yoktur ve bağlam iddianın merkezi önermesiyle açıkça uyuşmaz.
- `unverifiable`: Bağlam iddiayı desteklemek veya çürütmek için yeterli kanıt sunmaz.

Eski `unsupported` ve `insufficient_information` etiketleri ana görevde `unverifiable` altında birleştirilmiştir. Köken bilgisi gerektiğinde `legacy_subtype` alanında tutulur ve model hedefi olarak kullanılmaz.

## Veri dağılımı

| Bölüm | supported | partially_supported | contradicted | unverifiable | Toplam |
|---|---:|---:|---:|---:|---:|
| Train | 1.230 | 1.230 | 1.230 | 2.460 | 6.150 |
| Dev | 120 | 120 | 120 | 240 | 600 |
| Test | 120 | 120 | 122 | 238 | 600 |

## Değerlendirme ilkesi

Dev seti model seçimi ve erken durdurma için kullanılabilir. Test seti yalnızca nihai değerlendirme içindir. Challenge seti eğitim, eşik ayarı veya prompt seçimi için kullanılmamalıdır.

## Durum

Bu paket yapısal olarak temizlenmiş kanonik v17 çalışma kopyasıdır. Dört sınıfa dönüşüm deterministik etiket eşlemesiyle yapılmıştır. İnsan çift anotasyonu ve uzman adjudication tamamlandığında sürüm numarası güncellenmelidir.
