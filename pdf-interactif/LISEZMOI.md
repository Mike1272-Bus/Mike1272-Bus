# PDF interactif : des liens vers tes vidéos, ta communauté, WhatsApp

`feuille_de_route_modele.pdf` est un modèle de 5 pages :
- la couverture, avec un bouton « Commencer » qui saute au sommaire ;
- un sommaire où chaque ligne ouvre sa page ;
- des pages d'étape avec une image de vidéo cliquable, un exercice, et des boutons WhatsApp et communauté ;
- une dernière page avec le lien vers l'ebook.

En bas de chaque page, « Sommaire » ramène au début.

## Changer les liens
1. Ouvre `liens.json` et remplace les adresses `https://VOTRE-LIEN-...` par les tiennes :
   - ta vidéo YouTube (en « non répertoriée » si tu veux qu'elle ne soit visible que par tes lecteurs) ;
   - le lien de ta communauté Skool (ou ton groupe WhatsApp) ;
   - ta page Chariow.
2. Lance `python3 build.py` : le PDF est refait avec les nouveaux liens.
3. Pour changer la miniature d'une vidéo, remplace `miniature_video1.jpg` (format 16:9).

## La même chose dans Canva (sans code)
1. Sélectionne une image ou un bouton, puis clique sur l'icône de lien (ou Ctrl+K) et colle l'adresse.
2. Pour un lien vers une autre page du même document, choisis la page dans la liste au lieu de coller une adresse.
3. Exporte en « PDF standard » : les liens restent cliquables.

## À tester avant d'envoyer
- Ouvre le PDF sur ton téléphone avec une application de lecture PDF : dans l'aperçu de WhatsApp, les liens ne marchent pas toujours.
- Touche chaque bouton une fois pour vérifier qu'il ouvre la bonne page.
