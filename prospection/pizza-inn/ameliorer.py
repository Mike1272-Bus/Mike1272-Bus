"""Pizza Inn : les 2 pizzas de leur affiche « Double Délice » détourées (sans prix ni textes), agrandies avec Real-ESRGAN, et le logo en disque.
Usage : python3 ameliorer.py <RealESRGAN_x4plus.pth>"""
import os, sys, torch, numpy as np, cv2
from PIL import Image, ImageDraw
from spandrel import ModelLoader
from rembg import remove, new_session
HERE = os.path.dirname(os.path.abspath(__file__)); SRC = os.path.join(HERE, "work", "src"); OUT = os.path.join(HERE, "assets", "img")
K = 1080 / 973; Y0 = round(338 * K)  # haut de l'affiche dans la capture
CROPS = {"pizza_viande": (0, 556, 742, 1077), "pizza_poulet": (494, 278, 1080, 712)}  # en pixels de l'affiche (1080 de large)
model = ModelLoader().load_from_file(sys.argv[1]).eval(); torch.set_num_threads(os.cpu_count()); sess = new_session("isnet-general-use")
ad = Image.open(os.path.join(SRC, "p2.jpg")).convert("RGB")
for name, (x0, y0, x1, y1) in CROPS.items():
    im = ad.crop((x0, y0 + Y0, x1, y1 + Y0))
    t = torch.from_numpy(np.array(im).astype(np.float32) / 255).permute(2, 0, 1)[None]; out = []
    with torch.no_grad():
        h = t.shape[2]
        for y in range(0, h, 120):
            a, b = max(0, y - 8), min(h, y + 128); o = model(t[:, :, a:b]); out.append(o[:, :, (y - a) * 4:(y - a) * 4 + (min(h, y + 120) - y) * 4])
    up = Image.fromarray((torch.cat(out, 2)[0].clamp(0, 1).permute(1, 2, 0).numpy() * 255).round().astype(np.uint8)); up = up.resize((up.width // 2, up.height // 2), Image.LANCZOS)
    up.save(os.path.join(HERE, "work", "up", name + ".png"))
    o = np.array(remove(up, session=sess)); s = up.width / (x1 - x0)
    if name == "pizza_poulet": o[: round((528 - y0) * s), : round((518 - x0) * s), 3] = 0  # le cadre rouge des prix
    o[..., 3] = np.where(o[..., 3] < 110, 0, o[..., 3])
    n, lab, st, _ = cv2.connectedComponentsWithStats((o[..., 3] > 0).astype(np.uint8), 8)
    keep = np.zeros(n, bool); keep[1:] = st[1:, 4] > 0.05 * st[1:, 4].max(); o[..., 3] = np.where(keep[lab], o[..., 3], 0)
    p = Image.fromarray(o); p.save(os.path.join(OUT, name + ".png")); print(name, p.size, flush=True)  # même cadre que le recadrage : les bords coupés restent droits
s1 = Image.open(os.path.join(SRC, "p1.jpg")).convert("RGB"); cx, cy, r = round(486 * K), round(975 * K), round(314 * K)
lg = s1.crop((cx - r, cy - r, cx + r, cy + r)).convert("RGBA"); S = lg.width * 4
m = Image.new("L", (S, S), 0); ImageDraw.Draw(m).ellipse((0, 0, S - 1, S - 1), fill=255); lg.putalpha(m.resize(lg.size, Image.LANCZOS))
lg.save(os.path.join(OUT, "logo.png")); print("logo", lg.size)
