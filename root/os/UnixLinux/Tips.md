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

* 3. Creating a Disk Partiton
```
fdisk is a menu-driven  command-line utility that allows you to create and manipulate partition tables on a hard disk.

# The output above shows the current partition tables of all devices that are attached to your system
❯ sudo fdisk -l

Disk /dev/sda: 119.2 GiB, 128035676160 bytes, 250069680 sectors
Disk model: SSD 128GB
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes

Disk /dev/sdb: 931.5 GiB, 1000204883968 bytes, 1953525164 sectors
Disk model: External USB 3.0
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 9278DAE8-2117-4A1A-B6D2-3906D4B1476C


chyi in openmediavault in ~ took 3s
❯ sudo fdisk /dev/sda

Welcome to fdisk (util-linux 2.33.1).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

The old ext4 signature will be removed by a write command.

Device does not contain a recognized partition table.
Created a new DOS disklabel with disk identifier 0xa02c5865.

Command (m for help): m

Help:

  DOS (MBR)
   a   toggle a bootable flag
   b   edit nested BSD disklabel
   c   toggle the dos compatibility flag

  Generic
   d   delete a partition
   F   list free unpartitioned space
   l   list known partition types
   n   add a new partition
   p   print the partition table
   t   change a partition type
   v   verify the partition table
   i   print information about a partition

  Misc
   m   print this menu
   u   change display/entry units
   x   extra functionality (experts only)

  Script
   I   load disk layout from sfdisk script file
   O   dump disk layout to sfdisk script file

  Save & Exit
   w   write table to disk and exit
   q   quit without saving changes

  Create a new label
   g   create a new empty GPT partition table
   G   create a new empty SGI (IRIX) partition table
   o   create a new empty DOS partition table
   s   create a new empty Sun partition table


Command (m for help): g
Created a new GPT disklabel (GUID: CDF62227-C81F-FC47-B9BD-8FE1FBD3B3DB).
The old ext4 signature will be removed by a write command.

Command (m for help): n
Partition number (1-128, default 1):
First sector (2048-250069646, default 2048):

Command (m for help): p
Disk /dev/sda: 119.2 GiB, 128035676160 bytes, 250069680 sectors
Disk model: SSD 128GB
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: CDF62227-C81F-FC47-B9BD-8FE1FBD3B3DB

Device     Start       End   Sectors   Size Type
/dev/sda1   2048 250069646 250067599 119.2G Linux filesystem

Command (m for help):


fdisk supports several partitioning schemes. MBR and GPT are the two most popular partition scheme standards. that store the partitioning information on a drive in a different way.
GPT is a newer standard allowing and has many advantages over MBR.

The main points to consider when choosing what partitioning standard to use.
    1. Use MBR to boot the disk in legacy BIOS mode.
    2. Use GPT to boot the disk in UEFI mode.
    3. The MBR standard supports creating a disk partition up to 2 TiB. If you have a disk of 2TiB or larger, use BPT.
    4. MBR has a limit of 4 primary partitions. If you need more partiton, one of the primary partitions can be set as an extended partition and hold additional logical partitions. With GPT, you can have up to 128 partitions, GPT doesn't support extended or logical paritions.

Now that the partitions have been created, the next step is to format the aprtitions and mount them to the system's directory tree.

chyi in openmediavault in ~
❯ lsblk -f
NAME                  FSTYPE      LABEL  UUID                                   FSAVAIL FSUSE% MOUNTPOINT
sda
└─sda1
sdb
└─sdb1                ext4        EXDISK 671cdfc1-9ed4-4b4b-9966-74197042607d    899.5G     2% /srv/dev-disk-by-uuid-671cdfc1-9ed4-4b4b-9966-74197042607d
mmcblk1
├─mmcblk1p1           vfat               1055-A88F                               498.1M     3% /boot/efi
├─mmcblk1p2           ext2               9b467e95-ac12-47e7-a640-ee91858316d2    342.4M    22% /boot
└─mmcblk1p3           LVM2_member        EfcPMq-OM1s-jXfP-b3qz-DLoP-quNu-vDIgJq
  ├─debian--vg-root   ext4               0d961d2a-ce75-4778-844c-f46b39f3c7a8      3.6G    62% /
  ├─debian--vg-swap_1 swap               8645aaee-475e-4377-9dfe-69890f76f335                  [SWAP]
  ├─debian--vg-var    ext4               ad6e24a1-7b88-44f0-a53b-e1c677b37275    319.5M    86% /var
  ├─debian--vg-tmp    ext4               0c3c3a7e-a925-45f4-aa5c-75585c37e858
  └─debian--vg-home   ext4               b4ec74b2-8781-4438-8ffa-b23ffadd3014     19.2G    46% /home
mmcblk1boot0
mmcblk1boot1

# Format both partitions to ext4
❯ sudo mkfs.ext4 -F /dev/sda1
mke2fs 1.44.5 (15-Dec-2018)
Discarding device blocks: done
Creating filesystem with 31258449 4k blocks and 7815168 inodes
Filesystem UUID: c0cd39ca-cf58-4bde-92d2-b07edc3042ee
Superblock backups stored on blocks:
        32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208,
        4096000, 7962624, 11239424, 20480000, 23887872

Allocating group tables: done
Writing inode tables: done
Creating journal (131072 blocks): done
Writing superblocks and filesystem accounting information: done
```

