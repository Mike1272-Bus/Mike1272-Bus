"""PDF « Système de gestion de stock automatisé : comment ça marche ».
Usage : python3 src/generer_pdf.py systeme_gestion_stock_automatise.pdf"""
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, Image, PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.graphics.shapes import Drawing, Rect, String, Line, Polygon

F = '../video-automatisation/assets/'
pdfmetrics.registerFont(TTFont('Bri', F + 'fonts/bricolage-800.ttf'))
pdfmetrics.registerFont(TTFont('WS', F + 'fonts/worksans-400.ttf'))
pdfmetrics.registerFont(TTFont('WSB', F + 'fonts/worksans-700.ttf'))
addMapping('WS', 0, 0, 'WS'); addMapping('WS', 1, 0, 'WSB')

NAVY = colors.HexColor('#0b1033'); BLUE = colors.HexColor('#2342ff'); GREEN = colors.HexColor('#15803d')
ORANGE = colors.HexColor('#b85400'); GREY = colors.HexColor('#4a5275'); LIGHT = colors.HexColor('#f3f5fc')

H1 = ParagraphStyle('h1', fontName='Bri', fontSize=24, leading=28, textColor=NAVY, spaceAfter=4)
SUB = ParagraphStyle('sub', fontName='WS', fontSize=11, leading=15, textColor=GREY, spaceAfter=8)
H2 = ParagraphStyle('h2', fontName='Bri', fontSize=15, leading=19, textColor=NAVY, spaceBefore=12, spaceAfter=6)
H3 = ParagraphStyle('h3', fontName='Bri', fontSize=12.5, leading=16, textColor=NAVY, spaceAfter=3)
B = ParagraphStyle('b', fontName='WS', fontSize=10, leading=14, textColor=NAVY, spaceAfter=2)
SM = ParagraphStyle('sm', fontName='WS', fontSize=9, leading=12, textColor=GREY)
MSG = ParagraphStyle('msg', fontName='WS', fontSize=9.5, leading=13, textColor=NAVY, backColor=colors.HexColor('#e7f6ec'),
                     borderPadding=(5, 7, 5, 7), spaceBefore=3, spaceAfter=3)

def bullets(items, st=B):
    return [Paragraph('•&nbsp;&nbsp;' + x, st) for x in items]

def boxed(flow, bg=LIGHT):
    t = Table([[flow]], colWidths=[174*mm])
    t.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,-1), bg), ('LEFTPADDING', (0,0), (-1,-1), 10), ('RIGHTPADDING', (0,0), (-1,-1), 10),
                           ('TOPPADDING', (0,0), (-1,-1), 8), ('BOTTOMPADDING', (0,0), (-1,-1), 8), ('ROUNDEDCORNERS', [8,8,8,8])]))
    return t

