VPS - Virtual Private Server
============================

1. How to Create a Sudo User on VPS
-----------------------------------
> The **sudo** command provides a mechanism for granting administrator privileges, ordinarily only available to the root user, to normal users.
```
# Step to Create a New Sudo User 
1. Log in server as the root user.
$ ssh root@server_ip_address

2. Use the adduser command to add a new user to your system
$ adduser username  # userdel -r username 
$ passwd username # Set and confirm the new password at the prompt. A strong password is highly recommended!

3. First create a new sudo group (groupadd sudo) and add this lines (sudo visudo). 
# Change visudo editor from nano to vim 
$ sudo update-alternative --config editor
# the 'sudo' group has all the sudo privileges
sudo   ALL=(ALL:ALL) ALL

3. Use the usermod command to add the user to the sudo group
$ usermod -aG sudo username  # By default, on Ubuntu, members of the sudo group have sudo privileges 

4. Test sudo access on New user account 
$ su - username # Use the su command to switch to the new user account 
$ sudo command_to_run # As the new user, verify that you can use sudo by prepending "sudo" to the command that you want to run with superuse privileges.
# For example. you can list the contents of the /root directory, which is normally only accessible to the root user.
$ sudo ls -la /root
```

2. How To Add Swap Space on Ubuntu 18.04
--------------------------------------------
> One of the easiest way of increasing the responsiveness of your server and guarding against out-of-memory errors in applications is to add some swap space.Although swap is generally recommended for systems utilizing traditional spinning hard drives, using swap with SSDs can cause issues with hardware degradation over time.
* What is Swap?
    - Swap is an area on a hard drive that has been designated as a place where the operating system can temporarily store data that it can no longer hold in RAM.
    - The infromation written to disk will be significantly slower than information kept in RAM, but the operating system will prefer to keep running application data in memory and use Swap for the older data.

* Check the System for Swap Information
    - $ sudo swapon --show  # check if the system has any configured swap by typing.
    - $ free -h  # verify that there is active swap using the free utility 

* Check Available Space on the Hard Drive Partition 
    - The most common way of allocating space for swap is to use a separate partition devoted to the task. However, altering the partitioning scheme is not always possible. can just as easily a swap file that resides on an existing partition.
    - $ df -h  # check the current disk usage by typing 
    - Generally, an amount equal to or double the amount of RAM on your system is a good staring point.

* How to empty swap
    - The Linux kernel underlying Ubuntu will automatically "swap in" those pages from disk to RAM as needed, so in general I'd say just let it happen naturaly
    - However, if you really feel that you need to force it you can momentarily disable and re-enable swap.
    - $ sudo swapoff -a 
    - $ sudo swapon -a 
    - $ sudo vim /etc/fstab 
```
# /etc/fstab: static file system information.
#
# Use 'blkid' to print the universally unique identifier for a
# device; this may be used with UUID= as a more robust way to name devices
# that works even if disks are added and removed. See fstab(5).
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
# / was on /dev/sda2 during installation
UUID=ec1f5568-1f51-4d1b-80d4-a940d7f3aa4f /               ext3    errors=remount-ro,discard,noatime 0       1
# /boot was on /dev/sda1 during installation
UUID=9b9407e6-ff9b-48cc-a19b-b1008ad90fb3 /boot           ext3    defaults        0       2
# Comment all below line
#/swapfile                                 none            swap    sw              0       0
#/swap none swap sw 0 0
```
    - Be careful doing this, as you may make your system unstable, especially if its already low on RAM.

* Create a Swap File
    - creating a swap file within our filesystem. Create a file of the swap size called swapfile in our root(/) directory.
    - The best way of creating a swap file is with the **fallocate** program. This command creates a file of a preallocated size instantly.
    - $ sudo fallocate -l 1G /swapfile   # If **faillocate** is not installed or if you get an error message saying **fallocate failed: Operation not supported** then you can use the following command to create the swap file:
    - $ sudo dd if=/dev/zero of=/swapfile bs=1024 count=1048576  
    - $ ls -lh /swapfile # verify that the correct amount of spaces was reserved by typing 

* Enabling the Swap File 
    - Now that we have a file of the correct size available, we need to actually turn this into swap space.
    - First, we need to lock down the permissions of the file so that only the users with **root** privileges can read the contents. This prevents normal users from being able to access the file, which would have significant security implications.
    - $ sudo chmod 600 /swapfile #Make the file only accessible to **root** by typing.
    - $ sudo mkswap /swapfile # mark the files as swap space 
    - $ sudo swapon -a 
    - $ sudo swapon --show # verify that the swap is available 

* Make the Swap File Permanent
    - Our recent changes have enabled the swap file for the current session. However, if we reboot. the server will not retain the swap settings automatically. Can change this by adding the swap file to our **/etc/fstab** file.
    - $ sudo cp /etc/fstab /etc/fstab.bak  # Back up the **/etc/fstab** file in case anything goes wrong
    - $ echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab # add the swap file information to the end of your **/etc/fstab** file by typing
    
