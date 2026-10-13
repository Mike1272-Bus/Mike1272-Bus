# Automatiser le contenu Allegra avec Claude Cowork

Ce dossier contient un **skill** (`allegra-contenu`) qui apprend à Cowork à préparer, chaque jour, les 2 publications d'Allegra Digital Ground (13 h et 19 h) : sujet, script, texte à l'écran, légende Facebook/TikTok, texte du statut WhatsApp et, si ton ordinateur le permet, la vidéo rendue.

**Cowork prépare, toi tu valides, puis Cowork programme** les posts sur Instagram, Facebook et TikTok (via Buffer). Rien ne part sans ton « valide ». Le statut WhatsApp, tu le postes toi-même (WhatsApp ne permet pas de l'automatiser).

## Ce qu'il y a dedans

| Fichier | Rôle |
|---|---|
| `allegra-contenu/SKILL.md` | La marche à suivre de Cowork |
| `allegra-contenu/references/regles_et_da.md` | Les règles (pas de chiffres inventés, pas de visages, registre « vous ») et la D.A. claire |
| `allegra-contenu/references/calendrier_type.md` | Quel type de post à 13 h et 19 h, chaque jour, et quel modèle de vidéo copier |
| `allegra-contenu/references/sujets.md` | La réserve d'idées (avant → après, démo, coulisses, offre) |
| `allegra-contenu/references/modele_sortie.md` | Où et comment Cowork range son travail |
| `allegra-contenu/references/publication_buffer.md` | Comment Cowork programme les posts validés sur Instagram, Facebook et TikTok |
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

## Brancher la publication automatique (une seule fois)

La chaîne : **Cowork** prépare → tu écris « Valide » → Cowork dépose la vidéo sur **Google Drive** → il crée les posts dans **Buffer** par **Zapier** → Buffer publie à 13 h et 19 h sur Instagram, Facebook et TikTok.

1. **Buffer** (buffer.com) : crée un compte. Le forfait gratuit accepte 3 réseaux, juste ce qu'il faut. Connecte :
   - **Instagram** : le compte doit être **professionnel** (Paramètres Instagram > Type de compte), relié à la page Facebook d'Allegra ;
   - **Facebook** : la **page** Allegra (pas ton profil perso) ;
   - **TikTok** : le compte TikTok d'Allegra (compte Business conseillé).
   Dans Buffer, règle le fuseau horaire sur **Kinshasa**.
2. **Zapier** : ouvre ce lien et connecte ton compte Buffer : https://mcp.zapier.com/api/v1/connect-auth/BufferCLIAPI?accountId=24986340 (l'action Buffer est déjà activée sur ton serveur Zapier).
3. **Dans Claude** (Paramètres > Connecteurs) : vérifie que **Zapier** et **Google Drive** sont activés, pour qu'ils marchent aussi dans Cowork.
4. **Premier essai** : dans Cowork, écris « Valide 19 h » sur un post prêt. Regarde dans Buffer que les 3 posts sont bien programmés. Au premier envoi, Cowork note les identifiants des canaux Buffer pour les jours suivants.

À savoir :
- Le forfait gratuit de Buffer garde **10 posts programmés par réseau** à la fois : largement assez pour 2 posts par jour.
- TikTok, par Buffer, publie la vidéo avec sa propre musique : pas de son tendance TikTok.
- Si Buffer refuse la vidéo venant de Google Drive, dis-le-moi : on passera par un autre hébergement.

## Le programmer tous les jours

Dans Cowork, crée une **tâche programmée** (*Scheduled*) :
- **Quand** : tous les jours à 7 h (tu as le temps de relire avant 13 h).
- **Dossier** : `Mike1272-Bus`.
- **Consigne** (à copier) :

> Utilise le skill allegra-contenu. Prépare les 2 publications Allegra d'aujourd'hui (13 h et 19 h) dans cowork-allegra/publications/. Fais le rendu des vidéos si les outils marchent, sinon écris A_RENDRE.md. Mets à jour cowork-allegra/suivi.md. Termine par un résumé court pour Mike et attends son « valide » avant de programmer quoi que ce soit dans Buffer.

Vers 8 h, tu relis dans Cowork et tu réponds « Valide 13 h et 19 h » (ou tu demandes une correction). Cowork programme alors les posts.

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
