"""Fabrique le PDF « Guide vidéo » : une page par vidéo, avec une image cliquable.

Les liens des vidéos sont dans liens.json :
- tant qu'une adresse commence par « fichier: », la vidéo est glissée DANS le PDF (pièce jointe
  posée sur l'image : elle s'ouvre avec Adobe Acrobat, sur téléphone comme sur ordinateur) ;
- dès que Mike met une vraie adresse (YouTube en « non répertoriée », par exemple), l'image devient
  un lien normal, qui marche dans toutes les applications.

Utilisation : python3 build_pdf.py
"""
import html, json, os, subprocess
import pymupdf as fitz  # PyMuPDF

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
E = html.escape
LIENS = json.load(open(os.path.join(HERE, "liens.json")))
WA = "https://wa.me/243831710181?text=" + "Bonjour%20Mike%2C%20je%20suis%20dans%20le%20guide%20vid%C3%A9o.%20Voici%20o%C3%B9%20j%27en%20suis%20%3A%20"

PAGES = [
    ("v0", "Bienvenue", "Avant de commencer", 4.5,
     ["Ce guide a un seul but : transformer ce que tu sais déjà faire en un produit que quelqu'un paie.",
      "4 étapes : casser le mythe, trouver ta compétence, choisir ton format, tester en 7 jours.",
      "Pas besoin de payer de la publicité pour commencer."],
     ["Prends une feuille et un stylo", "Garde ce PDF ouvert à côté du guide"]),
    ("v1", "Le mythe à casser", "Chapitre 1", 3.2,
     ["Pas besoin d'un diplôme rare, de savoir coder, de parler anglais couramment ou d'un talent spécial.",
      "On ne vend presque jamais un talent rare : on vend la solution à un problème précis.",
      "Ce que tu fais déjà, mieux que les gens autour de toi, peut devenir un petit guide, une checklist ou une courte formation."],
     ["Note 3 choses que tu fais sans y penser", "Note 3 choses qu'on te demande souvent"]),
    ("v2", "Trouve ta compétence vendable", "Chapitre 2", 3.2,
     ["Qu'est-ce que les gens autour de moi me demandent souvent ?",
      "Qu'est-ce que je pourrais expliquer à quelqu'un qui part de zéro ?",
      "Pour quoi est-ce qu'on m'appelle, moi, quand on est bloqué ?"],
     ["Écris 3 réponses à chaque question (9 lignes)", "Entoure celle qui revient le plus souvent", "Ou celle pour laquelle on t'a déjà dit merci, ou payé"]),
    ("v3", "Choisis ton format", "Chapitre 3", 3.2,
     ["Pas besoin d'un site, d'une application ni d'heures de montage.",
      "4 formats simples : le mini-guide, le modèle prêt à remplir, la checklist, la capsule vidéo.",
      "Pour ton premier produit, prends le plus rapide à faire. Pas parfait : prêt cette semaine."],
     ["Choisis ton format", "Écris le titre de ton produit"]),
    ("v4", "Le test en 7 jours", "Chapitre 4", 3.2,
     ["Jours 1 et 2 : ton offre en une phrase. « J'aide [telle personne] à obtenir [tel résultat] grâce à [ma compétence]. »",
      "Jour 3 : un message à 10 ou 15 proches. Jours 4 et 5 : ta phrase en statut. Jour 6 : un petit prix.",
      "Jour 7 : le bilan. Personne ne réagit ? C'est une information : change d'angle."],
     ["Écris ta phrase d'offre aujourd'hui", "Envoie ton premier message demain", "Note chaque « oui »"]),
    ("v5", "Et après ?", "La suite", 5.0,
     ["Tu sais trouver ta compétence, choisir ton format et tester ton idée en une semaine.",
      "Le vrai travail commence : vendre encore et encore, te faire connaître, construire un revenu qui tient.",
      "Un premier résultat, même petit ? Tu es prêt pour la suite."],
     ["Écris-moi sur WhatsApp : ta compétence, ta phrase, ton test"]),
]


