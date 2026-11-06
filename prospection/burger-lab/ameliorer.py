"""Burger Lab : recadrage des photos de leurs publications et stories (sans l'interface Instagram, sans mains), logo en disque.
Le milkshake (petit recadrage) passe par Real-ESRGAN. Usage : python3 ameliorer.py <RealESRGAN_x4plus.pth>"""
import os, sys, torch, numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter
from spandrel import ModelLoader
HERE = os.path.dirname(os.path.abspath(__file__)); SRC = os.path.join(HERE, "work", "src"); OUT = os.path.join(HERE, "assets", "img")
K = 1080 / 973  # capture affichée -> pixels réels
CROPS = {  # boîtes en coordonnées d'affichage
    "burger": ("b6.jpg", (0, 300, 973, 1560)),     # story : sans la barre du haut ni le champ « Envoyer un message »
    "tenders": ("b4.jpg", (0, 340, 973, 1550)),    # publication
    "wings": ("b5.jpg", (0, 215, 973, 1595)),      # story vue du dessus, 4 sauces
    "milkshake": ("b2.jpg", (250, 445, 815, 828)), # le haut du gobelet seulement : la main commence juste en dessous
}
model = None
for name, (src, box) in CROPS.items():
    im = Image.open(os.path.join(SRC, src)).convert("RGB").crop(tuple(round(v * K) for v in box))
    if name == "milkshake":
        if model is None: model = ModelLoader().load_from_file(sys.argv[1]).eval(); torch.set_num_threads(os.cpu_count())
        t = torch.from_numpy(np.array(im).astype(np.float32) / 255).permute(2, 0, 1)[None]; out = []
        with torch.no_grad():
            h = t.shape[2]
            for y in range(0, h, 120):
                a, b = max(0, y - 8), min(h, y + 128); o = model(t[:, :, a:b]); out.append(o[:, :, (y - a) * 4:(y - a) * 4 + (min(h, y + 120) - y) * 4])
        im = Image.fromarray((torch.cat(out, 2)[0].clamp(0, 1).permute(1, 2, 0).numpy() * 255).round().astype(np.uint8)); im = im.resize((im.width // 2, im.height // 2), Image.LANCZOS)
    else:
        im = im.filter(ImageFilter.UnsharpMask(radius=1.2, percent=60, threshold=2))
    im = ImageEnhance.Color(im).enhance(1.05); im.save(os.path.join(OUT, name + ".jpg"), quality=92); print(name, im.size, flush=True)
s = Image.open(os.path.join(SRC, "b1.jpg")).convert("RGB"); cx, cy, r = round(486 * K), round(975 * K), round(312 * K)
lg = s.crop((cx - r, cy - r, cx + r, cy + r)).convert("RGBA"); S = lg.width * 4
m = Image.new("L", (S, S), 0); ImageDraw.Draw(m).ellipse((0, 0, S - 1, S - 1), fill=255); lg.putalpha(m.resize(lg.size, Image.LANCZOS))
lg.save(os.path.join(OUT, "logo.png")); print("logo", lg.size)
