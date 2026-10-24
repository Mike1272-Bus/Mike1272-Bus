# Fatburger Kinshasa : vidéo « le burger monte, étage par étage » (22 s, sans voix)

Toutes les images viennent des photos et des captures envoyées par Mike (profil, story « Commandez maintenant »). Couleurs reprises de leur logo : bleu turquoise, jaune, rouge. Le seul texte repris de chez eux : « Commandez maintenant » (leur story). Aucun prix, aucune promesse de livraison.

Concept différent de Burger Guys : ici les couches tombent une par une et la tour monte, pendant que la caméra recule.

| Temps | Scène |
|---|---|
| 0 - 1,4 s | Rayons rétro qui tournent, « On monte un burger ? » |
| 1,4 - 6,5 s | Les 7 couches tombent et s'empilent : le pain, 1 steak, 2 steaks, 3 steaks !, tomate et cornichons, la salade, le pain du dessus |
| 6,5 - 9,3 s | Flash, reflet sur le pain, « Ça, c'est un BURGER. », le logo en tampon |
| 9,4 - 12,5 s | « Et pour aller avec… les milkshakes » : les 4 gobelets montent un par un |
| 12,7 - 15,5 s | Le plateau vu de dessus : « Burgers, frites, onion rings… pour toute la bande » |
| 15,7 - 18,2 s | Burger, frites, boisson et sac : « le menu complet » |
| 18,5 - 22 s | Logo, « Commandez maintenant », « Fatburger · Kinshasa », le burger |

Fabrication : `upscale.py` (agrandissement ×4 du burger, dans un venv avec opencv-contrib), `crop.py` (détourage), `layers.py` (couches et gobelets), `mix.py` (son), puis `npx hyperframes@0.8.77 render -o renders/fatburger.mp4`.

Note technique : les images sont déclarées dans les attributs `style` des balises, pas dans la feuille de style. Sinon, `hyperframes check` plante (« Maximum call stack size exceeded ») : il parcourt avec une regex tout ce qui précède la balise racine, images intégrées comprises.
