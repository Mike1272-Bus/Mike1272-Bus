"""Bilengi : recadrages (logo, leurs bouteilles et le verre de leur affiche, miel, pilipili), agrandissement Real-ESRGAN.
Écartés : le livreur dessiné (personne), le burger et les sandwichs de l'affiche (on parle boisson et épicerie).
Usage : python3 ameliorer.py <RealESRGAN_x4plus.pth>"""
import os, sys, torch, numpy as np
from PIL import Image, ImageDraw, ImageEnhance
from spandrel import ModelLoader
HERE = os.path.dirname(os.path.abspath(__file__)); SRC = os.path.join(HERE, "work", "src"); OUT = os.path.join(HERE, "assets", "img")
CROPS = {  # nom : (fichier, boîte, facteur final)
    "logo": ("logo.jpg", (8, 8, 217, 217), 4),
    "bouteilles": ("flyer.jpg", (26, 270, 150, 400), 4),
    "verre": ("flyer.jpg", (120, 168, 330, 458), 4),
    "miel": ("miel.jpg", (0, 0, 554, 554), 2),
    "pilipili": ("pilipili.jpg", (0, 0, 480, 640), 2),
}
model = ModelLoader().load_from_file(sys.argv[1]).eval(); torch.set_num_threads(os.cpu_count())
def upscale(im):
    t = torch.from_numpy(np.array(im).astype(np.float32) / 255).permute(2, 0, 1)[None]; out = []
    with torch.no_grad():
        h = t.shape[2]
        for y in range(0, h, 120):
            a, b = max(0, y - 8), min(h, y + 128); o = model(t[:, :, a:b]); out.append(o[:, :, (y - a) * 4:(y - a) * 4 + (min(h, y + 120) - y) * 4])
    return Image.fromarray((torch.cat(out, 2)[0].clamp(0, 1).permute(1, 2, 0).numpy() * 255).round().astype(np.uint8))
only = sys.argv[2:]
for name, (src, box, f) in CROPS.items():
    if only and name not in only: continue
    im = Image.open(os.path.join(SRC, src)).convert("RGB").crop(box); up = upscale(im)
    if f == 2: up = up.resize((up.width // 2, up.height // 2), Image.LANCZOS)
    up = ImageEnhance.Color(up).enhance(1.06)
    if name == "verre":  # on recouvre de leur vert les bords des autres ronds de l'affiche (bouteilles, burger)
        d = ImageDraw.Draw(up); g = up.getpixel((int(up.width * 0.83), int(up.height * 0.8))); W, H = up.size
        d.rectangle((0, int(H * 0.35), int(W * 0.172), H), fill=g); d.rectangle((int(W * 0.905), int(H * 0.32), W, H), fill=g)
    if name == "logo":  # disque
        up = up.convert("RGBA"); S = up.width * 4; m = Image.new("L", (S, S), 0); ImageDraw.Draw(m).ellipse((0, 0, S - 1, S - 1), fill=255)
        up.putalpha(m.resize(up.size, Image.LANCZOS)); up.save(os.path.join(OUT, "logo.png"))
    else: up.save(os.path.join(OUT, name + ".jpg"), quality=92)
    print(name, im.size, "->", up.size, flush=True)
