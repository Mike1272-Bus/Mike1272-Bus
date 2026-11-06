# Publier automatiquement sur Facebook et Instagram (via Zapier)

Cowork publie lui-même, par le connecteur **Zapier**, à l'heure du créneau : la page Facebook d'Allegra (action « Create Page Video ») et le compte Instagram d'Allegra en Reel (action « Publish Video »). La vidéo passe par **Google Drive** pour avoir un lien public.

Ces actions publient **tout de suite** (elles ne programment pas). C'est pour ça qu'il y a deux tâches programmées dans Cowork : une à 13 h, une à 19 h. Chacune publie le post validé de son créneau.

## La règle d'or

**Rien ne part sans le « oui » de Mike.** Tu publies seulement un post dont le statut est « validé » dans `suivi.md`, c'est-à-dire après que Mike a écrit, par exemple : « Valide 13 h et 19 h », « Valide 13 h », ou « Valide tout ». S'il demande une correction, corrige, renvoie-lui le résumé, et attends. Un post « à valider » à l'heure du créneau ne part pas : rappelle-le à Mike.

## Quand Mike écrit « valide »

Passe le ou les posts en « validé » dans `suivi.md`, puis prépare le lien de la vidéo tout de suite (étape 2 ci-dessous), pour que la publication de 13 h ou 19 h n'ait plus qu'à l'envoyer. Si Mike écrit « publie maintenant », publie tout de suite.

## Les étapes de publication (tâche de 13 h ou de 19 h)

1. **Trouver le post du créneau** dans `suivi.md` : date du jour, heure du créneau, statut « validé ». S'il n'y en a pas, arrête-toi et dis-le à Mike en une ligne.
2. **Le lien de la vidéo.** Vérifie la vidéo (`renders/allegra-….mp4`, format 9:16, entre 3 s et 90 s, moins de 100 Mo). Dépose-la sur Google Drive (connecteur Google Drive) dans le dossier `Allegra - publications/AAAA-MM-JJ/`, partage « Tous les utilisateurs disposant du lien peuvent lire », et fabrique le lien direct : `https://drive.google.com/uc?export=download&id=<ID>`.
3. **Facebook** : Zapier, Facebook Pages, « Create Page Video ».
   - Page : la page Allegra (identifiant noté en bas de ce fichier) ;
   - Video : le lien direct ;
   - Title : le titre court du post (exemple : « Une photo de pizza devient une pub ») ;
   - Description : tout le texte de `legende.txt`.
4. **Instagram** : Zapier, Instagram for Business, « Publish Video » (publié en Reel).
   - Instagram Account to Use : le compte Allegra (identifiant noté en bas de ce fichier) ;
   - Video : le même lien direct ;
   - Caption : tout le texte de `legende.txt` (2 200 caractères maximum).
5. **Vérifier la réponse** de Zapier pour chaque réseau. En cas d'échec : une seule nouvelle tentative, puis note l'erreur. Ne jamais publier deux fois le même post : avant de réessayer, regarde si le premier envoi n'est pas déjà passé.
6. **Noter dans `suivi.md`** : statut « publié FB + IG » (ou « publié FB, échec IG : <raison> »).
7. **Dire à Mike** en une ligne : « Publié à 13 h sur Facebook et Instagram ✅ Le statut WhatsApp est à poster : <texte de statut_whatsapp.txt> ».

## Le statut WhatsApp

WhatsApp ne permet pas de publier un statut automatiquement. Donne à Mike la vidéo et le texte de `statut_whatsapp.txt` : il le poste en 30 secondes.

## Si quelque chose manque

- **Pas de connecteur Zapier ou Google Drive dans Cowork** : ne publie pas. Dis à Mike de les activer (Paramètres > Connecteurs) et laisse le post en « validé ».
- **Zapier refuse (« task limit », plus de tâches)** : ne réessaie pas. Dis à Mike que le forfait Zapier du mois est épuisé et donne-lui le plan B : publier lui-même la vidéo et la légende dans Meta Business Suite (Facebook et Instagram en une fois).
- **La première fois**, choisis la page Facebook et le compte Instagram d'**Allegra** dans les listes de Zapier (pas ceux de DigitalMikaelson). En cas de doute, demande à Mike. Note ensuite les identifiants ci-dessous.

## Les identifiants (à remplir au premier envoi)

- Page Facebook Allegra (Zapier `page`) :
- Compte Instagram Allegra (Zapier `instagramPageId`) :
