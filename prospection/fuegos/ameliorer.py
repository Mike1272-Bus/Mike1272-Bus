"""Fuegos : recadrage des photos (sans les mains ni les prix), agrandissement Real-ESRGAN, logo en disque.
Usage : python3 ameliorer.py <RealESRGAN_x4plus.pth>"""
import os, sys, torch, numpy as np
from PIL import Image, ImageEnhance, ImageDraw
from spandrel import ModelLoader
HERE = os.path.dirname(os.path.abspath(__file__)); SRC = os.path.join(HERE, "work", "src"); OUT = os.path.join(HERE, "assets", "img")
K = 1080 / 973  # capture affichée -> pixels réels
CROPS = {  # boîtes en coordonnées d'affichage : ni mains, ni bras, ni prix, ni textes de l'affiche
    "burger": ("f2.jpg", (300, 862, 973, 1236)),
    "tacos": ("f3.jpg", (420, 1132, 866, 1468)),
    "dealbox": ("f4.jpg", (0, 838, 973, 1690)),
}
def upscale(im, model):
    t = torch.from_numpy(np.array(im).astype(np.float32) / 255).permute(2, 0, 1)[None]; out = []
    with torch.no_grad():  # par bandes pour limiter la mémoire
        h = t.shape[2]; step = 120
        for y in range(0, h, step):
            a, b = max(0, y - 8), min(h, y + step + 8); o = model(t[:, :, a:b])
            out.append(o[:, :, (y - a) * 4:(y - a) * 4 + (min(h, y + step) - y) * 4])
    o = torch.cat(out, 2)[0].clamp(0, 1).permute(1, 2, 0).numpy(); return Image.fromarray((o * 255).round().astype(np.uint8))
if __name__ == "__main__":
    model = ModelLoader().load_from_file(sys.argv[1]).eval(); torch.set_num_threads(os.cpu_count())
    for name, (src, box) in CROPS.items():
        im = Image.open(os.path.join(SRC, src)).convert("RGB").crop(tuple(round(v * K) for v in box))
        up = upscale(im, model); up = up.resize((up.width // 2, up.height // 2), Image.LANCZOS)  # x2 final, plus net
        up = ImageEnhance.Contrast(up).enhance(1.04); up = ImageEnhance.Color(up).enhance(1.08)
        up.save(os.path.join(OUT, name + ".jpg"), quality=92); print(name, im.size, "->", up.size, flush=True)
    s = Image.open(os.path.join(SRC, "f1.jpg")).convert("RGB"); cx, cy, r = round(486 * K), round(940 * K), round(316 * K)
    lg = s.crop((cx - r, cy - r, cx + r, cy + r)).convert("RGBA"); S = lg.width * 4
    m = Image.new("L", (S, S), 0); ImageDraw.Draw(m).ellipse((0, 0, S - 1, S - 1), fill=255); lg.putalpha(m.resize(lg.size, Image.LANCZOS))
    lg.save(os.path.join(OUT, "logo.png")); print("logo", lg.size)
    # version sans le disque : on retire le bordeaux du fond, il reste l'écriture crème et la flamme rouge
    a = np.array(lg).astype(float); bg = np.array([90, 12, 0.0]); d = np.sqrt(((a[..., :3] - bg) ** 2).sum(2))
    a[..., 3] = np.clip((d - 40) / 60, 0, 1) * a[..., 3]; o = Image.fromarray(a.astype(np.uint8)); o = o.crop(o.getbbox())
    o.save(os.path.join(OUT, "logo_seul.png")); print("logo_seul", o.size)
