Install and Configure GitLab ON RASPBERRY PI
============================================
> GitLab CE, or Community Edition, is an open-source application primarily used to host Git repositories, with additional development-related features like issue tracking. It is designed to be hosted using your own infrastructure, and provides flexibility in deploying as an internal repository store for your development team, a public way to interface with users, or a means for contributors to host their own projects.

GitLab Installation
-------------------
> strongly recommend downloading the Omnibus package installation since it is quicker to install, easier to up upgrade, and it contains features to enhance reliability not found in other methods. strongly recommend at least 4GB of free RAM to run GitLab.
```
# run the following Bash script to get the newest version of GitLab Community Edition set up:

#!/usr/bin/env bash 

# Install GitLab 
echo "Updating OS"
sudo apt-get update 
sudo apt-get install curl openssh-server ca-certificates postfix 

curl -sS https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh | sudo bash 
sudo apt-get install gitlab-ce 

sudo nano /etc/gitlab/gitlab.rb 

sudo gitlab-ctl reconfigure 

# Start all 
sudo gitlab-ctl start 
```
