# External storage configuration 

> Can connect extract hard disk, SSD, or USB stick to any of the USB ports on the Raspberry Pi, and mount the file system to access the data stored on it. 
> By default, Raspberry pi automatically mounts the popular file systems such as FAT, NTFS, and HFS+at the/media/pi/f7b11615-a4e5-46d4-aed0-7533c9a7807b location 


## Mounting a storage device 
```
  1. Plug the storage device into a USB port on the Raspberry Pi 
  2. List all the disk partitions on the Pi using the following command:
$ sudo lsblk -o UUID,NAME,FSTYPE,SIZE,MOUNTPOINT,LABEL,MODEL
UUID                                 NAME        FSTYPE   SIZE MOUNTPOINT                       LABEL  MODEL
                                     sda                931.5G                                         External_U
f7b11615-a4e5-46d4-aed0-7533c9a7807b └─sda1      ext4   931.5G /media/pi/f7b11615-a4e5-46d4-aed        
                                     mmcblk0             59.6G                                         
6341-C9E5                            ├─mmcblk0p1 vfat     256M /boot                            boot   
80571af6-21c9-48a0-9df5-cffb60cf79af └─mmcblk0p2 ext4    59.4G /                                rootfs 

The Raspberry Pi uses mount points / and /boot.
Use the SIZE,LABEL,and MODEL columns to identify the name of the disk partition that points to your storage device. 

The FSTYPE colume contains the filesystem type, if your storage device uses an exFAT file syste, install the exFAT driver:
  $ sudo apt update 
  $ sudo apt instalkl exfat-fuse

If your storage device uses an NTFS file system, you wil have read-only access to it. If you want to write to the device, install the ntfs-3g driver. 
  $ sudo apt update 
  $ sudo apt instal ntfs-3g

Run the following command to get the location of the disk partition 
$ sudo blkid 
/dev/mmcblk0p1: LABEL_FATBOOT="boot" LABEL="boot" UUID="6341-C9E5" TYPE="vfat" PARTUUID="ea7d04d6-01"
/dev/mmcblk0p2: LABEL="rootfs" UUID="80571af6-21c9-48a0-9df5-cffb60cf79af" TYPE="ext4" PARTUUID="ea7d04d6-02"
/dev/sda1: UUID="f7b11615-a4e5-46d4-aed0-7533c9a7807b" TYPE="ext4"
/dev/mmcblk0: PTUUID="ea7d04d6" PTTYPE="dos"

Create a target folder to be the mount point of the storage device. The mount point name used in this case is mydisk 
$ sudo mkdir /mnt/exdisk

Mount the storage device at the mount point you created 
$ sudo mount /dev/sda1 /mnt/exdisk 

Verify that the storage device is mounted successfully by listing the contents 
$ ls /mnt/exdisk
```

## Setting up automatic mounting 
```
  Modify the fstab file to define the lcoation where the storafe device will be automatically mounted when the raspberry pi start up. In the fstab file. the disk partition is identified by the universally unique identifier (UUID)

  1. Get the UUID of the disk partition:
  $ sudo blkid 

  2. Find the disk partition from the list and note the UUID
  f7b11615-a4e5-46d4-aed0-7533c9a7807b

  3. Open the fstab file using a command line editor such as vim:
  $ sudo vim /etc/fstab 

  4. Add the following line in the fstab file 
  UUID=f7b11615-a4e5-46d4-aed0-7533c9a7807b /mnt/exdisk ext4 defaults,auto,users,rw,nofail 0 0 

  5. If the filesystem type is FAT or NTFS, add ,umask=000 immediately fater nofail - this will allow all users full read/write access to every file on the storage device. 

```

## Unmounting a storage device 
```
  When the Raspberry Pi shuts down, the system takes care of unmounting the storage device so that it is safe to unplug it. 
  $ sudo umount /mnt/exdisk 
```

## Dealing with 'target is busy'
```
   The target is busy message means there are files on the storage device that are in use by program. To close the files, use the following procedure. 
   1. Close any program which has open files on the storage device .
   2. If you have a terminal open, make sure that you are not in the folder where the storage device is mounted, or in a sub-folder of it.
   3. If you are still unable to unmound the storage device, you can use the lsof tool to check which program has files open on the devices
   $ sudo apt install lsof
   $ lsof /mnt/exdisk
```
