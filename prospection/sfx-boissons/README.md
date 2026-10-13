# Bruitages « boissons » (envoyés par Mike le 13 octobre)

À utiliser dans les vidéos des **marques de boissons** (et des plats avec une boisson). Ce ne sont pas les bruitages gourmands fabriqués pour +243 (croustillant, grésillement).

Préparation : le silence du début est coupé (le son démarre à 0 s, donc l'heure qu'on met dans `mix.py` est l'heure exacte du son), le volume est égalisé (-18 LUFS, crête -1 dB), une courte fin en fondu.

| Fichier | Durée | Ce qu'on entend (d'après l'analyse du spectre, **à confirmer à l'écoute**) | Pour quelle image |
|---|---|---|---|
| `boisson-1-tintements.wav` | 5,0 s | Petits chocs secs et espacés, par grappes : glaçons ou verre qui tinte | Glaçons qui tombent, verres qui trinquent |
| `boisson-2-versement-petillant.wav` | 5,1 s | Quelques chocs, puis un pétillement dense pendant environ 3 s | La boisson qui coule et mousse, les bulles qui montent |
| `boisson-3-versement-long.wav` | 7,1 s | Démarre après un court blanc, puis un souffle continu jusqu'à la fin, avec des chocs au début et vers 4,5 s | Un long versement, plan lent sur le verre qui se remplit |
| `boisson-4-ouverture-et-versement.wav` | 7,9 s | Un « clac » au début (capsule ou canette ?), puis un écoulement grave jusqu'à 6,5 s, puis un pétillement plus doux | Ouverture de la bouteille puis versement : idéal pour le début d'une vidéo |
| `boisson-5-gorgee.wav` | 3,3 s | Son doux, deux petites parties : une gorgée, ou un « ahh » ? | La fin : le plaisir de boire, juste avant le logo |

## Comment s'en servir dans `mix.py`
Dans la liste `SFX`, utiliser le chemin du dossier, comme pour les autres sons :

```python
SFX_BOISSONS = os.path.join(ROOT, "..", "sfx-boissons")
# (heure, fichier, volume)
(0.4, os.path.join(SFX_BOISSONS, "boisson-4-ouverture-et-versement.wav"), 0.8),
```

Couper un son trop long : `atrim=duration=2.5` dans le filtre de l'entrée (comme `typing` dans les anciens mix).

## À vérifier
- Les fichiers s'appelaient « videoplayback » : ils viennent sans doute d'une vidéo en ligne. Avant de les mettre dans une vidéo **publiée** par un client, vérifier qu'ils sont libres de droits (chaîne de bruitages gratuits, mention « no copyright »). Pour une vidéo d'essai envoyée en privé, pas de problème.
