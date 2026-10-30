"""Améliore les plats du menu +243 (captures des stories) : recadrage, agrandissement x4 Real-ESRGAN, détourage, pastilles de prix retirées.
Usage : python3 ameliorer.py <RealESRGAN_x4plus.pth>"""
import os, sys, torch, numpy as np, cv2
from PIL import Image, ImageEnhance
from spandrel import ModelLoader
from rembg import remove, new_session
HERE = os.path.dirname(os.path.abspath(__file__)); SRC = os.path.join(HERE, "work", "src"); UP = os.path.join(HERE, "work", "up"); OUT = os.path.join(HERE, "assets", "img")
model = ModelLoader().load_from_file(sys.argv[1]).eval(); torch.set_num_threads(os.cpu_count()); sess = new_session("isnet-general-use")
OX, OY = 60, 780  # décalage du recadrage de repérage
CROPS = {  # nom : (capture, boîte x0, y0, x1, y1 dans le repérage)
    "classique": ("s7.jpg", (640, 176, 752, 272)), "b243": ("s7.jpg", (636, 48, 746, 140)),
    "crispy": ("s7.jpg", (318, 48, 426, 140)), 
    "pepperon": ("s7.jpg", (12, 322, 122, 416)), "ailes": ("s6.jpg", (12, 50, 124, 148)),
    "fingers": ("s6.jpg", (12, 178, 122, 272)), "family": ("s6.jpg", (10, 444, 120, 534)),
    "shawarma": ("s6.jpg", (312, 34, 418, 116)), 
    "wings": ("s5.jpg", (634, 48, 746, 142)),
    "frite": ("s5.jpg", (12, 444, 118, 536)), 
}
def upscale(im):
    t = torch.from_numpy(np.array(im).astype(np.float32) / 255).permute(2, 0, 1)[None]
    with torch.no_grad(): o = model(t)
    return Image.fromarray((o[0].clamp(0, 1).permute(1, 2, 0).numpy() * 255).round().astype(np.uint8))
def badge_mask(a):  # pastilles de prix : disques rouges vifs (on prend l'enveloppe, texte blanc compris)
    r, g, b = [a[..., i].astype(int) for i in range(3)]
    red = ((r > 170) & (g < 90) & (b < 90)).astype(np.uint8)
    n, lab, st, _ = cv2.connectedComponentsWithStats(red, 8); m = np.zeros(red.shape, np.uint8)
    for k in range(1, n):
        if st[k, 4] < 400: continue
        pts = np.argwhere(lab == k)[:, ::-1].astype(np.float32); hull = cv2.convexHull(pts)
        (cx, cy), R = cv2.minEnclosingCircle(pts)
        if 45 < R < 115 and cv2.contourArea(hull) > 0.55 * np.pi * R * R:  # un disque, pas un aliment rouge
            cv2.circle(m, (int(cx), int(cy)), int(R), 1, -1)
    return cv2.dilate(m, np.ones((15, 15), np.uint8)) > 0
def clean(a):
    a[..., 3] = np.where(a[..., 3] < 130, 0, a[..., 3])
    m = (a[..., 3] > 0).astype(np.uint8); k, lab, st, _ = cv2.connectedComponentsWithStats(m, 8)
    keep = np.zeros(k, bool); keep[1:] = st[1:, 4] > 0.04 * st[1:, 4].max(); a[..., 3] = np.where(keep[lab], a[..., 3], 0)
    o = Image.fromarray(a); return o.crop(o.getbbox())
only = sys.argv[2:]; HD = {"classique", "b243", "ailes", "fingers", "wings", "pepperon", "shawarma", "frite", "crispy"}; NOBADGE = {"wings"}
for name, (src, (x0, y0, x1, y1)) in CROPS.items():
    if only and name not in only: continue
    im = Image.open(os.path.join(SRC, src)).convert("RGB").crop((x0 + OX, y0 + OY, x1 + OX, y1 + OY))
    p = os.path.join(UP, name + ".png")
    if os.path.exists(p): up = Image.open(p).convert("RGB")  # déjà agrandie
    else:
        up = upscale(im); up = ImageEnhance.Contrast(up).enhance(1.06); up = ImageEnhance.Color(up).enhance(1.15); up.save(p)
    bm = badge_mask(np.array(up)) if name not in NOBADGE else np.zeros((up.height, up.width), bool)
    if name in HD:  # deuxième passage pour les plats montrés en grand (pastilles repérées avant)
        up = upscale(up); up = up.resize((up.width // 2, up.height // 2), Image.LANCZOS)
        bm = np.array(Image.fromarray(bm).resize(up.size, Image.NEAREST))
    o = np.array(remove(up, session=sess)); o[bm, 3] = 0; o = clean(o)
    o.save(os.path.join(OUT, name + ".png")); print(name, im.size, "->", o.size, flush=True)
