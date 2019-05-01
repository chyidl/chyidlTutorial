Apple Airplay on Raspberry Pi
=============================
> Make Raspberry Pi into an AirPlay receiver. With Apple having officially discontinued line of AirPort routers, including the AirPlay-enabled AirPort Express, using a Raspberry Pi to fill the gap has become an even more appealing option. There's a reliable third-party community that regularly updates the open-sourced software.

Configure the Airplay Server
----------------------------
* 1.Install Dependencies
```
    First off, you'll need to install some dependencies so you can build the Airplay server application., Run the following:
    $ sudo apt-get update
    $ sudo apt-get install autoconf automake avahi-daemon build-essential git libasound2-dev libavahi-client-dev libconfig-dev libdaemon-dev libpopt-dev libssl-dev libtool xmltoman 
```

* 2.Build & Install shairport-sync 
```
    shairport-sync turns your Linux machine into an Apple Airplay server. One of the best things about it is that it runs entirely on the command line, and while it has a million configuration options, it's surprisingly easy to get working out of the box.
    
    First grab it from github:
    $ git clone https://github.com/mikebrady/shairport-sync.git 
    $ cd shairport-sync 
    $ autoreconf -i -f 
    $ ./configure --with-alsa --with-avahi --with-ssl=openssl --with-systemd --with-metadata 
    
    Finally build and install the application
    $ make -j4 
    $ sudo make install
```

* 3.Configure the Audio Output
```
    Now you need to configure the audio path on Raspberry Pi. It's generally set to "auto" but you need to force it to go the 3.5mm jack. 
    $ sudo raspi-config 
```

* 4.Set the Volume 
```
    The Volume can tend to be very low, so change it to max using 
    $ amixer sset PCM,0 100% 
```

* 5.Test Airplay to the Raspberry Pi 
```
    Now start shairport-sync with:
    $ sudo service shairport-sync start
```

* 6.Configure shairport-sync to Start Automatically 
```
    start servicely manually: want shairport-sync to run as soon as the Pi has booted
    $ sudo systemctl enable shairport-sync
```

* 7.Prevent Wifi Dropouts
```
    The Raspberry Pi wifi will tend to go into power-saving mode periodically, which can cause serious audio glitching when using Airplay.
    $ sudo vim /etc/network/interfaces
    Go to the end of the file and add the lines:
        # Disable wifi power management 
        wireless-power off 
```

Show Artist & Song Metadata Using Airplay on Raspberry Pi
=========================================================

Enable Airplay Metadata
-----------------------
```
$ sudo vim /usr/local/etc/shairport-sync.conf 

Now search for metadata entry, First of all, uncomment it all and change the enabled filed to "yes"

// How to deal with metadata, including artwork
metadata =
{
    enabled = "yes"; // set this to yes to get Shairport Sync to solicit metadata from the source and to pass it on via a pipe
    include_cover_art = "no"; // set to "yes" to get Shairport Sync to solicit cover art from the source and pass it via the pipe. You must also set "enabled" to "yes".
    pipe_name = "/tmp/shairport-sync-metadata";
    pipe_timeout = 5000; // wait for this number of milliseconds for a blocked pipe to unblock before giving up
    socket_address = "226.0.0.1"; // if set to a host name or IP address, UDP packets containing metadata will be sent to this address. May be a multicast address. "socket-port" must be non-zero and "enabled" must be set to yes"
    socket_port = 5555; // if socket_address is set, the port to send UDP packets to
    socket_msglength = 65000; // the maximum packet size for any UDP metadata. This will be clipped to be between 500 or 65000. The default is 500.
};

You've now enabled the metadata steaming

$ sudo systemctl restart shairport-sync 

When you start playing something via Airplay now, the metadata will be sent through a Unix pipe. Pipes allow programs to communicate with each other asynchronously. They're similar to network socket, but much easier to use.

The pipe_name mentioned in the shairport-sync.conf file above happens to be /tmp/shairport-sync-metadata, so you can dump the contents of the pipe just like a file:

$ cat /tmp/shairport-sync-metadata 

This should display raw data every time you change track. 

$ sudo cat /tmp/shairport-sync-metadata
<item><type>73736e63</type><code>666c7372</code><length>10</length>
<data encoding="base64">
MTUzMjk4Mzc2OA==</data></item>
<item><type>73736e63</type><code>70666c73</code><length>0</length></item>
<item><type>73736e63</type><code>70666672</code><length>0</length></item>
<item><type>73736e63</type><code>70726772</code><length>32</length>
<data encoding="base64">
MTUzMjk4NzEyMC8xNTMyODkzOTI4LzE1NDA3OTYwODA=</data></item>
<item><type>73736e63</type><code>7072736d</code><length>0</length></item>
<item><type>73736e63</type><code>70766f6c</code><length>25</length>
<data encoding="base64">
LTE0LjQxLC0yNy4xOCwtOTYuMzAsMC4wMA==</data></item>
<item><type>73736e63</type><code>70766f6c</code><length>25</length>
<data encoding="base64">
LTE0Ljg1LC0yOC40NiwtOTYuMzAsMC4wMA==</data></item>
<item><type>73736e63</type><code>70766f6c</code><length>25</length>
<data encoding="base64">
LTE1LjE5LC0yOS40MywtOTYuMzAsMC4wMA==</data></item>
<item><type>73736e63</type><code>70766f6c</code><length>25</length>
<data encoding="base64">

Now that proves you're receiving information from the Airplay client. The airtist, album and track names are encoded in base64 format which enables them to be sent safely inside XML.

$ git clone https://github.com/mikebrady/shairport-sync-metadata-reader.git 
$ cd shairport-sync-metadata-reader 
$ autoreconf -i -f 
$ ./confugure 
$ make
$ sudo make install 

What you have done here is built a program called shairport-sync-metadata-reader. Now you're ready to decode the metadata.
$ sudo systemctl restart shairport-sync

Now check the metadata decodes correctly by sending the output of the pipe into the shairport-sync-metadata-reader 
$ shairport-sync-metadata-reader < /tmp/shairport-sync-metadata

At this point you should see something useful, such as:
$ shairport-sync-metadata-reader < /tmp/shairport-sync-metadata
"ssnc" "snua": "AirPlay/375.3".
"ssnc" "acre": "1310186374".
"ssnc" "daid": "C2E9F5D5D502353".
Client's IP: "fe80::8f8:e61f:6e75:5f3e".
"ssnc" "svip": "fe80::299a:94bb:bcb3:5100".
"ssnc" "pbeg": "".
"ssnc" "pvol": "-15.59,-30.60,-96.30,0.00".
"ssnc" "pvol": "-15.59,-30.60,-96.30,0.00".
"ssnc" "prgr": "3347162622/3349623128/3358798334".
"ssnc" "flsr": "3349718073".
"ssnc" "mdst": "3349624367".
Persistent ID: "577615886".
Album Name: "A Head Full of Dreams".
Artist: "Coldplay".
Composer: "Guy Berryman, Jonny Buckland, Will Champion & Chris Martin".
Genre: "Alternative rock".
Title: "Adventure of a Lifetime".
"ssnc" "mden": "3349624367".
"ssnc" "prgr": "3347162074/3349624367/3358797786".
"ssnc" "pffr": "".
"ssnc" "mdst": "3349625071".
 
 Woohoo! There you have it, album Name, Aritist, Composer, Genre and Title fields are all filled in.
```

![Airplay on Raspberry Pi](/imgs/raspberrypi/airplay-raspberrypi.png?raw=true)
