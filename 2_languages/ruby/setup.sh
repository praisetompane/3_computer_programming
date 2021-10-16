echo "installing ruby"
brew update
brew install ruby
echo "done"

mkdir $HOME/gems

install_dir="/home/linuxbrew/.linuxbrew/lib/ruby/gems/3.0.0/bin"

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

echo "installing jekyll"
gem install jekyll bundler
echo "done"

#required for the bundler
brew install gcc@5
