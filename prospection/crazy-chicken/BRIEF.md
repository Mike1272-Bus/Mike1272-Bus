# Crazy Chicken (Lubumbashi) : vidéo « seau de poulet » (20 s, sans voix)

Toutes les images viennent de leur affiche (capture Google Maps envoyée par Mike) : agrandie ×2 (EDSR x4 sur l'image réduite), puis détourée (rembg, modèle isnet-general-use) en 3 morceaux : le seau, le poulet pané + sauce, le logo. Textes repris de l'affiche : « Seau de poulet », « Salade de fruits », « Salade normal(e) ». Couleurs de leur affiche (orange vif, rouge du logo, blanc), police ronde Baloo 2. Aucun prix, aucun numéro (inconnu).

| Temps | Scène |
|---|---|
| 0 - 2,6 s | Logo, « Lubumbashi, une petite faim ? » |
| 2,6 - 7,6 s | « Notre grand seau de poulet » : le seau tombe et rebondit, miettes, « bien rempli et doré » |
| 7,6 - 11,6 s | Le poulet pané arrive avec sa sauce : « Croustillant », « avec sa sauce » |
| 11,6 - 14,6 s | « Et pour accompagner : » Salade de fruits, Salade normale |
| 14,6 - 20 s | Logo, « Crazy Chicken · Lubumbashi », le seau et le poulet, « Commandez maintenant ! » |

Fabrication : `assets/img/*.png` (détourages), `mix.py` (son), puis `npx --yes hyperframes@0.8.77 render . -q high -o renders/raw.mp4` et compression.
