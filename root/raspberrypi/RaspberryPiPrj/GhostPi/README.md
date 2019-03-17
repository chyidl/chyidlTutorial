Build Ghost Blog on Raspberry Pi
================================

Prerequisites
-------------
* Linux (A server with at least 1GB memory) 
* Nginx 
* Node.js 
* MySQL 
* Systemd 

Server Setup 
------------
```
Create a new user 
# login via ssh 
$ ssh root@your_server_ip 

# Create a new user and follow prompts 
$ adduser <user>

# Add user to superuser group to unlock admin privileges 
$ usermod -aG sudo <user>

# Then log in as the new user 
$ su - <user>

# Update package lists 
$ sudo apt-get update 

# Update installed packages 
$ sudo apt-get upgrade 
```

Install Nginx 
-------------
```
# install Nginx
$ sudo apt-get install nginx 
```

Install MySQL
-------------
```
# Install MySQL
$ sudo apt-get install mysql-server 

# Now update your user with this password 
# Replace 'password' with your password, but keep the quote marks!
mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';

# Then exit MySQL
mysql> quit 

# and login to your Ubuntu user again 
$ su - <user>
```

Install Node.js
---------------
```
# Add the NodeSource APT repository for Node 8 
$ curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash 

# Install Node.js 
$ sudo apt-get install -y nodejs 
```

Install Ghost-CLI
-----------------
```
Ghost-CLI is a commandline tool to help you get Ghost installed and configured for use, quickly and easily. The npm module can be installed with npm or yarn

$ sudo npm install ghost-cli@latest -g 
```

Install Ghost
-------------
```
Create a directory 
# We'll name ours 'ghost' in this example; you can use whatever you want
$ sudo mkdir -p /var/www/ghost 

# Replace <user> with the name of your user who will own this directory
$ sudo chown <user>:<user> /var/www/ghost
 /var/www/ghost

# Set the correct permissionsuser
$ sudo chmod 775 /var/www/ghost 

# Then navigate into it 
$ cd /var/www/ghost 

# Run the install process 
$ ghost install
```

Install questions
-----------------
```
# Blog URL -- https://RPi3B 
# MySQL hostname -- localhost 
# MySQL username/password 
# Ghost database name -- must already exist and have the correct permissions.
# Set up a ghost MySQL user 
# Set up Nginx 
# Set up SSL 
# Enter your email: SSL certification setup requires an email address 
# Set up systemd -- systemd is the recommended process manager tool to keep Ghost running smoothly 
# start Ghost? 
```
