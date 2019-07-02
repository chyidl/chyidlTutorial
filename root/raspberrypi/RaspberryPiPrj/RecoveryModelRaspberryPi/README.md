Make a self-healing Raspberry Pi
================================

> Most modern operating systems come with a "recovery partition", a reserved area of the drive containing everything needed to get the machine back to a clean install. So, if something goes badly wrong, you can start over.

How to create a bootable image featuring a restore partition
------------------------------------------------------------
```
# Make sure you have uuidgen installed 
$ sudo apt-get install uuid-runtime 

# Create a working directory on your macOS and downloaded both the Raspbian Full and Raspbian Lite images
$ wget 2019-06-20-raspbian-stretch-full.zip && unzip 
$ wget 2019-06-20-raspbian-stretch-lite.zip && unzip 

# Calculate measure the image size in sectors, each one 512 bytes in size. 
# Find out how many sectors are used by the partitions:
$ fdisk -lu 2019-06-20-raspbian-stretch-full.img 
$ fdisk -lu 2019-06-20-raspbian-stretch-lite.img 

```
