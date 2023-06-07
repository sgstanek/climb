#!/bin/bash
chmod +x *.sh

./pythonSetup.sh
./psqlSetup.sh

source venv/bin/activate
python setupSocial.py
