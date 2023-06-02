#!/bin/bash

# Ensure python3 and pip are installed
sudo apt-get update
sudo apt-get install -y python3 python3-pip python3-venv

# Recreate the virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the dependencies from requirements.txt
pip install -r requirements.txt

python - << END
import getpass
from dotenv import set_key

# Ask for password
password = getpass.getpass()

# Write password to .env file
set_key(".env", "CLIMB_DB_PASS", password)

print("Password saved in .env file.")
END

echo "Python setup complete."
