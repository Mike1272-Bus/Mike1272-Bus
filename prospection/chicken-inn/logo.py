"""Logo Chicken Inn détouré à partir de leur visuel « Bonne fête des parents » (c8) : rembg + forme complétée avec les pixels d'origine."""
import sys, numpy as np, cv2
from PIL import Image
from rembg import remove, new_session
sr = cv2.dnn_superres.DnnSuperResImpl_create(); sr.readModel(sys.argv[1]); sr.setModel("edsr", 4)
im = Image.open("work/src/c8_logo.png").convert("RGB")
c = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR); u = sr.upsample(c); b = cv2.GaussianBlur(u, (0, 0), 2); u = cv2.addWeighted(u, 1.25, b, -0.25, 0)
U = Image.fromarray(cv2.cvtColor(u, cv2.COLOR_BGR2RGB))
o = np.array(remove(U, session=new_session("isnet-general-use")))
m = (o[..., 3] > 130).astype(np.uint8)
cnts, _ = cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE); c = max(cnts, key=cv2.contourArea)
hull = np.zeros_like(m); cv2.fillPoly(hull, [cv2.convexHull(c)], 1)
low = np.zeros_like(m); low[int(m.shape[0] * 0.45):] = 1
alpha = cv2.erode(np.where((m == 1) | ((hull == 1) & (low == 1)), 255, 0).astype(np.uint8), np.ones((5, 5), np.uint8))
out = Image.fromarray(np.dstack([np.array(U), alpha])); out.crop(out.getbbox()).save("assets/img/logo.png")
