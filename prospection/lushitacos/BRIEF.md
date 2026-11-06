# LushiTacos : « Comment naît un bon tacos ? » (24 s, storytelling, musique seule)

Images : 3 photos de leur fiche Google (2 photos de tacos, leur affiche « faites-vous livrer » avec numéros et adresse), recadrées et agrandies (Real-ESRGAN, `ameliorer.py`). Sur la photo de la planche, la caméra ne va jamais tout à droite : un petit logo « O » d'une autre marque y est imprimé sur le papier.
Couleurs de leur affiche : brun, crème, orange ; motif « grill » en fond ; titres en Young Serif.

| Temps | Scène |
|---|---|
| 0 - 3,2 s | « Comment naît un bon tacos ? » |
| 3,2 - 11,6 s | Leur photo de la planche ; la caméra s'y promène, étape par étape : 1 La tortilla, 2 On la garnit, 3 On la grille, 4 On la sert |
| 11,6 - 15,6 s | « Le résultat : » leurs deux tacos, « Grillé dehors, garni dedans. » |
| 15,6 - 19,2 s | « Pas envie de vous déplacer ? » leur affiche, « Faites-vous livrer. » |
| 19,2 - 24 s | « LushiTacos, commandes & livraison », 081 289 2716, 098 515 2233, 34, avenue Boundy, Réf. : École Belle Vue, en face de la Regideso |

Fabrication : `python3 ameliorer.py <RealESRGAN_x4plus.pth>`, `python3 mix.py`, `npx hyperframes@0.8.77 render . -q high -o renders/raw.mp4`, compression ffmpeg → `renders/lushitacos.mp4`.
