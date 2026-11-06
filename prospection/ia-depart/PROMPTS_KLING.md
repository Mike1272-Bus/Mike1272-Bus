# Prompts Kling : pubs boissons « style grande marque »

Le style des grandes pubs de soda : **gros plan héroïque** sur la bouteille, **gouttes de fraîcheur** qui coulent sur le verre, **glaçons** qui tombent au ralenti, **éclaboussures** dorées, lumière chaude qui brille à travers le jus, et la bouteille bien droite au centre à la fin.
On s'en **inspire** sans copier : on ne cite aucune marque dans le prompt, sinon l'IA risque d'ajouter leurs logos.

## Réglages dans Kling
1. **Image to Video** (image vers vidéo), pas « Text to Video ».
2. Image : `elembo-depart-9x16.jpg` ou `bilengi-depart-9x16.jpg` (déjà au format vertical 9:16).
3. Durée : **5 s**. Mode : **Standard** (il coûte moins de crédits que Professional ; garde Professional pour la version finale d'un client qui paie).
4. Colle le **prompt** (en anglais, l'IA le comprend mieux) et, si le champ existe, le **negative prompt** (ce qu'on ne veut pas).
5. Curseur « Creativity / Relevance » : vers **Relevance** (milieu-droite). L'IA reste fidèle à l'image et ne déforme pas l'étiquette.
6. Génère **2 versions** si tes crédits le permettent, puis garde la meilleure.

**Negative prompt** (le même pour toutes) :
```
people, person, hands, fingers, face, body, text, letters, new logo, distorted label, melted bottle, extra bottles, blurry, low quality, watermark, cartoon
```

---

## Elembo (image : `elembo-depart-9x16.jpg`)

### Prompt 1 : « La pluie de fraîcheur » (le plus « grande marque »)
```
Premium soft drink commercial, cinematic hero shot. The three glass juice bottles stand still in the center, perfectly sharp, labels unchanged. Ice-cold condensation droplets slowly run down the glass, fine mist rises around the bottles. In slow motion, fresh pineapple chunks and orange slices fall from above and burst into golden juice splashes behind the bottles, droplets sparkling in warm sunlight. Glowing backlight shines through the orange-yellow juice. Gentle slow camera push-in. Ultra realistic, 4K, shallow depth of field, vibrant warm colors, no people.
```
*Traduction : pub de soda haut de gamme, plan héroïque. Les 3 bouteilles restent nettes au centre, étiquettes intactes. Des gouttes glacées coulent sur le verre, une légère brume monte. Au ralenti, des morceaux d'ananas et des tranches d'orange tombent et éclatent en éclaboussures de jus doré derrière les bouteilles. La lumière brille à travers le jus. Lent travelling avant. Très réaliste, couleurs chaudes, aucune personne.*

### Prompt 2 : « La vague de jus »
```
High-end beverage advertisement. A swirling wave of fresh orange and pineapple juice rises in slow motion and curls around the three glass bottles, then splashes down, leaving the bottles shining with cold droplets. Bright sunny golden light, tiny juice droplets frozen in the air, the camera slowly orbits a few degrees. Labels stay sharp and unchanged. Photorealistic, commercial lighting, no people.
```
*Traduction : une vague de jus d'orange et d'ananas monte au ralenti, s'enroule autour des bouteilles puis retombe ; les bouteilles brillent de gouttes fraîches ; lumière dorée ; la caméra tourne un peu autour ; étiquettes nettes.*

---

## Bilengi (image : `bilengi-depart-9x16.jpg`, le verre de leur affiche)

### Prompt 3 : « Le verre qui se remplit »
```
Premium fresh juice commercial, cinematic slow motion. Pineapple, green apple and pink grapefruit juice streams keep pouring smoothly into the tall glass, the glass fills up, swirls of golden and pink juice mix inside, then two ice cubes drop in with a slow-motion splash, droplets flying and sparkling. Fresh green background, bright clean studio light, gentle camera push-in. Ultra realistic, vivid colors, no people.
```
*Traduction : les jets d'ananas, de pomme verte et de pamplemousse continuent de couler dans le grand verre, qui se remplit ; le jus tourbillonne ; deux glaçons tombent avec une éclaboussure au ralenti ; fond vert frais ; lumière studio ; lent travelling avant.*

### Prompt 4 : « Fraîcheur glacée »
```
Close-up beverage hero shot. The glass of fresh fruit juice is ice cold: frost and condensation droplets appear and slide down the glass, small bubbles rise inside, the fruits above gently drip their last drops of juice. Soft rim light, sparkling highlights, slow camera move upward. Photorealistic advertising style, no people.
```
*Traduction : gros plan, le verre devient glacé : buée et gouttes qui glissent, petites bulles qui montent, les fruits au-dessus laissent tomber leurs dernières gouttes ; lumière qui fait briller le verre ; la caméra monte lentement.*

---

## Après la génération
- Télécharge la vidéo (**sans** l'agrandir ni la retoucher) et envoie-la-moi.
- Je la mets au début de la vidéo de la marque (à la place de la scène 1), avec le **logo net par-dessus**, le texte, la musique et les bruitages boissons. Le filigrane de la version gratuite sera en grande partie caché par notre texte ou recadré, mais **pour un client qui paie, il faudra générer sans filigrane** (abonnement).
- Si l'étiquette est déformée : relance en déplaçant le curseur encore plus vers « Relevance », ou ajoute « the bottles do not move » au début du prompt.

### OpenArt, c'est quoi ?
C'est un site qui regroupe plusieurs IA d'images et de vidéos au même endroit (dont des modèles comme Kling). Je n'ai pas vérifié son offre gratuite. Pour aujourd'hui, **reste sur Kling directement** : c'est plus simple et tes crédits gratuits du jour y sont.
