"""Agrandit ×4 les photos Burger Guys (300 px) avec EDSR, puis un léger renfort de netteté."""
import cv2, glob, os, sys
S = sys.argv[1]
sr = cv2.dnn_superres.DnnSuperResImpl_create(); sr.readModel(os.path.join(S, "EDSR_x4.pb")); sr.setModel("edsr", 4)
here = os.path.join(os.path.dirname(os.path.abspath(__file__)), "work")
for f in sorted(glob.glob(os.path.join(here, "src", "p*.jpg"))):
    im = cv2.imread(f)
    up = sr.upsample(im)
    blur = cv2.GaussianBlur(up, (0, 0), 2.0)
    up = cv2.addWeighted(up, 1.25, blur, -0.25, 0)
    out = os.path.join(here, "up", os.path.basename(f).replace(".jpg", ".png"))
    cv2.imwrite(out, up); print(out, up.shape)
