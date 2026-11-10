# Les 6 modèles de messages WhatsApp à créer chez Meta

À créer dans **WhatsApp Manager > Modèles de message > Créer**.
Pour les six : catégorie **Utilitaire** (Utility), langue **Français (fr)**, nom exactement comme ci-dessous (en minuscules, avec le tiret bas).
Les `{{1}}`, `{{2}}`… sont remplis par n8n, dans cet ordre. Meta demande un exemple pour chaque variable : utiliser ceux donnés.

---

## 1. `nouvelle_commande`

```
Nouvelle commande reçue. Client : {{1}} ({{2}}). Produit : {{3}}, quantité {{4}}. Montant : {{5}}. Adresse : {{6}}. Stock restant : {{7}}. Bonne journée !
```

Exemples : {{1}} Jean · {{2}} 0810000000 · {{3}} Riz 25 kg · {{4}} 2 · {{5}} 72 · {{6}} Gombe · {{7}} 18 sacs

## 2. `alerte_stock_bas`

```
Alerte stock de votre boutique : {{1}} pour {{2}} (code {{3}}). Il reste {{4}} et votre seuil d'alerte est {{5}}. Pensez à réapprovisionner ce produit auprès de votre fournisseur.
```

Exemples : {{1}} Stock bas · {{2}} Riz 25 kg · {{3}} P001 · {{4}} 3 sacs · {{5}} 5

## 3. `bilan_du_soir`

```
Bilan de votre boutique du {{1}} : {{2}} commande(s), ventes {{3}}, marge brute {{4}}. Commandes pas encore livrées : {{5}}. En rupture : {{6}}. À commander : {{7}}. Bonne soirée !
```

Exemples : {{1}} 06/10/2026 · {{2}} 12 · {{3}} 450 · {{4}} 80 · {{5}} 3 · {{6}} Huile 5 L · {{7}} Riz 25 kg (reste 3)

## 4. `confirmation_commande` (envoyé au client)

```
Bonjour {{1}}, votre commande est bien enregistrée : {{2}}, quantité {{3}}, montant {{4}}. Nous vous recontactons pour la livraison. Merci pour votre confiance !
```

Exemples : {{1}} Jean · {{2}} Riz 25 kg · {{3}} 2 sacs · {{4}} 72

## 5. `arrivage_stock`

```
Marchandise reçue dans votre boutique : {{1}}, quantité {{2}}, fournisseur {{3}}. Le stock est maintenant de {{4}}. Bonne journée !
```

Exemples : {{1}} Huile 5 L · {{2}} 10 bidons · {{3}} Grossiste B · {{4}} 11 bidons

## 6. `stock_du_matin`

```
Bonjour, point du stock du {{1}} : {{2}} produit(s) à réapprovisionner. Liste : {{3}}. En rupture : {{4}}. Bonne journée !
```

Exemples : {{1}} 11/10/2026 · {{2}} 2 · {{3}} Riz 25 kg : 8 sacs chez Grossiste A ; Huile 5 L : 8 bidons · {{4}} Huile 5 L

---
Attention au mot « recommander » : Meta le lit comme « conseiller un produit » et classe le modèle en Marketing (plus cher). Utiliser « réapprovisionner ». Le premier modèle `alerte_stock` a été reclassé en Marketing pour cette raison, d'où le nom `alerte_stock_bas`.

Si Meta refuse un modèle, il donne la raison : envoie-la au chat « Produits & accompagnements », on corrige le texte. Si tu changes un nom de modèle ou l'ordre des variables, il faut changer aussi le nœud WhatsApp dans n8n.
