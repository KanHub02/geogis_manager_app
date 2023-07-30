#!/bin/sh
echo " --- Make migrations"
python src/manage.py makemigrations
echo " --- Migrate"
python src/manage.py migrate
echo " --- Collect static files"
python src/manage.py collectstatic --no-input
echo " --- Start server"
cd src/
gunicorn core.wsgi --bind 0.0.0.0:1111 --workers 4 --threads 4 --reload