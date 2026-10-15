# Ruche du Terroir, jour 5 (vendredi 16 octobre) : spot « miel au clou de girofle » + concours (27 s)

Demande de Mike (15 octobre) : un vrai « spot publicitaire » avec des animations, « genre le miel qui coule », associé au pot de la Ruche, et la vidéo IA prévue n'est pas arrivée à temps.
Mixkit (vidéos de miel) est bloqué par le réseau depuis notre outil, et la règle de la Ruche est « uniquement les images du client » : le miel est donc **calculé en code** (`miel.py`) :
- `assets/video/rideau.webm` : un rideau de miel qui coule du haut avec des gouttes (4 s, avec transparence) ;
- `assets/video/ruban.webm` : un filet de miel qui tombe et s'empile (6 s, avec transparence), posé sur le couvercle du pot.
Chaque forme est une distance signée ; on en tire l'épaisseur puis la lumière (reflets, couleur plus foncée là où c'est épais). Calcul en 540x960, agrandi x2.

Le pot : leur vrai pot clou de girofle (`photos-client/detoure-v2`) agrandi x2 avec Real-ESRGAN (`pot_hd.py`). Cuillère et logo : ceux des jours précédents. Clous de girofle dessinés en SVG.

| Temps | Scène |
|---|---|
| 0 - 4,2 s | Le rideau de miel coule, « Ce vendredi, on vous fait plaisir. » |
| 4,2 - 11,4 s | Leur pot arrive, le filet de miel coule et déborde sur le couvercle, les clous de girofle tombent, reflet sur le pot. « Le miel au clou de girofle · Pur miel congolais, macéré au clou de girofle. » |
| 11,4 - 22,2 s | Le rideau repasse puis s'efface : « CONCOURS », « Gagnez un pot de miel + une cuillère à miel », les 3 étapes, dates, mention Instagram |
| 22,2 - 27 s | Logo, « Commandez sur WhatsApp » +243 859 072 956, le pot |

Son : musique + sons discrets (le versement doux sous le filet de miel, impact sur « CONCOURS », pops, carillon).
Fabrication : `python3 miel.py`, `python3 pot_hd.py <RealESRGAN_x4plus.pth>`, `python3 mix.py`, `npx hyperframes@0.8.77 render . -q high -o renders/raw.mp4`, compression ffmpeg (crf 21) → `renders/ruche-jour5-spot-miel.mp4`.
