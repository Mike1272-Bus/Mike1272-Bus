---
workflow: general-video
flow: automation
storyboard: no
message: "Demo de 10 techniques de motion design appliquees a de vraies photos (pas des formes abstraites), en identite Blockframe ADG."
destination: tiktok
aspect: 1080x1920
language: fr
audience: "Mike (fondateur ADG) - decision creative interne, pas un post client"
angle: "showcase technique, pas de narration, pas de CTA produit"
length: ~22s
---

## Intent

Suite a la demo motion-design-demo (formes abstraites), l'utilisateur a demande la meme chose mais avec de vraies photos deja envoyees, pour voir comment habiller de vraies images avec du mouvement plutot qu'un simple pop-in ou fondu.

10 photos deja recues et validees (sans filigrane/marque tierce) dans le projet tiktok-boutique-18, reutilisees telles quelles :
- l01-imagemarque.jpeg, l03-negocie.jpeg, l04-livraisonretard.jpeg, l05-inspirerconfiance.jpeg,
  l06-boutiqueenligne.jpeg, l07-petitsvendeurs.jpg, l08-dejapaye.jpeg, l08-doitreponse.jpeg,
  l08-prendauserieux.jpeg, l08-vraieentreprise.jpeg

Une technique differente par photo, chacune etiquetee a l'ecran (vocabulaire pedagogique) :
1. Ken Burns (zoom + pan lent)
2. Reveal par masque (wipe horizontal anime, pas un fondu)
3. Iris circulaire (cercle qui s'agrandit pour reveler)
4. Bascule 3D (rotateY, perspective)
5. Parallaxe (photo et cadre bougent a des vitesses differentes)
6. Whip pan (transition rapide avec flou de mouvement)
7. Diagonale (clip-path polygon anime)
8. Duo split-screen (deux photos entrent simultanement de chaque cote)
9. Légende cinétique sur la photo (texte qui se revele par-dessus l'image)
10. Focus pull (flou + zoom qui se stabilise net, sortie)

## Customizations

- Identite Blockframe : jaune #F7CB46, noir, creme #FFFDF5, police display "Arial Black", fond a pois, cadres bordure noire + ombre portee dure.
- Pas de voix-off, pas de sous-titres narratifs - juste le nom de la technique affiche en etiquette.
- Logo ADG en coin sur chaque scene.

## Notes

- Demande directe de l'utilisateur ("Fais en avec 10 images que je t'ai envoyé récemment"), suite de la conversation sur le motion-design-demo precedent.
- GSAP core uniquement (clip-path, transform, perspective - pas de plugin premium).