def dur(v):
    p = os.path.join(ROOT, v, "renders", f"{v}.mp4")
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p], capture_output=True, text=True).stdout
    return float(out or 0)


def thumbs():
    for v, *_r in PAGES:
        at = [p for p in PAGES if p[0] == v][0][3]
        src = os.path.join(ROOT, v, "renders", f"{v}.mp4")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(at), "-i", src, "-frames:v", "1", "-vf", "scale=1280:-2", "-q:v", "3", os.path.join(HERE, f"miniature_{v}.jpg")], check=True)


def page_html():
    toc = "".join(f'<a href="#{v}"><div class="n">{k}</div><div><b>{E(t)}</b><span>{E(c)} · vidéo de {int(round(dur(v)))} s</span></div><i>Voir ▸</i></a>' for k, (v, t, c, *_r) in enumerate(PAGES))
    pages = []
    for k, (v, t, c, _at, ret, todo) in enumerate(PAGES):
        href = LIENS[v] if not LIENS[v].startswith("fichier:") else f"https://video.local/{v}"
        pages.append(f"""
<section class="page" id="{v}">
  <div class="tag">Vidéo {k} · {E(c)}</div>
  <h2>{E(t)}</h2>
  <a class="video" href="{E(href)}"><img src="miniature_{v}.jpg" alt=""><div class="play"></div><div class="cap">▶ Regarder la vidéo ({int(round(dur(v)))} s)</div></a>
  <div class="box"><h3>Ce que tu retiens</h3>{''.join(f'<p class="li">{E(x)}</p>' for x in ret)}</div>
  <div class="todo"><h3>À faire</h3>{''.join(f'<div>{E(x)}</div>' for x in todo)}</div>
  <a class="btn g" href="{WA}">Une question ? <small>Écris-moi sur WhatsApp</small></a>
  <a class="back" href="#sommaire">◂ Sommaire</a><span class="num">{k + 3}</span>
</section>""")
    return f"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><title>Guide vidéo · Gagne ta vie sans diplôme</title>
