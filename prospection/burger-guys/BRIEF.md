# Burger Guys (Kinshasa) : vidéo « les ingrédients forment le burger » (22 s, sans voix)

Toutes les images viennent des 7 photos et de la capture du profil envoyées par Mike. Les photos font 300 px : elles ont été agrandies ×4 avec un modèle de super-résolution (EDSR, `upscale.py`) avant le détourage. Les seuls textes repris de chez eux : « The Real Ones » (leur logo) et le néon « Homemade with ♥ » de leur salle (traduit « Fait maison, avec amour »). Aucun prix, aucune promesse de livraison.

| Temps | Scène |
|---|---|
| 0 - 1,4 s | « KINSHASA » · « Tu as faim ? » |
| 1,4 - 6,9 s | Les 5 couches de leur burger arrivent une par une, écartées, avec leur étiquette : le pain, la salade, le steak + le cheddar, la sauce, le pain du dessus |
| 6,9 - 9,5 s | Tout se resserre d'un coup (impact, miettes), reflet sur le pain, vapeur, « The Real Ones », « Burger Guys, Kinshasa » |
| 9,6 - 12,4 s | Le burger se range dans le coin : « Et à côté… les onion rings », cartes « Les frites », « Le poulet pané » |
| 12,4 - 14,2 s | Leur photo du menu tombe : « Le menu complet », « Burger, frites, poulet pané et sauces » |
| 14,3 - 17,8 s | Leur salle, le néon « Homemade with ♥ » qui s'allume, « Fait maison, avec amour. » |
| 17,9 - 22 s | Logo Burger Guys, « On t'attend ! », « Burger Guys · Kinshasa », le burger qui remonte |

Fabrication : `upscale.py` (agrandissement, dans un venv avec opencv-contrib), `crop.py` (détourage), `layers.py` (couches du burger), `mix.py` (son), puis `npx hyperframes@0.8.77 render -o renders/burger-guys.mp4`.
Le numéro de contact n'est pas dans la vidéo (pas encore connu) : à ajouter sur la carte de fin dès qu'on l'a.
