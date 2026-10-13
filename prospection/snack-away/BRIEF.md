# Snack Away (Kinshasa) : « Midi approche… Où est-ce qu'on mange ? » (25 s, storytelling, musique seule)

Images : 4 envoyées par Mike (photos de leur fiche Google Maps : salle, Sandwich Teriyaki, Zinger Burger, et la capture de la fiche). Recadrées sans logo ni texte, agrandies avec Real-ESRGAN (`ameliorer.py`). Le logo vient du haut du visuel Teriyaki.
Couleurs de leur salle et de leur logo : jaune, noir, zigzag noir et blanc de leur mur, rouge et vert du logo. Titres en Oswald (proche des mots de leur mur), récit en Instrument Serif italique. Chaque scène glisse depuis le bas, comme une page qu'on tourne.

| Temps | Scène |
|---|---|
| 0 - 3,8 s | Zigzags qui défilent, « Kinshasa », « Midi approche… », « Où est-ce qu'on mange ? » |
| 3,8 - 8,4 s | Fond jaune : « Là où les murs sont jaunes… », leur salle, leur logo |
| 8,4 - 13 s | « Pour ceux qui aiment le croustillant : » le Zinger Burger, « Crispy chicken » |
| 13 - 17,6 s | « Pour ceux qui préfèrent le sandwich : » le Sandwich Teriyaki |
| 17,6 - 20,8 s | « Et pour tous les autres : » les mots de leur mur, un par un (Fresh salads, Crispy chicken, Snacks, Cold smoothies, Tasty burgers) |
| 20,8 - 25 s | Logo, Kinshasa, la salle, « On vous attend ! » |

Fabrication : `python3 ameliorer.py <RealESRGAN_x4plus.pth>`, `python3 mix.py`, `npx hyperframes@0.8.77 render . -q high -o renders/raw.mp4`, compression ffmpeg → `renders/snack-away.mp4`.
À ajouter quand on l'a : leur numéro ou leur adresse sur la carte de fin.
