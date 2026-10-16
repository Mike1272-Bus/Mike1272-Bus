# Ruche du Terroir, jour 5 (vendredi 16 octobre) : spot « PAF ! CONCOURS ! » (26 s)

Demande de Mike (15 octobre) : un vrai « spot publicitaire » pour le miel au clou de girofle + le lancement du concours.
Première version : du miel qui coule, calculé en code. Avis de Mike : « Les effets miel ne sont pas réussis, laisse tomber ça. Ajoute plutôt d'autres effets spéciaux comme "PAF ! CONCOURS !", toujours avec la même D.A. »
Version actuelle : **effets bande dessinée** (bulles d'explosion « PAF ! » et « CONCOURS ! », étoiles, trame de points, lignes de vitesse, secousses, flashs), dans la même D.A. que la série : fond brun doré, rayons de lumière, orange #f29a0e, crème #ffe2b0, jaune #ffc21a, gros titres jaunes cernés de noir (police Baloo 2 ExtraBold).

Le pot : leur vrai pot clou de girofle (`photos-client/detoure-v2`) agrandi x2 avec Real-ESRGAN (`pot_hd.py`). Cuillère et logo : ceux des jours précédents. Clous de girofle, bulles et étoiles dessinés en SVG.

| Temps | Scène |
|---|---|
| 0 - 3,8 s | Bulle « PAF ! » + étoiles, « Ce vendredi, on vous fait plaisir. » |
| 3,8 - 10,6 s | Leur pot sur une bulle d'explosion, clous de girofle qui tombent. « Le miel au clou de girofle · Pur miel congolais, macéré au clou de girofle. » |
| 10,6 - 21,2 s | Bulle « CONCOURS ! », lignes de vitesse, pot + cuillère, les 3 étapes en cartes BD, « Du 16 au 24 octobre » (16/10 : étapes « Partagez cette vidéo » et « Identifiez 5 personnes qui s'abonnent à la page », icônes cloche, mégaphone, bulle), mention Instagram |
| 21,2 - 26 s | Logo sur une bulle, « Commandez sur WhatsApp » +243 859 072 956, le pot |

Son : musique + bruitages BD (impact grave + pop sur chaque « PAF », whooshs, pops sur les cartes, carillon à la fin).
Pas de prix, pas de grammage, pas de promesse de santé.
Fabrication : `python3 pot_hd.py <RealESRGAN_x4plus.pth>`, `python3 mix.py`, `npx hyperframes@0.8.77 render . -q high -o renders/raw.mp4`, compression ffmpeg (crf 21) → `renders/ruche-jour5-spot-miel.mp4`.
