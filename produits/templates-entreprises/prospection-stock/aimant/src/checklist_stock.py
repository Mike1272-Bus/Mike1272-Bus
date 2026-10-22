# Checklist « Votre stock vous fait-il perdre de l'argent ? » (aimant de la chaîne WhatsApp My automation)
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
import os

F = "/mnt/skills/examples/canvas-design/canvas-fonts/"
pdfmetrics.registerFont(TTFont("Titre", F + "BricolageGrotesque-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Texte", F + "WorkSans-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Gras", F + "WorkSans-Bold.ttf"))

ENCRE, ACCENT, FOND, NUIT, DOUX, BLANC = (HexColor(c) for c in ("#12142a", "#5b57f0", "#eceef6", "#1c1f3d", "#a9acd0", "#ffffff"))
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.abspath(os.path.join(ICI, "../../../../.."))
LOGO = os.path.join(RACINE, "site-web/landing-systeme-stock/logo/wordmark_ink.png")
SORTIE = os.path.join(ICI, "..", "checklist_stock_my_automation.pdf")

QUESTIONS = [
    "Je connais le stock exact de chaque produit, sans avoir à recompter.",
    "Quand un client demande un article, je sais en moins d'une minute s'il est disponible.",
    "Je suis prévenu avant qu'un produit tombe en rupture, pas quand le client le demande.",
    "Le mois dernier, mon cahier ou mon Excel correspondait à ce qu'il y avait vraiment en rayon.",
    "Chaque soir, je connais mes ventes et ma marge de la journée, sans faire de calcul.",
    "Je vois ce qui se vend dans ma boutique, même quand je n'y suis pas.",
    "Je sais quoi racheter, et chez quel fournisseur, sans chercher.",
]

W, H = A4
c = canvas.Canvas(SORTIE, pagesize=A4)
c.setTitle("Votre stock vous fait-il perdre de l'argent ? Checklist My automation")
c.setFillColor(FOND); c.rect(0, 0, W, H, fill=1, stroke=0)
M = 42

def wrap(txt, font, size, width):
    mots, lignes, l = txt.split(), [], ""
    for m in mots:
        t = (l + " " + m).strip()
        if pdfmetrics.stringWidth(t, font, size) <= width: l = t
        else: lignes.append(l); l = m
    return lignes + [l]

# En-tête
y = H - 44
if os.path.exists(LOGO):
    img = ImageReader(LOGO); iw, ih = img.getSize(); lw = 120
    c.drawImage(img, M, y - lw * ih / iw, lw, lw * ih / iw, mask="auto")
c.setFillColor(ACCENT); c.setFont("Gras", 9)
c.drawRightString(W - M, y - 10, "CHECKLIST · 2 MINUTES")
y -= 62
c.setFillColor(ENCRE); c.setFont("Titre", 27)
for l in wrap("Votre stock vous fait-il perdre de l'argent ?", "Titre", 27, W - 2 * M):
    c.drawString(M, y, l); y -= 32
c.setFont("Texte", 11.5); c.setFillColor(HexColor("#3d4063"))
for l in wrap("7 affirmations. Cochez honnêtement « oui » ou « non ». Chaque « non » est une fuite : du temps ou des ventes qui partent sans qu'on le voie.", "Texte", 11.5, W - 2 * M):
    c.drawString(M, y, l); y -= 16
y -= 14

# Questions
for i, q in enumerate(QUESTIONS, 1):
    lignes = wrap(q, "Texte", 12, W - 2 * M - 175)
    h = 14 + 15 * len(lignes)
    c.setFillColor(BLANC); c.roundRect(M, y - h, W - 2 * M, h, 10, fill=1, stroke=0)
    c.setFillColor(ACCENT); c.circle(M + 22, y - h / 2, 12, fill=1, stroke=0)
    c.setFillColor(BLANC); c.setFont("Gras", 11); c.drawCentredString(M + 22, y - h / 2 - 4, str(i))
    c.setFillColor(ENCRE); c.setFont("Texte", 12)
    ty = y - h / 2 + 7.5 * (len(lignes) - 1) - 4
    for l in lignes: c.drawString(M + 46, ty, l); ty -= 15
    for k, lab in enumerate(("Oui", "Non")):
        bx = W - M - 112 + k * 56
        c.setStrokeColor(ENCRE); c.setLineWidth(1.2); c.roundRect(bx, y - h / 2 - 7, 14, 14, 3, fill=0, stroke=1)
        c.setFont("Texte", 11); c.drawString(bx + 19, y - h / 2 - 4, lab)
    y -= h + 6

# Résultat
y -= 16
c.setFillColor(ENCRE); c.setFont("Titre", 15); c.drawString(M, y, "Votre résultat"); y -= 20
RES = [("Aucun « non »", "Bravo : votre suivi est solide. Gardez ce rythme."),
       ("1 ou 2 « non »", "Il y a des fuites. Elles se corrigent vite, souvent sans rien changer à vos habitudes."),
       ("3 « non » ou plus", "Le travail à la main vous coûte du temps et des ventes chaque semaine. C'est le bon moment d'en parler.")]
for t, d in RES:
    c.setFillColor(ACCENT); c.setFont("Gras", 11); c.drawString(M, y, t)
    c.setFillColor(ENCRE); c.setFont("Texte", 11)
    for l in wrap(d, "Texte", 11, W - 2 * M - 120): c.drawString(M + 120, y, l); y -= 15
    y -= 5

# Bandeau final
bh = 80
c.setFillColor(NUIT); c.roundRect(M, 34, W - 2 * M, bh, 14, fill=1, stroke=0)
c.setFillColor(BLANC); c.setFont("Titre", 15)
c.drawString(M + 20, 34 + bh - 26, "Calculons ensemble ce que ça vous coûte")
c.setFillColor(DOUX); c.setFont("Texte", 10.5)
c.drawString(M + 20, 34 + bh - 43, "15 minutes en appel vidéo, gratuit et sans engagement, avec vos propres chiffres.")
c.setFillColor(HexColor("#25d366")); c.setFont("Gras", 12.5)
c.drawString(M + 20, 34 + 16, "WhatsApp : +243 831 710 181")
c.setFillColor(BLANC); c.setFont("Texte", 10.5)
c.drawRightString(W - M - 20, 34 + 17, "my-automation-rdc.vercel.app")
c.save()
print(SORTIE)
