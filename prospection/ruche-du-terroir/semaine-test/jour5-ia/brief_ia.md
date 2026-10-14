# Jour 5 (vendredi 16 octobre) : vidéo IA + motion design, miel au clou de girofle et lancement du concours

## 1. Quelle IA choisir (recherche du 14 octobre 2026)

| IA | Gratuit ? | Point fort | Point faible |
|---|---|---|---|
| **Kling** (klingai.com) | Crédits gratuits (quotidiens ou mensuels selon les sources, à vérifier dans le compte) | La plus fidèle à l'image de départ (le pot garde sa forme). Accepte une image de début **et** une image de fin | Filigrane en gratuit, 720p, génération lente aux heures chargées |
| **Hailuo / MiniMax** (hailuoai.video) | Crédits gratuits | Souvent citée pour l'usage commercial en gratuit | Moins fidèle aux détails (étiquette) |
| **Veo** (Google Flow / Gemini) | Accès gratuit limité, chiffres qui changent | Le plus réaliste (lumière, liquides) | Peu d'essais gratuits, à vérifier |
| **Runway** | 125 crédits une seule fois | Bon contrôle | Filigrane, peu de crédits |

**Choix : Kling en premier** (fidélité au pot), **Hailuo en secours**. Les offres gratuites changent souvent : vérifier dans le compte avant.

