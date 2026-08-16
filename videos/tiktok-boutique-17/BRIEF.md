# Vidéo 17 — Dimanche — Récap de la semaine / transformation

message: "Comment vous allez passer d'un simple vendeur qui poste des photos sur WhatsApp, TikTok ou Instagram, à une entreprise qu'on prend au sérieux."
angle: présentation agence + récap de la semaine + transformation, registre "vous" (comme le script fourni)
CTA: guide gratuit + mini CRM en commentaire

## Audio
Pas de voix réelle envoyée pour cette vidéo. Aucun outil de clonage vocal n'est connecté dans cet environnement (ni HeyGen ni ElevenLabs configurés) — généré avec la seule voix française locale disponible : Kokoro `ff_siwis` (voix féminine). Ne correspond pas à la vraie voix utilisée sur les vidéos précédentes ; à remplacer par un enregistrement réel si besoin.
Généré ligne par ligne (6 lignes), concaténé avec 0.35s de silence entre chaque, durée totale 83.76s.

## Images
41 images reçues via GitHub, nommées phrase par phrase.
- Toutes placées selon le texte, sauf 2 phrases manquantes → remplacées par 2 illustrations maison : "Instagram" (ligne 1) et "garde une trace de chaque client / fil WhatsApp" (fin ligne 5)
- 1 image remplacée : la capture d'écran CRM portait le branding d'un outil tiers ("SanTMS") → remplacée par une illustration maison neutre
- 40 images réelles + 3 générées = 43 assets, placement mot-à-mot via matching de phrases sur words.json

## Révision — prononciation + images réelles

### Prononciation (TTS Kokoro)
Le moteur TTS lisait "WhatsApp" et "Allegra Digital Ground" en bascule anglais au milieu de la phrase française (espeak détecte ces mots comme anglais et change d'accent), ce qui donnait un rendu déformé. Corrigé en réécrivant ces mots phonétiquement dans le texte envoyé au TTS uniquement (sous-titres et texte affiché restent inchangés, orthographe correcte) :
- "WhatsApp" → "Ouwatsap" (lignes 1, 3, 5)
- "Allegra Digital Ground" → "Alegra Dijital Graoünd" (ligne 2)

Lignes 1, 2, 3, 5 régénérées avec Kokoro `ff_siwis`, durées et timing (voix + sous-titres + placement d'images) recalculés en cascade. Durée totale : 82.582s (avant : 83.76s).

### Images réelles (remplacement des illustrations maison)
3 des 4 images envoyées par l'utilisateur ont remplacé des illustrations générées :
- `s1-2.png` ("simple vendeur") → photo réelle (commerçant au téléphone/tablette)
- `s5-4.png` ("vous avez besoin d'un vrai système de gestion de la relation client") → photo réelle (interface de segmentation de contacts)
- `s5-7.png` ("et qui garde une trace de chaque client") → illustration neutre fournie (icônes CRM, sans marque)

La 4e image envoyée ("de gestion de la relation client.jpeg") n'a **pas** été utilisée : c'est une capture d'écran avec le branding visible d'un outil tiers (TextMagic, logo + nom de compte "Steven Knight"), même problème que la capture "SanTMS" écartée précédemment sur cette vidéo. L'illustration précédente reste en place le temps qu'une image de remplacement neutre soit fournie.

## Rendu
Voir renders/
