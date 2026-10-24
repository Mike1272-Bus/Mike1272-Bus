"""Visuels Burger Guys, uniquement à partir de leurs photos (agrandies ×4 dans work/up)."""
import os
import numpy as np
import cv2
from PIL import Image, ImageDraw
from rembg import remove, new_session

ROOT = os.path.dirname(os.path.abspath(__file__))
UP = os.path.join(ROOT, "work", "up")
OUT = os.path.join(ROOT, "assets", "img")
S_U2, S_IS = new_session("u2net"), new_session("isnet-general-use")


def src(name, box=None):
    im = Image.open(os.path.join(UP, name + ".png")).convert("RGB")
    return im.crop(box) if box else im


def mask(img, boost=2.0):
    u = np.array(remove(img, session=S_U2, only_mask=True)).astype(float)
    i = np.array(remove(img, session=S_IS, only_mask=True)).astype(float)
    a = np.clip(np.maximum(u, i * boost), 0, 255)
    a[a < 25] = 0
    return a.astype(np.uint8)


def cut(img, name, a=None, biggest=True):
    a = mask(img) if a is None else a
    if biggest:
        n, lab, st, _ = cv2.connectedComponentsWithStats((a > 0).astype(np.uint8))
        k = 1 + int(np.argmax(st[1:, cv2.CC_STAT_AREA]))
        a = np.where(lab == k, a, 0).astype(np.uint8)
    im = Image.fromarray(np.dstack([np.array(img), a]), "RGBA")
    im = im.crop(Image.fromarray(a).getbbox())
    im.save(os.path.join(OUT, name + ".png"))
    print(name, im.size)
    return im


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    cut(src("p1", (330, 170, 1130, 960)), "burger")
    cut(src("p1", (0, 560, 480, 900)), "frites")
    cut(src("p7", (0, 330, 560, 1200)), "onion_rings")
    cut(src("p7", (500, 300, 1200, 1200)), "chicken")
    cut(src("p6", (180, 300, 1060, 1000)), "burger_sauce")
    # logo rond (capture d'écran de leur profil)
    s = np.array(Image.open(os.path.join(ROOT, "work", "src", "logo_screen.png")).convert("RGB")).astype(int)
    red = (s[..., 0] > 200) & (s[..., 1] < 90) & (s[..., 2] < 90)
    ys, xs = np.where(red)
    cx, cy, r = (xs.min() + xs.max()) // 2, (ys.min() + ys.max()) // 2, (xs.max() - xs.min()) // 2
    lg = Image.fromarray(s.astype(np.uint8)).crop((cx - r, cy - r, cx + r, cy + r)).resize((720, 720), Image.LANCZOS).convert("RGBA")
    m = Image.new("L", (720 * 4, 720 * 4), 0); ImageDraw.Draw(m).ellipse((6, 6, 720 * 4 - 6, 720 * 4 - 6), fill=255)
    lg.putalpha(m.resize((720, 720), Image.LANCZOS)); lg.save(os.path.join(OUT, "logo.png")); print("logo", cx, cy, r)
    # photos pleine image
    src("p3").save(os.path.join(OUT, "menu.jpg"), quality=92)
    src("p4").save(os.path.join(OUT, "salle.jpg"), quality=92)
    src("p2").save(os.path.join(OUT, "duo.jpg"), quality=92)
