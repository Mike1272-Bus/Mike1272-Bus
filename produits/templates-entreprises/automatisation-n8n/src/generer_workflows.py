"""Génère les 4 workflows n8n (WhatsApp) du système de gestion de stock automatisé.
Usage : python3 src/generer_workflows.py   (depuis le dossier automatisation-n8n)"""
import json, uuid

def nid(): return str(uuid.uuid4())
SHEET = "COLLE_ICI_LE_LIEN_DU_GOOGLE_SHEET"
SENDER = "CHOISIS_TON_NUMERO_WHATSAPP_BUSINESS"
PATRON = "243XXXXXXXXX"
RANGE_PRODUITS = "A4:P204"

def doc(): return {"__rl": True, "value": SHEET, "mode": "url"}
def sheet(n): return {"__rl": True, "value": n, "mode": "name"}
READ_FMT = {"outputFormatting": {"values": {"general": "UNFORMATTED_VALUE", "date": "SERIAL_NUMBER"}}}

def read_node(name, sheetname, pos, produits=False, once=False):
    opts = dict(READ_FMT)
    if produits:
        opts["dataLocationOnSheet"] = {"values": {"rangeDefinition": "specifyRangeA1", "range": RANGE_PRODUITS}}
    n = {"parameters": {"documentId": doc(), "sheetName": sheet(sheetname), "options": opts},
         "name": name, "type": "n8n-nodes-base.googleSheets", "typeVersion": 4.5, "position": pos, "id": nid(),
         "alwaysOutputData": True}
    if once: n["executeOnce"] = True
    return n

def append_node(name, sheetname, pos):
    return {"parameters": {"operation": "append", "documentId": doc(), "sheetName": sheet(sheetname),
        "columns": {"mappingMode": "autoMapInputData", "value": {}, "matchingColumns": [], "schema": []},
        "options": {"cellFormat": "USER_ENTERED", "handlingExtraData": "ignoreIt"}},
        "name": name, "type": "n8n-nodes-base.googleSheets", "typeVersion": 4.5, "position": pos, "id": nid()}

def code_node(name, js, pos):
    return {"parameters": {"jsCode": js}, "name": name, "type": "n8n-nodes-base.code", "typeVersion": 2, "position": pos, "id": nid()}

def wa_node(name, template, params, pos, to=PATRON, soft=False):
    n = {"parameters": {"resource": "message", "operation": "sendTemplate", "phoneNumberId": SENDER,
        "recipientPhoneNumber": to, "template": f"{template}|fr",
        "components": {"component": [{"type": "body", "bodyParameters": {"parameter": [{"type": "text", "text": p} for p in params]}}]}},
        "name": name, "type": "n8n-nodes-base.whatsApp", "typeVersion": 1.1, "position": pos, "id": nid()}
    if soft: n["onError"] = "continueRegularOutput"
    return n

def form_node(name, title, desc, fields, done, pos):
    return {"parameters": {"formTitle": title, "formDescription": desc, "formFields": {"values": fields},
        "options": {"respondWithOptions": {"values": {"formSubmittedText": done}}}},
        "name": name, "type": "n8n-nodes-base.formTrigger", "typeVersion": 2.2, "position": pos, "id": nid(), "webhookId": nid()}

def schedule_node(name, hour, pos):
    return {"parameters": {"rule": {"interval": [{"field": "days", "triggerAtHour": hour, "triggerAtMinute": 0}]}},
        "name": name, "type": "n8n-nodes-base.scheduleTrigger", "typeVersion": 1.2, "position": pos, "id": nid()}

def if_node(name, expr, pos):
    return {"parameters": {"conditions": {
        "options": {"caseSensitive": True, "leftValue": "", "typeValidation": "loose", "version": 2},
        "conditions": [{"id": nid(), "leftValue": expr, "rightValue": True, "operator": {"type": "boolean", "operation": "true", "singleValue": True}}],
        "combinator": "and"}, "options": {}},
        "name": name, "type": "n8n-nodes-base.if", "typeVersion": 2.2, "position": pos, "id": nid()}

def link(*names):
    c = {}
    for a, b in zip(names, names[1:]):
        c.setdefault(a, {"main": [[]]})["main"][0].append({"node": b, "type": "main", "index": 0})
    return c

def wf(name, nodes, conns):
    return {"name": name, "nodes": nodes, "connections": conns,
            "settings": {"executionOrder": "v1", "timezone": "Africa/Kinshasa"}, "pinData": {}}

