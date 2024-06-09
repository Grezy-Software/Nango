#! /usr/bin/env bash

# deactivate
sudo apt install git-flow
sudo apt install python3
sudo apt install python3.12
sudo apt install python3.12-distutils
pip3 install --upgrade pip

rm -rf .venv
pip install virtualenv
python3 -m virtualenv .venv --python=python3.12
printf "\n===============================================\nVirtual python environment has been created.\n"
source .venv/bin/activate
printf "Virtual python environment has been activated.\n"
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.12
pip install pip-tools
printf "Compiling requirements... This may take a few minutes.\n"
pip-compile ./requirements/development.txt --output-file ./full-requirements.txt --resolver=backtracking --strip-extras
pip install -r ./full-requirements.txt
pre-commit install
printf "Done installing requirements for local .venv!\nHave fun coding!\n"