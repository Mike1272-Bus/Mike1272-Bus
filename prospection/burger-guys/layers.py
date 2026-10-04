"""Couches du burger (coupes légèrement ondulées) et nettoyage des bords des accompagnements."""
import os
import numpy as np
import cv2
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(ROOT, "assets", "img")


def load(name):
    return np.array(Image.open(os.path.join(IMG, name)).convert("RGBA"))


def save(arr, name):
    Image.fromarray(arr, "RGBA").save(os.path.join(IMG, name))


# 1) le burger en 5 couches de même taille, qui se superposent au pixel près
b = load("burger.png")
h, w = b.shape[:2]
Y, X = np.mgrid[0:h, 0:w]
wave = lambda base, ph: base + 7 * np.sin(X / 37.0 + ph)
bands = [("l_pain_haut", None, wave(228, 0)), ("l_bacon", wave(228, 0), wave(372, 1.3)),
         ("l_steak", wave(372, 1.3), wave(522, 2.1)), ("l_salade", wave(522, 2.1), wave(592, .4)),
         ("l_pain_bas", wave(592, .4), None)]
for name, top, bot in bands:
    m = np.ones((h, w), bool)
    if top is not None: m &= Y >= top
    if bot is not None: m &= Y < bot
    out = b.copy(); out[..., 3] = np.where(m, b[..., 3], 0); save(out, name + ".png"); print(name)


# 2) frites et onion rings : bords nets (on durcit le masque, on garde la couleur dorée)
def harden(name, gold):
    a = load(name)
    al = a[..., 3].astype(np.uint8)
    r, g, bl = [a[..., i].astype(int) for i in range(3)]
    keep = (al > 90)
    if gold:
        keep &= (r > 120) & (r > bl + 40) & (g > 60)
    keep = cv2.morphologyEx(keep.astype(np.uint8), cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(keep)
    big = [k for k in range(1, n) if st[k, cv2.CC_STAT_AREA] > 1500]
    keep = np.isin(lab, big).astype(np.float32)
    keep = cv2.GaussianBlur(keep, (0, 0), 1.2)
    a[..., 3] = (keep * 255).astype(np.uint8)
    im = Image.fromarray(a, "RGBA"); im = im.crop(im.getbbox()); im.save(os.path.join(IMG, name)); print(name, im.size)


harden("frites.png", True)
harden("onion_rings.png", True)
