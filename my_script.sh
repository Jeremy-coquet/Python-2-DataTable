#!/bin/bash

Project=$(basename "$(pwd)")

if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed. Please install Python 3 first."
    exit 1
fi

python3 -m venv venv_$Project

source "venv_$Project/bin/activate"

sudo apt-get update
sudo apt-get install -y libpq-dev

if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "requirements.txt file is missing."
    deactivate
    exit 1
fi

echo "Virtualenv created and dependencies installed."
echo "To activate the virtualenv later, run: source venv_$Project/bin/activate"
