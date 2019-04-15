Welcome Message When SSH Start
==============================

```
You need to edit two files:
    1. /etc/motd (Message of the Day)
    2. /etc/ssh/sshd_config: Change the setting PrintLastLog to "no", this will disable the "LastLogin" message.
    3. sudo /etc/init.d/ssh restart 
And then restart your sshd.
```
