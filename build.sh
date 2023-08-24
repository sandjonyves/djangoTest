#! /bin/bash

# build the project

echo "Building the project..."

python3.9 -m pip install requirements.txt

echo "Make Migration..."
python3.9 manage.py makemigrate --noinput
python3.9 manage.py migrate --noinput

echo "Collect Static"
python3.9 manage.py collectstatic --clear

