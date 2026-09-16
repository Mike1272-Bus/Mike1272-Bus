---
workflow: general-video
flow: automation
storyboard: no
message: "David a filmé son atelier une seule fois — et son guide continue de se vendre pendant qu'il travaille sur autre chose."
destination: tiktok
aspect: 1080x1920
language: fr
length: ~35-40s
angle: "suite directe d'academy-01 (storytelling personnel, méthode REVEAL) — preuve concrète par l'histoire de David"
audience: "petits entrepreneurs/artisans francophones (Afrique/RDC) qui ont un métier manuel ou un savoir-faire"
---

## Intent

"Épisode 1, Partie 2" pour la marque **DigitalMikaelson** (série Michaelson
Digital Academy, pilier Produits Digitaux). C'est la suite directe
d'`academy-01`, qui se terminait sur le cliffhanger "Et pour David... est-ce
que ça a marché ? La suite arrive demain." Ce nouvel épisode répond à la
question : montre concrètement comment David (menuisier, 20 ans de métier) a
transformé son savoir-faire en produit digital, ses débuts hésitants, ses
premières ventes, et se termine par un CTA "Abonne-toi" animé.

Ouverture : hook typewriter reprenant l'identité de la série — "ÉPISODE 1"
tapé lettre par lettre (même mécanique que dans academy-01), suivi de
"PARTIE 2" tapé de la même façon (même style : gris, monospace, curseur qui
clignote, clic clavier en sound effect).

## Beats (découpage fourni par l'utilisateur)

1. **Pour David, ça voulait dire...** — texte motion design + petite
   illustration animée : "filmer une seule fois comment il construit une
   table" (extraits vidéo à venir) → "et vendre cette vidéo" (illustration :
   image vidéo à gauche + argent à droite qui s'avancent et se rejoignent en
   une petite explosion) → "à quelqu'un qui veut apprendre" (extraits vidéo)
   → "où qu'il soit" (extraits vidéo).
2. **Au début, il n'y croyait pas** — motion design très explicatif avec
   illustrations qui bougent → "Qui va payer pour regarder un vieux
   menuisier travailler ?" (extraits vidéo).
3. **Mais on a essayé quand même** — illustrations fluides qui bougent →
   "On a filmé son atelier" (extraits vidéo) → "ses mains, vingt ans de
   métier" (extraits vidéo).
4. **On en a fait un guide simple** — image de couverture du guide (canvas,
   à venir) → "étape par étape" (illustration : progression par étapes qui
   avance vers un point final, motion fluide).
5. **La première vente est tombée trois jours plus tard** — notification de
   vente générée en motion design → "Et une autre a suivi la semaine
   d'après" (notification x2).
6. **Aujourd'hui, David vend son guide pendant qu'il est dans son atelier**
   — motion design → "en train de construire autre chose" (extraits vidéo)
   + notification téléphone en overlay motion design.
7. **Si toi aussi tu as une compétence que tu utilises** — 4 images (à
   venir) qui apparaissent les unes après les autres, motion fluide →
   "depuis des années, tu as peut-être déjà un produit digital sans le
   savoir" (motion design très explicatif).
8. **Cette semaine, je te montre étape par étape comment David a fait** —
   illustration calendrier / jours de la semaine qui défilent → "Abonne-toi
   pour ne rien rater" (bouton "ABONNE-TOI" en motion design, suivi d'une
   flèche qui clique dessus avec un sound effect).

## Assets

Plusieurs beats référencent des extraits vidéo réels et des images que
l'utilisateur enverra ensuite (atelier, mains au travail, couverture du
guide, 4 images "compétences"). Construire ces beats avec des zones
`shot-card` prêtes à recevoir le média (mêmes classes que academy-01), à
défaut d'un placeholder motion-design temporaire clairement marqué en
attendant l'asset réel. Les beats purement motion design (emballage/argent,
notifications, calendrier, bouton abonne-toi) sont entièrement générés,
aucun asset externe requis.

## Customizations

- Voix : pas encore enregistrée — construire la timeline avec des durées
  provisoires raisonnables par beat, à resynchroniser (même technique de
  rescale proportionnel/silence-detect que academy-01) une fois la vraie
  voix envoyée.
- Système visuel Blockframe identique à academy-00/academy-01 : jaune
  #F7CB46, noir/encre #0A0A05, crème #FFFDF5, Archivo Black + Work Sans,
  bordures épaisses + ombre portée dure (pas de flou), fond à pois.
  Typewriter du hook : gris #6B6B66, monospace (JetBrains Mono via Google
  Fonts, injecté automatiquement par le compiler HyperFrames).
- SFX synthétisés localement via ffmpeg (pas de clé API requise) pour :
  clic clavier du hook, clic du bouton "Abonne-toi".
- CTA final : bouton "ABONNE-TOI" animé + flèche qui clique + son.

## Notes

- Pas de formes/motifs abstraits en remplissage — chaque scène doit annoncer
  clairement soit un vrai visuel (photo/vidéo à intégrer), soit une
  illustration motion design entièrement assumée comme telle.
- Respecter la règle du compte : pas de tirets longs, pas d'énumérations à
  trois éléments par réflexe stylistique, pas de virgule d'Oxford dans les
  textes affichés à l'écran.
- Marque : **DigitalMikaelson** (un seul mot, à utiliser tel quel dans toute
  communication/branding).
