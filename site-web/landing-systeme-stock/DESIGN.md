# DA : landing « Système de stock » (My automation)

Références de Mike : une maquette « verre 3D » lavande (mise en page en cases, panneaux bleu nuit) et dupliq.co.uk (police, fond géométrique en réseau, formulaire final).

- **Couleurs** : fond `#eceef6` → `#e2e1f6`, encre `#12142a`, accent `#5b57f0` (survol `#4a46e0`), accent clair `#7e7bff`, nuit `#12142a` / `#1c1f3d`, texte sur nuit `#eef0ff` / `#a9acd0`, WhatsApp `#25d366`.
- **Police** : Josefin Sans (300, 400, 600, 700), proche de Brandon Grotesque (police payante de Dupliq). Titres en 700.
- **Fond géométrique** : réseau de points reliés (SVG généré), blanc à 10 % sur les panneaux nuit, violet très léger sur le fond clair.
- **Formes** : boutons en pilule, cases arrondies 16 à 32 px, verre (fond blanc translucide + flou) surtout sur les objets 3D du premier écran.
- **Images** : vidéo de vente My automation, images tirées de la vidéo, illustrations 3D Fluent Emoji (Microsoft, licence MIT). Aucune personne.
- **Le workflow** est le fil de la page : démo « Simuler une vente » (tubes de stock), panneau du circuit animé (vente → stock → WhatsApp → client → alerte), 4 messages du jour.
- **Appel à l'action** : WhatsApp +243 831 710 181 (message pré-rempli) + formulaire final (Google Sheet + email + WhatsApp).

## Mise en ligne
- Adresse : https://my-automation-rdc.vercel.app (domaine ajouté au projet Vercel `allegra-digital-ground`, faute de droit pour créer un projet).
- Copie publiée : `allegra-landing/site/my-automation/`. Le fichier `allegra-landing/site/vercel.json` envoie ce domaine vers ce dossier.
- Après une modif ici, recopier `index.html` et `media/` dans `allegra-landing/site/my-automation/`, puis redéployer.
