# Détoure les icônes fournies par Mike (tuile carrée arrondie, fond transparent).
import numpy as np
from PIL import Image, ImageDraw
U = "/root/.claude/uploads/d253aa54-2766-50cc-8e30-b570e99679f0/"

def bounds(mask):
    ys, xs = np.where(mask)
    return xs.min(), ys.min(), xs.max(), ys.max()

def tile(im, box, out, size=256, rad=0.24):
    x0, y0, x1, y1 = box
    side = max(x1 - x0, y1 - y0)
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    c = im.crop((int(cx - side / 2), int(cy - side / 2), int(cx + side / 2), int(cy + side / 2))).resize((size, size), Image.LANCZOS).convert("RGBA")
    big = Image.new("L", (size * 4, size * 4), 0)
    ImageDraw.Draw(big).rounded_rectangle((4, 4, size * 4 - 5, size * 4 - 5), radius=int(size * 4 * rad), fill=255)
    m = big.resize((size, size), Image.LANCZOS)
    c.putalpha(m)
    a = np.asarray(c).copy(); a[a[..., 3] == 0, :3] = 0
    Image.fromarray(a).save(out, optimize=True)
    print(out, box)

def load(f): 
    im = Image.open(U + f).convert("RGB"); return im, np.asarray(im).astype(int)

# Gemini : tuile blanche au centre (le halo du fond est bleuté)
im, a = load("3c8f1130-image.png")
r, g, b = a[..., 0], a[..., 1], a[..., 2]
m = (r > 228) & (b - r < 5) & (g > 228)
m[:, :400] = False; m[:, 1160:] = False
x0, y0, x1, y1 = bounds(m)
tile(im, (x0 + 3, y0 + 3, x1 - 3, y1 - 3), "assets/icons/gemini.png")

# ChatGPT : tuile blanche sur fond gris
im, a = load("70a4a1f7-image.jpg")
tile(im, (191, 106, 455, 364), "assets/icons/chatgpt.png")

# Claude : tuile orange
im, a = load("572c367b-image.jpg")
r, g, b = a[..., 0], a[..., 1], a[..., 2]
m = (r > 180) & (r - b > 90)
x0, y0, x1, y1 = bounds(m)
tile(im, (x0 + 3, y0 + 3, x1 - 3, y1 - 3), "assets/icons/claude.png")

# Chariow : logo sur fond blanc, on garde une tuile blanche
im, a = load("358d55fc-image.png")
tile(im, (0, 0, 511, 511), "assets/icons/chariow.png", rad=0.22)
