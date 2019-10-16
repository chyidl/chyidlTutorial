Getting Started with Centos
---------------------------

```
# Install Software Updates
The first thing you should to update the Linux distribution's packages. This applies the latest security patches and bug fixes to help protect VPS
$ yum update    # CentOS
$ sudo apt-get update && apt-get upgrade    # Debian/Ubuntu 

# Set the Hostname 
A hostname is used to identify VPS and easy-to-remember name.

Arch/CentOS 7/Debian 8/Fedora /Ubuntu 16.04 and above
Replace example_hostname with one of your choice.
$ hostnamectl set-hostname example_hostname

CentOS 6
Replace hostname with one of your choice.
$ echo "HOSTNAME=example_hostname" >> /etc/sysconfig/network 
$ hostname "hostname"

# Update Your System's hosts File 
The hosts file creates static associations between IP addresses and hostnames or domains which the system prioritizes before DNS for name resolution. 

# Set the Timezone 
All new VPS will be set to UTC time by default. However, you may prefer your VPS use the time zone which you live in so log file timestamps as relative to your local time.

Arch Linux / CentOS 7/Fedora 
$ timedatectl list-timezones    # View all available time zones 
Use the Up, Down, Page Up and Page Down keys to navigate. Copy the time zone you want as a mouse selection. The press q to exit the list.
Set the time zone (for example, Asia/Shanghai)
$ timedatectl set-timezone 'Asia/Shanghai'

# Check the Time 
Use the date command to view the current date and time according to your server.
[root@prod-jumpmachine ~]# date
Mon Oct 14 10:46:11 CST 2019
```

Secure Your Server
------------------
```
# Update Your System-Frequently

Keeping your software up to date is the single biggest security precaution you can take for any operating system.Software updates range from critical vulnerability patches to minor bug fixes, and many software vulnerabilities are actually by the time they become public.

# Automatic Security Updates 
    1. CentOS uses yum-cron for automatic updates.
        The yum-cron RPM package provides a service which is started automatically. 
        $ yum install -y yum-cron 
        $ vim /etc/yum/yum-cron.conf 
            apply_updates = yes 
        yum-cron updates your system every time when there are new updates available.
    2. Debian and Ubuntu use unattended upgrades.
        
# Add a Limited User Account 
recommend creating a limited user account and using that all times. Administrative tasks will be done using sudo to temporarily evevate your limited user's privileges so you can administer your server.

CentOS / Fedora 
    # Create the user, replacing example_user with your desired username, and assign a password:
    $ useradd example_user && paddwd example_user 
    
    # Add the user to the wheel group for sudo privileges:
    $ usermod -aG wheel example_user 

Ubuntu
    # Create the user, replacing example_user with your desired username. You'll then be aksed to assign the user a password:
    $ adduser example_user 
    
    # Add the user to the sudo group so you'll have administrative privileges:
    $ adduser example_user sudo 

# Harden SSH Access 
    By default, password authentication is used to connect to your VPS via SSH. A cryptographic key-pair is more secure because a private key takes the place of a password, which is generally much more diffcult to brute-force. In this section we'll create a key-pair and configure the VPS to not accept passwords for SSH logins.

    # Create an Authentication Key-pair 
        1. This is done on your local computer and will create a 4096-bit RSA key-pair. 
            $ ssh-keygen -b 4096    # Linux/OS X/Windows 10 
            # default names id_rsa and id_rsa.pub before entering your passphrase. On Linux and OSX, these files will be saved in /home/your_username/.ssh directory. on Windwos, thet will be saved in C:\Users\MyUserName\.ssh 
        2. Upload the public key to your VPS.
            # Linux -- From your local computer 
            $ ssh-copy-id example@vps_ip              
            
            # OS X 
            On your vps(while signed in as your limited user)
            $ mkdir -p ~/.ssh && sudo chmod -R 700 ~/.ssh/ 
            From your local computer 
            $ scp ~/.ssh/id_rsa.pub example_user@vsp_ip:~/.ssh/authorized_keys 

# SSH Daemon Options
    1. Disallow root logins over SSH. 
        $ sudo vim /etc/ssh/sshd_config 
            PermitRootLogin no 
    2. Disable SSH password authentication. This requires all users connecting via SSH to use key authentication.
        $ sudo vim /etc/ssh/sshd_config 
            # Change to no to disable tunnelled clear text passwords
            PasswordAuthentication no 
    3. Listen on only one internet protocol. The SSH daemon listens for incoming connections over both IPv4 and IPv6 by default. Unless you need to SSH into your vps using both protocols, disable whichever you do not need. 
        $ sudo vim /etc/ssh/sshd_config 
            AddressFamily inet      # to listen only on IPv4 
            AddressFamily inet6     # to listen only on IPv6 
    4. Restart the SSH service to load the new configuration. 
        $ sudo systemctl restart sshd   # If you're using a Linux distribution which uses systemd (CentOS 7, Debian 8, Fedora, Ubuntu 15.10+)
        OR
        $ sudo service sshd restart # If your init system is SystemV or Upstart (CentOS 6, Debian 7, Ubuntu 14.04)
```

Remove Unused Network-Facing Services
-------------------------------------
```
Most Linux distributions install with running network services which listen for incoming connections from the internet, the loopback interface, or a combination of both. Network-facing services which are not need should be removed from the system to reduce the attack surface of both running processes and installed packages.

# Determine Running Services 
$ sudo ss -atpu 
Netid    State          Recv-Q      Send-Q                 Local Address:Port                   Peer Address:Port      
tcp      LISTEN         0           128                          0.0.0.0:ssh                         0.0.0.0:*          users:(("sshd",pid=1686,fd=3))
tcp      ESTAB          0           0                      192.168.1.243:ssh                   192.168.1.251:49695      users:(("sshd",pid=16244,fd=3),("sshd",pid=16132,fd=3))
tcp      LISTEN         0           128                             [::]:ssh                            [::]:*          users:(("sshd",pid=1686,fd=4))

TCP - Peer Address:Port 
    0.0.0.0:*, which translates into any incoming IPv4 address to any port, and over any network interface.
    [::]:*, sshd process listening for any incoming SSH connections over IPv6 to any port, and again over any network interface.
    LISTEN, ESTABLISHED, CLOSE_WAIT 

UDP - UDP sockets are stateless
    UDP sockets are stateless, meaning they are either open or closed and every process's connection is independent of those which occurred before and after. 

# Uninstall the Listening Services 
CentOS
$ sudo yum remove package_name 

Debian/Ubuntu
$ sudo apt purge package_name 

Fedora
$ sudo dnf remove package_name 

# Configure a Firewall 
Using a firewall to block unwanted inbound traffic to your VPS provides a highly effective security layer. A best practice is to allow only the traffic you need, and deny everything else. 
    Iptables: is the controller for netfilter, the Linux kernel's packet filtering framework. Iptables is included in most List distributions by default.
    FirewallID: is the iptables controller available for the CentOS / Fedora family of distributions.
    UFW: provides an iptables fontend for Debian and Ubuntu 
```
