GitLab: Build your own Private GitLab Repository 
=================================================

> Make a simple yet cool Git server that is perfect for hosting your next code project. If you're a programmer, then your probably have heard of Git before.Git is a hugely popular version control software for the development of software. 

Attach USB Storage to your Raspberry Pi
---------------------------------------
```
Pre-requistes
    For most USB hard drives you will need a power supply (PSU) capable of supplying at least 2.5A @ 5V, for some drives you many need even more power than this. This may mean that your setup will need one PSU for the Raspberry Pi and an additional one per hard drive you add.

    We will be formatting our drive with the EXT4 filesystem and using a unique label so that we can use multiple devices at the same time.

Step 1. Identify the drive
    The Linux command lsblk will list all bulk storage devices.
$ sudo lsblk
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda           8:0    1 59.8G  0 disk
└─sda1        8:1    1 59.8G  0 part
mmcblk0     179:0    0 29.8G  0 disk
├─mmcblk0p1 179:1    0  256M  0 part /boot/firmware
└─mmcblk0p2 179:2    0 29.6G  0 part /

Step 2. Create the partitions
    Using the fdisk tool to wipe out the existing partitions and create new ones. This is not always essential but ensures we have a known state on the disk.
$ sudo fdisk /dev/sda
    First wipe the existing partitions:
Command (m for help): o
Created a new DOS disklabel with disk identifier 0x04e2ae16.
The old gpt signature will be removed by a write command.

Now create a single partition by accepting all the defaults
Finally write the changes:

Step 3. Format the new partition 
$ sudo fdisk -l /dev/sda
[sudo] password for pi:
Disk /dev/sda: 59.8 GiB, 64172851200 bytes, 125337600 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 34086D2F-E64E-4934-91A7-DA3E5962F2D5

Device     Start       End   Sectors  Size Type
/dev/sda1   2048 125337566 125335519 59.8G Linux filesystem

Now format the partition we just created and at the same time attach a unique label
$ sudo mkfs.ext4 -L USBSHARE /dev/sda1 

Step 4. Pick a mount-point 
    For a Linux operating system we need to pick a directory to mount our storage under. This could be almost any folder including /home/pi for instance. we'll keep things simple and pick /mnt/usbshare.
$ sudo mkdir /mnt/usbshare 
    Let's test the mount point temporarily and then make things permanent.
$ sudo mount -L USBSHARE /mnt/usbshare 
$ ls /mnt/usbshare/

Now we were able to mount our drive using a label instead of the device /USBSHARE name of /dev/sda1 - as long as we keep the labels unique for all devices we attach we can use this method of identify them.

Step 5. Make it permanent
    If you intend on using the drive permanently then follow this step. The next step involves editing the fstab file which is used to mount disks at system boot time:
$ sudo vim /etc/fstab
    Since used an ext4 file-system and that is also used for the SD card's root filesystem, we can use the same settings. You should see two lines like the following:
$ sudo vim /etc/fstab
LABEL=writable  /        ext4   defaults        0 0
LABEL=system-boot       /boot/firmware  vfat    defaults        0       1

Add a line underneath, save the file, then reboot.
LABEL=USBSHARE          /mnt/usbshare   ext4    defaults,noatime    0   1
# a swapfile is not a swap partition, no line here
#   use  dphys-swapfile swap[on|off]  for that

Now that your drive is attached let's look at how to keep the drive working reliably and a few uses for that extra storage.

Best practices:
    Always shutdown with shutdown -h 0 or halt -h - never pull the power cable.
    
    If you are using the drive only temporarily then type in sudo unmount /mnt/usbshare before pulling out the USB cable - or shutdown the system first.
    
    If you have a power-cut or accidental power-out then you can repair the filesystem like this:

$ sudo umount /mnt/usbshare 
$ sudo fsck /dev/sda1 
    
    Optimizing power consumption 
```

Configure Swap
--------------
> Even with a newer Pi, the first setting you will want to change is to ensure the device has enough memory available by expanding the seap space to 4GB.
```
# The config file /etc/dphys-swapfile allows the user to set up the working environment for dphys-swapfile. 
$ sudo vim /etc/dphys-swapfile 
# The default value in Raspbian is:
CONF_SWAPSIZE=100 
# We will need to change this to:
CONF_SWAPSIZE=1024
# Then you will need to stop and start the service that manages the swapfile own Rasbian:
$ sudo /etc/init.d/dphys-swapfile stop 
$ sudo /etc/init.d/dphys-swapfile start 
# You can then verify the amount of memory + swap by issuing the following command:
$ free -m 
```

GitLab Installation 
-------------------
```
GitHub is a web service based on the software Git. Git allows you to store the history of your software code base and easily control versioning.

1. Install required dependencies.
$ sudo apt-get install curl openssh-server ca-certificates postfix apt-transport-https 
Select Internet Site when primpted. On the next screen, enter your server's domain name to configure how the system will send mail.

2. Installing GitLab from source 
    Installing from source means that we will take the source code from gitlab.com and use that to code in order to install it on our server. 
    
    https://gitlab.com/gitlab-org/gitlab-ce/blob/master/VERSION  -- v11.10.4 
    
    Getting ready 
        1. A server running Debain or Ubuntu: preferably one of the latest versions, and running as 64-bit 
        2. Git Version 2.21 or higher 
        3. A text editor, using Vim 
        4. A working mail server 
        5. You have to setup the database 
        6. You have to install all the server dependencies 

    Download the source code:
        $ cd /home/pi
        $ git clone https://gitlab.com/gitlab-org/gitlab-ce.git -b 11-10-stable gitlab

    In config/gitlab.yml, we need to change the host to the fully-qualified domain name of your GitLab instance. Also change the email_from to the e-mail address you want to use as a from address for all the e-mails that are sent by GitLab.


```

Set-up remote git repository on a standard server 
-------------------------------------------------
The first thing to do is to install Git on the remote server, Once you do that the reset of the process is split into three sections:

* Server set up 
* Local set-up (push commits)
* Server (pull commits)

Server set-up
-------------
```
# Create the SSH Key Pair 
$ ssh-keygen -C "youremail@mailprovider.com"

$ ssh -pxxxx username@xxx.xxx.xxx.xxx (This is you connecting to your remote server)

# fist make sure that Linux is up to date. Run  the following commands
$ sudo apt update 
$ sudo apt upgrade -y 

# then make sure Git is installed 
$ sudo apt install git

# create new git user and no create home directories,and no login
$ sudo useradd -r -s /sbin/nologin git 

# Remove user home directory and mail spool by using the -r flag
$ sudo userdel -r user_name 

# Firstly, need to make a directory for where our new repository will be stored. The -p tag will create any directories in our path that doesn't already exits.
public server$ mkdir -p ~/GitRepository/chutils

# initialize the Git repository using the bare command.
# Because the Git in the Server is purely for sharing, so users are not allowed to log in directlry to the server to change the workspace.
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

![Private Git Server](/imgs/ilikeit/GitCrashCourse/privateGitServer.png?raw=true)
