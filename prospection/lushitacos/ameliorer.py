"""LushiTacos : recadrage des photos de leur fiche Google (sans les bandeaux de l'appli), agrandissement Real-ESRGAN.
Usage : python3 ameliorer.py <RealESRGAN_x4plus.pth>"""
import os, sys, torch, numpy as np
from PIL import Image, ImageEnhance
from spandrel import ModelLoader
HERE = os.path.dirname(os.path.abspath(__file__)); SRC = os.path.join(HERE, "work", "src"); OUT = os.path.join(HERE, "assets", "img")
K = 1080 / 923  # capture affichée -> pixels réels
CROPS = {"planche": ("l1.jpg", (0, 604, 923, 1346)), "duo": ("l3.jpg", (0, 762, 923, 1188)), "affiche": ("l2.jpg", (0, 362, 923, 1205))}
model = ModelLoader().load_from_file(sys.argv[1]).eval(); torch.set_num_threads(os.cpu_count())
for name, (src, box) in CROPS.items():
    im = Image.open(os.path.join(SRC, src)).convert("RGB").crop(tuple(round(v * K) for v in box))
    if im.width > 700: im = im.resize((700, round(im.height * 700 / im.width)), Image.LANCZOS)  # la capture est déjà agrandie : on repart d'une taille proche de l'original
    t = torch.from_numpy(np.array(im).astype(np.float32) / 255).permute(2, 0, 1)[None]; out = []
    with torch.no_grad():
        h = t.shape[2]
        for y in range(0, h, 120):
            a, b = max(0, y - 8), min(h, y + 128); o = model(t[:, :, a:b]); out.append(o[:, :, (y - a) * 4:(y - a) * 4 + (min(h, y + 120) - y) * 4])
    up = Image.fromarray((torch.cat(out, 2)[0].clamp(0, 1).permute(1, 2, 0).numpy() * 255).round().astype(np.uint8))
    up = up.resize((up.width // 2, up.height // 2), Image.LANCZOS); up = ImageEnhance.Color(up).enhance(1.08); up = ImageEnhance.Contrast(up).enhance(1.04)
    up.save(os.path.join(OUT, name + ".jpg"), quality=92); print(name, im.size, "->", up.size, flush=True)
