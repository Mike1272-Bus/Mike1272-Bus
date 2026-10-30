# Voix ElevenLabs pour les 6 avant / après (TikTok)

But : une accroche parlée au début (sur la partie « AVANT ») et une fin parlée (sur la carte de fin). Le milieu reste musique + effets.
Pour économiser les crédits : **une seule génération** avec les 7 phrases (environ 360 caractères au total). La fin est la même pour les 6 vidéos.

## Réglages
- Modèle : Multilingual v2 (ou le plus récent qui parle français).
- Voix : Voice Library → langue **French**, usage **Advertisement / Narration**, une voix grave et posée. Écouter l'aperçu avant (gratuit), puis générer **une seule fois**.
- Stabilité ~50 %, Similarité ~75 %, Style 0 à 20 %, vitesse normale.

## Le texte à coller (tel quel, une phrase par ligne)
```
Votre burger est bon. Mais votre photo ne le vend pas.

Une glace qu'on fait défiler, personne ne l'achète.

Une robe en photo, on passe. Regardez la différence.

Vos produits de beauté méritent mieux qu'une photo plate.

Une basket en photo, c'est joli. Regardez ça.

Votre gadget est top. Mais en photo, personne ne le voit.

Votre vidéo d'essai est gratuite. Écrivez ESSAI.
```

Télécharger le MP3 et le mettre ici : `voix/tout.mp3`. Puis : `python3 ajouter_voix.py` → `renders/voix/avant-apres-<produit>.mp4`.
(Ou bien un fichier par phrase : `voix/burger.mp3`, `voix/glace.mp3`, `voix/vetements-femmes.mp3`, `voix/cosmetiques.mp3`, `voix/chaussures.mp3`, `voix/gadget.mp3`, `voix/fin.mp3`.)
