# Bilengi, les délices d'Afrique : « Une envie de fraîcheur ? » (24 s)

Première vidéo « marques de boissons ». Motion design + les bruitages boissons de Mike (`prospection/sfx-boissons/`) + musique. La scène 1 est prévue pour recevoir un **clip IA** (voir plus bas).
Images : leur logo, leur affiche « Bar à jus Bilengi Bio » (verre de jus, photo de leurs bouteilles), leurs pots de miel et de pilipili (`ameliorer.py`, Real-ESRGAN). Couleurs : le vert de leur logo, le vert clair de l'anneau, l'orange de « Les délices d'Afrique ». Bulles qui montent pendant toute la vidéo.

| Temps | Scène | Son |
|---|---|---|
| 0 - 3,3 s | Logo, « Une envie de fraîcheur ? » | ouverture de la bouteille (boisson-4) |
| 3,3 - 7,9 s | Le verre de jus de leur affiche, « Jus de fruits frais. » | le versement continue |
| 7,9 - 12 s | « Et à emporter, bien frais. » Leurs bouteilles dans un rond, « Bilengi Bio » | tintements, pétillement |
| 12 - 16,8 s | « Et dans l'épicerie : » miel naturel, pilipili, « Produits 100 % naturel » | pops |
| 16,8 - 20 s | Le logo qui tourne, « Bilengi, les délices d'Afrique » | la gorgée, juste avant |
| 20 - 24 s | Bar à jus Bilengi Bio, Matadi, 16 av. Sita Landu (réf. rond-point RTNC), Réservation 081 554 4433, Livraison à domicile | carillon |

## Le clip IA (à générer, puis à mettre à la place du fond de la scène 1)
Règle : **aucune personne** (ni main, ni visage). On part d'une **photo réelle** (image → vidéo) pour que le produit reste juste, et on garde le logo net par-dessus en motion design.
Image de départ conseillée : `assets/img/bouteilles.jpg` (leurs bouteilles) ou `assets/img/verre.jpg`.
Format 9:16, 5 secondes. Outils : voir `prospection/IA_VIDEO_OUTILS.md`.

1. **Bouteille fraîche** (depuis `bouteilles.jpg`) :
   « Slow cinematic push-in on three bottles of fresh orange-yellow fruit juice on a wooden table, cold condensation droplets running down the glass, tiny bubbles rising inside, soft morning light, fresh green leaves in the background, no people, no hands, product commercial style, vertical 9:16. »
   *(Lent travelling avant sur trois bouteilles de jus, gouttes de fraîcheur sur le verre, petites bulles, lumière du matin, feuilles vertes, aucune personne.)*
2. **Les fruits qui éclaboussent** (depuis `verre.jpg`) :
   « Pineapple, green apple and pink grapefruit juice streams pouring into a tall glass in slow motion, splashes and droplets flying, ice cubes dropping in, vivid green background, no people, no hands, high-end beverage commercial, vertical 9:16. »
   *(Ananas, pomme verte et pamplemousse qui coulent au ralenti dans un grand verre, éclaboussures, glaçons, fond vert vif, aucune personne.)*
3. **Ambiance fête, sans personne** (texte → vidéo, à recouvrir de notre texte) :
   « Festive outdoor juice bar stand at sunset in Central Africa, string lights, colorful fresh fruits (pineapple, passion fruit, ginger, red chili) on a wooden counter, glasses of juice with ice, gentle camera move, no people, vertical 9:16. »
   *(Stand de bar à jus en fête au coucher du soleil, guirlandes, fruits frais sur un comptoir en bois, verres de jus, aucune personne.)*

Une fois le clip téléchargé : le mettre dans `assets/video/`, puis l'ajouter en `<video class="clip">` derrière le texte de la scène 1 (0 à 3,3 s), avec un voile vert léger pour que le texte reste lisible.

Fabrication : `python3 ameliorer.py <RealESRGAN_x4plus.pth>`, `python3 mix.py`, `npx hyperframes@0.8.77 render . -q high -o renders/raw.mp4`, compression ffmpeg → `renders/bilengi.mp4`.
