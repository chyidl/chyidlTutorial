# Tips

* 1. How to get a list of all valid IP addresses in a local network?
```
$ sudo apt-get install nmap

$ nmap -sn 192.168.1.0/24
will scan the entire .1 to .254 range
This does a simple ping scan in the entire subnet to see which hosts are online.
```

* 2. Htop Setup Screen
```
$ vim .config/htop/htoprc
# Beware! This file is rewritten by htop when settings are changed in the interface.
# The parser is also very primitive, and not human-friendly.
fields=0 48 17 18 38 39 40 2 46 47 49 1
sort_key=46
sort_direction=1
hide_threads=0
hide_kernel_threads=1
hide_userland_threads=0
shadow_other_users=0
show_thread_names=0
show_program_path=1
highlight_base_name=0
highlight_megabytes=1
highlight_threads=1
tree_view=1
header_margin=1
detailed_cpu_time=0
cpu_count_from_zero=0
update_process_names=0
account_guest_in_cpu_meter=0
color_scheme=0
delay=15
left_meters=LeftCPUs Memory Swap
left_meter_modes=1 1 1
right_meters=RightCPUs Tasks LoadAverage Uptime
right_meter_modes=1 2 2 2
```

* 3. How to Mount a USB Drive in Debian
> Most Linux distributions are configured to automatically mount USB devices as soon as they are inserted into the USB ports. However, in some cases, you are still required to mount the USB drives manually in order to access them.
```
Step 1: Plug-in the USB drive

Step 2: Find out the USB device name and the file system
$ sudo fdisk -l
...

Disk /dev/sda: 931.5 GiB, 1000204883968 bytes, 1953525164 sectors
Disk model: External USB 3.0
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x00000000

Device     Boot Start        End    Sectors   Size Id Type
/dev/sda1        2048 1953523711 1953521664 931.5G  7 HPFS/NTFS/exFAT

Step 3: Create a Mount Point directory where we want to mount our USB drive
$ sudo mkdir /mnt/EXDISK

Step 4: Mount the USB drive to the mount point
$ sudo mount /dev/sda1 /mnt/EXDISK

Step 5: Verify the USB drive is mounted successfully
$ mount | grep /dev/sda1
/dev/sda1 on /mnt/EXDISK type fuseblk (rw,nosuid,nodev,relatime,user_id=0,group_id=0,default_permissions,allow_other,blksize=4096)

Step 6: To access and browse the mounted device
$ cd /media/USB/

chyi in debian in /mnt/EXDISK
❯ ll
total 2.4M
drwxrwxrwx 1 root root 128K Aug  6  2020 books/
drwxrwxrwx 1 root root 128K Jun 21  2020 Downloads/
drwxrwxrwx 1 root root 128K Jun 27  2020 GitHub/
drwxrwxrwx 1 root root 128K Dec 20 12:54 iMacBackup/
-rwxrwxrwx 1 root root 1.1M Jul 17  2020 just-for-fun.pdf*
drwxrwxrwx 1 root root 128K Feb 20 18:29 Kindle/
drwxrwxrwx 1 root root 128K Jun 17  2020 movies/
drwxrwxrwx 1 root root 128K Aug 15  2020 Paper/
-rwxrwxrwx 1 root root   10 Jun 17  2020 README.md*
drwxrwxrwx 1 root root 128K Jun 21  2020 SmartCar/
drwxrwxrwx 1 root root 128K Jan  8 23:14 Softwares/

Step 7: Unmount a USB drive
-- Once you are done with using the mounted USB drive, you will need tp unmount or detach it. But before going to unmount, make sure no other process is running on the drive, otherwise the drive will fail to detach and you will receive the error message.
$ sudo unmount <mountpoint_directory>
```
