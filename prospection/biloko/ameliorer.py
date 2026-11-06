"""Biloko : le plat de leur affiche (agrandi Real-ESRGAN, détouré, prix et textes retirés) et le logo en disque.
Usage : python3 ameliorer.py <RealESRGAN_x4plus.pth>"""
import os, sys, torch, numpy as np, cv2
from PIL import Image, ImageDraw
from spandrel import ModelLoader
from rembg import remove, new_session
HERE = os.path.dirname(os.path.abspath(__file__)); SRC = os.path.join(HERE, "work", "src"); OUT = os.path.join(HERE, "assets", "img")
K = 1080 / 973  # capture affichée -> pixels réels
model = ModelLoader().load_from_file(sys.argv[1]).eval(); torch.set_num_threads(os.cpu_count())
im = Image.open(os.path.join(SRC, "b2.jpg")).convert("RGB").crop(tuple(round(v * K) for v in (360, 600, 973, 1135)))
t = torch.from_numpy(np.array(im).astype(np.float32) / 255).permute(2, 0, 1)[None]; out = []
with torch.no_grad():
    h = t.shape[2]
    for y in range(0, h, 120):
        a, b = max(0, y - 8), min(h, y + 128); o = model(t[:, :, a:b]); out.append(o[:, :, (y - a) * 4:(y - a) * 4 + (min(h, y + 120) - y) * 4])
up = Image.fromarray((torch.cat(out, 2)[0].clamp(0, 1).permute(1, 2, 0).numpy() * 255).round().astype(np.uint8))
up = up.resize((up.width // 2, up.height // 2), Image.LANCZOS); up.save(os.path.join(HERE, "work", "up", "plat.png"))
o = np.array(remove(up, session=new_session("isnet-general-use"))); H, W = o.shape[:2]; s = W / 680  # repères pris sur le recadrage de 680 px
m = Image.new("L", (W, H), 0); d = ImageDraw.Draw(m)
d.polygon([(400 * s, 420 * s), (640 * s, 395 * s), (680 * s, 470 * s), (680 * s, 594 * s), (400 * s, 594 * s)], fill=255)  # pastille de prix
d.rectangle((0, 0, 175 * s, 275 * s), fill=255)  # textes de l'affiche à gauche
d.rectangle((370 * s, 0, 440 * s, 80 * s), fill=255); d.rectangle((600 * s, 380 * s, 680 * s, 594 * s), fill=255)  # traits jaunes
o[..., 3] = np.where(np.array(m) > 0, 0, o[..., 3]); o[..., 3] = np.where(o[..., 3] < 120, 0, o[..., 3])
n, lab, st, _ = cv2.connectedComponentsWithStats((o[..., 3] > 0).astype(np.uint8), 8)
keep = np.zeros(n, bool); keep[1:] = st[1:, 4] > 0.05 * st[1:, 4].max(); o[..., 3] = np.where(keep[lab], o[..., 3], 0)
# (détourage abandonné, voir plus bas)
s1 = Image.open(os.path.join(SRC, "b1.jpg")).convert("RGB"); cx, cy, r = round(486 * K), round(940 * K), round(318 * K)
lg = s1.crop((cx - r, cy - r, cx + r, cy + r)).convert("RGBA"); S = lg.width * 4
mm = Image.new("L", (S, S), 0); ImageDraw.Draw(mm).ellipse((0, 0, S - 1, S - 1), fill=255); lg.putalpha(mm.resize(lg.size, Image.LANCZOS))
lg.save(os.path.join(OUT, "logo.png")); print("logo", lg.size)
# le détourage perd les frites (jaune sur jaune) : on garde plutôt une photo cadrée, sans textes ni prix
s = up.width / 680; up.crop((round(178 * s), 0, up.width, round(396 * s))).save(os.path.join(OUT, "plat.jpg"), quality=92)
