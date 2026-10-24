# Automatiser le contenu Allegra avec Claude Cowork

Ce dossier contient un **skill** (`allegra-contenu`) qui apprend à Cowork à préparer, chaque jour, les 2 publications d'Allegra Digital Ground (13 h et 19 h) : sujet, script, texte à l'écran, légende Facebook/Instagram, texte du statut WhatsApp et, si ton ordinateur le permet, la vidéo rendue.

**Cowork prépare, toi tu valides, puis Cowork publie** à 13 h et 19 h sur la page Facebook et le compte Instagram d'Allegra (via Zapier). Rien ne part sans ton « valide ». Le statut WhatsApp, tu le postes toi-même (WhatsApp ne permet pas de l'automatiser).

## Ce qu'il y a dedans

| Fichier | Rôle |
|---|---|
| `allegra-contenu/SKILL.md` | La marche à suivre de Cowork |
| `allegra-contenu/references/regles_et_da.md` | Les règles (pas de chiffres inventés, pas de visages, registre « vous ») et la D.A. claire |
| `allegra-contenu/references/calendrier_type.md` | Quel type de post à 13 h et 19 h, chaque jour, et quel modèle de vidéo copier |
| `allegra-contenu/references/sujets.md` | La réserve d'idées (avant → après, démo, coulisses, offre) |
| `allegra-contenu/references/modele_sortie.md` | Où et comment Cowork range son travail |
| `allegra-contenu/references/publication_meta.md` | Comment Cowork publie les posts validés sur Facebook et Instagram |
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

La chaîne : **Cowork** prépare à 7 h → tu écris « Valide » → à 13 h et à 19 h, Cowork met la vidéo sur **Google Drive** et la publie par **Zapier** sur la page Facebook et le compte Instagram d'Allegra.

1. **Instagram en compte professionnel « Entreprise »** (pas « Créateur » : Zapier ne publie que sur les comptes Entreprise). Dans Instagram : Paramètres > Type de compte et outils > Passer à un compte professionnel > Entreprise. Puis **relie-le à la page Facebook d'Allegra** (Meta Business Suite ou Paramètres de la page > Comptes liés). Tu dois être administrateur de la page.
2. **Zapier, Facebook Pages** : ouvre ce lien et connecte ton Facebook, en cochant la page Allegra : https://mcp.zapier.com/api/v1/connect-auth/FacebookV2CLIAPI?accountId=24986340
3. **Zapier, Instagram** : tes 3 connexions Instagram actuelles n'ont plus d'accès valide (j'ai vérifié : « access_token missing »). Reconnecte-en une avec ce lien, en cochant la page Facebook et le compte Instagram d'Allegra : https://mcp.zapier.com/api/v1/connect-auth/InstagramBusinessCLIAPI?accountId=24986340
4. **Dans Claude** (Paramètres > Connecteurs) : vérifie que **Zapier** et **Google Drive** sont activés, pour qu'ils marchent aussi dans Cowork.
5. **Premier essai** : sur un post prêt, écris à Cowork « Valide 19 h, publie maintenant ». Regarde la page et le compte Instagram. Cowork note alors les identifiants de la page et du compte pour les jours suivants.

**Le coût Zapier, à savoir avant :** chaque publication par Zapier compte **2 tâches**. 2 posts par jour × 2 réseaux = environ **240 tâches par mois**. Le forfait gratuit de Zapier n'en donne que **100** : il tient environ 12 jours. Pour tout le mois, il faut le forfait payant de Zapier (vérifie le prix sur zapier.com/pricing). Sans payer : Cowork prépare tout, et tu publies toi-même dans **Meta Business Suite**, où tu peux aussi programmer les 2 posts du jour sur Facebook et Instagram en une fois (2 minutes le matin).

## Le programmer tous les jours

Dans Cowork, crée **3 tâches programmées** (*Scheduled*), toutes sur le dossier `Mike1272-Bus`.

**Tâche 1, « Allegra : préparer »**
- **Quand** : tous les jours à 7 h (tu as le temps de relire avant 13 h).
- **Dossier** : `Mike1272-Bus`.
- **Consigne** (à copier) :

> Utilise le skill allegra-contenu. Prépare les 2 publications Allegra d'aujourd'hui (13 h et 19 h) dans cowork-allegra/publications/. Fais le rendu des vidéos si les outils marchent, sinon écris A_RENDRE.md. Mets à jour cowork-allegra/suivi.md. Termine par un résumé court pour Mike et attends son « valide » avant de publier quoi que ce soit.

**Tâche 2, « Allegra : publier 13 h »** (tous les jours à 13 h) et **Tâche 3, « Allegra : publier 19 h »** (tous les jours à 19 h). Consigne (change l'heure) :

> Utilise le skill allegra-contenu. Publie sur Facebook et Instagram le post Allegra de 13 h d'aujourd'hui, seulement s'il est « validé » dans cowork-allegra/suivi.md, en suivant references/publication_meta.md. Sinon, ne publie rien et rappelle-le à Mike.

Vers 8 h, tu relis dans Cowork et tu réponds « Valide 13 h et 19 h » (ou tu demandes une correction). Les tâches de 13 h et 19 h publient ensuite toutes seules.

Le soir, ou le lendemain matin, donne tes chiffres à Cowork :
> Hier : burger 13 h, 120 vues Instagram, 2 messages VIDÉO. Offre 19 h, 80 vues statut, 1 message ESSAI.

Il les note dans `suivi.md`, et chaque lundi il fait le bilan : ce qu'on garde, ce qu'on arrête, ce qu'on double.

## Les limites (à savoir avant)

- **L'application doit être ouverte.** Une tâche programmée ne tourne que si Claude Desktop est ouvert et l'ordinateur allumé (pas en veille). Sinon, elle se lance quand tu rouvres l'application : la publication de 13 h partira donc en retard si ton PC était éteint.
- **Le rendu vidéo** demande **Node.js**, **ffmpeg**, **Python** et internet sur ton ordinateur (HyperFrames télécharge Chrome la première fois). S'ils manquent, Cowork prépare tout (script, textes, légende, dossier de la vidéo) et écrit `A_RENDRE.md` : tu demandes ensuite le rendu à Claude Code, qui le fait dans le cloud.
- **La voix de l'accroche** (2 s) : Cowork ne l'enregistre pas. Il met l'accroche en texte à l'écran ; enregistre-la au téléphone et dépose-la dans le dossier si tu veux la voix.
- **Les forfaits** : les tâches programmées de Cowork demandent un forfait payant de Claude.
- **La synchronisation** : Cowork travaille sur la copie de ton ordinateur. Pour que les autres chats voient ses fichiers, fais *Commit* puis *Push* dans GitHub Desktop (et *Pull* avant, pour récupérer leur travail).

## Si tu modifies le skill

Change les fichiers dans `allegra-contenu/`, puis refais le zip et réimporte-le dans Cowork :
```
cd cowork-allegra && zip -r allegra-contenu.zip allegra-contenu
```
