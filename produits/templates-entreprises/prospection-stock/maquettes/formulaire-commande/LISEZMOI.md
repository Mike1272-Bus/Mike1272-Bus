# Formulaire de commande avec images et couleurs (L'Univers du crochet)

`index.html` : page pour téléphone. La personne choisit le modèle (illustration ou vraie photo), la couleur (l'illustration prend la couleur choisie), la quantité, donne ses coordonnées et appuie sur « Commander ».
Testé dans un navigateur : choix, quantité, champs obligatoires et message de commande fonctionnent.

## Comment la commande arrive
1. **Toujours** : WhatsApp s'ouvre avec la commande déjà écrite (modèle, couleur, quantité, nom, numéro, adresse). La personne appuie sur Envoyer : la boutique la reçoit. Pas de compte Meta, pas de serveur.
2. **En plus, si `lienEnregistrement` est rempli** : la commande s'enregistre aussi dans le Google Sheet (lien d'un workflow n8n en ligne avec un nœud Webhook en POST). À faire par le chat Automatisation.

## À remplir en haut du fichier (partie « À REMPLIR »)
- `whatsapp` : numéro de la boutique (243…, sans + ni 0)
- `MODELES` : nom, `photo` (ex. `photos/sac.jpg`, sinon l'illustration s'affiche), `prix`
- `COULEURS` : nom et code couleur

## Pour envoyer le lien sur WhatsApp
Mettre la page en ligne (hébergement gratuit de page statique, ex. Vercel ou GitHub Pages), puis envoyer le lien. Ne jamais citer les outils au client.

## Brancher la page au workflow (tout connecté)
`workflow_commande_depuis_la_page.json` = copie du Stock 1 qui marche, avec un seul changement : la commande arrive de la page (nœud Webhook « Commande depuis la page », POST, chemin `commande-crochet`) au lieu du formulaire n8n. La suite est identique : lire les produits → préparer → ajouter dans Commandes → WhatsApp patron → WhatsApp client → alerte stock bas.
Testé : la page envoie exactement les champs attendus (Nom du client, Téléphone du client, Code produit, Quantité, Adresse de livraison, Note avec la couleur) et le code de préparation les lit correctement. Pas encore testé dans n8n lui-même.

1. n8n → Importer depuis un fichier → ce JSON. Vérifier les identifiants Google Sheets et WhatsApp dans les nœuds. Activer.
2. Le lien du nœud Webhook (Production URL) est en `localhost` : la page en ligne ne peut pas l'atteindre. Il faut n8n accessible sur internet : tunnel pour tester (`cloudflared tunnel --url http://localhost:5678`), n8n hébergé pour un vrai client.
3. Coller `https://<adresse-publique>/webhook/commande-crochet` dans `lienEnregistrement` (index.html).
4. Onglet Produits : une ligne par modèle, avec les mêmes codes que dans la page (P001 Sac, P002 Bonnet, P003 Robe bébé, P004 Écharpe).
5. Mettre la page en ligne et envoyer le lien.

## Envoyer le lien aux clientes depuis WhatsApp (sans API, avec l'appli WhatsApp Business)
- **Message d'accueil** (Outils professionnels → Message d'accueil) : envoyé automatiquement à chaque nouvelle cliente, avec le lien.
- **Réponse rapide** `/commander` (Outils professionnels → Réponses rapides) : le vendeur tape /commander, le message avec le lien s'écrit tout seul.
- **Profil de la boutique** : mettre le lien dans le champ « Site web ».
- **Statut** : publier le lien avec une photo des nouveautés.
Aperçu du lien : balises og:* dans index.html (mettre une image `apercu.png` à côté de la page, avec l'adresse complète une fois en ligne).

## La boutique gère sa vitrine elle-même (depuis son tableau Google, sur téléphone)
Ce qu'elle peut changer : le titre, le sous-titre, les photos, les noms, les prix, les couleurs de chaque modèle, afficher ou cacher un modèle, ses numéros Mobile Money. Le reste (mise en page, couleurs du site, fonctionnement) reste chez nous.

**Onglet « Réglages vitrine »** (2 colonnes : Clé, Valeur)
| Clé | Valeur |
|---|---|
| Titre | 🧶 L'Univers du crochet |
| Sous-titre | Choisissez votre modèle et votre couleur, on s'occupe du reste. |
| WhatsApp | 243… (sans + ni 0) |
| M-Pesa / Orange Money / Airtel Money | numéros (laisser vide si pas utilisé) |
| Devise | $ ou FC |

**Onglet « Vitrine »** (une ligne par modèle)
| Modèle | Code | Photo | Prix | Couleurs | Afficher | Stock |
|---|---|---|---|---|---|---|
| Sac au crochet | P001 | lien Google Drive de la photo (partagée « tous les utilisateurs disposant du lien ») | 25 | Rose, Bleu, Blanc | Oui | formule |
- Couleurs : les noms séparés par des virgules (rose, bleu, vert, mauve, beige, multicolore…).
- Afficher = Non : le modèle disparaît.
- Stock (pack stock + vitrine) : formule `=IFERROR(INDEX(Produits!K:K;MATCH(B2;Produits!A:A;0));"")`. À 0, le modèle s'affiche « Épuisé » et on ne peut pas commander plus que le stock. Seul ce chiffre est publié : les ventes et les clientes restent privées.

**Publier** : Fichier > Partager > Publier sur le Web > choisir l'onglet > CSV > Publier. Coller les 2 liens dans `LIENS_TABLEAU` (index.html). Ne publier que ces 2 onglets.

## Paiement Mobile Money (niveau 1, sans compte chez un opérateur)
Après « Commander », la cliente voit son code de commande (CMD-…), le montant et les numéros Mobile Money de la boutique, puis envoie sa commande sur WhatsApp avec la capture du paiement. Le code est aussi écrit dans la note de la commande (tableau). Paiement automatique dans la page (agrégateur) = option à part, plus tard.

Testé (navigateur, faux tableau) : titre et sous-titre lus, modèle caché, « Épuisé » à 0, quantité bloquée au stock, couleurs propres à chaque modèle, envoi au tableau avec le code, écran de paiement, message WhatsApp.
