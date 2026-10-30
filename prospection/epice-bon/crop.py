"""Prépare les visuels d'Epicé Bon à partir des captures Instagram (recadrage, logo rond)."""
import os
from PIL import Image, ImageDraw

U = "/root/.claude/uploads/d253aa54-2766-50cc-8e30-b570e99679f0/"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "img")
os.makedirs(OUT, exist_ok=True)

CROPS = {
    "200425c7-image.png": ("pots.jpg", (0, 415, 1080, 1850)),
    "7203d523-image.png": ("gamme.jpg", (0, 1395, 1080, 1680)),
    "68b8f4d2-image.png": ("poisson.jpg", (0, 495, 1080, 1490)),
    "a25461ff-image.png": ("poulet.jpg", (0, 495, 1080, 1490)),
    "bdd097ce-image.png": ("legumes.jpg", (200, 993, 888, 1504)),
    "6e4a27e8-image.png": ("plats.jpg", (0, 490, 1080, 1468)),
}
for src, (dst, box) in CROPS.items():
    im = Image.open(U + src).convert("RGB").crop(box)
    im.save(os.path.join(OUT, dst), quality=94)
    print(dst, im.size)

# logo : on cherche le disque blanc sur la ligne et la colonne du centre
src = Image.open(U + "a1da3f43-image.png").convert("RGB")
cx, cy = 540, 1082
row = [x for x in range(1080) if min(src.getpixel((x, cy))) > 225]
col = [y for y in range(700, 1500) if min(src.getpixel((cx, y))) > 225]
x0, x1, y0, y1 = row[0], row[-1], col[0], col[-1]
print("disque", x0, x1, y0, y1)
cx, cy, r = (x0 + x1) / 2, (y0 + y1) / 2, min(x1 - x0, y1 - y0) / 2 - 3
logo = src.crop((int(cx - r), int(cy - r), int(cx + r), int(cy + r))).resize((640, 640), Image.LANCZOS).convert("RGBA")
mask = Image.new("L", (640, 640), 0)
ImageDraw.Draw(mask).ellipse((2, 2, 638, 638), fill=255)
logo.putalpha(mask)
logo.save(os.path.join(OUT, "logo.png"))
print("logo.png")
