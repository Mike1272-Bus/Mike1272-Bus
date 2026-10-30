"""Les 2 bonus du guide « Gagne ta vie sans diplôme », dans la DA du guide (bleu nuit, jaune, Baloo + Work Sans).

  python3 build.py   ->  bonus1_60_idees_produits.pdf  et  bonus2_kit_test_7_jours.pdf
"""
import html, os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
E = html.escape
WA = "https://wa.me/243831710181?text=Bonjour%20Mike%2C%20j%27ai%20une%20question%20sur%20le%20guide%20%C2%AB%20Gagne%20ta%20vie%20sans%20dipl%C3%B4me%20%C2%BB."

CSS = """
@font-face { font-family: 'Baloo'; font-weight: 800; src: url('Baloo2-ExtraBold.ttf'); }
@font-face { font-family: 'Work Sans'; font-weight: 400; src: url('worksans-400.ttf'); }
@font-face { font-family: 'Work Sans'; font-weight: 700; src: url('worksans-700.ttf'); }
@page { size: 148mm 210mm; margin: 0; }
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Work Sans', sans-serif; color: #211e5c; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.page { width: 148mm; height: 210mm; padding: 13mm 12mm 12mm; position: relative; overflow: hidden; page-break-after: always; background: #fbf8f2; }
.page:last-child { page-break-after: auto; }
h1, h2, h3, .h { font-family: 'Baloo', sans-serif; font-weight: 800; line-height: 1.05; }
h2 { font-size: 21pt; margin-bottom: 3mm; }
h2 span, h1 span { background: linear-gradient(transparent 58%, #f7c21a 58%, #f7c21a 92%, transparent 92%); padding: 0 1mm; }
h3 { font-size: 13pt; }
p { font-size: 10pt; line-height: 1.5; margin-bottom: 2.5mm; }
a { text-decoration: none; color: inherit; }
.tag { display: inline-block; font-weight: 700; font-size: 8.3pt; letter-spacing: 1.5pt; text-transform: uppercase; color: #e8553d; margin-bottom: 1.5mm; }
.num { position: absolute; right: 12mm; bottom: 7mm; font-size: 8.5pt; color: #8a8db0; }
.foot { position: absolute; left: 12mm; bottom: 7mm; font-size: 8.5pt; color: #8a8db0; font-weight: 700; }
.btn { display: block; border-radius: 4mm; padding: 3.8mm 5mm; font-weight: 700; font-size: 11pt; margin-top: 3mm; }
.btn small { display: block; font-weight: 400; font-size: 8.8pt; opacity: .9; margin-top: .5mm; }
.btn.y { background: #f7c21a; color: #211e5c; }
.btn.g { background: #1f9d55; color: #fff; }
.cover { background: #211e5c; color: #fff; }
.cover .tag { color: #f7c21a; }
.cover h1 { font-size: 31pt; margin: 4mm 0 4mm; color: #fff; }
.cover h1 span { color: #f7c21a; background: none; padding: 0; }
.cover p { color: #dfe1ff; font-size: 11pt; }
.cover .big { font-family: 'Baloo'; font-size: 96pt; color: #f7c21a; line-height: .8; margin-top: 14mm; }
.cover .ebook { position: absolute; right: 12mm; bottom: 22mm; width: 46mm; border-radius: 2mm; box-shadow: 0 3mm 6mm rgba(0,0,0,.4); transform: rotate(4deg); }
.cover .brand { position: absolute; left: 12mm; bottom: 10mm; font-size: 8.5pt; color: #aab0e6; }
.cover .pill { display: inline-block; background: #5fd0e4; color: #211e5c; font-weight: 700; font-size: 8.5pt; border-radius: 3mm; padding: 1mm 3mm; letter-spacing: 1pt; }
.steps div { display: flex; gap: 3.5mm; align-items: flex-start; background: #fff; border: .45mm solid #211e5c; border-radius: 4mm; padding: 3mm 3.5mm; margin-bottom: 3mm; box-shadow: 1.2mm 1.4mm 0 #f7c21a; }
.steps .n { flex: 0 0 9mm; height: 9mm; border-radius: 50%; background: #211e5c; color: #f7c21a; font-family: 'Baloo'; font-size: 15pt; text-align: center; line-height: 10mm; }
.steps p { margin: 0; font-size: 10pt; }
.metier { background: #fff; border: .45mm solid #211e5c; border-radius: 4.5mm; padding: 3mm 4mm 2mm; margin-bottom: 3.6mm; box-shadow: 1.4mm 1.6mm 0 #f7c21a; position: relative; }
.metier .hd { display: flex; gap: 3mm; align-items: center; margin-bottom: 2mm; }
.metier img { flex: 0 0 12mm; width: 12mm; height: 12mm; }
.metier .k { font-weight: 700; font-size: 8pt; letter-spacing: 1.2pt; text-transform: uppercase; color: #e8553d; }
.metier h3 { margin: .3mm 0 0; font-size: 12pt; }
.metier h3 em { font-style: normal; color: #e8553d; }
.metier ol { list-style: none; counter-reset: i; }
.metier li { counter-increment: i; position: relative; padding-left: 7mm; font-size: 9.6pt; line-height: 1.4; margin-bottom: 1.4mm; }
.metier li:before { content: counter(i); position: absolute; left: 0; top: .2mm; width: 4.8mm; height: 4.8mm; border-radius: 50%; background: #f7c21a; font-family: 'Baloo'; font-size: 9pt; text-align: center; line-height: 5.4mm; }
.box { background: #fff; border: .45mm solid #211e5c; border-radius: 4.5mm; padding: 3.5mm 4mm; margin-bottom: 3.5mm; box-shadow: 1.4mm 1.6mm 0 #f7c21a; }
.box h3 { font-size: 11.5pt; margin-bottom: 1.5mm; }
.msg { background: #dcf8c6; border-radius: 3.5mm 3.5mm 1mm 3.5mm; padding: 2.5mm 3.5mm; font-size: 9.8pt; line-height: 1.45; margin: 1.5mm 0 2.5mm; }
.msg b { color: #e8553d; font-weight: 700; }
.blank { color: #e8553d; font-weight: 700; }
.phrase { font-family: 'Baloo'; font-size: 15pt; line-height: 1.3; text-align: center; padding: 2mm 0; }
.ex { font-size: 9.3pt; padding-left: 5mm; position: relative; margin-bottom: 1.4mm; line-height: 1.4; }
.ex:before { content: ""; position: absolute; left: 0; top: 1.5mm; width: 2.2mm; height: 2.2mm; border-radius: 50%; background: #e8553d; }
table { width: 100%; border-collapse: collapse; font-size: 9pt; background: #fff; }
th { background: #211e5c; color: #fff; font-weight: 700; text-align: left; padding: 2mm 2mm; font-size: 8.6pt; }
td { border-bottom: .3mm solid #d8dbea; padding: 2mm 2mm; vertical-align: top; }
td.c { width: 8mm; text-align: center; }
td.c i { display: inline-block; width: 4.2mm; height: 4.2mm; border: .5mm solid #211e5c; border-radius: 1mm; }
.jr { font-family: 'Baloo'; font-size: 11pt; white-space: nowrap; }
.lines i { display: block; height: 7.5mm; border-bottom: .35mm dashed #a3a6c4; }
"""


