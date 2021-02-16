fish-shell
==========
> Fish aka "the friendly interactive shell"
```
fish can be installed:
(ubuntu) $ sudo apt-get install fish
root@unreal-pod-1:~# fish -v
fish, version 3.1.0
root@unreal-pod-1:~# which fish
/usr/bin/fish

switching to fish
(ubuntu) $ chsh -s /usr/bin/fish
```

* oh-my-fish
> The Fish Shell Framework
```
Install Powerline Font
$ sudo apt-get install fonts-powerline

$ curl -L https://get.oh-my.fish | fish

Getting Started
    omf update [omf] [<package>...] : Update Oh My Fish, all package repositories, and all installed packages
    omf install [<name>|<url>] : Install one or more packages
    omf repositories [list|add|remove] : Manage user-installed package repositories
    omf list : List installed packages
    omf theme <theme>: Apply a theme
    omf remove <name> : Remove a theme or package
```

* starship
> The minimal, blazing-fast, and infinitely customizable prompt for any shell!
```
Installation
$ curl -fsSL https://starship.rs/install.sh | bash

Add the init script to your shell config file
# ~/.config/fish/config.fish
$ starship init fish | source
```

Vimrc
=====
- [.vimrc](/root/ilikeit/Fish-Vim-Tmux/vimrc)


FAQ
---
* How to fix: Connection refused by port 22?
```
1. Make sure OpenSSH is installed
$ sudo apt list --installed | grep openssh-server

2. Check SSH service
$ sudo service ssh status

3. Check SSH server listening port
$ sudo netstat -ltnp |grep sshd

4. Allow SSH in firewall
$ sudo ufw allow

5. Resolve Duplicate IP address conflict
$ sudo apt install arping
ping the SSH server's IP address
```
