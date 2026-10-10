import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, Image
from reportlab.lib.styles import ParagraphStyle

F = '/home/user/Mike1272-Bus/produits/templates-entreprises/video-automatisation/assets/'
pdfmetrics.registerFont(TTFont('Bri', F + 'fonts/bricolage-800.ttf'))
pdfmetrics.registerFont(TTFont('WS', F + 'fonts/worksans-400.ttf'))
pdfmetrics.registerFont(TTFont('WSB', F + 'fonts/worksans-700.ttf'))
from reportlab.lib.fonts import addMapping
addMapping('WS', 0, 0, 'WS'); addMapping('WS', 1, 0, 'WSB')

NAVY = colors.HexColor('#0b1033'); BLUE = colors.HexColor('#2342ff'); YEL = colors.HexColor('#f4c518')
GREY = colors.HexColor('#4a5275'); LIGHT = colors.HexColor('#f3f5fc'); ORANGE = colors.HexColor('#b85400')

H1 = ParagraphStyle('h1', fontName='Bri', fontSize=24, leading=28, textColor=NAVY, spaceAfter=4)
SUB = ParagraphStyle('sub', fontName='WS', fontSize=11, leading=15, textColor=GREY, spaceAfter=10)
H2 = ParagraphStyle('h2', fontName='Bri', fontSize=15, leading=19, textColor=NAVY, spaceBefore=10, spaceAfter=6)
B = ParagraphStyle('b', fontName='WS', fontSize=10, leading=14, textColor=NAVY)
CT = ParagraphStyle('ct', fontName='Bri', fontSize=13, leading=16, textColor=NAVY)
NUM = ParagraphStyle('num', fontName='Bri', fontSize=20, leading=22, textColor=colors.white, alignment=1)
LAB = ParagraphStyle('lab', fontName='WSB', fontSize=8.5, leading=11, textColor=BLUE)

T = [
 ("Boutiques de téléphones et d'accessoires", "1",
  "Des dizaines de petits articles (coques, chargeurs, écouteurs, câbles) faciles à perdre de vue ou à se faire voler. Les patrons sont à l'aise avec la technologie : ce sont eux qui diront oui le plus vite.",
  "« accessoires téléphone Kinshasa », « phone shop Kinshasa ». Gombe, Matonge, Grand Marché.",
  "Combien de chargeurs il vous reste, là, sans aller compter ?"),
 ("Boutiques de cosmétiques et de beauté", "1",
  "Beaucoup de références (crèmes, parfums, mèches, perruques) et elles vendent déjà en ligne. Faciles à trouver et à joindre sur WhatsApp.",
  "« cosmétiques Kinshasa », « mèches Kinshasa », « parfums Kinshasa » sur Instagram et Facebook.",
  "Il vous arrive de dire à une cliente « c'est fini » alors qu'il en restait ?"),
 ("Dépôts de boissons et alimentations générales", "2",
  "Du stock qui part tous les jours (cartons, casiers, sacs). Une rupture, c'est une vente perdue tout de suite. La démo du template parle justement de riz et d'huile.",
  "« dépôt boissons Kinshasa », « alimentation » ou « supermarché » + nom de la commune, sur Google Maps.",
  "Comment vous savez quand il faut recommander ?"),
 ("Quincailleries et dépôts de matériaux", "2",
  "Un stock qui coûte cher (ciment, fers, peinture) et des unités différentes (sac, barre, pot), que gère la colonne « Unité ». La valeur du stock les intéresse beaucoup.",
  "« quincaillerie Kinshasa », « matériaux de construction Kinshasa », surtout sur Google Maps.",
  "Vous savez combien vaut tout ce qu'il y a dans votre dépôt aujourd'hui ?"),
 ("Boutiques de vêtements et de chaussures", "2",
  "Beaucoup de modèles, de tailles et de couleurs (un code par taille dans le template). Elles vendent beaucoup sur Instagram, TikTok et WhatsApp, donc faciles à trouver.",
  "« boutique vêtements Kinshasa », « chaussures Kinshasa », « friperie Kinshasa » sur Instagram et Facebook.",
  "Quand une cliente demande une taille, vous savez tout de suite s'il vous la reste ?"),
 ("Librairies et papeteries (fournitures scolaires)", "2",
  "La rentrée scolaire, c'est maintenant : cahiers, stylos, sacs partent très vite et les ruptures coûtent cher en cette période. Beaucoup de petites références.",
  "« librairie Kinshasa », « papeterie Kinshasa », « fournitures scolaires Kinshasa », sur Google Maps et Facebook.",
  "Pendant la rentrée, vous avez manqué de quels articles ?"),
 ("Grossistes et demi-grossistes", "3",
  "De gros volumes et beaucoup d'argent bloqué dans le stock. Le tableau de bord (valeur du stock, marge du mois) leur parle directement. Plus long à convaincre, mais la vente vaut plus.",
  "« grossiste Kinshasa », « vente en gros Kinshasa », « demi-gros » + type de produit.",
  "Vous savez quelle marge vous avez faite le mois dernier ?"),
 ("Boutiques de pièces détachées (motos et voitures)", "3",
  "Des centaines de références avec des codes, exactement ce que gère la colonne « Code ». Un mécanicien qui attend une pièce repart chez le concurrent.",
  "« pièces détachées Kinshasa », « pièces moto Kinshasa », « garage » + commune, sur Google Maps et Facebook.",
  "Quand on vous demande une pièce, combien de temps pour savoir si vous l'avez ?"),
 ("Restaurants et fast-foods", "3",
  "Ils gèrent un stock de produits (ingrédients, boissons, emballages) et beaucoup sont déjà dans ta liste de prospection (Burger Guys, Fatburger, Savane…). Le template s'ajoute à la vidéo animée.",
  "D'abord ta liste de prospection WhatsApp, puis « restaurant Kinshasa », « fast food Kinshasa ».",
  "Il vous arrive de manquer de boissons ou d'emballages en plein service ?"),
 ("Pharmacies", "3",
  "Énormément de références, et une rupture de médicament fait fuir le client. Attention : il leur faut une colonne « date de péremption » avec une alerte. À ajouter au template avant de les démarcher.",
  "« pharmacie » + nom de la commune, sur Google Maps.",
  "Comment vous repérez les produits qui vont bientôt périmer ?"),
]

