#! /usr/bin/env bash

# deactivate
sudo apt install git-flow
sudo apt install python3
sudo apt install python3.11
sudo apt install python3.11-distutils
pip3 install --upgrade pip

rm -rf .venv
pip install virtualenv
python3 -m virtualenv .venv --python=python3.11
printf "\n===============================================\nVirtual python environment has been created.\n"
source .venv/bin/activate
printf "Virtual python environment has been activated.\n"
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11
pip install pip-tools
printf "Compiling requirements... This may take a few minutes.\n"
pip-compile ./setup/requirements/requirements.txt --output-file ./setup/requirements/full-requirements.txt --resolver=backtracking --strip-extras
pip install -r ./setup/requirements/full-requirements.txt
pre-commit install
printf "Done installing requirements for local .venv!\nHave fun coding!\n"