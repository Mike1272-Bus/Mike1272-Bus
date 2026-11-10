# Série « Gâteaux de fêtes » (10 pâtisseries) : la petite voix ElevenLabs

Décision de Mike (20 octobre) : chaque vidéo garde le motion design + l'animation IA + les bruitages, et on ajoute **une petite voix d'environ 10 secondes**. Crédits ElevenLabs gratuits : on les économise.

## La voix
- **Une seule voix pour les 10 vidéos**, pour qu'on reconnaisse la série. Pour des gâteaux, une **voix féminine chaleureuse et souriante** colle mieux. Hugo (voix masculine sérieuse) reste la voix d'Allegra pour nos propres vidéos.
- Réglages : modèle **Multilingual v2**, langue français. Stabilité au milieu, et vitesse normale ou un peu lente (pour une voix gourmande).

## Économiser les crédits
1. Pour chaque pâtisserie, j'écris 2 phrases courtes, environ 25 mots en tout (≈ 10 secondes) : l'**accroche** au début, la **fin** sur la carte de contact.
2. Tu colles **les 10 textes en une seule fois** dans ElevenLabs, chacun séparé par une ligne vide, puis tu génères **un seul fichier MP3** et tu me l'envoies.
3. Je le découpe phrase par phrase et je le place dans chaque vidéo. La musique baisse automatiquement pendant la voix (même méthode que `avant-apres/ajouter_voix.py`).
4. Réécouter **avant** de régénérer : chaque nouvelle génération recoûte des crédits.

## Le modèle de texte (à adapter avec les vraies infos de chaque pâtisserie)
- Accroche (≈ 4 s) : « Noël approche… Et si cette année, votre gâteau de fête venait de chez [Nom] ? »
- Fin (≈ 5 s) : « [Spécialité vue sur leurs photos]. Commandez dès maintenant sur WhatsApp ! »

On n'invente rien : pas de prix, pas de date limite de commande, pas de promesse. Tout vient de leurs publications.
Secret professionnel : dans les messages aux pâtisseries, on ne dit jamais comment la vidéo ou la voix sont faites.
