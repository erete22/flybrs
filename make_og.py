"""FLYbrs OG image - 1200x630 sosyal medya preview."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path

OUT = Path(__file__).parent / "og.png"

W, H = 1200, 630
GOLD = (201, 169, 97)
GOLD_LIGHT = (232, 201, 122)
CREAM = (245, 230, 200)
DARK = (10, 10, 10)
DARK_2 = (22, 20, 15)

# Vertical gradient background
img = Image.new("RGB", (W, H), DARK)
d = ImageDraw.Draw(img)
for y in range(H):
    t = y / H
    r = int(DARK[0] * (1 - t) + DARK_2[0] * t)
    g = int(DARK[1] * (1 - t) + DARK_2[1] * t)
    b = int(DARK[2] * (1 - t) + DARK_2[2] * t)
    d.line([(0, y), (W, y)], fill=(r, g, b))

# Glow lekeleri (radial)
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
gd.ellipse([200, -100, 600, 300], fill=(201, 169, 97, 25))
gd.ellipse([700, 300, 1300, 800], fill=(201, 169, 97, 18))
glow = glow.filter(ImageFilter.GaussianBlur(radius=80))
img.paste(glow, (0, 0), glow)

f_b = lambda s: ImageFont.truetype("C:/Windows/Fonts/georgiab.ttf", s)
f_i = lambda s: ImageFont.truetype("C:/Windows/Fonts/georgiai.ttf", s)
f_s = lambda s: ImageFont.truetype("C:/Windows/Fonts/arial.ttf", s)

d = ImageDraw.Draw(img)

# Üst bar — yıldız ikonu + marka
d.text((80, 60), "⭐", font=f_b(60), fill=GOLD)
d.text((160, 75), "FLYbrs", font=f_b(54), fill=GOLD_LIGHT)

# Sağda canlı status
d.ellipse([W - 200, 80, W - 184, 96], fill=(80, 220, 100))
d.text((W - 168, 78), "21 AJAN CANLI", font=f_s(20), fill=GOLD_LIGHT)

# Ana başlık (büyük, serif italic)
d.text((80, 220), "Senin yerine çalışan", font=f_i(72), fill=CREAM)
d.text((80, 310), "bir AI ordusu.", font=f_b(82), fill=GOLD_LIGHT)

# Alt açıklama
d.text((80, 430), "Kripto sinyal · İçerik üretimi · Otomatik raporlar", font=f_s(28), fill=(200, 190, 170))
d.text((80, 470), "Telegram'dan komut → sonuç telefonuna düşer", font=f_s(28), fill=(200, 190, 170))

# Alt CTA bar
d.rectangle([0, 560, W, 562], fill=GOLD)
d.text((80, 580), "@flybrs_bot · 30 saniyede ücretsiz başla", font=f_b(28), fill=GOLD_LIGHT)
d.text((W - 280, 580), "OTONOM · TÜRKÇE · 7/24", font=f_s(22), fill=GOLD)

img.save(OUT, "PNG", quality=92, optimize=True)
print(f"OK: {OUT} ({OUT.stat().st_size // 1024} KB, {W}x{H})")
