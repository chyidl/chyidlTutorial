Scheduling tasks with Cron
==========================
> Linux use two service utilities that allow to run commands, programs, and tasks at predetermined times. The cron and at services to schedule tasks to run at a specific time in the future. The at service specifies a one-time tasks that runs at a certain time. The cron service can schedule tasks on a repetitive basic, such as daily, weekly, or monthly.

> The command crontab (cron table) is used to edit the list of scheduled tasks in operation, and is done on a per-user basis; each user (including root) has their own crontab

* Editing crontab 
```
$ crontab -e    # edit the cron table 

crond: 
    daemon is the background service that enables cron functionality.
cron: 
    service checks for files in the "/var/spool/cron" and "/etc/cron.d" directories and the "/etc/anacrontab" file. 
    "/var/spool/cron" : The individual user cron files are located 
    "/etc/cron.d": system services and applications 
    "/etc/anacrontab": 

Each user, including root, can have a cron file. These files don't exist by default, but can be created in the "/var/spool/cron" directory using the 
$ crontab -e # Create or Edit a cron file

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name  command to be executed
*/10 *  *  *  *   pi      /home/pi/chyidl.com/AM2302/DHT2302.py &
@reboot python /home/pi/myscript.py &    # To run a command every time the Raspberry Pi starts up

$ crontab -l    # View scheduled tasks 
```

* cron crontab log
```
On a default installation the cron jobs get logged to 
/var/log/syslog 

You can see just cron jobs in that logfile by running 
$ grep CRON /var/log/syslog
```