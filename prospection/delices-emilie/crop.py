"""Prépare les visuels des Délices d'Émilie à partir de leurs captures Instagram uniquement."""
import os
import numpy as np
from PIL import Image, ImageDraw
from rembg import remove, new_session

U = "/root/.claude/uploads/d253aa54-2766-50cc-8e30-b570e99679f0/"
ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "assets", "img")
os.makedirs(OUT, exist_ok=True)
S_U2, S_IS = new_session("u2net"), new_session("isnet-general-use")


def cutout(img, clear=(), solid=True):
    i = np.array(remove(img, session=S_IS, only_mask=True)).astype(float)
    if solid:
        u = np.array(remove(img, session=S_U2, only_mask=True)).astype(float)
        a = np.clip(np.maximum(u, i * 2.0), 0, 255)
    else:
        a = np.clip((i - 40) * 2.2, 0, 255)
    a[a < 20] = 0
    for x0, y0, x1, y1 in clear:
        a[y0:y1, x0:x1] = 0
    im = Image.fromarray(np.dstack([np.array(img), a.astype(np.uint8)]), "RGBA")
    return im.crop(im.getbbox())


def save(im, name):
    im.save(os.path.join(OUT, name))
    print(name, im.size)


def src(name, box):
    return Image.open(U + name + "-image.png").convert("RGB").crop(box)


# logo : le disque rose de la photo de profil
logo_src = Image.open(U + "1a44bbcc-image.png").convert("RGB")
cx, cy, r = 540, 1082, 352
logo = logo_src.crop((int(cx - r), int(cy - r), int(cx + r), int(cy + r))).resize((640, 640), Image.LANCZOS).convert("RGBA")
mask = Image.new("L", (640, 640), 0)
ImageDraw.Draw(mask).ellipse((2, 2, 638, 638), fill=255)
logo.putalpha(mask)
save(logo, "logo.png")

# butterfly cake (on efface la pastille « 1/3 » d'Instagram)
save(cutout(src("f3f432f1", (0, 420, 1080, 1856)), clear=[(925, 200, 1080, 300)]), "cake.png")
# la cuisine : bol, génoise, crème, plateau tournant
save(cutout(src("0fbcbb78", (0, 685, 1080, 1402)), solid=False), "cuisine.png")
# gâteau au chocolat
save(cutout(src("b0cba215", (0, 592, 1080, 1730)), clear=[(925, 30, 1080, 120)]), "choco.png")
