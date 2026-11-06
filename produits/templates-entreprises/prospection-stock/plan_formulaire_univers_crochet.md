# Plan : formulaire de commande avec photos et couleurs (L'Univers du crochet)

À transmettre au chat Automatisation pour la fabrication. Le chat Prospection garde la partie vente.

## Le besoin
Un lien envoyé sur WhatsApp. La personne (cliente, ou vendeur pour la cliente) l'ouvre sur son téléphone, voit les modèles en photo, choisit le modèle et la couleur, et passe commande. **Sans paiement en ligne** : paiement à la livraison ou par Mobile Money, confirmé ensuite par WhatsApp.

## Ce que la personne voit (sur téléphone)
1. Titre : « Commander chez L'Univers du crochet 🧶 »
2. Les modèles en **photos**, chacun avec un numéro et un nom (1. Sac, 2. Bonnet, 3. Robe bébé…)
3. Liste « Modèle » (choix parmi les noms)
4. Liste « Couleur » (Rose, Bleu, Blanc…), avec idéalement des pastilles de couleur
5. Quantité
6. Nom, téléphone WhatsApp, quartier / adresse de livraison
7. Note (taille, prénom à broder…)
8. Bouton « Commander » → « Merci ! Votre commande est enregistrée, on vous écrit sur WhatsApp pour confirmer. »

## Ce qui se passe derrière (automatique)
- Nouvelle ligne dans l'onglet Commandes : date, cliente, téléphone, modèle, couleur, quantité, adresse, statut « à confirmer ».
- Message WhatsApp au patron : « Nouvelle commande : 1 sac rose, Maman Sarah, Lemba ».
- Message WhatsApp à la cliente : confirmation de la commande.
- Statuts suivis dans le tableau : à confirmer → en confection → prête → livrée.
- Option : suivi de la laine par couleur, alerte quand une couleur manque.

## Deux façons de le fabriquer
**Version 1 (rapide)** : formulaire n8n. Un bloc en haut affiche les photos numérotées, puis les listes Modèle et Couleur. Simple, assez joli, peu de travail.
**Version 2 (plus belle, plus tard)** : petite page sur mesure, où l'on **touche la photo** du modèle et la pastille de couleur. Elle envoie la commande au même système. Plus de travail.
→ Commencer par la version 1. Passer à la version 2 si le client le demande.

## Ce qu'il faut pour que le lien marche sur WhatsApp
- Aujourd'hui n8n tourne sur l'ordinateur de Mike (localhost) : **le lien ne s'ouvre pas ailleurs**. Pour un vrai client, il faut un n8n **en ligne** (hébergé), sinon le lien est mort dès que l'ordinateur s'éteint.
- WhatsApp vers la cliente : en mode test, Meta n'envoie qu'aux numéros enregistrés. Pour un vrai client : numéro dédié, entreprise vérifiée, modèles de messages validés, coût par message à vérifier chez Meta.

## Ce qu'il faut demander au client
- La liste de ses modèles, avec **une photo** de chacun et son prix
- La liste de ses couleurs disponibles
- Livraison : zones, frais, délais de confection
- Le numéro qui reçoit les commandes

## À décider par Mike
- Est-ce inclus dans les 150 $ ou une option en plus ? (Commande en ligne par les clientes = plus proche d'une petite boutique en ligne.)
- Pas de chiffre ni de délai promis au client avant validation par le chat Automatisation.