def schema():
    W, H = 174*mm, 92*mm
    d = Drawing(W, H)
    def box(x, y, w, h, title, sub, fill, fg=colors.white):
        d.add(Rect(x, y, w, h, rx=8, ry=8, fillColor=fill, strokeColor=None))
        d.add(String(x + w/2, y + h - 15, title, fontName='WSB', fontSize=9.5, fillColor=fg, textAnchor='middle'))
        for k, line in enumerate(sub):
            d.add(String(x + w/2, y + h - 28 - 11*k, line, fontName='WS', fontSize=7.8, fillColor=fg, textAnchor='middle'))
    def arrow(x1, y1, x2, y2, col=GREY):
        d.add(Line(x1, y1, x2, y2, strokeColor=col, strokeWidth=1.6))
        import math
        a = math.atan2(y2 - y1, x2 - x1); s = 6
        d.add(Polygon([x2, y2, x2 - s*math.cos(a - 0.4), y2 - s*math.sin(a - 0.4), x2 - s*math.cos(a + 0.4), y2 - s*math.sin(a + 0.4)], fillColor=col, strokeColor=None))
    # colonne gauche : déclencheurs
    box(0, 64*mm, 44*mm, 24*mm, 'Vendeur', ['formulaire', '« Nouvelle commande »'], BLUE)
    box(0, 34*mm, 44*mm, 24*mm, 'Magasinier', ['formulaire', '« Arrivage »'], BLUE)
    box(0, 4*mm, 44*mm, 24*mm, 'Horloge', ['8 h : point du matin', '19 h : bilan du soir'], colors.HexColor('#e07b00'))
    # centre : n8n
    box(64*mm, 22*mm, 44*mm, 48*mm, 'n8n', ['le moteur', '', 'lit, calcule,', 'écrit, prévient'], NAVY)
    # droite
    box(128*mm, 52*mm, 46*mm, 36*mm, 'Google Sheets', ['le template de stock', '= la mémoire', 'Produits, Commandes,', 'Arrivages, Tableau de bord'], GREEN)
    box(128*mm, 4*mm, 46*mm, 36*mm, 'WhatsApp', ['messages au patron', '(et confirmation', 'au client)'], colors.HexColor('#16a34a'))
    for y in (76, 46, 16):
        arrow(44*mm, y*mm, 64*mm, (46 + (y - 46) * 0.45)*mm)
    arrow(108*mm, 56*mm, 128*mm, 68*mm, GREEN); arrow(128*mm, 62*mm, 108*mm, 50*mm, GREEN)
    arrow(108*mm, 36*mm, 128*mm, 24*mm, colors.HexColor('#16a34a'))
    k = 0.85
    d.scale(k, k); d.width, d.height = W * k, H * k
    d.hAlign = 'CENTER'
    return d

def footer(c, d):
    c.saveState(); c.setFont('WS', 8); c.setFillColor(GREY)
    c.drawString(18*mm, 10*mm, 'Allegra Digital Ground · Système de gestion de stock automatisé')
    c.drawRightString(192*mm, 10*mm, str(d.page)); c.restoreState()

def auto(num, titre, quand, etapes, messages, col=BLUE):
    flow = [Paragraph(f'<font color="{col.hexval()}">AUTOMATISATION {num}</font>', ParagraphStyle('k', fontName='WSB', fontSize=8.5, leading=11, textColor=col)),
            Paragraph(titre, H3), Paragraph('<font name="WSB">Quand :</font> ' + quand, B), Paragraph('<font name="WSB">Ce qui se passe :</font>', B)]
    flow += [Paragraph(f'{i}.&nbsp;&nbsp;{e}', B) for i, e in enumerate(etapes, 1)]
    for who, txt in messages:
        flow.append(Paragraph(f'<font name="WSB">{who}</font> « {txt} »', MSG))
    return KeepTogether([boxed(flow), Spacer(1, 7)])

doc = SimpleDocTemplate(sys.argv[1], pagesize=A4, leftMargin=18*mm, rightMargin=18*mm, topMargin=16*mm, bottomMargin=18*mm,
                        title='Système de gestion de stock automatisé', author='Allegra Digital Ground')
s = []
s.append(Image(F + 'img/logo_adg.png', width=24*mm, height=19*mm, hAlign='LEFT'))
s.append(Spacer(1, 4))
s.append(Paragraph('Système de gestion de stock automatisé', H1))
s.append(Paragraph('Comment ça marche, ce qui est automatisé, et comment on l\'installe. Construit autour du template « Gestion de stock » de Desire.', SUB))

s.append(Paragraph('L\'idée en une phrase', H2))
s.append(Paragraph('Le commerçant ne touche plus au tableau : <font name="WSB">il remplit deux petits formulaires sur son téléphone</font> (une vente, un arrivage), et le système range tout dans le template, calcule le stock et le prévient sur WhatsApp quand il faut agir.', B))

