Introduction to Golang
======================
```
Creators:
    Robert Griesemar、Rob Pike、Ken Thompson

Why a New Language?
    Python + Java + C/C++ 
    Python: Easy to use, but slow 
    Java: Increasingly complex type system
    C/C++: Complex type system Slow compile times
    Go: Concurrency

Go (golang)
    Strong and statically typed 
    Excellent community 
    Key features
        Simplicity 
        Fast compile times 
        Garbage collected 
        Built-in concurrency 
        Compile to standalone binaries 

https://golang.org
https://golang.org/doc/
https://golang.org/doc/effective_go.html 
https://golang.org/pkg/
https://golang.org/project/
https://golang.org/help/
https://golangbridge.org/
https://play.golang.org/ -- The Go Playground 
```

Setting Up a Development Environment 
------------------------------------
```
1. Download golang binary
$ wget https://dl.google.com/go/go1.12.6.linux-amd64.tar.gz 

2. Download the archive and extract it into /usr/local, creating a Go tree in /usr/local/go. 
$ sudo tar -C /usr/local -xzf go1.12.6.linux-amd64.tar.gz

3. Add /usr/local/go/bin to the PATH environment variable.adding this line to your /etc/profile (for a system-wide installation) or $HOME/.profile
export GOROOT=/usr/local/go
export PATH=$PATH:$GOROOT/bin

4. Check Go Version 
$ go version 

5. Set GOPATH 
export GOPATH=/home/chyiyaqing/golib
export PATH=$PATH:$GOPATH/bin 

6. Test GOPATH 
$ go get github.com/nsf/gocode 

7. Create MyGoCode 
$ export GOPATH=$GOPATH:/home/chyiyaqing/MyGoCode
$ mkdir MyGoCode
$ mkdir -p MyGoCode/bin MyGoCode/src MyGoCode/pkg 

Download and Install Visual Studio Code http://code.visualstudio.com 
Click Extensions
$ go get -v github.com/golang/lint/golint 


```

Install Golang on MacOS With Homebrew!
--------------------------------------
```
Installing Go via the Terminal 
$ brew install go 

Create your Go folder via the terminal && change directory into 
$ mkdir MyGoCode && cd MyGoCode 

Go requires a specific folder structure in order to manage local packages and code
$ mkdir bin pkg src 

Setup the GOPATH environment variable
$ vim ~/.zshrc 
# Keep in mind that $HOME is equal to "~" AKA /Users/your_username. 
First of all export some paths, and save them in your .zshrc or .bashrc files for easy use. Use sudo if you get error.
# Go development 
export GOPATH="${HOME}/golib"
export GOROOT="$(brew --prefix golang)/libexec"
export PATH=$PATH:${GOPATH}/bin:${GOROOT}/bin
$ test -d "${GOPATH}" || mkdir "${GOPATH}"
$ test -d "${GOPATH}/src/github.com" || mkdir -p "${GOPATH}/src/github.com"

# Also a bunch of dev tools!
$ go get golang.org/x/tools/cmd/godoc 
$ go get github.com/golang/lint/golint 

Setting up the VS Code text editor for Go 
Open VS Code via spotlight. Press Command + Space and type "VS Code" then press enter 
When VS Code opens, press command + shift + p and type "shell".
"Shell Command: Install 'code' command in PATH"
Click "Auto Save" in the file dropdown at the top of the screen. 
```
