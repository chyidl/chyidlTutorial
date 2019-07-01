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
