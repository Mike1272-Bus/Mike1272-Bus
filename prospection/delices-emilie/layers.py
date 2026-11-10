"""Découpe les gâteaux détourés en couches de même taille, qui se superposent au pixel près."""
import os
import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(ROOT, "assets", "img")


def load(name):
    return np.array(Image.open(os.path.join(IMG, name)).convert("RGBA"))


def keep(arr, mask, name):
    out = arr.copy()
    out[..., 3] = np.where(mask, arr[..., 3], 0)
    Image.fromarray(out, "RGBA").save(os.path.join(IMG, name))
    print(name, int(mask.sum()))


def grid(arr):
    h, w = arr.shape[:2]
    return np.mgrid[0:h, 0:w]


# cuisine : on garde la main jusqu'au poignet, puis plateau + 4 couches
k = load("cuisine.png")
Y, X = grid(k)
a = k[..., 3].astype(float)
a[(X > 555) & (Y < 300)] = 0
fade = np.clip((Y - 185) / 45.0, 0, 1)
a = np.where((X > 470) & (Y < 230), a * fade, a)
k[..., 3] = a.astype(np.uint8)
col = (X >= 76) & (X <= 370) & (Y < 375)
keep(k, ~col, "k_plateau.png")
keep(k, col & (Y >= 328), "k_genoise1.png")
keep(k, col & (Y >= 290) & (Y < 328), "k_creme1.png")
keep(k, col & (Y >= 247) & (Y < 290), "k_genoise2.png")
keep(k, col & (Y < 247), "k_creme2.png")

# chocolat : le corps, puis les tablettes en 3 groupes
c = load("choco.png")
Y, X = grid(c)
top = Y < 160
keep(c, ~top, "c_corps.png")
for i, (x0, x1) in enumerate([(0, 330), (330, 640), (640, 10000)]):
    keep(c, top & (X >= x0) & (X < x1), f"c_tab{i}.png")

# butterfly cake : socle, étages, dessus, puis les papillons qui volent
b = load("cake.png")
Y, X = grid(b)
b[..., 3] = np.where((X > 850) & (Y < 222), 0, b[..., 3])
pa = (X >= 565) & (X < 785) & (Y < 200)
pb = (X >= 90) & (X < 360) & (Y < 200)
keep(b, Y >= 960, "b_socle.png")
keep(b, (Y >= 830) & (Y < 960), "b_bleu.png")
keep(b, (Y >= 640) & (Y < 830), "b_rose.png")
keep(b, (Y >= 400) & (Y < 640), "b_lilas.png")
keep(b, (Y >= 290) & (Y < 400), "b_dessus.png")
keep(b, (Y < 290) & ~pa & ~pb, "b_deco.png")
keep(b, pa, "b_papA.png")
keep(b, pb, "b_papB.png")
Image.fromarray(b, "RGBA").save(os.path.join(IMG, "cake.png"))
