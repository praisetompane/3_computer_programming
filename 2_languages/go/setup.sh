echo "installing go"
brew update
brew install go
echo "done"

echo "installing goimports"
go install golang.org/x/tools/cmd/goimports@latest
echo "done"
