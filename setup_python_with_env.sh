#!/usr/bin/env bash

##################################################################################################################
# Author 	: 	Piotr Skalski
# Website 	: 	https://github.com/SkalskiP
##################################################################################################################

sudo apt-get update
sudo apt-get install python-dev
sudo apt-get install python-pip
sudo apt-get install libjpeg8-dev
sudo ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib
pip install pillow
sudo apt-get build-dep python-imaging
sudo pip install virtualenv  
virtualenv -p python3 .env       # Create a virtual environment
source .env/bin/activate         # Activate the virtual environment
pip install -r requirements.txt  # Install dependencies
deactivate
echo "**************************************************"
echo "*****         End of Python Setup         ********"
echo "**************************************************"
echo ""
echo "If you had no errors, You can proceed to work with your virtualenv as normal."
echo "(run 'source .env/bin/activate' in your assignment directory to load the venv,"
echo " and run 'deactivate' to exit the venv. See assignment handout for details.)"
