---
name: allegra-contenu
description: Crée les publications du jour d'Allegra Digital Ground (agence de vidéos animées pour les commerces de Kinshasa) pour Instagram, Facebook, TikTok et le statut WhatsApp. À utiliser quand Mike demande « le contenu Allegra du jour », « les vidéos Allegra de demain », « prépare les posts Allegra », ou quand la tâche programmée du matin se lance. Produit 2 publications par jour (13 h et 19 h) : idée, script, texte à l'écran, légende et, si possible, la vidéo rendue. Après le « valide » de Mike, les programme sur Instagram, Facebook et TikTok via Buffer. À utiliser aussi quand Mike écrit « valide », « valide 13 h », « publie » ou « programme les posts Allegra ». Ne publie jamais sans son accord.
---

# Contenu Allegra : les 2 publications du jour

Tu fabriques le contenu organique d'**Allegra Digital Ground** : des vidéos courtes qui montrent aux commerçants de Kinshasa ce que nous faisons, pour qu'ils nous écrivent sur WhatsApp. Tu prépares tout ; **Mike relit et valide**. Après son « valide », tu programmes les posts sur Instagram, Facebook et TikTok (via Buffer). Le statut WhatsApp, c'est lui qui le poste.

Lis d'abord, dans cet ordre :
1. `references/regles_et_da.md` : les règles (non négociables) et la direction artistique.
2. `references/calendrier_type.md` : quel type de publication à quelle heure, selon le jour.
3. `references/sujets.md` : la réserve d'idées par secteur.
4. `references/modele_sortie.md` : où et comment ranger ce que tu produis.
5. `references/publication_buffer.md` : comment programmer les posts validés.
6. Le fichier `suivi.md` (dans le dossier `cowork-allegra/`) : ce qui a déjà été fait, pour ne pas se répéter, et les chiffres notés par Mike.

## Le dossier de travail

Le dossier partagé avec Cowork est le dépôt **Mike1272-Bus** (copie sur l'ordinateur de Mike). Chemins utiles, depuis la racine du dépôt :
- Modèles de vidéos (HyperFrames, D.A. claire) : `prospection/contenu-allegra/mer14-transformations/` (avant → après), `prospection/contenu-allegra/mar13-essai/` (offre), `prospection/contenu-allegra/mer14-demo-pizza/` (démo d'une photo).
- Logo et marque : `prospection/contenu-allegra/marque/` ; icônes 3D : `prospection/contenu-allegra/_icons/`.
- Clips libres de droits déjà triés (sans visages) : `prospection/contenu-allegra/stock/raw/`, crédits dans `stock/credits.txt`.
- Musique et bruitages : `video-excel-13h/assets/audio/musique.wav`, `video-excel-13h/assets/sfx/`.
- Ce que tu produis : `cowork-allegra/publications/AAAA-MM-JJ/`.

## La marche à suivre

1. **Date et créneaux.** Prends la date du jour (ou celle demandée). Regarde dans `calendrier_type.md` les 2 types à faire (13 h et 19 h).
2. **Choisir les sujets.** Prends dans `sujets.md` un sujet de chaque type, dans un **secteur différent** de ceux des 3 derniers jours (regarde `suivi.md`). Vérifie qu'un clip de `stock/raw/` existe pour ce secteur ; sinon, choisis un autre secteur. N'invente jamais un client.
3. **Écrire chaque publication** selon `modele_sortie.md` : accroche (2 secondes, dite par la voix), scènes avec le texte à l'écran, fin avec le mot-clé et le numéro, puis la légende Facebook/TikTok et le texte court du statut WhatsApp.
4. **Fabriquer la vidéo (si l'ordinateur le permet).** Copie le modèle qui correspond au type dans `cowork-allegra/publications/AAAA-MM-JJ/<heure>-<sujet>/` (sans `renders/` ni `node_modules/`), puis :
   - **La photo « avant »** : tire-la du clip choisi (`ffmpeg -ss 1 -i stock/raw/<clip>.mp4 -frames:v 1 assets/img/<produit>_photo.jpg`). L'« après » est fait avec cette même photo.
   - **Les textes et l'accent** dans `index.html` : remplace ceux du modèle, garde la D.A. claire.
   - **Les chemins de `mix.py`** : le modèle remonte de 3 dossiers pour trouver `video-excel-13h/`. Depuis `cowork-allegra/publications/AAAA-MM-JJ/<heure>-<sujet>/`, il faut en remonter 4 : corrige `SFX_DIR` et `MUSIC` (`"..", "..", "..", ".."`). Recale aussi la liste `SFX` et `DUR` sur les nouvelles scènes.
   - **La voix de l'accroche** (`assets/audio/voix-hook.wav`) : celle du modèle ne dit pas la nouvelle phrase. Si Mike a déposé un enregistrement de l'accroche dans le dossier, utilise-le. Sinon, enlève la voix de `mix.py`, garde l'accroche en texte à l'écran, et écris dans le résumé : « Enregistre l'accroche (2 s) au téléphone si tu veux la voix. »
   Ensuite :
   - `python3 mix.py`
   - `npx --yes hyperframes@0.8.77 lint`
   - `npx --yes hyperframes@0.8.77 render . -q high -o renders/raw.mp4`
   - `ffmpeg -i renders/raw.mp4 -c:v libx264 -crf 23 -preset slow -pix_fmt yuv420p -c:a aac -b:a 128k -movflags +faststart renders/<nom>.mp4`, puis supprime `raw.mp4`.
   Regarde 4 ou 5 images de la vidéo (ffmpeg) avant de dire qu'elle est prête : texte lisible, rien qui déborde, pas de visage.
   **Si une de ces commandes ne marche pas** (Node, ffmpeg ou internet absents), ne force pas : laisse le dossier de la vidéo prêt, écris dans `A_RENDRE.md` ce qui manque, et dis-le à Mike. Il fera le rendu avec Claude Code.
5. **Mettre à jour `suivi.md`** : une ligne par publication (date, heure, type, secteur, sujet, mot-clé, statut « à valider »).
6. **Résumé pour Mike** (court, en « tu », avec un emoji d'encouragement) : les 2 sujets, où sont les fichiers, ce qui reste à faire, la phrase à répondre pour lancer la programmation (« Valide 13 h et 19 h »), et la question du soir : « Combien de vues et de messages (VIDÉO / ESSAI) pour les posts d'hier ? ».

## Quand Mike valide

Mike répond « Valide 13 h et 19 h » (ou demande des corrections). Passe les posts validés en « validé » dans `suivi.md`, puis suis `references/publication_buffer.md` : vidéo sur Google Drive, post Buffer pour Instagram, Facebook et TikTok à l'heure prévue, statut « programmé ». Rien n'est envoyé sans ce « valide ».

## Le soir (si Mike donne ses chiffres)

Note-les dans `suivi.md`. Chaque lundi, fais le bilan de la semaine : quel type et quel secteur ramènent le plus de **messages** (pas de vues). Propose de faire plus de ce qui marche et d'arrêter ce qui ne ramène rien (règle Hormozi : garder, arrêter, doubler).

## Les interdits (rappel)

Aucun chiffre, résultat, prix ou témoignage inventé. Aucune vidéo ou photo d'une entreprise sans son accord écrit (confirmé par Mike). Aucune personne ni visage dans les images. Pas de Pinterest. Registre « vous » dans tout le contenu Allegra. Rien n'est programmé ni publié sans le « valide » de Mike.
