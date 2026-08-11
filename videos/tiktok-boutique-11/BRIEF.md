---
workflow: general-video
flow: automation
storyboard: no
message: "L'outil gratuit que personne n'utilise pour prouver qu'on n'est pas une arnaque et rassurer instantanement."
destination: tiktok
aspect: 1080x1920
language: fr
audience: "petits commercants qui vendent en ligne"
length: 85s
angle: "outil/valeur pratique, ton pedagogique - contenu 'mardi' du calendrier hebdo ADG"
---

## Intent

Onzieme video de la serie (contenu "mardi": outil/valeur pratique). Le probleme du jour:
poster de belles photos sur TikTok/WhatsApp/Instagram ne prouve rien - n'importe qui peut le
faire, meme une arnaque. La solution: la fiche Google Business (gratuite, 10 minutes), qui
affiche etoiles et vrais avis clients, une preuve verifiable.

Voix reelle de l'utilisateur envoyee en un seul fichier audio continu (80.666s, 7 lignes),
sans ASR disponible dans cet environnement pour un decoupage mot-a-mot precis. Decoupage des
7 scenes fait par estimation ponderee par nombre de caracteres, recalee sur les silences
detectes (ffmpeg silencedetect) quand un pic de silence tombait a moins de 1.5s de l'estimation.

## Assets (25 images fournies par l'utilisateur, mappees par paragraphe ; 2 generees par l'agent)

- Accroche (4: 3 utilisateur + 1 generee): accroche-1.jpg / accroche-2.jpg / accroche-3.jpg /
  accroche-4.png (**generee** - l'original fourni avait un filigrane Dreamstime visible)
- Situation (3 utilisateur): situation-1.png / situation-2.jpg / situation-3.jpg
- Vrai probleme (3 utilisateur): vraiprobleme-1.jpg / vraiprobleme-2.png (deux femmes en robe,
  exemple de "belles photos qui ne prouvent rien") / vraiprobleme-3.jpg
- Consequence (2 utilisateur): consequence-1.jpg / consequence-2.jpg
- Declic (4 utilisateur, 1 doublon retire): declic-1.jpg / declic-2.jpg (capture Google
  Business reelle) / declic-3.jpg / declic-4.png
- Solution (5 utilisateur): solution-1.jpg / solution-2.jpg / solution-3.png / solution-4.jpg
  / solution-5.jpg (icone "10 minutes")
- Benefice (3 utilisateur): benefice-1.jpg / benefice-2.jpg / benefice-3.png
- CTA (1 generee par l'agent): cta-1.png - "Ecris GRATUIT en message", style BlockFrame

## Customizations

- **Sous-titres/captions obligatoires** (regle permanente depuis la video 4), synchronises sur
  la vraie voix via estimation ponderee par caracteres (pas d'ASR disponible).
- **Regle "images sequentielles par scene, coupe nette"** (regle permanente depuis video 7/8).
- Voix-off: vraie voix de l'utilisateur (audio/voice.mp3, piste continue unique pour les 7
  lignes, sans decoupage/reencodage - une seule piste audio sur tout le timeline principal).
- CTA muet (pas de ligne vocale enregistree pour le CTA) - carte visuelle statique 4.5s.
- Meme systeme de marque (preset blockframe) que les videos 1 a 10 pour la coherence de la serie.
- Mot-cle DM du CTA: "GRATUIT" - a brancher sur le systeme de reponse automatique (base de
  connaissances allegra-agent-kb.md), separement de ce livrable video.
- Pas de mention de l'IA.

## Notes

- Une image fournie par l'utilisateur portait un filigrane visible (Dreamstime, scene Accroche)
  - remplacee par une illustration generee en style BlockFrame ("100% GRATUIT").
  - la meme illustration deux-femmes-en-robe apparaissait par erreur en double dans "Vrai
  probleme" ET "Declic" - le doublon a ete retire de la scene "Declic" (elle appartient
  uniquement a "Vrai probleme", ou elle illustre exactement le propos).
