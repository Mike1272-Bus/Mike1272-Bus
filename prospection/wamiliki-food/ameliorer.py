"""Améliore les photos Wamiliki Food (captures d'écran) : recadrage, agrandissement x4 Real-ESRGAN, lumière et couleurs.
Usage : python3 ameliorer.py <RealESRGAN_x4plus.pth>"""
import os, sys, torch, numpy as np
from PIL import Image, ImageEnhance, ImageFilter
from spandrel import ModelLoader
HERE = os.path.dirname(os.path.abspath(__file__)); SRC = os.path.join(HERE, "work", "src"); UP = os.path.join(HERE, "work", "up")
model = ModelLoader().load_from_file(sys.argv[1]).eval(); torch.set_num_threads(os.cpu_count())
K = 1080 / 923  # capture affichée -> pixels réels
CROPS = {  # nom : (capture, boîte en coordonnées d'affichage), choisies sans personnes
    "tacos_coca": ("w7.jpg", (30, 520, 923, 1400)),
    "tacos_tranches": ("w6.jpg", (15, 640, 923, 1375)),
    "tacos_dedans": ("w3.jpg", (110, 140, 813, 1395)),
    "poulet_mayo": ("w10.jpg", (37, 640, 923, 1435)),
    "logo": ("w10.jpg", (410, 468, 580, 638)),
}
def upscale(im):
    t = torch.from_numpy(np.array(im).astype(np.float32) / 255).permute(2, 0, 1)[None]
    out = []
    with torch.no_grad():  # par bandes pour limiter la mémoire
        h = t.shape[2]; step = 160
        for y in range(0, h, step):
            a, b = max(0, y - 8), min(h, y + step + 8)
            o = model(t[:, :, a:b])
            out.append(o[:, :, (y - a) * 4:(y - a) * 4 + (min(h, y + step) - y) * 4])
    o = torch.cat(out, 2)[0].clamp(0, 1).permute(1, 2, 0).numpy()
    return Image.fromarray((o * 255).round().astype(np.uint8))
for name, (src, box) in CROPS.items():
    im = Image.open(os.path.join(SRC, src)).convert("RGB").crop(tuple(int(v * K) for v in box))
    if im.width > 700: im = im.resize((700, round(im.height * 700 / im.width)), Image.LANCZOS)
    up = upscale(im)
    up = ImageEnhance.Contrast(up).enhance(1.06); up = ImageEnhance.Color(up).enhance(1.12); up = ImageEnhance.Brightness(up).enhance(1.03)
    up.save(os.path.join(UP, name + ".png")); print(name, im.size, "->", up.size, flush=True)
