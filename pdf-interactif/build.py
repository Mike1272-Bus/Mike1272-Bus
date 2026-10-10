"""Remplace les {{LIENS}} par ceux de liens.json, puis Chrome imprime le PDF (les liens restent cliquables)."""
import json, os, re, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
links = json.load(open(os.path.join(HERE, "liens.json")))
html = open(os.path.join(HERE, "modele.html")).read()
html = re.sub(r"\{\{(\w+)\}\}", lambda m: links[m.group(1)].replace("&", "&amp;"), html)
tmp = os.path.join(HERE, "_build.html"); open(tmp, "w").write(html)
out = os.path.join(HERE, "feuille_de_route_modele.pdf")
subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=4000",
                f"--print-to-pdf={out}", "file://" + tmp], check=True, capture_output=True)
os.remove(tmp)
print("ok", out)
