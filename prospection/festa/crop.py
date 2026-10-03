"""Prépare les visuels de Festa à partir des captures Instagram (bouteilles, affiche, logo rond)."""
import os
from PIL import Image, ImageDraw

U = "/root/.claude/uploads/d253aa54-2766-50cc-8e30-b570e99679f0/"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "img")
os.makedirs(OUT, exist_ok=True)

CROPS = {
    "9f125950-image.png": ("orange.jpg", (150, 622, 676, 1682)),
    "d8c1bc31-image.png": ("maracuja.jpg", (310, 955, 738, 1690)),
    "cca07d46-image.png": ("grenadine.jpg", (377, 744, 722, 1565)),
    "cc0ffe8e-image.png": ("cola.jpg", (380, 777, 722, 1376)),
    "c4ccd815-image.png": ("fun.jpg", (0, 378, 1080, 1456)),
}
for src, (dst, box) in CROPS.items():
    im = Image.open(U + src).convert("RGB").crop(box)
    im.save(os.path.join(OUT, dst), quality=94)
    print(dst, im.size)

src = Image.open(U + "71b43ee7-image.png").convert("RGB")
cx, cy, r = 540, 1082, 352
logo = src.crop((cx - r, cy - r, cx + r, cy + r)).resize((640, 640), Image.LANCZOS).convert("RGBA")
mask = Image.new("L", (640, 640), 0)
ImageDraw.Draw(mask).ellipse((3, 3, 637, 637), fill=255)
logo.putalpha(mask)
logo.save(os.path.join(OUT, "logo.png"))
print("logo.png")
