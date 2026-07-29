---
workflow: general-video
flow: automation
storyboard: no
message: "L'erreur qui fait exploser le prix de tes pubs Facebook: y toucher pendant la phase d'apprentissage."
destination: tiktok
aspect: 1080x1920
language: fr
audience: "petits commercants qui font ou envisagent de faire de la pub Facebook/Meta"
length: 40s
angle: "guide/astuce pointue, ton direct, pas de bases evidentes - contenu 'vendredi' du calendrier hebdo ADG"
---

## Intent

Sixieme video de la serie (contenu "vendredi": guide). Angle resserre sur UNE erreur precise et peu connue plutot qu'un guide generaliste (rejete par l'utilisateur: "tout le monde sait tout ca"): la phase d'apprentissage de Facebook Ads, et l'erreur commune de modifier une pub trop tot, qui la fait recommencer a zero et exploser son cout. CTA: inciter a s'abonner pour apprendre a gerer sa pub correctement (pas de lien en bio cette fois).

## Assets (10 vraies images fournies par l'utilisateur + 1 illustration generee par l'agent)

- `accroche-pub-explose.png` — illustration: laptop avec bannieres "PUB", sac d'argent, pouce leve, icone Instagram. Accroche (top).
- `accroche-erreur-alerte.jpg` — illustration: main avec loupe sur des documents, triangle d'alerte rouge. Accroche (bottom).
- `explication-lancement.png` — illustration: fusee qui decolle. Explication (top) — le lancement d'une pub.
- `explication-apprentissage.png` — illustration generee par l'agent (deja validee par l'utilisateur): anneau de progression "60% Apprentissage" avec icone sablier. Explication (bottom).
- `erreur-impatience.jpg` — vraie photo: homme d'affaires qui regarde sa montre avec impatience. Erreur (top) — l'attente qu'on ne respecte pas.
- `erreur-reflexion.jpg` — illustration: personnage pensif au telephone avec ampoule d'idee, engrenages. Erreur (bottom) — la decision de modifier trop tot.
- `consequence-restart.jpg` — icone "RESTART" bleue avec fleches circulaires. Consequence (top) — le redemarrage a zero.
- `consequence-adsmanager.webp` — illustration: dashboard Ads Manager avec graphiques et loupe. Consequence (bottom) — le contexte ou ca se joue.
- `solution-multiplateforme.jpg` — illustration: mockup de pubs sur Facebook/Messenger/Instagram/WhatsApp. Solution (top) — une bonne gestion multi-plateforme.
- `solution-pub-reussie.webp` — vraie capture: exemple de pub Instagram/Facebook reussie (deux ecrans telephone, produit qui capte l'attention, bouton "Shop now"). Solution (bottom).
- `cta-sabonner.png` — illustration generee par l'agent: cloche de notification + bouton "S'ABONNER", style BlockFrame. CTA (scene unique).

## Customizations

- **Sous-titres/captions obligatoires** (regle permanente depuis la video 4).
- **Regle d'empilement des images** (regle permanente depuis la video 4): toutes les scenes a deux images (Accroche, Explication, Erreur, Consequence, Solution) empilent les cartes verticalement, une en haut une en bas, toutes deux entierement visibles, jamais superposees. La scene CTA est une image unique.
- Voix-off: voix locale Kokoro (`ff_siwis`, francais) en attendant la vraie voix de l'utilisateur.
- Meme systeme de marque (preset blockframe) que les videos 1 a 5 pour la coherence de la serie.
- Ton direct/insight, pas de bases evidentes. CTA final: inciter a s'abonner pour apprendre a bien gerer sa pub (pas de "lien en bio" cette fois, pas de produit).
- Pas de mention de l'IA.

## Notes

- Script ecrit en francais simple, deja valide par l'utilisateur mot pour mot (voir voiceover par frame dans STORYBOARD.md).
- Deux illustrations sont generees par l'agent lui-meme (HTML/CSS/SVG rendu via Playwright, style BlockFrame) faute d'acces a un generateur d'images IA dans cet environnement (HeyGen bloque par la politique reseau du sandbox): `explication-apprentissage.png` (deja validee) et `cta-sabonner.png` (nouvelle, a valider a la revue finale).
