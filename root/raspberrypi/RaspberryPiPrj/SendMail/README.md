SendMail Server
===============
> SendMail is a MTA (Mail Transfer Agent) server used for transferring email from between different hosts. SendMail uses SMTP (Simple Mail Transfer Protocol) protocol. Most of the system administrators preferred to use SendMail server as MTA than other MTAs.

* 1. Install Sendmail 
    - $ yum install sendmail sendmail-cf m4 

* 2.Configure SendMail Server 
```
# various sendmail configuration files exists in /etc/mail directory 
    access - Allow/Deny other systems to use Sendmail for outbound emails 
    domaintable - Used for domain name mapping for Sendmail 
    local-host-names - Used to define aliases for the host.
    mailertable - Defined the instructions that override routing for particular domains.
    virtusertable - Specifies a domain-specific form of aliasing, allowing multiple virtual domains to be hosted on one machine.
```
