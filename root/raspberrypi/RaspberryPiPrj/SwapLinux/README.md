Swap RAM
--------
> One of the easiest ways to make your server more responsive, and guard against out-of-memory errors in your application, is to add some swap space. Swap is an area on a storage drive where the operating system can temporarily store data that it can not longer hold in memory.

> This gives you the ability to increase the amount of information that your server can keep in its working memory, with some caveats. Reading from and writing to swap is slower than using memory, but it can provide a good safety net for when your server is low on memory.

> Without swap. a server that runs out of memory may start killing applications to free up memory, or even crash. This can cause you to lose unsaved data or experience downtime. To ensure reliable data access, some applications require swap to function.

Create and Enable a Swap file on CentOS 7 Server
------------------------------------------------
```
Check the System for Swap Information
    - swapon, swapoff - enable/disable devices and files for paging and swapping 
        -s, --summary: Display swap usage summary by device. Equivalent to "cat /proc/swaps"

[chyi@zong ~]$ swapon -s
Filename                                Type            Size    Used    Priority
/swapfile                               file    2097148 264     -2

[chyi@zong ~]$ free -m
              total        used        free      shared  buff/cache   available
Mem:           1998         463          91           8        1443        1356
Swap:          2047           0        2047

Check Available Storage Space 
> The typical way of allocating space for swap is to use a separate partition that is dedicated to the task. However, altering the partition scheme is not always possible due to hardware or software constraints. Fortunately, we can just easily create a swap file that resides on an exsisting partition.

[chyi@zong ~]$ df -h
Filesystem      Size  Used Avail Use% Mounted on
devtmpfs        990M     0  990M   0% /dev
tmpfs          1000M     0 1000M   0% /dev/shm
tmpfs          1000M  8.8M  991M   1% /run
tmpfs          1000M     0 1000M   0% /sys/fs/cgroup
/dev/vda1        40G  8.6G   29G  23% /
tmpfs           200M     0  200M   0% /run/user/0
tmpfs           200M     0  200M   0% /run/user/1000

Create a Swap File 
    fallocate - preallocate or deallocate space to a file 
        -l, --length length: Specifies the length of the range, in bytes 
[chyi@zong ~]$ sudo fallocate -l 2G /swapfile
[chyi@zong ~]$ ls -lh /swapfile 
-rw------- 1 root root 2.0G Nov  5 16:06 /swapfile

Enable a Swap File 

# adjust the permissions on our swap file so that it isn't readable by anyone besides the root account.
[chyi@zong ~]$ sudo chmod 600 /swapfile 

# set up the swap space 
    mkswap - set up a Linux swap area 
[chyi@zong ~]$ sudo mkswap /swapfile 

Make the Swap File Permanent
# modifying the fstab file, which is a table that manages filesystems and partitions.

[chyi@zong ~]$ sudo vim /etc/fstab
    #
    # /etc/fstab
    # Created by anaconda on Thu Mar 21 07:01:01 2019
    #
    # Accessible filesystems, by reference, are maintained under '/dev/disk'
    # See man pages fstab(5), findfs(8), mount(8) and/or blkid(8) for more info
    #
    UUID=84953f78-f1ba-4dbd-ac60-aaabc2e4cb9c /                       ext4    defaults        1 1
    # add a line that will tell the operating system to automatically use the swap file that you created.
    /swapfile       swap    swap    sw      0       0

Tweak Your Swap Settings (Optional)
    Swappiness:
        - The swappiness parameter determines how often your system swaps data out of memory to the swap space. This is a value between 0 and 100 that represents the percentage of memory usage that will trigger the use of swap.
        0 - will not swap data Telling the system not to rely on the swap as much will generally make your system faster.
        100 - try to put more data into swap in an effort to keep more memory free.

[chyi@zong ~]$ cat /proc/sys/vm/swappiness
10      # For a VPS system, we'd probably want to move it closer to 0 
[chyi@zong ~]$ sudo sysctl vm.swappiness=0
vm.swappiness = 0
To make the setting persist between reboots, add the outputted line to our sysctl configuration file:
[chyi@zong ~]$ sudo vim /etc/sysctl.conf
# sysctl settings are defined through files in
# /usr/lib/sysctl.d/, /run/sysctl.d/, and /etc/sysctl.d/.
#
# Vendors settings live in /usr/lib/sysctl.d/.
# To override a whole file, create a new file with the same in
# /etc/sysctl.d/ and put new settings there. To override
# only specific settings, add a file with a lexically later
# name in /etc/sysctl.d/ and put new settings there.
#
# For more information, see sysctl.conf(5) and sysctl.d(5).
vm.swappiness = 0

    Cache Pressure: modify the vfs_cache_pressure. This setting affects the storage of specific filesystem metadata entries. Constantly reading and refreshing this information is generally very costly, so storing it on the cache for longer is excellent for your system performance.

[chyi@zong ~]$ cat /proc/sys/vm/vfs_cache_pressure
100
[chyi@zong ~]$ sudo sysctl vm.vfs_cache_pressure=50
[sudo] password for chyi: 
vm.vfs_cache_pressure = 50
[chyi@zong ~]$ sudo vim /etc/sysctl.conf
# sysctl settings are defined through files in
# /usr/lib/sysctl.d/, /run/sysctl.d/, and /etc/sysctl.d/.
#
# Vendors settings live in /usr/lib/sysctl.d/.
# To override a whole file, create a new file with the same in
# /etc/sysctl.d/ and put new settings there. To override
# only specific settings, add a file with a lexically later
# name in /etc/sysctl.d/ and put new settings there.
#
# For more information, see sysctl.conf(5) and sysctl.d(5).
vm.swappiness = 0
vm.vfs_cache_pressure = 50


```