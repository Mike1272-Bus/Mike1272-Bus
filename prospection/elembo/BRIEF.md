# Elembo : « Des fruits 100 % congolais » (24 s, bruitages boissons)

Image : la photo des 3 bouteilles envoyée par Mike (PNG détouré), séparée bouteille par bouteille (`decoupe.py`). Fruits et flèches du recyclage dessinés en SVG, dans le style des étiquettes (orange + feuille verte, ananas jaune). Fond crème-jaune, bulles. Titres en Baloo 2.
Textes : leur site elembo-rdc.com et leurs étiquettes (voir `message.md`, « À savoir »).

| Temps | Scène | Son |
|---|---|---|
| 0 - 3,6 s | Les fruits tombent et rebondissent : « Kongo-Central. Des fruits 100 % congolais. » | pops |
| 3,6 - 9 s | « Fraîchement pressés, puis mis en bouteille. » Les 3 bouteilles montent : Jus d'ananas, Ananas-orange, Jus d'orange | ouverture et versement (boisson-4) |
| 9 - 14 s | « Dans la bouteille : » ✓ Bio ✓ Sans additif chimique ✓ Faible en sucre ajouté, « Une alternative saine aux sodas classiques. » | pétillement + pings |
| 14 - 17,3 s | « Et la bouteille ? » flèches du recyclage, « En verre recyclé. Moins de déchets dans les rues. » | tintements |
| 17,3 - 20,5 s | Les 3 bouteilles, « La vie saine se fait avec du jus de fruits. » | la gorgée |
| 20,5 - 24 s | La bouteille ananas-orange, « Elembo », « Made in DRC », elembo-rdc.com | carillon |

## Le clip IA (à générer, puis à mettre en fond de la scène 1)
Règle : aucune personne. Image de départ : `assets/img/trio.png` ou une bouteille seule. 9:16, 5 s. Outils : `prospection/IA_VIDEO_OUTILS.md`.
1. « Three glass bottles of pineapple and orange juice standing on a sunny wooden table in a tropical garden, fresh pineapples and oranges around them, cold droplets on the glass, gentle camera orbit, no people, no hands, beverage commercial, vertical 9:16. »
   *(Trois bouteilles de jus sur une table en bois au soleil, ananas et oranges autour, gouttes fraîches, la caméra tourne doucement, aucune personne.)*
2. « Slow motion: a ripe pineapple and an orange fall into clear water and burst into a splash of yellow and orange juice, bright sunlight, white background, no people, vertical 9:16. »
   *(Au ralenti : un ananas et une orange tombent dans l'eau et éclatent en jus jaune et orange, plein soleil, fond blanc, aucune personne.)*
3. « Aerial shot of green pineapple fields in the hills of Central Africa at sunrise, soft mist, no people, vertical 9:16. »
   *(Vue aérienne de champs d'ananas sur des collines d'Afrique centrale au lever du soleil, aucune personne.)* → pour la scène « Kongo-Central ».

Fabrication : `python3 decoupe.py`, `python3 mix.py`, `npx hyperframes@0.8.77 render . -q high -o renders/raw.mp4`, compression ffmpeg → `renders/elembo.mp4`.
