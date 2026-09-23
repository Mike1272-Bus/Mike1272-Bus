# -*- coding: utf-8 -*-
"""Génère le carnet PDF « Les vérités cachées » (Stratigraphie Lumineuse)."""
import math
import os
import random
import re

from reportlab.lib.colors import Color, HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Flowable, Frame, KeepTogether,
                                NextPageTemplate, PageBreak, PageTemplate,
                                Paragraph, Spacer, Table, TableStyle)

from contenu import CHAPITRES

FONTS = ("/root/.claude/skills/synced/e026b770-e89c-4483-b66d-20d65ff8a59c_"
         "b603504e-56cc-43ac-8018-db062e692acb/canvas-design/canvas-fonts/")
for name, fn in [("Crimson", "CrimsonPro-Regular"), ("Crimson-B", "CrimsonPro-Bold"),
                 ("Crimson-I", "CrimsonPro-Italic"), ("ISerif", "InstrumentSerif-Regular"),
                 ("ISerif-I", "InstrumentSerif-Italic"), ("Mono", "DMMono-Regular"),
                 ("Display", "Italiana-Regular"), ("Jura", "Jura-Light")]:
    pdfmetrics.registerFont(TTFont(name, FONTS + fn + ".ttf"))
pdfmetrics.registerFontFamily("Crimson", normal="Crimson", bold="Crimson-B",
                              italic="Crimson-I", boldItalic="Crimson-B")

W, H = A4
ML, MR, MT, MB = 74, 74, 92, 82
CW = W - ML - MR

PAPER = HexColor("#F3EEE4")
INK = HexColor("#1D1916")
SOFT = HexColor("#6F665C")
RULE = HexColor("#CBBFAE")
COPPER = HexColor("#A8592F")


def ink(a):
    return Color(INK.red, INK.green, INK.blue, alpha=a)


# ------------------------------------------------------------------ styles
BODY = ParagraphStyle("body", fontName="Crimson", fontSize=11.2, leading=15.6,
                      textColor=INK, spaceAfter=7, alignment=TA_LEFT)
LEAD = ParagraphStyle("lead", parent=BODY, fontName="Crimson-I", fontSize=12.6,
                      leading=17.6, textColor=SOFT, spaceAfter=14)
H2 = ParagraphStyle("h2", fontName="ISerif", fontSize=19, leading=23, textColor=INK,
                    spaceBefore=20, spaceAfter=9, keepWithNext=1)
LABEL = ParagraphStyle("label", fontName="Mono", fontSize=6.8, leading=9,
                       textColor=COPPER, spaceBefore=7, spaceAfter=2.5,
                       keepWithNext=1)
BULLET = ParagraphStyle("bullet", parent=BODY, leftIndent=15, bulletIndent=2,
                        spaceAfter=3.5)
NUMBERED = ParagraphStyle("numbered", parent=BULLET, bulletFontName="Mono",
                          bulletFontSize=7.5, bulletColor=COPPER)
QUOTE = ParagraphStyle("quote", fontName="ISerif-I", fontSize=15, leading=20,
                       textColor=INK, leftIndent=18, spaceBefore=8, spaceAfter=12)
CELL = ParagraphStyle("cell", fontName="Crimson", fontSize=9.8, leading=12.4,
                      textColor=INK)
HEAD = ParagraphStyle("head", fontName="Mono", fontSize=6.4, leading=8.4,
                      textColor=SOFT)


def inline(s):
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"\*(.+?)\*", r"<i>\1</i>", s)
    return s


def spaced(s, n=1):
    return (" " * n).join(s)


# ------------------------------------------------------------------ flowables
class QuoteRule(Flowable):
    """Citation avec un filet de cuivre à gauche."""

    def __init__(self, text):
        super().__init__()
        self.p = Paragraph(inline(text), QUOTE)

    def wrap(self, aw, ah):
        w, h = self.p.wrap(aw, ah)
        self.h = h + QUOTE.spaceBefore + QUOTE.spaceAfter
        return aw, self.h

    def draw(self):
        c = self.canv
        top = self.h - QUOTE.spaceBefore
        bottom = QUOTE.spaceAfter
        c.setStrokeColor(COPPER)
        c.setLineWidth(1.1)
        c.line(2, bottom + 2, 2, top - 3)
        self.p.drawOn(c, 0, bottom)


