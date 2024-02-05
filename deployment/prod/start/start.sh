#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input
gunicorn my_recipes_web_app.wsgi:application --bind 0.0.0.0:8000
