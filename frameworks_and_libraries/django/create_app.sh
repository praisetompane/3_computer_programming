#!/bin/zsh
#quick utility to create Django app

app=$1
pipenv run python manage.py startapp $app