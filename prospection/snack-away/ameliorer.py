"""Snack Away : recadrage des photos (sans les textes de leurs visuels), agrandissement Real-ESRGAN, logo.
Usage : python3 ameliorer.py <RealESRGAN_x4plus.pth>"""
import os, sys, torch, numpy as np
from PIL import Image, ImageEnhance
from spandrel import ModelLoader
HERE = os.path.dirname(os.path.abspath(__file__)); SRC = os.path.join(HERE, "work", "src"); OUT = os.path.join(HERE, "assets", "img")
CROPS = {  # boîtes en pixels des images d'origine
    "zinger": ("zinger.jpg", (0, 96, 700, 600)),      # sans le logo en haut ni « Zinger Burgers » en bas
    "teriyaki": ("teriyaki.jpg", (0, 92, 700, 525)),  # sans le logo en haut ni « Sandwich Teriyaki » en bas
    "salle": ("salle.jpg", (0, 0, 784, 588)),
    "logo": ("teriyaki.jpg", (276, 14, 426, 90)),
}
model = ModelLoader().load_from_file(sys.argv[1]).eval(); torch.set_num_threads(os.cpu_count())
def upscale(im):
    t = torch.from_numpy(np.array(im).astype(np.float32) / 255).permute(2, 0, 1)[None]; out = []
    with torch.no_grad():
        h = t.shape[2]
        for y in range(0, h, 120):
            a, b = max(0, y - 8), min(h, y + 128); o = model(t[:, :, a:b]); out.append(o[:, :, (y - a) * 4:(y - a) * 4 + (min(h, y + 120) - y) * 4])
    return Image.fromarray((torch.cat(out, 2)[0].clamp(0, 1).permute(1, 2, 0).numpy() * 255).round().astype(np.uint8))
for name, (src, box) in CROPS.items():
    im = Image.open(os.path.join(SRC, src)).convert("RGB").crop(box); up = upscale(im)
    if name != "logo": up = up.resize((up.width // 2, up.height // 2), Image.LANCZOS)
    up = ImageEnhance.Color(up).enhance(1.06); up.save(os.path.join(OUT, name + (".png" if name == "logo" else ".jpg")), quality=92); print(name, im.size, "->", up.size, flush=True)
