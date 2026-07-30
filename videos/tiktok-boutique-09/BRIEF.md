---
workflow: general-video
flow: automation
storyboard: no
message: "Toutes ces lecons disent la meme chose : il est temps de transformer ta boutique WhatsApp en vraie boutique en ligne."
destination: tiktok
aspect: 1080x1920
language: fr
audience: "petits commercants qui vendent en ligne"
length: 28.4s
angle: "recap de la semaine + transformation, ton direct, deuxieme personne (tu) - contenu 'dimanche' du calendrier hebdo ADG"
---

## Intent

Neuvieme video de la serie (contenu "dimanche": transformation). Recap rapide des 6 lecons de la semaine (site pro, outils, preparation pub, temps de reponse, phase d'apprentissage, confiance), concluant sur le vrai fil rouge: transformer sa boutique WhatsApp en vraie boutique en ligne. CTA: "Le lien est en bio".

**Toutes les images sont reutilisees telles quelles depuis les videos precedentes (02 a 08)** — aucune nouvelle photo/generation, sur demande explicite de l'utilisateur.

## Assets (tous reutilises, aucune nouvelle generation)

- Accroche: `accroche-1-erreurs.jpg` (= v06 accroche-erreur-alerte.jpg) / `accroche-2-clients.jpg` (= v04 money-bag-loss.jpg) / `accroche-3-jourapresjour.jpg` (= v05 consequence-femme-bureau.jpg)
- Site+outils (lundi/mardi): `siteoutils-1-statut.jpg` (= v02 whatsapp-status-crowded.jpg) / `siteoutils-2-vraisite.jpg` (= v02 nyara-site.jpg) / `siteoutils-3-outils.jpg` (= v03 ecommerce-icons.jpg)
- Pub+reponse (mercredi/jeudi): `pubreponse-1-preparation.jpg` (= v04 rethink-planning.jpg) / `pubreponse-2-ciblage.jpg` (= v04 targeting-manual.jpg) / `pubreponse-3-reponse.jpg` (= v05 consequence-notif-badge.jpg)
- Apprentissage+confiance (vendredi/samedi): `confiance-1-tropto.png` (= v05 declic-sablier.png) / `confiance-2-prix.png` (= v06 accroche-pub-explose.png) / `confiance-3-confiance.png` (= v08 probleme-1-confiance.png)
- Transformation: `transformation-1-lecons.jpg` (= v06 erreur-reflexion.jpg) / `transformation-2-transformer.jpg` (= v05 solution-boutique-illustration.jpg) / `transformation-3-vraieboutique.jpg` (= v02 saudagar-site.jpg)
- CTA: `cta-lienenbio.png` (= v05 cta-link-in-bio.png)

## Customizations

- **Sous-titres/captions obligatoires** (regle permanente depuis la video 4).
- **3 images sequentielles par scene, coupe nette** (regle permanente depuis la video 7) sur les 5 scenes narratives; CTA = image unique.
- Voix-off: voix locale Kokoro (`ff_siwis`, francais).
- Meme systeme de marque (preset blockframe) que les videos precedentes.
- Ton direct, deuxieme personne ("tu"), jamais "je". CTA final: "Le lien est en bio".
- Pas de mention de l'IA.

## Notes

- Script ecrit et valide par l'utilisateur mot pour mot.
- Timing des 3 images par scene calcule a partir des timestamps mots-a-mots (estimation deterministe par poids de caracteres), en localisant les frontieres de clause dans chaque `audio/lines/NN.words.json`.
