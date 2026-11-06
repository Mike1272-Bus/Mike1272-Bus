"""Détoure les plats améliorés (rembg isnet-general-use) et le logo (disque)."""
import os, numpy as np, cv2
from PIL import Image, ImageDraw
from rembg import remove, new_session
HERE = os.path.dirname(os.path.abspath(__file__)); UP = os.path.join(HERE, "work", "up"); OUT = os.path.join(HERE, "assets", "img")
sess = new_session("isnet-general-use")
def clean(o):
    a = np.array(o); a[..., 3] = np.where(a[..., 3] < 130, 0, a[..., 3])
    m = (a[..., 3] > 0).astype(np.uint8); k, lab, st, _ = cv2.connectedComponentsWithStats(m, 8)
    keep = np.zeros(k, bool); keep[1:] = st[1:, 4] > 0.03 * st[1:, 4].max(); a[..., 3] = np.where(keep[lab], a[..., 3], 0)
    o = Image.fromarray(a); return o.crop(o.getbbox())
for n in ("tacos_tranches", "tacos_coca", "poulet_mayo"):
    im = Image.open(os.path.join(UP, n + ".png")); im = im.resize((im.width // 2, im.height // 2), Image.LANCZOS)
    o = clean(remove(im, session=sess)); o.save(os.path.join(OUT, n + ".png")); print(n, o.size)
# photo plein cadre (intérieur du tacos), allégée
im = Image.open(os.path.join(UP, "tacos_dedans.png")); im = im.resize((1080, round(im.height * 1080 / im.width)), Image.LANCZOS); im.save(os.path.join(OUT, "tacos_dedans.jpg"), quality=90)
# logo : disque blanc bordé de rouge
lg = Image.open(os.path.join(UP, "logo.png")).convert("RGBA"); s = lg.width; m = Image.new("L", (s, s), 0)
ImageDraw.Draw(m).ellipse((10, 10, s - 10, s - 10), fill=255); lg.putalpha(m); lg.save(os.path.join(OUT, "logo.png")); print("logo", lg.size)

# retouches : canette (marque d'une autre entreprise) et bout de comptoir retirés, ligne du numéro (illisible) masquée
def zero(n, fx0, fy0, fx1, fy1):
    p = os.path.join(OUT, n + ".png"); a = np.array(Image.open(p)); h, w = a.shape[:2]
    a[int(h * fy0):int(h * fy1), int(w * fx0):int(w * fx1), 3] = 0; o = Image.fromarray(a); o.crop(o.getbbox()).save(p)
zero("tacos_coca", 0.0, 0.0, 1.0, 0.24); zero("tacos_coca", 0.25, 0.0, 0.55, 0.12)
zero("poulet_mayo", 0.0, 0.0, 0.22, 0.2); zero("poulet_mayo", 0.0, 0.0, 0.2, 0.13)
p = os.path.join(OUT, "logo.png"); lg = Image.open(p); d = ImageDraw.Draw(lg); s = lg.width
d.rectangle((int(s * 0.26), int(s * 0.745), int(s * 0.74), int(s * 0.835)), fill=(255, 255, 255, 255)); lg.save(p)
zero("tacos_coca", 0.3, 0.0, 0.62, 0.13); zero("poulet_mayo", 0.18, 0.0, 0.45, 0.12); zero("poulet_mayo", 0.0, 0.1, 0.1, 0.32)
lg = Image.open(p); d = ImageDraw.Draw(lg); d.rectangle((int(s * 0.26), int(s * 0.745), int(s * 0.78), int(s * 0.84)), fill=(255, 255, 255, 255)); lg.save(p)
# ligne « AMILIKI » refaite en Oswald (la capture l'avait abîmée : tache grise sur le I)
from PIL import ImageFont
lg = Image.open(p); d = ImageDraw.Draw(lg); d.rectangle((444, 456, 642, 512), fill=(255, 255, 255, 255))
f = ImageFont.truetype(os.path.join(HERE, "assets", "fonts", "Oswald-Bold.ttf"), 60)
t = Image.new("RGBA", (400, 120), (0, 0, 0, 0)); ImageDraw.Draw(t).text((0, 0), "AMILIKI", font=f, fill=(17, 17, 17, 255)); t = t.crop(t.getbbox())
lg.alpha_composite(t.resize((192, 46), Image.LANCZOS), (447, 461)); lg.save(p)
