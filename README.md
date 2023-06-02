# CLIMB
A script is provided to setup the python venv and the psql database for this project. Run the python setup script first, because it will ask for the database passwrod which will then be used in the psql setup script. Here are the commands you should use to setup the python venv and database:

	chmod +x psqlSetup.sh
	chmod +x pythonSetup.sh
	./pythonSetup.sh
	./psqlSetup.sh
	
Now the python enviorment and database should both be working, and the database migrations should be applied. You can start the server with:

	python manage.py runserver