def pdf(name, body, title):
    page = f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>{E(title)}</title><style>{CSS}</style></head><body>{body}</body></html>'
    tmp = os.path.join(HERE, "_build.html")
    open(tmp, "w").write(page)
    out = os.path.join(HERE, name)
    subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=4000",
                    f"--print-to-pdf={out}", "file://" + tmp], check=True, capture_output=True)
    os.remove(tmp)
    print("ok", out)


# ------------------------------------------------------------------ bonus 1 : 60 idées
# Les 14 premiers viennent de la série « Ton métier = ton produit », les 6 derniers de sa réserve.
METIERS = [
    ("pot_of_food", "Cuisine", "ceux qui surveillent leur poids", ["Un livre de recettes congolaises plus légères, avec moins d'huile et de sucre.", "Un plan de repas pour la prise de masse, avec des aliments du marché.", "Une liste de courses de la semaine, avec les bonnes portions."]),
    ("wrench", "Mécanique", "les propriétaires de groupes électrogènes", ["Une checklist d'entretien, pour que le groupe dure plus longtemps.", "Un guide des pannes les plus courantes, et de ce qu'il faut vérifier en premier.", "Une fiche pour calculer sa consommation de carburant."]),
    ("globe_with_meridians", "Anglais", "les candidats aux bourses d'études", ["Un guide pour réussir l'entretien de bourse en anglais.", "Un modèle de lettre de motivation en anglais, prêt à adapter.", "Des fiches de vocabulaire pour parler de ses études et de son projet."]),
    ("abacus", "Comptabilité", "les trésoriers de likelemba et d'associations", ["Un modèle de tableau qui calcule les cotisations et les tours tout seul.", "Un guide pour éviter les disputes d'argent dans un groupe.", "Une mini-formation pour présenter des comptes clairs à chaque réunion."]),
    ("thread", "Couture", "les femmes rondes", ["Des patrons de tenues en pagne pour les grandes tailles, en PDF à imprimer.", "Un guide des coupes qui mettent chaque silhouette en valeur.", "Une mini-formation pour adapter un patron standard à toutes les tailles."]),
    ("high_voltage", "Électricité", "les familles qui passent au solaire", ["Un guide pour choisir son panneau et sa batterie selon ce qu'on veut alimenter.", "Une fiche pour calculer la consommation de la maison, appareil par appareil.", "Une checklist des erreurs à éviter avant d'acheter."]),
    ("speech_balloon", "Lingala", "les enfants de la diaspora", ["Des leçons audio courtes, pour apprendre le lingala en famille.", "Un livre de comptines et de chansons en lingala, avec la traduction.", "Des fiches de phrases du quotidien, pour parler aux grands-parents."]),
    ("birthday_cake", "Pâtisserie", "ceux qui n'ont pas de four", ["Un livre de recettes de gâteaux à la casserole, sans four.", "Une mini-formation filmée au téléphone, pour réussir son premier gâteau sans four.", "Une fiche pour calculer le coût d'un gâteau et vendre des parts au bureau ou à l'école."]),
    ("laptop", "Excel", "les candidats aux tests de recrutement des ONG", ["Des exercices Excel du même genre que les tests, avec les corrigés.", "Une mini-formation sur les formules qui reviennent le plus souvent.", "Des modèles de tableaux prêts à l'emploi : budget, suivi d'activités, inventaire."]),
    ("musical_notes", "Chant", "les chorales d'église", ["Des fiches qui séparent chaque chant voix par voix : soprano, alto, ténor, basse.", "Des audios pour que chaque choriste apprenne sa voix à la maison.", "Des exercices de respiration et d'échauffement avant la répétition."]),
    ("camera_with_flash", "Photo au téléphone", "les vendeuses en ligne", ["Une mini-formation pour photographier ses produits avec un fond fait maison.", "Un pack de réglages pour que toutes les photos aient le même style.", "Une checklist pour une séance photo produits réussie."]),
    ("lipstick", "Maquillage", "les maquilleuses qui débutent dans les mariages", ["Un modèle de grille de prix et de contrat pour les mariages.", "Une checklist de tout ce qu'il faut emporter le jour J.", "Un guide pour construire son portfolio avec son téléphone."]),
    ("triangular_ruler", "Maths", "les élèves qui préparent l'Examen d'État", ["Des fiches de révision par chapitre, avec l'essentiel sur une page.", "Des exercices du même genre que ceux de l'examen, avec les corrigés.", "Un planning de révision sur un mois."]),
    ("chicken", "Élevage", "les salariés qui veulent un revenu en plus", ["Un guide pour démarrer un petit élevage de poules pondeuses dans une parcelle.", "Une fiche de suivi de l'alimentation et des vaccins.", "Un calcul simple pour savoir si l'élevage gagne de l'argent."]),
    ("clapper_board", "Montage vidéo", "les églises qui publient leurs prédications", ["Un pack de modèles de titres et de sous-titres, prêts à utiliser.", "Une mini-formation pour monter une prédication avec son téléphone.", "Une checklist pour publier chaque prédication au bon format, sur chaque réseau."]),
    ("artist_palette", "Graphisme (Canva)", "les églises et les organisateurs d'événements", ["Un pack de modèles Canva pour les affiches de culte et d'événements.", "Une mini-formation pour faire une affiche propre avec son téléphone.", "Un kit de visuels pour les réseaux : annonces, programmes, versets du jour."]),
    ("envelope", "Démarches administratives", "la diaspora qui fait des papiers en RDC à distance", ["Un guide des démarches les plus demandées, avec les étapes et les pièces à prévoir.", "Des modèles de lettres et de procurations, prêts à adapter.", "Une checklist pour ne rien oublier avant de lancer une démarche."]),
    ("running_shoe", "Coaching sportif", "ceux qui s'entraînent à la maison sans matériel", ["Un programme de 4 semaines sans matériel, en PDF.", "Des vidéos courtes de chaque exercice, filmées au téléphone.", "Une fiche de suivi pour noter ses séances et ses progrès."]),
    ("droplet", "Plomberie", "les propriétaires qui louent des appartements", ["Une checklist d'entretien de la plomberie entre deux locataires.", "Un guide des petites réparations à faire soi-même.", "Une fiche pour repérer une fuite avant qu'elle coûte cher."]),
    ("soap", "Fabrication de savon", "les femmes qui lancent une petite production à la maison", ["Un guide de recettes de savon, pas à pas.", "Une fiche pour calculer le coût de revient d'un savon et fixer son prix.", "Une mini-formation filmée pour réussir sa première fabrication."]),
]


