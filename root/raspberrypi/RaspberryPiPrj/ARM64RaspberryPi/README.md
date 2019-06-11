ARM64 Ubuntu Raspberry Pi
=========================
* ARMHF vs ARM64 
> ARMHF stands for "arm hard float", and is the name given to a debian port for arm processors(armv7+) that have hardware floating point support.
> ARM64 supports hardware floating point and NEON by default
```
Raspberry Pi 3B + Raspbian 9 
$ uname -a
Linux RPi3B 4.14.98-v7+ #1200 SMP Tue Feb 12 20:27:48 GMT 2019 armv7l GNU/Linux

Raspberry Pi 3BPlus + Ubuntu ARM64 
$ uname -a
Linux RPi3BPlus 4.15.0-1034-raspi2 #36-Ubuntu SMP PREEMPT Fri Apr 5 06:21:41 UTC 2019 aarch64 aarch64 aarch64 GNU/Linux

'arm64' is the Debian port name for the 64-bit ARMv8 architecture,referred to as 'aarch64' in upstream toolchains (GNU triplet aarch64-linux-gnu), and some other distros.

```

* How to determine python 32bit or 64bit mode
```
ne way is to look at sys.maxsize
$ python3 -c 'import sys;print("%x" % sys.maxsize, sys.maxsize > 2**32)'
('7fffffff', False)

$ python3 -c 'import sys;print("%x" % sys.maxsize, sys.maxsize > 2**32)'
7fffffffffffffff True
```

* First boot (Username/Password)
> The login username is "ubuntu", password is "ubuntu". You will be asked to change the password on first login.

> Create a sudo user "$ sudo adduser new_user", and add "new_user" to "sudo" group, "$ sudo usermod -aG sudo new_user"

* Setting on-board Wi-Fi up on Raspberry Pi via the command line  
```

Setup WiFi on Raspberry Pi 2B Using USB Dongle
1. Check for USB WiFi Dongle Hardware
# To check whether the Raspberry Pi detected the WiFi Dongle hardware that is plugged in to the USB port, type the following command in the terminal and hit enter.
$ lsusb
Bus 001 Device 006: ID 0a12:0001 Cambridge Silicon Radio, Ltd Bluetooth Dongle (HCI mode)
Bus 001 Device 005: ID 0d8c:013c C-Media Electronics, Inc. CM108 Audio Controller
Bus 001 Device 004: ID 148f:5370 Ralink Technology, Corp. RT5370 Wireless Adapter
Bus 001 Device 003: ID 0424:ec00 Standard Microsystems Corp. SMSC9512/9514 Fast Ethernet Adapter
Bus 001 Device 002: ID 0424:9514 Standard Microsystems Corp. SMC9514 Hub
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

Step1:
$ sudo apt-get install wireless-tools 

Step2:
$ sudo apt-get install wpasupplicant , ifupdown

Step3: add below content to /etc/network/interfaces(Network Interfaces File):
auto wlan0
allow-hotplug wlan0
iface wlan0 inet dhcp
wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf 

Step4: Adding the network details to the Raspberry Pi
$ sudo vim /etc/wpa_supplicant/wpa_supplicant.conf (WPA Supplicant File)
country=CN 

network={
    ssid="XXX"
    psk="XXX"
    id_str="home"
}

# Hidden networks 
network={
    ssid="yourHiddenSSID"
    scan_ssid=1
    psk="Your_wifi_password"
    id_str="cpmpany"
}

Getting WiFi network details

Reboot the Raspberry Pi 

This will list all available WiFi networks
$ sudo iwlist wlan0 scan 

verfiy whether has successful connected 
$ sudo ifconfig wlan0 
$ sudo iwconfig 
```

* Timezone, locale
```
Check Current Timezone Settings 
$ timedatectl # Use the timedatectl command to show the current timezone and time

Show all Available Timezones 
$ timedatectl list-timezones | grep -i Asia/Hong_Kong
Asia/Hong_Kong

Change Timezone 
$ sudo timedatectl set-timezone Asia/Hong_Kong 
```

* Swap 
```
There is no swap partition/file included. If you want swap, it's recommended you do:
$ sudo apt-get install dphys-swapfile

STOP THE SWAP 
$ sudo dphys-swapfile swapoff 

MODIFY THE SIZE OF THE SWAP 
As root, edit the file /etc/dphys-swapfile and modify the variable CONF_SWAPSIZE:
CONF_SWAPSIZE=1024
To modify the swap file, edit the variable CONF_SWAPFILE, and run $ dphys-swapfile setup, which will create and initialize the file.

START THE SWAP 
$ sudo dphys-swapfile swapon
```