class SetChapter(Flowable):
    def __init__(self, idx):
        super().__init__()
        self.idx = idx

    def wrap(self, aw, ah):
        return 0, 0

    def draw(self):
        self.canv._doctemplate.chapter = self.idx


class Marker(Flowable):
    """Enregistre la page de départ d'un chapitre (pour le sommaire)."""

    def __init__(self, idx):
        super().__init__()
        self.idx = idx

    def wrap(self, aw, ah):
        return 0, 0

    def draw(self):
        self.canv._doctemplate.pages[self.idx] = self.canv.getPageNumber()


def table(rows):
    data = []
    for i, r in enumerate(rows):
        st = HEAD if i == 0 else CELL
        txt = [c.upper() if i == 0 else c for c in r]
        data.append([Paragraph(inline(c), st) for c in txt])
    n = len(rows[0])
    widths = {2: [0.36, 0.64], 3: [0.3, 0.35, 0.35], 4: [0.25, 0.17, 0.3, 0.28]}
    cw = [CW * f for f in widths.get(n, [1 / n] * n)]
    t = Table(data, colWidths=cw, repeatRows=1, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 5.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5.5),
        ("LINEABOVE", (0, 0), (-1, 0), 0.9, INK),
        ("LINEBELOW", (0, 0), (-1, 0), 0.4, INK),
        ("LINEBELOW", (0, 1), (-1, -1), 0.25, RULE),
    ]))
    return [Spacer(1, 6), t, Spacer(1, 12)]


def parse(texte):
    out, rows, first = [], [], True
    for raw in texte.strip().split("\n") + [""]:
        line = raw.strip()
        if rows and not line.startswith("|"):
            out += table(rows)
            rows = []
        if not line:
            continue
        if line.startswith("|"):
            rows.append([c.strip() for c in line.strip("|").split("|")])
        elif line.startswith("### "):
            nb = "\u00a0"
            out.append(Paragraph((nb * 3).join(nb.join(w) for w in line[4:].split()),
                                 LABEL))
        elif line.startswith("## "):
            out.append(Paragraph(inline(line[3:]), H2))
        elif line.startswith("- "):
            out.append(Paragraph(inline(line[2:]), BULLET,
                                 bulletText="–"))
        elif re.match(r"^\d+\. ", line):
            n, rest = line.split(" ", 1)
            out.append(Paragraph(inline(rest), NUMBERED, bulletText=n.rstrip(".")))
        elif line.startswith("> "):
            out.append(QuoteRule(line[2:]))
        else:
            out.append(Paragraph(inline(line), LEAD if first else BODY))
        first = False
    return out


# ------------------------------------------------------------------ drawing
def paper(c):
    c.setFillColor(PAPER)
    c.rect(0, 0, W, H, stroke=0, fill=1)


def mono(c, x, y, s, size=6.4, color=SOFT, anchor="l", track=1):
    s = spaced(s, track) if track else s
    c.setFont("Mono", size)
    c.setFillColor(color)
    if anchor == "r":
        c.drawRightString(x, y, s)
    elif anchor == "c":
        c.drawCentredString(x, y, s)
    else:
        c.drawString(x, y, s)


