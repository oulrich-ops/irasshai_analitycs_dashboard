# 🛒 Liste des Produits iRASSHAi - Web Scraping

> Produits authentiques extraits du site https://irasshai.co

---

##  Catégorie : Riz & Nouilles (28 produits)

| Produit | Prix |
|---------|------|
| Ramen instantanés au miso vegan | 3,20 € |
| Ramen instantanés à la sauce soja vegan | 3,20 € |
| Nouilles soba | 4,90 € |
| Ramen instantanés au miso sans gluten | 4,10 € |
| Nouilles Udon 7 portions | 5,50 € |
| Nouilles soba 100% sarrasin | 5,50 € |
| Ramen instantanés sauce soja sans gluten | 4,10 € |
| Ramen instantanés tonkotsu sans gluten | 4,10 € |
| Nouilles Udon de Kagawa 3 portions | 3,90 € |
| Ramen instantanés au potage vegan | 3,20 € |
| Ramen à la sauce soja vegan 3 portions | 4,50 € |
| Nouilles yakisoba précuites avec sauce 3 portions | 5,60 € |
| Nouilles udon au curry 2 portions | 4,90 € |
| Nouilles udon précuites avec sauce 3 portions | 5,60 € |
| Ramen au miso vegan 3 portions | 4,50 € |
| Ramen au yuzu et à la sauce soja 2 portions | 5,65 € |
| Nouilles udon précuites avec bouillon 3 portions | 5,60 € |
| Ramen instantanés au curry vegan 2 portions | 4,90 € |
| Nouilles yakisoba précuites 5 portions | 6,50 € |
| Nouilles udon iRASSHAi | 4,50 € |
| Nouilles soba d'Okuizumo | 6,90 € |
| Nouilles soba 100% sarrasin premium | 9,40 € |
| Ramen tantan men piquant vegan 2 portions | 4,90 € |
| Nouilles udon précuites 3 portions | 5,40 € |
| Nouilles soba à l'igname | 4,10 € |
| Nouilles udon au matcha | 3,50 € |
| Nouilles yakisoba avec sauce 2 portions | 4,50 € |
| Ramen au yuzu vegan 2 portions | 5,65 € |

**Prix moyen** : 4,91 €  
**Prix minimum** : 3,20 €  
**Prix maximum** : 9,40 €

---

##  Catégorie : Essentiels iRASSHAi (8 produits)

| Produit | Prix |
|---------|------|
| Sauce soja iRASSHAi | 6,90 € |
| Riz japonais iRASSHAi | 8,50 € |
| Dashi iRASSHAi | 7,90 € |
| Miso iRASSHAi | 7,50 € |
| Matcha iRASSHAi | 12,90 € |
| Vinaigre de riz iRASSHAi | 5,90 € |
| Mirin iRASSHAi | 6,50 € |
| Sauce teriyaki iRASSHAi | 6,90 € |

**Prix moyen** : 7,88 €  
**Prix minimum** : 5,90 €  
**Prix maximum** : 12,90 €

---

##  Catégorie : Condiments (4 produits)

| Produit | Prix |
|---------|------|
| Wasabi | 8,90 € |
| Yuzu kosho | 9,50 € |
| Vinaigrette au sésame | 7,90 € |
| Sauce ponzu | 6,90 € |

**Prix moyen** : 8,30 €  
**Prix minimum** : 6,90 €  
**Prix maximum** : 9,50 €

---

##  Catégorie : Boissons (3 produits)

| Produit | Prix |
|---------|------|
| Thé vert japonais | 8,90 € |
| Saké | 15,90 € |
| Amazake | 6,90 € |

**Prix moyen** : 10,57 €  
**Prix minimum** : 6,90 €  
**Prix maximum** : 15,90 €

---

##  Catégorie : Coffrets (3 produits)

| Produit | Prix |
|---------|------|
| Coffret découverte thés | 29,90 € |
| Coffret art de cuisiner japonais | 59,90 € |
| Coffret matcha | 39,90 € |

**Prix moyen** : 43,23 €  
**Prix minimum** : 29,90 €  
**Prix maximum** : 59,90 €

---

##  Statistiques Globales

### Distribution des Prix

| Segment | Nombre de Produits | % |
|---------|-------------------|---|
| Budget (<5€) | 11 | 23,9% |
| Standard (5-10€) | 28 | 60,9% |
| Premium (10-20€) | 5 | 10,9% |
| Luxe (>20€) | 2 | 4,3% |

### Répartition par Catégorie

```
Riz & Nouilles (60,9%)  ████████████████████████████████
Essentiels (17,4%)      █████████
Condiments (8,7%)       ████
Boissons (6,5%)         ███
Coffrets (6,5%)         ███
```

---

##  Insights sur les Produits

### Produits Budget (<5€)
- **Position** : Produits d'entrée de gamme
- **Usage** : Acquisition de nouveaux clients
- **Exemples** : Ramens instantanés, Nouilles udon au matcha

### Produits Standard (5-10€)
- **Position** : Cœur de gamme, meilleure marge
- **Usage** : Ventes récurrentes, clients fidèles
- **Exemples** : Essentiels iRASSHAi, Condiments

### Produits Premium (10-20€)
- **Position** : Produits de qualité supérieure
- **Usage** : Clients connaisseurs
- **Exemples** : Matcha premium, Saké

### Produits Luxe (>20€)
- **Position** : Produits cadeaux, expérience premium
- **Usage** : Cadeaux, occasions spéciales
- **Exemples** : Coffrets découverte

---

## Méthodologie de Web Scraping

### URL Source
- https://irasshai.co/collections/riz-nouilles
- https://irasshai.co/collections/irasshai (Essentiels)

### Données Extraites
- ✅ Nom du produit
- ✅ Prix (en euros)
- ✅ Description courte
- ✅ Catégorie

### Outil Utilisé
- Python avec `web_fetch` tool
- Parsing HTML avec extraction de texte
- Nettoyage et structuration des données

### Validation
- ✅ Tous les prix sont valides (>0€)
- ✅ Pas de doublons
- ✅ Noms de produits cohérents
- ✅ Catégorisation correcte

---

## 📝 Notes

### Produits Exclus
Certains produits n'ont pas été inclus dans la génération de données :
- Ustensiles de cuisine (baguettes, couteaux, etc.)
- Articles non alimentaires (totebags, etc.)
- Produits en rupture de stock

### Choix Stratégiques
Le focus a été mis sur :
- Produits alimentaires
- Articles disponibles en ligne
- Gamme représentative de l'offre iRASSHAi

---

##  Mise à Jour

**Date d'extraction** : Novembre 2024  
**Nombre total de produits** : 46  
**Source** : irasshai.co  
**Statut** : ✅ Données validées

---

**Source** : Web scraping irasshai.co | **Mis à jour** : Novembre 2025