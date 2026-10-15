# Vin Semuliki : aperçu IA + motion design (12 s)

Marque : **Semuliki SARL** (Instagram `semulikisarl`), Lubumbashi. Produit : **Vin Semuliki**, 13 % d'alcool, 300 ml, bouchon jaune, étiquette bleue avec un léopard.
Textes repris de leurs publications : « Le voici enfin Vin SEMULIKI », « Nguvu kama ya chui ! » (« la force du léopard », en swahili), « Saveur ya mboka », « ingrédients naturels, zéro additif », « Déjà disponible à Lubumbashi, en gros et en détail ».
Images : leur publication (bouteilles dans une glacière, en forêt : déjà une image IA) et leur photo de profil, envoyées par Mike le 15 octobre (`photos-client/`).

**Non repris volontairement :** « donne l'endurance sexuelle, apaise les douleurs dorsales ». Ce sont des promesses de santé pour un alcool : risqué pour eux, et ce n'est pas à nous de les répéter.
**Ajouté :** « L'abus d'alcool est dangereux pour la santé. À consommer avec modération. » (obligatoire pour une pub d'alcool sérieuse).
La photo de profil montre une main : pas utilisée (règle : aucune personne).

## Version actuelle (motion design) : `renders/semuliki-apercu.mp4`

| Temps | Scène | Son |
|---|---|---|
| 0 - 3,4 s | Leur visuel, la caméra entre vers la bouteille, éclat de lumière, « LE VOICI ENFIN », « Vin Semuliki » | ouverture et versement, montée |
| 3,4 - 6,8 s | Fond brun, taches de léopard, 3 coups de griffe, « NGUVU KAMA YA CHUI ! » en contour qui se remplit de jaune, « SAVEUR YA MBOKA. » | impact, 3 griffes |
| 6,8 - 9,6 s | La bouteille dans un cadre doré, rayons qui tournent, « 13 % d'alcool », « 300 ml », « Ingrédients naturels, zéro additif. » | impact, pops |
| 9,6 - 12 s | Bandeau rouge « VIN SEMULIKI », « SEMULIKI », slogan, bouteille, « Déjà disponible à Lubumbashi », mention modération, « Aperçu · Allegra Digital Ground » | tintements, carillon |

## Les prompts IA (OpenArt / Kling, « Image to Video », 9:16, 5 s)

Images de départ : `ia-depart/A-post-9x16.jpg` (leur visuel au format vertical) ou `ia-depart/B-post-carre.jpg`.

**Clip 1 « La fraîcheur »** (image A ou B)
> La bouteille glacée dans la glacière, gouttes qui coulent, glaçons qui brillent, rivière qui coule, caméra qui avance.
```
Premium beverage TV commercial. The ice-cold amber bottle in the cooler from the image, covered in condensation droplets slowly running down. Ice cubes glistening, the river flowing in the background, sun rays through the forest mist, lens flare pulsing behind the bottle. Slow cinematic push-in toward the bottle. Photorealistic, 4K, cinematic color grading. Keep the bottle shape, yellow cap and label exactly as in the image.
```

**Clip 2 « La force du léopard »** (« Text to Video », sans image, sans personne)
> Un léopard marche lentement dans la forêt tropicale au lever du soleil, puis regarde la caméra.
```
Cinematic slow-motion shot of a majestic leopard walking through a misty tropical rainforest at sunrise, golden light rays, shallow depth of field, it stops and looks into the camera with intense eyes. Nature documentary quality, photorealistic, 4K, warm amber color grading. No people, no text.
```

**Clip 3 « Le versement »** (« Text to Video »)
> Un vin ambré versé au ralenti dans un verre, avec des glaçons, sur fond brun chaud.
```
Ultra slow-motion macro shot: amber-red wine pours into a glass with ice cubes, glowing splashes and droplets frozen in the air, warm dark brown background, strong golden backlight. Premium drink commercial, photorealistic, 4K, high contrast cinematic lighting. No people, no text.
```

**Négatif (pour tous)**
```
text, letters, words, changed label, deformed bottle, extra bottles, people, hands, faces, cartoon, low quality, blurry, flicker, fast motion
```

Quand les clips arrivent : clip 1 à la place du visuel de la scène 1, clip 2 en fond de la scène 2 (sous « Nguvu kama ya chui ! »), clip 3 en ouverture ou avant la carte de fin.

## Fabrication
`python3 mix.py`, `npx hyperframes@0.8.77 render . -q high -o renders/raw.mp4`, puis compression ffmpeg → `renders/semuliki-apercu.mp4`.

## Version avec le clip IA (15 octobre, soir) : `renders/semuliki-apercu-ia.mp4` (13,6 s)

Clip fait par Mike sur idea.ai (image de départ : leur visuel), 10,7 s en 1440×2560. On garde les 8 premières secondes : après, c'est l'écran « Created with idea.ai ». Le filigrane « idea.ai » (en haut à gauche) et le titre fixe « SEMULIKI » généré par l'IA sont cachés sous un bandeau brun, où l'on met nos propres titres animés.

| Temps | Scène |
|---|---|
| 0 - 4,1 s | Clip IA (la caméra avance vers la bouteille dans la glacière), « LE VOICI ENFIN », « SEMULIKI », « VIN SEMULIKI · 300 ml » |
| 4,1 - 8 s | Suite du clip : 3 coups de griffe, « NGUVU KAMA YA CHUI ! » en contour qui se remplit, « SAVEUR YA MBOKA. » |
| 8 - 10,8 s | La bouteille, « 13 % d'alcool », « 300 ml », « Ingrédients naturels, zéro additif. » |
| 10,8 - 13,6 s | Carte de fin (bandeau, slogan, Lubumbashi, modération, « Aperçu · Allegra Digital Ground ») |

La version sans IA est gardée : `versions/index-sans-ia.html` et `renders/semuliki-apercu.mp4`.
