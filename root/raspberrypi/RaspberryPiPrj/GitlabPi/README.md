GITLAB ON RASPBERRY PI
======================

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
