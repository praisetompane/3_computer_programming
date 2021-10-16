brew install zsh

echo "installing oh-my-szh"
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
echo "done"

chsh -s $(which zsh)