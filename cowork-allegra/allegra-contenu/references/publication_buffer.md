# Publier automatiquement : Instagram, Facebook et TikTok (via Buffer)

Buffer publie à l'heure prévue sur les 3 réseaux. Cowork lui envoie les posts par le connecteur **Zapier** (action Buffer), avec la vidéo déposée sur **Google Drive**.

## La règle d'or

**Rien ne part sans le « oui » de Mike.** Cowork publie seulement les posts dont le statut est « validé » dans `suivi.md`, c'est-à-dire après que Mike a écrit, par exemple : « Valide 13 h et 19 h », « Valide 13 h », ou « Valide tout ». S'il demande une correction, corrige, renvoie-lui le résumé, et attends.

## Les étapes, pour chaque post validé

1. **Vérifier avant d'envoyer.** La vidéo existe (`renders/allegra-….mp4`, moins de 50 Mo, 9:16), la légende est prête, l'heure prévue (13 h ou 19 h, heure de Kinshasa) n'est pas déjà passée. Si l'heure est passée, demande à Mike : maintenant, ou au prochain créneau ?
2. **Déposer la vidéo sur Google Drive** (connecteur Google Drive), dans le dossier `Allegra - publications/AAAA-MM-JJ/`. Partage : « Tous les utilisateurs disposant du lien peuvent lire ». Garde l'identifiant du fichier et fabrique le lien direct : `https://drive.google.com/uc?export=download&id=<ID>`.
3. **Créer le post dans Buffer** (connecteur Zapier, action Buffer « update » = créer un post), **une fois par réseau** :

   | Réseau | Texte | Type |
   |---|---|---|
   | Instagram | `legende.txt` | Reel |
   | Facebook | `legende.txt` | Vidéo (ou Reel) |
   | TikTok | `legende.txt`, en enlevant la ligne « (Exemple…) » si elle dépasse la place | Vidéo |

   Mets le lien direct de la vidéo dans le champ média, et l'heure prévue (13:00 ou 19:00, fuseau Africa/Kinshasa). Si l'action propose « ajouter à la file » au lieu d'une heure précise, prends l'heure précise.
4. **Vérifier.** Relis la réponse de Zapier pour chaque réseau. Un échec = ne pas réessayer en boucle : une seule nouvelle tentative, puis note l'erreur.
5. **Noter dans `suivi.md`** : statut « programmé » (ou « échec Buffer : <raison> »), et l'heure.
6. **Dire à Mike** en une ou deux lignes : « Programmé : 13 h (Instagram, Facebook, TikTok), 19 h (…). » ou ce qui a échoué.

## Le statut WhatsApp

WhatsApp ne permet pas de publier un statut automatiquement. Donne à Mike la vidéo et le texte de `statut_whatsapp.txt` : il le poste en 30 secondes.

## Si quelque chose manque

- **Pas de connecteur Zapier ou Google Drive dans Cowork** : ne publie pas. Dis à Mike de les ajouter (Paramètres > Connecteurs) et laisse les posts en « validé ».
- **La première fois**, l'action Buffer demande de choisir l'organisation et les 3 canaux (Instagram, Facebook, TikTok) : note leurs identifiants à la fin de ce fichier pour les jours suivants.

## Les identifiants Buffer (à remplir au premier envoi)

- Organisation :
- Canal Instagram :
- Canal Facebook :
- Canal TikTok :
