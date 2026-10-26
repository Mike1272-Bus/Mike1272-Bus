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
