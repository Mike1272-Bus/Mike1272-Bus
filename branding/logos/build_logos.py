"""Pistes de logo DigitalMikaelson : SVG individuels + planche de présentation."""
import os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
NAVY, GOLD, BLUE, CYAN = "#201f5b", "#f7c21b", "#1f8fd1", "#6fd3f5"
STAR = "M50 {t} C{a} {b} {c} {d} {r} 50 C{c} {e} {a} {f} 50 {btm} C{g} {f} {h} {e} {l} 50 C{h} {d} {g} {b} 50 {t} Z"

def star(cx, cy, s):
    # étoile 4 branches centrée en (cx, cy), rayon s
    k = lambda v: round(v, 2)
    return (f"M{k(cx)} {k(cy-s)} C{k(cx+s*.1)} {k(cy-s*.27)} {k(cx+s*.27)} {k(cy-s*.1)} {k(cx+s)} {k(cy)} "
            f"C{k(cx+s*.27)} {k(cy+s*.1)} {k(cx+s*.1)} {k(cy+s*.27)} {k(cx)} {k(cy+s)} "
            f"C{k(cx-s*.1)} {k(cy+s*.27)} {k(cx-s*.27)} {k(cy+s*.1)} {k(cx-s)} {k(cy)} "
            f"C{k(cx-s*.27)} {k(cy-s*.1)} {k(cx-s*.1)} {k(cy-s*.27)} {k(cx)} {k(cy-s)} Z")

# chaque piste : (id, nom, idée, fonction(ink, accent, soft, paper) -> contenu SVG)
LOGOS = [
    ("etincelle", "L'Étincelle",
     "L'idée qui s'allume : ton savoir-faire devient une valeur. Reprend les étoiles déjà présentes dans tous tes visuels, donc la marque se reconnaît tout de suite.",
     lambda ink, acc, soft, paper: f'<circle cx="50" cy="50" r="44" fill="{ink}"/><path d="{star(47, 53, 26)}" fill="{acc}"/><path d="{star(71, 28, 8)}" fill="{soft}"/>'),
    ("telephone", "Le Téléphone-guide",
     "Un téléphone qui contient un document : tout se fait avec ton téléphone, et ce qui en sort est un produit. Lisible même tout petit.",
     lambda ink, acc, soft, paper: f'<rect x="27" y="10" width="46" height="80" rx="11" fill="none" stroke="{ink}" stroke-width="6"/><line x1="44" y1="20" x2="56" y2="20" stroke="{ink}" stroke-width="4" stroke-linecap="round"/><path d="M38 32 H55 L63 40 V70 Q63 73 60 73 H41 Q38 73 38 70 Z" fill="{acc}"/><path d="M55 32 V40 H63" fill="none" stroke="{ink}" stroke-width="3" stroke-linejoin="round"/><line x1="44" y1="52" x2="57" y2="52" stroke="{ink}" stroke-width="3.5" stroke-linecap="round"/><line x1="44" y1="61" x2="53" y2="61" stroke="{ink}" stroke-width="3.5" stroke-linecap="round"/>'),
    ("monogramme", "Le Monogramme DM",
     "Les initiales D et M imbriquées : le M se lit en creux dans le D. Sérieux et professionnel, comme une marque de formation.",
     lambda ink, acc, soft, paper: f'<path d="M20 14 H46 C69 14 84 30 84 50 C84 70 69 86 46 86 H20 Z" fill="{ink}"/><polyline points="33,66 33,35 47,53 61,35 61,66" fill="none" stroke="{paper}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><circle cx="84" cy="16" r="7" fill="{acc}"/>'),
    ("croissance", "La Croissance",
     "Trois barres qui montent dans un téléphone : tes premiers revenus grandissent, étape par étape. Parle directement de gagner sa vie.",
     lambda ink, acc, soft, paper: f'<rect x="24" y="10" width="52" height="80" rx="12" fill="{ink}"/><rect x="34" y="56" width="9" height="20" rx="3" fill="{soft}"/><rect x="46" y="44" width="9" height="32" rx="3" fill="{BLUE if ink == NAVY else CYAN}"/><rect x="58" y="28" width="9" height="48" rx="3" fill="{acc}"/>'),
    ("m-fleche", "Le M qui monte",
     "Un M dont la dernière branche devient une flèche vers le haut : Mikaelson et la progression dans une seule forme.",
     lambda ink, acc, soft, paper: f'<polyline points="16,82 16,34 40,62 62,36" fill="none" stroke="{ink}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/><line x1="62" y1="36" x2="84" y2="14" stroke="{acc}" stroke-width="9" stroke-linecap="round"/><polyline points="66,14 84,14 84,32" fill="none" stroke="{acc}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>'),
    ("bulle", "La Bulle d'idée",
     "Une bulle de conversation avec une étincelle : l'accompagnement sur WhatsApp, là où tout se passe avec tes clients.",
     lambda ink, acc, soft, paper: f'<path d="M20 16 H80 Q88 16 88 24 V64 Q88 72 80 72 H44 L28 86 V72 H20 Q12 72 12 64 V24 Q12 16 20 16 Z" fill="{ink}"/><path d="{star(50, 44, 19)}" fill="{acc}"/>'),
    ("transformation", "La Transformation",
     "Un point, puis un contour, puis un bloc plein : un savoir-faire qui prend forme jusqu'à devenir un produit. Le plus conceptuel des sept.",
     lambda ink, acc, soft, paper: f'<circle cx="18" cy="62" r="6" fill="{ink}"/><rect x="33" y="44" width="24" height="24" rx="7" fill="none" stroke="{ink}" stroke-width="5"/><rect x="64" y="30" width="30" height="38" rx="8" fill="{acc}"/><line x1="72" y1="44" x2="86" y2="44" stroke="{ink}" stroke-width="3.5" stroke-linecap="round"/><line x1="72" y1="53" x2="82" y2="53" stroke="{ink}" stroke-width="3.5" stroke-linecap="round"/>'),
]

