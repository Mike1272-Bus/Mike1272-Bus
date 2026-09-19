# Contexte projet — Michaelson Digital Academy / DigitalMikaelson

Document de passation à joindre à une nouvelle session Claude pour qu'elle
reprenne le travail en parallèle de celle-ci, sans avoir à relire tout
l'historique de conversation. Dépôt : `Mike1272-Bus/Mike1272-Bus`, branche
de travail `claude/hyperframe-skill-setup-h5eamt`.

## Le projet

Série de vidéos verticales (TikTok/Reels, 1080×1920) pour la marque
**DigitalMikaelson** (un seul mot), pilier "Produits Digitaux" de
Michaelson Digital Academy. Public cible : petits entrepreneurs/artisans
francophones (Afrique/RDC) avec un métier manuel ou un savoir-faire.

Construites avec le framework **HyperFrames** (HTML/CSS/GSAP → rendu MP4
via Chrome headless). Chaque épisode est un projet séparé dans
`videos/academy-0X/`.

**Lire en premier** : `videos/BLOCKFRAME-STYLE.md` — guide de style
durable (palette, typo, sizing des éléments motion design, pattern du CTA
"Abonne-toi", règle d'angle éditorial contrarian, usage des vrais logos).
Toutes les règles qu'il contient s'appliquent sans qu'on ait besoin de les
redemander.

## La série : personnage et framework

- **Oncle David** : menuisier, personnage récurrent qui illustre chaque
  concept. A créé un guide digital de menuiserie ("Guide Ultime du
  Menuisier"), l'a vendu sans budget pub, uniquement via le marketing
  digital.
- **VENDRE** : le framework marketing digital introduit à l'épisode 2 —
  **V**isibilité, **E**ngagement, **N**otoriété, **D**istribution,
  **R**elance, **É**volution. Un épisode par lettre à partir de l'épisode 3,
  cadence annoncée par l'utilisateur : 2 vidéos par jour.

## État des épisodes

| Projet | Contenu | Statut |
|---|---|---|
| `academy-01` | Épisode 1 — histoire d'Oncle David (partie 1) | Livré, voix synchronisée, rendu final envoyé |
| `academy-01-partie2` | Épisode 1, partie 2 | Livré, voix synchronisée, rendu final envoyé |
| `academy-02` | Épisode 2 — présentation du framework VENDRE | Livré, voix synchronisée, rendu final envoyé |
| `academy-03` | Épisode 3 — **V, Visibilité** | Livré, voix synchronisée, rendu final envoyé |
| `academy-04` | Épisode 4 — **E, Engagement** | Livré, voix synchronisée, rendu final envoyé |
| `academy-05` (à créer) | Épisode 5 — **N, Notoriété** | Script rédigé et humanisé, **en attente de validation de l'utilisateur** avant scaffold/assets |

## Script épisode 5 en attente de validation

```
Épisode 5.

On te dit : pour être connu, il faut viser le plus grand nombre et plaire
à tout le monde. En vrai, la notoriété n'a rien à voir avec ça. Être
reconnu, c'est être reconnu pour une seule chose précise, par les bonnes
personnes.

Dans notre stratégie VENDRE, le N, c'est la Notoriété. Concrètement,
c'est le moment où on commence à te reconnaître pour un sujet précis. Pas
pour tout. Pour un seul truc.

Et ça implique trois choses concrètes. Un : spécialise-toi sur un seul
angle plutôt que de parler de tout. Plus tu es précis, plus on te
reconnaît vite. Deux : reste reconnaissable, avec le même ton et le même
style à chaque vidéo. Trois : répète le même message jusqu'à ce qu'il
soit associé à toi. Toi, tu en as peut-être marre de le dire. Les autres
viennent tout juste de l'entendre pour la première fois.

Regarde Oncle David. Il ne parle pas de tout l'artisanat, juste de son
guide de menuiserie. Résultat : quand quelqu'un pense à un guide pratique
pour apprendre un métier manuel, c'est lui qu'on recommande.

Une fois que tu es reconnu pour ton truc, l'étape suivante, c'est de
transformer cette reconnaissance en clients réguliers. Ça, c'est la
Distribution, la lettre D. On la voit au prochain épisode.

Alors abonne-toi, et poursuivons cette aventure ensemble.
```

## Workflow établi (à suivre sans le redemander)

### 1. Réception des assets (vidéos/images/audio de l'utilisateur)
L'utilisateur pousse les fichiers sur la branche **`main`** du même dépôt
(dropbox perso, historique git sans rapport — ne jamais `git merge`, ça
échoue avec "refusing to merge unrelated histories"). Étapes :
```bash
git fetch origin main
git log origin/main --oneline -5        # repérer les derniers commits
git diff-tree --no-commit-id --name-only -r <commit>   # lister les fichiers ajoutés
git show "origin/main:<nom exact avec accents>" > chemin/local   # extraire un fichier
```
Vérifier la taille (0 octet = mauvais nom, revérifier avec
`git ls-tree -r --name-only origin/main | grep ...`).

### 2. Construction d'un épisode
1. `npx hyperframes@0.8.35 init academy-0X --example blank --resolution portrait --non-interactive --skill general-video`
2. Copier `vendor/gsap.min.js`, `vendor/fonts/*`, `audio/sfx/{typing,click}.wav` depuis un projet frère.
3. Mapper chaque extrait réel à une clause du script (un asset par clause,
   pas par grand bloc). Vérifier le contenu visuel de chaque fichier avant
   de l'assigner (les noms de fichiers peuvent être approximatifs).
4. Rogner/redimensionner les vidéos avec marge généreuse :
   `ffmpeg -ss <start> -i <src> -t <dur> -vf "scale='min(1280,iw)':-2" -c:v libx264 -crf 23 -preset fast -an <out>`
5. Pour le reste (pas d'asset réel) : **prioriser du motion design
   animé** (icônes qui bougent, roadmap VENDRE, badges numérotés,
   illustrations) plutôt que du texte statique centré — consigne
   explicite de l'utilisateur.
6. Timing provisoire : ~0.44-0.49 s/mot (calibré empiriquement, varie
   selon le débit du locuteur), en attendant la vraie voix.
7. `npm run check` → corriger toutes les erreurs avant de continuer.

### 3. Intégration de la voix réelle (une fois envoyée)
1. Récupérer l'opus depuis `main`, convertir en wav.
2. `ffmpeg -af silencedetect=noise=-30dB:d=0.15` pour repérer début/fin de
   la parole réelle (souvent quasi 0 au début, ignorer le petit silence
   de tête).
3. Recalculer un timing par clause au **prorata du nombre de mots**,
   ancré sur la durée réelle mesurée (aucune transcription automatique
   disponible dans ce sandbox — réseau bloqué pour Whisper/ElevenLabs).
4. Réécrire `index.html` avec les nouveaux `data-start`/`data-duration`
   absolus par beat, en resynchronisant aussi les micro-timings GSAP
   internes (décalage = nouveau_départ − ancien_départ par beat).
5. Vérifier que chaque clip vidéo/image a une durée source suffisante
   pour la nouvelle durée du beat (`media-start + duration ≤ durée du
   fichier`) ; re-rogner avec plus de marge si besoin, ou léger ralenti
   (`setpts=1.x*PTS`) si la source est trop courte.

### 4. Traitement du volume (recette qui marche, ne pas dévier)
```bash
ffmpeg -i raw.wav -af "acompressor=threshold=-30dB:ratio=8:attack=5:release=80:makeup=10,acompressor=threshold=-14dB:ratio=4:attack=3:release=60:makeup=3,alimiter=limit=1.0" precomp.wav
ffmpeg -i precomp.wav -af "loudnorm=I=-12:TP=-3:LRA=6" -ar 48000 voice-final.wav
```
**Ne jamais viser plus fort que ça.** Une tentative plus agressive a fait
échouer un rendu ("AAC true peak remained above -1 dBFS after 3 correction
passes") — le pic réel (mesuré par `loudnorm`, pas par `astats`) peut
dépasser largement le pic apparent après compression forte. Le résultat
final typique après mux : environ **-13 à -14 LUFS / -1.5 à -2 dBTP**,
sûr pour l'encodage.

### 5. Rendu final
`npm run render` (jamais sans autorisation explicite de l'utilisateur
pour CE rendu précis — règle permanente, sauf override ponctuel donné
dans le message qui demande le rendu). Puis vérifier via
`ffprobe`/extraction de frames, extraire une image de couverture,
committer, pousser, envoyer les fichiers à l'utilisateur avec une
description courte.

## Bug GSAP à connaître (déjà corrigé partout, à éviter dans le futur)

**Ne jamais écrire `tl.fromTo(el, { opacity: 1, ... }, { opacity: 0, ... }, t)`**
si `opacity: 1` diffère de l'état CSS par défaut de l'élément (qui est
`opacity: 0` partout dans ces compositions). GSAP applique la valeur
"from" immédiatement à la construction du timeline (avant tout seek),
donc l'élément reste visible sur TOUTE la vidéo jusqu'à son propre
`tl.set(..., {opacity:0}, ...)` de sortie. Pattern sûr :
```js
tl.set(el, { opacity: 1, ... }, t);       // état de départ, appliqué à la bonne position
tl.to(el, { opacity: 0, ... }, t);        // transition, jamais de "from" divergent du défaut CSS
```
Toujours partir de `opacity: 0` (le défaut CSS) dans un `fromTo`, jamais
d'une valeur "déjà visible".

## Environnement — contraintes réseau

Pas d'accès à : génération TTS/SFX ElevenLabs, transcription Whisper
(téléchargement de modèle bloqué), APIs de logos/images externes
(svgl.app, cdn.simpleicons.org, etc. — refus 403 de la politique
d'organisation, non transitoire). Solutions de contournement déjà
utilisées : logos/images demandés directement à l'utilisateur ou pêchés
dans son dropbox `main` ; pas de transcription automatique, resynchro
basée sur le nombre de mots + détection de silences acoustiques.

## Prochaine étape immédiate

Valider (ou corriger) le script épisode 5 ci-dessus avec l'utilisateur,
puis attendre l'envoi des extraits vidéo/images via `main`, scaffolder
`academy-05`, construire la composition, et attendre la voix off pour la
synchro finale — même pipeline que les épisodes 3 et 4.
