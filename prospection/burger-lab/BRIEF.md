# Burger Lab (Kinshasa / Gombe) : « L'expérience Burger Lab » (27,5 s, storytelling « labo »)

Demande de Mike : un très bon rendu, car le compte est très actif. Idée : prendre leur nom au mot, chaque plat devient une expérience de labo.
Images : captures de @burgerlabrdc (logo, publications et stories). Recadrées sans l'interface Instagram ni les mains (`ameliorer.py`) ; le haut du milkshake agrandi avec Real-ESRGAN.
Couleurs : leur rouge, leur jaune moutarde, blanc ; fond « papier millimétré » ; titres en Baloo 2 (rond et épais comme leur logo).

| Temps | Scène |
|---|---|
| 0 - 3,6 s | Logo, « Ici, on ne cuisine pas… on fait des expériences. » |
| 3,6 - 9,4 s | Expérience n°1, le burger : annotations (logo gravé sur le pain, oignon, champignons, fromage fondu, salade), tampon « VALIDÉ » |
| 9,4 - 14,4 s | Expérience n°2, le croustillant : annotations (poulet croustillant, frites, coleslaw, sauces), tampon, leur phrase « Croustillant, généreux et terriblement gourmand. » |
| 14,4 - 19,2 s | Expérience n°3, les sauces : les 4 pots entourés et numérotés, « 4 sauces. Laquelle choisir ? » |
| 19,2 - 23,2 s | Expérience n°4, mode milkshake : un interrupteur passe de OFF à ON, le milkshake, Vanille / Chocolat / Fraise / Oreo |
| 23,2 - 27,5 s | Conclusion de l'expérience : logo, « L'expérience Burger Lab », Kinshasa · Gombe, @burgerlabrdc |

Son : musique + sons discrets (ping des annotations, tampon, clic de l'interrupteur, carillon).
Fabrication : `python3 ameliorer.py <RealESRGAN_x4plus.pth>`, `python3 mix.py`, `npx hyperframes@0.8.77 render . -q high -o renders/raw.mp4`, compression ffmpeg → `renders/burger-lab.mp4`.
