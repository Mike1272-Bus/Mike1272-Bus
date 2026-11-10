"""Passe une vidéo Allegra (modèle bleu) dans la D.A. claire (fond crème, Inter, titres orange en relief, nouveau logo).
Usage : python3 appliquer_da_claire.py <dossier-video> ..."""
import os, re, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "marque", "fonts")
CSS = """
      /* ===== D.A. claire (comme les vidéos paniers) ===== */
      @font-face { font-family: 'Inter'; font-weight: 600; src: url('assets/fonts/inter-latin-600-normal.woff2') format('woff2'); }
      @font-face { font-family: 'Inter'; font-weight: 800; src: url('assets/fonts/inter-latin-800-normal.woff2') format('woff2'); }
      @font-face { font-family: 'Inter'; font-weight: 900; src: url('assets/fonts/inter-latin-900-normal.woff2') format('woff2'); }
      html, body { background: #ffffff; }
      #root { background: radial-gradient(ellipse at 50% 45%, #ffffff 0%, #f8f3ea 62%, #ecdfc6 100%); color: #1c1206; }
      #root, #root * { font-family: 'Inter', sans-serif !important; }
      .swoosh { position: absolute; left: -300px; top: -300px; width: 1680px; height: 2520px; }
      .orb { display: none; }
      .sm { font-weight: 600; color: #1c1206; }
      .big { font-weight: 900; letter-spacing: -0.045em; color: #f29a0e; text-shadow: 0 6px 0 #9c5200, 0 18px 30px rgba(60,30,0,0.25); }
      .ext { font-weight: 900; letter-spacing: -0.05em; color: #f29a0e; text-shadow: 0 3px 0 #d47c00, 0 6px 0 #b86600, 0 9px 0 #9c5200, 0 12px 0 #7f4300, 0 30px 40px rgba(60,30,0,0.3); }
      .y { color: #f29a0e; font-weight: 800; }
      .eyebrow { font-weight: 800; color: #c66f00; }
      .obj { filter: drop-shadow(0 26px 34px rgba(60,30,0,0.28)); }
      .phone { background: #111; border: 16px solid #111; box-shadow: 0 40px 70px rgba(0,0,0,0.25); }
      .num { background: #1c1206; color: #ffd60a; font-weight: 900; box-shadow: 0 16px 30px rgba(0,0,0,0.3); }
      .ttl { font-weight: 900; color: #1c1206; letter-spacing: -0.045em; }
      .card, .vcard, .deal { background: #fff; border: 3px solid #eadfcb; box-shadow: 0 18px 36px rgba(60,30,0,0.12) !important; }
      .vcard { border: 10px solid #fff; }
      #c2b, #cb { border: 10px solid #fff !important; box-shadow: 0 0 0 6px #f29a0e, 0 30px 60px rgba(60,30,0,0.3) !important; }
      .txtl { background: #e8dcc6; }
      .fix, .stamp, .chip { font-weight: 900; background: linear-gradient(180deg, #ffe14d, #ffcc00); color: #2a1a00; box-shadow: 0 12px 0 #c99a00, 0 26px 40px rgba(60,30,0,0.25); }
      .chip.alt { background: linear-gradient(180deg, #ff3d7f, #d90f57); color: #fff; border: none; box-shadow: 0 12px 0 #8f0838, 0 26px 40px rgba(60,0,20,0.25); line-height: 130px; }
      .tag, .tag2 { font-weight: 800; }
      .tg { background: linear-gradient(180deg, #ffe14d, #ffcc00); color: #2a1a00; box-shadow: 0 8px 0 #c99a00; }
      .tr { background: linear-gradient(180deg, #ff3d7f, #d90f57); color: #fff; box-shadow: 0 8px 0 #8f0838; }
      .deal b { color: #1c1206; font-weight: 900; } .deal span { color: #c66f00; font-weight: 800; }
      .pol { box-shadow: 0 30px 60px rgba(60,30,0,0.25); }
      #ph { background: #111; border: 18px solid #111; box-shadow: 0 40px 70px rgba(0,0,0,0.25); }
      #hd { background: #008069; }
      #hd b { color: #fff; font-weight: 800; } #hd span { color: #d4efe8; }
      #hd .lg { background: #fff; }
      #btn { font-weight: 900; background: linear-gradient(180deg, #ffe14d, #ffcc00); color: #2a1a00; box-shadow: 0 12px 0 #c99a00, 0 26px 40px rgba(60,30,0,0.25); }
      .fix { font-size: 52px; }
      #numb { top: 1675px; left: 190px; width: 700px; height: 100px; border-radius: 50px; background: #1a9e4b; color: #fff; font-weight: 800; font-size: 50px; line-height: 100px; box-shadow: 0 14px 30px rgba(0,0,0,0.18); }
      #wm { color: #1c1206; text-shadow: none; font-weight: 900; letter-spacing: 0.04em; font-size: 32px; top: 1806px; }
      #wm img { width: 70px; height: 72px; }
      #bug { color: #1c1206; text-shadow: none; font-weight: 900; padding: 8px 22px 8px 10px; border-radius: 999px; background: rgba(255,255,255,0.88); box-shadow: 0 8px 20px rgba(60,30,0,0.15); font-size: 32px; opacity: 1; }
      #bug img { width: 54px; height: 56px; }
      #demo { background: rgba(255,255,255,0.92); color: #c66f00; border: none; box-shadow: 0 8px 20px rgba(0,0,0,0.2); font-weight: 800; }
      #logoici { background: rgba(255,255,255,0.88); border-color: #f29a0e; color: #f29a0e; font-weight: 900; }
      #iris { background: #f29a0e; }
      #fade { background: #ffffff; }
"""
SWOOSH = ('<svg class="swoosh" viewBox="0 0 1680 2520"><path d="M1500 -100 C 900 800, 700 1300, 200 2600" fill="none" stroke="#efe6d6" stroke-width="230" stroke-linecap="round"/>'
          '<path d="M1700 900 C 1300 1500, 1100 2000, 900 2700" fill="none" stroke="#f3ecdf" stroke-width="160" stroke-linecap="round"/></svg>')
OLD_SVG = re.compile(r'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120".*?</svg>', re.S)

for d in sys.argv[1:]:
    p = os.path.join(d, "index.html"); s = open(p).read()
    if "D.A. claire" in s:
        print(d, "déjà fait"); continue
    os.makedirs(os.path.join(d, "assets", "fonts"), exist_ok=True)
    for f in ("inter-latin-600-normal.woff2", "inter-latin-800-normal.woff2", "inter-latin-900-normal.woff2"):
        shutil.copy(os.path.join(FONTS, f), os.path.join(d, "assets", "fonts", f))
    for f in ("logo-icone-v2.svg", "photo-profil-v2.png"):
        shutil.copy(os.path.join(HERE, "marque", f), os.path.join(d, "assets", "img", f))
    s = s.replace("    </style>", CSS + "    </style>", 1)
    s = s.replace('<div class="grid"></div>', SWOOSH, 1)
    s = OLD_SVG.sub('<img src="assets/img/logo-icone-v2.svg" alt="" />', s)
    s = s.replace("assets/img/photo-profil.png", "assets/img/photo-profil-v2.png")
    assert "logo-icone-v2" in s and "swoosh" in s, d
    open(p, "w").write(s); print(d, "ok")
