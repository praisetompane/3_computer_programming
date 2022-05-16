echo "installing python"
brew update
brew install python
echo "done"

echo "installing pip"
python3 -m ensurepip --upgrade
echo "done"

echo "installing virtualenv"
pip3 install virtualenv
echo "installing virtualenv"