---
workflow: general-video
flow: companion
storyboard: yes
message: "Ta compétence, même sans diplôme, peut devenir un produit digital que tu vends."
destination: instagram-reels
aspect: 1080x1920
language: fr
length: 58s
audience: "Jeunes francophones (RDC/Afrique) sans emploi ou sous-payés, cible d'une pub Meta clic-vers-WhatsApp"
narration: yes
---

## Intent

Publicité Meta (clic-vers-WhatsApp) pour DigitalMikaelson, qui vend l'ebook
"Gagne ta vie sans diplôme". Ton encourageant, jamais moralisateur : on
reconnaît la situation du spectateur en une phrase, puis on bascule vers la
possibilité. Un vrai pivot émotionnel à mi-parcours (de "le problème" à "tout
a changé"). Se termine sur le CTA "Envoyer un message" WhatsApp, sans jamais
mentionner de prix.

## Voix off (verbatim — VO_MODE, ne pas reformuler)

"Que vous soyez salarié, étudiant, ou sans emploi, vous avez tous une chose
en commun : vous êtes détenteurs d'un savoir-faire qu'on appelle une
compétence, dans des domaines comme la cuisine, la couture, les langues, ou
la comptabilité. Mais le problème, c'est qu'une compétence, ce n'est pas un
savoir qu'on garde pour soi. C'est un savoir qu'on partage, et qu'on
monétise. Quelqu'un à l'autre bout du monde pourrait avoir besoin de ce que
vous savez faire. Jusqu'à présent, le problème, c'était la distance. Mais
avec l'arrivée des produits digitaux, tout ça a changé. Vous pouvez
connaître une langue, et l'enseigner à quelqu'un à des milliers de
kilomètres, sans jamais le rencontrer. J'ai écrit un guide simple, étape par
étape, pour transformer ce que vous savez déjà faire en produit digital, et
le vendre. Pas de blabla : juste ce qu'il faut faire, concrètement. Cliquez
sur 'Envoyer un message', et écrivez-moi sur WhatsApp maintenant."

## Découpage validé (14 plans, timecodes indicatifs sur 58s)

1. 0:00–0:03 — Fond dégradé navy plein cadre (identité couverture ebook), léger zoom continu. Pastille "DIGITALMIKAELSON".
2. 0:03–0:06 — 3 cartes en cascade : salarié / étudiant / sans emploi (photos IA déjà générées, voir Assets).
3. 0:06–0:09 — Fusion en "UNE COMPÉTENCE." (texte jaune, gros).
4. 0:09–0:14 — Montage 4 domaines : cuisine / couture / langues / comptabilité (photos, voir Assets).
5. 0:14–0:20 — Retour fond navy, vignette plus sombre, "MAIS...".
6. 0:20–0:23 — Cadenas qui s'ouvre, texte "ON PARTAGE. ON MONÉTISE." mot par mot.
7. 0:23–0:28 — Carte réseau/distance (`ch1_reseau.jpg`), zoom lent.
8. 0:28–0:31 — "LE PROBLÈME : LA DISTANCE."
9. 0:31–0:35 — Pivot : flash blanc bref, "TOUT A CHANGÉ." (scale-up rapide).
10. 0:35–0:41 — Morph/cross-fade langue (`ebook_anglais.jpg`) → connexion mondiale (`ch1_reseau.jpg`), ligne animée mini-globe.
11. 0:41–0:44 — Reveal de la couverture réelle de l'ebook, chute avec léger rebond.
12. 0:44–0:49 — Bandeau qui glisse : "COMPÉTENCE → PRODUIT DIGITAL → VENTE".
13. 0:49–0:52 — Signature de marque : "PAS DE BLABLA." puis "JUSTE CE QU'IL FAUT FAIRE."
14. 0:52–0:58 — CTA final : bande noire slide-up (identité couverture ebook), icône WhatsApp réelle, numéro, bouton "ENVOYER UN MESSAGE" qui pulse.

## Assets

Répertoire source (lecture seule, à copier dans le projet avant usage) :
`/tmp/claude-0/-home-user-Mike1272-Bus/d253aa54-2766-50cc-8e30-b570e99679f0/scratchpad/`

- `icons/` → couverture de l'ebook (page 0 du PDF rendu / `cover_thumb`), `ch1_reseau.jpg`, `ebook_anglais.jpg`, `logo_card.png` — vrais visuels déjà utilisés dans l'ebook, brand-consistants.
- `cover/wa_icon_clean.png` — vraie icône WhatsApp déjà utilisée sur la couverture de l'ebook et en pub CTA.
- 4 photos générées (Canva `generate-image`, déjà validées par l'utilisateur) pour les plans 2 et 4 :
  - salarié (media MAHWN2srx-A)
  - étudiante (media MAHWN_3rjrk)
  - personne sans emploi, traitement digne, non dramatisé (media MAHWNzX5SVs)
  - comptabilité, calculatrice + cahier (media MAHWN6IRocA)
  - Ces 4 doivent être téléchargées depuis Canva et placées dans `public/` avant le build (pas encore de fichiers locaux).

## Customizations

- Fond et palette : reprendre exactement l'identité de la couverture de
  l'ebook — dégradé diagonal NAVY (#211E5C), accents JAUNE (#F7C72A) et CYAN
  (#7EDEE8), bande CTA finale noire avec la même disposition
  icône-WhatsApp + numéro que la couverture.
- Typographie : Bricolage Grotesque Bold pour les titres/texte à l'écran,
  WorkSans pour le texte secondaire (mêmes polices que l'ebook).
- CTA final : bouton "ENVOYER UN MESSAGE" façon bouton Meta clic-vers-WhatsApp, en pulsation légère continue.
- Musique : instrumentale, climat sourd/posé jusqu'au flash du plan 9, puis plus enjouée jusqu'à la fin. Pas de titre de morceau précis imposé.
- SFX : whoosh sur les transitions de cartes, flash caméra au plan 9, notification WhatsApp discrète au CTA final.

## Notes

- Numéro WhatsApp réel : +243 831 710 181. Ne jamais afficher de prix (règle de marque).
- Ne jamais inventer de statistique, de témoignage, ou de date limite non fournie par l'utilisateur.
- Registre "vous" tout du long (déjà dans le script) — ne pas glisser vers "tu".
- Signature de marque à respecter au mot : "Pas de blabla, juste ce qu'il faut faire, concrètement."
