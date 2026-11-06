# +243 Fast Food (Lubumbashi) : « le burger parfait » + le menu croustillant (23,5 s, sans voix)

Demande de Mike : un mélange d'ingrédients qui forment le burger parfait, les autres plats du menu montrés de façon croustillante, avec des bruitages gourmands.
Toutes les images viennent des 8 captures envoyées par Mike (logo, stories « Menu »). Aucun prix, aucune personne. Couleurs de leur logo : noir, rouge, blanc, et le ruban rouge à encoches de leur menu.

| Temps | Scène | Son |
|---|---|---|
| 0 - 2,4 s | Logo, « Lubumbashi, le burger parfait ? » | impacts |
| 2,4 - 9,2 s | « Les ingrédients » : les 6 ingrédients de leur menu arrivent en étiquettes (salade, tomate, oignon, cornichon, sauce cheddar, 150 g de viande hachée), les 5 couches du Classique tombent une par une, le mélange est aspiré au centre et tout se resserre d'un coup (miettes, flash), reflet sur le pain, vapeur, « Le Classique, servi avec des frites » | chute de chaque couche, croc, grésillement |
| 9,2 - 12,4 s | « Et voici le +243 », le burger, vapeur, « 150 g de viande hachée » | croc, grésillement |
| 12,4 - 18,4 s | « Croustillant, tout le menu » : ailes de poulet, chicken fingers, buffalo wings, pizza Pepperon, shawarma, frites (un plat par « croc », miettes qui éclatent) | croustillant à chaque plat |
| 18,4 - 19,9 s | « Burgers, poulets, pizzas, shawarmas… » : 4 plats en grille | pops |
| 19,9 - 23,5 s | Logo, « +243 Fast Food », Lubumbashi, Bâtiment Hypnose · Av. Mama Yemo, « Livraison disponible », +243 991 815 555 | carillon |

Fabrication :
1. `python3 ameliorer.py <RealESRGAN_x4plus.pth>` : recadrage des plats sur les captures (`work/src`), agrandissement Real-ESRGAN (x8 pour les plats montrés en grand), pastilles de prix retirées, détourage rembg.
2. `python3 couches.py` : le Classique coupé en 5 couches (pain, tomate, cheddar + viande, tomate, frites) et le logo en disque.
3. `python3 bruitages.py` : bruitages gourmands fabriqués (croustillant, croquer, grésillement, couche).
4. `python3 mix.py` puis `npx hyperframes@0.8.77 render . -q high -o renders/raw.mp4`, compression ffmpeg → `renders/243-fast-food.mp4`.

À vérifier : le numéro +243 991 815 555 (lu en petit sur le menu).
