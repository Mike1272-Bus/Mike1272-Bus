# Landing page Allegra Digital Ground (v3, 13 oct. 2026)

En ligne : https://allegra-digital-ground.vercel.app (projet Vercel `allegra-digital-ground`, dossier publié : `site/`).

Inspirée de la structure de dupliq.me (style « néo-brutal » clair : bordures noires, ombres décalées, bulles, fond quadrillé), adaptée à Allegra : vidéos, avant/après, motion design, montage.

- `site/` : la page (HTML statique, aucune compilation). Les sections : accueil (éventail photos → vidéos), avant/après, la formule (produit, portrait, montage), 9 formats vidéo, « pas que des burgers », vitrine avec le son, galerie, ce que vous recevez, l'offre (vidéo d'essai gratuite), FAQ, dernier appel.
- `build_media.py` : fabrique `site/media/` (boucles courtes, photos « avant », images de la galerie) à partir des vidéos Allegra et des vidéos de Mike. Relancer après avoir ajouté une vidéo.
- `sources/presentation.mp4` : l'ancienne vidéo explicative (utilisée pour la carte « Vidéo explicative »).
- `video/` : la vidéo de présentation de la v1 (HyperFrames).

Règles : aucun chiffre, prix ou témoignage inventé (la section « résultats » montre ce que le client reçoit, pas des statistiques). Les exemples produits sont faits avec des images libres de droits (mention sur la page). Aucune vidéo de client sans son accord écrit. Le portrait et le montage sont des vidéos de Mike.

À compléter par Mike : des vidéos de vrais clients (avec accord écrit) et leurs résultats réels, les liens Instagram / TikTok d'Allegra.

## Vidéo de présentation Instagram (15 oct.)

`video-instagram/` : Reel de 32,6 s (1080×1920) qui présente Allegra en suivant le site : accroche, « Nous, c'est Allegra.digital », photos → vidéos, avant/après, la formule, 9 formats, l'offre d'essai, appel WhatsApp. Rendu : `video-instagram/renders/allegra_presentation_instagram.mp4`, légende : `video-instagram/legende.md`. Pour refaire : `python3 clips.py && python3 mix.py && npx --yes hyperframes@0.8.77 render . -q high -o renders/raw.mp4`.
