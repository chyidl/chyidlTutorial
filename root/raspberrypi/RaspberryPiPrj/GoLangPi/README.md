Install Go Lang on Raspberry Pi
===============================

Install Go Lang on MacOS with Homebrew
--------------------------------------
```
$ brew install go 

# export paths save them in .zshrc or .bashrc files for easy use.
# Go development 
export GOPATH="${HOME}/.go"
export GOROOT="$(brew --prefix golang)/libexec"
export PATH="$PATH:${GOPATH}/bin:${GOPATH}/bin"

test -d "${GOPATH} || mkdir "${GOPATH}"
test -d "${GOPATH}/src/github.com" || mkdir -p "${GOPATH}/src/github.com"

# bunch dev tools 
go get golang.org/x/tools/cmd/godoc
go get github.com/golang/lint/golint
```