#!/bin/bash


export PYTHONUNBUFFERED=1
export VIRTUAL_ENV=/home/django/venv
export PATH="/home/django/venv/bin:$PATH"

#python manage.py makemigrations --no-input && python manage.py migrate --no-input
#python manage.py collectstatic --no-input

gunicorn -c gunicorn.conf.py