"""Couches du burger Fatburger (coupes ondulées) et les 4 milkshakes séparés."""
import os
import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(ROOT, "assets", "img")


def load(name):
    return np.array(Image.open(os.path.join(IMG, name)).convert("RGBA"))


def keep(arr, m, name, size=None):
    out = arr.copy(); out[..., 3] = np.where(m, arr[..., 3], 0)
    out[out[..., 3] == 0] = 0  # pixels transparents vidés : fichiers bien plus légers
    im = Image.fromarray(out, "RGBA")
    if size: im = im.resize(size, Image.LANCZOS)
    im.save(os.path.join(IMG, name), optimize=True); print(name, int(m.sum()))


b = load("burger.png")
h, w = b.shape[:2]
Y, X = np.mgrid[0:h, 0:w]
wave = lambda base, ph: base + 8 * np.sin(X / 41.0 + ph)
cuts = [wave(215, 0), wave(455, 1.1), wave(578, 2.0), wave(680, 0.6), wave(775, 1.7), wave(866, 2.6)]
names = ["l_pain_haut", "l_salade", "l_tomate", "l_steak1", "l_steak2", "l_steak3", "l_pain_bas"]
for i, n in enumerate(names):
    m = np.ones((h, w), bool)
    if i > 0: m &= Y >= cuts[i - 1]
    if i < len(cuts): m &= Y < cuts[i]
    keep(b, m, n + ".png", (900, 846))

s = load("shakes.png")
h, w = s.shape[:2]
Y, X = np.mgrid[0:h, 0:w]
keep(b, np.ones(b.shape[:2], bool), "burger.png", (900, 846))
for i, (x0, x1) in enumerate([(0, 122), (122, 368), (368, 600), (600, 10000)]):
    keep(s, (X >= x0) & (X < x1), f"shake{i}.png")
keep(s, np.ones(s.shape[:2], bool), "shakes.png")
