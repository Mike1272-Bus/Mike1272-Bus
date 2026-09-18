---
workflow: general-video
flow: automation
storyboard: no
message: "Un like ne prouve rien. L'Engagement — le E de VENDRE — c'est ce qui prouve un vrai intérêt : un commentaire, une réponse, un aller-retour."
destination: tiktok
aspect: 1080x1920
language: fr
length: ~96s
angle: "contrarian — nomme la croyance classique (plus de likes/commentaires/partages = meilleur contenu) et la renverse : un like ne prouve rien, l'engagement se mesure à l'effort"
audience: "petits entrepreneurs/artisans francophones (Afrique/RDC) qui ont un métier manuel ou un savoir-faire"
---

## Intent

Épisode 4 de Michaelson Digital Academy / DigitalMikaelson, deuxième
deep-dive lettre par lettre de la méthode VENDRE : le **E — Engagement**.
Suit l'angle éditorial contrarian défini dans `../BLOCKFRAME-STYLE.md`.

Structure : croyance classique (likes/commentaires/partages = bon contenu)
→ renversée (un like ne prouve rien) → définition de l'Engagement dans
VENDRE → 3 implications concrètes (commentaire > like, contenu qui donne
une raison de réagir, répondre compte autant que publier) → teaser du
guide gratuit VENDRE (lead magnet fin de module) → CTA "abonne-toi + commente
'présent'" (CTA thématique, pas le CTA standard, à la demande explicite de
l'utilisateur pour cet épisode).

## Assets

19 extraits vidéo/images réels envoyés par l'utilisateur via le dropbox
GitHub `main`, un par clause de script. Le reste (roadmap VENDRE E-allumé,
mégaphone, pouce qui se dégonfle, pouce barré, checklist "trois choses",
badges numérotés 1/2/3, bulles de discussion question/opinion/débat,
cadenas qui se déverrouille) est du motion design animé, en priorisant les
illustrations qui bougent plutôt que le texte statique, à la demande de
l'utilisateur.

## Customizations

- Hook typewriter "ÉPISODE 4" — mécanique standard.
- CTA : variante thématique "Abonne-toi + commente 'présent' pour montrer
  que tu es là" (demandée explicitement pour cet épisode, cohérente avec
  le thème de l'engagement) plutôt que le CTA générique habituel.
- Voix off reçue et intégrée : resynchro complète sur 94.5s de voix réelle
  (modèle proportionnel au nombre de mots ancré sur les silences mesurés).
- Volume : même recette que l'épisode 3 (compression + loudnorm en mode
  dynamique ciblant un pic sûr) — -13.5 LUFS / -1.8 dBTP en sortie, safe
  pour l'encodage AAC du rendu.
- Bug corrigé en cours de build : un cadenas (illustration du guide
  gratuit) restait visible en arrière-plan sur tout l'épisode à cause d'un
  `fromTo` GSAP démarrant depuis `opacity:1` au lieu de la valeur par
  défaut `opacity:0` — corrigé en repartant systématiquement de l'état
  caché par défaut.

## Notes

- Continuité : réutilise `guide-menuiserie-cover.jpg` (déjà utilisé dans
  academy-03) pour la mention d'Oncle David dans le teaser du guide
  gratuit — pas de nouveau tournage nécessaire.
- Marque : **DigitalMikaelson**.
