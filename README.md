🛒 E-Commerce Sales Prediction Web App

📌 Description du projet

Ce projet est une application Machine Learning de bout en bout permettant de prédire les ventes d’un produit e-commerce à partir de plusieurs caractéristiques produit.

L’objectif est de combiner :

Analyse exploratoire des données
Construction d’un modèle prédictif
Déploiement d’une application web interactive

L’utilisateur saisit les informations du produit, puis le modèle estime automatiquement le montant prédit des ventes.

📸 Aperçu de l’application

![capture](ven1.png)

🎯 Objectifs

Analyser les données de ventes e-commerce
Identifier les variables influençant les ventes
Construire un modèle de prédiction performant
Déployer le modèle dans une application Flask
Fournir des prédictions en temps réel via une interface simple et intuitive

🧠 Pipeline Machine Learning

1. Préparation des données
Nettoyage des données
Sélection des variables
Encodage des variables catégorielles
Transformation des données
2. Analyse exploratoire (EDA)
Distribution des ventes
Analyse par catégorie
Analyse par région
Corrélations entre variables

4. Entraînement du modèle

Plusieurs modèles de régression ont été testés.
Le modèle retenu est :

✅ XGBoost Regressor

Choisi pour :

sa haute performance sur données tabulaires
sa robustesse
sa précision de prédiction
4. Déploiement

Le modèle entraîné a été exporté puis intégré dans une application web développée avec Flask.

🛠 Technologies utilisées

Analyse & Machine Learning

Python
Pandas
NumPy
Scikit-learn
XGBoost

Visualisation

Matplotlib
Seaborn

Déploiement Web

Flask
HTML
CSS
