"""Elembo : les 3 bouteilles (image envoyée par Mike, déjà détourée) séparées une par une, ombres retirées.
Usage : python3 decoupe.py"""
import os, numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, "assets", "img")
im = Image.open(os.path.join(HERE, "work", "src", "bouteilles.png")).convert("RGBA"); a = np.array(im)
lum = a[..., :3].mean(2); Y = np.arange(a.shape[0])[:, None]
a[..., 3] = np.where((Y > 735) & (lum < 60), 0, a[..., 3])  # l'ombre noire sous les bouteilles
clean = Image.fromarray(a); clean.save(os.path.join(OUT, "trio.png"))
for name, (x0, x1) in {"ananas": (140, 362), "ananas_orange": (362, 592), "orange": (592, 830)}.items():
    b = a.copy(); b[:, :x0, 3] = 0; b[:, x1:, 3] = 0; p = Image.fromarray(b); p = p.crop(p.getbbox()); p.save(os.path.join(OUT, name + ".png")); print(name, p.size)
