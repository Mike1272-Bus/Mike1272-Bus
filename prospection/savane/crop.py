"""Visuels Savane, uniquement à partir de leurs publications, de leur photo de profil et de leur vidéo."""
import os
import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "work", "src")
OUT = os.path.join(ROOT, "assets", "img")
K = 1080 / 973  # les captures font 1080 px de large, affichées à 973


def shot(n):
    return Image.open(os.path.join(SRC, f"c{n}.png")).convert("RGB")


def box(x0, y0, x1, y1):
    return tuple(int(v * K) for v in (x0, y0, x1, y1))


os.makedirs(OUT, exist_ok=True)
# logo blanc « Savane » : agrandi ×3 puis seuillé, bords nets
lg = shot(2).crop(box(330, 360, 650, 440)).convert("L").resize((1065 * 3 // 1, 266 * 3 // 1), Image.LANCZOS)
a = np.array(lg).astype(float)
a = np.clip((a - 90) * 255 / 80, 0, 255).astype(np.uint8)
logo = Image.new("RGBA", lg.size, (255, 255, 255, 0)); logo.putalpha(Image.fromarray(a))
logo = logo.crop(logo.getbbox()); logo.save(os.path.join(OUT, "logo.png")); print("logo", logo.size)

# photos sans le logo ni l'adresse imprimés dessus
for name, n, b in [("cocktail", 2, (0, 452, 973, 1395)), ("calamars", 3, (0, 545, 973, 1488)),
                   ("plateau", 6, (0, 515, 973, 1440)), ("bouchees", 7, (0, 530, 973, 1470))]:
    im = shot(n).crop(box(*b)); im.save(os.path.join(OUT, name + ".jpg"), quality=92); print(name, im.size)
