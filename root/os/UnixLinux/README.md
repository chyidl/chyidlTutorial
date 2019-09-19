GNU/Linux Operating System 
==========================

The GNU Manifesto
-----------------

* What's GNU? Gnu's Not Unix!
    GNU, which stands for Gnu's Not Unix, is the name for the complete Unix-compatible software system. 
    The GNU Project set out to develop a complete free Unix-like system: GNU 
    Once Trovalds freed Linux in 1992, it fit into the last major gap in the GNU system. People could then combine Linux with the GNU system to make a complete free system -- a version of the GNU system which also contained Linux. The GNU/Linux system, in other words. 

Linux and the GNU System
------------------------

Linux is the kernel: the program in the system that allocates the machine's resources to the other programs that you run. The kernel is an essential part of an operating system, but useless by itself; it can only function in the context of a complete operating system. Linux is normally used in combination with the GNU operating system: the whole system is basically GNU with Linux added. or GNU/Linux. All the so-called "Linux" distributions are really distributions of GNU/Linux.

Today there are many different variants of the GNU/Linux system (often called "distros"). 

Add a User to a Group on Linux
------------------------------
```
# add a New Group 
$ sudo groupadd mynewgroup 

# Add an existing User Account to a Group 
$ sudo usermod -a -G examplegroup exampleusername 

# Change a User's Primary Group 
# While a user account can be part of multiple groups, one of the groups is alwasys the "primary group" and the others are "secondary groups".
$ sudo usermod -g groupname username 

# View the Groups a User Account is Assigned To 
$ groups 

# To View the numericial IDs associated with each group, run the id command instead.
$ id 

# View All Groups on the System
$ getent group 
```

How to Change the Timezone in Linux
-----------------------------------
```
1. Open Terminal 

2. Check your current time zone
➜  ~ cd /usr/share/zoneinfo
➜  zoneinfo tzselect
Please identify a location so that time zone rules can be set correctly.
Please select a continent, ocean, "coord", or "TZ".
 1) Africa
 2) Americas
 3) Antarctica
 4) Asia
 5) Atlantic Ocean
 6) Australia
 7) Europe
 8) Indian Ocean
 9) Pacific Ocean
 10) coord - I want to use geographical coordinates.
 11) TZ - I want to specify the time zone using the Posix TZ format.
#? 4
Please select a country whose clocks agree with yours.
 1) Afghanistan           18) Israel                35) Palestine
 2) Armenia               19) Japan                 36) Philippines
 3) Azerbaijan            20) Jordan                37) Qatar
 4) Bahrain               21) Kazakhstan            38) Russia
 5) Bangladesh            22) Korea (North)         39) Saudi Arabia
 6) Bhutan                23) Korea (South)         40) Singapore
 7) Brunei                24) Kuwait                41) Sri Lanka
 8) Cambodia              25) Kyrgyzstan            42) Syria
 9) China                 26) Laos                  43) Taiwan
 10) Cyprus                27) Lebanon               44) Tajikistan
 11) East Timor            28) Macau                 45) Thailand
 12) Georgia               29) Malaysia              46) Turkmenistan
 13) Hong Kong             30) Mongolia              47) United Arab Emirates
 14) India                 31) Myanmar (Burma)       48) Uzbekistan
 15) Indonesia             32) Nepal                 49) Vietnam
 16) Iran                  33) Oman                  50) Yemen
 17) Iraq                  34) Pakistan
#? 13

The following information has been given:

            Hong Kong

Therefore TZ='Asia/Hong_Kong' will be used.
Local time is now:      Thu Sep 19 13:42:41 HKT 2019.
Universal Time is now:  Thu Sep 19 05:42:41 UTC 2019.
Is the above information OK?
1) Yes
2) No
#? 1

You can make this change permanent for yourself by appending the line
        TZ='Asia/Hong_Kong'; export TZ
to the file '.profile' in your home directory; then log out and log in again.

Here is that TZ value again, this time on standard output so that you
can use the /usr/bin/tzselect command in shell scripts:
Asia/Hong_Kong

3. Set clock to stay synced with internet time servers 
    $ sudo apt-get install ntpdate 
```

Set Up Time Synchronization 
---------------------------
> Accurate timekeeping has become a critical component of modern software deployments. Whether it's making sure logs are recorded in the right order or database updates are applied correctly, out-of-sync time can cause errors, data corruption, and other hard to debug issues.
```
# Navigating Basic Time Commands 
$ date 

# list the available time zones
$ timedatectl list-timezones 

# set the time zone with timedatectl set-timezone
$ sudo timedatectl set-timezone Asia/Hong_Kong

# verify your changes by running date again
$ date 

# query the status of timesyncd by running timedatectl with no arguments.
$ timedatectl
                      Local time: Sat 2019-03-16 13:14:41 HKT
                  Universal time: Sat 2019-03-16 05:14:41 UTC
                        RTC time: Sat 2019-03-16 05:14:42  (Real time Clock)
                       Time zone: Asia/Hong_Kong (HKT, +0800)
       System clock synchronized: yes
systemd-timesyncd.service active: yes
                 RTC in local TZ: no

# If timesyncd isn't enabled, turn it on with timedatectl 
$ sudo timedatectl set-ntp on|yes
```