def card(i, t):
    title, prio, why, where, q = t
    pc = {'1': BLUE, '2': colors.HexColor('#3a5bff'), '3': GREY}[prio]
    ptxt = {'1': 'PRIORITÉ 1', '2': 'PRIORITÉ 2', '3': 'PRIORITÉ 3'}[prio]
    body = [
        [Paragraph(f'<font name="WSB" color="{pc.hexval()}" size="8.5">{ptxt}</font>', B)],
        [Paragraph(title, CT)],
        [Paragraph('<font name="WSB" color="#2342ff">POURQUOI</font><br/>' + why, B)],
        [Paragraph('<font name="WSB" color="#2342ff">OÙ LES TROUVER</font><br/>' + where, B)],
        [Paragraph('<font name="WSB" color="#b85400">LA QUESTION À LEUR POSER</font><br/><i>' + q + '</i>', B)],
    ]
    inner = Table(body, colWidths=[150*mm])
    inner.setStyle(TableStyle([('LEFTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 4), ('TOPPADDING', (0,0), (-1,-1), 1)]))
    n = Table([[Paragraph(str(i), NUM)]], colWidths=[12*mm], rowHeights=[12*mm])
    n.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,-1), NAVY if prio != '1' else BLUE), ('VALIGN', (0,0), (-1,-1), 'MIDDLE'), ('ROUNDEDCORNERS', [6,6,6,6])]))
    t = Table([[n, inner]], colWidths=[18*mm, 154*mm])
    t.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,-1), LIGHT), ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 8), ('RIGHTPADDING', (0,0), (-1,-1), 8), ('TOPPADDING', (0,0), (-1,-1), 9), ('BOTTOMPADDING', (0,0), (-1,-1), 7),
        ('ROUNDEDCORNERS', [8,8,8,8])]))
    return KeepTogether([t, Spacer(1, 6)])

def footer(c, d):
    c.saveState(); c.setFont('WS', 8); c.setFillColor(GREY)
    c.drawString(18*mm, 10*mm, 'Allegra Digital Ground · Template « Gestion de stock » · cibles de prospection')
    c.drawRightString(192*mm, 10*mm, str(d.page)); c.restoreState()

doc = SimpleDocTemplate(sys.argv[1], pagesize=A4, leftMargin=18*mm, rightMargin=18*mm, topMargin=16*mm, bottomMargin=18*mm,
                        title='Template Gestion de stock : 10 types d\'entreprises à prospecter', author='Allegra Digital Ground')
s = []
s.append(Image(F + 'img/logo_adg.png', width=34*mm, height=27*mm, hAlign='LEFT'))
s.append(Spacer(1, 4))
s.append(Paragraph('Template « Gestion de stock »', H1))
s.append(Paragraph('Les 10 types d\'entreprises à prospecter en premier à Kinshasa, du plus facile à convaincre au moins facile.', SUB))
s.append(Paragraph('Comment on les a choisis', H2))
for x in ['Beaucoup de produits différents, et un stock qui tourne vite.',
          'Un patron souvent sur son téléphone, joignable sur WhatsApp.',
          'Un stock suivi aujourd\'hui dans un cahier ou de tête.',
          'Une rupture ou une perte qui leur coûte vraiment de l\'argent.']:
    s.append(Paragraph('•&nbsp;&nbsp;' + x, B))
s.append(Spacer(1, 4))
s.append(Paragraph('<font name="WSB">Priorité 1</font> : à contacter cette semaine. <font name="WSB">Priorité 2</font> : juste après. <font name="WSB">Priorité 3</font> : plus long à convaincre ou un réglage à prévoir.', B))
s.append(Paragraph('Les 10 cibles', H2))
for i, t in enumerate(T, 1):
    s.append(card(i, t))
s.append(Paragraph('Où chercher, pour tous', H2))
for x in ['<font name="WSB">Google Maps</font> : tape le type de commerce + le nom de la commune. Le numéro est souvent affiché.',
          '<font name="WSB">Facebook et Instagram</font> : le numéro WhatsApp est souvent dans la bio ou les publications.',
          '<font name="WSB">Tes contacts WhatsApp</font> : regarde les statuts, beaucoup de commerçants y publient leurs produits.']:
    s.append(Paragraph('•&nbsp;&nbsp;' + x, B))
s.append(Paragraph('Comment s\'y prendre', H2))
for x in ['Commence par les priorités 1 : 10 boutiques de téléphones et 10 de cosmétiques.',
          'Pose d\'abord la question de la fiche, sans parler du template. Écoute la réponse.',
          'Si la personne reconnaît le problème, montre la vidéo ou une capture du tableau de bord.',
          'Note chaque contact dans le fichier de prospection : nom, commune, numéro, réponse, date de relance.',
          'Une relance 3 à 5 jours après, puis on arrête.']:
    s.append(Paragraph('•&nbsp;&nbsp;' + x, B))
doc.build(s, onFirstPage=footer, onLaterPages=footer)
print('ok')
