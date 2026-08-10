---
workflow: general-video
flow: automation
storyboard: no
message: "Tes clients negocient toujours le prix en DM ? Le probleme c'est pas eux, c'est qu'aucun prix n'est jamais affiche clairement."
destination: tiktok
aspect: 1080x1920
language: fr
audience: "petits commercants qui vendent en ligne"
length: 51s
angle: "listicle/pedagogique, ton doux, pas confrontationnel - contenu 'lundi' du calendrier hebdo ADG"
---

## Intent

Dixieme video de la serie (contenu "lundi": pedagogique, ton doux). Le probleme du jour: les clients negocient toujours le prix en message prive parce qu'aucun prix n'est jamais affiche clairement nulle part. Reponse pedagogique et doute-desamorcante (pas confrontationnel): montrer qu'avec une vraie fiche produit/boutique en ligne, le prix visible desamorce la negociation. CTA doux: ecrire "BOUTIQUE" en message (le lien en bio n'est pas encore regle cote utilisateur).

Script valide mot pour mot par l'utilisateur avant construction (voir voiceover par frame dans STORYBOARD.md).

## Assets (25 images fournies par l'utilisateur, mappees par lui-meme par paragraphe/scene ; 3 images generees par l'agent en remplacement d'images filigranees + l'image du CTA)

- Accroche (3 images utilisateur): accroche-1.jpg / accroche-2.jpg / accroche-3.jpg
- Situation (3 images utilisateur): situation-1.jpg / situation-2.jpg / situation-3.png
- Vrai probleme (5 images utilisateur): vraiprobleme-1.png / vraiprobleme-2.jpg / vraiprobleme-3.jpeg / vraiprobleme-4.png / vraiprobleme-5.jpg
- Consequence (3 images utilisateur): consequence-1.jpg / consequence-2.png / consequence-3.jpg
- Declic (4 images utilisateur): declic-1.jpeg / declic-2.jpg / declic-3.jpg / declic-4.jpg
- Solution (3 images: 2 utilisateur + 1 generee): solution-1.png (**genere** — l'original fourni avait un filigrane 123RF visible) / solution-2.jpg / solution-3.png
- Benefice (4 images: 3 utilisateur + 1 generee): benefice-1.jpg / benefice-2.webp / benefice-3.jpg / benefice-4.png (**genere** — l'original fourni avait un filigrane Dreamstime visible)
- CTA (1 image generee par l'agent, a la demande explicite de l'utilisateur "le CTA tu t'en charges"): cta-1.png — visuel "Ecris BOUTIQUE en message" style BlockFrame

## Customizations

- **Sous-titres/captions obligatoires** (regle permanente depuis la video 4).
- **Regle "3 images sequentielles par scene, coupe nette"** (regle permanente depuis video 7/8) — adaptee ici avec un nombre variable d'images par scene (3 a 5), selon ce que l'utilisateur a fourni par paragraphe.
- Voix-off: voix locale Kokoro (`ff_siwis`, francais) en attendant la vraie voix de l'utilisateur (envoyee a ElevenLabs separement, pas encore integree a ce rendu).
- Meme systeme de marque (preset blockframe) que les videos 1 a 9 pour la coherence de la serie.
- Ton pedagogique/doux, deuxieme personne ("tu"), jamais "je".
- **CTA**: "Ecris BOUTIQUE en message" — PAS de "lien en bio" (probleme du lien en bio pas encore regle cote utilisateur au moment de la production). Mot-cle "BOUTIQUE" a brancher sur le systeme de reponse automatique DM (base de connaissances allegra-agent-kb.md), separement de ce livrable video.
- Pas de mention de l'IA.

## Notes

- Script ecrit en francais simple et parle, deja valide mot pour mot par l'utilisateur (accroche choisie parmi 5 propositions "ghostwriter").
- Deux images fournies par l'utilisateur portaient un filigrane visible (123RF sur l'image "solution", Dreamstime sur l'image "benefice") — remplacees par des illustrations generees en style BlockFrame (HTML/CSS/SVG + capture Playwright, meme methode que les 16 illustrations de la video 7), a la demande explicite de l'utilisateur.
- Timing des images par scene: repartition egale sur la duree de la ligne de voix-off (pas d'ASR disponible dans cet environnement pour un alignement mot-a-mot precis — meme contrainte que les videos precedentes).
