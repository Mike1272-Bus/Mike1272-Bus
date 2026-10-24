# Mini-site vitrine : La Ruche du Terroir (démo)

Une page, pensée d'abord pour le téléphone. Tout vient de leurs publications Instagram : photos, slogans, parfums, adresse, téléphone, e-mail. Aucun prix n'est affiché (ils n'en publient pas) : les boutons ouvrent WhatsApp avec la demande déjà écrite.

## Sections
1. Accueil : « Le miel, votre allié de bien-être au quotidien », la gamme de pots, bouton WhatsApp
2. Nos miels : cannelle, moringa, toute la gamme (cannelle, gingembre, clou de girofle, poivre noir, hibiscus, moringa) et le gingembre en poudre
3. Packs cadeaux pour les entreprises (« Faites plaisir à vos équipes avec des produits locaux »), bouton devis
4. Citation, puis contact : WhatsApp, téléphone, e-mail, adresse avec itinéraire, Instagram
5. Bouton WhatsApp flottant sur téléphone

## Qualité (règles de la Front-End Checklist appliquées)
- HTML validé (html-validate) : `lang="fr"`, HTML sémantique, un seul `h1`, IDs uniques, textes alternatifs sur toutes les images, lien « Aller au contenu »
- Zoom autorisé, focus visible au clavier, contrastes conformes (WCAG AA), animations coupées si « réduire les animations » est activé
- CSS dans un fichier séparé, variables de couleurs, unités relatives, animations en transform/opacity uniquement
- Polices hébergées sur le site (Fraunces + DM Sans, sous-ensemble latin), préchargées, `font-display: swap`
- Images WebP avec largeur et hauteur, chargement différé sous la ligne de flottaison, image principale en priorité haute
- SEO : titre, description, Open Graph (image `og-image.jpg`), données structurées schema.org `Store`
- Aucun JavaScript

Lighthouse (mobile, serveur local sans compression) : Performance 95 · Accessibilité 100 · Bonnes pratiques 100 · SEO 100.

## Mise en ligne (seulement après l'accord de La Ruche du Terroir)
- Héberger le dossier tel quel (Netlify, Vercel, Cloudflare Pages ou leur hébergeur) : la compression et le cache de l'hébergeur feront monter la performance.
- Remplacer `og-image.jpg` par son adresse complète dans la balise `og:image` (ex. `https://leur-domaine/og-image.jpg`).
- Enlever la ligne « Site démo préparé par… » ou la garder en signature, selon l'accord.
- Faire un QR code vers l'adresse du site pour leurs pots, affiches et paniers.

Captures : dossier `apercu/`. Pour les refaire : `python3 -m http.server 8765` dans ce dossier, puis `node shoot.mjs`.
