# Fuegos (Kinshasa) : « petite faim, grosse faim, très grosse faim » (25 s, storytelling, musique seule)

Demande de Mike : une vidéo en storytelling, sans les bruitages gourmands de la vidéo +243.
Images : les 4 captures envoyées par Mike (photo de profil et 3 publications Instagram de @fuegoskinshasa). Recadrées sans mains, sans bras, sans prix et sans les textes des affiches, puis agrandies avec Real-ESRGAN (`ameliorer.py`).
Couleurs de leur logo : bordeaux, crème, flamme rouge. Titres en Young Serif (proche de leurs affiches), récit en Instrument Serif italique. Fumée et braises en fond (« Gourmet on Fire »).

| Temps | Scène |
|---|---|
| 0 - 3,8 s | « Kinshasa. Tout commence par une petite faim… » |
| 3,8 - 8,8 s | Petite faim : Sandwich Tacos (poulet · viande), « Poivrons, oignons, maïs, fromage cheddar » |
| 8,8 - 14,2 s | « Puis la faim grandit… » puis grosse faim : Cheese Burger Viande et ses ingrédients |
| 14,2 - 19,6 s | « Et quand c'est la très grosse faim… » puis Deal Box : 1 Zinger burger + 2 pièces de poulet broast, frites et Pepsi |
| 19,6 - 25 s | « Petite ou très grosse faim, une seule adresse : » le logo Fuegos, Kinshasa, @fuegoskinshasa |

Fabrication : `python3 ameliorer.py <RealESRGAN_x4plus.pth>`, `python3 mix.py` (musique seule), `npx hyperframes@0.8.77 render . -q high -o renders/raw.mp4`, puis compression ffmpeg → `renders/fuegos.mp4`.
À ajouter quand on l'a : leur numéro de commande sur la carte de fin.
