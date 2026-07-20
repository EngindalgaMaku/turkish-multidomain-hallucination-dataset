# Dört Sınıflı Etiketleme Kılavuzu

## Temel ilke

Etiket, esas olarak `context` ile `claim` arasındaki kanıt ilişkisine göre verilir. `question`, claim'in referanslarını ve bilgi ihtiyacını anlamaya yardımcı olur; tek başına kanıt değildir.

## Karar sırası

1. Claim'i atomik önermelere ayır.
2. Bütün atomlar bağlamca destekleniyorsa `supported`.
3. En az bir atom destekleniyor ve en az bir atom desteklenmiyor ya da çelişiyorsa `partially_supported`.
4. Desteklenen atom yoksa ve bağlam merkezi iddiayla açıkça uyuşmuyorsa `contradicted`.
5. Destek veya açık çelişki kurulamıyorsa `unverifiable`.

## Etiket tanımları

### supported
Bütün atomik önermeler bağlam tarafından açıkça desteklenir. Önemli bir ek bilgi yoktur.

### partially_supported
Claim birden fazla atom içerir. En az biri desteklenir; en az biri bağlamda bulunmaz veya bağlamla çelişir.

### contradicted
Bağlam, claim'in merkezi önermesine karşı uyumsuz bir değer, yön, zaman, taraf, koşul veya ilişki sunar. Yalnız dış dünya bilgisiyle yanlış olduğu bilinen claim'ler bu sınıfa verilmez.

### unverifiable
Bağlam, claim'i doğrulamak veya çürütmek için yeterli kanıt sunmaz. Eski `unsupported` ve `insufficient_information` alt türleri bu ana sınıfta birleşir.

## Sık hatalar

- Soruyu kanıt gibi kullanmak.
- Aynı konunun geçmesini destek saymak.
- Dış bilgiyle çelişki kurmak.
- Birleşik claim'deki desteklenen atomu gözden kaçırmak.
- Açık uyumsuz değer varken `unverifiable` vermek.