s.append(Paragraph('Les 4 outils et leur rôle', H2))
tb = Table([
    [Paragraph('<font name="WSB">Outil</font>', B), Paragraph('<font name="WSB">Son rôle</font>', B), Paragraph('<font name="WSB">Image simple</font>', B)],
    [Paragraph('Google Sheets (le template)', B), Paragraph('Garde toutes les données et fait tous les calculs : stock, valeur, marge, état, quantité à commander.', B), Paragraph('La mémoire', B)],
    [Paragraph('Formulaires n8n', B), Paragraph('Saisir une vente ou un arrivage en 20 secondes, sur téléphone, sans ouvrir le tableau.', B), Paragraph('La porte d\'entrée', B)],
    [Paragraph('n8n', B), Paragraph('Lit les formulaires, écrit dans le tableau, décide qui prévenir, et déclenche les messages à 8 h et 19 h.', B), Paragraph('Le moteur', B)],
    [Paragraph('WhatsApp (API Meta)', B), Paragraph('Envoie les messages au patron et la confirmation au client.', B), Paragraph('La voix', B)],
], colWidths=[42*mm, 100*mm, 32*mm])
tb.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), LIGHT), ('LINEBELOW', (0,0), (-1,-1), 0.6, colors.HexColor('#dde3f5')),
                        ('VALIGN', (0,0), (-1,-1), 'TOP'), ('TOPPADDING', (0,0), (-1,-1), 5), ('BOTTOMPADDING', (0,0), (-1,-1), 5)]))
s.append(tb)
s.append(Spacer(1, 4))
s.append(Paragraph('<font name="WSB">Règle d\'or</font> : le tableau calcule, n8n transporte. Si on change une formule dans le template, les automatisations continuent de marcher.', B))
s.append(Paragraph('Le schéma', H2))
s.append(schema())

s.append(PageBreak())
s.append(Paragraph('Les 4 automatisations', H2))
s.append(auto(1, 'Une vente', 'le vendeur remplit le formulaire « Nouvelle commande » (client, téléphone, code produit, quantité, adresse).',
    ['n8n lit l\'onglet Produits et retrouve le produit, son prix et son stock.',
     'Il calcule le montant, le coût d\'achat et le stock restant.',
     'Il ajoute la ligne dans l\'onglet <font name="WSB">Commandes</font> : le stock baisse tout seul dans le tableau.',
     'Il prévient le patron, puis envoie une confirmation au client.',
     'Si le stock passe sous le seuil d\'alerte, il envoie une alerte au patron.'],
    [('Patron :', 'Nouvelle commande reçue. Client : Jean (0812345678). Produit : Huile 5 L, quantité 2 bidons. Montant : 30…'),
     ('Client :', 'Bonjour Jean, votre commande est bien enregistrée : Huile 5 L, quantité 2 bidons, montant 30…'),
     ('Patron :', 'Alerte stock de votre boutique : Stock bas pour Huile 5 L (code P002). Il reste 1 bidon…')]))
s.append(auto(2, 'Un arrivage de marchandise', 'le magasinier remplit le formulaire « Arrivage » à chaque livraison (code produit, quantité, prix d\'achat, fournisseur).',
    ['n8n retrouve le produit (si le prix est vide, il prend le prix d\'achat habituel).',
     'Il ajoute la ligne dans l\'onglet <font name="WSB">Arrivages</font> : le stock monte tout seul.',
     'Il prévient le patron avec le nouveau stock.'],
    [('Patron :', 'Marchandise reçue dans votre boutique : Huile 5 L, quantité 10 bidons, fournisseur Grossiste B. Le stock est maintenant de 11 bidons.')], GREEN))
s.append(auto(3, 'Le point du matin', 'chaque jour à 8 h, tout seul.',
    ['n8n lit l\'onglet Produits.',
     'Il garde les produits « À commander » et « Rupture », avec la quantité conseillée et le fournisseur.',
     'S\'il y en a, il envoie la liste au patron. S\'il n\'y en a pas, il ne dérange personne.'],
    [('Patron :', 'Bonjour, point du stock du 11/10/2026 : 2 produit(s) à recommander. Liste : Riz 25 kg : 8 sacs chez Grossiste A ; Huile 5 L : 8 bidons…')], colors.HexColor('#e07b00')))
