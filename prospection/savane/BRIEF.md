# Savane Kinshasa : vidéo élégante (22 s, sans voix)

Restaurant au Hilton Kinshasa, 2ème étage (groupe Miraya's Food & Beverages). Univers haut de gamme : noir, or, jungle, motifs. Tout vient de leurs publications Instagram et de leur vidéo « Le plaisir commence dans les détails ». Toutes les phrases sont les leurs (légendes de leurs publications). On n'utilise pas les stories de clientes repartagées (photos et noms de personnes).

Style : sobre et luxueux, pas de motion « fun ». Police Cormorant Garamond (serif) + Work Sans, frise grecque dorée reprise des lettres de leur logo.

| Temps | Scène |
|---|---|
| 0 - 2,6 s | Deux frises dorées se dessinent, le logo Savane apparaît, « Kinshasa » |
| 2,6 - 5,25 s | Leur vidéo : la carte s'ouvre, les pages. « Le début parfait de votre expérience Savane » |
| 5,25 - 9,85 s | Leur vidéo : la préparation des sushis. « Le plaisir commence dans les détails. » |
| 9,85 - 15 s | Leurs photos dans des cadres dorés : cocktail (« Préparé avec précision. Servi avec caractère. »), calamars et bouchées (« De nouvelles bouchées font leur entrée à la carte. »), plateau (« Retrouvez ceux qui comptent. ») |
| 15 - 16,75 s | Leur vidéo : le plateau vu de dessus. « Réservez chez Savane. » |
| 16,8 - 22 s | Logo entre les frises, « Hilton Kinshasa · 2ème étage », « Réservations », +243 988 533 333 |

Fabrication : `crop.py` (logo, photos sans le texte imprimé), `mix.py` (son), puis `npx hyperframes@0.8.77 render -o renders/savane.mp4`. Les extraits vidéo sont coupés directement dans la composition (`data-media-start`).
