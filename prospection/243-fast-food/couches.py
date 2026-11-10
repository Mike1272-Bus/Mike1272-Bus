"""Couches du burger « Classique » (coupes légèrement ondulées) et logo détouré en disque."""
import os, numpy as np
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__)); IMG = os.path.join(HERE, "assets", "img")
b = np.array(Image.open(os.path.join(IMG, "classique.png")).convert("RGBA")); h, w = b.shape[:2]
b[:265, :88, 3] = 0; b[:, 668:, 3] = 0; b[:30, 470:, 3] = 0; b[:58, :200, 3] = 0; b[:110, :130, 3] = 0  # bouts de fond du menu
Y, X = np.mgrid[0:h, 0:w]; wave = lambda base, ph: base + 5 * np.sin(X / 31.0 + ph)
bands = [("l_pain", None, wave(205, 0)), ("l_tomate", wave(205, 0), wave(252, 1.1)), ("l_viande", wave(252, 1.1), wave(402, 2.3)),
         ("l_tomate2", wave(402, 2.3), wave(468, .5)), ("l_frites", wave(468, .5), None)]
for name, top, bot in bands:  # toutes les couches gardent la même taille : elles se superposent au pixel près
    m = np.ones((h, w), bool)
    if top is not None: m &= Y >= top
    if bot is not None: m &= Y < bot
    o = b.copy(); o[..., 3] = np.where(m, b[..., 3], 0); Image.fromarray(o).save(os.path.join(IMG, name + ".png")); print(name)
# logo : le disque noir de leur photo de profil
s = Image.open(os.path.join(HERE, "work", "src", "s1.jpg")).convert("RGB"); cx, cy, r = 540, 1110, 350  # repérés sur la capture
lg = s.crop((int(cx - r), int(cy - r), int(cx + r), int(cy + r))).convert("RGBA"); S = lg.width * 4
m = Image.new("L", (S, S), 0); ImageDraw.Draw(m).ellipse((0, 0, S - 1, S - 1), fill=255); lg.putalpha(m.resize(lg.size, Image.LANCZOS))
lg.save(os.path.join(IMG, "logo.png")); print("logo", lg.size, cx, cy)
