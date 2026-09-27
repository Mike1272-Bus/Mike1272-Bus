"""Met en page plan_30_jours.md en PDF aux couleurs DigitalMikaelson."""
import os, re, subprocess, markdown

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "plan_30_jours.md")
ASSETS = os.path.abspath(os.path.join(HERE, "..", "..", "page-chariow", "visuels", "src"))

md = open(SRC, encoding="utf-8").read()
md = re.sub(r"^# .*\n", "", md, count=1)
lines, prev = [], ""
for line in md.split("\n"):
    is_item = bool(re.match(r"^(\s*[-*] |\s*\d+\. )", line))
    prev_item = bool(re.match(r"^(\s*[-*] |\s*\d+\. )", prev))
    if is_item and prev.strip() and not prev_item and not prev.startswith((">", "|")):
        lines.append("")
    lines.append(line); prev = line
md = "\n".join(lines)
md = md.replace("- [ ] ", "- <span class='box'></span> ")
body = markdown.markdown(md, extensions=["tables", "sane_lists"])
body = re.sub(r"<td>([A-E])</td>", r"<td><span class='t t\1'>\1</span></td>", body)
body = body.replace("<hr />", "")
body = re.sub(r"<h2>(\d+)\. ", r"<h2><span class='n'>\1</span>", body)

