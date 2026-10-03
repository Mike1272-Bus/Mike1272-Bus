"""Prépare les visuels de La Kinoise à partir des captures Instagram (recadrage, logo rond)."""
import os
from PIL import Image, ImageDraw

U = "/root/.claude/uploads/d253aa54-2766-50cc-8e30-b570e99679f0/"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "img")
os.makedirs(OUT, exist_ok=True)

CROPS = {
    "074a2412-image.png": ("rayon.jpg", (0, 376, 1080, 1722)),
    "47676b6d-image.png": ("arabica.jpg", (0, 403, 1080, 1748)),
    "9dca55f6-image.png": ("mains.jpg", (0, 726, 1080, 1360)),
    "e21c87c3-image.png": ("stand.jpg", (0, 741, 1080, 1344)),
}
for src, (dst, box) in CROPS.items():
    im = Image.open(U + src).convert("RGB").crop(box)
    im.save(os.path.join(OUT, dst), quality=94)
    print(dst, im.size)

logo = Image.open(U + "d7279a99-image.png").convert("RGB").crop((184, 754, 896, 1466)).resize((640, 640), Image.LANCZOS).convert("RGBA")
mask = Image.new("L", (640, 640), 0)
ImageDraw.Draw(mask).ellipse((8, 8, 632, 632), fill=255)
logo.putalpha(mask)
logo.save(os.path.join(OUT, "logo.png"))
print("logo.png")