def bonus1():
    pages = [f"""
<section class="page cover">
  <div class="tag">Bonus 1 · Gagne ta vie sans diplôme</div>
  <div class="big">60</div>
  <h1>idées de produits digitaux, <span>métier par métier</span></h1>
  <p>20 savoir-faire, la bonne personne à aider pour chacun, et 3 produits que tu peux créer avec ton téléphone.</p>
  <img class="ebook" src="ebook.png" alt="">
  <div class="brand">DigitalMikaelson · Pas de blabla, juste ce qu'il faut faire, concrètement.</div>
</section>
<section class="page">
  <div class="tag">Mode d'emploi</div>
  <h2>Comment utiliser <span>cette liste</span></h2>
  <p>Chaque fiche suit la même règle : <b>une compétence, une niche, un produit</b>. On ne vend pas « des recettes » à tout le monde, on les vend à une personne précise, qui a un problème précis.</p>
  <div class="steps">
    <div><b class="n">1</b><p><b>Trouve ton métier</b>, ou le plus proche du tien. Tu fais de la coiffure ? Regarde la couture et le maquillage : le raisonnement est le même.</p></div>
    <div><b class="n">2</b><p><b>Choisis une seule idée</b>, la plus rapide à faire avec ce que tu as déjà (chapitre 3 du guide).</p></div>
    <div><b class="n">3</b><p><b>Passe au test en 7 jours</b> (chapitre 4) avant de passer des semaines dessus. Le kit du bonus 2 te donne les messages à envoyer.</p></div>
    <div><b class="n">4</b><p><b>Change la niche si besoin.</b> Garde ta compétence, mais aide une autre personne : le même savoir-faire peut servir plusieurs publics.</p></div>
  </div>
  <a class="btn y" href="{WA}">Ton métier n'est pas dans la liste ?<small>Écris-moi sur WhatsApp, on trouve ta niche ensemble</small></a>
  <span class="num">2</span>
</section>"""]
    n = 3
    for k in range(0, len(METIERS), 3):
        blocs = ""
        for j, (ic, m, cible, idees) in enumerate(METIERS[k:k + 3]):
            lis = "".join(f"<li>{E(x)}</li>" for x in idees)
            blocs += f'<div class="metier"><div class="hd"><img src="img/{ic}_3d.png" alt=""><div><div class="k">Idées {(k + j) * 3 + 1} à {(k + j) * 3 + 3}</div><h3>{E(m)} → <em>{E(cible)}</em></h3></div></div><ol>{lis}</ol></div>'
        pages.append(f'<section class="page"><div class="tag">Bonus 1 · 60 idées</div>{blocs}<span class="foot">Gagne ta vie sans diplôme</span><span class="num">{n}</span></section>')
        n += 1
    pages.append(f"""
<section class="page cover">
  <div class="tag">Et maintenant ?</div>
  <h1>Une idée, <span>un test</span>, une semaine</h1>
  <p>Ne choisis pas l'idée la plus originale : choisis celle que tu peux faire cette semaine, pour la personne que tu connais le mieux. Puis teste-la avec le kit du bonus 2.</p>
  <a class="btn y" href="{WA}">Une question sur ton idée ?<small>Écris-moi sur WhatsApp : +243 831 710 181</small></a>
  <img class="ebook" src="ebook.png" alt="">
  <div class="brand">DigitalMikaelson</div>
</section>""")
    pdf("bonus1_60_idees_produits.pdf", "".join(pages), "Bonus 1 : 60 idées de produits digitaux")