html = f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><style>
@font-face {{ font-family: 'Baloo 2'; font-weight: 800; src: url('file://{ASSETS}/Baloo2-ExtraBold.ttf'); }}
@font-face {{ font-family: 'Work Sans'; font-weight: 400; src: url('file://{ASSETS}/worksans-400.ttf'); }}
@font-face {{ font-family: 'Work Sans'; font-weight: 700; src: url('file://{ASSETS}/worksans-700.ttf'); }}
@page {{ size: A4; margin: 18mm 16mm 20mm; }}
@page :first {{ margin: 0; }}
:root {{ --navy:#201f5b; --deep:#15144a; --gold:#f7c21b; --blue:#1f8fd1; --cyan:#6fd3f5; --ink:#1d1c3f; }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font-family: 'Work Sans'; font-size: 10.5pt; line-height: 1.5; color: var(--ink); }}
.cover {{ width: 210mm; height: 297mm; position: relative; overflow: hidden; color: #fff; page-break-after: always;
  background: radial-gradient(circle at 85% 20%, #2d2c7a 0%, var(--navy) 45%, var(--deep) 100%); }}
.cover .ring {{ position: absolute; right: -70mm; top: -30mm; width: 160mm; height: 160mm; border-radius: 50%; border: 5mm solid var(--gold); opacity: .9; }}
.cover .logo {{ position: absolute; left: 18mm; top: 18mm; background: #fff; border-radius: 6mm; padding: 4mm 6mm; }}
.cover .logo img {{ width: 52mm; display: block; }}
.cover .kicker {{ position: absolute; left: 18mm; top: 92mm; font-family: 'Baloo 2'; font-size: 16pt; color: var(--cyan); letter-spacing: .5pt; }}
.cover h1 {{ position: absolute; left: 18mm; top: 102mm; margin: 0; font-family: 'Baloo 2'; font-size: 52pt; line-height: .98; }}
.cover h1 span {{ color: var(--gold); }}
.cover .sub {{ position: absolute; left: 18mm; top: 172mm; width: 120mm; font-size: 13pt; line-height: 1.45; opacity: .92; }}
.cover .goals {{ position: absolute; left: 18mm; top: 205mm; display: flex; flex-direction: column; gap: 4mm; }}
.cover .goal {{ background: var(--gold); color: var(--navy); font-family: 'Baloo 2'; font-size: 15pt; border-radius: 10mm; padding: 2.5mm 7mm 1mm; width: max-content; }}
.cover .foot {{ position: absolute; left: 18mm; bottom: 16mm; font-size: 10pt; opacity: .75; }}
h2 {{ font-family: 'Baloo 2'; font-weight: 800; color: var(--navy); font-size: 20pt; line-height: 1.1; margin: 0 0 4mm; padding-top: 2mm;
      display: flex; align-items: center; gap: 4mm; page-break-after: avoid; }}
h2 .n {{ flex: none; width: 11mm; height: 11mm; border-radius: 50%; background: var(--gold); color: var(--navy); display: inline-flex;
         align-items: center; justify-content: center; font-size: 16pt; padding-top: 1.2mm; }}
h2:not(:first-of-type) {{ margin-top: 9mm; }}
h2.break {{ page-break-before: always; margin-top: 0; }}
h3 {{ font-family: 'Baloo 2'; color: var(--blue); font-size: 13pt; margin: 5mm 0 2mm; page-break-after: avoid; }}
p {{ margin: 0 0 3mm; }}
strong {{ color: var(--navy); }}
ul, ol {{ margin: 0 0 3mm; padding-left: 6mm; }}
li {{ margin-bottom: 1.4mm; }}
li::marker {{ color: var(--blue); }}
ul li:has(.box) {{ list-style: none; margin-left: -6mm; }}
.box {{ display: inline-block; width: 3.6mm; height: 3.6mm; border: .5mm solid var(--navy); border-radius: 1mm; margin-right: 2mm; vertical-align: -.5mm; }}
blockquote {{ margin: 3mm 0; padding: 3mm 5mm; background: #fff7d6; border-left: 1.5mm solid var(--gold); border-radius: 0 3mm 3mm 0; }}
blockquote p {{ margin: 0; }}
code {{ font-family: 'Work Sans'; background: #eef3ff; color: var(--blue); padding: .3mm 1.5mm; border-radius: 1mm; font-size: 9.5pt; }}
table {{ width: 100%; border-collapse: separate; border-spacing: 0; margin: 2mm 0 5mm; font-size: 9.3pt; line-height: 1.38;
         border-radius: 3mm; overflow: hidden; border: .3mm solid #d9d9ec; }}
thead th {{ background: var(--navy); color: #fff; font-family: 'Baloo 2'; font-weight: 800; font-size: 10.5pt; text-align: left; padding: 2.4mm 3mm 1.4mm; }}
td {{ padding: 2mm 3mm; vertical-align: top; border-top: .3mm solid #e6e6f2; }}
tbody tr:nth-child(even) td {{ background: #f6f6fc; }}
tr {{ page-break-inside: avoid; }}
.t {{ display: inline-block; width: 6.5mm; height: 6.5mm; border-radius: 50%; text-align: center; font-family: 'Baloo 2'; font-size: 10pt; line-height: 7.2mm; }}
.tA {{ background: var(--gold); color: var(--navy); }} .tB {{ background: var(--navy); color: #fff; }} .tC {{ background: var(--cyan); color: var(--navy); }}
.tD {{ background: var(--blue); color: #fff; }} .tE {{ background: #25d366; color: var(--navy); }}
.cal td:first-child {{ font-family: 'Baloo 2'; font-size: 12pt; color: var(--navy); text-align: center; width: 10mm; }}
</style></head><body>
<section class="cover">
  <div class="ring"></div>
  <div class="logo"><img src="file://{ASSETS}/logo_dm.png"></div>
  <div class="kicker">TIKTOK + INSTAGRAM</div>
  <h1>Stratégie<br>organique<br><span>30 jours</span></h1>
  <div class="sub">Attirer des abonnés, faire réagir l'algorithme et vendre le guide « Gagne ta vie sans diplôme ».</div>
  <div class="goals"><div class="goal">3 000 abonnés</div><div class="goal">5 messages « EBOOK » par jour</div><div class="goal">Des commentaires sur chaque post</div></div>
  <div class="foot">DigitalMikaelson · Plan de publication</div>
</section>
<main>{body}</main>
</body></html>"""
# le calendrier est le tableau qui suit le titre de la section 7
html = re.sub(r"(<h2><span class='n'>7</span>[\s\S]*?)<table>", r"\1<table class='cal'>", html, count=1)
for n in ("2", "4", "7", "8"):
    html = html.replace(f"<h2><span class='n'>{n}</span>", f"<h2 class='break'><span class='n'>{n}</span>")
open(os.path.join(HERE, "plan_30_jours.html"), "w", encoding="utf-8").write(html)
subprocess.run(["node", os.path.join(HERE, "print.mjs")], check=True)
