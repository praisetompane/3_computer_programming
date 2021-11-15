echo "installing open JDK 11"
brew install --cask adoptopenjdk
echo "done"


echo 'export PATH="/usr/local/opt/openjdk@11/bin:$PATH"' >> ~/.zshrc