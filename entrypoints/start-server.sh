#!/bin/sh
echo "Создаю миграции..."
python src/manage.py makemigrations
echo "Отправляю миграции..."
python src/manage.py migrate
echo "Собираю статику..."
python src/manage.py collectstatic --no-input
echo "Запускаю сервер..."
cd src/
gunicorn core.wsgi --bind 0.0.0.0:1111 --workers 4 --threads 4 --reload