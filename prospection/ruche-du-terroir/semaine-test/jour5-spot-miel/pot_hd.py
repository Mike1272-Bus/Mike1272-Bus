"""Le vrai pot « clou de girofle » (photos-client/detoure-v2) agrandi x2 net avec Real-ESRGAN (la transparence suit en bicubique).
Usage : python3 pot_hd.py <RealESRGAN_x4plus.pth>"""
import os, sys, torch, numpy as np
from PIL import Image
from spandrel import ModelLoader
HERE = os.path.dirname(os.path.abspath(__file__))
src = Image.open(os.path.join(HERE, "..", "..", "photos-client", "detoure-v2", "clou-de-girofle.png")).convert("RGBA")
model = ModelLoader().load_from_file(sys.argv[1]).eval()
rgb = np.array(src.convert("RGB")).astype(np.float32) / 255
with torch.no_grad(): o = model(torch.from_numpy(rgb).permute(2, 0, 1)[None])
up = Image.fromarray((o[0].clamp(0, 1).permute(1, 2, 0).numpy() * 255).round().astype(np.uint8)).resize((src.width * 2, src.height * 2), Image.LANCZOS)
up.putalpha(src.getchannel("A").resize(up.size, Image.BICUBIC)); up.save(os.path.join(HERE, "assets", "img", "pot.png")); print(up.size)
