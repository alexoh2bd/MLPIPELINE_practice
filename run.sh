#!/bin/bash

# python -m venv venv
# source venv/bin/activate
# pip install -r requirements.txt

python3 src/data/cleaning.py

python3 src/models/model1/model.py