* Tweak your Swap Settings (There are a few options that you can configure how often your system swaps data out of RAM to the swap space.)
    - Adjusting the **Swappiness** Property: The **swappiness** parameter configures how often your system swaps data out of RAM to the swap space.This is a value between 0 and 100 that represents a percentage.
    - With values close to zero, the kernel will not swap data to the disk unless absolutely necessary.  Remember, interactions with the swap file are "expensive" in that they take a lot longer than interactions with RAM and they can cause a significant reduction in performance. Telling the system not to rely on the swap much will generally make your system faster.
    - Values that are closer to 100 will try to put more data into swap in an effort to keep more RAM space free.
    - $ cat /proc/sys/vm/swappiness  # For a Desktop, a swappiness setting of 60 is not a bad value. For a server, you might want to move it closer to 0
    - $ sudo sysctl vm.swappiness=10 # This setting will persist until the next reboot. can set this value automatically at restart by adding the line to **/etc/sysctl.conf** file.
    - $ sudo vim /etc/sysctl.conf  
    - At the bottom, you can add:
    - vm.swappiness=10  

* Adjusting the Cache Pressure Setting 
    - Another related value that you might want to modify is the **vfs_cache_pressure**. This setting configures how much the system will choose to cache inode and dentry information over other data.
    - $ cat /proc/sys/vm/vfs_cache_pressure  #    
    - $ sudo vim /etc/sysctl.conf 
    - At the bottom, add the line that specifies your new value:
    - vm.vfs_cache_pressure=50     
* Conclusion
    - Add Swap file give you some breathing room in cases that would otherwise lead to out-of-memory exceptions. Swap space can be incredibly useful in avoiding some of these common problem 
    - If you are running into OOM(out of memory) errors, or if you find that system is unable to use the applications you need, the best solution is to optimize your application configurations or upgrade your server.   


3. Setup the Date and Timezone
----------------------------------
Setting the correct date, time, time zone and synchronization are the first basic steps that you should perform when previsioning your Ubuntu 18.04 server for the first time.
* Step 1: Checking your local Ubuntu time settings 
    - $ timedatectl # check Ubuntu local time, time zone and synchronization status                                             

* Step 2: Checking the list of available time zones on Ubuntu server 
    - $ timedatectl list-timezones | less #  Asia/Hong_Kong 

* Step 3: Changing the time zone on Ubuntu 
    - $ sudo timedatectl set-timezone Asia/Hong_Kong 

* Step 4: Enabling/Disabling time synchronization 
    - Ubuntu the time synced daemon which connects to a pool of Network Time Protocol servers to get constant and accurate time updates.
    - $ timedatectl # check **systemd-timesyncd.service active** status is already set to "yes". 
    - $ sudo timedatectl set-ntp on/off # can turn on/off timesynced daemon by typing the command below.

Kill Zombie Process 
-------------------
> A zombie or a defunct process in Linux is a process that has been complted, but its entry still remains in the process table due to lack of correspondence between the parent and child processes.Usually, a parent process keeps a check on the status of its child processes through the wait() function. When the child process has finished, the wait function signals the parent to completely exit the process from the memory. However, if the parent fails to call the wait function for any of its chidlren, the child process remains alive in the system as a dead or zombie process. These zombie processes might accumulate, in large numbers, on your system and affect its performance. In that case, you might have to kill these zombies manually through the ways and commands described in this tutorial.
```
# Viewing Zombie Processes 
$ top 
top - 09:41:23 up 17 days, 19:47, 19 users,  load average: 0.24, 0.21, 0.17
Tasks: 206 total,   2 running, 154 sleeping,   0 stopped,   2 zombie

# further details about the zombie process, use the following command:
$ ps axo stat,ppid,pid,comm | grep -w defunct   # 

# Killing z Zombie-Process 
> How zombie processes are a threat to our system's performance. It is important to learn that zombies are dead and mostly completed processes that do not take memory or CPU resources. However, each of these processes has a unique process ID assigned to them which comes from a limited pool of PIDs reserved for your processor. If a large number of zombies gather they will eat up most part of the PID pool and the new processes will not be able to launch due to lack of a process ID.

> A small number of defunct programs occupying your system is not a big threat but that means that their parent programs have not been able to call them off due to a bug or a missing wait() function.

> When a parent process has not been able to call the wait() function automatically, we need to manually signal the parent processes to run the wait function on all its chidlren so the ones with a complete state can be called back. We can do this by running the SIGCHLD command. When that doesn't work, we can manually kill the parent process so that all its zombie chidlren are also killed, freeing the processes IDs for the new processes.

$ sudo kill -s SIGCHLD PID    # signals the zombie's parent process to kill the command 
$ sudo kill -9 PID
```

Scientific Internet
-------------------
```
Google 
Google Scholar 
Github 
Wikipedia
Travis-ci 

Stackoverflow 
Golang 
Reddit 
Medium 
Quora
Blogs

Mac 
  $ brew install fish 
  $ brew install vim 
  $ brew install tmux 
  $ brew install wget

Move faster in Shell:
  Ctrl-A : Start 
  Ctrl-E : End 
  Ctrl-F : Forware 
  Ctrl-B : Backward 
  Ctrl-P : Previous 
  Ctrl-N : Next 
  Ctrl-R: Backward Search


```