HELPERS = r"""
// Lit un nombre, même s'il arrive en texte (« 1 250 », « 12,5 »)
function num(v) {
  if (typeof v === 'number') return v;
  if (v === undefined || v === null || v === '') return 0;
  const s = String(v).replace(/\s/g, '').replace(',', '.');
  const n = parseFloat(s.replace(/[^0-9.\-]/g, ''));
  return isNaN(n) ? 0 : n;
}
// WhatsApp (modèles Meta) : pas de retour à la ligne ni de case vide dans les variables
function wa(v) {
  const s = String(v ?? '').replace(/[\n\r\t]+/g, ' ').replace(/ {2,}/g, ' ').trim();
  return s === '' ? '-' : s.slice(0, 900);
}
// Numéro RDC au format international : 0812345678 -> 243812345678
function telIntl(v) {
  let d = String(v ?? '').replace(/\D/g, '');
  if (d.startsWith('00')) d = d.slice(2);
  if (d.startsWith('0')) d = '243' + d.slice(1);
  else if (d.length === 9) d = '243' + d;
  return d;
}
function trouver(code) {
  const c = String(code || '').trim().toUpperCase();
  const p = $input.all().map(i => i.json).find(x => String(x['Code'] || '').trim().toUpperCase() === c);
  if (!p) throw new Error(`Code produit inconnu : ${c}. Vérifiez l'onglet Produits.`);
  return [c, p];
}
"""

# ---------------- 1. Vente ----------------
JS_VENTE = HELPERS + r"""
const f = $('Formulaire de commande').first().json;
const qte = num(f['Quantité']);
if (qte <= 0) throw new Error('La quantité doit être supérieure à 0.');
const [code, produit] = trouver(f['Code produit']);
const prixVente = num(produit['Prix de vente (1 unité)']);
const prixAchat = num(produit["Prix d'achat (1 unité)"]);
const stockApres = num(produit['Stock actuel']) - qte;
const seuil = num(produit["Seuil d'alerte"]);
const unite = produit['Unité'] || '';

return [{ json: {
  // Colonnes de l'onglet Commandes
  'Date': $now.toFormat('yyyy-MM-dd HH:mm'),
  'Client': f['Nom du client'],
  'Téléphone': String(f['Téléphone du client']),
  'Code produit': code,
  'Produit': produit['Produit'],
  'Quantité': qte,
  'Prix unitaire': prixVente,
  'Montant': qte * prixVente,
  "Coût d'achat": qte * prixAchat,
  'Statut': 'Nouvelle',
  'Adresse': f['Adresse de livraison'] || '',
  'Note': f['Note'] || '',
  // Pour les messages (pas écrit dans le tableau)
  _stockApres: stockApres,
  _seuil: seuil,
  _wa: {
    client: wa(f['Nom du client']), tel: wa(f['Téléphone du client']), telClient: telIntl(f['Téléphone du client']),
    produit: wa(produit['Produit']), code: wa(code), qte: wa(`${qte} ${unite}`), montant: wa(qte * prixVente),
    adresse: wa(f['Adresse de livraison']), stock: wa(`${stockApres} ${unite}`), seuil: wa(seuil),
    etat: stockApres <= 0 ? 'Rupture de stock' : 'Stock bas',
    fournisseur: wa(produit['Fournisseur'] || 'non renseigné'),
  },
}}];
"""
P = "={{ $('Préparer la commande').item.json._wa.%s }}"
n1 = [
  form_node("Formulaire de commande", "Nouvelle commande", "À remplir par le vendeur pour chaque commande reçue (WhatsApp, appel, boutique).",
    [{"fieldLabel": "Nom du client", "requiredField": True}, {"fieldLabel": "Téléphone du client", "placeholder": "ex. 0812345678", "requiredField": True},
     {"fieldLabel": "Code produit", "placeholder": "ex. P001", "requiredField": True}, {"fieldLabel": "Quantité", "fieldType": "number", "requiredField": True},
     {"fieldLabel": "Adresse de livraison"}, {"fieldLabel": "Note", "fieldType": "textarea"}], "Commande enregistrée. Merci !", [0, 0]),
  read_node("Lire les produits", "Produits", [220, 0], produits=True),
  code_node("Préparer la commande", JS_VENTE, [440, 0]),
  append_node("Ajouter dans Commandes", "Commandes", [660, 0]),
  wa_node("WhatsApp patron : nouvelle commande", "nouvelle_commande", [P % k for k in ("client", "tel", "produit", "qte", "montant", "adresse", "stock")], [880, 0]),
  wa_node("WhatsApp client : confirmation", "confirmation_commande", [P % k for k in ("client", "produit", "qte", "montant")], [1100, 0],
          to="={{ $('Préparer la commande').item.json._wa.telClient }}", soft=True),
  if_node("Stock bas ?", "={{ $('Préparer la commande').item.json._stockApres <= $('Préparer la commande').item.json._seuil }}", [1320, 0]),
  wa_node("WhatsApp patron : alerte stock", "alerte_stock_bas", [P % k for k in ("etat", "produit", "code", "stock", "seuil")], [1540, -100]),
]
W1 = wf("Stock 1 : vente → tableau, WhatsApp patron et client, alerte stock", n1,
        link(*[n["name"] for n in n1]))

