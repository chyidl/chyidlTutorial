Use Fail2ban to Secure Your Server
==================================

What is Fail2Ban
----------------
> Fail2ban is a log-parsing application that monitors system logs for symptoms of an automated attack on your VPS.When an attempted compromise is located, using the defined parameters, Fail2ban will add a new rule to iptables to block the IP address of the attacker, either for a set amount of time or permanently. Fail2ban can also alert your through email that an attack is occuring.

> Fail2ban is primarily focused on SSH attacks, althoug it can be further confgured to work for any service that uses log files and can be compromise.

Install Fail2ban 
----------------
```
CentOS 7
    1. Ensure your system is up to date and install the EPEL repository:
        $ yum update && yum install epel-release 
    2. Install Fail2Ban 
        $ yum install fail2ban 
    3. Install Sendmail if you additionally would like email support. Sendmail is not required to use Fail2Ban 
        $ yum install sendmail 
    4. Start and enable Fail2ban and, if needed, Sendmail: 
        $ systemctl start fail2ban 
        $ systemctl enable fial2ban 
        $ systemctl start sendmail 
        $ systemctl enable sendmail 

Ubuntu
    1. Ensure your system is up to date 
        $ apt-get update && apt-get upgrade -y
    2. Install Fail2ban
        $ sudo apt-get install fail2ban     # the service will automatically start 
    3. (Optional) If you would like email support, install Sendmail:
        $ sudo apt-get install sendmail 
    4. Allow SSH access through UFW and then enable the firewall 
        $ ufw allow ssh 
        $ ufw enable 
```

Configure Fail2ban 
------------------
```
Fail2ban reads .conf configuration files first, the .local files override any settings. all changes to the configuration are generally done in .local files, leaving the .conf files untouched.

# Configure fail2ban.local 
    1. fail2ban.conf contains the default configuration profile. The default settings will give you a reasonable working setup. If you want to make any changes, it's best to do it in a separate file, faile2ban.local, which override fail2ban.conf. Rename a copy fail2ban.conf to fail2ban.local 
        $ cp /etc/fail2ban/fail2ban.conf /etc/fail2ban/fail2ban.local 
    2. edit the definitions in fail2ban.local to match your desired configuration.
        $ sudo vim /etc/fail2ban/fail2ban.local 
            loglevel: The level of detail that Fail2ban 
            logtarget: Logs actions into a specific file. 
            socket: The location of the socket file.
            pidfile: The location of the PID file

# Configure jail.local Settings 
    1. The jail.conf file will enable Fail2ban for SSH by default for Debian and Ubuntu, but not CentOS. but not CentOS, ALl other protocols and cofigurations (HTTP, FTP, etc.) are commented out. 
        $ cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local 
    2. If using CentOS or Fedora you will need to change the backend option in jail.local from auto to systemd.
        $ sudo vim /etc/fail2ban/jail.local 
            backend = systemd 
        # No jails are enabled by default in CentOS 7. For example, to enable the SSH daemon jail, uncomment the following lines in jail.local
            [sshd]
            enabled = true
    3. whitelist IP, add them to the ignoreip line. 
        $ sudo vim /etc/fail2ban/jail.local 
            ignoreip = 127.0.0.1/8 ::1
    4. Ban Time and Retry Amount
        Set bantime, findtime, and maxretry to define the circumstances and the length of time of a ban:
        $ sudo vim /etc/fail2ban/jail.local 
            bantime = 10m       # The length of time in seconds for which an IP is banned. If set to a negative number, the ban will be permanent. 
            findtime = 10m      # The length of time between login attempts before a ban is set. 
            maxretry = 3        # How many attempts can be made to access the server from a single IP before a ban is imposed 

# Email Alerts
    To receive email when fail2ban is triggered, adjust the email settings:
        destemail: The email address where you would like to receive the emails.
        sendername: The name under which the email shows up.
        sender: The email address from which Fail2ban will send emails.
```