def svg(body, size=None):
    s = f' width="{size}" height="{size}"' if size else ""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"{s}>{body}</svg>'

LIGHT = (NAVY, GOLD, CYAN, "#ffffff")
DARK = ("#ffffff", GOLD, CYAN, NAVY)

os.makedirs(os.path.join(HERE, "svg"), exist_ok=True)
cards = []
for i, (lid, name, idea, fn) in enumerate(LOGOS, 1):
    open(os.path.join(HERE, "svg", f"{i}_{lid}.svg"), "w").write(svg(fn(*LIGHT)))
    open(os.path.join(HERE, "svg", f"{i}_{lid}_fond_bleu.svg"), "w").write(svg(fn(*DARK)))
    cards.append(f"""
<div class="card">
  <div class="num">{i}</div>
  <div class="row">
    <div class="tile light">{svg(fn(*LIGHT))}</div>
    <div class="tile dark">{svg(fn(*DARK))}</div>
    <div class="tiny"><div class="t32">{svg(fn(*LIGHT), 32)}</div><div class="t32 d">{svg(fn(*DARK), 32)}</div><span>taille icône</span></div>
  </div>
  <div class="lock"><div class="li">{svg(fn(*LIGHT))}</div><div><div class="wm"><span class="d">Digital</span>Mikaelson</div><div class="tag">PRODUITS DIGITAUX</div></div></div>
  <h2>{name}</h2>
  <p>{idea}</p>
</div>""")

html = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face {{ font-family: 'Baloo 2'; font-weight: 800; src: url('Baloo2-ExtraBold.ttf'); }}
@font-face {{ font-family: 'Work Sans'; font-weight: 700; src: url('worksans-700.ttf'); }}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ width: 1080px; background: #f4f3fa; font-family: 'Work Sans'; font-weight: 700; color: {NAVY}; }}
header {{ background: {NAVY}; color: #fff; padding: 60px 60px 50px; }}
header h1 {{ font-family: 'Baloo 2'; font-size: 64px; line-height: 1; }}
header h1 span {{ color: {GOLD}; }}
header p {{ margin-top: 14px; font-size: 24px; color: #cfd3ff; }}
.grid {{ padding: 40px 40px 60px; display: grid; grid-template-columns: 1fr 1fr; gap: 30px; }}
.card {{ position: relative; background: #fff; border-radius: 30px; padding: 30px; box-shadow: 0 10px 30px rgba(32,31,91,.1); }}
.num {{ position: absolute; right: 24px; top: 20px; font-family: 'Baloo 2'; font-size: 30px; color: {GOLD}; }}
.row {{ display: flex; gap: 16px; align-items: flex-end; }}
.tile {{ width: 170px; height: 170px; border-radius: 22px; display: flex; align-items: center; justify-content: center; }}
.tile svg {{ width: 118px; height: 118px; }}
.tile.light {{ background: #f4f3fa; }} .tile.dark {{ background: {NAVY}; width: 110px; height: 110px; }} .tile.dark svg {{ width: 74px; height: 74px; }}
.tiny {{ display: flex; flex-direction: column; gap: 8px; align-items: center; font-size: 13px; color: #8a89a8; }}
.t32 {{ width: 44px; height: 44px; border-radius: 10px; background: #f4f3fa; display: flex; align-items: center; justify-content: center; }}
.t32.d {{ background: {NAVY}; }}
.lock {{ display: flex; align-items: center; gap: 14px; margin-top: 24px; padding: 16px 18px; border: 2px solid #ecebf5; border-radius: 18px; }}
.li svg {{ width: 64px; height: 64px; display: block; }}
.wm {{ font-family: 'Baloo 2'; font-size: 38px; line-height: 1; padding-top: 6px; }}
.wm .d {{ color: {BLUE}; }}
.tag {{ font-size: 13px; letter-spacing: 4px; color: #8a89a8; margin-top: 2px; }}
h2 {{ font-family: 'Baloo 2'; font-size: 32px; margin-top: 20px; line-height: 1.1; }}
p {{ font-size: 18px; line-height: 1.4; color: #4a4970; margin-top: 8px; }}
</style></head><body>
<header><h1>DigitalMikaelson <span>· pistes de logo</span></h1><p>7 propositions aux couleurs de ta marque. Choisis 1 ou 2 favorites, on les affine ensuite.</p></header>
<div class="grid">{''.join(cards)}</div>
</body></html>"""
open(os.path.join(HERE, "planche_logos.html"), "w", encoding="utf-8").write(html)
subprocess.run(["node", os.path.join(HERE, "render.mjs")], check=True)
