# 🛒 E-Commerce Sales Prediction with Flask & XGBoost

## 📌 Description du projet

Ce projet est une application web développée avec **Python** et **Flask** permettant de **prédire les ventes (Sales Prediction)** d’un produit e-commerce grâce au **Machine Learning**.

Le modèle de prédiction utilise **XGBoost**, sélectionné comme meilleur modèle après comparaison avec plusieurs algorithmes (**Linear Regression, Random Forest et XGBoost**).

L’utilisateur entre les caractéristiques du produit via une interface web interactive, puis l’application prédit automatiquement le montant estimé des ventes.

---

## 🚀 Fonctionnalités

- Prédiction des ventes en temps réel
- Interface web simple et intuitive
- Formulaire interactif
- Encodage automatique des variables catégorielles
- Chargement du modèle sauvegardé (.pkl)
- Affichage instantané du résultat

---

## 🛠️ Technologies utilisées

- **Python**
- **Flask**
- **Pandas**
- **Scikit-learn**
- **XGBoost**
- **Joblib**
- **HTML**
- **CSS**

---

## 📊 Variables utilisées

### Variables d'entrée :

- **Quantity** → Quantité commandée
- **Weight** → Poids du produit
- **Category** → Catégorie produit
- **Region** → Région de vente

### Variable cible :

- **Sales** → Montant des ventes prédit

---

## 🤖 Modèles testés

| Modèle | R² Score | MAE | RMSE |
|--------|----------|------|------|
| Linear Regression | 0.642 | 30.713 | 101.048 |
| Random Forest | 0.770 | 10.424 | 81.028 |
| **XGBoost** | **0.789** | **11.596** | **77.480** |

### ✅ Meilleur modèle sélectionné : XGBoost

## 📈 Insights principaux

### 1. Le modèle XGBoost offre les meilleures performances
- **R² = 0.789** → bonne capacité à expliquer la variation des ventes.
- **RMSE = 77.48** → erreur globale la plus faible parmi les modèles testés.
- XGBoost a été choisi comme modèle final pour la prédiction.

### 2. La quantité influence fortement les ventes
- Plus la **quantité commandée** augmente, plus le montant des ventes prédit augmente.
- Cette variable a un impact direct sur le chiffre d’affaires.

### 3. Certaines catégories génèrent plus de revenus
- Les catégories comme **Electronics** et **Food** peuvent produire des ventes plus élevées.
- La catégorie produit est un facteur important dans la prédiction.

### 4. La région peut affecter les ventes
- Les ventes peuvent varier selon la région (**North, South, East, West**).
- Certaines régions montrent un potentiel commercial plus important.

### 5. Le poids du produit peut influencer le prix final
- Le **Weight** peut être lié au coût ou à la valeur du produit.
- Son impact contribue à améliorer la précision du modèle.

### 6. Application pratique
- Automatiser l’estimation des ventes avant commercialisation.
- Aider à la prise de décision commerciale.
- Optimiser la gestion des stocks et la stratégie produit.
- ## 📷 Capture d’écran

![Capture écran](appEcommerceSales.png)

