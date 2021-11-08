# Django Recipes

This is a website, based on django, to store cooking recipes


## References 

To start the project I followed the [sibtc's tutorial](https://simpleisbetterthancomplex.com/tutorial/2021/06/27/how-to-start-a-production-ready-django-project.html)
https://developer.mozilla.org/fr/docs/Learn/Server-side/Django/Models


## Inspiration
https://github.com/vitorfs/bootcamp/blob/master/config/settings/base.py
https://github.com/vitorfs/parsifal/blob/dev/parsifal/settings/base.py


## What i did:

1. use the tree organisation of sibtc
1. use python decouple
2. Add an account app to fix Django User Model : https://simpleisbetterthancomplex.com/article/2021/07/08/what-you-should-know-about-the-django-user-model.html
3. add recipe application following mozzilla tutorial


## historique des commandes

mkdir django-recipes
cd django-recipes/
git clone https://github.com/cedlerouge/django-recipes.git
# préparation environnement python
virtualenv venv
source venv/bin/activate
pip install django
django-admin startproject recipes .
mkdir -p recipes/{locale,static,templates}
# préparation des environnements de développement
mkdir requirements
touch requirements/{base,local,production,tests}.txt
pip install dj-database-url
pip install psycopg2-binary
pip install python-decouple
pip freeze > requirements/base.txt
pip install black coverage factory-boy flake8 isort tox
pip freeze > requirements/tests.txt
pip install django-debug-toolbar
pip install ipython
vim requirements/local.txt
pip install gunicorn sentry-sdk
pip freeze | grep "sentry\|guni" > requirements/production.txt
mkdir recipes/settings
touch recipes/settings/{__init__,base,local,production,tests}.py
rm recipes/settings.py
# test des environnement après avoir modifier le ficher manage.py pour lancer par défaut l'environnement local
python manage.py runserver
python manage.py runserver --settings=recipes.settings.production
python manage.py runserver --settings=recipes.settings.tests
mkdir recipes/apps
touch recipes/apps/__init__.py
# creation de l'application accounts pour changer le comportement du modèle User de django
mkdir recipes/apps/accounts
django-admin startapp accounts recipes/apps/accounts
python manage.py makemigrations recipes.apps.accounts --empty --name="postgres_extensions"
# création de l'application recipe
python manage.py startapp recipe recipes/apps/recipe
## creation des objets du modeles (recipe/models.py)
python manage.py makemigrations
## création des objets de l'administration (recipe/admin.py)
# creation du superutilisateur
python manage.py createsuperuser



## Pages pour l'application recipe

* /recipe/
* /recipe/id
* /recipe/ingredient
* /recipe/ingredient/id


## ideas : add a notion of group to share recipe into a group or publicly