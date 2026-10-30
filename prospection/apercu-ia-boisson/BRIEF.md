# Aperçu IA + motion design pour une marque de boisson (15 octobre)

Inspiration : spot « Suntory Strong Zero » envoyé par Mike (17 s).
But : une vidéo de **10 à 12 s** qui montre à une nouvelle marque de boisson ce qu'Allegra sait faire. On l'envoie avec un message court.

## 1. Ce qui rend le spot Suntory efficace

| Moment | Ce qu'on voit | Ce qu'on garde |
|---|---|---|
| 0 à 4 s | Gros plan de la canette, gouttes de fraîcheur, la caméra monte lentement | Le produit est la star dès la 1re seconde |
| 4 à 8,5 s | Tranches de citron et jus en ralenti, plongeon dans l'eau, explosion de bulles | Le goût se **voit** : fruit, fraîcheur, bulles |
| 8,5 à 11 s | Titre « ZERO SUCRE » en contour jaune qui se remplit | Un seul argument, écrit en gros |
| 11 à 15 s | 3 canettes dans le noir, la lumière s'allume, « NOUVEAU » | La gamme, le côté premium |
| 15 à 17 s | Logo blanc sur fond bleu nuit | Fin propre, on retient le nom |

Ingrédients : ralenti, 2 couleurs fortes (bleu canard + jaune), lettres grasses et serrées, lumière dramatique, une seule idée par plan.

## 2. Notre version (10 à 12 s)

**L'IA fait la fraîcheur, le motion design fait la vérité** (même règle que pour la Ruche) : la vraie bouteille nette, le vrai logo, les textes.

| Temps | Image | Motion design Allegra |
|---|---|---|
| 0 à 4 s | Clip IA 1 : la bouteille, gouttes de fraîcheur, caméra qui monte | Petit mot « NOUVEAU » qui claque, bruit d'ouverture |
| 4 à 7 s | Clip IA 2 : fruit / ingrédient qui tombe en ralenti dans la boisson, bulles | Titre en contour qui se remplit de la couleur de la marque (ex. « 100 % FRAIS », à choisir avec la vraie promesse de la marque) |
| 7 à 9,5 s | La **vraie** photo de la bouteille détourée, lumière qui s'allume derrière | Nom du produit en gros, lettres serrées |
| 9,5 à 12 s | Fond couleur de la marque | Logo de la marque, puis « Aperçu · Allegra Digital Ground » |

Son : bruitages de `prospection/sfx-boissons/` (ouverture et versement, pétillant, tintements) + musique courte.
Format : 9:16 (1080×1920) pour WhatsApp et statuts. Version 1:1 possible si besoin.

## 3. Les prompts (OpenArt / Kling, « Image to Video », 9:16, 5 s)

Image de départ : **la photo la plus nette de leur bouteille**, de face, fond simple. Remplacer `[FRUIT]` par l'ingrédient réel (citron, gingembre, ananas, bissap…) et `[COLOR]` par la couleur de la marque.

**Clip 1 « La fraîcheur »**
```
Premium beverage TV commercial, extreme close-up of the ice-cold bottle from the image, covered in fresh condensation droplets slowly running down the glass. Slow vertical camera move from the bottom to the cap. Deep [COLOR] background with soft gradient, dramatic rim light making the droplets sparkle. Ultra slow motion, photorealistic, 4K, cinematic color grading. Keep the bottle shape and label exactly as in the image.
```

**Clip 2 « Le goût »** (sans image de départ, « Text to Video », ou avec une photo de l'ingrédient)
```
Ultra slow-motion macro shot: fresh [FRUIT] slices fall and plunge into sparkling liquid, creating an explosion of tiny bubbles and glowing splashes. Deep [COLOR] background, strong backlight, crisp droplets frozen in the air. Premium soft drink commercial, photorealistic, 4K, high contrast cinematic lighting.
```

**Clip 3 (bonus, si crédits) « La révélation »**
```
Three bottles from the image stand in total darkness on a dark wooden surface. Spotlights switch on one by one, revealing the bottles with glowing rim light and cold condensation. Slow cinematic push-in. Premium beverage commercial, photorealistic, 4K. Keep the bottles and labels exactly as in the image.
```

**Négatif (pour tous)**
```
text, letters, words, changed label, deformed bottle, extra bottles, people, hands, faces, cartoon, low quality, blurry, flicker, fast motion
```

Conseils : 2 essais par clip si possible ; garder seulement les meilleures secondes ; le filigrane n'est pas grave, je le cache au montage.

## 4. Le message à envoyer avec la vidéo

> Bonjour l'équipe [Marque] 👋
> Voici un petit aperçu de ce que nous pouvons faire pour vous 🎬
> Si une collaboration vous intéresse, nous préparons la version complète avec vos produits. On en parle ?
> Mike, Allegra Digital Ground

## 5. Ce qu'il me faut

1. Le nom de la marque (et son compte Instagram ou Facebook).
2. 1 ou 2 photos nettes de la bouteille (ou canette).
3. Le logo (même une capture de leur photo de profil).
4. La couleur principale et le goût / l'ingrédient phare.
5. Les clips IA générés.

Rappels : aucune personne à l'image ; on ne publie rien sans l'accord écrit de la marque ; c'est un aperçu privé envoyé à la marque, pas une pub publique.
