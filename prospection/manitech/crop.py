"""Visuels ManiTech, uniquement à partir de leurs publications Instagram et de leur site."""
import os
import numpy as np
import cv2
from PIL import Image, ImageDraw
from rembg import remove, new_session

U = "/root/.claude/uploads/d253aa54-2766-50cc-8e30-b570e99679f0/"
ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "assets", "img")
S_U2, S_IS = new_session("u2net"), new_session("isnet-general-use")


def src(name, box):
    return Image.open(U + name + "-image.png").convert("RGB").crop(box)


def mask(img):
    u = np.array(remove(img, session=S_U2, only_mask=True)).astype(float)
    i = np.array(remove(img, session=S_IS, only_mask=True)).astype(float)
    a = np.clip(np.maximum(u, i * 2.0), 0, 255)
    a[a < 25] = 0
    return a.astype(np.uint8)


def pieces(img, min_area, prefix, names):
    a = mask(img)
    n, lab, st, _ = cv2.connectedComponentsWithStats((a > 0).astype(np.uint8))
    comps = sorted([k for k in range(1, n) if st[k, cv2.CC_STAT_AREA] > min_area], key=lambda k: st[k, cv2.CC_STAT_LEFT])
    rgb = np.array(img)
    for k, nm in zip(comps, names):
        x, y, w, h = st[k, :4]
        al = np.where(lab == k, a, 0)
        im = Image.fromarray(np.dstack([rgb, al]), "RGBA").crop((x, y, x + w, y + h))
        im.save(os.path.join(OUT, f"{prefix}{nm}.png"))
        print(nm, im.size)
    return len(comps)


# la gamme du site (fond blanc) : miel, pot 390 g, sachet 250 g, sauce pilipili, confiture de mangues
print("site", pieces(src("0917b7a4", (40, 670, 1040, 1150)), 4000, "p_", ["miel", "pot", "sachet", "pilipili", "mangue"]))
# la gamme CityMarket : on garde la confiture d'ananas (à droite)
print("city", pieces(src("b8bd7ba2", (120, 1180, 990, 1670)), 4000, "c_", ["a", "b", "c", "d", "e", "f"]))
# badge rouge « Manitech »
b = src("4ae2df69", (426, 455, 665, 615))
al = mask(b)
Image.fromarray(np.dstack([np.array(b), al]), "RGBA").crop(Image.fromarray(al).getbbox()).save(os.path.join(OUT, "badge.png"))
# logo rond ManiTech Congo
cx, cy, r = 540, 1110, 352
lg = Image.open(U + "f109e5cc-image.png").convert("RGB").crop((cx - r, cy - r, cx + r, cy + r)).resize((640, 640), Image.LANCZOS).convert("RGBA")
m = Image.new("L", (640, 640), 0); ImageDraw.Draw(m).ellipse((3, 3, 637, 637), fill=255); lg.putalpha(m)
lg.save(os.path.join(OUT, "logo.png"))
# photos : le chef (sans le texte), le rayon de supermarché (sans le texte)
src("5786a25a", (0, 536, 1080, 1460)).save(os.path.join(OUT, "chef.jpg"), quality=92)
src("4ae2df69", (0, 374, 1080, 1370)).save(os.path.join(OUT, "rayon.jpg"), quality=92)
print("ok")

# séparation des produits (coupes verticales entre deux produits voisins)
def split(name, cuts):
    g = Image.open(os.path.join(OUT, name))
    for nm, (x0, x1) in cuts.items():
        im = g.crop((x0, 0, x1, g.height)); im = im.crop(im.getbbox()); im.save(os.path.join(OUT, nm + ".png")); print(nm, im.size)

split("gamme_site.png", {"miel": (0, 118), "pot": (118, 290), "sachet": (290, 598), "pilipili": (598, 780), "mangue": (780, 937)})
split("gamme_city.png", {"ananas": (652, 813)})
