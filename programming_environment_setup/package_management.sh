sudo apt-get install software-properties-common
sudo apt-add-repository -y ppa:rael-gc/rvm
sudo apt-get update
sudo apt-get install rvm
sudo usermod -a -G rvm $USER
rvm install ruby-2.6.8

echo "installing brew"
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
echo "done"

install_dir="/home/linuxbrew/.linuxbrew/bin"
echo $install_dir
z_shell_config=~/.zshrc
bash_config=~/.bashrc
z_shell_environment=~/.zshenv #sub with ~/.bashrc if you use bash
git_facade=~/.git_facade

if [ -f "$z_shell_config" ]; then
    echo "" >> $z_shell_config
    echo "export PATH=$install_dir:$"PATH"" >> $z_shell_config
    echo "Updated Z Shell config"
    
fi

if [ -f "$bash_config" ]; then
    echo "export PATH=$install_dir:$"PATH"" >> $bash_config
    echo "Updated Bash config"
    
fi

