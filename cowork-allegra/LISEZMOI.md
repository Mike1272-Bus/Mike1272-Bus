# Automatiser le contenu Allegra avec Claude Cowork

Ce dossier contient un **skill** (`allegra-contenu`) qui apprend à Cowork à préparer, chaque jour, les 2 publications d'Allegra Digital Ground (13 h et 19 h) : sujet, script, texte à l'écran, légende Facebook/TikTok, texte du statut WhatsApp et, si ton ordinateur le permet, la vidéo rendue.

**Cowork prépare, toi tu valides et tu publies.** Le skill ne publie jamais rien.

## Ce qu'il y a dedans

| Fichier | Rôle |
|---|---|
| `allegra-contenu/SKILL.md` | La marche à suivre de Cowork |
| `allegra-contenu/references/regles_et_da.md` | Les règles (pas de chiffres inventés, pas de visages, registre « vous ») et la D.A. claire |
| `allegra-contenu/references/calendrier_type.md` | Quel type de post à 13 h et 19 h, chaque jour, et quel modèle de vidéo copier |
| `allegra-contenu/references/sujets.md` | La réserve d'idées (avant → après, démo, coulisses, offre) |
| `allegra-contenu/references/modele_sortie.md` | Où et comment Cowork range son travail |
| `allegra-contenu.zip` | Le même skill, prêt à importer dans Cowork |
| `suivi.md` | Le tableau des posts et de leurs chiffres (vues, messages) |
| `publications/` | Ce que Cowork produit, un dossier par jour |

## Installation (une seule fois)

1. **Avoir le dépôt sur ton ordinateur.** Avec GitHub Desktop : *Clone* du dépôt `Mike1272-Bus`, puis choisis la branche `claude/gallant-goldberg-l20gu3`. (Sans GitHub Desktop : bouton *Code* > *Download ZIP* sur GitHub, puis décompresse.)
2. **Ouvrir Claude Desktop**, onglet **Cowork**.
3. **Importer le skill** : *Customize* > *Skills* > ajouter un skill > choisir `cowork-allegra/allegra-contenu.zip`. Vérifie qu'il est activé.
4. **Donner le dossier à Cowork** : dans une tâche Cowork, choisis le dossier `Mike1272-Bus` comme dossier de travail.
5. **Tester à la main** : écris à Cowork
   > Fais le contenu Allegra de demain.

   Regarde le résultat dans `cowork-allegra/publications/<date>/`. Si quelque chose ne va pas, dis-le à Cowork : il corrige.

## Le programmer tous les jours

Dans Cowork, crée une **tâche programmée** (*Scheduled*) :
- **Quand** : tous les jours à 7 h (tu as le temps de relire avant 13 h).
- **Dossier** : `Mike1272-Bus`.
- **Consigne** (à copier) :

> Utilise le skill allegra-contenu. Prépare les 2 publications Allegra d'aujourd'hui (13 h et 19 h) dans cowork-allegra/publications/. Fais le rendu des vidéos si les outils marchent, sinon écris A_RENDRE.md. Mets à jour cowork-allegra/suivi.md. Termine par un résumé court pour Mike. Ne publie rien.

Le soir, ou le lendemain matin, donne tes chiffres à Cowork :
> Hier : burger 13 h, 120 vues TikTok, 2 messages VIDÉO. Offre 19 h, 80 vues statut, 1 message ESSAI.

Il les note dans `suivi.md`, et chaque lundi il fait le bilan : ce qu'on garde, ce qu'on arrête, ce qu'on double.

## Les limites (à savoir avant)

- **L'application doit être ouverte.** Une tâche programmée ne tourne que si Claude Desktop est ouvert et l'ordinateur allumé (pas en veille). Sinon, elle se lance quand tu rouvres l'application.
- **Le rendu vidéo** demande **Node.js**, **ffmpeg**, **Python** et internet sur ton ordinateur (HyperFrames télécharge Chrome la première fois). S'ils manquent, Cowork prépare tout (script, textes, légende, dossier de la vidéo) et écrit `A_RENDRE.md` : tu demandes ensuite le rendu à Claude Code, qui le fait dans le cloud.
- **La voix de l'accroche** (2 s) : Cowork ne l'enregistre pas. Il met l'accroche en texte à l'écran ; enregistre-la au téléphone et dépose-la dans le dossier si tu veux la voix.
- **Les forfaits** : les tâches programmées de Cowork demandent un forfait payant de Claude.
- **La synchronisation** : Cowork travaille sur la copie de ton ordinateur. Pour que les autres chats voient ses fichiers, fais *Commit* puis *Push* dans GitHub Desktop (et *Pull* avant, pour récupérer leur travail).

## Si tu modifies le skill

Change les fichiers dans `allegra-contenu/`, puis refais le zip et réimporte-le dans Cowork :
```
cd cowork-allegra && zip -r allegra-contenu.zip allegra-contenu
```
