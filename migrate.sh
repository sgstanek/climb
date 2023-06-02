#!/bin/bash

# This script performs database migrations

source venv/bin/activate

python manage.py makemigrations
python manage.py migrate
