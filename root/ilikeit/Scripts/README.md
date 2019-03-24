Awesome Scripts 
===============

> Where is the Shell, there is a way

- [VPS Banchemark Script](/root/ilikeit/Scripts/vpsBanchmark.sh)


FAQ 
---
```
mkdir   -- make directories 
touch   -- change file access and modification times and If not exist will create new files 
mv      -- move files 
cp      -- opy files 
rm      -- remove directory entries 

awk     -- pattern-drirected scanning and processing language 
sed     -- stream editor 
grep    -- file pattern searcher 
xargs   -- construct argument list(s) and execute utility 
find    -- walk a file hierarchy
sort    -- sort or merge records (lines) of text and binary files 
uniq    -- report or omit repeated lines 
head    -- output the first part of files 


查看连接你服务器top10用户端的IP地址
$ netstat -nat | awk '{print $5}' | awk -F ':' '{print $1}' | sort | uniq -c | sort -rn | head -n 10 

查看最常用的10个命令
cat .bash_history | sort | uniq -c | sort -rn | head -n 10 


```

Handy Bash Shell Aliases For Linux/Unix/macOS 
---------------------------------------------

> An bash alias is nothing but the shortcut to commands.

```
$ alias  # By default alias command shows a list of aliases that are defined for the current user.

$ alias cls='clear'  # clear the screen 
$ \cls  # call alias with a backslash 
$ unalias cls  # delete/remove a bash alias, but you need to delete the alias from the ~/.bashrc file 

A note about privileged access 
# if user is not root, pass all commands via sudo 
if [ $UID -ne 0]; then 
    alias reboot='sudo reboot'
    alias update='sudo apt-get upgrade'
fi 

A note about os specific aliases 
# Get is name via uname 
_myos="$(uname)"
case $_myos in 
    Linux) alias foo='/path/to/linux/bin/foo' ;; 
    FreeBSD|OpenBSD) alias foo='/path/to/bsd/foo' ;;
    MacOS) alias foo='/path/to/macos/bin/foo' ;;
    *) ;;
esac 

#1: Control ls command output 
    
    alias ls='ls --color=auto'  # Colorize the ls output 
    alias ll='ls -la'  # Use a long listing format 
    alias l.='ls -d .* --color=auto'

#2: Control cd command behavior 
    
    alias cd..='cd ..'  # get rid of command not found 
    alias ..='cd ..'    # a quick way to get out of current directory 
    alias ...='cd ../../../' 

#3: Control grep command output 
    
    alias grep='grep --color=auto'
    alias egrep='egrep --color=auto'
    alias fgrep='fgrep --color=auto'

#4: Start calculator with math support 
    
    alias bc='bc -l'

#5: Generate sha1 digest 
    
    alias sha1='openssl sha1' 



    
```
