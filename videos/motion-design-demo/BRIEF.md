---
workflow: general-video
flow: automation
storyboard: no
message: "Demo courte montrant 4 techniques de vrai motion design (texte cinetique, morph de forme, compteur anime, carte 3D + particules), en identite Blockframe ADG."
destination: tiktok
aspect: 1080x1920
language: fr
audience: "Mike (fondateur ADG) - decision creative interne, pas un post client"
angle: "showcase technique/creatif, pas de narration, pas de CTA produit"
length: ~18s
---

## Intent

Suite a la question de l'utilisateur "Comment creer du vrai motion design ?", demo de 4 techniques distinctes pour montrer la difference avec les simples pop-in d'images utilises jusqu'ici dans les videos TikTok ADG:

1. Texte cinetique (kinetic typography) - le titre se dessine/apparait mot par mot avec effet de "wipe"
2. Morph de forme - un cercle se transforme en carre arrondi (border-radius + rotation), pas juste un fade
3. Icone + compteur anime - un graphique de croissance qui monte, un chiffre qui s'incremente en direct
4. Carte finale en pseudo-3D + particules - une carte avec effet de profondeur (tilt 3D CSS) et des particules qui flottent en arriere-plan

Pas de voix-off, pas de produit, pas de CTA - pur showcase visuel pour que Mike juge s'il veut ce style pour du contenu futur.

## Customizations

- Identite Blockframe : jaune #F7CB46, noir #000, creme #FFFDF5, police display "Arial Black", fond a pois (dotgrid), cartes bordure noire epaisse + ombre portee dure (meme systeme que toutes les autres videos/carrousels ADG).
- Sous-titres/voix : aucun (demo muette, juste un fond musical optionnel si disponible, sinon silencieux).
- Format vertical 1080x1920 (TikTok), single composition (pas de sous-scenes separees, duree courte).

## Notes

- Demande directe de l'utilisateur ("Vas-y montre ça"), pas d'interview brief menee - contexte deja fourni dans ma proposition precedente (liste des 4 techniques).
- GSAP core uniquement (pas de plugin MorphSVG premium) - le "morph de forme" est fait via border-radius/scale/rotate, pas via interpolation de path SVG.
