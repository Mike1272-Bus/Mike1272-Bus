"""PDF : méthode de vente Allegra, inspirée de la masterclass de Chanel (vendre un logiciel SaaS)."""
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, KeepTogether
from reportlab.lib.styles import ParagraphStyle

F = '/home/user/Mike1272-Bus/produits/templates-entreprises/video-automatisation/assets/'
pdfmetrics.registerFont(TTFont('Bri', F + 'fonts/bricolage-800.ttf'))
pdfmetrics.registerFont(TTFont('WS', F + 'fonts/worksans-400.ttf'))
pdfmetrics.registerFont(TTFont('WSB', F + 'fonts/worksans-700.ttf'))
addMapping('WS', 0, 0, 'WS'); addMapping('WS', 1, 0, 'WSB')
NAVY = colors.HexColor('#0b1033'); HOT = colors.HexColor('#e2360c'); GREY = colors.HexColor('#4a5275'); LIGHT = colors.HexColor('#f3f5fc')
H1 = ParagraphStyle('h1', fontName='Bri', fontSize=24, leading=28, textColor=NAVY, spaceAfter=4)
SUB = ParagraphStyle('sub', fontName='WS', fontSize=11, leading=15, textColor=GREY, spaceAfter=6)
H2 = ParagraphStyle('h2', fontName='Bri', fontSize=16, leading=20, textColor=NAVY, spaceBefore=14, spaceAfter=6, keepWithNext=1)
H3 = ParagraphStyle('h3', fontName='Bri', fontSize=12, leading=15, textColor=HOT, spaceBefore=6, spaceAfter=3, keepWithNext=1)
B = ParagraphStyle('b', fontName='WS', fontSize=10, leading=14, textColor=NAVY, spaceAfter=3)
SM = ParagraphStyle('sm', fontName='WS', fontSize=9, leading=12, textColor=NAVY)
QUOTE = ParagraphStyle('q', fontName='WS', fontSize=9.5, leading=13.5, textColor=GREY, backColor=colors.HexColor('#f6f3ee'),
                       borderPadding=(6, 8, 6, 8), spaceBefore=4, spaceAfter=8)
MSG = ParagraphStyle('msg', fontName='WS', fontSize=9.5, leading=13.5, textColor=NAVY, backColor=colors.HexColor('#e7f6ec'),
                     borderPadding=(6, 8, 6, 8), spaceBefore=4, spaceAfter=8)
b = lambda t: f'<font name="WSB">{t}</font>'


def bl(items):
    return [Paragraph('•&nbsp;&nbsp;' + x, B) for x in items]


def nl(items):
    return [Paragraph(f'{b(str(i))}.&nbsp;&nbsp;{x}', B) for i, x in enumerate(items, 1)]


def table(data, widths):
    t = Table([[Paragraph(str(c), SM) for c in r] for r in data], colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([('LINEBELOW', (0, 0), (-1, -1), 0.5, colors.HexColor('#dde3f5')), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                           ('TOPPADDING', (0, 0), (-1, -1), 4), ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
                           ('BACKGROUND', (0, 0), (-1, 0), LIGHT)]))
    return t


def chanel(t):
    return Paragraph(b('Ce que dit Chanel : ') + t, QUOTE)


def msg(t):
    return Paragraph(t.replace('\n', '<br/>'), MSG)


def footer(c, d):
    c.saveState(); c.setFont('WS', 8); c.setFillColor(GREY)
    c.drawString(18 * mm, 10 * mm, 'Allegra Digital Ground · Méthode de vente (usage interne)')
    c.drawRightString(192 * mm, 10 * mm, str(d.page)); c.restoreState()


W = 174 * mm
doc = SimpleDocTemplate(sys.argv[1], pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm, topMargin=16 * mm, bottomMargin=18 * mm,
                        title='Méthode de vente Allegra', author='Allegra Digital Ground')
s = [Image(F + 'img/logo_adg.png', width=24 * mm, height=19 * mm, hAlign='LEFT'), Spacer(1, 3),
     Paragraph('Notre méthode de vente, du premier message au client installé', H1),
     Paragraph('Inspirée de la masterclass de Chanel « Si je devais vendre ton produit » (vendre un logiciel SaaS), écoutée en entier, '
               'et adaptée à ce qu\'on vend : des automatisations pour les entreprises de RDC, à commencer par le système de stock. Document interne.', SUB)]

