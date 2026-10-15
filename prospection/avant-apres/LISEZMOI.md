# Avant / après : 6 vidéos de démonstration Allegra (16 s, vertical)

Pour montrer aux commerçants la différence entre une photo fixe et une vidéo animée.
- **Style** : DA crème de la Ruche (fond crème, gros texte en relief, cartes blanches, pilule WhatsApp verte), une couleur par produit.
- **Avant** (0 à 4 s) : une simple photo dans un fil d'actualité, 0 like, on passe sans s'arrêter.
- **Après** (4 à 12 s) : le produit en mouvement, mots qui claquent, icônes 3D, badge « NOUVEAU », reflet, bouton « Commandez sur WhatsApp ».
- **Fin** (12 à 16 s) : « Vos produits méritent ça. Vidéo d'essai gratuite. Écrivez ESSAI », +243 831 710 181.

Images : clips libres de droits Mixkit (crédits dans `../contenu-allegra/stock/credits.txt`), sans visages. Marqué « Exemple de pub · Allegra ». Pas de prix, pas de vraie marque.

| Vidéo | Mots | Clips |
|---|---|---|
| `renders/avant-apres-burger.mp4` | Juteux. Croustillant. Irrésistible. | burger-1, burger-3 |
| `renders/avant-apres-cosmetiques.mp4` | Éclat. Couleur. Glamour. | maquillage-3, cosmetique-1 |
| `renders/avant-apres-glace.mp4` | Fraîche. Fondante. Gourmande. | glace-1, glace-2 |
| `renders/avant-apres-chaussures.mp4` | Confort. Style. Énergie. | baskets-3, baskets-2 |
| `renders/avant-apres-gadget.mp4` | Précis. Élégant. Connecté. | smartwatch-2, montre-1 |
| `renders/avant-apres-vetements-femmes.mp4` | Élégance. Douceur. Confiance. | robe-2 (ralenti), robe-1, tissu-1 |

Refaire : `python3 prep.py` (clips) puis `python3 build.py` (compositions), puis le rendu dans chaque dossier.

## Légende à poster (une par vidéo, changer le produit)
> Avant : une photo qu'on fait défiler 😴 Après : une vidéo qui donne envie d'acheter 🔥
> Vos produits méritent ça. Nous transformons vos photos en vidéos pub.
> 🎁 Vidéo d'essai gratuite : écrivez ESSAI au +243 831 710 181
> #Kinshasa #RDC #publicité #vidéo #commerce

## Calendrier de publication : 2 vidéos par jour (13 h et 19 h)

13 h = une démo avant / après (on montre). 19 h = une vidéo qui pousse à écrire (on demande).

| Jour | 13 h | 19 h |
|---|---|---|
| Jeu 15 | Avant/après burger | Vidéo d'essai gratuite (`contenu-allegra/mar13-essai`) |
| Ven 16 | Avant/après glace | 3 photos, 3 transformations (`contenu-allegra/mer14-transformations`) |
| Sam 17 | Avant/après mode femme | Démo pizza (`contenu-allegra/mer14-demo-pizza`) |
| Dim 18 | Avant/après cosmétiques | Nouvelle vidéo (chat Contenu Allegra) |
| Lun 19 | Avant/après chaussures | Nouvelle vidéo (chat Contenu Allegra) |
| Mar 20 | Avant/après gadget | Rappel de l'offre d'essai (même vidéo que jeudi, nouvelle légende) |

Descriptions des avant / après (1re phrase) :
- Burger : Votre burger mérite mieux qu'une photo qu'on fait défiler 🍔🔥
- Glace : Une photo de glace ? On passe. Une glace qui fond sous le chocolat ? On commande 🍦
- Mode femme : Vos robes méritent d'être vues en mouvement 👗✨
- Cosmétiques : Vos produits de beauté, présentés comme dans une vraie pub 💄
- Chaussures : Une basket en photo, c'est joli. En vidéo, ça donne envie de l'avoir 👟⚡
- Gadget : Vos gadgets méritent une présentation à leur hauteur ⌚📱
Les légendes de 19 h sont dans `contenu-allegra/textes_a_poster.md`.

Fin de chaque description :
> Avant : une photo qu'on fait défiler 😴 Après : une vidéo qui donne envie d'acheter.
> Nous transformons vos photos en vidéos pub.
> 🎁 Vidéo d'essai gratuite : écrivez ESSAI au +243 831 710 181
> #Kinshasa #RDC #publicité #marketingdigital #[produit]
