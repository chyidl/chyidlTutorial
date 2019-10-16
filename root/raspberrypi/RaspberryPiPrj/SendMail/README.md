SendMail Server
===============

> SendMail is a MTA (Mail Transfer Agent) server used for transferring email from between different hosts. SendMail uses SMTP (Simple Mail Transfer Protocol) protocol. Most of the system administrators preferred to use SendMail server as MTA than other MTAs.

* 1. Remove Postfix 
```
# remove the existing postfix installation on Ubuntu 
$ sudo systemctl stop postfix 
$ sudo pat remove postfix && apt purge postfix 
```

* 2. Install Sendmail 
```
    - $ yum install sendmail sendmail-cf m4     # CentOS 
    - $ sudo apt-get install sendmail           # Ubuntu 
```

* 3.Configure SendMail Server 
```
# The execute the sendmailconfig command to complte the basic configuration. 
$ sudo sendmailconfig 

# various sendmail configuration files exists in /etc/mail directory 
    access - Allow/Deny other systems to use Sendmail for outbound emails 
    domaintable - Used for domain name mapping for Sendmail 
    local-host-names - Used to define aliases for the host.
    mailertable - Defined the instructions that override routing for particular domains.
    virtusertable - Specifies a domain-specific form of aliasing, allowing multiple virtual domains to be hosted on one machine.

    $ sudo vim /etc/hosts       # Configure /etc/hosts 
        127.0.0.1 localhost RPi3BPlus 
    $ sudo sendmailconfig       # Sendmail config 
```

* 4. Receive Incomming Emails 
```
$ sudo vim /etc/mail/sendmail.mc 
    # allow receiving an email from anywhere. 
    dnl DAEMON_OPTIONS(`Family=inet,  Name=MTA-v4, Port=smtp, Addr=127.0.0.1')dnl
    dnl DAEMON_OPTIONS(`Family=inet,  Name=MSP-v4, Port=submission, M=Ea, Addr=127.0.0.1')dnl

# add your domain names to /etc/mail/local-host-names files 
    $ cat /etc/mail/local-host-names 
        localhost
        localhost.RPi3BPlus 
```
