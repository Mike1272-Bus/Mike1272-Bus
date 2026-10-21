# Contexte pour Claude (lu automatiquement à chaque nouveau chat)

Mike (DigitalMikaelson / Allegra Digital Ground / My automation, Kinshasa, RDC) : produits digitaux, prospection d'entreprises avec des vidéos animées, accompagnements, contenu TikTok. **Tout ce qui est automatisation pour entreprises se vend sous le nom « My automation »** (plus Allegra).

- **Commence toujours par lire `TABLEAU_DE_BORD.md`** : l'état de chaque projet, les prochaines actions, les dossiers. Mets-le à jour quand quelque chose avance.
- Le contexte complet de la marque est dans `projet-claude/contexte_projet.md`.
- Écris en français simple. « tu » pour DigitalMikaelson (jeunes), « vous » pour les entreprises (Allegra Digital Ground, My automation). Jamais les deux dans le même texte. Skill `copywriting` pour tout texte de marque.
- Ne jamais inventer : chiffres, prix, témoignages, résultats.
- **Secret professionnel** : dans tout document ou message pour un client (devis, PDF, messages), ne jamais dire comment on fabrique les vidéos (IA, banque d'images, outils, logiciels). On décrit seulement le résultat.
- Vidéos : HyperFrames (skills dans `.claude/skills`). Uniquement les images des clients, **aucune illustration de personnes**. Jamais de publication sans l'accord écrit de l'entreprise ou de la personne.
- Branche de travail : `claude/gallant-goldberg-l20gu3`. Plusieurs chats travaillent en parallèle sur cette branche : fais `git pull` avant de commencer et avant chaque push, ne touche qu'aux fichiers de ton pôle (et à ta section du tableau de bord), commits en français, puis push.
- Économie de tokens : réponses courtes par défaut (l'essentiel d'abord, détails seulement si Mike les demande). Ne pas relire des fichiers déjà lus ni tout le dépôt : lire seulement ce qui sert. Vérifier les vidéos avec une seule planche d'images, et seulement pour un rendu final. Ne pas envoyer d'images dans la conversation si un fichier suffit. Pour un nouveau sujet, conseiller à Mike d'ouvrir un nouveau chat (le contexte est dans ce fichier et le tableau de bord).
