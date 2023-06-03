#!/bin/bash

# Update package lists
sudo apt-get update

# Install PostgreSQL
sudo apt-get install -y postgresql postgresql-contrib

# Start the PostgreSQL service
sudo service postgresql start

# Switch to the PostgreSQL user
sudo su - postgres <<EOF
# Create the user
psql -c "CREATE USER climbdbuser WITH PASSWORD '$(dotenv -f .env get CLIMB_DB_PASS)';"

# Create the database with the new user as owner
psql -c "CREATE DATABASE climbdb OWNER climbdbuser;"

# Set client encoding to UTF-8
psql -c "UPDATE pg_database SET encoding = pg_char_to_encoding('UTF8') WHERE datname = 'climbdb';"

# Set timezone to UTC
psql -c "ALTER DATABASE climbdb SET timezone TO 'UTC';"

# Exit from postgres user
EOF
source venv/bin/activate
python manage.py makemigrations
python manage.py migrate
