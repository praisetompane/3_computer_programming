#!/bin/zsh
'''
    quick utility to create Django project.
    accepts project name as parameter
    Example:
    $ ./create_project.sh my_app
'''

project=$1
mkdir $project
cp run_project.sh ./$project

cd $project

"laying out root folder"
touch app.py

touch README.md
echo "#" $project >> ./README.md

touch setup.sh
touch requirements.txt
"done"

echo "creating app folder"
mkdir app
cd ./app
touch __init__.py
echo "done"


