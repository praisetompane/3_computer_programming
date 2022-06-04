echo "installing go"
brew update
brew install go
echo "done"

echo "installing formatters"
go install mvdan.cc/gofumpt@latest
go get github.com/daixiang0/gci
echo "done"


# add to ~zshenv or bashrc
export GOPATH=$HOME/projects/go
export PATH=$PATH:/usr/local/go/bin:$GOPATH/bin
export GONOPROXY=none
