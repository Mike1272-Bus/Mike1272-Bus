"""Découpe les produits et le logo dans les captures Facebook de Chicken Inn (agrandissement EDSR x4 puis détourage rembg)."""
import os, sys, cv2, numpy as np
from PIL import Image, ImageDraw
from rembg import remove, new_session
HERE = os.path.dirname(os.path.abspath(__file__)); SRC = os.path.join(HERE, "work", "src"); OUT = os.path.join(HERE, "assets", "img")
sr = cv2.dnn_superres.DnnSuperResImpl_create(); sr.readModel(sys.argv[1]); sr.setModel("edsr", 4)
sess = new_session("isnet-general-use")
def up(img, box, f=2):
    c = cv2.cvtColor(np.array(img.crop(box)), cv2.COLOR_RGB2BGR)
    c = cv2.resize(c, None, fx=f / 4, fy=f / 4, interpolation=cv2.INTER_AREA) if f < 4 else c
    u = sr.upsample(c); b = cv2.GaussianBlur(u, (0, 0), 2); u = cv2.addWeighted(u, 1.25, b, -0.25, 0)
    return Image.fromarray(cv2.cvtColor(u, cv2.COLOR_BGR2RGB))
def cut(name, src, box, f=2):
    o = remove(up(Image.open(os.path.join(SRC, src)).convert("RGB"), box, f), session=sess); o = o.crop(o.getbbox()); o.save(os.path.join(OUT, name + ".png")); print(name, o.size)
cut("deux_pieces_frites", "c1.jpg", (100, 880, 1060, 1560))
cut("burger_frites", "c4.jpg", (560, 1000, 1060, 1330), 4)
cut("quart_poulet", "c3.jpg", (0, 990, 540, 1330), 4)
cut("pack_famille", "c5.jpg", (710, 1270, 1080, 1455), 4)
cut("assiette_frites", "c2.jpg", (316, 1264, 940, 1850))
# logo : voir logo.py (détourage + remplissage de la forme avec les pixels d'origine)

# nettoyage : traces semi-transparentes, pastilles de prix (on n'affiche pas les prix), logo détouré
def clean(name, zero=()):
    im = Image.open(os.path.join(OUT, name + ".png")); a = np.array(im)
    a[..., 3] = np.where(a[..., 3] < 130, 0, a[..., 3])
    for x0, y0, x1, y1 in zero: a[y0:y1, x0:x1, 3] = 0
    o = Image.fromarray(a); o = o.crop(o.getbbox()); o.save(os.path.join(OUT, name + ".png")); print("propre", name, o.size)
clean("deux_pieces_frites", [(0, 0, 600, 350)])
clean("burger_frites", [(0, 800, 600, 1400)])
clean("quart_poulet", [(0, 800, 600, 1400)])
clean("pack_famille"); clean("assiette_frites")
