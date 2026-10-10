import sys
OUT = sys.argv[1]
ICON = {
 'form': '<rect x="22" y="12" width="56" height="76" rx="10" fill="none" stroke="#fff" stroke-width="8"/><path d="M36 38h28M36 54h28M36 70h16" stroke="#fff" stroke-width="8" stroke-linecap="round"/>',
 'sheet': '<rect x="14" y="18" width="72" height="64" rx="9" fill="none" stroke="#fff" stroke-width="8"/><path d="M14 40h72M14 61h72M40 18v64" stroke="#fff" stroke-width="7"/>',
 'code': '<path d="M36 26L14 50l22 24M64 26l22 24-22 24" fill="none" stroke="#fff" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>',
 'wa': '<path d="M50 14C30 14 14 29 14 47c0 7 2 13 6 18l-5 18 19-5c5 2 10 3 16 3 20 0 36-15 36-34S70 14 50 14z" fill="#fff"/>',
 'if': '<path d="M50 12L88 50 50 88 12 50z" fill="none" stroke="#fff" stroke-width="8" stroke-linejoin="round"/><path d="M50 36v18M50 64v2" stroke="#fff" stroke-width="8" stroke-linecap="round"/>',
 'clock': '<circle cx="50" cy="50" r="36" fill="none" stroke="#fff" stroke-width="8"/><path d="M50 30v21l14 9" stroke="#fff" stroke-width="8" stroke-linecap="round" fill="none"/>',
 'bolt': '<path d="M56 10L22 56h24l-6 34 36-48H52z" fill="#fff"/>',
}
COL = {'form':'#2342ff','sheet':'#16a34a','code':'#6b4dff','wa':'#16a34a','if':'#e07b00','clock':'#e07b00','bolt':'#2342ff'}
WF1 = [('form','Formulaire de commande','Déclencheur'),('sheet','Lire les produits','Google Sheets'),('code','Préparer la commande','Calcul'),
       ('sheet','Ajouter dans Commandes','Google Sheets'),('wa','WhatsApp : nouvelle commande','WhatsApp'),('if','Stock bas ?','Condition'),('wa','WhatsApp : alerte stock','WhatsApp')]
CAP1 = ["Le vendeur envoie le formulaire","n8n lit vos produits et vos prix","Il calcule le montant et le stock restant",
        "Il écrit la commande dans votre tableau","Il vous prévient sur WhatsApp","Le stock est bas ?","Oui : une alerte pour recommander"]
WF2 = [('clock','Chaque soir à 19 h','Déclencheur'),('sheet','Lire les commandes','Google Sheets'),('sheet','Lire les produits','Google Sheets'),
       ('code','Préparer le bilan','Calcul'),('wa','WhatsApp : bilan du soir','WhatsApp')]
CAP2 = ["19 h : n8n se réveille tout seul","Il lit les commandes du jour","Il regarde votre stock","Il prépare le bilan","Et vous l'envoie sur WhatsApp"]
Y1 = [600 + i*182 for i in range(7)]
Y2 = [640 + i*215 for i in range(5)]
T1 = [6.4 + i*1.9 for i in range(7)]
T2 = [22.0 + i*1.35 for i in range(5)]

def node(pref, i, n, y):
    ic, title, sub = n
    return f'''<div class="node" id="{pref}n{i}" style="top:{y}px"><div class="nring" id="{pref}r{i}"></div><div class="nic" style="background:{COL[ic]}"><svg viewBox="0 0 100 100">{ICON[ic]}</svg></div><div class="nt">{title}</div><div class="ns">{sub}</div><div class="ok" id="{pref}k{i}">✓</div></div>'''
def links(pref, ys, labels={}):
    out=[]
    for i in range(len(ys)-1):
        y1=ys[i]+128; y2=ys[i+1]
        out.append(f'<path id="{pref}l{i}" d="M540 {y1} L540 {y2}" />')
    return '\n'.join(out)
html = open(sys.argv[2]).read()
html = html.replace('%%WF1NODES%%','\n'.join(node('a',i,n,Y1[i]) for i,n in enumerate(WF1)))
html = html.replace('%%WF2NODES%%','\n'.join(node('b',i,n,Y2[i]) for i,n in enumerate(WF2)))
html = html.replace('%%WF1LINKS%%', links('a',Y1)).replace('%%WF2LINKS%%', links('b',Y2))
html = html.replace('%%CAP1%%','\n'.join(f'<div class="cap tL" id="ac{i}">{c}</div>' for i,c in enumerate(CAP1)))
html = html.replace('%%CAP2%%','\n'.join(f'<div class="cap tD" id="bc{i}">{c}</div>' for i,c in enumerate(CAP2)))
html = html.replace('%%Y1%%',str(Y1)).replace('%%Y2%%',str(Y2)).replace('%%T1%%',str(T1)).replace('%%T2%%',str(T2))
open(OUT,'w').write(html)
print('ok')
