"""Prépare les visuels de La Ruche du Terroir à partir des captures Instagram (recadrage, logo rond)."""
import os
from PIL import Image, ImageDraw

U = "/root/.claude/uploads/d253aa54-2766-50cc-8e30-b570e99679f0/"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "img")
os.makedirs(OUT, exist_ok=True)

CROPS = {
    "5f5b78c2-image.png": ("cannelle.jpg", (300, 875, 940, 1490)),
    "5493bbe6-image.png": ("gamme.jpg", (0, 1290, 1080, 1650)),
    "58fc664e-image.png": ("panier.jpg", (0, 750, 1080, 1262)),
    "b8c3846c-image.png": ("moringa.jpg", (200, 1040, 880, 1530)),
}
for src, (dst, box) in CROPS.items():
    im = Image.open(U + src).convert("RGB").crop(box)
    im.save(os.path.join(OUT, dst), quality=94)
    print(dst, im.size)

src = Image.open(U + "26e76acc-image.png").convert("RGB")
print("capture", src.size)
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
