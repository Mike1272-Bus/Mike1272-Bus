# Données nettoyées du fichier PROSPECTION.xlsx de Mike (lu le 13/10/2026)
import re
from openpyxl import load_workbook
SRC = 'PROSPECTION_original.xlsx'  # fichier de Mike, à mettre à côté du script

SEG = {  # type d'origine -> (segment, priorité, pourquoi)
 'COSMETIQUE': ('Cosmétique et parfumerie', 'A'), 'PARFUMERIE': ('Cosmétique et parfumerie', 'A'),
 'MAGASIN DE TELEPHOPHONE': ('Téléphones, électronique, informatique', 'A'), 'MAGASIN DE TELEPHONE': ('Téléphones, électronique, informatique', 'A'),
 'ELECTRONIQUE': ('Téléphones, électronique, informatique', 'A'), 'INFORMATIQUE': ('Téléphones, électronique, informatique', 'A'),
 'JEUX ET INFORMATIQUE': ('Téléphones, électronique, informatique', 'A'),
 'QUINCAILLERIES': ('Quincaillerie et peinture', 'A'), 'PEINTURE BATIMENT': ('Quincaillerie et peinture', 'A'),
 "BOUTIQUE D'HABILLEMENT": ('Habillement', 'B'), 'HABILLEMENT': ('Habillement', 'B'), 'HABILLEMENT FEMME': ('Habillement', 'B'),
 'HABILLEMENT ET DIVERS FEMME': ('Habillement', 'B'),
 'ENTREPOT': ('Entrepôt et distribution', 'B'), "PRODUCTION ET DISTRIBUTION D'EAU": ('Entrepôt et distribution', 'B'),
 'PHARMACEUTIQUE': ('Pharmacie', 'C'), 'PHARMACIE': ('Pharmacie', 'C'),
 "TRAITEMENT D'EAU": ('À vérifier', 'C'), 'CONSTRUCTION': ('À vérifier', 'C'),
}
FIX_NAME = {'ELETRONIC STORE': 'ELECTRONIC STORE', 'XIAIMI STORE KINSHASA': 'XIAOMI STORE KINSHASA'}

def load():
    wb = load_workbook(SRC); ws = wb.active
    rows = []
    for r in ws.iter_rows(min_row=2, values_only=True):
        _, n, nom, ville, tel, typ = r[:6]
        if not nom or not isinstance(n, int): continue
        nom = re.sub(r'\s+', ' ', str(nom)).strip()
        nom_aff = FIX_NAME.get(nom, nom)
        typ = str(typ).strip()
        seg, prio = SEG[typ]
        digits = re.sub(r'\D', '', str(tel))
        notes = []
        if nom != nom_aff: notes.append(f'Nom corrigé (fichier : {nom})')
        if not ville: notes.append('Ville manquante')
        if not digits.startswith('243'): notes.append('Numéro hors RDC (+90 = Turquie) : vérifier avant d\'écrire'); prio = 'C'
        if nom == 'BRICOKIN': notes.append('Le nom évoque le bricolage alors que le type est « cosmétique » : vérifier')
        if seg == 'Pharmacie': notes.append('Attendre la colonne « date de péremption » dans le template')
        if seg == 'À vérifier': notes.append('Besoin de stock à confirmer (service ou chantier, pas une boutique)')
        rows.append(dict(n=n, nom=nom_aff, ville=(ville or '').title() or '?', tel=str(tel).strip(), wa=digits,
                         type_orig=typ.replace('TELEPHOPHONE','TELEPHONE').capitalize(), seg=seg, prio=prio, notes='. '.join(notes)))
    return rows

HOOK = {
 'Téléphones, électronique, informatique': "Avec tous vos modèles, accessoires et pièces, savoir exactement ce qu'il reste en stock prend vite du temps.",
 'Cosmétique et parfumerie': "Avec autant de références, il arrive qu'un produit manque sans qu'on l'ait vu venir, ou qu'on dise « c'est fini » alors qu'il en restait.",
 'Quincaillerie et peinture': "Dans une quincaillerie, le stock coûte cher. Savoir ce qu'il reste et ce qu'il vaut, sans tout recompter, change beaucoup de choses.",
 'Habillement': "Entre les modèles, les tailles et les couleurs, savoir tout de suite si un article est encore disponible n'est pas toujours simple.",
 'Entrepôt et distribution': "Quand la marchandise entre et sort tous les jours, garder un stock juste et savoir quoi recommander devient vite un travail à plein temps.",
 'Pharmacie': "Avec autant de références, une rupture passe vite inaperçue, et un client qui ne trouve pas son produit va ailleurs.",
 'À vérifier': "Quand la marchandise entre et sort tous les jours, garder un stock juste prend vite du temps.",
}
def message1(nom, seg):
    return (f"Bonjour {nom} 👋\n\nJe suis Mike, d'Allegra Digital Ground.\n\n{HOOK[seg]}\n\n"
            "On a créé un système simple : vous notez vos ventes et vos arrivages depuis votre téléphone, "
            "le stock se calcule tout seul, et vous recevez sur WhatsApp les alertes de stock bas et le bilan du soir.\n\n"
            "Je vous envoie une vidéo de 37 secondes qui montre comment ça marche 👇\n\n"
            "Petite question : aujourd'hui, comment suivez-vous votre stock ? Cahier, Excel, ou de tête ?")
MESSAGE2 = ("Merci pour votre réponse 🙏\n\nVoici ce qui se passe à l'intérieur du système, étape par étape (35 secondes) 👇\n\n"
            "Je vous propose de vous le montrer avec vos propres produits, en appel vidéo WhatsApp de 15 minutes. "
            "Quel jour vous arrange cette semaine ?")
RELANCE1 = ("Bonjour {nom}, je reviens vers vous pour la petite vidéo envoyée il y a quelques jours. "
            "Le suivi du stock, c'est un sujet chez vous en ce moment ? Un simple oui ou non m'aide déjà 🙏")
RELANCE2 = ("Bonjour {nom}, dernier message de ma part sur ce sujet. "
            "Si un jour vous voulez voir le système avec vos produits, répondez simplement « STOCK » et je vous le montre en 15 minutes. Bonne journée !")
SEG_ORDER = ['Téléphones, électronique, informatique', 'Cosmétique et parfumerie', 'Quincaillerie et peinture',
             'Habillement', 'Entrepôt et distribution', 'Pharmacie', 'À vérifier']
def vague(r):
    if r['prio'] == 'A' and r['seg'] == 'Téléphones, électronique, informatique': return 1
    if r['prio'] == 'A': return 2
    return 3
