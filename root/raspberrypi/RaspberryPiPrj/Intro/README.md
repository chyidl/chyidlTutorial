Raspberry Pi
============

SD cards
--------
> The Raspberry Pi should work with any compatible SD card, although there are some guidelines that should be followed:
* SD card size (capacity)
    - For installation of NOOBS or the image installation of Raspbian, the minimum recommended card size is 8GB. For Raspbian Lite image installations recommend a minimum of 4GB. Some distributions, specifically LibreELEC and Arch, can run on mush smaller cards
    - Only the Raspberry Pi 3A, 3B+ and Compute Module 3+ can boot from an SD card larger than 256GB. This is because there was a bug in the SoC used on previous models of Pi.

* SD card class 
    - The card class determines the sustanined write speed for the card; a class 4 card will be able to write at 4MB/s, whereas a class 10 should be attain 10MB/s. However, it should be noted that this does not mean a class 10 card will outperform a class 4 card for general usage, because often this write speed is achieved at the cost of read speed and increased seek times.

* Troubleshooting 
    - Make sure you are using a genuine SD card. There are many cheap SD cards available which are actually smaller than advertised or which will not last very long.
    - Make sure you are using a good quality power supply. You can check your power supply by measuring the voltage between TP1 and TP2 on the Raspberry Pil if this drops below 4.75V when doing complex tasks then it is most likely unsuitable.
    - Make sure you are using a good quality USB cable for the power supply. When using a lower quality power supply, the TP1 -> TP2 voltage can drop below 4.75V. This is generally due to the resistance of the wires in the USB power cable; to save money, USB cables have as little copper in them as possible, and as much as 1V (1W) can be lost over the length of the cable.
    - Make sure you are shutting your Raspberry Pi down properly before powering it off. Type _sudo halt_ and wait for the Pi to signal it is ready to be powered off by flashing the activity LED.

Installing operating system images
----------------------------------
* Download the image 
    - Official images for recommended operating systems are available to download from the Raspberry Pi website [Downloads page](https://www.raspberrypi.org/downloads/)

* Writing an image to the SD card (macOS)
    - If you are comfortable with the command line, you can write the image to an SD card without any additional software.
```
$ diskutil list 
/dev/disk0 (internal):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                         251.0 GB   disk0
   1:                        EFI EFI                     314.6 MB   disk0s1
   2:                 Apple_APFS Container disk1         250.7 GB   disk0s2

/dev/disk1 (synthesized):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      APFS Container Scheme -                      +250.7 GB   disk1
                                 Physical Store disk0s2
   1:                APFS Volume Macintosh HD            45.0 GB    disk1s1
   2:                APFS Volume Preboot                 66.5 MB    disk1s2
   3:                APFS Volume Recovery                1.0 GB     disk1s3
   4:                APFS Volume VM                      2.1 GB     disk1s4

/dev/disk2 (external, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:     Apple_partition_scheme                        *7.9 GB     disk2
   1:        Apple_partition_map                         254.0 KB   disk2s1
   2:                  Apple_HFS Chyi Yaqing’s iPod      7.9 GB     disk2s2

/dev/disk3 (external, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:     FDisk_partition_scheme                        *1.0 TB     disk3
   1:                  Apple_HFS TOSHIBA-1TB             1.0 TB     disk3s1

/dev/disk4 (external, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:     FDisk_partition_scheme                        *7.8 GB     disk4
   1:                      Linux                         53.0 MB    disk4s1
   2:                      Linux                         7.8 GB     disk4s2
```
    - Identify the disk (not the partiton) of you SD card, disk4, not disk4s1 
    - Unmount your SD card by using the disk identifier, to prepare it for copying data:
```
$ diskutil unmountDisk /dev/disk4                                                               
Unmount of all volumes on disk4 was successful
```
    - Copy the data to your SD card
```
$ sudo dd bs=1m if=./kali-rolling.img of=/dev/disk4 conv=sync

This will take a few minutes, depending on the image file size. You can check the progress by sending a SIGINFO singal (Press Ctrl+T).

33160+0 records in
33160+0 records out
16977920 bytes transferred in 5.212609 secs (3257087 bytes/sec)
```
    - Eject the Card 
```
$ sudo diskutil eject /dev/disk4
```

Backup up SD Card on macOS 
--------------------------
```
1. With your SD card inserted into a card reader on your Mac, begain the process of making a full image backup of your Raspberry Pi.

2. With the Termianl application now open on your Mac device, need to utilize the folliwing command. This command will display all available disks on your device.
$ diskutil list 
/dev/disk4 (external, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:     FDisk_partition_scheme                        *7.8 GB     disk4
   1:                      Linux                         53.0 MB    disk4s1
   2:                      Linux                         7.8 GB     disk4s2

3. create a copy of your SD cards image, and save it to your directory 
$ sudo dd if=/dev/disk4 of = ./pmOS.dmg
```
