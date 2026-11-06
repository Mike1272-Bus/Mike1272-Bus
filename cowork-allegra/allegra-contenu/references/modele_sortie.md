# Le modèle de sortie

## Où ranger

```
cowork-allegra/publications/AAAA-MM-JJ/
  13h-<sujet-court>/
    script.md
    legende.txt
    statut_whatsapp.txt
    (copie du modèle de vidéo : index.html, mix.py, assets/…)
    renders/allegra-AAAA-MM-JJ-13h-<sujet-court>.mp4   ← si le rendu a marché
    A_RENDRE.md                                       ← seulement si le rendu n'a pas marché
  19h-<sujet-court>/
    (pareil)
```

`<sujet-court>` : 1 à 3 mots en minuscules, sans accents, avec des tirets (exemple : `glace-cornet`). Quand tu copies un modèle, ne copie pas son dossier `renders/` (crée-en un vide) ni `node_modules/`.

## script.md

```markdown
# AAAA-MM-JJ, 13 h : <titre>

Type : avant → après | démo | coulisses | offre
Secteur : <secteur>
Clip(s) : stock/raw/<fichier>.mp4
Mot-clé : VIDÉO | ESSAI
Durée : 20 à 25 s

## Accroche (voix, 2 à 3 s)
> <une phrase, registre « vous »>

## Scènes (texte à l'écran)
| Temps | À l'écran | Texte |
|---|---|---|
| 0 à 3 s | … | … |
| … | … | … |
| fin | Téléphone WhatsApp, pilule verte du numéro | Écrivez <MOT-CLÉ> au +243 831 710 181 |

## Musique et bruitages
<musique, et les moments des bruitages : whoosh aux transitions, pop sur les textes>
```

## legende.txt

Même forme que `prospection/contenu-allegra/textes_a_poster.md` :

```
<phrase d'accroche avec 1 emoji>
<2 ou 3 phrases simples qui disent ce qu'on voit>
<appel : Écrivez VIDÉO (ou ESSAI) au +243 831 710 181 …>
(Exemple de pub réalisé avec des images libres de droits.)
#Kinshasa #RDC #<secteur> #publicité #vidéo
```

## statut_whatsapp.txt

Une ou deux lignes, pour accompagner la vidéo en statut :

```
<accroche courte> 👉 Écrivez <MOT-CLÉ> au +243 831 710 181
```

## A_RENDRE.md (seulement si besoin)

Ce qui a bloqué (la commande et le message d'erreur), et la phrase à donner à Claude Code : « Fais le rendu de `cowork-allegra/publications/AAAA-MM-JJ/13h-<sujet>` ».
