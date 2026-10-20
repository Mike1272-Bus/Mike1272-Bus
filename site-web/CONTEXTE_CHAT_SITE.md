# Pôle « Site web » : contexte du chat (landing pages et sites)

Ce chat sert **uniquement** à créer des landing pages et des sites internet. Lis d'abord `CLAUDE.md`, puis ce fichier. Ne relis pas tout le dépôt.

## Ce qui existe déjà
- **Landing Allegra v3** : en ligne sur https://allegra-digital-ground.vercel.app. Le code est dans `allegra-landing/site/` (HTML statique) et les explications dans `allegra-landing/LISEZMOI.md`. Le style est néo-brutal clair, inspiré de dupliq.me.
- Les textes des services Chariow sont dans `page-chariow/`.
- Les éléments de marque sont dans `projet-claude/contexte_projet.md` et `branding/`. Logos : `Logo ADG.png`, `logo allegra.jfif`.

## Méthode (bon résultat, peu de tokens)
1. **Une référence de DA** : Mike donne 1 à 3 sites qu'il aime (lien + 2 à 4 captures : ordinateur et téléphone). On ne copie pas le site. On reprend sa **direction artistique** : couleurs, polices, espacements, rythme des sections, style des boutons et des cartes. On ne reprend jamais ses textes, ses logos ni ses images.
2. **`DESIGN.md`** dans le dossier du projet : la DA traduite en règles. Ce fichier sert de référence pour tout le reste :
   - palette (5 à 7 couleurs) ;
   - 2 polices Google Fonts maximum ;
   - tailles de texte, arrondis, ombres, espacements ;
   - plan des sections.
3. **Textes d'abord** (`textes.md`), avec le skill `copywriting` : « vous » pour Allegra, « tu » pour DigitalMikaelson. Aucun chiffre, prix ni témoignage inventé.
4. **Page en HTML + CSS statique**, un seul fichier `index.html` avec les variables CSS de `DESIGN.md`. Pas de framework : moins de code, moins de tokens, rapide sur les connexions RDC. On ne passe à Next.js (skill `web-project-scaffold`) que pour une vraie boutique avec paiement Mobile Money.
5. **Vérification** : une capture téléphone et une capture ordinateur, seulement à la fin.
6. **Mise en ligne** gratuite sur Vercel, comme la landing Allegra.

## Règles anti « site IA moche »
- Pas de dégradés violet-bleu, ni d'emojis en guise d'icônes, ni de « glassmorphism » partout.
- Une seule couleur d'accent, beaucoup d'espace blanc et une vraie hiérarchie des titres.
- Les vraies photos et vidéos des clients ou de Mike. **Aucune illustration de personnes.**
- Le téléphone d'abord : la majorité des visiteurs viennent de WhatsApp, TikTok ou Facebook.
- Un seul appel à l'action principal : le bouton WhatsApp **+243 831 710 181**, avec un message pré-rempli.
- **Secret professionnel** : ne jamais dire comment on fabrique les vidéos (IA, banques d'images, outils).

## Skills
Mike va fournir des skills de design. Range chacun dans `.claude/skills/<nom>/SKILL.md`. Un skill = un dossier. Note-le ici une fois installé.

| Skill | Rôle | Installé |
|---|---|---|
| `copywriting` | Textes de marque | oui |
| `web-project-scaffold` | Site React ou boutique (si besoin) | oui (intégré) |
| `emil-design-eng` | Finitions UI, détails qui font « pro » | oui |
| `animate`, `review-animations`, `animation-performance` | Animations web propres et légères | oui |
| `mobile-native` | Rendu « appli » sur téléphone | oui |
| `break-ui`, `prototype`, `find-animation-opportunities`, `improve-animations`, `animation-vocabulary`, `apple-design`, `pick-ui-library` | Tests, variantes, audit | oui |
| `animate-expo`, `write-swift`, `ask-sonner` | Pack Emil Kowalski, peu utiles ici (apps mobiles, React) | oui |
| `impeccable` (pbakaus) | Direction artistique, critique, audit et finition des pages (anti « site IA ») | oui |
| *(à venir)* | DA / design | |

## Organisation
- Chaque nouveau site a son dossier : `site-web/<nom-du-projet>/`, qui contient `DESIGN.md`, `textes.md`, `index.html` et `images/`. La landing Allegra reste dans `allegra-landing/`.
- Branche `claude/gallant-goldberg-l20gu3` : `git pull` avant de commencer et avant chaque push. Commits en français. Ne touche qu'à `site-web/`, `allegra-landing/` et à la section « Site web » du tableau de bord.
