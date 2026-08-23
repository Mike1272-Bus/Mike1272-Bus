---
workflow: general-video
flow: automation
storyboard: no
message: "Recap de la semaine (confiance, livraison, marque, boutique, erreurs) qui debouche sur Le Kit Entreprise Serieuse, lance samedi."
destination: tiktok
aspect: 1080x1920
language: fr
audience: "petits commercants qui vendent en ligne (RDC/Kinshasa)"
angle: "recap de la semaine + transformation, ton direct, deuxieme personne (tu) - contenu 'dimanche' du calendrier hebdo ADG"
---

## Intent

Dixieme video de la serie (nouveau cycle hebdo, apres un retour au format carrousel pour lundi-samedi cette semaine-la). Contenu "dimanche": recap rapide des 6 themes de la semaine (confiance/lundi, livraison/mardi, marque/mercredi, boutique en ligne/jeudi, erreurs qui coutent des ventes/vendredi, lancement du Kit/samedi), puis explication concrete du Kit Entreprise Serieuse (guide + systeme de gestion de la relation client) et de la transformation qu'il apporte. CTA final: ecrire "KIT" en message.

Structure standard imposee par l'utilisateur pour tous les scripts futurs: accroche -> CTA d'abonnement (juste apres l'accroche) -> corps -> CTA mot-cle (a la toute fin).

## Assets

51 images recues via GitHub, nommees phrase par phrase (tres bon nommage, meme convention que les videos 16/17). Placement mot-a-mot par correspondance de phrases sur les timestamps de `audio/lines/NN.words.json`.

QA effectuee avant placement:
- 1 image exclue: "Et un systeme de gestion de la relation client deja pret" originale montrait un template Google Sheets de suivi financier personnel, en RUSSE (langue et contenu hors-sujet) -> remplacee par une carte texte generee maison (meme esthetique blockframe que les CTA des carrousels precedents).
- Reste (50 images) verifie sans filigrane ni marque tierce identifiable (metadonnees EXIF + relecture visuelle en planche contact).

## Customizations

- Sous-titres/captions obligatoires.
- Voix-off: Kokoro `ff_siwis` (seule voix francaise locale disponible dans cet environnement; pas d'acces ElevenLabs ici, confirme par l'utilisateur).
- Meme systeme de marque (preset blockframe) que les videos precedentes.
- Ton direct, deuxieme personne ("tu"), jamais "je".
- Logo officiel ADG (`Logo ADG.png` du repo) integre dans la composition (marque de fin / watermark coin).
- CTA final: "Ecris 'KIT' en message si tu veux rattraper ce que tu as manque cette semaine."
- Pas de mention de l'IA.

## Notes

- Script redige et valide par l'utilisateur (accroche, CTA abonnement, recap des 6 jours, transformation detaillee sur le Kit passee au skill /humanizer, CTA mot-cle).
