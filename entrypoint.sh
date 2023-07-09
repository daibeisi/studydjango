#!/bin/bash


export PYTHONUNBUFFERED=1
export VIRTUAL_ENV=/home/django/venv
export PATH="/home/django/venv/bin:$PATH"


gunicorn -c gunicorn.conf.py