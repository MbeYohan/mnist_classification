# mnist_classification
Travaux Pratiques: De la conception au déploiement de  modèles de Deep Learning



TP Deep Learning  – Classification des chiffres MNIST

Ce projet est mon premier travail pratique en Deep Learning. Il a été réalisé dans le cadre du cours Réseau de Neurones Artificiels et Deep Learning II à l'ENSPY. L’objectif est de construire un modèle de réseau de neurones avec Keras pour reconnaître les chiffres manuscrits du jeu de données MNIST, puis de le suivre avec MLflow, et enfin de le déployer avec Flask et Docker.

 Ce que j’ai appris
- Comment créer un réseau de neurones avec Keras
- Comment utiliser Git et GitHub pour gérer mon projet
- Comment suivre les performances du modèle avec MLflow
- Comment créer une API avec Flask pour faire des prédictions
- Comment utiliser Docker pour conteneuriser mon application

Installation du projet
1. Cloner le projet :
   git clone https://github.com/MbeYohan/mnist_classification.git
   cd mnistclassification
2. Créer un environnement virtuel :
   python -m venv env
   source env/bin/activate  # ou .\env\Scripts\activate sur Windows
3. Installer les bibliothèques :
   pip install -r requirements.txt

Entraînement du modèle
Le fichier train_model.py contient le code pour entraîner le modèle sur les données MNIST.
Pour lancer l’entraînement :  python train_model.py
Le modèle est sauvegardé dans le fichier mnist_model.h5.

Suivi avec MLflow
J’ai utilisé MLflow pour enregistrer les paramètres et les performances du modèle.
Pour lancer l’interface MLflow :  mlflow ui
Puis ouvrir http://localhost:5000 dans le navigateur.

API Flask
Le fichier app.py permet de faire des prédictions avec le modèle via une API web.
Pour lancer l’API :python app.py
On peut envoyer une image sous forme de tableau (1x784) en JSON pour obtenir une prédiction.

🐳 Docker
J’ai créé un fichier Dockerfile pour conteneuriser mon application.
Pour construire l’image :  docker build -t mnist-api 
Pour lancer le conteneur :  docker run -p 5000:5000 mnist-api
