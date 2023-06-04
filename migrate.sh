#!/bin/bash

# This script performs database migrations

source venv/bin/activate

python manage.py makemigrations accountManager
python manage.py makemigrations dataManager
python manage.py makemigrations pageManager
python manage.py makemigrations

python manage.py migrate