def rings(c, cx, cy, rmax, seed, copper_r):
    """Cernes concentriques irréguliers ; un seul cerne en cuivre."""
    rnd = random.Random(seed)
    r, k = 5.0, 0
    while r < rmax:
        phase = rnd.uniform(0, math.tau)
        amp = 0.35 + 0.9 * (r / rmax) ** 1.6
        p = c.beginPath()
        steps = 180
        for i in range(steps + 1):
            a = math.tau * i / steps
            rr = r + amp * math.sin(3 * a + phase) + 0.45 * amp * math.sin(7 * a - phase)
            x, y = cx + rr * math.cos(a), cy + rr * math.sin(a)
            p.moveTo(x, y) if i == 0 else p.lineTo(x, y)
        p.close()
        c.setStrokeColor(ink(0.18 + 0.5 * (1 - r / rmax) ** 0.7))
        c.setLineWidth(0.32 if k % 5 else 0.55)
        c.drawPath(p, stroke=1, fill=0)
        r += rnd.uniform(1.7, 3.9) * (0.8 + 0.5 * r / rmax)
        k += 1
    c.setStrokeColor(COPPER)
    c.setLineWidth(1.2)
    c.circle(cx, cy, copper_r, stroke=1, fill=0)


def cover(c, doc):
    paper(c)
    mono(c, ML, H - 54, "PLANCHE 00")
    mono(c, W - MR, H - 54, "STRATIGRAPHIE LUMINEUSE", anchor="r")
    c.setStrokeColor(ink(0.8))
    c.setLineWidth(0.4)
    c.line(ML, H - 62, W - MR, H - 62)

    cx, cy, rmax = W / 2, 528, 208
    rings(c, cx, cy, rmax, seed=1750, copper_r=131)
    # graduation radiale : l'échelle du temps lue du centre vers l'extérieur
    c.setStrokeColor(INK)
    c.setLineWidth(0.45)
    c.line(cx, cy, cx + rmax + 22, cy)
    for r, lab in [(0, "− 5 000"), (131, "PRÉSENT"), (168, "+ 20"), (rmax, "+ 1 000")]:
        x = cx + r
        c.line(x, cy - 3.5, x, cy + 3.5)
    mono(c, cx + rmax + 28, cy - 2.2, "ANS", size=5.6, track=1)
    c.setFillColor(COPPER)
    a = math.radians(-38)
    c.circle(cx + 131 * math.cos(a), cy + 131 * math.sin(a), 2.6, stroke=0, fill=1)
    # repères au pied du cercle
    yl = cy - rmax - 22
    for x, lab in [(cx - rmax, "Ø 416"), (cx, "N = 8"), (cx + rmax, "FIG. 1")]:
        mono(c, x, yl, lab, size=5.6, anchor="c")

    c.setFillColor(INK)
    c.setFont("Display", 50)
    c.drawString(ML - 2, 196, "Les vérités cachées")
    c.setFont("Crimson-I", 15)
    c.setFillColor(SOFT)
    c.drawString(ML, 168, "de la vente de produits digitaux")
    c.setStrokeColor(COPPER)
    c.setLineWidth(1.1)
    c.line(ML, 146, ML + 38, 146)
    mono(c, ML, 124, "CARNET D'ÉTUDE EN HUIT COUPES")
    mono(c, ML, 112, "DU PASSÉ LE PLUS ANCIEN AU FUTUR LE PLUS LOINTAIN")
    c.setStrokeColor(ink(0.8))
    c.setLineWidth(0.4)
    c.line(ML, 70, W - MR, 70)
    mono(c, ML, 56, "DIGITALMIKAELSON")
    mono(c, W / 2, 56, "KINSHASA", anchor="c")
    mono(c, W - MR, 56, "MMXXVI", anchor="r")


def strata(c, x0, y0, w, h, seed, n=92):
    """Strates horizontales ondulées, comme une coupe géologique."""
    rnd = random.Random(seed)
    waves = [(rnd.uniform(0.6, 1.8), rnd.uniform(0, math.tau), rnd.uniform(1.5, 5.5))
             for _ in range(3)]
    for i in range(n):
        t = i / (n - 1)
        base = y0 + t * h
        drift = rnd.uniform(-0.6, 0.6)
        p = c.beginPath()
        steps = 140
        for j in range(steps + 1):
            u = j / steps
            dy = sum(a * math.sin(u * f * math.tau + ph + t * 2.2)
                     for f, ph, a in waves) * (0.35 + 0.65 * math.sin(math.pi * t))
            x, y = x0 + u * w, base + dy + drift
            p.moveTo(x, y) if j == 0 else p.lineTo(x, y)
        c.setStrokeColor(ink(0.16 + 0.58 * t ** 1.4))
        c.setLineWidth(0.3 if i % 6 else 0.55)
        c.drawPath(p, stroke=1, fill=0)


