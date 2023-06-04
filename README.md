# CLIMB

## Setup

A script is provided to setup the python venv and the psql database for this project. Run the python setup script first, because it will ask for the database passwrod which will then be used in the psql setup script. Here are the commands you should use to setup the python venv and database:

	chmod +x *.sh
	./setup.sh
	
Now the python enviorment and database should both be working, and the database migrations should be applied. You can start the server with:

	./run.sh

Create a superuser to access the admin tools:

	python manage.py createsuperuser
	
Then navigate to `/admin/` to access the admin portal

## Structure

The main project is called **climb**. The **pageManager** app handles displaying most of the site content. The **accountManager** app handles user accounts. The **dataManager** app handles non-user data, such as locations and routes. 

The project uses *PostgreSQL* as a database. The *Django* template language and *Bootstrap* are used for the front end. 
