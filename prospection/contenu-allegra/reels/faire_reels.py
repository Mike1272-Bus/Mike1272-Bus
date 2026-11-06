"""Transforme les vidéos « statut WhatsApp » en Reels Instagram / Facebook :
fin adaptée aux réseaux (commentaire ou message privé, pas de téléphone WhatsApp), textes gardés dans la zone visible,
petit logo du haut retiré (l'en-tête Reels le recouvre). Usage : python3 faire_reels.py"""
import os, re, shutil

HERE = os.path.dirname(os.path.abspath(__file__)); BASE = os.path.dirname(HERE)
REELS = [  # dossier source, dossier Reel, mode de fin
    ("mar13-burger", "r1-mar13-apres-midi-burger", "commentaire"),
    ("mar13-essai", "r2-mar13-soir-essai", "message"),
    ("mer14-transformations", "r3-mer14-apres-midi-transformations", "commentaire"),
    ("mer14-demo-pizza", "r4-mer14-soir-pizza", "message"),
]
CSS = """
      /* ===== fin de Reel (Instagram / Facebook) ===== */
      .ig { position: absolute; left: 120px; width: 840px; border-radius: 40px; background: #fff; border: 3px solid #eadfcb; box-shadow: 0 18px 36px rgba(60,30,0,0.14); padding: 30px 34px; }
      .ig .hd { font-weight: 800; font-size: 28px; color: #8a7a66; letter-spacing: 0.02em; margin-bottom: 26px; }
      .ig .row { position: relative; min-height: 96px; padding-left: 104px; margin-bottom: 26px; }
      .ig .av { position: absolute; left: 0; top: 0; width: 80px; height: 80px; border-radius: 50%; background: #e8dcc6; }
      .ig .av img { width: 100%; height: 100%; border-radius: 50%; }
      .ig .nm { font-weight: 800; font-size: 30px; color: #1c1206; }
      .ig .tx { font-weight: 600; font-size: 36px; color: #1c1206; margin-top: 6px; white-space: nowrap; }
      .ig .typ { position: relative; height: 50px; }
      .ig .typ span { position: absolute; left: 0; top: 0; }
      .ig .rep { margin-left: 70px; }
      .ig .rep .tx { white-space: normal; font-size: 32px; line-height: 1.3; }
      .bigpill { position: absolute; left: 90px; width: 900px; height: 140px; border-radius: 70px; text-align: center; line-height: 140px; font-weight: 900; font-size: 66px; white-space: nowrap;
        background: linear-gradient(180deg, #ffe14d, #ffcc00); color: #2a1a00; box-shadow: 0 12px 0 #c99a00, 0 26px 40px rgba(60,30,0,0.25); }
      .sub { position: absolute; left: 0; width: 1080px; text-align: center; font-weight: 800; font-size: 32px; letter-spacing: 0.12em; text-transform: uppercase; color: #c66f00; }
"""
TXT = {
    "commentaire": dict(l1="Vous voulez", l2="la vôtre ?", hd="Commentaires", word="VIDÉO",
                        rep="Merci ! On vous écrit en message privé 📩", pill="Commentez « VIDÉO »", sub="on vous répond en privé"),
    "message": dict(l1="Votre vidéo", l2="d'essai gratuite", hd="Messages", word="ESSAI",
                    rep="Avec plaisir ! Envoyez-nous 3 photos de votre produit 📸", pill="Écrivez « ESSAI » en privé", sub="5 places cette semaine"),
}

def cta_html(s, k, t):
    return f'''      <!-- Fin du Reel : {t["pill"]} -->
      <div class="scene" id="{s}"><div class="cam" id="{k}">
        <div class="line" style="top:270px"><span class="w sm" id="z1">{t["l1"]}</span></div>
        <div class="line" style="top:360px" data-layout-allow-overlap><span class="w ext" id="z2" style="font-size:{150 if len(t["l2"]) < 12 else 118}px">{t["l2"]}</span></div>
        <div class="ig" id="z3" style="top:600px">
          <div class="hd">{t["hd"]}</div>
          <div class="row"><div class="av"></div><div class="nm">Vous</div><div class="tx typ"><span id="z4">{t["word"]}</span></div></div>
          <div class="row rep" id="z5"><div class="av"><img src="assets/img/photo-profil-v2.png" alt="" /></div><div class="nm">Allegra Digital</div><div class="tx">{t["rep"]}</div></div>
        </div>
        <div class="bigpill" id="z6" style="top:1130px">{t["pill"]}</div>
        <div class="sub" id="z7" style="top:1310px">{t["sub"]}</div>
      </div></div>

'''

