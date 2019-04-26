Process Monitoring with Supervisord
===================================

> As some point you'll likely find yourself writing a scirpt which needs to run all the time -a "long running script". These are scripts that shouldn't an error, or ones that should restart when the system reboots.
> To accomplish this, we need something to watch these scripts. Such tools are process watches. They watch processes and restart them if they fail, and ensure that start on system boot.

* Supervisor Components
    - supervisord: The server of supervisor, It is responsible for starting child programming.
    - supervisorctl: The command-line client piece of the supervisor.
    - configuration file: /etc/supervisord.conf 
    - Web Server: http://localhost:9001/ after activating the configuration file's [inet_http_server] section
    - XML-RPC Interface: 

* Installing a Distribution Package
    - Some Linux distributions offer a version of Supervisor that is installable through the system package manager. These packages are made by third parties, not the Supervisor developers, and often include distribution-specific changes to Supervisor.
    - A feature of distribution packages of Supervisor is that they will usually include integration into the service management infrastructure of the distribution, allowing supervisord to automatically start when the system boots.
    - $ apt-cache show supervisor 

* Installing to A System With Internet Access 
    - Internet-Installing With Pip
        * $ sudo -H python3 -m pip install supervisor 

* Creating a Configuration File
    - Once the Supervisor installation has completed, run echo_supervisord_conf. This will print a "sample" Supervisor configuration file to your terminal's stdout.
    - $ sudo mkdir /etc/supervisor
    - $ echo_supervisord_conf > supervisord.conf 
    - $ mv supervisord.conf /etc/supervisor/supervisord.conf 
    - Configuration for Supervisord is found in /etc/supervisor/supervisord.conf 
        * [include]
        * files = /etc/supervisor/conf.d/*.conf
    - So, any files found in /etc/supervisor/conf.d and ending in .conf will be included.

* Create supervisord.service management infrastructure of the distribution, e.g.allowing supervisord to automatically start when the sustem boots.
```
/etc/systemd/system/supervisor.service
[Unit]
Description=Supervisor process control system for UNIX
Documentation=http://supervisord.org
After=network.target

[Service]
ExecStart=/usr/local/bin/supervisord -n -c /etc/supervisor/supervisord.conf
ExecStop=/usr/local/bin/supervisorctl $OPTIONS shutdown
ExecReload=/usr/local/bin/supervisorctl -c /etc/supervisor/supervisord.conf $OPTIONS reload
KillMode=process
Restart=on-failure
RestartSec=50s

[Install]
WantedBy=multi-user.target
```
    - $ sudo systemctl start supervisor  # start service 
    - $ sudo systemctl status supervisor # view service status 
    - $ sudo systemctl enable supervisor # auto start service on system startup

* Running Supervisor
    - The Python Script, an exmaple long-running script 
```
#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
"""
file: apscheduler_demo.py
descript: demostrates how to use the background scheduler to schedule a job that execute on 3 second
intervals.
"""
from datetime import datetime 
import time 
import os 
from apscheduler.schedulers.background import BackgroundScheduler


def tick():
    print("Tick! The time is: %s" % datetime.now())

if __name__ == '__main__':
    scheduler = BackgroundScheduler() 
    scheduler.add_job(tick, 'interval', seconds=3)
    scheduler.start()
    print("Press Ctrl+{0} to exit".format('Break' if os.name == 'nt' else 'C'))

    try:
        # This is here to simulate application activity (which keeps the main thread alive)
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible 
        scheduler.shutdown()
```
    - create a configuration for it called apscheduler_demo.conf. This file will be created at /etc/supervisor/conf.d/apscheduler_demo.conf:
```
$ cat /etc/supervisor/conf.d/apscheduler_demo.conf
[program:apscheduler_demo]  # Define the program to monitor 
command=/usr/bin/python3 /home/pi/chyidl.com/PyPrj/apscheduler_demo.py
directory=/home/pi/chyidl.com/PyPrj  # Set a directory for Supervisord to "cd" into for before running the process
autostart=true  # Setting this "true" means the process will start when Supervisord starts 
autorestart=true  # If this is "true", the program will be restarted if it exits unexpectedly 
startretries=3  # The number of retries to do before the process is considerd "failed"
stderr_logfile=/var/log/PyPrj/apscheduler_demo.err.log  # The file to write any errors output 
stdout_logfile=/var/log/PyPrj/apscheduler.out.log  # The file to write regular output 
user=pi  # The user the process is run as 
environment=SECRET_PASSPHRASE="this is secret" # Environment variables to pass to the process.
```
    - $ sudo mkdir /var/log/PyPrj
    - Controlling Processes
        * $ sudo supervisorctl reread  # Reload the daemon's configuration files, without add/remove (no restarts) 
        * $ sudo supervisorctl update  # Reload config and add/remove as necessary, and will restart affected programs
        * $ sudo supervisorctl status  # Get all process status info.
        * $ sudo supervisorctl start   # Start a process 
    - Web Interface 
        * We can configure a web interface which comes with Supervisord, Inside of /etc/supervisord.conf 

    - Double check this with the ps command:
        * $ ps aux | grep /usr/bin/python3 
    
    - This nginx configuration worsk 
```
location /supervisor {
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    # hack the host https://github.com/Supervisor/supervisor/issues/251
    proxy_set_header Host $http_host/supervisor/index.html;
    proxy_redirect off;
    rewrite ^/supervisor(.*)$ /$1 break;
    proxy_pass http://127.0.0.1:8999/;
}
```
![supervisord](/imgs/ilikeit/SupervisordCrashCourse/supervisord.png?raw=true)