# ---------------------------------------------------------------- résumé
s.append(Paragraph('En bref : les 6 étapes', H2))
s.append(Paragraph('Chanel a vendu des logiciels pendant des années (un logiciel de planning pour restaurants, cabinets et usines, puis un CRM). '
                   'Sa méthode tient en 6 étapes. Voici ce que chacune devient chez nous.', B))
s.append(table([
    ['Étape', 'L\'idée de Chanel', 'Chez Allegra'],
    ['1. Le client idéal', 'Ton produit peut servir tout le monde, ton discours non. Vise ceux que tu sers mieux que personne.', 'Commerces avec stock, 1 à 3 points de vente, patron souvent absent, tout à la main (cahier, Excel).'],
    ['2. Le pipeline', 'Les prospects ne sont pas tous au même stade. Note tout, relance au bon moment, plante des graines chaque jour.', 'Un fichier de suivi, 6 stades, un message prêt pour chaque stade, 20 contacts par jour.'],
    ['3. Les signaux', 'On obtient le rendez-vous grâce à un signal : un changement chez le prospect.', 'Nouvelle boutique, recrutement, pubs Facebook, avis « rupture » : on écrit « j\'ai vu ça ».'],
    ['4. Découverte avant démo', 'Ne montre pas l\'outil trop vite. Pose des questions, fais calculer le coût de ne rien faire, puis démo sur SES besoins.', '15 minutes de questions, le patron calcule lui-même ses pertes, puis démo avec 3 de SES produits.'],
    ['5. Le compte, pas la licence', 'Entre petit, puis grandis avec le client. L\'argent est dans le suivi.', 'On commence par « vente + alerte », puis bilan, arrivages, 2e boutique, autres tâches.'],
    ['6. Le système', 'Écris ta méthode, récolte les mots de tes clients, ne développe que ce qui est demandé.', 'Formation interne, messages prêts, avis clients (avec accord), une vidéo par fonction.'],
], [32 * mm, 72 * mm, 70 * mm]))

# ---------------------------------------------------------------- étape 1
s.append(Paragraph('Étape 1 · Le client que tu sers mieux que personne', H2))
s.append(chanel('« Ce n\'est pas parce que ton produit peut répondre à plein de besoins que ta prospection doit s\'adresser à tout le monde. '
                'Ça peut être vrai pour le produit, ça ne doit pas être vrai pour le discours. » Elle conseille aussi de regarder ce que le prospect '
                'utilise déjà : une entreprise très équipée, avec un système énorme, change rarement, car le changement lui coûte trop cher.'))
s.append(Paragraph('Chez nous', H3))
s.append(table([
    ['On vise en premier', 'On évite pour l\'instant'],
    ['Commerces avec beaucoup de produits : quincailleries, cosmétiques, téléphones, alimentation, grossistes.', 'Les grandes entreprises qui ont déjà un logiciel de gestion complet : le changement leur coûte trop cher (sauf si elles en sont mécontentes).'],
    ['1 à 3 points de vente, 2 à 10 employés.', 'Ceux qui vendent très peu de produits différents : le gain est trop petit.'],
    ['Le patron n\'est pas toujours sur place.', 'Ceux qui n\'ont pas de smartphone ou pas de WhatsApp.'],
    ['Tout se fait à la main : cahier, Excel rempli à la main, comptage le soir.', ''],
], [87 * mm, 87 * mm]))
s.append(Paragraph('La question qui trie tout de suite : ' + b('« Aujourd\'hui, chez vous, le stock et les ventes, vous les suivez comment ? »') +
                   ' Réponse « cahier » ou « Excel » : c\'est notre client. Réponse « on a un logiciel » : on note le nom du logiciel et la date de fin de contrat, et on revient plus tard.', B))
s.append(Paragraph('Un discours par niche', H3))
s.append(table([
    ['Niche', 'La douleur dont on parle'],
    ['Quincaillerie', 'Des produits chers qui dorment, des ruptures de ciment ou de tôles au mauvais moment.'],
    ['Cosmétiques', 'Des centaines de références, impossible de savoir ce qui reste sans tout recompter.'],
    ['Téléphones et accessoires', 'Des petits articles qui disparaissent sans que personne ne s\'en rende compte.'],
    ['Pharmacie', 'Les ruptures et les dates de péremption (alerte à ajouter au système).'],
    ['Alimentation, grossistes', 'Beaucoup d\'entrées et de sorties chaque jour, des calculs du soir interminables.'],
], [45 * mm, 129 * mm]))