def cta_js(t0, dur):
    return f'''      // fin du Reel
      word("#z1", {t0 + 0.1:.2f});
      IN("#z2", {{ y: -300, scale: 1.4 }}, {{ y: 0, scale: 1, duration: 0.5, ease: "bounce.out" }}, {t0 + 0.35:.2f});
      IN("#z3", {{ y: 900 }}, {{ y: 0, duration: 0.5, ease: "expo.out" }}, {t0 + 0.2:.2f});
      IN("#z4", {{ scale: 0.4, x: -40 }}, {{ scale: 1, x: 0, duration: 0.35, ease: "back.out(2.2)" }}, {t0 + 0.9:.2f});
      IN("#z5", {{ y: 120, scale: 0.8, transformOrigin: "0% 0%" }}, {{ y: 0, scale: 1, duration: 0.4, ease: "back.out(1.8)" }}, {t0 + 1.6:.2f});
      IN("#z6", {{ scale: 0.3 }}, {{ scale: 1, duration: 0.45, ease: "back.out(2.5)" }}, {t0 + 2.5:.2f});
      FT("#z6", {{ scale: 1 }}, {{ scale: 1.05, duration: 0.25, yoyo: true, repeat: 3, ease: "sine.inOut" }}, {t0 + 3.1:.2f});
      word("#z7", {t0 + 2.8:.2f}, 0.3);
      FT("#fade", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.3 }}, {dur - 0.3:.2f});
'''

for src, dst, mode in REELS:
    d = os.path.join(HERE, dst)
    if os.path.exists(d): shutil.rmtree(d)
    shutil.copytree(os.path.join(BASE, src), d, ignore=shutil.ignore_patterns("renders", "snapshots"))
    m = os.path.join(d, "mix.py"); open(m, "w").write(open(m).read().replace('ROOT, "..", "..", "..", "video-excel-13h"', 'ROOT, "..", "..", "..", "..", "video-excel-13h"'))
    p = os.path.join(d, "index.html"); s = open(p).read()
    dur = float(re.search(r'data-duration="([\d.]+)" data-width', s).group(1))
    # 1. la scène qui contient le téléphone WhatsApp
    scenes = list(re.finditer(r'<div class="scene" id="(s\d)"><div class="cam" id="(k\d)">', s))
    for i, m in enumerate(scenes):
        end = scenes[i + 1].start() if i + 1 < len(scenes) else s.index('<div class="ab" id="bug">')
        if 'id="ph"' in s[m.start():end]: break
    sid, kid = m.group(1), m.group(2)
    a = s.rfind("<!--", 0, m.start()); a = s.rfind("\n", 0, a) + 1
    end = s.rfind("</div></div>", m.start(), end) + len("</div></div>\n")
    t0 = float(re.search(rf'\["#{sid}", "#{kid}", ([\d.]+),', s).group(1))
    s = s[:a] + cta_html(sid, kid, TXT[mode]) + s[end:].lstrip("\n")
    # 2. petit logo du haut retiré (caché par l'en-tête Reels)
    s = re.sub(r'\s*<div class="ab" id="bug">.*?</div>\n', "\n", s, count=1, flags=re.S)
    # 3. animations de fin remplacées
    lines = s.split("\n"); i0 = next(i for i, l in enumerate(lines) if "appel à l'action" in l and l.strip().startswith("//"))
    i1 = next(i for i, l in enumerate(lines) if l.strip().startswith("gsap.set(HIDE"))
    lines[i0:i1] = [l for l in lines[i0:i1] if '"#fade"' in l and False] + cta_js(t0, dur).rstrip("\n").split("\n")
    s = "\n".join(lines).replace("    </style>", CSS + "    </style>", 1)
    open(p, "w").write(s)
    print(dst, "fin à", t0, "s, durée", dur)
