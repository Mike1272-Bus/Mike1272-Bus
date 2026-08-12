---
workflow: general-video
flow: automation
storyboard: no
message: "Mon avis : ton produit est bon, mais ta page ressemble a un profil personnel, pas a un business."
destination: tiktok
aspect: 1080x1920
language: fr
audience: "petits commercants qui vendent en ligne"
length: 117s
angle: "avis premiere personne, ton direct - contenu 'mercredi' du calendrier hebdo semaine 3 ADG"
---

## Intent

Douzieme video produite (Mercredi, semaine 3 du calendrier hebdo - a ne pas confondre avec
l'ancien script "Mercredi paiement" de la semaine 2, jamais construit). Message: le vrai
probleme n'est pas le produit mais l'image de la page (photo de profil floue, pas de nom
clair, contenu mélangé perso/business) - ca fait fuir un client avant meme qu'il pose une
question. Solution gratuite en 10 minutes, puis version "boutique en ligne" pour ne plus la
reconstruire a chaque fois.

## Format visuel — NOUVEAU pour cette video

A la demande explicite de l'utilisateur ("créer une vidéo avec du texte motion design qui
bouge avec une flèche/curseur comme sur un ordi pour les effets, transitions"), cette video
abandonne le format BlockFrame photo-sequentielle des videos precedentes pour un format
**typographie cinetique + curseur desktop simule**:

- Chaque ligne de voix-off est decoupee en groupes de mots (2-3 mots ou fin de ponctuation).
- Chaque groupe s'affiche en grand texte (carte blanche, bordure/ombre noire) au centre de
  l'ecran, popping in/out en rythme avec la voix.
- Un curseur de souris (fleche blanche/noire) se deplace vers une position deterministe
  avant chaque groupe, fait un "clic" (pulse + effet ripple), puis le texte apparait —
  imite une interaction d'ordinateur, sert de transition entre les groupes.
- Fond en aplat de couleur (palette BlockFrame habituelle : bleu/rose/creme/jaune/vert),
  meme badge numerote que le reste de la serie pour la coherence visuelle globale.
- **Le texte cinetique remplace le bandeau de sous-titres habituel** (regle "captions
  obligatoires" respectee via ce texte synchronise au mot, plus visible qu'un bandeau bas
  d'ecran classique).

## Audio

Vraie voix de l'utilisateur (audio/voice.mp3, 116.846s, une seule piste continue pour les
8 lignes - le CTA est cette fois vocalise, contrairement a la video 11 ou il etait muet).
Decoupage des 8 lignes fait par estimation ponderee par nombre de caracteres, recale sur
les silences detectes (ffmpeg silencedetect) - pas d'ASR disponible dans cet environnement.

Note: la duree totale de cet audio est ~15-20% plus longue que ce que ce texte donnerait a
un debit "normal" (comme les videos precedentes) - debit plus lent/pose sur cet
enregistrement precis, confirme coherent ligne par ligne (pas un signe de script errone).

## Assets

Aucune photo fournie cette fois (utilisateur presse, "je n'ai pas le temps de t'envoyer des
photos") - video entierement generee via texte + curseur, sans aucune image externe.

## Customizations

- CTA: mot-cle DM "MARQUE" (deja vocalise dans l'audio, contrairement aux videos precedentes
  ou le CTA visuel etait muet et genere separement).
- Pas de mention de l'IA.
- Meme systeme de couleurs (preset blockframe) que le reste de la serie.