* Change swap size in Ubuntu 
```
Swap is a special area on your computer, which the operating system can use as additional RAM.

In the following example, we'll extend the swap space avilable in the /swapfile from 1GB to 2GB 

1. Turn off all swap processes
    $ sudo swapoff -a 

2. Resize the swap 
    $ sudo dd if=/dev/zero of=/swapfile bs=4M count=512
    if = input file 
    of = output file 
    bs = block size 
    count = multiplier of blocks 
    
    To Set the right permissions type:
    $ sudo chmod 600 /swapfile

3. Make the file usable as swap 
    Use the mkswap utility to set up the file as Linux swap area:
    $ sudo mkswap /swapfile 

4. Activate the swap file
    $ sudo swapon /swapfile 
    
    To make the change permanent open the /etc/fstab file and append the following line:
    /swapfile swap swap defaults 0 0 

5. Verify the swap status.
    $ sudo swapon --show 
    $ sudo free -h 

How to adjust the swappiness value
    Swappiness is a Linux kernel property that defines how often the system will use the swap space. Swappiness can have a value between 0 and 100.
    A low value will make the kernel to try to avoid swapping whenever possible while a higher value will make the kernel to use the swap more aggressively.

    The default swappiness value is 60. You can check the current swappiness value by typing the following command:
    $ cat /proc/sys/vm/swapiness
    
    While the swappiness value of 60 is OK for Desktops, for production servers you may need to set a lower value.
    For example, to set the swappiness value to 10, type:
    $ sudo sysctl vm.swappiness=10

    To make this parameter persistent across reboots append the following line to the /etc/sysctl.conf file:
    $ sudo vim /etc/sysctl.conf 
        vm.swappiness=10 

    The optimal swappiness value depends on your system workload and how the memory is being used. You should adjuest this parameter in small 
    increments to find an optimal value.


How to remove Swap File:
    01. First, deactivate the swap using the following command:
        $ sudo swapoff -v /swapfile 
    02. Remove the swap file entry /swapfile swap swap defaults 0 0  from the /etc/fstab file.
    03. Finally delete the actual swapfile file:
        $ sudo rm /swapfile 
```

* Headless VncServer Configuration 
```
configure accessing the pi with osx's Screen
1. $ sudo raspi-config > Interface Options > VNC > Enable.
2. Generate the password you wish to use in screen with vncpasswd -print 
pi@RPi2B:~ $ vncpasswd -print
Password:
Verify:
Password=bf8c3dcbaeaeb962267ad00c568c0850
3. Copy the output of that command(e.g.Password=bf8c3dcbaeaeb962267ad00c568c0850)for the config file.
4. Create and edit the following file here:
$ sudo vim /etc/vnc/config.d/common.custom 
5.Add the following config:
Encryption=PreferOn
Authentication=VncAuth
Password=bf8c3dcbaeaeb962267ad00c568c0850
6. Restart the vnc service:
$ sudo systemctl restart vncserver-x11-serviced 
7. Open Screen with the instructions above, and use the password you provided to vncpasswd.
mac> Finder > Go > Connect to Server... 
8. If you need to monitor the logs for vncserver, you can use journalctl
$ sudo journalctl -u vncserver-x11-serviced.service 
```

Install Multiple Tomcat Instances 8.5 and JDK 8 on One Raspberry
----------------------------------------------------------------
```
    Running multiple Tomcat Instances on one server
    Advanced Configuration - Multiple Tomcat Instance
    Running Multiple Tomcat Instances on Single Machine 

Understand Tomcat Directory Structure:
    bin     : This directory contains the startup and shudown scripts for both Windows and Linux.
    conf    : This directory contains the main configuration files for Tomcat. The two most important are the server.xml and the global web.xml
    server  : This directory contains the Tomcat Java Archive files.
    lib     : This directory contains Java Archive files that Tomcat is dependent upon.
    logs    : This directory contains Tomcat's log files 
    src     : This directory contains the source code used by the Tomcat server. Once Tomcat is released, it will probably contain interfaces and abstract classes only.
    webapps : All web applications are deployed in this directory; it contains the WAR file.
    work    : This is the directory in which Tomcat will place all servlets that are generated from JPSs. If you want to see exactly how a particular JSP is interpreted, look in this directory.

Tomcat server ports:
    Connector Port: This is the port where Apache Tomcat listen for the HTTP requests.
    Shutdown Port: This port is used when we try to shutdown the Apache Tomcat Server.
    AJP (Apache JServ Protocol) Connector Port: The Apache JServ Protocol (AJP) is a binary protocol that can conduct inbound requests from a web server through to an application server that sits behind the web server.
    Redirect Port: Any redirection happending inside Apache Tomcat will happen through this port.

Mac/Linux/Unix:
    ./catalina.sh start|stop

Kill process using command kill -9 <process ID>
$ kill -9 <PID>

Change HTTP, HTTPS, AJP, Shutdown Ports
File location: Tomcat/conf/server.xml 
    1: <Server port="9005" shutdown="SHUTDOWN">
    2: <Connector port="9080" protocol="HTTP/1.1"
            connectionTimeout="20000"
            redirectPort="9443" />
    3: <!-- Define an AJP 1.3 Connector on port 8009 -->
       <Connector port="9009" protocol="AJP/1.3" redirectPort="9443" />

The startup.sh and shutdown.sh script files make use of catalina.sh for performing the startup and shutdown operations.

$ vim catalina.sh 
# chyi_add 2019-05-29
export CATALINA_HOME=/root/chyi_backup/apache-tomcat-8.5.41
export CATALINA_BASE=/root/chyi_backup/apache-tomcat-8.5.41

The main different from running a single Tomcat instance is you need to set CATALINA_BASE to the directory you set up for the particular instance you want to start[or stop]

```