EPOCHS = [(0.06, "− 5 000"), (0.56, "PRÉSENT"), (0.72, "+ 20"), (0.94, "+ 1 000")]


def opener(c, doc):
    paper(c)
    ch = CHAPITRES[doc.chapter]
    i = doc.chapter + 1
    mono(c, ML, H - 54, "PLANCHE %02d" % i)
    mono(c, W - MR, H - 54, "COUPE %s / VIII" % ch["num"], anchor="r")
    c.setStrokeColor(ink(0.8))
    c.setLineWidth(0.4)
    c.line(ML, H - 62, W - MR, H - 62)

    c.setFillColor(INK)
    c.setFont("Display", 112)
    c.drawString(ML - 4, H - 196, ch["num"])

    # bloc de strates
    bx, by, bw, bh = ML, 262, CW, 250
    strata(c, bx, by, bw, bh, seed=97 * i + 13)
    # axe du temps
    ay = by - 24
    c.setStrokeColor(INK)
    c.setLineWidth(0.45)
    c.line(bx, ay, bx + bw, ay)
    for k in range(41):
        x = bx + bw * k / 40
        c.line(x, ay, x, ay - (4 if k % 5 == 0 else 2))
    for p, lab in EPOCHS:
        mono(c, bx + bw * p, ay - 14, lab, size=5.6, anchor="c")
    # la carotte de cuivre
    c.setStrokeColor(COPPER)
    c.setFillColor(COPPER)
    if ch["pos"] is not None:
        x = bx + bw * ch["pos"]
        c.setLineWidth(1.3)
        c.line(x, ay + 4, x, by + bh + 16)
        c.circle(x, ay, 2.4, stroke=0, fill=1)
        mono(c, x + 7, by + bh + 11, ch["epoque"], size=6, color=COPPER)
    else:
        x, y = bx + bw * 0.5, by + bh + 36
        c.setLineWidth(1.2)
        c.circle(x, y, 13, stroke=1, fill=0)
        c.circle(x, y, 2.4, stroke=0, fill=1)
        mono(c, x + 22, y - 2, ch["epoque"], size=6, color=COPPER)

    c.setFillColor(INK)
    c.setFont("Display", 34)
    c.drawString(ML - 1, 166, ch["titre"])
    c.setFont("Crimson-I", 13)
    c.setFillColor(SOFT)
    c.drawString(ML, 142, ch["sous_titre"])
    c.setStrokeColor(ink(0.8))
    c.setLineWidth(0.4)
    c.line(ML, 70, W - MR, 70)
    mono(c, ML, 56, "LES VÉRITÉS CACHÉES")
    mono(c, W - MR, 56, str(c.getPageNumber()), anchor="r", track=0)


def body(c, doc):
    paper(c)
    ch = CHAPITRES[doc.chapter]
    mono(c, ML, H - 54, "LES VÉRITÉS CACHÉES")
    mono(c, W - MR, H - 54, "%s  —  %s" % (ch["num"], ch["titre"].upper()), anchor="r")
    c.setStrokeColor(ink(0.8))
    c.setLineWidth(0.4)
    c.line(ML, H - 62, W - MR, H - 62)
    c.setStrokeColor(COPPER)
    c.setLineWidth(1.1)
    c.line(ML, H - 62, ML + 22, H - 62)
    mono(c, W / 2, 48, str(c.getPageNumber()), anchor="c", track=0)