# ---------------------------------------------------------------- étape 2
s.append(Paragraph('Étape 2 · Le pipeline : chaque prospect à son stade', H2))
s.append(chanel('« Vous ne pouvez pas avoir des prospects qui sont tous au même stade. » Il faut noter chaque conversation, la date de fin de contrat, '
                'le bon moment pour revenir, et préparer une ressource pour chaque stade. « Le but, c\'est de planter des graines de manière régulière. »'))
s.append(Paragraph('Nos 6 stades (à suivre dans prospection_50_entreprises.xlsx)', H3))
s.append(table([
    ['Stade', 'Comment on le reconnaît', 'Ce qu\'on lui envoie'],
    ['1. Pas conscient', 'Il trouve normal de tout faire à la main.', 'La question : « le stock, c\'est encore noté à la main ? »'],
    ['2. Conscient', 'Il dit « oui, c\'est vrai que c\'est lourd ».', 'La vidéo de vente (71 s) : « ce n\'est pas normal, ça se règle ».'],
    ['3. Intéressé', 'Il pose des questions, demande le prix.', 'Proposition : 15 minutes de découverte, deux créneaux au choix.'],
    ['4. Démo faite', 'Il a vu le système avec ses produits.', 'Récapitulatif écrit + proposition + date de démarrage.'],
    ['5. Essai ou installation', 'Il a dit oui.', 'Le planning d\'installation (voir étape 4).'],
    ['6. Pas maintenant', '« On verra après les fêtes », « on a déjà un logiciel ».', 'On note la date et la raison, on revient au bon moment.'],
], [34 * mm, 62 * mm, 78 * mm]))
s.append(Paragraph('Les bons moments pour revenir, en RDC', H3))
s += bl(['L\'inventaire de fin d\'année (décembre, janvier) : le moment où le comptage à la main fait le plus mal.',
         'L\'ouverture d\'un nouveau point de vente ou l\'arrivée d\'un nouveau gérant.',
         'Les gros moments de vente : fêtes de fin d\'année, rentrée scolaire (papeteries, uniformes).',
         'La fin d\'un contrat de logiciel, pour ceux qui sont déjà équipés.'])
s.append(Paragraph(b('Règle : ') + 'rien ne reste dans ta tête. Chaque contact = une ligne dans le fichier, avec la prochaine action et sa date.', B))

# ---------------------------------------------------------------- étape 3
s.append(Paragraph('Étape 3 · Les signaux pour obtenir le rendez-vous', H2))
s.append(chanel('Un nouveau directeur commercial, un plan de recrutement, un changement de logo, un agrandissement, un rachat : ce sont des signaux. '
                'On obtient le rendez-vous en disant « j\'ai vu ça, je pense pouvoir vous aider ». Et il faut cadrer : si le prospect dit '
                '« envoyez-moi un accès, je regarderai », on refuse poliment, car un outil vide ne montre rien.'))
s.append(table([
    ['Signal chez le prospect', 'Où le voir', 'Première phrase'],
    ['Ouverture d\'une 2e boutique', 'Facebook, Instagram, en passant devant', '« J\'ai vu que vous ouvrez à Limete, félicitations. Avec deux boutiques, suivre le stock à la main devient vite compliqué… »'],
    ['Recrutement de vendeurs', 'Annonces, statuts WhatsApp', '« J\'ai vu que vous recrutez. Plus de vendeurs, c\'est plus de ventes à noter et à vérifier… »'],
    ['Pubs Facebook en cours', 'Bibliothèque publicitaire Meta', '« J\'ai vu votre pub sur les nouveaux arrivages. Quand ça se vend vite, le stock suit difficilement… »'],
    ['Avis clients « rupture », « pas de réponse »', 'Google Maps', '« Un client parlait d\'un produit introuvable. C\'est souvent un problème de suivi du stock… »'],
    ['Nouveaux arrivages très fréquents', 'Leurs publications', '« Vous recevez beaucoup de marchandise. Comment vous suivez ce qui entre et ce qui sort ? »'],
], [42 * mm, 42 * mm, 90 * mm]))
s.append(Paragraph('Si le prospect dit « envoyez-moi juste les infos »', H3))
s.append(msg('Avec plaisir. Mais un système vide ne vous montrera pas grand-chose : ce qui compte, c\'est comment il marche avec VOS produits. '
             'Je vous propose 15 minutes, je le prépare avec 3 de vos articles. Mardi 10 h ou jeudi 15 h, qu\'est-ce qui vous arrange ?'))

