# Ciblage des entreprises structurées (à partir de la semaine du 9 nov.)

Google Sheet : « My automation - Ciblage entreprises structurées »
https://docs.google.com/spreadsheets/d/16dgAeDbysGYepnkNM0DpHNy1j9J9DKhsXn_VAe28rRw/edit
Onglet « Entreprises » (une ligne par entreprise, score et priorité calculés tout seuls) + onglet « Méthode ».

## Les signaux relevés
Pub Meta active · nombre de pubs actives · ancienneté de la pub (jours) · nombre de points de vente · service client · vend en gros · déjà un logiciel (en moins).
Score : pub active +3, +1 par pub (5 max), ancienneté 14 j +1 / 30 j +2, 2 points de vente +2 / 3 et plus +3, service client +2, vente en gros +2, logiciel -2.
Priorité : A = 10 et plus · B = 6 à 9 · C = moins de 6.

## Comment on collecte (testé le 31 oct.)
- **Bibliothèque des pubs Meta** : lecture automatique qui fonctionne (pays : RDC, pubs actives, mot-clé). On récupère le nom de la page, la date de début, le texte de la pub, le numéro WhatsApp, et le nombre de pubs par page. Mots-clés : grossiste kinshasa, dépôt, supermarché, alimentation, quincaillerie, pharmacie, distributeur, boissons, cosmétiques gros.
- **Google Maps / recherche web** : adresses, nombre de boutiques, numéro du service client.
- **Pages Facebook / Instagram / site** : vente en gros, service client, logiciel déjà en place.
Règle : ne jamais inventer, laisser vide ce qu'on ne sait pas.

## Premier test (31 oct., mot-clé « grossiste kinshasa ») : 4 entreprises ajoutées
MOMBONGO NA KIN (5 pubs, priorité A) · MOMBONGO DIRECT (B) · RN SHOPPING (B) · MINA SHOP (B). Plus 6 entreprises déjà connues (KYRA, Le Comptoir des Parfums, ORCA, Muda Markets, Klammshop, Biofoods).

## Plan
Semaine du 2 nov. : WhatsApp (chaîne + nouvelles catégories). Semaine du 9 nov. : collecte de 30 à 50 entreprises structurées, puis appels (script : `script_appel_entreprises.md`), les priorités A d'abord.
