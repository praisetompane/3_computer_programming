#!/bin/zsh
'''
    quick utility to create Django app
    Example:
    $ ./create_app.sh my_app
'''

app=$1
pipenv run python manage.py startapp $app