#1) Need to have virtualenv (ubuntu):
sudo apt-get install -y python3-venv
python3 -m pip install virtualenv

#2) New virtual environment:
python3 -m virtualenv venv

#3) Venv activation:
source venv/bin/activate

#4) Install all requirements inside virtualenv using setup.py and setup.cfg:
pip3 install .

#5) Update default_build path in ./codegen/config.ini

# Additional nice to know:
# Venv deactivation:
deactivate
# Info:
pip list
# Update requirements:
pip3 freeze > ./requirements/requirements.txt

#-------------GENERATE_USECASE-------------
#Run code generator:
python3 -m codegen

#-------------UNIT_TESTS-------------
#RUN TESTS
python3 -m unittest

#-------------RUN_FLASK_TEST-------------
#RUN FLASK
python -m flask run -h 0.0.0.0

