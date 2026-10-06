# Automatisation n8n : commerces avec du stock

Pour : boutiques, dépôts, pharmacies, quincailleries, alimentations. Prolonge le template Excel « Gestion de stock » de Desire.
Se vend **en service d'installation** (voir `../plan.md`), pas en template à faire soi-même.

## Ce que ça fait

| Workflow | Déclencheur | Ce qui se passe |
|---|---|---|
| `workflow_1_commande_alerte_stock.json` | Le vendeur remplit un formulaire en ligne (sur téléphone) pour chaque commande | 1. La commande s'ajoute seule dans l'onglet **Commandes** du Google Sheet. 2. Le patron reçoit un message Telegram « Nouvelle commande ». 3. Si le stock passe sous le seuil : alerte 🟠 « Stock bas » ou 🔴 « Rupture ». |
| `workflow_2_bilan_du_soir.json` | Chaque soir à 19 h (heure de Kinshasa) | Message Telegram : nombre de commandes du jour, total des ventes, marge brute, commandes pas encore livrées, produits à commander ou en rupture. |

Le stock et le tableau de bord du Google Sheet tiennent compte des commandes du formulaire automatiquement. Une commande passée en **Annulée** (colonne Statut) ne compte plus.

## Les fichiers

- `gestion_de_stock_auto.xlsx` : la version du template avec l'onglet **Commandes** (à ouvrir dans Google Sheets, pas Excel)
- `workflow_1_commande_alerte_stock.json` et `workflow_2_bilan_du_soir.json` : à importer dans n8n

## Installation chez un client (environ 1 h)

**1. Le Google Sheet**
1. Sur le Google Drive du client (ou le tien) : Nouveau > Importer `gestion_de_stock_auto.xlsx`, puis Ouvrir avec Google Sheets, puis Fichier > Enregistrer au format Google Sheets.
2. Supprimer les lignes EXEMPLE, remplir les produits avec le client (comme pour la version Excel).
3. Ne pas renommer les onglets ni les titres de colonnes : n8n s'en sert.

**2. Telegram (gratuit)**
1. Le patron installe Telegram. Dans Telegram, ouvrir **@BotFather**, envoyer `/newbot`, choisir un nom : on obtient un **token**.
2. Le patron envoie un message (n'importe quoi) à son nouveau bot.
3. Récupérer son **chat ID** : ouvrir **@userinfobot** dans Telegram, il le donne.

**3. n8n**
1. Dans n8n : Workflows > Importer depuis un fichier > choisir chaque `.json`.
2. Créer les identifiants (Credentials) : **Google Sheets OAuth2** (compte Google du Sheet) et **Telegram** (le token).
3. Dans chaque nœud Google Sheets : remplacer `COLLE_ICI_LE_LIEN_DU_GOOGLE_SHEET` par le lien du Sheet, choisir l'identifiant Google.
4. Dans chaque nœud Telegram : remplacer `COLLE_ICI_TON_CHAT_ID_TELEGRAM` par le chat ID, choisir l'identifiant Telegram.
5. **Tester avant d'activer** : ouvrir le workflow 1, cliquer « Test workflow », remplir le formulaire avec un vrai code produit. Vérifier la ligne dans Commandes et le message Telegram. Faire pareil pour le workflow 2 (« Test workflow »).
6. Activer les deux workflows. Dans le nœud « Formulaire de commande », copier le **lien de production** du formulaire et l'envoyer au vendeur (à épingler sur son téléphone).

## Hébergement de n8n

Deux options : n8n Cloud (payant, rien à installer) ou n8n auto-hébergé sur un petit serveur (moins cher, mais il faut l'installer et le maintenir). Vérifier les prix du moment avant de fixer le tarif client. Un même n8n peut servir plusieurs clients (un jeu de workflows par client).

## À savoir / limites

- **Testé** : les formules du Google Sheet (avec de fausses commandes), le code des 2 nœuds Code (avec de fausses données), et tous les noms de réglages des nœuds comparés au code source de n8n (version 2.15). **Pas encore testé dans un vrai n8n avec un vrai Google Sheet et Telegram** : à faire une fois sur ton compte avant la première installation chez un client, et corriger si un nœud demande un réglage.
- Pas de WhatsApp automatique : il faut l'API officielle de Meta (compte vérifié, coût par conversation). On commence par Telegram. Si le client préfère, on peut remplacer les nœuds Telegram par Gmail.
- Le formulaire demande le **code produit** (ex. P001) : donner au vendeur la liste des codes.
- Deux commandes envoyées à la même seconde peuvent fausser l'alerte de stock (pas le stock lui-même, qui est recalculé par le Sheet).

## Prix (à fixer, rien n'est décidé)

Installation : [PRIX] · Suivi au mois : [PRIX]
