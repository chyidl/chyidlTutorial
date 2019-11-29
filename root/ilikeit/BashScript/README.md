Bash Script
===========

A Brief History of Bash 
-----------------------
* The Shell 
> Shells (or command line interpreters) began with the first Unix shell back in 1971, called the V6 shell. Written by Ken Thompson from Bell Labs, this shell (simply the /bin/sh) was a user program that executed from outside of the kernel.
> In 1977, the Bourne shell was introduced having been created by Stephen Bourne while at Bell Labs for V7 Unix. The Bourne shell itself was written with one of the main goals being to support interactive execution of commands for the operating syste, thus scripting was born.

* The Bourne Again Shell 
> This is an open source (GNU) project that was intended to completely replace the Bourne shell. It was developed by Brian Fox and has become the standard shell for almost all Linux distributions over time.
> Base is released under the GPL.

Core Concepts
-------------
* Bash environment 
* Core bash configuration files 
    -  $HOME/.bash_profile file 
```
 # $ vim ~/.bashrc
 # .bash_profile                                                                                                               
  
 # Get the aliases and functions
 if [ -f ~/.bashrc ]; then
     . ~/.bashrc
 fi
  
 # User specific environment and startup programs
  
 PATH=$PATH:$HOME/.local/bin:$HOME/bin
  
 export PATH
 alias lZ="ls -alZ"
```
    - $HOME/.bashrc file 
```
# $ bash # run .bashrc
 # .bashrc
  
 # Source global definitions
 if [ -f /etc/bashrc ]; then
-    . /etc/bashrc
 fi
  
 # Uncomment the following line if you don't like systemctl's auto-paging feature:
 # export SYSTEMD_PAGER=
  
 # User specific aliases and functions
 source scl_source enable devtoolset-7     

 # Add BASH HISTORYCONROL
 export HISTCONTROL=ignoredups:ignorespace  # 

 run .bashrc file 
 $ . ~/.bashrc
```
    - $HOME/.bash_history file 
```
will be the last hundred commands that are captured in the bash history 
$ env | grep HISTCONTROL
```
    - $HOME/.bash_logout file 
```
# ~/.bash_logout                                                                                 
cp ~/.bashrc.original ~/.bashrc

# use to clean exit close or logout execute someting when you log out terminal session 
```

* Bash environment variables 
* What makes a file a bash script 
* Exit codes and return status 
* Pipes and redirects 
* Signals 
* Foreground and background

Scripting
---------
* Execute permissions and PATH
* The runtime environment 
* Comments 
* Static variables
* Dynamic variables
* I/O Handling 
* Conditionals
* Flow control
* Declaring functions
* Arrays 
* Parsing runtime arguments
* Value testing
* Functions 
* Code blocks 
* Sub shells
* Special structures (&&, ||, {}, etc)
* How to do math 
* handling errors within a script 
* Advanced I/O (IPC, signals, interactive user input, redirection, file handles)
* Advanced find 
* External dependencies (sourcing external file, libraries, etc)
* Date and time (timezones, formatting, adding stamps to files)
* Metadata
* Directory and file attributes 
* Automation of common system administration activities 
* Using in conjunction with CRON, things to be aware of 
