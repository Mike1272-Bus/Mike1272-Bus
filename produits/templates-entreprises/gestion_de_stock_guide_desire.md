# Template « Gestion de stock » : fiche pour Desire

Fichier : `gestion_de_stock.xlsx` (marche dans Excel, l'appli Excel sur téléphone et Google Sheets).

## Ce qu'il y a dedans (4 onglets)

| Onglet | Rôle |
|---|---|
| Mode d'emploi | Les explications pour le commerçant, en « vous » |
| Tableau de bord | Valeur du stock, produits à commander, en rupture, ventes, achats et marge du mois. Devise ($ ou FC) et mois au choix |
| Produits | La liste des produits (200 lignes) : prix d'achat, prix de vente, stock de départ, seuil d'alerte. Le stock actuel et l'état (OK / À commander / Rupture) se calculent seuls |
| Mouvements | Une ligne par entrée ou sortie (1 000 lignes). Code produit et type en liste déroulante ; nom, prix et montant automatiques |

Couleurs : **jaune** = le commerçant remplit, **gris** = calculé, on n'y touche pas.

## Comment l'installer chez un commerce (environ 30 min)

1. Supprimer les lignes EXEMPLE (onglets Produits et Mouvements).
2. Avec le commerçant : saisir ses produits, ses prix, et **compter le stock du jour** (stock de départ).
3. Choisir le seuil d'alerte de chaque produit avec lui (« à partir de combien vous recommandez ? »).
4. Lui faire saisir 2 ou 3 vraies ventes devant toi, puis lui montrer le Tableau de bord.
5. Lui laisser le Mode d'emploi. Rappel au bout de 3 jours : « Vous arrivez à noter les ventes ? »

## Pour l'adapter avec Claude

Exemples de demandes : « ajoute une colonne Fournisseur », « fais une version pour une pharmacie avec la date de péremption », « passe à 500 produits ». Le fichier a été généré par script : demande au chat « Produits & accompagnements » de le régénérer avec la modification.

## Limites à dire honnêtement au client

- Un seul point de vente par fichier.
- La marge affichée est une marge brute : elle ne compte pas le loyer, le transport ni les salaires.
- Le tableau ne remplace pas un comptage : faire un inventaire de temps en temps et corriger avec une ligne Entrée ou Sortie.