# ---------------- 2. Arrivage ----------------
JS_ARRIVAGE = HELPERS + r"""
const f = $('Formulaire d\'arrivage').first().json;
const qte = num(f['Quantité reçue']);
if (qte <= 0) throw new Error('La quantité reçue doit être supérieure à 0.');
const [code, produit] = trouver(f['Code produit']);
const prix = num(f["Prix d'achat unitaire"]) || num(produit["Prix d'achat (1 unité)"]);
const fournisseur = f['Fournisseur'] || produit['Fournisseur'] || '';
const unite = produit['Unité'] || '';
const stockApres = num(produit['Stock actuel']) + qte;

return [{ json: {
  // Colonnes de l'onglet Arrivages
  'Date': $now.toFormat('yyyy-MM-dd HH:mm'),
  'Code produit': code,
  'Produit': produit['Produit'],
  'Quantité': qte,
  "Prix d'achat unitaire": prix,
  'Montant': qte * prix,
  'Fournisseur': fournisseur,
  'Note': f['Note'] || '',
  _wa: { produit: wa(produit['Produit']), qte: wa(`${qte} ${unite}`), stock: wa(`${stockApres} ${unite}`), fournisseur: wa(fournisseur || 'non renseigné') },
}}];
"""
A = "={{ $('Préparer l\\'arrivage').item.json._wa.%s }}"
n3 = [
  form_node("Formulaire d'arrivage", "Arrivage de marchandise", "À remplir à chaque livraison reçue d'un fournisseur.",
    [{"fieldLabel": "Code produit", "placeholder": "ex. P001", "requiredField": True}, {"fieldLabel": "Quantité reçue", "fieldType": "number", "requiredField": True},
     {"fieldLabel": "Prix d'achat unitaire", "fieldType": "number", "placeholder": "laisser vide = prix habituel"},
     {"fieldLabel": "Fournisseur"}, {"fieldLabel": "Note", "fieldType": "textarea"}], "Arrivage enregistré. Merci !", [0, 0]),
  read_node("Lire les produits", "Produits", [220, 0], produits=True),
  code_node("Préparer l'arrivage", JS_ARRIVAGE, [440, 0]),
  append_node("Ajouter dans Arrivages", "Arrivages", [660, 0]),
  wa_node("WhatsApp patron : marchandise reçue", "arrivage_stock", [A % k for k in ("produit", "qte", "fournisseur", "stock")], [880, 0]),
]
W3 = wf("Stock 3 : arrivage de marchandise → tableau + WhatsApp", n3, link(*[n["name"] for n in n3]))

# ---------------- 4. Point du matin ----------------
JS_MATIN = HELPERS + r"""
const produits = $input.all().map(i => i.json).filter(p => p['Code']);
const aRecommander = produits.filter(p => p['État'] === 'À commander' || p['État'] === 'Rupture');
const ligne = (p) => {
  const q = num(p['Quantité à commander']);
  const four = p['Fournisseur'] ? ` chez ${p['Fournisseur']}` : '';
  return `${p['Produit']} : ${q} ${p['Unité'] || ''}${four}`.replace(/ {2,}/g, ' ');
};
const rupture = produits.filter(p => p['État'] === 'Rupture').map(p => p['Produit']);
return [{ json: {
  nb: aRecommander.length,
  jour: wa($now.toFormat('dd/MM/yyyy')),
  combien: wa(aRecommander.length),
  liste: wa(aRecommander.map(ligne).join(' ; ') || 'aucun'),
  rupture: wa(rupture.join(', ') || 'aucun'),
}}];
"""
n4 = [
  schedule_node("Chaque matin à 8 h", 8, [0, 0]),
  read_node("Lire les produits", "Produits", [220, 0], produits=True),
  code_node("Préparer la liste à commander", JS_MATIN, [440, 0]),
  if_node("Quelque chose à commander ?", "={{ $json.nb > 0 }}", [660, 0]),
  wa_node("WhatsApp patron : à commander aujourd'hui", "stock_du_matin", ["={{ $json.%s }}" % k for k in ("jour", "combien", "liste", "rupture")], [880, -100]),
]
W4 = wf("Stock 4 : point du matin, liste à commander", n4, link(*[n["name"] for n in n4]))

# ---------------- 2. Bilan du soir (inchangé, plage produits élargie) ----------------
old = json.load(open("workflow_2_bilan_du_soir.json"))
for n in old["nodes"]:
    rng = n["parameters"].get("options", {}).get("dataLocationOnSheet")
    if rng: rng["values"]["range"] = RANGE_PRODUITS
old["name"] = "Stock 2 : bilan du soir sur WhatsApp"

for fname, w in [("workflow_1_commande_alerte_stock.json", W1), ("workflow_2_bilan_du_soir.json", old),
                 ("workflow_3_arrivage_marchandise.json", W3), ("workflow_4_point_du_matin.json", W4)]:
    json.dump(w, open(fname, "w"), ensure_ascii=False, indent=2)
    print("ok", fname, len(w["nodes"]), "nœuds")
