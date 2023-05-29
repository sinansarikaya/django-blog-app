#!/bin/bash

# Create a virtual environment and activate it
python -m venv venv
source venv/bin/activate

# Install required packages and run collectstatic
pip install -r requirements.txt
python manage.py collectstatic --noinput