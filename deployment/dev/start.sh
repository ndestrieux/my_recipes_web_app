#!/bin/sh

python manage.py migrate --no-input
python -u manage.py runserver 0.0.0.0:8000
