"""Miel calculé image par image (pas de vidéo de banque d'images) : un rideau qui coule avec des gouttes, et un ruban qui tombe et se plie.
Chaque forme est une « distance signée » (négative dedans) ; on en tire l'épaisseur, puis la lumière (reflets brillants, couleur plus foncée là où c'est épais).
Sortie : vidéos WebM VP9 avec transparence dans assets/video/. Usage : python3 miel.py [rideau|ruban]"""
import os, sys, subprocess, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, "assets", "video"); WORK = os.path.join(HERE, "work")
W, H, S = 540, 960, 2  # calcul en demi-résolution (le miel est lisse), agrandi x2 à l'encodage
FPS = 30
Y, X = np.mgrid[0:H, 0:W].astype(np.float32)
L = np.array([-0.45, -0.65, 0.62], np.float32); L /= np.linalg.norm(L)
HV = L + np.array([0, 0, 1], np.float32); HV /= np.linalg.norm(HV)

def smin(a, b, k):  # union douce : les formes fusionnent comme un liquide
    h = np.clip(0.5 + 0.5 * (b - a) / k, 0, 1)
    return b * (1 - h) + a * h - k * h * (1 - h)

def shade(d, depth=40.0):
    th = np.clip(-d, 0, None)
    h = np.sqrt(np.clip(th / depth, 0, 1)) * depth  # profil bombé
    gy, gx = np.gradient(h)
    n = np.dstack([-gx, -gy, np.ones_like(h) * 1.6]); n /= np.linalg.norm(n, axis=2, keepdims=True)
    t = np.clip(th / 22.0, 0, 1)[..., None] ** 0.8
    light = np.array([250, 170, 40], np.float32); deep = np.array([140, 52, 0], np.float32)
    col = light * (1 - t) + deep * t
    ndl = np.clip((n * L).sum(2), 0, 1)[..., None]
    col = col * (0.55 + 0.55 * ndl)
    spec = np.clip((n * HV).sum(2), 0, 1) ** 90 * 1.6 + np.clip((n * HV).sum(2), 0, 1) ** 14 * 0.22
    rim = (1 - np.abs(n[..., 2])) ** 3 * 0.35
    col = col + (spec[..., None] * np.array([255, 250, 235]) + rim[..., None] * np.array([255, 210, 120]))
    a = np.clip(0.5 - d * 0.9, 0, 1) * 0.96
    rgba = np.dstack([np.clip(col, 0, 255), a * 255]).astype(np.uint8)
    return rgba

def capsule_v(x0, y0, y1, r_top, r_mid, r_tip):  # coulée verticale qui s'affine puis fait une goutte au bout
    yc = np.clip(Y, y0, y1); u = np.clip((yc - y0) / max(y1 - y0, 1), 0, 1)
    r = r_top * (1 - u) ** 2 + r_mid * 2 * u * (1 - u) + r_mid * u * u
    r = r + (r_tip - r_mid) * np.exp(-((yc - y1) / (1.3 * r_tip)) ** 2)
    return np.sqrt((X - x0) ** 2 + (Y - yc) ** 2) - r

def ease_in(x): return x * x * (3 - 2 * x)

def rideau(t):
    edge = 70 * ease_in(min(t / 0.9, 1)) * (1 + 0.18 * np.sin(X / 37 + 1.3) + 0.1 * np.sin(X / 13 + t * 2))
    d = Y - edge  # la nappe du haut
    rng = np.random.default_rng(7)
    for i in range(11):
        x0 = 20 + i * 50 + rng.uniform(-14, 14); t0 = 0.35 + rng.uniform(0, 1.0); w = rng.uniform(9, 20)
        if t < t0: continue
        p = (t - t0); length = 22 * p + 95 * p ** 2.1 * rng.uniform(0.6, 1.25)  # lent puis plus vite (le miel est épais)
        top = 40; d = smin(d, capsule_v(x0, top, top + length, w * 1.5, w * 0.7, w * 1.15), 18)
    return d

def ruban(t):
    base = 905; grow = min(t / 5.0, 1)
    rx = 60 + 70 * grow; ry = 8 + 70 * grow  # le tas de miel qui grossit (une demi-ellipse posée)
    cy = base - ry * 0.55
    mound = (np.sqrt(((X - 270) / rx) ** 2 + ((Y - cy) / ry) ** 2) - 1) * min(rx, ry)
    mound = np.maximum(mound, Y - base)
    d = mound
    n_folds = int(t / 0.3)
    for k in range(max(0, n_folds - 7), n_folds):  # les derniers plis, bien visibles sur le dessus du tas
        yk = cy - ry * 0.8 + (n_folds - 1 - k) * 4 - 6; half = rx * (0.62 - 0.05 * (n_folds - 1 - k))
        xo = 270 + 10 * np.sin(k * 1.9); dx = np.clip(X, xo - half, xo + half)
        seg = np.sqrt((X - dx) ** 2 + (Y - yk) ** 2) - 11
        d = smin(d, seg, 14)
    top = cy - ry * 0.8 - 6; reach = min(1, t / 0.7) * top
    yc = np.clip(Y, -10, reach)
    xs = 270 + 7 * np.sin(yc / 80 - t * 2.4) * (yc / H)
    stream = np.sqrt((X - xs) ** 2 + (Y - yc) ** 2) - (11 + 1.5 * np.sin(yc / 45 + t * 3))
    return smin(d, stream, 16)

def render(name, fn, dur):
    fr = os.path.join(WORK, name); os.makedirs(fr, exist_ok=True)
    from PIL import Image
    for i in range(int(dur * FPS)):
        Image.fromarray(shade(fn(i / FPS)), "RGBA").save(os.path.join(fr, f"f{i:04d}.png"))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", os.path.join(fr, "f%04d.png"),
                    "-vf", f"scale={W * S}:{H * S}:flags=bicubic", "-c:v", "libvpx-vp9", "-pix_fmt", "yuva420p", "-b:v", "6M", "-auto-alt-ref", "0",
                    os.path.join(OUT, name + ".webm")], check=True)
    print(name, "ok")

if __name__ == "__main__":
    what = sys.argv[1:] or ["rideau", "ruban"]
    if "rideau" in what: render("rideau", rideau, 4.0)
    if "ruban" in what: render("ruban", ruban, 6.0)