* 4. How To Mount and Unmount Drivers on Linux
```
# To list partitions with filesystems types, use the "lsblk" command with the "-f" option
❯ sudo lsblk -f
NAME                  FSTYPE      LABEL  UUID                                   FSAVAIL FSUSE% MOUNTPOINT
sda
└─sda1                ext4               c0cd39ca-cf58-4bde-92d2-b07edc3042ee    110.9G     0% /mnt/INNERDISK
sdb
└─sdb1                ext4        EXDISK 671cdfc1-9ed4-4b4b-9966-74197042607d    899.5G     2% /srv/dev-disk-by-uuid-671cdfc1-9ed4-4b4b-9966-74197042607d
mmcblk1
├─mmcblk1p1           vfat               1055-A88F                               498.1M     3% /boot/efi
├─mmcblk1p2           ext2               9b467e95-ac12-47e7-a640-ee91858316d2    342.4M    22% /boot
└─mmcblk1p3           LVM2_member        EfcPMq-OM1s-jXfP-b3qz-DLoP-quNu-vDIgJq
  ├─debian--vg-root   ext4               0d961d2a-ce75-4778-844c-f46b39f3c7a8      3.6G    62% /
  ├─debian--vg-swap_1 swap               8645aaee-475e-4377-9dfe-69890f76f335                  [SWAP]
  ├─debian--vg-var    ext4               ad6e24a1-7b88-44f0-a53b-e1c677b37275    318.7M    86% /var
  ├─debian--vg-tmp    ext4               0c3c3a7e-a925-45f4-aa5c-75585c37e858
  └─debian--vg-home   ext4               b4ec74b2-8781-4438-8ffa-b23ffadd3014     19.2G    46% /home
mmcblk1boot0
mmcblk2boot1

# Mounting Drives Permanently using fstab (static information about filesystems, mountpoints)

The fstab contains multiple columns:
    Filesystem:
        you can either specify a UUID (for universal unique identifier), a label(if you chose a label for your disk), a network ID or a device name(which is not recommended at all)
    Mountpoint: the directory on the filesystem that you are going to use in order to access data stored on the disk
    Filesystem type: the type of filesystem you use
    Options: some options that you can specify in order to tune your mount ("ro" for a read-only mount or "noexec" to prevent binary execution)
    Dump: in order to enable to disable filesystem dumping on the system (using the dump command)
    Pass Num:
```

* 5. Benchmark Hard Disks
```
Hdparm is a simple commad line app for Linux that allows you to manage storage devices by setting and removing parameters. It also includes an option to test read speeds or storage devices.

# Install hdparm
$ sudo apt install hdparm

# run a hard disk benchmark using Hdparm
❯ sudo hdparm -tT /dev/sda

/dev/sda:
 Timing cached reads:   3954 MB in  2.00 seconds = 1977.90 MB/sec
 Timing buffered disk reads: 1566 MB in  3.00 seconds = 521.69 MB/sec

chyi in openmediavault in ~ took 15s
❯ sudo hdparm -tT /dev/sdb

/dev/sdb:
 Timing cached reads:   3780 MB in  2.00 seconds = 1890.48 MB/sec
 Timing buffered disk reads: 346 MB in  3.00 seconds = 115.15 MB/sec

dd is a command line utility for Linux that allows you to copy and convert files and data. it is capable of copying large chunks of data, cloning hard disks, creating bootable USB drives and so on.

# check hard disk write speed using dd
chyi in openmediavault in /mnt/INNERDISK/benchmark🔒
❯ sudo dd if=/dev/zero of=benchfile bs=4k count=200000 && sync; rm benchfile
200000+0 records in
200000+0 records out
819200000 bytes (819 MB, 781 MiB) copied, 1.60309 s, 511 MB/s
rm: remove write-protected regular file 'benchfile'? y

# To perform a read test using dd
❯ dd if=/dev/zero of=/dev/null && sync
^C22169467+0 records in
22169466+0 records out
11350766592 bytes (11 GB, 11 GiB) copied, 16.8848 s, 672 MB/s



```
