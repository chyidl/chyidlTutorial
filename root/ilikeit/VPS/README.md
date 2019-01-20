VPS - Virtual Private Server
============================

1. How to Create a Sudo User on VPS
-----------------------------------
The **sudo** command provides a mechanism for granting administrator privileges, ordinarily only available to the root user, to normal users.

```
# Step to Create a New Sudo User 
1. Log in server as the root user.
$ ssh root@server_ip_address

2. Use the adduser command to add a new user to your system
$ adduser username  # userdel -r username 
$ passwd username # Set and confirm the new password at the prompt. A strong password is highly recommended!

3. First create a new sudo group (groupadd sudo) and add this lines (sudo visudo). Then once again add username to the group
# the 'sudo' group has all the sudo privileges
%sudo   ALL=(ALL:ALL) ALL

3. Use the usermod command to add the user to the sudo group
$ usermod -aG sudo username  # By default, on Ubuntu, members of the sudo group have sudo privileges 

4. Test sudo access on New user account 
$ su - username # Use the su command to switch to the new user account 
$ sudo command_to_run # As the new user, verify that you can use sudo by prepending "sudo" to the command that you want to run with superuse privileges.
# For example. you can list the contents of the /root directory, which is normally only accessible to the root user.
$ sudo ls -la /root
```
