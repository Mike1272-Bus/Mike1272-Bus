# Vidéos du guide « Gagne ta vie sans diplôme »

6 vidéos en motion design (16:9, fond blanc, sans voix pour l'instant), une par étape du guide, et le PDF « Guide vidéo » qui les contient.

- `finales/v0.mp4` à `v5.mp4` : les vidéos à envoyer ou à mettre sur YouTube.
- `pdf/pages_video_du_guide.pdf` : les pages vidéo du guide, dans la DA du guide (9 pages, à insérer au début de chaque chapitre du guide). Les 6 vidéos sont **dans** le PDF : toucher l'image d'une vidéo l'ouvre avec Adobe Acrobat (téléphone ou ordinateur). Dans d'autres applications PDF, les vidéos sont dans la liste des pièces jointes.
- `build.py` : décrit les scènes de chaque vidéo. `python3 build.py` refait les compositions, puis dans `vN/` : `npx --yes hyperframes@0.8.77 render -o renders/vN.mp4`.
- `pdf/build_pdf.py` : refait le PDF.

## Passer aux liens YouTube (conseillé)
1. Mets chaque vidéo de `finales/` sur YouTube en « non répertoriée ».
2. Dans `pdf/liens.json`, remplace `fichier:pdf/videos/vN.mp4` par le lien YouTube de la vidéo.
3. `python3 pdf/build_pdf.py` : l'image devient un lien normal, qui marche dans toutes les applications, et le PDF redevient léger.

## Quand Mike enverra ses voix
Un audio par vidéo (script dans `../scripts_videos_ebook.md`). On recale la durée de chaque scène sur sa voix dans `build.py`, puis on refait le rendu.
