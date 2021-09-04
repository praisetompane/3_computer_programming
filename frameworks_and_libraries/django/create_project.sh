'''
    accepts project name as parameter
'''
project=$1
mkdir $project
cp run_project.sh ./$project
cp create_app.sh ./$project
cd $project

echo "creating virtual environment $project and installing Django"
pipenv install django 
echo "done"

echo "creating Django project called $project"
pipenv run django-admin startproject $project .
echo "done"