# ------------------------------------------------------------------ bonus 2 : le kit du test en 7 jours
def bonus2():
    jours = [("J1-J2", "Écris ton offre en une phrase (page 2)"), ("J3", "Envoie le message à 10 ou 15 proches (page 3)"), ("J4", "Publie ta phrase en statut"),
             ("J5", "Republie, réponds à chaque réaction"), ("J6", "Propose un petit prix aux intéressés (page 4)"), ("J7", "Fais le bilan (page 5)")]
    rows = "".join(f'<tr><td class="jr">{E(j)}</td><td>{E(t)}</td><td class="c"><i></i></td></tr>' for j, t in jours)
    suivi = "".join('<tr><td>&nbsp;</td><td class="c"><i></i></td><td class="c"><i></i></td><td class="c"><i></i></td></tr>' for _ in range(7))
    body = f"""
<section class="page cover">
  <div class="tag">Bonus 2 · Gagne ta vie sans diplôme</div>
  <div class="big">7</div>
  <h1>Le kit du <span>test en 7 jours</span></h1>
  <p>Le chapitre 4, prêt à l'emploi : ta phrase d'offre à trous, les messages à copier-coller, et le tableau pour suivre chaque jour.</p>
  <img class="ebook" src="ebook.png" alt="">
  <div class="brand">DigitalMikaelson · Pas de blabla, juste ce qu'il faut faire, concrètement.</div>
</section>

<section class="page">
  <div class="tag">Jours 1 et 2</div>
  <h2>Ta phrase <span>d'offre</span></h2>
  <div class="box"><div class="phrase">J'aide <span class="blank">[telle personne]</span><br>à obtenir <span class="blank">[tel résultat]</span><br>grâce à <span class="blank">[ma compétence]</span>.</div></div>
  <div class="box"><h3>Exemples</h3>
    <p class="ex">J'aide les vendeuses du marché à calculer leurs prix sans perdre d'argent.</p>
    <p class="ex">J'aide les trésoriers de likelemba à présenter des comptes clairs à chaque réunion.</p>
    <p class="ex">J'aide les familles qui passent au solaire à choisir leur panneau sans se tromper.</p>
  </div>
  <div class="box"><h3>À toi</h3><div class="lines"><i></i><i></i><i></i></div></div>
  <p style="font-size:9pt">Si tu n'arrives pas à la dire en une phrase claire, reviens au chapitre 2.</p>
  <span class="foot">Bonus 2 · Kit du test</span><span class="num">2</span>
</section>

<section class="page">
  <div class="tag">Jours 3 à 5</div>
  <h2>Les messages <span>à copier-coller</span></h2>
  <div class="box"><h3>Jour 3 · À 10 ou 15 proches, un par un</h3>
    <div class="msg">Salut <b>[prénom]</b> ! Je prépare un petit guide pour aider <b>[telle personne]</b> à <b>[tel résultat]</b>. Ça t'intéresserait, pour toi ou pour quelqu'un que tu connais ?</div>
    <div class="msg">Salut <b>[prénom]</b>, j'ai une question rapide : est-ce que tu as déjà eu du mal à <b>[le problème]</b> ? Je prépare quelque chose là-dessus et ton avis m'aiderait.</div>
  </div>
  <div class="box"><h3>Jours 4 et 5 · En statut WhatsApp, Facebook ou story</h3>
    <div class="msg">Je prépare un petit guide pour <b>[telle personne]</b> qui veut <b>[tel résultat]</b>. Ça t'intéresse ? Écris-moi « OUI » en privé.</div>
    <div class="msg">Question du jour : est-ce que <b>[le problème]</b> t'est déjà arrivé ? Réponds en privé, je prépare une solution simple.</div>
  </div>
  <p style="font-size:9pt">Compte chaque « oui » dans le tableau de la page 5. Réponds à tout le monde, même à ceux qui disent non : demande-leur pourquoi.</p>
  <span class="foot">Bonus 2 · Kit du test</span><span class="num">3</span>
</section>

<section class="page">
  <div class="tag">Jour 6</div>
  <h2>Proposer <span>un petit prix</span></h2>
  <div class="box"><h3>À ceux qui ont dit oui</h3>
    <div class="msg">Merci pour ton intérêt ! Le guide sera prêt le <b>[date]</b>. Pour les premières personnes, il est à <b>[ton prix]</b>. Je te le réserve ?</div>
  </div>
  <div class="box"><h3>Si la personne hésite</h3>
    <div class="msg">Pas de souci ! Qu'est-ce qui te ferait dire oui : le prix, le contenu, ou le moment ?</div>
  </div>
  <div class="box"><h3>Après un paiement</h3>
    <div class="msg">Merci beaucoup ! Je t'envoie le guide le <b>[date]</b>. Quand tu l'auras lu, tu me diras ce qui t'a le plus servi ?</div>
  </div>
  <p style="font-size:9pt">Le but n'est pas de devenir riche au jour 6 : c'est de voir si les gens sortent vraiment leur argent, ou s'ils disent « ça m'intéresse » par politesse.</p>
  <span class="foot">Bonus 2 · Kit du test</span><span class="num">4</span>
</section>

<section class="page">
  <div class="tag">Ton suivi</div>
  <h2>Le tableau <span>des 7 jours</span></h2>
  <table><tr><th>Jour</th><th>Ce que tu fais</th><th>Fait</th></tr>{rows}</table>
  <h3 style="margin:4mm 0 2mm">Les réponses</h3>
  <table><tr><th>Prénom</th><th>A répondu</th><th>Intéressé</th><th>A payé</th></tr>{suivi}</table>
  <span class="foot">Bonus 2 · Kit du test</span><span class="num">5</span>
</section>

<section class="page">
  <div class="tag">Jour 7</div>
  <h2>Le <span>bilan</span></h2>
  <div class="box"><h3>Au moins une personne a payé, ou s'est vraiment engagée ?</h3><p>Ton idée tient la route. Prends le temps de bien finir ton produit, et garde les premiers messages : ils te serviront pour vendre.</p></div>
  <div class="box"><h3>Personne n'a réagi ?</h3><p>Ce n'est pas un échec, c'est une information. Change l'angle (une autre personne, un autre résultat), ou reprends ta liste du chapitre 2 et teste une autre compétence. Le bonus 1 te donne des idées.</p></div>
  <div class="box"><h3>Mes chiffres</h3><div class="lines"><i></i><i></i><i></i></div></div>
  <a class="btn g" href="{WA}">Dis-moi le résultat de ton test<small>WhatsApp : +243 831 710 181, je t'aide pour la suite</small></a>
  <span class="foot">Bonus 2 · Kit du test</span><span class="num">6</span>
</section>"""
    pdf("bonus2_kit_test_7_jours.pdf", body, "Bonus 2 : le kit du test en 7 jours")


if __name__ == "__main__":
    bonus1()
    bonus2()
