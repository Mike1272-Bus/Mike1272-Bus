# Jambo « Jus ya Mboka » : aperçu IA + motion design (12 s)

Inspiration : le spot Suntory Strong Zero (voir `../apercu-ia-boisson/BRIEF.md`).
Images : les 2 photos de leurs stories Instagram (compte « Jus », janvier 2020) et leur logo, envoyées par Mike le 15 octobre (`photos-client/`).
Goûts vus sur les étiquettes : Maracuja, Citron menthe, Mangue, Gingembre citron, Bissap. Mention « Jus ya Mboka ». Bouteilles plastique 250 ml et bouteilles en verre.

⚠️ Les photos datent de **janvier 2020** : vérifier que la marque est toujours active (publications récentes) avant d'envoyer.

## Version actuelle (100 % motion design, sans IA) : `renders/jambo-apercu.mp4`

| Temps | Scène | Son |
|---|---|---|
| 0 - 3,4 s | Nuit bleue, la caméra monte le long de la bouteille Maracuja, gouttes de fraîcheur, « JAMBO » | ouverture et versement |
| 3,4 - 6,6 s | Bulles, fruits qui tombent au ralenti (citron, maracuja, bissap, mangue, menthe, gingembre, dessinés par nous), « JUS YA MBOKA » en contour qui se remplit de jaune, « le jus du pays » | impact + pétillement |
| 6,6 - 9,6 s | Les 5 bouteilles en verre dans le noir, les projecteurs s'allument un par un, noms des goûts, « 5 GOÛTS » | 5 clics |
| 9,6 - 12 s | Fond rouge Jambo, logo, « Jus ya Mboka », les 3 bouteilles plastique montent, « Aperçu · Allegra Digital Ground » | tintements, gorgée |

Les scènes 1 et 2 sont prévues pour recevoir les clips IA : quand Mike envoie les clips, on les met en fond à la place (le texte reste par-dessus).

## Les prompts IA (OpenArt / Kling, « Image to Video », 9:16, 5 s)

Images de départ prêtes dans `ia-depart/` :
- `C-maracuja-seule.jpg` : la bouteille Maracuja seule (clip 1)
- `A-trio-9x16.jpg` : les 3 bouteilles plastique, déjà au format vertical (clip 3)
- `D-cinq-bouteilles.jpg` : les 5 bouteilles en verre (bonus)

**Clip 1 « La fraîcheur »** (image C)
> La bouteille glacée, couverte de gouttes, la caméra monte lentement, lumière chaude derrière.
```
Premium beverage TV commercial. Extreme close-up of the ice-cold juice bottle from the image, covered in fresh condensation droplets slowly running down the plastic. Slow vertical camera move from the bottom to the red cap. Deep dark navy blue background, warm orange rim light making the droplets sparkle. Ultra slow motion, photorealistic, 4K, cinematic color grading. Keep the bottle shape, red cap and label exactly as in the image.
```

**Clip 2 « Le goût »** (« Text to Video », sans image)
> Des morceaux de maracuja et de citron plongent dans un jus doré, explosion de bulles.
```
Ultra slow-motion macro shot: halves of fresh passion fruit and lemon slices fall and plunge into golden orange juice, creating an explosion of tiny bubbles and glowing splashes, juice droplets frozen in the air. Deep dark navy blue background, strong warm backlight. Premium juice commercial, photorealistic, 4K, high contrast cinematic lighting.
```

**Clip 3 « La révélation »** (image A)
> Les 3 bouteilles dans le noir, les projecteurs s'allument un par un.
```
The three juice bottles from the image stand in total darkness on a dark surface. Warm spotlights switch on one by one from above, revealing each bottle with glowing rim light and cold condensation. Slow cinematic push-in. Premium beverage commercial, photorealistic, 4K. Keep the bottles, red caps and labels exactly as in the image.
```

**Négatif (pour tous)**
```
text, letters, words, changed label, deformed bottle, extra bottles, people, hands, faces, cartoon, low quality, blurry, flicker, fast motion
```

## Fabrication
`python3 decoupe.py` (détourage des bouteilles, fond sombre : seuil couleur ; bissap : silhouette de la mangue), `python3 mix.py`, `npx hyperframes@0.8.77 render . -q high -o renders/raw.mp4`, puis compression ffmpeg → `renders/jambo-apercu.mp4`.
