# Recevoir les demandes du formulaire (Google Sheet + email + WhatsApp)

Quand un visiteur remplit le formulaire :
1. sa demande s'ajoute dans le Google Sheet **« My automation - Demandes de démo (site) »** (dans le Drive de Mike) ;
2. un email arrive sur tambwemike92@gmail.com ;
3. WhatsApp s'ouvre chez le visiteur avec son message prêt pour le +243 831 710 181.

## À faire une seule fois (5 minutes, par Mike)
1. Ouvrir le Google Sheet « My automation - Demandes de démo (site) ».
2. Menu **Extensions → Apps Script**. Effacer le code présent et coller le contenu de `Code.gs`. Enregistrer.
3. **Déployer → Nouveau déploiement** → type **Application Web**.
   - Exécuter en tant que : **Moi**
   - Qui a accès : **Tout le monde**
4. Autoriser l'accès (Google demande la permission pour le Sheet et l'email).
5. Copier l'**URL de l'application Web** (elle finit par `/exec`) et l'envoyer à Claude.
   Claude la colle dans `index.html` (`const LEAD_ENDPOINT = '...'`) et redéploie le site.

Tant que l'URL n'est pas collée, le formulaire envoie seulement sur WhatsApp.
