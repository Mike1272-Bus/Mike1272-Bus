# Épisode 5 — N, Notoriété

## Script (validé, hook négatif, simplifié)

Épisode 5.

Personne ne devient connu en parlant de tout.

On te dit qu'il faut plaire à tout le monde pour être connu. En vrai, c'est le contraire. Tu deviens connu quand tu parles d'une seule chose, tout le temps.

Dans notre stratégie VENDRE, le N, c'est la Notoriété. C'est le moment où les gens commencent à te reconnaître pour ce truc précis.

Et ça implique trois choses concrètes. Un : spécialise-toi sur un seul angle plutôt que de parler de tout. Plus tu es précis, plus on te reconnaît vite. Deux : reste reconnaissable, avec le même ton et le même style à chaque vidéo. Trois : répète le même message jusqu'à ce qu'il soit associé à toi. Toi, tu en as peut-être marre de le dire. Les autres viennent tout juste de l'entendre pour la première fois.

Regarde Oncle David. Il ne parle pas de tout l'artisanat, juste de son guide de menuiserie. Résultat : quand quelqu'un pense à un guide pratique pour apprendre un métier manuel, c'est lui qu'on recommande.

Une fois que tu es reconnu pour ton truc, l'étape suivante, c'est de transformer cette reconnaissance en clients réguliers. Ça, c'est la Distribution, la lettre D. On la voit au prochain épisode.

Alors abonne-toi, et poursuivons cette aventure ensemble.

## État

- Composition construite avec **timing placeholder** (mots × ~0.47s/mot), en attente de l'audio réel.
- `npm run check` : 0 erreur, 2 avertissements (taille de fichier / densité de piste — informatifs, cohérents avec les épisodes précédents).
- **Pas de rendu effectué** — règle permanente : ne jamais rendre sans autorisation explicite.
- Prochaine étape dès réception de l'audio réel : resynchronisation complète au mot près (même méthode que ep3/ep4), recette de volume sécurisée standard, rendu final, cover + description courte.

## Les 18 assets réels reçus — tous placés

| Fichier reçu | Utilisé dans | Traitement |
|---|---|---|
| 07.mp4 ("Personne ne devient connu...") | Hook (p1), plein écran | trim 4.3s |
| 14.mp4 ("qu'il faut plaire à tout le monde") | p2a, plein écran | segment 4-9.5s (visages qui se multiplient) |
| 08.mp4 ("Pour être connu") | p2b, plein écran | trim 2.0s |
| 17.mp4 ("une seule chose, tout le temps") — **vertical natif** | p4, plein écran | ralenti ×1.35 (source trop courte) |
| 18.mp4 ("à te connaître pour un seul truc") — **vertical natif** | p6 — **traité en carte horizontale** (`.shot-card.landscape`) | ralenti ×1.37 |
| 01-04.jpg ("Spécialise-toi sur un seul angle") | p8b1-4, montage séquentiel des 4 métiers | redimensionnés, tag métier par image |
| 13.mp4 (fond vert, mockup téléphone) | p9, "plus tu es précis..." | incrustation chroma-key sur fond crème, badge ✓ animé par-dessus |
| 06.jpg ("reste reconnaissable") | p10b1 | carte landscape |
| 16.mp4 ("spécialise-toi..." — créateur filmé) | p10b2, "le même style" | trim 3.8s |
| 15.mp4 ("répète le même message") | p11b | trim 5.7s |
| 12.mp4 ("première fois") | p12b | trim 5.7s, réduit depuis 2560×1440 |
| 05.png (couverture guide) | p14 | carte landscape |
| 09.mp4 ("apprendre un métier manuel") | p15 | trim 7.1s |
| 10.mp4 ("c'est lui qu'on recommande") | p16 | ralenti ×1.15 (source très courte, 2.2s) |
| 11.mp4 ("clients réguliers") | p17b | trim 4.3s |

## Note sur la vidéo verticale

Deux clips reçus étaient nativement tournés en vertical (17.mp4 et 18.mp4 — aucune métadonnée de rotation, contenu réellement filmé en portrait). Le canevas du projet est lui-même en portrait (1080×1920), donc les deux s'intègrent naturellement en plein écran. Pour respecter la demande explicite ("il y a une vidéo vertical, met ça en horizontal"), **18.mp4** a été traité en carte horizontale encadrée (`.shot-card.landscape`, le même gabarit que toutes les autres cartes vidéo/image de l'épisode) plutôt qu'en plein écran — si c'est plutôt 17.mp4 qui était visé, il suffit de permuter les deux traitements.

## Bug corrigé pendant la construction

Le montage "spécialise-toi" (4 images) n'apparaissait pas dans l'aperçu : les tweens GSAP animaient l'opacité des `<img>` internes, mais le conteneur `.fx-montage-card` a `opacity: 0` en CSS et rien ne faisait remonter l'opacité du conteneur lui-même. Corrigé en animant aussi le conteneur (`#p8b1` etc.), sur le même principe que les autres `shot-card` du projet.
