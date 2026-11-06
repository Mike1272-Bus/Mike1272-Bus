# Prospection B2B en RDC avec 0 $ : avis et plan

Réponse au cahier des charges « Automatisation, scraping et prospection B2B RDC » (19 oct. 2026).
Pour Mike, débutant, budget 0 $, Kinshasa / Lubumbashi / Goma.

Les prix et les limites gratuites des outils changent souvent : **vérifie toujours sur le site de l'outil** avant de t'engager. Rien ici n'est un chiffre de résultat garanti.

---

## 0. L'avis en 5 lignes

1. **Ton cahier des charges est trop compliqué pour démarrer.** Scraping, Docker, IA, API Meta : c'est 6 outils à apprendre avant ton premier client. Il faut l'inverse : vendre d'abord, automatiser ensuite.
2. **Tu as déjà ce qu'il faut pour vendre** : le système de stock (n8n + Google Sheets + WhatsApp), la vidéo de vente, 52 entreprises listées et les messages d'approche.
3. **N'utilise pas de WhatsApp « non officiel »** (Evolution API, Baileys) chez un client : le numéro peut être bloqué par WhatsApp. On reste sur l'API officielle de Meta.
4. **Le scraping de Facebook / Google Maps est risqué** (compte bloqué, règles non respectées) et inutile au début : 20 entreprises par jour se trouvent à la main en 1 heure.
5. **Ce qui fait signer en RDC, c'est la démo en direct** : le téléphone du patron qui sonne pendant que tu lui parles.

---

## 1. Les outils : le plus simple possible, à 0 $

### Ce que je garde, ce que je retire

| Dans ton document | Mon avis | À la place |
|---|---|---|
| n8n en local avec Docker + ngrok | Trop compliqué pour débuter. Si ton PC s'éteint, plus rien ne marche. | **n8n Cloud** pour les démos (attention : c'est un essai gratuit limité dans le temps, regarde la date de fin dans ton compte). Pour durer à 0 $ : voir « Plan B » plus bas. |
| Make (1 000 opérations / mois) | Bien pour une démo, trop juste pour plusieurs clients. | À garder en secours. |
| Apify (scraping) | Inutile au début, et risqué sur Facebook. | Recherche à la main (section 2). |
| Gemini / OpenAI | Pas nécessaire pour vendre le système de stock. | Plus tard, pour des messages personnalisés automatiques. |
| Evolution API / Baileys (WhatsApp non officiel) | **Risque de blocage du numéro.** | API officielle WhatsApp (ce qu'on a installé) + l'appli **WhatsApp Business** gratuite pour ta prospection. |
| Meta Lead Ads (webhooks) | Il faut payer des pubs pour avoir des leads. | Plus tard, quand tu auras un budget. |

### La solution la plus simple pour un débutant à 0 $

**Google Sheets + Google Forms + Apps Script** (tout est gratuit avec un compte Gmail) :
- Google Forms remplace le formulaire de vente.
- Apps Script (le petit langage de Google, intégré au Sheet) peut faire les calculs, envoyer les e-mails et même appeler l'API WhatsApp. Pas de serveur à louer, pas de Docker.
- Inconvénient : il faut écrire un peu de code. Je peux l'écrire pour toi si n8n Cloud devient payant.

### Plan B pour garder n8n gratuitement

Des hébergeurs proposent un petit serveur gratuit à vie (par exemple Oracle Cloud « Always Free » ou Google Cloud « free tier »). On peut y installer n8n une fois. C'est plus technique (1 à 2 heures avec moi pas à pas), mais ensuite tu as n8n sans limite et sans payer. **À faire seulement après ton premier client.**

---

## 2. Trouver les entreprises sans scraping et sans risque

| Source (gratuite) | Comment faire | Pourquoi c'est bien |
|---|---|---|
| **Bibliothèque publicitaire Meta** (facebook.com/ads/library, pays : RDC) | Cherche « Kinshasa », « boutique », « immobilier »… Note les pages qui font de la pub. | Une entreprise qui paie des pubs a de l'argent **et** reçoit des messages : elle a besoin d'automatiser. |
| **Google Maps** | Cherche « quincaillerie Limete », « pharmacie Gombe »… Note le nom, le numéro et les avis. | Numéros souvent visibles. Les avis montrent les problèmes (« jamais de réponse », « rupture »). |
| **Facebook et Instagram** | Pages des commerces, groupes « business Kinshasa ». | Tu vois leur activité réelle pour personnaliser la première ligne. |
| **Annuaires** (moncongo.com, etc.) | Déjà utilisés pour ta liste de 52 entreprises. | Coordonnées rassemblées. |
| **LinkedIn** (gratuit) | Patrons et gérants de PME à Kinshasa / Lubumbashi. | Bon pour les entreprises plus structurées. |
| **Sur le terrain** | Gombe, Limete, Zando, Kintambo : 5 commerces par jour avec la démo sur ton téléphone. | Le plus efficace en RDC : confiance immédiate. |

**Règle :** 20 nouvelles entreprises par jour, notées dans `prospection_50_entreprises.xlsx`. C'est assez pour remplir ton agenda de démos.

**Pour envoyer :** l'appli WhatsApp Business gratuite (étiquettes, réponses rapides, message d'accueil) + les liens wa.me déjà prêts dans ton fichier de suivi. Envoie **à la main**, en personnalisant : jamais d'envoi en masse, sinon ton numéro sera signalé.

