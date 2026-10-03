"""Prépare les visuels de Tomela à partir des captures Instagram (recadrage, logo rond)."""
import os
from PIL import Image, ImageDraw

U = "/root/.claude/uploads/d253aa54-2766-50cc-8e30-b570e99679f0/"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "img")
os.makedirs(OUT, exist_ok=True)

CROPS = {
    "04473e17-image.png": ("vins.jpg", (133, 1143, 655, 1776)),
    "64f2ec30-image.png": ("coffrets.jpg", (0, 500, 1080, 1576)),
    "c8bae901-image.png": ("coffret.jpg", (40, 500, 1040, 1530)),
    "d686f25e-image.png": ("bouteilles.jpg", (0, 560, 1080, 940)),
}
for src, (dst, box) in CROPS.items():
    im = Image.open(U + src).convert("RGB").crop(box)
    im.save(os.path.join(OUT, dst), quality=94)
    print(dst, im.size)

src = Image.open(U + "57ba9bf1-image.png").convert("RGB")
print("capture", src.size)
cx, cy = 540, 1082
row = [x for x in range(1080) if min(src.getpixel((x, 760))) > 225]
col = [y for y in range(600, 1600) if min(src.getpixel((cx, y))) > 225]
x0, x1, y0, y1 = row[0], row[-1], col[0], col[-1]
print("disque", x0, x1, y0, y1)
cy = (y0 + y1) / 2
r = (y1 - y0) / 2 - 3
logo = src.crop((int(cx - r), int(cy - r), int(cx + r), int(cy + r))).resize((640, 640), Image.LANCZOS).convert("RGBA")
mask = Image.new("L", (640, 640), 0)
ImageDraw.Draw(mask).ellipse((2, 2, 638, 638), fill=255)
logo.putalpha(mask)
logo.save(os.path.join(OUT, "logo.png"))
print("logo.png")
