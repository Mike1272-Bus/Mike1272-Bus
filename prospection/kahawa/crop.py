"""Prépare les visuels de Kahawa Congo Coffee à partir des captures Instagram (recadrage, logo rond)."""
import os
from PIL import Image, ImageDraw

U = "/root/.claude/uploads/d253aa54-2766-50cc-8e30-b570e99679f0/"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "img")
os.makedirs(OUT, exist_ok=True)

CROPS = {
    "5f0271da-image.png": ("verre.jpg", (0, 375, 1080, 1725)),
    "75657023-image.png": ("boissons.jpg", (0, 500, 1080, 1725)),
    "78d416f2-image.png": ("plats.jpg", (0, 550, 1080, 1775)),
    "0e57dd8a-image.png": ("frappe.jpg", (0, 733, 1080, 1955)),
    "c06b5dc3-image.png": ("gobelet.jpg", (0, 733, 1080, 1955)),
}
for src, (dst, box) in CROPS.items():
    im = Image.open(U + src).convert("RGB").crop(box)
    im.save(os.path.join(OUT, dst), quality=94)
    print(dst, im.size)

src = Image.open(U + "4219606e-image.png").convert("RGB")
cx = 540
col = [y for y in range(600, 1600) if min(src.getpixel((cx, y))) > 225]
y0, y1 = col[0], col[-1]
cy, r = (y0 + y1) / 2, (y1 - y0) / 2 - 3
print("disque", y0, y1)
logo = src.crop((int(cx - r), int(cy - r), int(cx + r), int(cy + r))).resize((640, 640), Image.LANCZOS).convert("RGBA")
mask = Image.new("L", (640, 640), 0)
ImageDraw.Draw(mask).ellipse((2, 2, 638, 638), fill=255)
logo.putalpha(mask)
logo.save(os.path.join(OUT, "logo.png"))
print("logo.png")
