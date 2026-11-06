"""Visuels Fatburger, uniquement à partir de leurs photos et de la capture de leur profil."""
import os
import numpy as np
import cv2
from PIL import Image, ImageDraw
from rembg import remove, new_session

ROOT = os.path.dirname(os.path.abspath(__file__))
W = os.path.join(ROOT, "work")
OUT = os.path.join(ROOT, "assets", "img")
S_U2, S_IS = new_session("u2net"), new_session("isnet-general-use")


def mask(img, boost=2.0):
    u = np.array(remove(img, session=S_U2, only_mask=True)).astype(float)
    i = np.array(remove(img, session=S_IS, only_mask=True)).astype(float)
    a = np.clip(np.maximum(u, i * boost), 0, 255)
    a[a < 25] = 0
    return a.astype(np.uint8)


def biggest(a):
    n, lab, st, _ = cv2.connectedComponentsWithStats((a > 0).astype(np.uint8))
    k = 1 + int(np.argmax(st[1:, cv2.CC_STAT_AREA]))
    return np.where(lab == k, a, 0).astype(np.uint8)


def save(img, a, name):
    im = Image.fromarray(np.dstack([np.array(img), a]), "RGBA")
    im = im.crop(Image.fromarray(a).getbbox()); im.save(os.path.join(OUT, name + ".png")); print(name, im.size)
    return im


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    b = Image.open(os.path.join(W, "up", "burger.png")).convert("RGB")
    save(b, biggest(mask(b)), "burger")
    s = Image.open(os.path.join(W, "src", "shakes.jpg")).convert("RGB").crop((30, 80, 780, 700))
    save(s, biggest(mask(s)), "shakes")
    # logo rond (capture du profil) : le disque turquoise
    sc = np.array(Image.open(os.path.join(W, "src", "logo_screen.png")).convert("RGB")).astype(int)
    teal = (sc[..., 0] < 90) & (sc[..., 1] > 170) & (sc[..., 2] > 190)
    ys, xs = np.where(teal)
    cx, cy, r = (xs.min() + xs.max()) // 2, (ys.min() + ys.max()) // 2, (xs.max() - xs.min()) // 2
    lg = Image.fromarray(sc.astype(np.uint8)).crop((cx - r, cy - r, cx + r, cy + r)).resize((720, 720), Image.LANCZOS).convert("RGBA")
    m = Image.new("L", (2880, 2880), 0); ImageDraw.Draw(m).ellipse((8, 8, 2872, 2872), fill=255)
    lg.putalpha(m.resize((720, 720), Image.LANCZOS)); lg.save(os.path.join(OUT, "logo.png")); print("logo", cx, cy, r)
    for n in ["plateau", "sac", "shakes"]:
        Image.open(os.path.join(W, "src", n + ".jpg")).convert("RGB").save(os.path.join(OUT, n + ".jpg"), quality=92)
