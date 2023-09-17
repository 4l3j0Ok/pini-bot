#!/bin/bash

python -m virtualenv .venv
./.venv/bin/python -m pip install -r requirements.txt
sudo apt install libffi-dev libnacl-dev python3.11-dev