<style>
  @font-face {{ font-family: 'Baloo'; font-weight: 800; src: url('Baloo2-ExtraBold.ttf'); }}
  @font-face {{ font-family: 'Work Sans'; font-weight: 400; src: url('worksans-400.ttf'); }}
  @font-face {{ font-family: 'Work Sans'; font-weight: 700; src: url('worksans-700.ttf'); }}
  @page {{ size: 148mm 210mm; margin: 0; }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: 'Work Sans', sans-serif; color: #141414; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
  .page {{ width: 148mm; height: 210mm; padding: 13mm 12mm 12mm; position: relative; overflow: hidden; page-break-after: always; background: #fff;
    background-image: linear-gradient(rgba(0,0,0,.035) .3mm, transparent .3mm), linear-gradient(90deg, rgba(0,0,0,.035) .3mm, transparent .3mm); background-size: 8mm 8mm; }}
  .page:last-child {{ page-break-after: auto; }}
  h1, h2, h3 {{ font-family: 'Baloo', sans-serif; font-weight: 800; line-height: 1.05; }}
  h2 {{ font-size: 22pt; margin-bottom: 3mm; color: #ff3d1f; }}
  h3 {{ font-size: 12pt; margin-bottom: 1.5mm; }}
  p {{ font-size: 10pt; line-height: 1.45; margin-bottom: 2mm; }}
  a {{ text-decoration: none; color: inherit; }}
  .tag {{ display: inline-block; font-weight: 700; font-size: 8.5pt; letter-spacing: 1.5pt; text-transform: uppercase; color: #ff3d1f; margin-bottom: 1.5mm; }}
  .btn {{ display: block; border-radius: 4mm; padding: 3.5mm 5mm; font-weight: 700; font-size: 11pt; margin-top: 3mm; }}
  .btn small {{ font-weight: 400; font-size: 9pt; opacity: .9; margin-left: 2mm; }}
  .btn.g {{ background: #1a9e4b; color: #fff; }}
  .btn.r {{ background: #ff3d1f; color: #fff; text-align: center; }}
  .back {{ position: absolute; left: 12mm; bottom: 7mm; font-size: 8.5pt; font-weight: 700; color: #8a8a8a; }}
  .num {{ position: absolute; right: 12mm; bottom: 7mm; font-size: 8.5pt; color: #8a8a8a; }}
  .video {{ display: block; position: relative; border-radius: 4mm; overflow: hidden; margin: 1mm 0 3.5mm; box-shadow: 0 2mm 5mm rgba(0,0,0,.2); border: .8mm solid #fff; }}
  .video img {{ display: block; width: 100%; height: 66mm; object-fit: cover; }}
  .video .play {{ position: absolute; left: 87%; top: 22%; width: 18mm; height: 18mm; margin: -9mm 0 0 -9mm; border-radius: 50%; background: #ff3d1f; border: 1.2mm solid #fff; box-shadow: 0 1mm 4mm rgba(0,0,0,.35); }}
  .video .play:after {{ content: ""; position: absolute; left: 6.6mm; top: 4.6mm; border-left: 6.5mm solid #fff; border-top: 4.2mm solid transparent; border-bottom: 4.2mm solid transparent; }}
  .video .cap {{ position: absolute; left: 0; right: 0; bottom: 0; padding: 2.3mm 4mm; background: rgba(20,20,20,.82); color: #fff; font-weight: 700; font-size: 9.5pt; }}
  .box {{ background: #fff; border: .4mm solid #e6e1d9; border-radius: 4mm; padding: 3.5mm 4mm 2mm; margin-bottom: 3mm; }}
  .li {{ position: relative; padding-left: 5mm; font-size: 9.3pt; margin-bottom: 1.4mm; }}
  .li:before {{ content: ""; position: absolute; left: 0; top: 1.6mm; width: 2.4mm; height: 2.4mm; border-radius: 50%; background: #ff3d1f; }}
  .todo {{ background: #fff8ec; border: .4mm solid #f3dfb8; border-radius: 4mm; padding: 3.5mm 4mm; }}
  .todo div {{ font-size: 10pt; padding: 1.1mm 0 1.1mm 7mm; position: relative; }}
  .todo div:before {{ content: ""; position: absolute; left: 0; top: 1.4mm; width: 4mm; height: 4mm; border: .5mm solid #141414; border-radius: 1mm; background: #fff; }}
  .cover h1 {{ font-size: 33pt; margin: 3mm 0 3mm; }}
  .cover h1 span {{ color: #ff3d1f; }}
  .cover .me {{ display: block; width: 56mm; height: 56mm; border-radius: 50%; object-fit: cover; margin: 9mm auto 4mm; border: 1.6mm solid #fff; box-shadow: 0 0 0 1.2mm #ff3d1f, 0 3mm 6mm rgba(0,0,0,.25); }}
  .cover .who {{ text-align: center; font-weight: 700; font-size: 10.5pt; }}
  .cover .btn {{ position: absolute; left: 12mm; right: 12mm; bottom: 20mm; }}
  .brand {{ position: absolute; left: 12mm; right: 12mm; bottom: 9mm; font-size: 8.5pt; color: #8a8a8a; text-align: center; }}
  .toc a {{ display: flex; align-items: center; gap: 3.5mm; background: #fff; border: .4mm solid #e6e1d9; border-radius: 4mm; padding: 3mm 3.5mm; margin-bottom: 2.6mm; }}
  .toc .n {{ flex: 0 0 11mm; height: 11mm; border-radius: 50%; background: #ff3d1f; color: #fff; font-family: 'Baloo'; font-size: 17pt; text-align: center; line-height: 12mm; }}
  .toc b {{ display: block; font-size: 11pt; }}
  .toc span {{ font-size: 8.8pt; color: #666; }}
  .toc i {{ margin-left: auto; font-style: normal; font-weight: 700; color: #ff3d1f; font-size: 9pt; white-space: nowrap; }}
  .legend {{ margin-top: 3mm; font-size: 8.8pt; color: #666; }}
  .end .me {{ display: block; width: 44mm; height: 44mm; border-radius: 50%; object-fit: cover; margin: 8mm auto 5mm; border: 1.4mm solid #fff; box-shadow: 0 0 0 1mm #1a9e4b, 0 3mm 6mm rgba(0,0,0,.25); }}
</style></head>
<body>
<section class="page cover" id="couverture">
  <div class="tag">Guide vidéo</div>
  <h1>Gagne ta vie <span>sans diplôme</span></h1>
  <p>6 vidéos courtes, une pour chaque étape du guide. Touche une image avec le bouton rouge pour regarder la vidéo, puis fais l'exercice de la page.</p>
  <img class="me" src="mike.jpg" alt="">
  <div class="who">Mike · DigitalMikaelson</div>
  <a class="btn r" href="#sommaire">Commencer ▸</a>
  <div class="brand">Pas de blabla, juste ce qu'il faut faire, concrètement.</div>
</section>
<section class="page" id="sommaire">
  <div class="tag">Sommaire</div>
  <h2>Les 6 vidéos</h2>
  <div class="toc">{toc}</div>
  <p class="legend">▶ Les images avec un bouton rouge ouvrent la vidéo. Les boutons verts ouvrent WhatsApp.</p>
  <span class="num">2</span>
</section>
{''.join(pages)}
<section class="page end" id="fin">
  <div class="tag">Et maintenant</div>
  <h2>Dis-moi où tu en es</h2>
  <p>Ta compétence, ta phrase d'offre, le résultat de ton test : écris-moi sur WhatsApp. Je te lis, et je t'accompagne pour l'étape suivante.</p>
  <img class="me" src="mike.jpg" alt="">
  <a class="btn g" href="{WA}">Écrire à Mike sur WhatsApp <small>+243 831 710 181</small></a>
  <a class="back" href="#sommaire">◂ Sommaire</a><span class="num">{len(PAGES) + 3}</span>
</section>
</body></html>"""


def build():
    thumbs()
    tmp = os.path.join(HERE, "_build.html")
    open(tmp, "w").write(page_html())
    raw = os.path.join(HERE, "_brut.pdf")
    subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=4000",
                    f"--print-to-pdf={raw}", "file://" + tmp], check=True, capture_output=True)
    os.remove(tmp)
    doc = fitz.open(raw)
    joints = 0
    for page in doc:
        for ln in page.get_links():
            uri = ln.get("uri", "")
            if not uri.startswith("https://video.local/"):
                continue
            v = uri.rsplit("/", 1)[1]
            fich = LIENS[v].split(":", 1)[1]
            data = open(os.path.join(ROOT, fich), "rb").read()
            r = ln["from"]
            page.delete_link(ln)
            an = page.add_file_annot(r.tl + (r.width / 2 - 10, r.height / 2 - 10), data, f"video_{v}.mp4", desc=f"Vidéo {v}", icon="Paperclip")
            an.set_opacity(0.01)
            an.update()
            # toute l'image devient la zone à toucher (PyMuPDF garde l'icône à 20 pt, on élargit le /Rect à la main)
            h = page.rect.height
            doc.xref_set_key(an.xref, "Rect", f"[{r.x0:.2f} {h - r.y1:.2f} {r.x1:.2f} {h - r.y0:.2f}]")
            joints += 1
    out = os.path.join(HERE, "guide_video_gagne_ta_vie.pdf")
    doc.save(out, garbage=3, deflate=True)
    os.remove(raw)
    print("ok", out, f"{os.path.getsize(out) / 1e6:.1f} Mo", joints, "vidéo(s) glissée(s) dans le PDF")


if __name__ == "__main__":
    build()
