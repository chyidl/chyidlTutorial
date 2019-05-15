Mount A USB Flash Disk On the Raspberry Pi
==========================================
* Step 1 - Plug In the Device 
* Step 2 - Identify The Devices Unique ID 
```
In order to find the unique reference (UUID) for your drive run the following command in the terminal 
$ ls -l /dev/disk/by-uuid
total 0
lrwxrwxrwx 1 root root 15 Jan 28  2018 4245-236F -> ../../mmcblk0p1
lrwxrwxrwx 1 root root 10 May  5 23:05 67E3-17ED -> ../../sda1
lrwxrwxrwx 1 root root 15 May  5 20:35 cb9fa157-6a4b-425b-aa26-fd4790634d69 -> ../../mmcblk0p2
lrwxrwxrwx 1 root root 10 May  5 23:05 D881-1F10 -> ../../sda2

$ sudo fdisk -l
Disk /dev/mmcblk0: 29.8 GiB, 32010928128 bytes, 62521344 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x85baa6c1

Device         Boot  Start      End  Sectors  Size Id Type
/dev/mmcblk0p1 *      2048   526335   524288  256M  c W95 FAT32 (LBA)
/dev/mmcblk0p2      526336 62521310 61994975 29.6G 83 Linux


Disk /dev/sda: 59.8 GiB, 64172851200 bytes, 125337600 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 34086D2F-E64E-4934-91A7-DA3E5962F2D5

Device      Start       End   Sectors  Size Type
/dev/sda1      40    409639    409600  200M EFI System
/dev/sda2  411648 125335551 124923904 59.6G Microsoft basic data
```
* Step 3 - Deleting all partitions on a USB drive using fdisk 
```
First to delete the old partitionas that remain on the USB key.
    1. Open a terminal and type sudo su 
    2. Type fdisk -l and note your USB drive letter.
    3. Type fdisk /dev/sdx (replacing x with your drive letter)
    4. Type d to proceed to delete a partition 
    5. Type 1 to select the 1st partition and press enter 
    6. Type d to proceed to delete another partition(fdisk should automatically select the second partition)

Next to create the new partition.
    1. Type n to make a new partition 
    2. Type p to make this partition primary and press enter 
    3. Type 1 to make this the first partition and then press enter 
    4. Press enter to accept the default first cylinder 
    5. Press enter again to accept the default last cylinder 
    6. Type w to write the new paritition information to the USB key 
    7. Type umount /dev/sdx (replacing x with your drive letter)
The last step is to create the fat filesystem. 
    1. Type mkfs.vfat -F 32 /dev/sdx1 (replacing x with your USB key drive letter)
That's it, you should now have a restored USB key with a single fat 32 partition that can be read from any computer
```
* Step 4 - Create a Mount Point 
```
A mount point is a directory that will point to the contents of your flash drive. Create a suitable folder:
$ sudo mkdir /mnt/usb 

Make sure the Pi user owns this folder:
$ sudo chown -R pi:pi /mnt/usb 
```
