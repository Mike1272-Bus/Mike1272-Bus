---
workflow: general-video
flow: companion
storyboard: yes
message: "Ta compétence, même sans diplôme, peut devenir un produit digital que tu vends."
destination: instagram-reels
aspect: 1080x1920
language: fr
length: 85s
audience: "Jeunes francophones (RDC/Afrique) sans emploi ou sous-payés, cible d'une pub Meta clic-vers-WhatsApp"
narration: yes
---

## Intent

Publicité Meta (clic-vers-WhatsApp) pour DigitalMikaelson, qui vend l'ebook
"Gagne ta vie sans diplôme". Structure de rétention : Hook visuel + sonore,
promesse explicite, puis 3 parties de valeur chacune suivie d'une boucle
ouverte, puis CTA. Ton encourageant, jamais moralisateur. Aucun prix affiché.

## Voix off (verbatim, VO_MODE, ne pas reformuler)

Environ 225 mots, soit environ 85 s à 2,65 mots/s. Voix générée par
l'utilisateur sur ElevenLabs.

| Bloc | Texte |
|---|---|
| Hook | Vous avez déjà un savoir-faire qui vaut de l'argent. Vous ne le savez juste pas encore. |
| Promesse | Je vais vous expliquer exactement pourquoi, dans quelques secondes. |
| Partie 1 | Que vous soyez salarié, étudiant, ou sans emploi, vous savez faire quelque chose : cuisiner, coudre, parler une langue, tenir une comptabilité. Et quelqu'un, quelque part, a besoin d'apprendre exactement ça. |
| Boucle ouverte 1 | Et pourtant... ce n'est même pas la partie la plus folle. |
| Partie 2 | Avec un produit digital, vous pouvez le lui enseigner à des milliers de kilomètres, sans jamais le rencontrer. Mon oncle David, menuisier, a transformé son savoir-faire en produit digital, sans budget pub. |
| Boucle ouverte 2 | Mais ce n'est toujours pas le plus important. |
| Partie 3 | J'ai écrit le guide pour faire pareil. Dedans, je vous explique pourquoi le diplôme n'est pas nécessaire pour commencer. Comment vous faire connaître sur internet. Quelle forme donner à votre produit. Comment le fabriquer et le vendre avec ce que vous avez déjà. Et comment savoir en une semaine si des gens en veulent, sans dépenser un centime. En suivant le guide, vous saurez ce que vous vendez et à qui, vous aurez un premier produit, et vous saurez si des gens sont prêts à le payer. Pas de blabla, juste ce qu'il faut faire, concrètement. |
| Boucle ouverte 3 | Et la meilleure partie ? Il suffit d'un message pour commencer. |
| CTA | Cliquez sur "Envoyer un message", écrivez-moi sur WhatsApp, et je vous accompagne. |

Badges à l'écran pendant la Partie 3 : 1. Pas besoin de diplôme,
2. Se faire connaître, 3. Choisir son produit (+ exemples : petit livre,
vidéo, modèle à remplir, checklist, kit), 4. Créer et vendre,
5. Tester en 7 jours.

## Direction visuelle (validée par l'utilisateur)

- Style de référence : motion design 2D en couches façon Alight Motion
  (photos détourées et extraits vidéo dans des cartes inclinées avec ombre
  portée, badges et textes qui glissent, rangées d'icônes en cascade,
  éclats décoratifs, légère parallaxe/perspective 3D). Pas de rendu 3D
  d'objet photoréaliste (pas d'outil de modélisation disponible) : la
  couverture de l'ebook sera animée en pseudo-3D.
- Fond : papier quadrillé clair (grille fine grise sur blanc cassé).
- Police : Baloo 2 ExtraBold, texte noir, accent orange pour les mots clés.
- Sous-titres : surlignage jaune mot par mot synchronisé à la voix off
  (style karaoké).

## Plan des extraits vidéo réels

| Partie | Extrait | Statut |
|---|---|---|
| Hook | 3 ou 4 plans de 0,5 s : mains qui cuisinent, cousent, écrivent, comptent | à fournir |
| Promesse | aucun (texte + son) | - |
| Partie 1 | 1 extrait par domaine : cuisine, couture, langues, comptabilité (4 cartes en cascade) | à fournir |
| Boucles ouvertes | aucun (texte + son d'impact) | - |
| Partie 2 | quelqu'un qui donne un cours en appel vidéo | à fournir |
| Partie 3 | mains de menuisier qui travaillent le bois (vraie vidéo de l'oncle David si disponible, sinon plan générique qui ne prétend pas être lui), puis couverture de l'ebook en pseudo-3D | à fournir |
| CTA | l'utilisateur face caméra disant le CTA, ou main tenant un téléphone avec WhatsApp | à fournir |

8 à 10 extraits de 3 à 5 s, verticaux de préférence. Sources possibles :
appli Pexels sur le téléphone de l'utilisateur, ou tournage maison
(Pexels/Pixabay/Mixkit sont bloqués par le réseau de l'environnement).

## Effets sonores (bibliothèque locale, placés par Claude)

whoosh / whoosh-short sur les entrées de cartes, impact-bass sur chaque
boucle ouverte, riser avant la Partie 3, pop/click sur les icônes,
notification au CTA WhatsApp. Musique de fond via MusicGen local.

## Assets

- `assets/` : couverture réelle de l'ebook, `ch1_reseau.jpg`,
  `ebook_anglais.jpg`, `ebook_couture.jpg`, `ch3_cuisine.jpg`,
  `logo_card.png`, `wa_icon_clean.png`.
- 4 photos Canva (salarié, étudiante, sans emploi, comptabilité) : toujours
  pas téléchargeables depuis l'environnement, à fournir par l'utilisateur
  si besoin.
- Voix off : la vraie voix de l'utilisateur (pas de TTS), à enregistrer.

## Notes

- Numéro WhatsApp réel : +243 831 710 181. Ne jamais afficher de prix.
- Ne jamais inventer de statistique, de témoignage ou de date limite.
- Registre "vous" tout du long.
- Signature de marque au mot : "Pas de blabla, juste ce qu'il faut faire, concrètement."
- `STORYBOARD.md`, `frame.md` et `index.html` correspondent encore à
  l'ancienne version (58 s, fond navy) et seront réécrits sur ce brief.
