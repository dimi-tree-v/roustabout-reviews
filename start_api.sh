#!/usr/bin/env bash

#. ./venv/bin/activate
. ./venv/Scripts/activate

cd roustabout_reviews
DJANGO_SETTINGS_MODULE="base.settings"
python manage.py migrate
# python manage.py makemigrations --check --dry-run
python manage.py runserver localhost:8000
