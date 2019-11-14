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

How to Mount and Unmount File systems in Linux
----------------------------------------------
* Using the CLI (for a headless installation)
```
Step 1: Check the block devices and the file systems that are assigned to those block devices 
$ lsblk 
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sdb           8:16   1 14.7G  0 disk 
├─sdb1        8:17   1  200M  0 part 
└─sdb2        8:18   1 14.5G  0 part 
mmcblk0     179:0    0 29.8G  0 disk 
├─mmcblk0p1 179:1    0  256M  0 part /boot/firmware
└─mmcblk0p2 179:2    0 29.6G  0 part /

Step 2: What kind of devices is sdb?
$ sudo lshw 
rpi3b                       
    description: Computer
    product: Raspberry Pi 3 Model B Rev 1.2
    serial: 0000000048dcddd0
    width: 64 bits
    capabilities: smp cp15_barrier setend swp
  *-core
       description: Motherboard
       physical id: 0
     *-cpu:0
          description: CPU
          product: cpu
          physical id: 0
          bus info: cpu@0
          size: 1200MHz
          capacity: 1200MHz
          capabilities: fp asimd evtstrm crc32 cpuid cpufreq
     *-cpu:1
          description: CPU
          product: cpu
          physical id: 1
          bus info: cpu@1
          size: 1200MHz
          capacity: 1200MHz
          capabilities: fp asimd evtstrm crc32 cpuid cpufreq
     *-cpu:2
          description: CPU
          product: cpu
          physical id: 2
          bus info: cpu@2
          size: 1200MHz
          capacity: 1200MHz
          capabilities: fp asimd evtstrm crc32 cpuid cpufreq
     *-cpu:3
          description: CPU
          product: cpu
          physical id: 3
          bus info: cpu@3
          size: 1200MHz
          capacity: 1200MHz
          capabilities: fp asimd evtstrm crc32 cpuid cpufreq
     *-memory
          description: System memory
          physical id: 4
          size: 912MiB
  *-usbhost
       product: DWC OTG Controller
       vendor: Linux 4.15.0-1048-raspi2 dwc_otg_hcd
       physical id: 1
       bus info: usb@1
       logical name: usb1
       version: 4.15
       capabilities: usb-2.00
       configuration: driver=hub slots=1 speed=480Mbit/s
     *-usb
          description: USB hub
          product: SMC9514 Hub
          vendor: Standard Microsystems Corp.
          physical id: 1
          bus info: usb@1:1
          version: 2.00
          capabilities: usb-2.00
          configuration: driver=hub maxpower=2mA slots=5 speed=480Mbit/s
        *-usb:0
             description: Generic USB device
             product: SMSC9512/9514 Fast Ethernet Adapter
             vendor: Standard Microsystems Corp.
             physical id: 1
             bus info: usb@1:1.1
             version: 2.00
             capabilities: usb-2.00
             configuration: driver=smsc95xx maxpower=2mA speed=480Mbit/s
        *-usb:1
             description: Mass storage device
             product: ADATA USB Flash Drive
             vendor: ADATA
             physical id: 3
             bus info: usb@1:1.3
             logical name: scsi1
             version: 10.75
             serial: 237151605003011C
             capabilities: usb-2.10 scsi emulated scsi-host
             configuration: driver=usb-storage maxpower=200mA speed=480Mbit/s
           *-disk
                description: SCSI Disk
                product: USB Flash Drive
                vendor: ADATA
                physical id: 0.0.0
                bus info: scsi@1:0.0.0
                logical name: /dev/sdb
                version: 1.00
                serial: 237151605003011C
                size: 14GiB (15GB)
                capabilities: removable
                configuration: ansiversion=6 logicalsectorsize=512 sectorsize=512
              *-medium
                   physical id: 0
                   logical name: /dev/sdb
                   size: 14GiB (15GB)
                   capabilities: gpt-1.00 partitioned partitioned:gpt
                   configuration: guid=22c6543d-e248-4ffc-8119-c05828a79df6
                 *-volume:0
                      description: Windows FAT volume
                      vendor: BSD  4.4
                      physical id: 1
                      logical name: /dev/sdb1
                      version: FAT32
                      serial: 67e3-17ed
                      size: 199MiB
                      capacity: 199MiB
                      capabilities: boot fat initialized
                      configuration: FATs=2 filesystem=fat label=EFI name=EFI System Partition
                 *-volume:1
                      description: data partition
                      vendor: Windows
                      physical id: 2
                      logical name: /dev/sdb2
                      serial: 3453fcc0-0076-4112-b360-533567226f19
                      capacity: 14GiB
  *-network:0
       description: Ethernet interface
       physical id: 2
       logical name: eth0
       serial: b8:27:eb:dc:dd:d0
       size: 10Mbit/s
       capacity: 100Mbit/s
       capabilities: ethernet physical tp mii 10bt 10bt-fd 100bt 100bt-fd autonegotiation
       configuration: autonegotiation=on broadcast=yes driver=smsc95xx driverversion=22-Aug-2005 duplex=half firmware=smsc95xx USB 2.0 Ethernet link=no multicast=yes port=MII speed=10Mbit/s
  *-network:1
       description: Ethernet interface
       physical id: 3
       logical name: docker0
       serial: 02:42:ed:3e:a3:82
       capabilities: ethernet physical
       configuration: broadcast=yes driver=bridge driverversion=2.3 firmware=N/A ip=172.17.0.1 link=no multicast=yes
  *-network:2
       description: Wireless interface
       physical id: 4
       logical name: wlan0
       serial: b8:27:eb:89:88:85
       capabilities: ethernet physical wireless
       configuration: broadcast=yes driver=brcmfmac driverversion=7.45.41.26 firmware=01-4527cfab ip=192.168.31.156 multicast=yes wireless=IEEE 802.11

So the USB stick - the block devices /dev/sdb - has the logical name /dev/sdb. And the FAT32 filesystem on that stick has the logical name /dev/sdb2

Step 3: Mounting the USB stick
$ sudo mkdir /media/usbstick 
$ sudo mount -t vfat /dev/sdb2 /media/usbstick 
```

Customize Welcome message in RHEL/CentOS
----------------------------------------
> Customizing Motd(message of the day) display messages that may be unique to the machine. One way to do this is to create a script that runs when a user logs on to the system.
```
# First, create a script, make it executable, and save it in /etc/profile.d/motd.sh
$ sudo vim /etc/profile.d/motd.sh

#!/bin/bash
#
echo -e "
##################################
#
# Welcome to `hostname`
# This system is running `cat /etc/redhat-release`
# kernel is `uname -r`
#
# You are logged in as `whoami`
#
##################################
"

# Second, edit /etc/ssh/sshd_config, and disable motd 
$ sudo vim /etc/ssh/sshd_config 
PrintMotd no
$ sudo systemctl restart sshd 
```

Deleting older log files 
------------------------
```
# delete older logs based on date.
$ man find - walk a file hierarchy (遍历文件层次结构)
     -mindepth n : Always true; do not apply any tests or actions at levels less than n. 
     -mtime n[smhdw]: If no units are specified, this primary evaluates to true if the difference between the file last modification time and the time find was started 
     -mtime 0: means at least 24 hourse 

$ find /mylog/path -mindepth 1 -mtime +6 -delete 
     -mindepth 1 means process all files except the command line arguments 
     -mtime +6 will check for the files modified 7 days ago
     -delete will delete.
```