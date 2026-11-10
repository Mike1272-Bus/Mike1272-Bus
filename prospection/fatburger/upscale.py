"""Agrandit ×4 (EDSR) le recadrage du burger, pour des couches nettes en grand."""
import cv2, os, sys
S = sys.argv[1]
here = os.path.join(os.path.dirname(os.path.abspath(__file__)), "work")
sr = cv2.dnn_superres.DnnSuperResImpl_create(); sr.readModel(os.path.join(S, "EDSR_x4.pb")); sr.setModel("edsr", 4)
for name, (x0, y0, x1, y1) in {"burger": (180, 140, 650, 575)}.items():
    im = cv2.imread(os.path.join(here, "src", name + ".jpg"))[y0:y1, x0:x1]
    up = sr.upsample(im)
    up = cv2.resize(up, None, fx=0.6, fy=0.6, interpolation=cv2.INTER_AREA)  # ×2,4 au final : net et léger
    cv2.imwrite(os.path.join(here, "up", name + ".png"), up); print(name, up.shape)
