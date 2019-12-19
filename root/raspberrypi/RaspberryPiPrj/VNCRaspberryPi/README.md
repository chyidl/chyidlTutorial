Display your Raspberry Pi's desktop
===================================

> VNC (Virtual Network Computing). VNC is a standard, widely supported way of securely presenting a GUI remotely over a network connection. You need a suitable server running on the machine that will be sharing its desktop, and a client app to present that desktop on the computer you're accessing the remote machine from. The client relays your mouse and keyboard input back to the remote computer.

> The Raspberry Pi Foundation recommends a specific VNC server, tightvncserver, written by TightVNC Software. You can install in the usual way:
```
$ sudo apt-get install tightvncserver 

# When the software has downloaded and installed, it's ready to run:
$ tightvncserver 
# You will be asked to set up an remote access control password and to enther it a second time, as verification. You'll also be asked if you'll like to enter a password for view-only access. This is optional. I just entered 'n' for no.

Apple has long provided Apple Remote Desktop (ARD), a tool for remotely accessing Mac desktop. Over the years, it has gained support for a variety of remote access technologies, including VNC.

ARD doesn't live in the Applications folder - it's actually buried deep in the System folder - but it can be launched via finder: just hit Command-K to invoke the standard Mac 'Connect to Server' dialog. Here, enter:
vnc://pi.local:5901

By default tightvncserver establishes an 800 x 400 desktop, but you can change the using the -geometry switch. You can set the colour depth using the -depth switch too. 
$ tightvncserver -geometry 800x600 -depth 24

# Of course, the bigger the desktop and the higher the colour depth, the more data needs to be sent to Pi to Mac, and the slower and less responsive the remote system will feel. Experment to find the size you prefer.
```

Install and Configure VNC on Ubuntu 
-----------------------------------
```
$ uname -a 
Linux RPi3BPlus 4.15.0-1049-raspi2 #53-Ubuntu SMP PREEMPT Wed Oct 2 01:04:00 UTC 2019 aarch64 aarch64 aarch64 GNU/Linux

# set up a VNC server on an Ubuntu 18.04 server and connect to it securely through an SSH tunnel. TightVNC, a fast and lightweight remote control package. will ensure vnc connection will be smooth and stable even on slower internet connections.

Step 1 - Installing the Desktop Environment and VNC Server 
    $ sudo apt update   # update list of package 
    $ sudo apt install xfce4 xfce4-goodies  # install Xfce desktop environment  
    $ sudo apt install tightvncserver   # install TightVNC server 
    # Complete the VNC server's initial confuguration, use the vncserver command to set up a secure password and create the initial configuration files:
    $ vncserver     # set up a secure password and create the initial configuration files (password must be between six and eight characters long, Passwords more than 8 characters will be truncated automatically)

Step 2 - Configuring the VNC Server 
    $ vncserver -kill :1    # stop the VNC server instance that is running on port 5901
    $ vim ~/.vnc/xstartup 
        #!/usr/bin/env bash 
        xrdb $HOME/.Xresources          # .Xresources is where a user can make change to certain settings of the graphical desktop, like terminal colors, cursor themes, and font rendering.
        startxfce4 &                    # launch Xfce 
    $ vncserver     # Restart the VNC server 

Step 3 - Connecting the VNC Desktop Securely 
    VNC itself doesn't use secure protocols when connecting. We'll use an SSH tunnel to connect securely to our server, and then tell our VNC client to use that tunnel rather than making a direct connection. 
    ... 

Step 4 - Running VNC as a System Service 
    Set up the VNC server as a systemd service
    $ sudo vim /etc/systemd/system/vncserver@.service       # The @ symbol at the end of the name will let us pass in an argument we can use in the service configuration. we will use this to specify the VNC display port we want to use when we manage the service 
[Unit]
Description=Start TightVNC server at startup 
After=syslog.target network.target 

[Service]
Type=forking
User=pi
Group=pi 
WorkingDirectory=/home/pi
PIDFile=/home/pi/.vnc/%H:%i.pid
ExecStartPre=-/usr/bin/vncserver -kill :i > /dev/null 2>&1          # stop VNC if it's already running 
ExecStart=/usr/bin/vncserver -depth 24 -geometry 1920x1080 :%i 
ExecStop=/usr/bin/vncserver -kill :%i 

[Install]
WantedBy=multi-user.target
    $ sudo systemctl daemon-reload  # make the system aware of the new unit file 
    $ sudo systemctl enable vncserver@1.service 
    $ sudo systemctl start|status| vncserver@1
```