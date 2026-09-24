# -*- coding: utf-8 -*-
"""Met en page la philosophie de design (philosophie-design.md) en PDF."""
import os

from reportlab.platypus import Frame, Paragraph, Spacer

from build import (BODY, CW, H, INK, LEAD, MB, ML, MR, MT, W, inline, mono,
                   paper, rings)
from reportlab.pdfgen.canvas import Canvas

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    lines = open(os.path.join(HERE, "philosophie-design.md"), encoding="utf-8").read()
    paras = [p.strip() for p in lines.split("\n\n") if p.strip()]
    titre = paras[0].lstrip("# ").strip()
    sous = paras[1].strip("*")
    corps = paras[2:]

    out = os.path.join(HERE, "philosophie-design.pdf")
    c = Canvas(out, pagesize=(W, H))
    c.setTitle("Stratigraphie Lumineuse — philosophie de design")
    c.setAuthor("DigitalMikaelson")
    paper(c)
    mono(c, ML, H - 54, "MANIFESTE")
    mono(c, W - MR, H - 54, "STRATIGRAPHIE LUMINEUSE", anchor="r")
    c.setStrokeColor(INK)
    c.setLineWidth(0.4)
    c.line(ML, H - 62, W - MR, H - 62)
    rings(c, W - MR - 34, H - 120, 34, seed=1750, copper_r=21)
    c.setFillColor(INK)
    c.setFont("Display", 32)
    c.drawString(ML - 1, H - 132, titre)

    story = [Paragraph(inline(sous), LEAD), Spacer(1, 4)]
    story += [Paragraph(inline(p), BODY) for p in corps]
    f = Frame(ML, MB - 10, CW, H - MT - MB - 60, leftPadding=0, rightPadding=0,
              topPadding=0, bottomPadding=0)
    f.addFromList(story, c)
    if story:
        raise SystemExit("Le texte ne tient pas sur une page")

    c.setStrokeColor(INK)
    c.line(ML, 58, W - MR, 58)
    mono(c, ML, 44, "DIGITALMIKAELSON")
    mono(c, W - MR, 44, "MMXXVI", anchor="r")
    c.showPage()
    c.save()
    print(out)


if __name__ == "__main__":
    main()
