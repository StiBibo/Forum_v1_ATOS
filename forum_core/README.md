# API REST de Gestion de Forum avec Django

## Description

Ce projet consiste à développer une API REST pour la gestion d'un forum en utilisant le framework Django. L'objectif sera d'implémenter les fonctionnalités de base du forum sans gestion des utilisateurs et se familiariser avec Django et les principes RESTful

## Fonctionnalités

- Création d'un nouveau forum
- Liste des forums existants
- Récupération des détails d'un forum spécifique
- Création de sujets dans un forum
- Liste de sujet par forum 
- Récupération des détails d'un sujet
- Ajout de messages à un sujet
- Liste des messages d'un sujet
- Liste de message par sujet 

## Technologies utilisées

- Python 3.12
- Django 5
- Implémenter une architecture RESTful
- Utiliser la base de données PostgreSQL
- Documenter l'API avec Postman

## Prérequis

Avant de démarrer, assurez-vous d'avoir installé les éléments suivants :
- Python 3.x
- PostgreSQL


Vous pouvez créer un environnement virtuel avec la commande suivante :
- python -m venv env

activer l'environement virtuel
- source env/Scripts/activate

- Clonage du Projet
Pour commencer, clonez le dépôt du projet à l'aide de Git. 
Utilisez la commande suivante pour télécharger le code source : git clone https://github.com/StiBibo/Forum_v1_ATOS.git

- Ensuite, accédez au répertoire du projet cloné : cd Forum_v1_ATOS


Installez les dépendances nécessaires en utilisant le fichier requirements.txt :
- pip install -r requirements.txt

Assurez-vous que PostgreSQL est installé et en cours d'exécution. Créez une base de données pour votre projet :
- Modifiez ensuite le fichier settings.py pour configurer PostgreSQL comme base de données (avec les informations propre a votre base de donné)

 Exemple:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'forum_BD',
        'USER': 'postgres',
        'PASSWORD': 'ella',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


Appliquez les migrations pour initialiser la base de données :
- python manage.py makemigrations
- python manage.py migrate


# Lancez le serveur local avec la commande suivante :
python manage.py runserver


## Documentation de l'API
Utilisez Postman. Importez les endpoints et leurs descriptions pour permettre une visualisation et un test rapide des fonctionnalités.
- Importer le fichier "Forum V1.postman_collection" dans Postman