**Le message vocal de 30 secondes** marche très bien en RDC : après le premier message écrit, une note vocale chaleureuse montre qu'une vraie personne est derrière.

---

## 3. Les niches à viser en premier

Sur les 50 secteurs de ton document, voici ceux qui donnent de l'argent le plus vite **avec ce qu'on a déjà construit** :

| Ordre | Niche | Pourquoi | Ce qu'on vend |
|---|---|---|---|
| 1 | **Commerces avec stock** : quincailleries, cosmétiques, téléphones, alimentation, grossistes | Système prêt, vidéo prête, 52 prospects déjà listés. | Système de stock automatisé (l'exemple de la vidéo). |
| 2 | **Pharmacies** | Même besoin de stock, plus les dates de péremption. | Système de stock + alerte avant péremption (à ajouter : une colonne et une alerte). |
| 3 | **Écoles privées** | Relances des frais scolaires, inscriptions : beaucoup de travail à la main chaque trimestre. | Relances WhatsApp automatiques + suivi des paiements dans un Sheet. |
| 4 | **Agences immobilières et location de voitures** | Beaucoup de messages entrants (souvent grâce à leurs pubs Facebook), peu de suivi. | Réponse rapide + suivi des demandes dans un Sheet + relance. |

**Mon conseil : commence par la niche 1 seulement**, jusqu'au premier client payant. Une niche, un message, une démo. Ensuite tu ajoutes la 2 (presque le même système).

**Niches oubliées dans ton document, à garder pour plus tard :**
- les **grossistes de Zando** (gros volumes, beaucoup de stock) ;
- les **restaurants qui livrent** (commandes WhatsApp à suivre) ;
- les **agences de transfert d'argent et de Mobile Money** (suivi de caisse) ;
- les **ONG** (rapports à produire chaque mois).

---

## 4. Ton plan de 7 jours, à 0 $

| Jour | À faire | Résultat attendu |
|---|---|---|
| **J1** | Finir le grand test (modèles Meta « Actif »). **Enregistrer ton écran et ton téléphone** pendant le test : formulaire, Sheet, notification WhatsApp. Décider les **[À DÉCIDER]** : prix, garantie, délai. | Une démo qui marche + des extraits vidéo de preuve. |
| **J2** | Reprendre les 52 entreprises, garder les 20 plus faciles à joindre (niche 1). Écrire une première ligne personnalisée pour chacune. | 20 messages prêts. |
| **J3** | Envoyer 20 messages « question » (méthode Hormozi, voir `messages_approche_hormozi.md`). Passer dans 5 commerces avec la démo. | Premières réponses. |
| **J4** | 20 nouveaux messages + relances J+2 + notes vocales aux personnes qui ont répondu. Envoyer la vidéo à ceux qui disent « oui ». | 2 à 3 démos fixées (objectif, pas une garantie). |
| **J5** | Démos de 15 minutes, sur **leurs** produits. Proposer un essai : installation sur leur stock, paiement en 2 fois (une partie au démarrage, le reste après 7 jours si ça marche). | Une proposition envoyée. |
| **J6** | Relances J+5, nouvelles démos, réponses aux objections (coupures internet : il faut un téléphone avec un peu de données mobiles ; pendant une coupure, le vendeur note la vente et l'envoie dès que le réseau revient ; vendeur pas à l'aise : formulaire très simple + formation de 15 minutes). | Un « oui ». |
| **J7** | Installer chez le premier client. Demander, avec son accord écrit, un court témoignage vidéo. | **Premier client + première preuve.** |

Un premier client en 7 jours, c'est un objectif, pas une promesse. Ce qui compte : **20 contacts par jour, tous les jours**, et noter chaque réponse pour améliorer le message.

---

## 5. Sur les prix de ton document

Ton document parle de 300 à 1 000 $ (vente à distance) et de 1 000 à 5 000 $ (démo en appel). Mon avis :
- Pour le **premier client**, vise plutôt un prix d'essai plus bas, en échange d'un témoignage et du droit de montrer son cas. Tu gagnes la preuve qui fera vendre les suivants.
- Ajoute un **suivi au mois** (le système tourne, tu corriges, tu ajoutes des alertes) : c'est ce qui crée un revenu régulier.
- Les messages WhatsApp « modèles » sont facturés par Meta : **intègre ce coût** dans ton prix mensuel, en vérifiant le tarif du moment sur le site de Meta.

Les montants exacts sont à toi de les fixer **[À DÉCIDER]**.
