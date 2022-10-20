#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
python manage.py makemigrations
python manage.py collectstatic --no-input
python manage.py migrate
#esto crea un super usuario la primera vez en render
#export DJANGO_SUPERUSER_EMAIL=dipa@dipa.com
#export DJANGO_SUPERUSER_PASSWORD=dipa1983
#python manage.py createsuperuser --no-input 