# ---------------------------------------------------------------- étape 4
s.append(Paragraph('Étape 4 · Découverte d\'abord, démo ensuite', H2))
s.append(chanel('L\'erreur des fondateurs, c\'est de montrer l\'outil trop vite parce qu\'ils en sont fiers. Le prospect voit tout, n\'a plus de raison de te parler, '
                'puis disparaît. « L\'argent se trouve dans l\'inconfort » : poser des questions, creuser, fixer la prochaine étape, faire un planning. '
                'Son astuce la plus forte : faire calculer au prospect ce que lui coûte le fait de ne rien changer. '
                '« Quand c\'est lui qui construit les chiffres, il ne peut plus dire que c\'est faux. »'))
s.append(Paragraph('Les questions de découverte (15 minutes, avant toute démo)', H3))
s += nl(['Comment vous notez une vente aujourd\'hui ? Qui le fait ?',
         'Qui compte le stock, et tous les combien ? Combien de temps ça prend ?',
         'Quand vous n\'êtes pas à la boutique, comment savez-vous ce qui s\'est vendu ?',
         'La dernière fois qu\'un produit a manqué, ça s\'est passé comment ? Le client est revenu ?',
         'Le soir, combien de temps pour faire les comptes ?',
         'Il vous arrive de trouver un écart entre le cahier et ce qu\'il reste vraiment ?',
         'Qu\'est-ce que vous aimeriez savoir chaque soir sans avoir à demander ?',
         'Si ça marchait parfaitement, ça changerait quoi pour vous ?'])
s.append(Paragraph('L\'atelier « ce que vous coûte le travail à la main »', H3))
s.append(Paragraph('Tu poses les questions, c\'est ' + b('le patron qui donne les chiffres') + ' et qui fait le calcul avec toi. Tu ne proposes aucun chiffre toi-même.', B))
s.append(table([
    ['Question', 'Sa réponse', 'Calcul'],
    ['Combien de temps par jour pour noter, recompter et faire les comptes ?', '… heures', '× jours de travail dans le mois = heures perdues par mois'],
    ['Combien de fois par mois un produit manque quand un client le demande ?', '… fois', '× bénéfice moyen sur une vente = argent perdu par mois'],
    ['Combien d\'écarts de stock (casse, oubli, vol) par mois ?', '… produits', '× prix d\'achat = argent perdu par mois'],
    ['Total par mois', '', 'C\'est le coût de ne rien faire, calculé par lui.'],
], [70 * mm, 25 * mm, 79 * mm]))
s.append(Paragraph('Ensuite seulement, tu compares avec le prix de l\'installation et du suivi. S\'il a trouvé lui-même que ça lui coûte plus cher de ne rien faire, la discussion sur le prix devient simple.', B))
s.append(Paragraph('Si le prospect veut la démo tout de suite', H3))
s.append(msg('Je peux vous la montrer maintenant, mais je risque de vous montrer les mauvais écrans. '
             'Ce serait une mauvaise idée qu\'on prenne 15 minutes pour que je comprenne votre façon de travailler, et que je vous montre ensuite le système avec vos propres produits ?'))
s.append(Paragraph('La démo qui vend', H3))
s += bl(['Jamais « regardez ce qu\'on a fait ailleurs » : on montre ' + b('SES') + ' produits et ' + b('SON') + ' téléphone qui sonne.',
         'Une vente de test devant lui : la notification arrive sur son WhatsApp. C\'est le moment fort.',
         'On relie chaque écran à une réponse de la découverte : « vous m\'avez dit que le soir vous perdez une heure : voilà le bilan qui arrive tout seul ».',
         b('On ne termine jamais sans prochaine étape') + ' : une date de démarrage, ou une date de rappel.'])
s.append(Paragraph('Le planning d\'installation à lui donner', H3))
s.append(table([
    ['Quand', 'Quoi'],
    ['Jour 0', 'Il nous envoie la liste de ses produits (même une photo du cahier suffit).'],
    ['Jours 1 et 2', 'On installe le système avec ses produits et son numéro WhatsApp.'],
    ['Jour 3', 'Formation du vendeur (15 minutes) et premières vraies ventes.'],
    ['Jour 7', 'Point ensemble : ce qui marche, ce qu\'on ajuste.'],
], [30 * mm, 144 * mm]))

# ---------------------------------------------------------------- étape 5
s.append(Paragraph('Étape 5 · Entrer petit, puis grandir avec le client', H2))
s.append(chanel('Ne vends pas tout de suite le gros projet : l\'entreprise ne peut pas tout absorber et n\'a même pas conscience de tous ses problèmes. '
                'Entre par une petite partie, donne un planning, puis élargis. Et surtout : « l\'argent se trouve aussi dans le suivi ». '
                'Un client qu\'on ne suit pas finit par partir.'))