def sommaire_page(c, doc):
    paper(c)
    mono(c, ML, H - 54, "SOMMAIRE")
    mono(c, W - MR, H - 54, "HUIT COUPES", anchor="r")
    c.setStrokeColor(ink(0.8))
    c.setLineWidth(0.4)
    c.line(ML, H - 62, W - MR, H - 62)
    c.setFillColor(INK)
    c.setFont("Display", 40)
    c.drawString(ML - 2, H - 150, "Sommaire")
    top, step = H - 222, 60
    for i, ch in enumerate(CHAPITRES):
        y = top - i * step
        c.setStrokeColor(RULE)
        c.setLineWidth(0.3)
        c.line(ML, y - 20, W - MR, y - 20)
        mono(c, ML, y + 3, ch["num"], size=7.5, color=COPPER, track=0)
        c.setFillColor(INK)
        c.setFont("ISerif", 19)
        c.drawString(ML + 44, y, ch["titre"])
        c.setFont("Crimson-I", 10.2)
        c.setFillColor(SOFT)
        c.drawString(ML + 44, y - 13, ch["sous_titre"])
        mono(c, W - MR - 40, y + 3, ch["epoque"], size=5.6, anchor="r")
        pg = doc.known_pages.get(i)
        mono(c, W - MR, y + 3, str(pg) if pg else "", size=7.5, anchor="r", track=0)
    # petite légende
    mono(c, ML, 110, "LECTURE : CHAQUE COUPE EST SITUÉE SUR L'AXE DU TEMPS,", size=5.6)
    mono(c, ML, 100, "DE − 5 000 ANS À + 1 000 ANS. LE FILET DE CUIVRE MARQUE L'ÉPOQUE.", size=5.6)
    c.setStrokeColor(ink(0.8))
    c.setLineWidth(0.4)
    c.line(ML, 70, W - MR, 70)
    mono(c, W / 2, 48, str(c.getPageNumber()), anchor="c", track=0)


def closing(c, doc):
    paper(c)
    cx, cy = W / 2, H / 2 + 40
    rings(c, cx, cy, 70, seed=2046, copper_r=44)
    c.setFillColor(INK)
    c.setFont("ISerif-I", 17)
    lines = ["Ce qui est rare, ce n'est pas le savoir.",
             "C'est l'exécution constante, pendant des années,",
             "quand personne ne regarde."]
    for k, s in enumerate(lines):
        c.drawCentredString(W / 2, cy - 130 - k * 24, s)
    mono(c, W / 2, cy - 222, "FIN DU CARNET", anchor="c")
    c.setStrokeColor(ink(0.8))
    c.setLineWidth(0.4)
    c.line(ML, 70, W - MR, 70)
    mono(c, ML, 56, "DIGITALMIKAELSON")
    mono(c, W - MR, 56, "MMXXVI", anchor="r")


# ------------------------------------------------------------------ build
class Doc(BaseDocTemplate):
    def __init__(self, path, known):
        super().__init__(path, pagesize=A4, leftMargin=ML, rightMargin=MR,
                         topMargin=MT, bottomMargin=MB,
                         title="Les vérités cachées de la vente de produits digitaux",
                         author="DigitalMikaelson")
        self.chapter = 0
        self.pages = {}
        self.known_pages = known
        full = Frame(0, 0, W, H, id="full", leftPadding=0, rightPadding=0,
                     topPadding=0, bottomPadding=0)
        text = Frame(ML, MB, CW, H - MT - MB, id="text", leftPadding=0,
                     rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([
            PageTemplate("cover", [full], onPage=cover),
            PageTemplate("sommaire", [full], onPage=sommaire_page),
            PageTemplate("opener", [full], onPage=opener),
            PageTemplate("body", [text], onPage=body),
            PageTemplate("closing", [full], onPage=closing),
        ])


def story():
    s = [Spacer(1, 1), NextPageTemplate("sommaire"), PageBreak(), Spacer(1, 1)]
    for i, ch in enumerate(CHAPITRES):
        s += [SetChapter(i), NextPageTemplate("opener"), PageBreak(),
              Marker(i), Spacer(1, 1), NextPageTemplate("body"), PageBreak()]
        s += parse(ch["texte"])
    s += [NextPageTemplate("closing"), PageBreak(), Spacer(1, 1)]
    return s


def build(path):
    first = Doc(path, {})
    first.build(story())
    Doc(path, first.pages).build(story())


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "les-verites-cachees.pdf")
    build(out)
    print(out)
