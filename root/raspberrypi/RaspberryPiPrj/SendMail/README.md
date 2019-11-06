Build SMTP Mail Server
======================
> SendMail is a MTA (Mail Transfer Agent) server used for transferring email from between different hosts. SendMail uses SMTP (Simple Mail Transfer Protocol) protocol. Most of the system administrators preferred to use SendMail server as MTA than other MTAs.

Prerequisties
-------------

* What is DNS (Domain Name System)?
    - IP address mapping domain name 

* Email sending operation?
```
    chyiyaqing@chyidl.com 
        chyiyaqing -- account name 
        chyidl.com -- Domain name
    
    Send Email: -> SMTP(Simple Message Transfer Protocol) Server  -> DNS(Domain Name System) Server -> MTA(Mail Transfer Agent) -> Select the appropriate inbox -> [POP | IMAP] -> Inbox
```

* What is a VPS?
```
VPS: Virtual Private Server 
    AWS、 Azure、DigitalOcean 

(Windows)
    Putty SSH Client: 
```

* What is SSL?
```
```

* Buy a domain name using GoDaddy?
```
```

Building our Mail Server 
------------------------
* What is Webmin?
```
Webmin is a web-based interface for system administration for Unix. Using any modern web browser, you can setup user accounts, Apache, DNS, file sharing and much more. Webmin removes the need to manually edit Unix configuration files like /etc/passwd, and let's you manage a system from the console or remotely.
```
* How To Install Webmin on Ubuntu 18.04
```
Step 1 - Installing Webmin 
> First, we need to add the Webmin repository so that we can easily install and update Webmin using our package manager. We do this by adding the repository to the /etc/apt/sources.list file. 

$ sudo vim /etc/apt/sources.list 
# add this line to the bottom of the file to add the new repository 
. . .
deb http://download.webmin.com/download/repository sarge contrib 

# add the Webmin PGP key so that your system will trust the new repository 
$ wget http://www.webmin.com/jcameron-key.asc 
$ sudo apt-key add jcameron-key.asc 

# Next, update the list of package to include the Webmin repository:
$ sudo apt update 

# Then install Webmin:
$ sudo apt install webmin 

Webmin install complete. You can now login to https://your_domain:10000/
as root with your root password, or as any user who can use sudo
to run commands as root.

Step2 - Securing Webmin with Nginx and Let's Encrypt 
> To access Webmin, you have to specify port 10000 and ensure the port is open on your firewall. This is inconvenient, especially if you're accessing Webmin using an FQDN like webmin.your_dommain We are going to use an Nginx virtual host to proxy requests to Webmin's server running on port 10000. we'll then secure the virtual host using a TLS/SSL certificate from Let's Encrypt.

> using Cerbot to obtain a free SSL certificate for Nginx and set up certificate to renew automatically. 

> Using a separate Nginx server block file instead of the default file. recommend creating new Nginx server block files for each doamin because it helps to avoid common mistakes and maintains the default files as fallback configuration. 

# Installing Certbot 
$ sudo add-apt-repository ppa:cerbot/cerbot # add the repository 

# Install Cerbot's Nginx package with apt:
$ sudo apt install python3-certbot-nginx 

# Confirming Nginx's Configuration 
> Certbox needs to be able to find the correct server block in your Nginx configuration for it to be able to automatically configure SSL. Specifically, it does this by looking for a server_name directive that matches the domain you request a certificate for.

$ sudo vim /etc/nginx/sites-available/your_domain.com   # create domain configure file 

    server_name your_domain.com www.your_domain.com 
$ sudo nginx -t 
    nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
    nginx: configuration file /etc/nginx/nginx.conf test is successful
$ sudo systemctl reload nginx   # reload Nginx to load the new configuration  
> Certbot can now find the correct server block and update it. 

# Obtaining an SSL Certificate 
> Certbot provides a variety of ways to obtain SSL certificates through plugins. The Nginx plugin will take care of reconfiguring Nginx and reloading the config whenever necessary. 

$ sudo certbot --nginx -d chyidl.com -d www.chyidl.com 
Saving debug log to /var/log/letsencrypt/letsencrypt.log
Plugins selected: Authenticator nginx, Installer nginx

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
You have an existing certificate that contains a portion of the domains you
requested (ref: /etc/letsencrypt/renewal/chyidl.com.conf)

It contains these names: chyidl.com

You requested these names for the new certificate: chyidl.com, www.chyidl.com.

Do you want to expand and replace this existing certificate with the new
certificate?
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
(E)xpand/(C)ancel: E
Renewing an existing certificate
Performing the following challenges:
http-01 challenge for chyidl.com
http-01 challenge for www.chyidl.com
Waiting for verification...
Cleaning up challenges
Deploying Certificate to VirtualHost /etc/nginx/sites-enabled/chyidl.com
Deploying Certificate to VirtualHost /etc/nginx/sites-enabled/chyidl.com

Please choose whether or not to redirect HTTP traffic to HTTPS, removing HTTP access.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
1: No redirect - Make no further changes to the webserver configuration.
2: Redirect - Make all requests redirect to secure HTTPS access. Choose this for
new sites, or if you're confident your site works on HTTPS. You can undo this
change by editing your web server's configuration.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Select the appropriate number [1-2] then [enter] (press 'c' to cancel): 2
Redirecting all traffic on port 80 to ssl in /etc/nginx/sites-enabled/chyidl.com
Redirecting all traffic on port 80 to ssl in /etc/nginx/sites-enabled/chyidl.com

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Your existing certificate has been successfully renewed, and the new certificate
has been installed.

The new certificate covers the following domains: https://chyidl.com and
https://www.chyidl.com

You should test your configuration at:
https://www.ssllabs.com/ssltest/analyze.html?d=chyidl.com
https://www.ssllabs.com/ssltest/analyze.html?d=www.chyidl.com
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

IMPORTANT NOTES:
 - Congratulations! Your certificate and chain have been saved at:
   /etc/letsencrypt/live/chyidl.com/fullchain.pem
   Your key file has been saved at:
   /etc/letsencrypt/live/chyidl.com/privkey.pem
   Your cert will expire on 2020-01-31. To obtain a new or tweaked
   version of this certificate in the future, simply run certbot again
   with the "certonly" option. To non-interactively renew *all* of
   your certificates, run "certbot renew"
 - If you like Certbot, please consider supporting our work by:

   Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
   Donating to EFF:                    https://eff.org/donate-le

# Verifying Certbot Auto-Renewal 
> Let's Encrypt's certificates are only valid for ninety days. This is to encourage users to automate their certificate renewal process. The certbot package we installed takes care of this for us by adding a renew script to /etc/cron.d. This script runs twice a day and will automatically renew any certificate that's within thiry days of expiration. 

$ sudo certbot renew --dry-run  # to test the renewal process 

Step3 - Using Webmin
> Webmin has modules that can control everything from the BIND DNS Server to something as simple as adding users to the system.

> Mapping Domain to IP (Configure DNS)
https://ping.eu 
Online Ping, Traceroute, DNS lookup, WHOIS, Port check, Reverse lookup, Proxy checker, Bandwidth meter, Network calculator, Network mask calculator, Country By IP, Unit converter.

> Reverse DNS (From IP GET DNS)
> Set the MX Record 
> Install Roundcude Web Mail System 
    Roundcube webmail is a browser-based multilingual IMAP client with an application-like user interface. It provides full functionality you expect from an email client, including MIME support, address book, folder manipulation, message searching and spell checkking. It a great way to bring all your external mails like Google. Yahoo, and other SMTP inboxes onto your own server. 

    - Modern user interface.
    - Cmplete support of IMAP and SMTP protocols including SSL and STARTTLS. 
    - Sieve scripts (Filters and vacation message).
    - Minimalistic resources requirements.
    - Multilingual capabilities 
    - Find-as-you-type address book 
    - Richtext/HTML message composing 
    - Searching messages and contacts 
    - Shared folders and ACL 

    1. Step 1: Install Nginx HTTP Server 
        $ sudo apt-get update 
        $ sudo apt-get install nginx 
        $ sudo systemctl stop|start|enable nginx.server 
    2. Step 2: Install MariaDB Database Server 
        $ sudo apt-get install mariadb-server mariadb-client 
        $ sudo systemctl stop|start|enable mysql.service|mariadb.service 
        $ sudo mysql_secure_installation    # secure MariaDB server by creating a root password and disabllowing remote root access.
    3. Step 3: Install PHP 7.2-FPM and Related Modules 
        $ sudo apt-get install software-properties-common 
        $ sudo add-apt-repository ppa:ondrej/php 
        $ sudo apt update
        $ sudo apt install php7.2-fpm php7.2-common php7.2-curl php7.2-mbstring php7.2-xmlrpc php7.2-mysql php7.2-gd php7.2-xml php7.2-intl php7.2-ldap php7.2-imagick php7.2-json php7.2-cli
```
```
# Mail Server with Webmin WHM 

```

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
