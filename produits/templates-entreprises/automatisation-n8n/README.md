# Automatisation n8n : commerces avec du stock

Pour : boutiques, dépôts, pharmacies, quincailleries, alimentations. Prolonge le template Excel « Gestion de stock » de Desire.
Se vend **en service d'installation** (voir `../plan.md`), pas en template à faire soi-même.

## Ce que ça fait

| Workflow | Déclencheur | Ce qui se passe |
|---|---|---|
| `workflow_1_commande_alerte_stock.json` | Le vendeur remplit un formulaire en ligne (sur téléphone) pour chaque commande | 1. La commande s'ajoute seule dans l'onglet **Commandes** du Google Sheet. 2. Le patron reçoit un message **WhatsApp** « Nouvelle commande ». 3. Si le stock passe sous le seuil : alerte WhatsApp « Stock bas » ou « Rupture de stock ». |
| `workflow_2_bilan_du_soir.json` | Chaque soir à 19 h (heure de Kinshasa) | Message **WhatsApp** : nombre de commandes du jour, total des ventes, marge brute, commandes pas encore livrées, produits à commander ou en rupture. |

Le stock et le tableau de bord du Google Sheet tiennent compte des commandes du formulaire automatiquement. Une commande passée en **Annulée** (colonne Statut) ne compte plus.

## Les fichiers

- `gestion_de_stock_auto.xlsx` : la version du template avec l'onglet **Commandes** (à ouvrir dans Google Sheets, pas Excel)
- `workflow_1_commande_alerte_stock.json` et `workflow_2_bilan_du_soir.json` : à importer dans n8n (alertes WhatsApp)
- `modeles_whatsapp_meta.md` : les 3 messages à faire valider par Meta
- `variante-telegram/` : la même chose avec Telegram (gratuit, sans validation Meta), si un client utilise Telegram

## Installation chez un client (environ 1 h)

**1. Le Google Sheet**
1. Sur le Google Drive du client (ou le tien) : Nouveau > Importer `gestion_de_stock_auto.xlsx`, puis Ouvrir avec Google Sheets, puis Fichier > Enregistrer au format Google Sheets.
2. Supprimer les lignes EXEMPLE, remplir les produits avec le client (comme pour la version Excel).
3. Ne pas renommer les onglets ni les titres de colonnes : n8n s'en sert.

**2. WhatsApp (API officielle de Meta, une seule fois pour toi)**

On utilise l'API officielle : c'est la seule qui ne risque pas de faire bloquer le numéro. Conseil : **un seul numéro « Allegra Alertes »** à ton nom, qui envoie les alertes à tous les patrons clients. Tu le configures une fois, ensuite chaque nouveau client = juste son numéro à ajouter.

1. Sur **developers.facebook.com** : Mes apps > Créer une app > type **Business**, puis ajouter le produit **WhatsApp**. Meta donne un **numéro de test** gratuit.
2. Dans WhatsApp > Configuration de l'API : ajouter ton propre numéro comme destinataire de test (Meta t'envoie un code).
3. Créer les **3 modèles de messages** de `modeles_whatsapp_meta.md` et attendre leur validation.
4. Noter le **jeton d'accès** (Access Token) et l'**ID du compte WhatsApp Business** (WhatsApp Business Account ID). Le jeton de test expire au bout de 24 h : pour un vrai client, créer un jeton permanent (Paramètres de l'entreprise > Utilisateurs système).
5. Pour passer en vrai : ajouter un vrai numéro (un numéro qui **n'est pas** déjà utilisé dans l'appli WhatsApp), vérifier l'entreprise chez Meta, ajouter un moyen de paiement. **Meta fait payer chaque message de modèle**, selon le pays : vérifier le tarif du moment sur la page des prix WhatsApp Business de Meta avant de fixer le prix client.

**3. n8n**
1. Dans n8n : Workflows > Importer depuis un fichier > choisir chaque `.json`.
2. Créer les identifiants (Credentials) : **Google Sheets OAuth2** (compte Google du Sheet) et **WhatsApp API** (jeton d'accès + ID du compte WhatsApp Business).
3. Dans chaque nœud Google Sheets : remplacer `COLLE_ICI_LE_LIEN_DU_GOOGLE_SHEET` par le lien du Sheet, choisir l'identifiant Google.
4. Dans chaque nœud WhatsApp : choisir l'identifiant WhatsApp, choisir le numéro d'envoi dans la liste (à la place de `CHOISIS_TON_NUMERO_WHATSAPP_BUSINESS`), remplacer `243XXXXXXXXX` par le numéro du patron (indicatif 243, sans + ni 0), et vérifier que le bon modèle est sélectionné.
5. **Tester avant d'activer** : ouvrir le workflow 1, cliquer « Test workflow », remplir le formulaire avec un vrai code produit. Vérifier la ligne dans Commandes et le message WhatsApp. Faire pareil pour le workflow 2 (« Test workflow »).
6. Activer les deux workflows. Dans le nœud « Formulaire de commande », copier le **lien de production** du formulaire et l'envoyer au vendeur (à épingler sur son téléphone).

## Hébergement de n8n

Deux options : n8n Cloud (payant, rien à installer) ou n8n auto-hébergé sur un petit serveur (moins cher, mais il faut l'installer et le maintenir). Vérifier les prix du moment avant de fixer le tarif client. Un même n8n peut servir plusieurs clients (un jeu de workflows par client).

## À savoir / limites

- **Testé** : les formules du Google Sheet (avec de fausses commandes), le code des 2 nœuds Code (avec de fausses données), et tous les noms de réglages des nœuds comparés au code source de n8n (version 2.15). **Pas encore testé dans un vrai n8n avec un vrai Google Sheet et WhatsApp** : à faire une fois sur ton compte avant la première installation chez un client, et corriger si un nœud demande un réglage.
- WhatsApp passe par l'API officielle de Meta : modèles validés, coût par message, numéro dédié. Les services « WhatsApp non officiels » (qui connectent un numéro normal) sont moins chers mais le numéro peut être bloqué par WhatsApp : on ne les utilise pas chez les clients.
- Pas de compte Meta prêt ? La `variante-telegram/` marche tout de suite et gratuitement.
- Le formulaire demande le **code produit** (ex. P001) : donner au vendeur la liste des codes.
- Deux commandes envoyées à la même seconde peuvent fausser l'alerte de stock (pas le stock lui-même, qui est recalculé par le Sheet).

## Prix (à fixer, rien n'est décidé)

Installation : [PRIX] · Suivi au mois : [PRIX]
