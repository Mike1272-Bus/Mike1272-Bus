"""Bruitages gourmands fabriqués à la main (bruit filtré) : croustillant, croquer, grésillement, chute d'une couche."""
import os, numpy as np
from scipy.signal import butter, sosfilt
from scipy.io import wavfile
SR = 44100; OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "sfx"); rng = np.random.default_rng(243)
bp = lambda x, lo, hi: sosfilt(butter(4, [lo, hi], "bandpass", fs=SR, output="sos"), x)
hp = lambda x, f: sosfilt(butter(4, f, "highpass", fs=SR, output="sos"), x)
lp = lambda x, f: sosfilt(butter(4, f, "lowpass", fs=SR, output="sos"), x)
def save(name, x):
    x = x / (np.abs(x).max() + 1e-9) * 0.9; st = np.stack([x, x], 1)
    wavfile.write(os.path.join(OUT, name + ".wav"), SR, (st * 32767).astype(np.int16)); print(name, len(x) / SR)
def grains(dur, n, t_end, lo=1400, hi=7500, decay=0.006):
    out = np.zeros(int(dur * SR))
    for _ in range(n):  # petits éclats de croûte, plus denses au début
        t = t_end * rng.random() ** 1.8; L = int(rng.uniform(0.004, 0.02) * SR); i = int(t * SR)
        g = rng.standard_normal(L) * np.exp(-np.arange(L) / (decay * SR)) * rng.uniform(0.3, 1.0)
        out[i:i + L] += g[:len(out) - i]
    return bp(out, lo, hi)
def thump(dur, f=70, d=0.06, amp=1.0):
    t = np.arange(int(dur * SR)) / SR; return amp * np.sin(2 * np.pi * f * t * (1 - 0.4 * t / dur)) * np.exp(-t / d)
# croustillant : une poignée d'éclats secs
save("croustillant", grains(0.5, 60, 0.32) + 0.15 * thump(0.5, 90, 0.03))
# croquer : coup de dent (grave) + croûte qui craque, en deux temps
c = np.zeros(int(0.7 * SR)); c += 0.6 * thump(0.7, 60, 0.05); c += grains(0.7, 45, 0.2)
c2 = grains(0.7, 30, 0.18) * 0.7; k = int(0.24 * SR); c[k:] += c2[:len(c) - k]; save("croquer", c)
# grésillement : la viande sur la plaque (souffle aigu qui ondule + petits crépitements)
D = 2.6; n = int(D * SR); t = np.arange(n) / SR
s = hp(rng.standard_normal(n), 3500) * (0.55 + 0.45 * lp(rng.standard_normal(n), 6) * 8).clip(0.2, 1.2) * 0.35
pops = np.zeros(n)
for _ in range(140):
    i = rng.integers(0, n - 400); L = rng.integers(40, 300); pops[i:i + L] += rng.standard_normal(L) * np.exp(-np.arange(L) / 60) * rng.uniform(0.3, 1)
s += hp(pops, 2000) * 0.9; env = np.minimum(1, t / 0.15) * np.minimum(1, (D - t) / 0.5); save("gresillement", s * env)
# chute d'une couche sur le burger : choc doux et mat
save("couche", thump(0.4, 110, 0.05) + 0.25 * bp(rng.standard_normal(int(0.4 * SR)) * np.exp(-np.arange(int(0.4 * SR)) / (0.02 * SR)), 300, 2500))
