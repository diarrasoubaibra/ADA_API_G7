    Ce projet est une API REST qui permet de gérer un forum, des sujets (subject), et des messages. 
Il a été développé avec Django et Django REST Framework (DRF), en utilisant une base de données PostgreSQL.
                                                                                          
                                                                                          
    Prérequis

Python 3.12
Django 5.x ou supérieur
PostgreSQL installé et configuré
Git (optionnel)

    Étapes d'installation

# Cloner le projet (si applicable)
Si vous avez un dépôt Git, utilisez la commande suivante pour cloner le projet :

- git clone https://github.com/diarrasoubaibra/ADA_API_G7.git

si vous avez creer un dossier pour pouvoir mettre le projet dedans alors utiliser la commande ci dessous pour naviguer a l'interrieur du projet 
- cd NomDossier

# Créer et activer un environnement virtuel
Créer l'environnement virtuel
- python -m venv env

Activer l'environnement virtuel
- .\env\Scripts\activate

# Installer les dépendances
Installez les dépendances du projet, qui sont listées dans le fichier requirements.txt
naviguer vers le dossier de notre projet
cd src ensuite tapé cette commande
# Installer les dépendances
- pip install -r requirements.txt                 ~ pour installer les dépendance du projet

# Configurer la base de données PostgreSQL
Créez une base de données PostgreSQL pour votre projet. Connectez-vous à PostgreSQL et exécutez la commande suivante pour créer une base de données :
- CREATE DATABASE metab_db;


DATABASES = {

    'default': {
    
        'ENGINE': 'django.db.backends.postgresql',
        
        'NAME': 'metab_db',
        
        'USER': 'votre_nom_utilisateur',
        
        'PASSWORD': 'votre_mot_de_passe',
        
        'HOST': 'localhost',
        
        'PORT': '5432',
        
    }
}

# Appliquer les migrations
Après avoir configuré la base de données, appliquez les migrations pour créer les tables nécessaires.

-python manage.py makemigrations

ensuite entrer cette commande

-python manage.py migrate

# Lancer le serveur de développement
Exécutez le serveur de développement pour démarrer l'API.
- python manage.py runserver

Vous pouvez maintenant accéder à l'API à l'adresse (https://documenter.getpostman.com/view/29787497/2sAXqp94CX).
