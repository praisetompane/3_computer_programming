echo "installing python"
brew install python
echo "done"

echo "installing pip"
python3 -m ensurepip --upgrade
echo "done"

echo "installing pipenv"
pip3 install pipenv
echo "installing pipenv"