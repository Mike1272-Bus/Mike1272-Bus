# Biloko (RDC) : « Un clic… Ding dong ! » (22 s, storytelling animé)

Demande de Mike : avec seulement 2 images (logo + une affiche), ajouter des animations pour bien raconter l'histoire.
Couleurs de leur logo : jaune vif qui tourne à l'orange, noir. Tout est dessiné en code (SVG/CSS), sauf le logo et le plat (de leur affiche, recadré sans prix ni texte, `ameliorer.py`).

| Temps | Scène |
|---|---|
| 0 - 3,6 s | La nuit, la pluie, une maison dont la fenêtre clignote : « Une petite faim… …et pas envie de sortir ? » |
| 3,6 - 7,8 s | « Ouvrez Biloko… » : le bouton noir au chariot (leur logo), le clic (onde), « Un clic. » « Livraison en un Clic », le bouton part à toute vitesse |
| 7,8 - 12,4 s | « Biloko vous livre » : un plan, la route se dessine du « restaurant » à « chez vous » et le scooter (sans personne) la suit, l'épingle saute à l'arrivée |
| 12,4 - 16,8 s | « Ding dong ! », le plat de leur affiche arrive, « Vos plats préférés, livrés chez vous ! » |
| 16,8 - 22 s | Logo, « Téléchargez l'application » Google Play / App Store, « ou commandez sur WhatsApp » 081 574 4630, le plat |

Son : musique + sons d'appli discrets (clic, notification, ping, carillon), pas de bruitages gourmands.
Fabrication : `python3 ameliorer.py <RealESRGAN_x4plus.pth>`, `python3 mix.py`, `npx hyperframes@0.8.77 render . -q high -o renders/raw.mp4`, compression ffmpeg → `renders/biloko.mp4`.
