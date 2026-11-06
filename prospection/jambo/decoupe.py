"""Détoure les bouteilles Jambo (fond sombre) : seuil couleur + nettoyage, garde la plus grande forme."""
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage as nd
NOMS = ["p-gingembre", "p-maracuja", "p-citron", "v-maracuja", "v-citron", "v-mangue", "v-gingembre"]
for n in NOMS:
    im = Image.open(f"work/{n}.png").convert("RGB"); a = np.asarray(im).astype(int)
    R, G, B = a[..., 0], a[..., 1], a[..., 2]; V = a.max(-1)
    m = (V > 125) | ((R > 120) & (R - G > 50)) | ((R - B > 30) & (R > 60) & (R - G > 25))
    m = nd.binary_opening(m, iterations=3)
    lab, k = nd.label(m); sz = nd.sum(m, lab, range(1, k + 1)); m = lab == (1 + int(np.argmax(sz)))
    m = nd.binary_closing(m, iterations=8); m = nd.binary_fill_holes(m)
    # remplir les trous de chaque ligne (verre transparent du goulot)
    for y in range(m.shape[0]):
        xs = np.where(m[y])[0]
        if len(xs) and xs[-1] - xs[0] < m.shape[1] * 0.9: m[y, xs[0]:xs[-1] + 1] = True
    m = nd.binary_opening(m, iterations=10 if n.startswith("p-") else 4)  # enlève les taches du mur près du bouchon
    lab, k = nd.label(m); sz = nd.sum(m, lab, range(1, k + 1)); m = lab == (1 + int(np.argmax(sz)))
    al = Image.fromarray((m * 255).astype("uint8")).filter(ImageFilter.GaussianBlur(1.5))
    out = im.convert("RGBA"); out.putalpha(al); out = out.crop(out.getbbox()); out.save(f"assets/img/{n}.png")
    print(n, out.size)

# Bissap (jus rouge foncé sur fond sombre) : le seuil ne marche pas. Même bouteille en verre que la mangue :
# on reprend la silhouette de la mangue, décalée sur la bouteille de bissap (photo 5 bouteilles).
K = 1080 / 973
src = Image.open("photos-client/5-bouteilles-verre.png").convert("RGB")
mg = Image.open("work/v-mangue.png").convert("RGB")
a = np.asarray(mg).astype(int); R, G, B = a[..., 0], a[..., 1], a[..., 2]; V = a.max(-1)
m = (V > 125) | ((R > 120) & (R - G > 50))
m = nd.binary_opening(m, iterations=3); lab, k = nd.label(m); sz = nd.sum(m, lab, range(1, k + 1)); m = lab == (1 + int(np.argmax(sz)))
m = nd.binary_closing(m, iterations=8); m = nd.binary_fill_holes(m)
for y in range(m.shape[0]):
    xs = np.where(m[y])[0]
    if len(xs) and xs[-1] - xs[0] < m.shape[1] * 0.9: m[y, xs[0]:xs[-1] + 1] = True
m = nd.binary_opening(m, iterations=4)
ys, xs = np.where(m); x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
ox, oy = int(400 * K) * 2, int(780 * K) * 2  # coin du recadrage mangue (x2)
big = src.resize((src.width * 2, src.height * 2), Image.LANCZOS)
DX = int((857 - 478) * K * 2) + 6; DY = int(-12 * K * 2)
X0, Y0 = ox + x0 + DX, oy + y0 + DY
crop = big.crop((X0, Y0, X0 + (x1 - x0) + 1, Y0 + (y1 - y0) + 1)).convert("RGBA")
al = Image.fromarray((m[y0:y1 + 1, x0:x1 + 1] * 255).astype("uint8")).filter(ImageFilter.GaussianBlur(1.5))
crop.putalpha(al); crop.save("assets/img/v-bissap.png"); print("v-bissap", crop.size)

# Maracuja : une tache du mur reste collée au bouchon (en haut à droite) : on l'efface.
im = Image.open("assets/img/p-maracuja.png"); a = np.asarray(im).copy(); h, w = a.shape[:2]
a[: int(h * 0.128), int(w * 0.885):, 3] = 0
Image.fromarray(a).save("assets/img/p-maracuja.png")