s.append(Paragraph('Nos niveaux', H3))
s.append(table([
    ['Niveau', 'Ce qu\'on installe', 'Quand le proposer'],
    ['1. Démarrage', 'Les ventes sur téléphone + l\'alerte de stock sur WhatsApp.', 'Au premier oui.'],
    ['2. Contrôle', '+ le bilan du soir et le point du matin.', 'Après 2 semaines, quand le niveau 1 est adopté.'],
    ['3. Complet', '+ les arrivages de marchandise.', 'Quand il se plaint des écarts à la réception.'],
    ['4. Plusieurs boutiques', 'Le même système dans un 2e point de vente.', 'Dès qu\'il en parle (signal !).'],
    ['5. Sur mesure', 'Autres tâches à la main : relances clients, factures, commandes fournisseurs.', 'Quand il demande « et pour… ? ».'],
], [34 * mm, 80 * mm, 60 * mm]))
s.append(Paragraph('Le suivi client (c\'est là qu\'on garde le revenu mensuel)', H3))
s += bl([b('Jour 7') + ' : « Comment ça se passe avec le vendeur ? Les messages arrivent bien ? »',
         b('Jour 30') + ' : « Qu\'est-ce que ça a changé ? Qu\'est-ce qui se fait encore à la main chez vous ? »',
         b('Chaque mois') + ' : un petit point, et on reprend ce qu\'il avait dit en découverte : « vous m\'aviez parlé de votre 2e boutique, où vous en êtes ? »',
         'Le but : être un partenaire de confiance, pas juste quelqu\'un qui a vendu un système.'])

# ---------------------------------------------------------------- étape 6
s.append(Paragraph('Étape 6 · Le système : pour vendre sans tout porter seul', H2))
s.append(chanel('Un jour tu devras déléguer la vente. « Si vous n\'avez pas de méthode de vente, un commercial n\'y réglera pas le problème, il va juste hériter du vide. » '
                'Écris tout, appelle tes clients contents pour savoir pourquoi ils ont signé, et ne développe pas une fonction tant que le marché ne l\'a pas demandée. '
                'Une fonction seule ne vend rien : on vend une émotion.'))
s.append(table([
    ['Ce qu\'il faut', 'Où on en est'],
    ['La méthode écrite', 'Ce document + la formation de 32 slides + les messages d\'approche.'],
    ['Les messages prêts pour chaque stade', 'messages_approche_hormozi.md (question, vidéo, relances, LinkedIn, terrain).'],
    ['Les mots des clients', 'À récolter chez les premiers clients, avec leur accord écrit : pourquoi ils ont dit oui, ce qu\'ils aiment, ce qui a changé.'],
    ['Une vidéo par fonction', 'Vidéo de vente (71 s) faite. À faire : une vidéo courte pour l\'alerte, le bilan du soir, les arrivages.'],
    ['Ne construire que ce qui est demandé', 'Exemple : l\'alerte de péremption, seulement quand une pharmacie la demande.'],
], [55 * mm, 119 * mm]))
s.append(Paragraph('Vendre l\'émotion, pas les outils', H3))
s.append(Paragraph('Le patron n\'achète pas « un tableau et des automatisations ». Il achète ' + b('la tranquillité') + ' (savoir ce qui se passe sans être là), '
                   + b('le contrôle') + ' (plus d\'écarts) et ' + b('du temps') + ' (plus de comptes le soir). Avec un client, on ne cite jamais les outils utilisés : on parle seulement du résultat.', B))

# ---------------------------------------------------------------- action
s.append(KeepTogether([Paragraph('Ce qu\'on fait cette semaine', H2)] + nl([
    'Trier les 52 entreprises du fichier avec la question de l\'étape 1, et noter leur stade (étape 2).',
    'Chercher un signal pour les 20 premières (étape 3) et écrire leur première phrase.',
    'Préparer une démo avec 3 produits « type » par niche, prête à adapter en 5 minutes.',
    'Imprimer ou garder sur le téléphone les 8 questions de découverte et le tableau du coût de ne rien faire.',
    'Après chaque échange : remplir le fichier de suivi (stade, prochaine action, date).',
])))
s.append(Spacer(1, 8))
s.append(Paragraph('Source : masterclass audio de Chanel (21 min), transcrite automatiquement puis relue. Les chiffres de ses exemples ne sont pas repris ici, '
                   'car la transcription n\'était pas assez fiable sur les nombres.', SM))

doc.build(s, onFirstPage=footer, onLaterPages=footer)
print('ok')