Sources : [OpenArt](https://openart.ai/blog/best-ai-image-to-video-generators/), [Pixmax](https://www.pixmax.ai/blog/best-image-to-video-ai-tools.html), [Toolradar](https://toolradar.com/blog/best-ai-image-to-video-generators), [Atlas Cloud](https://www.atlascloud.ai/blog/guides/kling-ai-free), [Metronome](https://metronome.com/pricing-index/kling-ai), [Costbench Veo](https://costbench.com/software/ai-video-generators/google-veo/free-plan).

## 2. La règle d'or pour que ça ne fasse pas « trop IA »

- **L'IA fait l'émotion** (le pot qui s'ouvre, le miel qui déborde, les abeilles, la lumière).
- **Le motion design fait la vérité** : le vrai pot de la Ruche, son étiquette nette, le texte, le concours, le numéro. L'IA déforme souvent les étiquettes : on ne montre jamais une étiquette « inventée » en gros plan.
- Clips courts (5 s), mouvements lents, une seule action par clip. On coupe les secondes ratées.
- Format **9:16**, mode « professionnel / haute qualité » si les crédits le permettent.

## 3. Les images de départ (déjà prêtes)

Dans `images-depart/` :
- `A-pot-clou-de-girofle.jpg` : leur vrai pot (clou de girofle) sur une table, lumière chaude.
- `B-cuillere.jpg` : leur vraie cuillère à miel.

## 4. Les prompts (à copier tels quels dans Kling, mode « Image to Video », 9:16, 5 s)

Les IA comprennent mieux l'anglais. Une phrase en français pour chacun dit ce que ça montre.

**Plan 1 : le pot s'ouvre et le miel déborde** (image de départ : A)
> Le couvercle doré s'ouvre tout seul, le miel monte et coule sur le pot, des abeilles sortent.

```
Cinematic macro product shot. The golden lid of the honey jar slowly twists and lifts off by itself. Thick, dark amber honey rises and gently overflows the rim, slowly dripping down the glass in glossy ribbons. Two or three honeybees fly out of the jar in soft slow motion. Warm golden morning light, shallow depth of field, floating dust in the light, subtle camera push-in. Keep the jar shape and label exactly as in the image. Photorealistic, premium food commercial.
```
Négatif (si le champ existe) :
```
text, letters, changed label, extra jars, cartoon, blurry, distorted, flicker, fast motion
```

**Plan 2 : la cuillère** (image de départ : B)
> Le miel coule lentement de la cuillère, en gros plan.

```
Extreme close-up slow motion of thick golden honey flowing from a wooden honey dipper, forming a long glossy ribbon that folds onto itself. Warm backlight makes the honey glow. Very slow, smooth camera orbit. Photorealistic food commercial, 4K detail.
```

**Plan 3 : le moment de partage** (sans image de départ, « Text to Video »)
> Une table de petit-déjeuner chaleureuse : pain, thé, miel qu'on partage.

```
Warm family breakfast table in a bright African home in the morning. Close-up on hands passing fresh bread with honey and pouring honey into cups of tea. Faces out of frame, soft sunlight through the window, joyful atmosphere, slow cinematic camera slide. Photorealistic, natural colors, premium commercial.
```
⚠️ À valider par Mike : la règle du projet est « aucune illustration de personnes ». Ce plan ne montre **que des mains**, sans visages. Si on veut une vraie famille avec des visages, il faut que Mike et la Ruche le décident (ce sont des personnes générées par IA, pas de vrais clients).

**Bonus (si crédits) : image de début + image de fin** : début = A, fin = leur visuel du pot seul. L'IA fait la transition entre les deux.

## 5. Le montage final (moi, motion design HyperFrames, 30 à 35 s)

1. Plan 1 IA (pot qui s'ouvre, miel qui déborde) + titre « Miel au clou de girofle ».
2. Plan 2 IA (cuillère) + « Un miel gustatif et soignant ».
3. Plan 3 IA (partage) + « À partager en famille ».
4. Motion design : le **vrai pot** net, « Concours : gagnez un pot + une cuillère à miel », les 3 étapes du concours, « du 16 au 18 octobre, tirage le 19 », « Concours non sponsorisé par Instagram ».
5. Fin WhatsApp : « Commandez » +243 859 072 956.

Musique plus douce (publicité), bruitages légers (abeilles, coulée).

## 6. Ce que Mike doit faire

1. Créer un compte gratuit sur Kling (et Hailuo en secours).
2. Lancer les 3 plans avec les images de départ et les prompts ci-dessus. Faire 2 essais par plan si les crédits le permettent.
3. M'envoyer les vidéos (même avec le filigrane : je recadre ou je le cache dans le montage).
4. Prévenir la Ruche que la vidéo de vendredi contient des images générées par IA, et avoir son accord.

## 7. Version finale pour OpenArt (Kling), style grande pub (14 octobre)

- **Miel choisi : clou de girofle** (prévu au planning du vendredi, et les clous de girofle sont très beaux à l'image).
- **Image à mettre :** `images-depart/A-pot-clou-de-girofle.jpg` (leur vrai pot, sans texte ni logo autour). Si on prend un de leurs visuels, choisir « Miel au clou de girofle », pot seul, mais le texte et l'abeille risquent d'être déformés par l'IA.
- Réglages : Image to Video, modèle Kling (la version la plus récente proposée), format 9:16, durée 5 s, qualité la plus haute permise.

**Plan 1 « La révélation »**
```
Epic premium commercial hero shot, in the style of a big soda brand TV ad. The honey jar stands on a warm wooden table. The golden lid slowly lifts off by itself and spins in the air. Thick dark amber honey rises and overflows the rim in glossy slow-motion waves, rolling down the glass. Whole cloves fall around the jar in slow motion and bounce on the table. Golden light rays, sparkling particles in the air, warm backlight making the honey glow. Smooth slow camera orbit around the jar, ending on a perfect hero shot of the jar. Keep the jar and its label exactly as in the image. Photorealistic, ultra detailed, 4K, cinematic color grading.
```
**Plan 2 « L'explosion de goût »**
```
Ultra slow-motion macro shot: a wave of golden honey splashes in the air and wraps around falling whole cloves and a cinnamon stick, droplets glowing in warm backlight, against a dark warm brown background. Rich, glossy, delicious textures. Camera slowly pushes in. Photorealistic premium food commercial, 4K, high contrast cinematic lighting.
```
**Plan 3 « Le partage »**
```
Warm breakfast table in a bright African home at sunrise. Close-up of hands dipping a wooden honey dipper into a jar and drizzling honey on fresh bread, cups of hot tea steaming next to it. Faces out of frame. Soft golden sunlight, joyful cozy atmosphere, slow cinematic camera slide. Photorealistic, natural skin tones, premium commercial.
```
**Négatif (pour les 3) :**
```
text, letters, words, changed label, deformed jar, extra jars, cartoon, low quality, blurry, flicker, distorted hands, extra fingers, faces
```