s.append(auto(4, 'Le bilan du soir', 'chaque jour à 19 h, tout seul.',
    ['n8n lit les commandes du jour et le stock.',
     'Il calcule le nombre de commandes, les ventes, la marge et les commandes pas encore livrées.',
     'Il envoie le bilan au patron.'],
    [('Patron :', 'Bilan de votre boutique du 11/10/2026 : 12 commande(s), ventes 450, marge brute 80. Commandes pas encore livrées : 3…')], colors.HexColor('#e07b00')))
s.append(Paragraph('Les chiffres des messages sont des exemples.', SM))

s.append(Paragraph('Une journée type chez le commerçant', H2))
for x in ['<font name="WSB">8 h</font> : le patron reçoit la liste de ce qu\'il faut recommander, et chez qui.',
          '<font name="WSB">10 h</font> : la livraison du grossiste arrive. Le magasinier remplit le formulaire « Arrivage » : le stock est à jour.',
          '<font name="WSB">Toute la journée</font> : chaque vente passe par le formulaire. Le patron et le client sont prévenus, les alertes partent toutes seules.',
          '<font name="WSB">19 h</font> : le bilan du jour arrive. Le patron change le statut des commandes livrées ou annulées dans le tableau.']:
    s.append(Paragraph('•&nbsp;&nbsp;' + x, B))

s.append(Paragraph('Ce qu\'il faut pour l\'installer', H2))
s += bullets(['Un compte Google (pour le tableau).',
              'Un compte n8n : n8n Cloud (payant) ou n8n installé sur un petit serveur.',
              'Un compte WhatsApp Business API chez Meta, avec un numéro qui n\'est pas déjà dans l\'appli WhatsApp, et les 6 modèles de messages validés.',
              '<font name="WSB">Coûts à prévoir</font> : l\'abonnement ou le serveur n8n, et les messages WhatsApp (Meta fait payer chaque message de modèle). Vérifier les tarifs du moment avant de fixer le prix au client.'])

s.append(Paragraph('Ordre de mise en place', H2))
for i, x in enumerate(['Lancer tout de suite la demande chez Meta (application + 6 modèles) : c\'est le plus long.',
                       'Mettre le template dans Google Sheets, saisir 2 ou 3 produits de test.',
                       'Importer les 4 workflows dans n8n, brancher Google Sheets, tester les formulaires sans WhatsApp.',
                       'Brancher WhatsApp quand les modèles sont validés, refaire une vente et un arrivage de test.',
                       'Tester le point du matin et le bilan du soir avec le bouton « Test workflow ».',
                       'Activer les 4 workflows et donner les liens des 2 formulaires au vendeur et au magasinier.'], 1):
    s.append(Paragraph(f'{i}.&nbsp;&nbsp;{x}', B))

s.append(Paragraph('Ce que le système ne fait pas (encore)', H2))
s += bullets(['Il ne lit pas les messages WhatsApp des clients : c\'est le vendeur qui saisit la commande dans le formulaire.',
              'Il ne prévient pas le client quand sa commande est livrée.',
              'Un seul point de vente par tableau.',
              'Il ne remplace pas un inventaire : compter le stock de temps en temps et corriger.'])
s.append(Paragraph('Plus tard, si les clients le demandent', H2))
s += bullets(['Commande directe par WhatsApp : le client écrit au numéro de la boutique et la commande s\'enregistre toute seule.',
              'Message au client quand le statut passe à « Livrée ».',
              'Plusieurs boutiques dans un seul tableau de bord.'])
s.append(Spacer(1, 6))
s.append(Paragraph('<font name="WSB">État au 11 octobre 2026</font> : les 4 automatisations sont construites et leur code est testé sur des données d\'exemple. Elles n\'ont pas encore tourné dans un vrai n8n : c\'est la prochaine étape, avant toute vente.', SM))
doc.build(s, onFirstPage=footer, onLaterPages=footer)
print('ok')
