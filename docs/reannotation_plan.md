# Yeniden Anotasyon Planı

## Öncelik

1. Test-600: yüzde 100 bağımsız çift anotasyon.
2. Uyuşmazlıklar: alan uzmanı adjudication.
3. Cohen's kappa: dört ana sınıf üzerinden.
4. Train-6150: sınıf ve alan bazında tabakalı kalite denetimi; mümkünse tam çift anotasyon.
5. Challenge-150: ayrı tanısal set olarak korunur.

## Körleme

Annotatörlere eski etiket, model tahmini, güven puanı ve hata raporu gösterilmemelidir. Yalnız `context`, `question` ve `claim` sunulmalıdır.

## Kayıt alanları

- `annotator_label`
- `confidence`
- `needs_expert_review`
- `notes`

Ana etiket dört sınıftan biri olmalıdır. `legacy_subtype` yalnız geçmiş izleme içindir.