```
Apache Tomcat(or simply Tomcat) is an open source web server and servlet container developed by the Apache Software Foundation(ASF). Tomcat implements ths Java Servlet and the JavaServer Pages[JSP] specifications from Oracle Corporation, and provides a "pure Java" HTTP web server environment for Java code to run.


Tomcat Structure:
    Environment Variables:
        $CATALINA_HOME: This variable points to the directory where our server is installed.
        $CATALINA_BASE: This variable points to the direoctory of a particular instance of Tomcat.If this variable is not set explicitly. Then it will assigned the same value as $CATALINA_HOME 
        Web applications are deploy under the $CATALINA_HOME/webapps directory 

Step 1: Install OpenJDK 
$ sudo apt update 
# Install the OpenJDK package by running
$ sudo apt-get install openjdk-8-jdk 
# Add JAVA_HOME=/usr/lib/jvm/java-8-openjdk-arm64 
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-arm64 

Step 2: Create Tomcat User 
# For security purposes, create a new system user and group with home directory /opt/tomcat that will run the Tomcat service
$ sudo useradd -r -m -U -d /opt/tomcat -s /bin/false tomcat

Step 3: Install Tomcat 
# download the latest binary release of Tomcat 9 from Tomcat downloads page 
$ wget http://www-eu.apache.org/dist/tomcat/tomcat-9/v9.0.20/bin/apache-tomcat-9.0.20.tar.gz -P /tmp
# Once the download is completed, extract the Tomcat archive and move it to the /opt/tomcat directory 
$ sudo tar xf /tmp/apache-tomcat-9*.tar.gz -C /opt/tomcat
# To have more control over Tomcat versions and updates, we will create a symbolic link latest which will point to the Tomcat.
$ sudo ln -s /opt/tomcat/apache-tomcat-9.0.20 /opt/tomcat/latest
# change the directory ownership to user and group tomcat 
$ sudo chown -RH tomcat: /opt/tomcat/latest
# The scripts inside bin/ directory must have executable flag 
$ sudo sh -c 'chmod +x /opt/tomcat/latest/bin/*.sh'

Step 4: Create a systemd Unit File 
# To run Tomcat as a service we will create a new unit file. create a file named tomcat.service in the /etc/systemd/system/
$ sudo vim /etc/systemd/system/tomcat.service
t]
Description=Tomcat 9 servlet container
After=network.target

[Service]
Type=forking
User=tomcat
Group=tomcat
Environment="JAVA_HOME=/usr/lib/jvm/java-8-openjdk-arm64"
Environment="JAVA_OPTS=-Djava.security.egd=file:///dev/urandom -Djava.awt.headless=true"
Environment="CATALINA_BASE=/opt/tomcat/latest"
Environment="CATALINA_HOME=/opt/tomcat/latest"
Environment="CATALINA_PID=/opt/tomcat/latest/temp/tomcat.pid"
Environment="CATALINA_OPTS=-Xms512M -Xmx1024M -server -XX:+UseParallelGC"
ExecStart=/opt/tomcat/latest/bin/startup.sh
ExecStop=/opt/tomcat/latest/bin/shutdown.sh

[Install]
WantedBy=multi-user.target

# Save and close the file and notify systemd that we created a new unit file:
$ sudo systemctl daemon-reload 
# Start the Tomcat service by executing
$ sudo systemctl start tomcat 
# Check the service status with the following command:
$ sudo systemctl status tomcat 
# enable the Tomcat service to be automatically started at boot time:
$ sudo system enable tomcat 
```

Deploy a WAR File to Apache Tomcat 
----------------------------------
```
Deploying a web application to Apache Tomcat is very straightforward using a WAR(Web Archive) file. By deploying we are placing a zipped web application in a location on the file system where Tomcat can make the web page(s) available to the world.
```

Set Up Hacking Linux Kit on Raspberry Pi 
----------------------------------------
```
```
