# FLYbrs — Custom Domain Bağlama Rehberi

Şu an site: `https://erete22.github.io/flybrs/` (GitHub URL'i)
Hedef: `https://flybrs.com` veya `.co` veya `.com.tr`

## Adım 1 — Domain satın al (5-10 dk)

| Sağlayıcı | Fiyat (yıllık) | Avantaj |
|-----------|----------------|---------|
| **Cloudflare** | ~$10 (.com), ~$8 (.co) | Marketplace fiyatına satar, gizli ücret yok, otomatik HTTPS |
| **Namecheap** | ~$11 (.com) | TR'den ödenebilir, kolay arayüz |
| **isimtescil.net** | ~150-200₺ (.com.tr) | TR domain için tek seçenek |
| **Hostinger** | ~$1 ilk yıl, sonra $13 | Promosyon ucuz |

**Öneri:** `.com` (Cloudflare) — global, ucuz, otomatik DNS.

## Adım 2 — DNS ayarları (5 dk)

Domain panelinde "DNS Records" bölümüne git, şu 5 kaydı ekle:

```
Tip    İsim    Değer                       TTL
A      @       185.199.108.153             Auto
A      @       185.199.109.153             Auto
A      @       185.199.110.153             Auto
A      @       185.199.111.153             Auto
CNAME  www     erete22.github.io           Auto
```

Bu 4 IP GitHub Pages'in resmi adresleri ([docs](https://docs.github.com/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)).

## Adım 3 — GitHub'a domain bildir (1 dk)

```bash
cd C:/tmp/flybrs_site
echo "flybrs.com" > CNAME
git add CNAME
git commit -m "feat: custom domain"
git push
```

Veya GitHub web UI'da: `repo > Settings > Pages > Custom domain` → `flybrs.com` yaz, kaydet.

## Adım 4 — HTTPS aktive (otomatik, 5-30 dk)

GitHub Let's Encrypt sertifikasını otomatik alır. **Pages ayarlarında "Enforce HTTPS"** check kutusunu işaretle.

## Adım 5 — Doğrulama

```bash
curl -sI https://flybrs.com | head -3
# HTTP/2 200
# Server: GitHub.com
```

DNS yayılması 5 dk - 24 saat sürer. Cloudflare'de genelde 5-10 dk.

## Adım 6 — Landing'deki URL'leri güncelle

`index.html` içinde:
- `<link rel="canonical" href="...">` → yeni domain
- Open Graph `og:url` → yeni domain
- og:image URL → yeni domain

Sonra `git push` → Pages otomatik yayınlar.

---

## Hızlı karar matrisi

| Hangi durumda | Ne al |
|---------------|-------|
| Global hedef, Türkiye ağırlıklı | `flybrs.com` (Cloudflare $10) |
| Sadece Türkiye | `flybrs.com.tr` (isimtescil ~200₺) |
| Bütçe sıfır | Bu rehberi unutma, sonra al; `erete22.github.io/flybrs` ile devam |
| Logo tipinde marka | `flybrs.co` (Cloudflare $8) — daha kısa |

**Öneri sırası:** flybrs.com → flybrs.co → flybrs.com.tr (en son tercih, çünkü TR-specific)

## Maliyet tablosu (1 yıl)

| Domain | İlk yıl | Yıllık yenileme |
|--------|---------|-----------------|
| flybrs.com (Cloudflare) | ~$10 ≈ 350₺ | ~$10 |
| flybrs.co (Cloudflare) | ~$8 ≈ 280₺ | ~$8 |
| flybrs.com.tr | ~150₺ | ~150₺ |

İlk yatırım: **350₺ civarı**. FLYbrs'in ilk Premium üyesi (499₺) bunu çıkarır + kâr.
