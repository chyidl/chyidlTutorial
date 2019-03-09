Git Server: Build your own Private Git Repository 
=================================================

Make a simple yet cool Git server that is perfect for hosting your next code project. If you're a programmer, then your probably have heard of Git before.Git is a hugely popular version control software for the development of software. 

Set-up remote git repository on a standard server 
-------------------------------------------------
The first thing to do is to install Git on the remote server, Once you do that the reset of the process is split into three sections:

* 1. Server set up 
* 2. Local set-up (push commits)
* 3. Server (pull commits)

Server set-up
-------------------------

```
$ ssh -pxxxx username@xxx.xxx.xxx.xxx (This is you connecting to your remote server)

# fist make sure that Linux is up to date. Run  the following commands
$ sudo apt update 
$ sudo apt upgrade -y 

# then make sure Git is installed 
$ sudo apt install git-core 

# Firstly, need to make a directory for where our new repository will be stored. The -p tag will create any directories in our path that doesn't already exits.
public server$ mkdir -p ~/GitRepository/chutils

# initialize the Git repository using the bare command. 
public server$ cd ~/GitRepository/chutils && git init --bare 
Initialized empty Git repository in /home/vps/GitRepository/chutils/

# You will need to repeat these steps whenever you need to make a new repository. Now that's all done we're ready to do our first commit 
```

Local set-up (push commits)
---------------------------

```
# You will need to initialize it before we can push the code to our Git Server. To do this enter the following command
local server$ mkdir -p ~/Downloads/chutils && cd ~/Downloads/chutils
local server$ git init 
local server$ git add * 
local server$ git commit -m "start of new project"

# add our remote Git directory by adding the following line.
# git remote add with other SSH port
local server$ git remote add origin ssh://username:public_server:port/home/vps/GitRepository/chutils

# It should come up with a success message. This message means our code has been pushed to our Git Server  
local server$ git push origin master 

# Removing a remote 
local server$ git remote rm <name>
```

Another Local set-up and test 
-----------------------------

```
# To test to see if everything is working correctly. you can clone the repository we just set up to a new folder.
local server$ mkdir ~/Downloads/chutils2 && cd ~/Downloads/chutils2
local server$ git clone username@publish_ip:port/home/xxx/GitRepository/chutils/ 

# As you can see, the Git Server is noe storing our code correctly. Now, this is the very basics of Git, and there is so much more to learn. 
```

! [Private Git Server](/imgs/ilikeit/GitCrashCourse/privateGitServer.png?raw=true)
