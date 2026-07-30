---
workflow: general-video
flow: automation
storyboard: no
message: "Le vrai probleme n'est pas la concurrence, c'est le manque de confiance que ton profil inspire."
destination: tiktok
aspect: 1080x1920
language: fr
audience: "petits commercants qui vendent en ligne"
length: 45s
angle: "avis/opinion tranchee, ton direct, deuxieme personne (tu) - contenu 'samedi' du calendrier hebdo ADG"
---

## Intent

Septieme video de la serie (contenu "samedi": opinion). Avis tranche: la concurrence n'est pas le vrai frein a la vente, c'est le manque de confiance qu'inspire le profil/la boutique du vendeur. CTA doux: "Le lien est en bio" pour inspirer plus confiance.

**Nouvelle regle standing (a partir de cette video, pour toutes les suivantes)**: chaque scene narrative est decoupee en **3 images sequentielles**, calees sur 3 morceaux de la phrase de la voix-off. Coupe nette entre les images (l'image precedente disparait completement quand la suivante arrive, jamais superposees). Seul le CTA garde une image unique.

## Assets (16 illustrations generees par l'agent — pas de generateur d'images IA photorealiste disponible dans cet environnement, HeyGen/mflux/Codex tous inaccessibles; illustrations vectorielles style BlockFrame via HTML/CSS/emoji + Playwright, deja validees par l'utilisateur sur un echantillon precedent)

- Accroche: `accroche-1-concurrence.png` (grille de boutiques, la concurrence) / `accroche-2-envrai.png` (icone de retournement, transition "en vrai") / `accroche-3-pasleprobleme.png` (grille de boutiques barree d'un X)
- Developpement: `developpement-1-milliers.png` (grille de boites/produits) / `developpement-2-vendfacile.png` (boutique etoilee avec courbe montante) / `developpement-3-memenombre.png` (balance entre deux groupes de boutiques egaux)
- Probleme: `probleme-1-confiance.png` (poignee de main) / `probleme-2-jamais.png` (chariot barre d'un interdit) / `probleme-3-inspirerien.png` (silhouette grise/floue, anonyme)
- Exemple: `exemple-1-memeprix.png` (deux boutiques, meme prix) / `exemple-2-deuxprofils.png` (comparaison profil pro coche vs profil flou) / `exemple-3-lechoix.png` (doigt qui pointe vers une poignee de main)
- Avis final: `avis-1-stop.png` (visage frustre/stop) / `avis-2-demandetoi.png` (gros point d'interrogation) / `avis-3-toimeme.png` (miroir + boutique)
- CTA: `cta-confiance.png` (bouclier + bouton "LIEN EN BIO")

## Customizations

- **Sous-titres/captions obligatoires** (regle permanente depuis la video 4).
- **NOUVELLE regle: 3 images sequentielles par scene, coupe nette** (regle permanente a partir de cette video) — remplace/complete la regle d'empilement a deux images des videos 4-6 (qui reste valable si une scene future n'a que 2 images).
- Voix-off: voix locale Kokoro (`ff_siwis`, francais) en attendant la vraie voix de l'utilisateur.
- Meme systeme de marque (preset blockframe) que les videos 1 a 6 pour la coherence de la serie.
- Ton direct/opinion tranchee, deuxieme personne ("tu"), jamais "je". CTA final: "Le lien est en bio" (pas de mention produit directe).
- Pas de mention de l'IA.

## Notes

- Script ecrit en francais simple et parle, deja valide par l'utilisateur mot pour mot (voir voiceover + decoupage par image dans STORYBOARD.md).
- Timing des 3 images par scene calcule a partir des timestamps mots-a-mots de la voix Kokoro (estimation deterministe par poids de caracteres, faute d'ASR reseau disponible), pas de decoupage arbitraire.
