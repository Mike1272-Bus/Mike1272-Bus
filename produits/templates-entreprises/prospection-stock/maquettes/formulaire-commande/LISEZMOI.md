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
