Linux 101
=========

Linux Common Commands
---------------------
```
1. df - report file system disk space usage 
    -B, --block-size=SIZE: scale sizes by SIZE before printing them; e.g., 
        '-BM' prints sizes in units of 1,048,576 bytes
        '-BK' prints sizes in units of 1024 bytes 
[chyi@zong /]$ df -BM 
Filesystem     1M-blocks  Used Available Use% Mounted on
devtmpfs            990M    0M      990M   0% /dev
tmpfs              1000M    0M     1000M   0% /dev/shm
tmpfs              1000M    9M      991M   1% /run
tmpfs              1000M    0M     1000M   0% /sys/fs/cgroup
/dev/vda1         40189M 3844M    34486M  11% /
tmpfs               200M    0M      200M   0% /run/user/1000
tmpfs               200M    0M      200M   0% /run/user/0

    -T, --print-type: print file system type 
[chyi@zong /]$ df -BM -T
Filesystem     Type     1M-blocks  Used Available Use% Mounted on
devtmpfs       devtmpfs      990M    0M      990M   0% /dev
tmpfs          tmpfs        1000M    0M     1000M   0% /dev/shm
tmpfs          tmpfs        1000M    9M      991M   1% /run
tmpfs          tmpfs        1000M    0M     1000M   0% /sys/fs/cgroup
/dev/vda1      ext4        40189M 3844M    34486M  11% /
tmpfs          tmpfs         200M    0M      200M   0% /run/user/1000
tmpfs          tmpfs         200M    0M      200M   0% /run/user/0

2. du - estimate file space usage 
   -a, --all: write counts for all files, not just directories 
   -c, --total: produce a grand total 
   -b, --bytes: equivalent to '--apparent-size --block-size=1'
   -k like --block-size=1K 
   -m like --block-size=1M 

3. cat - concatenate files and print on the standard output
[chyi@zong /]$ cat /proc/cpuinfo    
processor       : 0
vendor_id       : GenuineIntel
cpu family      : 6
model           : 63
model name      : Intel(R) Xeon(R) CPU E5-2620 v3 @ 2.40GHz
stepping        : 2
microcode       : 0x1
cpu MHz         : 2394.454
cache size      : 15360 KB
physical id     : 0
siblings        : 1
core id         : 0
cpu cores       : 1
apicid          : 0
initial apicid  : 0
fpu             : yes
fpu_exception   : yes
cpuid level     : 13
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon rep_good nopl xtopology eagerfpu pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm invpcid_single ibrs ibpb fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid xsaveopt arat spec_ctrl
bogomips        : 4788.90
clflush size    : 64
cache_alignment : 64
address sizes   : 40 bits physical, 48 bits virtual
power management:

[chyi@zong /]$ cat /proc/meminfo
MemTotal:        2046924 kB
MemFree:          163352 kB
MemAvailable:    1546112 kB
Buffers:           54124 kB
Cached:          1426220 kB
SwapCached:            0 kB
Active:           675832 kB
Inactive:        1072532 kB
Active(anon):     268576 kB
Inactive(anon):     8400 kB
Active(file):     407256 kB
Inactive(file):  1064132 kB
Unevictable:           0 kB
Mlocked:               0 kB
SwapTotal:             0 kB
SwapFree:              0 kB
Dirty:                24 kB
Writeback:             0 kB
AnonPages:        268040 kB
Mapped:            46632 kB
Shmem:              8956 kB
Slab:              99644 kB
SReclaimable:      86356 kB
SUnreclaim:        13288 kB
KernelStack:        2848 kB
PageTables:         7128 kB
NFS_Unstable:          0 kB
Bounce:                0 kB
WritebackTmp:          0 kB
CommitLimit:     1023460 kB
Committed_AS:    1115292 kB
VmallocTotal:   34359738367 kB
VmallocUsed:      271376 kB
VmallocChunk:   34358947836 kB
HardwareCorrupted:     0 kB
AnonHugePages:    192512 kB
CmaTotal:              0 kB
CmaFree:               0 kB
HugePages_Total:       0
HugePages_Free:        0
HugePages_Rsvd:        0
HugePages_Surp:        0
Hugepagesize:       2048 kB
DirectMap4k:       57188 kB
DirectMap2M:     2039808 kB
DirectMap1G:           0 kB

[chyi@zong ~]$ cat /proc/swaps
Filename                                Type            Size    Used    Priority
/swapfile                               file            2097148 143872  -2

[chyi@zong ~]$ cat /proc/version
Linux version 3.10.0-1062.4.1.el7.x86_64 (mockbuild@kbuilder.bsys.centos.org) (gcc version 4.8.5 20150623 (Red Hat 4.8.5-39) (GCC) ) #1 SMP Fri Oct 18 17:15:30 UTC 2019

[chyi@zong ~]$ cat /proc/net/dev
Inter-|   Receive                                                |  Transmit
 face |bytes    packets errs drop fifo frame compressed multicast|bytes    packets errs drop fifo colls carrier compressed
  eth0: 8041505018 2967528    0    0    0     0          0         0 1123975564 2562359    0    0    0     0       0          0
    lo: 29685667   46948    0    0    0     0          0         0 29685667   46948    0    0    0     0       0          0

4. free - Display amount of free and used memory in the system
    -s, --seconds seconds: Continuously display the result delay seconds apart. You may actually specify any floating point number for delay,
[chyi@zong ~]$ free -s 1
              total        used        free      shared  buff/cache   available
Mem:        2046924     1433392       72232        2896      541300      457896
Swap:       2097148      143872     1953276

              total        used        free      shared  buff/cache   available
Mem:        2046924     1433408       72236        2896      541280      457944
Swap:       2097148      143872     1953276

5. lsof - list open files 
   -i: 3306 
[chyi@zong ~]$ sudo lsof -i:3306
COMMAND  PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
mysqld  1416 mysql   17u  IPv6  55843      0t0  TCP *:mysql (LISTEN)

6. netstat - Print network connections, routing tables, interface statistics, masquerade connections, and multicast memberships
    -t, -tcp: 
    -u, -udp: 
    --numberic, -n: Show numerical addresses instead of trying to determine symbolic host, port or user names.
    --listening, -l: Show only listening sockets, (These are omitted by default.)
    --program, -p: Show the PID and name of the program to which each socket belongs.

[chyi@zong ~]$ sudo netstat -tunlp | grep 3306
[sudo] password for chyi: 
tcp6       0      0 :::3306                 :::*                    LISTEN      1416/mysqld         

7. nohup (no hangup) - run a command immune to hangups, with output to a non-tty 
> nohup is 'no hangup'. Normally, when we log out from the system then all the running programs or processes are hangup or terminated.

[chyi@zong ~]$ nohup --version
nohup (GNU coreutils) 8.22
Copyright (C) 2013 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by Jim Meyering.
    - Using nohup command without '&' then it returns to shell command prompt immediately after running that particular command in the background.
[chyi@zong ~]$ vim ./sleep.sh 
    #!/usr/bin/env bash
    echo "sleep 5 seconds"
    sleep 5
    echo "What's going on everybody!"

[chyi@zong ~]$ nohup bash ./sleep.sh 
nohup: ignoring input and appending output to ‘nohup.out’
[chyi@zong ~]$ cat nohup.out 
sleep 5 seconds
What's going on everybody!

    - Using nohup command with '&' then it doesn't return to shell command prompt after running the command in the background.
[chyi@zong ~]$ nohup bash sleep.sh &
[1] 9598
[chyi@zong ~]$ nohup: ignoring input and appending output to ‘nohup.out’

[chyi@zong ~]$ fg
nohup bash sleep.sh
[chyi@zong ~]$ fg
-bash: fg: current: no such job

8. ls - list directory contents 

9. mkdir - make directories 
    -p, --parents: no error if existing, make parent directories as needed.

10. cp - copy files and directories 
    -R, -r, --recursive: copy directories recursively

11. rm - remove files or directories 
    -R, -r, --recursive: remove directories and their contents recursively 
    -f, --force: ignore nonexistent files and arguments, never prompt 

12. touch - change file timestamps 
    -t STAMP: use [[CC]YY]MMDDhhmm[.ss] instead of current time 

13. mv - move (rename) files 
    mv SOURCE DIRECTORY

14. stat - display file or file system status 

[chyi@zong ~]$ stat sleep.sh 
  File: ‘sleep.sh’
  Size: 85              Blocks: 8          IO Block: 4096   regular file
Device: fd01h/64769d    Inode: 394856      Links: 1
Access: (0775/-rwxrwxr-x)  Uid: ( 1000/    chyi)   Gid: ( 1000/    chyi)
Access: 2019-11-06 13:45:40.136590367 +0800
Modify: 2019-11-06 13:45:29.864600806 +0800
Change: 2019-11-06 13:45:29.867600802 +0800
 Birth: -

15. chmod - change file mode bits 
    -R, --recursive: change files and directories recursively 
    read(r): 4, write(w): 2, execute(x): 1

16. ps - report a snapshot of the current processes.
    -A : Select all processes. Identical to -e 
    -a : Select all processes except both session leaders and processes not associated with a terminal.
    -u userlist: Select by effective user ID (EUID) or name. 
    -w : wide output. Use this option twice for unlimited width.
    -f : Do full-format listing. This option can be combined with many other UNIX-style options to add additional columns.

[chyi@zong ~]$ ps -aux --sort -pmem | head -n 10        # 前10个内存使用最多的进程
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root      8230  0.0 47.1 1100596 965608 pts/2  T    10:52   0:01 mysql -u root -p
mysql     1416  1.0 11.6 1150312 238952 ?      Sl   Nov05  14:51 /usr/sbin/mysqld --daemonize --pid-file=/var/run/mysqld/mysqld.pid
root      4922  0.4  1.4 903848 29668 ?        Sl   Nov05   4:45 /opt/hosteye/bin/hosteye --is_child_mode=true --is_console_mode=false --start_mode=0
root      1195  0.0  0.3 284776  8048 ?        SNl  Nov05   0:55 ./bcm-si -N 78431e27-b82c-4112-aa6f-5561f2f9c7ae -v 3
root      9012  0.0  0.2 156796  5572 ?        Ss   13:08   0:00 sshd: chyi [priv]
root      1134  0.0  0.2 219596  4876 ?        SNl  Nov05   0:16 ./bcm-agent
chyi      9015  0.0  0.1 116636  3412 pts/3    Ss   13:08   0:00 -bash
root       381  0.0  0.1  39080  3360 ?        Ss   Nov05   0:00 /usr/lib/systemd/systemd-journald
root      1092  0.0  0.1 222760  3168 ?        Ssl  Nov05   0:05 /usr/sbin/rsyslogd -n

[chyi@zong ~]$ ps -aux --sort +pmem | head -n 10        # 前10个内存使用最少的进程
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         2  0.0  0.0      0     0 ?        S    Nov05   0:00 [kthreadd]
root         4  0.0  0.0      0     0 ?        S<   Nov05   0:00 [kworker/0:0H]
root         6  0.0  0.0      0     0 ?        S    Nov05   0:04 [ksoftirqd/0]
root         7  0.0  0.0      0     0 ?        S    Nov05   0:00 [migration/0]
root         8  0.0  0.0      0     0 ?        S    Nov05   0:00 [rcu_bh]
root         9  0.0  0.0      0     0 ?        R    Nov05   0:02 [rcu_sched]
root        10  0.0  0.0      0     0 ?        S<   Nov05   0:00 [lru-add-drain]
root        11  0.0  0.0      0     0 ?        S    Nov05   0:00 [watchdog/0]
root        13  0.0  0.0      0     0 ?        S    Nov05   0:00 [kdevtmpfs]

17. kill - send a signal to a process or a group of processes. 
   -9, -SIGKILL: Kill signal

18. killall - kill processes by name 
    -9, -SIGKILL: kill signal

19. tar - manipulate tape archives
    -c, --create : create a new archive containing the specified items.
    -v, --verbose: Produce verbose output.
    -f file, --file file: Read the archive from or write the archive to the specified file.
    -x, --extract, --get: extract files from an archive
    -z, --gzip: filter the archive through gzip
    -j, --bzip2: filter the archive through bzip2  
    -Z, --compress, --uncompress: filter the archive through compress
           Note: You might need to install external program (lzip/ncompress/lzma...) to use some of these compression options
    -tvf archive.tar: List all files in archive.tar verbosely.

[chyi@zong ~]$ tar -cvf nohup.tar *.out         # tar -xvf nohup.tar 
nohup.out
[chyi@zong ~]$ ls
nohup.out  nohup.tar  sleep.sh

[chyi@zong ~]$ tar -czf nohup.tar.gz *.out      # tar -xzf nohup.tar.gz 
[chyi@zong ~]$ ls
nohup.out  nohup.tar.gz  sleep.sh

[chyi@zong ~]$ tar -cjf nohup.tar.bz2 *.out     # tar -xjf nohup.tar.bz2 
[chyi@zong ~]$ ls
nohup.out  nohup.tar.bz2  sleep.sh

[chyi@zong ~]$ tar -cZf nohup.tar.Z *.out       # tar -xZf nohup.tar.Z 
[chyi@zong ~]$ ls
nohup.out  nohup.tar.Z  sleep.sh

20. zip - package and compress (archive) files 

21. cron - daemon to execute scheduled commands

22. at, batch, atq, atrm - queue, examine or delete jobs for later execution.

23. crontab - maintains crontab files for individual users 
    -e : Edits the current crontab using the editor specified by the VISUAL or EDITOR environment variables.
    -r : Removes the current crontab.
    -u : Appends the name of the user whose crontab is to be modified.
    -l : Displays the current crontab on standard output.

24. ssh - OpenSSH SSH client (remote login program)

25. scp - secure copy (remote file copy program)

26. wget - The non-interactive network downloader.
    -b, --background: Go to background immediately after startup. If no output file is specified via the -o, output is redirected to wget-log.
    -O , --output-document=file : The documents will not be written to the appropriate files, but all willbe concatenated together and written to file.
    -c, --continue : Continue getting a partially-downloaded file. This is useful when you want to finished up a download started by a previous instance of Wget, or by another program. 

27. ip - show / mainpulate routing, devices, policy routing and tunnels
    ip addr : Shows addresses assigned to all network interfaces. 

28. netstat - Print network connections, routing tables, interface statistics, masquerade connections, and multicast memberships 
    -t, --tcp: 
    -u, --udp:
    -n, --numeric: Show numerical addresses instead of trying to determine symbolic host, port or user names.

[chyi@zong ~]$ netstat -tn | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -n      # 查看服务器IP连接数
      1 100.67.8.32
      1 100.67.8.33
      1 101.88.222.63
      1 Address
      1 servers)
      2 100.67.8.25
      2 127.0.0.1
      2 58.247.91.82

29. awk, gawk - pattern scanning and processing language.
    
30. cut - remove sections from each line of files.
    -d, --delimiter=DELIM: use DELIM instead of TAB for field delimiter 
    -f, --fields=LIST: select only these fields; also print ant line that contains no delimiter character, unless the -s option is specified.    

31. sort - sort lines of text files
    -n, --numeric-sort: compare according to string numerical value 
    -r, --reverse: reverse the result of comparisons 

32. uniq - report or omit repeated lines 
    -c, --count: prefix lines by the number of occurrences.

33. tail - output the last part of files 
    -f, --follow: output appended data as the file grows
    -c, --bytes=K: output the last K bytes; or use -c +K to output bytes starting with the Kth of each file.
    -n, --lines=K: output the last K lines, instead of the last 10; or use -n +K to output starting with the Kth.
```

![Linux Performance Tools](/imgs/raspberrypi/Linux101/linux_perf_tools_full.png?raw=true)
```
在Linux不同子系统出现性能问题后，应该用什么样的工具来观测和分析.
性能问题的本质：就是系统资源已经达到瓶颈、但请求的处理还不够快，无法支撑更多的请求.
性能分析：就是找出应用或系统的瓶颈，并设法去避免或者缓解，从而更高效地利用系统资源处理更多的请求。
    选择指标评估应用程序和系统的性能
    为应用程序和系统设置性能目标
    进行性能基准测试
    性能分析定位瓶颈
    优化系统和应用程序
    性能监控和告警

性能领域大师 Brendan Gregg. 不仅是动态追踪工具DTrace的作者，特别注意就是性能工具的选用，一个正确的选择胜过千百次的努力。但是切记，千万不要把性能工具当作学习的全部，工具只能解决问题的手段，关键在于你的用法，主要真正理解他们背后的原理，并且结合具体场景，融汇贯通系统的不同组件，才能真正掌握他们.
```

平均负载
--------
```
╭─    ~ ─────────────────────────────────────────────────────────────────────────────── ✔  with pi at RPi3BPlus
╰─ uptime
 09:25:51 up 8 days, 20:22,  4 users,  load average: 0.45, 0.20, 0.13
09:25:51  // 当前时间
8 days, 20:22  // 系统运行时间
4 users // 当前登陆用户数
0.45, 0.20, 0.13 // 过去1分钟，5分钟， 15分钟的平均负载(Load Average)

uptime gives a one line display of the following information.  The current time, how long the system has been running, how many users are currently logged on, and the system load averages for the past 1, 5, and 15  min‐utes.

平均负载是指单位时间内，系统处于可运行状态和不可中断状态的平均进程数，也就是平均活跃进程数.和CPU使用率没有直接关系。
    可运行状态的进程：正在使用CPU或者正在等待CPU进程，也是ps命令看到处于R状态(Running或Runnable)的进程
    不可中断状态的进程：正处于内核态关键流程中的进程，并且这些流程是不可中断，比如常见等待硬件设备I/O响应,ps命令中的D状态(Uninterruptible Sleep).
    不可中断状态实际上是系统对进程和硬件设备的一种保护机制
平均负载其实就是平均活跃进程数，平均活跃进程数，直观上理解就是单位时间内的活跃进程数，实际上是活跃进程数的指数衰减平均值，理想情况下，就是每个CPU上都刚好运行着一个进程，这样每个CPU都得到充分利用.

# 获取系统有多少CPU
$ grep 'processor' /proc/cpuinfo | wc -l

平均负载与CPU使用率：
    平均负载是指单位时间内，处于可运行状态和不可中断状态的进程数，包含正在使用的CPU的进程还包括等待CPU和等待IO的进程
    CPU使用率是单位时间内CPU繁忙情况的统计，跟平均负载并不一定完全一致
    CPU密集型进程，使用大量CPU会导致平均负载升高，此时CPU利用率和平均负载是一致的
    I/O密集型进程，等待I/O会导致平均负载升高，但CPU使用率不一定很高
    大量等待CPU进程调度也会导致平均负载升高，此时的CPU使用率也会比较高

# 安装stress, sysstat 
$ sudo apt-get install stress sysstat 
    stress: 是Linux系统压力测试工具，用于异常进程模拟平均负载升高的场景
    sysstat: 是Linux性能工具,用来监控和分析系统的性能。
        mpstat: 常用的多核CPU性能分析工具，用来实时查看每个CPU的性能指标，以及所有CPU的平均指标
        pidstat: 是一个常用的进程性能分析工具，用来实时查看进程的CPU、内存、I/O以及上下文切换等性能指标

# 场景一: CPU密集型进程
    首先，模拟一个CPU使用率100%的
    $ sudo stress --cpu 1 --timeout 600
   
    观察uptime查看平均负载
    $ sudo watch -d uptime  # -d 查看表示高亮显示变化的区域
    Every 2.0s: uptime                                                        RPi3BPlus: Wed Aug 28 11:23:49 2019
    11:23:49 up 8 days, 22:20,  8 users,  load average: 1.15, 0.73, 0.40

    查看CPU使用率的变化情况
    $ sudo mpstat -P ALL 5  # -P ALL 表示监控所有的CPU，后面数字表示间隔5秒输出一组数据
    11:23:13 AM  CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle
    11:23:18 AM  all   26.76    0.00    0.46    0.10    0.00    0.05    0.00    0.00    0.00   72.63
    11:23:18 AM    0   99.80    0.00    0.00    0.00    0.00    0.20    0.00    0.00    0.00    0.00
    11:23:18 AM    1    1.41    0.00    0.81    0.00    0.00    0.00    0.00    0.00    0.00   97.78
    11:23:18 AM    2    0.41    0.00    0.21    0.41    0.00    0.00    0.00    0.00    0.00   98.97
    11:23:18 AM    3    4.06    0.00    0.81    0.00    0.00    0.00    0.00    0.00    0.00   95.13
    
    查看具体进程CPU使用率
    $ sudo pidstat -u 5 1  # 间隔5秒后输出一组数据
    Linux 4.15.0-1043-raspi2 (RPi3BPlus)    08/28/2019      _aarch64_       (4 CPU)

    11:25:55 AM   UID       PID    %usr %system  %guest   %wait    %CPU   CPU  Command
    11:26:00 AM     0         8    0.00    0.20    0.00    0.00    0.20     0  rcu_preempt
    11:26:00 AM     0        51    0.00    0.20    0.00    0.00    0.20     2  kswapd0
    11:26:00 AM   111      1356    0.20    0.20    0.00    0.00    0.40     0  redis-server
    11:26:00 AM     0      1373    0.79    0.00    0.00    0.00    0.79     1  containerd
    11:26:00 AM  1001      1544    0.20    0.00    0.00    0.00    0.20     1  java
    11:26:00 AM   112      1860    0.20    0.00    0.00    0.00    0.20     1  mysqld
    11:26:00 AM     0      3313   99.80    0.00    0.00    0.20   99.80     1  stress
    11:26:00 AM     0      4108    0.00    0.20    0.00    0.00    0.20     2  mpstat
    11:26:00 AM     0      4309    0.00    0.20    0.00    0.00    0.20     1  kworker/1:1
    11:26:00 AM     0      5276    0.40    0.79    0.00    0.00    1.19     3  pidstat
    11:26:00 AM  1001      8508    0.40    0.99    0.00    0.00    1.39     3  nload
    11:26:00 AM  1001     16267    1.19    0.20    0.00    0.40    1.39     0  tmux: server
    11:26:00 AM  1001     16505    0.00    0.20    0.00    0.00    0.20     3  sshd

    Average:      UID       PID    %usr %system  %guest   %wait    %CPU   CPU  Command
    Average:        0         8    0.00    0.20    0.00    0.00    0.20     -  rcu_preempt
    Average:        0        51    0.00    0.20    0.00    0.00    0.20     -  kswapd0
    Average:      111      1356    0.20    0.20    0.00    0.00    0.40     -  redis-server
    Average:        0      1373    0.79    0.00    0.00    0.00    0.79     -  containerd
    Average:     1001      1544    0.20    0.00    0.00    0.00    0.20     -  java
    Average:      112      1860    0.20    0.00    0.00    0.00    0.20     -  mysqld
    Average:        0      3313   99.80    0.00    0.00    0.20   99.80     -  stress
    Average:        0      4108    0.00    0.20    0.00    0.00    0.20     -  mpstat
    Average:        0      4309    0.00    0.20    0.00    0.00    0.20     -  kworker/1:1
    Average:        0      5276    0.40    0.79    0.00    0.00    1.19     -  pidstat
    Average:     1001      8508    0.40    0.99    0.00    0.00    1.39     -  nload
    Average:     1001     16267    1.19    0.20    0.00    0.40    1.39     -  tmux: server
    Average:     1001     16505    0.00    0.20    0.00    0.00    0.20     -  sshd

场景二：I/O密集型进程
    # 运行stress模拟I/O压力，不断执行sync 
    $ sudo stress -i 1 --timeout  600

    # 查看平均负载
    $ watch -d uptime 

    # 运行mpstat 查看CPU使用率变化
    $ sudo mpstat -P ALL 5 1 # 显示所有CPU的指标，并在间隔5秒输出一组数据
    $ sudo pidstat -u 5 # 间隔5秒后输出一组数据， -u表示CPU指标

场景三： 大量进程的场景
    当系统中运行进程超出CPU运行能力，就会出现等待CPU的进程
    $ sudo stress -c 8 --timeout 600  # 模拟8个进程
    
    # 查看平均负载,明显8个进程要多余CPU数，系统CPU处于严重过载状态，平均负载过高
    Every 2.0s: uptime                                              RPi3BPlus: Wed Aug 28 13:11:39 2019
    13:11:39 up 9 days, 8 min,  8 users,  load average: 7.18, 3.28, 1.55

    # 运行pidstat 查看进程情况
    $ sudo pidstat -u 5  # 间隔5秒后输出数据
    01:13:21 PM   UID       PID    %usr %system  %guest   %wait    %CPU   CPU  Command
    01:13:26 PM     0         8    0.00    0.20    0.00    0.00    0.20     0  rcu_preempt
    01:13:26 PM     0       328    0.00    0.20    0.00    0.20    0.20     3  kworker/3:1
    01:13:26 PM     0       592    0.00    0.20    0.00    0.00    0.20     1  jbd2/mmcblk0p2-
    01:13:26 PM     0      1085    0.00    0.20    0.00    0.00    0.20     2  kworker/2:2
    01:13:26 PM   111      1356    0.40    0.20    0.00    0.00    0.60     1  redis-server
    01:13:26 PM  1001      1544    0.20    0.20    0.00    0.00    0.40     1  java
    01:13:26 PM   112      1860    0.20    0.00    0.00    0.00    0.20     1  mysqld
    01:13:26 PM     0      2953    0.00    0.20    0.00    0.00    0.20     1  kworker/1:1
    01:13:26 PM  1001      3564    0.60    0.00    0.00    0.60    0.60     2  watch
    01:13:26 PM     0      4664    0.40    0.80    0.00    2.00    1.20     1  pidstat
    01:13:26 PM     0      5321   48.80    0.40    0.00   51.20   49.20     2  stress
    01:13:26 PM     0      5322   47.80    0.60    0.00   52.00   48.40     1  stress
    01:13:26 PM     0      5323   48.40    0.20    0.00   51.60   48.60     1  stress
    01:13:26 PM     0      5324   48.20    0.40    0.00   51.80   48.60     0  stress
    01:13:26 PM     0      5325   48.20    0.20    0.00   51.60   48.40     3  stress
    01:13:26 PM     0      5326   48.00    0.40    0.00   51.60   48.40     0  stress
    01:13:26 PM     0      5327   49.20    0.60    0.00   50.20   49.80     3  stress
    01:13:26 PM     0      5328   48.00    0.60    0.00   51.20   48.60     2  stress
    01:13:26 PM  1001      8508    0.80    0.60    0.00    0.20    1.40     3  nload
    01:13:26 PM  1001     10899    2.60    1.60    0.00    0.00    4.20     3  mysqldump
    01:13:26 PM     0     13504    0.00    0.20    0.00    0.00    0.20     0  kworker/u8:3
    01:13:26 PM  1001     16267    0.20    0.00    0.00    0.00    0.20     0  tmux: server
    01:13:26 PM  1001     16505    0.20    0.00    0.00    0.00    0.20     0  sshd

    01:13:26 PM   UID       PID    %usr %system  %guest   %wait    %CPU   CPU  Command
    01:13:31 PM     0         8    0.00    0.20    0.00    0.00    0.20     1  rcu_preempt
    01:13:31 PM     0         9    0.00    0.20    0.00    0.00    0.20     3  rcu_sched
    01:13:31 PM     0        15    0.00    0.20    0.00    0.00    0.20     1  ksoftirqd/1
    01:13:31 PM     0        20    0.00    0.20    0.00    0.00    0.20     2  ksoftirqd/2
    01:13:31 PM     0      1325    0.20    0.00    0.00    0.00    0.20     3  accounts-daemon
    01:13:31 PM   111      1356    0.00    0.20    0.00    0.00    0.20     1  redis-server
    01:13:31 PM     0      1373    0.20    0.00    0.00    0.00    0.20     1  containerd
    01:13:31 PM  1001      1544    0.00    0.20    0.00    0.00    0.20     1  java
    01:13:31 PM   112      1860    0.20    0.20    0.00    0.00    0.40     1  mysqld
    01:13:31 PM  1001      3564    0.80    0.20    0.00    1.40    1.00     3  watch
    01:13:31 PM     0      3970    0.00    0.20    0.00    0.00    0.20     0  kworker/u8:1
    01:13:31 PM     0      4664    0.20    1.00    0.00    2.20    1.20     1  pidstat
    01:13:31 PM     0      5321   46.20    0.20    0.00   53.80   46.40     2  stress
    01:13:31 PM     0      5322   47.20    0.20    0.00   52.60   47.40     2  stress
    01:13:31 PM     0      5323   47.00    0.40    0.00   52.60   47.40     3  stress
    01:13:31 PM     0      5324   46.00    0.60    0.00   53.00   46.60     1  stress
    01:13:31 PM     0      5325   46.60    0.60    0.00   52.80   47.20     3  stress
    01:13:31 PM     0      5326   47.00    0.40    0.00   52.80   47.40     0  stress
    01:13:31 PM     0      5327   46.80    0.40    0.00   52.80   47.20     1  stress
    01:13:31 PM     0      5328   46.20    0.40    0.00   53.60   46.60     0  stress
    01:13:31 PM  1001      8508    0.20    1.20    0.00    0.00    1.40     3  nload
    01:13:31 PM  1001     10899    3.00    1.40    0.00    0.20    4.40     0  mysqldump
    01:13:31 PM  1001     16267    2.00    0.60    0.00    3.00    2.60     2  tmux: server
    01:13:31 PM  1001     16505    0.20    0.20    0.00    0.00    0.40     2  sshd
平均负载高的时候可以使用mpstat, pidstat 工具，辅助分析负载来源
```

CPU上下文切换
-------------
![CPU 上下文](/imgs/raspberrypi/Linux101/CPU_Content.png?raw=true)
```
Linux是一个多任务操作系统，支持远大于CPU核心数的任务同时运行，每个任务运行前，CPU需要知道任务从那里加载和运行，需要系统事前处理CPU寄存器和程序计数器Program Counter, PC.

CPU 寄存器：CPU内置的容量小，速度极快的内存。
程序计数器：用来存储CPU正在执行的指令位置、或者即将执行的下一条指令位置。他们都是CPU在运行任何任务前，必须的依赖环境，因此叫做CPU上下文

CPU上下文切换：就是先把前一个任务的CPU上下文(CPU寄存器和程序计数器)保存，然后加载新任务的上下文到寄存器和程序计数器，最后跳转到程序计数器所指的新位置.运行新任务.保存下来的上下文会存储在系统内核中，并在任务重新调度执行时再次加载进来。这样就能保证任务原来的状态不受影响，让任务看起来还是连续运行.

CPU上下文切换分为:
    进程上下文切换
    线程上下文切换
    中断上下文切换

# 进程上下文切换： 
Linux按照特权等级，把进程的运行空间分为内核空间(Ring 0)和用户空间(Ring 3)。
    内核空间(Ring 0) 具有最高权限，可以直接访问所有资源
    用户空间(Ring 3) 只能访问受限资源，不能直接访问内存等硬件设备，必须通过系统调用陷入到内核中，才能访问这些特权资源.
进程可以在用户空间运行又可以在内核空间运行，进程在用户空间运行时，被称为进程的用户态，而陷入内核空间的时候，被称为进程的内核态.
一次系统调用的过程，发生两次CPU上下文切换。CPU寄存器原来用户态的指令位置需要先保存起来，接着，为了执行内核态代码，CPU寄存器需要更新为内核态的新位置，最后才是跳转到内核态运行内核任务，系统调用结束后，CPU寄存器需要恢复原来保存的用户态，然后再切换到用户空间.

进程上下文切换:是指从一个进程切换到另一个进程运行
系统调用：过程中始终是同一个进程在运行，通常称为特权模式切换，而不是上下文切换。
进程是由内核来管理和调度，进程的切换只能发生在内核态，所以，进程的上下文不仅包括虚拟内存、栈、全局变量等用户空间的资源，还包括内核堆栈、寄存器等内核空间的状态.
进程的上下文切换比系统调用时多一些步骤，在保存当前进程的内核态和CPU寄存器之前，需要先把该进程的虚拟内存、栈等保存下来，加载下一进程的内核态后，还需要刷新进程的虚拟内存和用户栈。

[How long does it take to make a context switch?](https://blog.tsunanet.net/2010/11/how-long-does-it-take-to-make-context.html)
每次上下文切换都需要几十纳秒到数微妙的CPU时间，这个时间还是相当可观，特别是在进程上下文切换次数较多的情况下，很容易导致CPU将大量时间耗费在寄存器、内核栈以及虚拟内存等资源的保存和恢复上。进而大大缩短真正运行进程的时间。

Linux通过TLB(Translation Lookaside Buffer)管理虚拟内存到物理内存的映射关系.当虚拟内存更新后，TLB也需要刷新，内存的访问会随着变慢，特别是多处理器系统上，缓存是被多个处理器共享、刷新缓存不仅会影响当前处理器的进程还会影响共享缓存的其他处理器的进程.

Linux为每一个CPU都维护一个就绪队列，将活跃进程(即正在运行和正在等待CPU的进程)按照优先级和等待CPU的时间排序，然后选择最需要CPU的进程，也就是优先级最高和等待CPU时间最长的进程运行。
    程序调度场景:
        1. CPU 时间划分为一段段的时间片，这些时间再被轮流分配给各个进程，这样，当某个进程的时间片耗尽就会系统挂起，切换到其他正在等待CPU的进程运行
        2. 进程在系统资源不足（比如内存不足）时，要等资源满足后才可以运行，这时候进程会被挂起，并由系统调度其他进程运行
        3. 当进程通过睡眠函数sleep将自己主动挂起，系统调度会触发调用其他进程运行
        4. 为了保证高优先级进程的运行，当前进程被挂起，由高优先级进程运行
        5. 硬件中断，CPU上的进程会被中断挂起，转而执行内核中的中断服务程序

# 线程上下文切换:
    线程与进程最大的区别在于，线程是调度的基本单位，而进程则是资源拥有的基本单位.内核中的任务调度，实际上调度对象是线程，而进程只是给线程提供虚拟内存，全局变量等资源。
    当进程只有一个线程时，可以认为进程就等于线程
    当进程拥有多个线程时，这些线程会共享相同的虚拟内存和全局变量等资源，这些资源在上下文切换时是不需要修改的。
    线程也有自己的私有数据，比如栈和寄存器，这些上下文切换时需要保存.

    线程的上下文切换分为两种情况:
        1. 前后两个线程属于不同进程，此时因为资源不共享，所以切换过程就跟进程上下文切换一样
        2. 前后两个线程属于同一进程，因为虚拟内存是共享，所以在切换时，虚拟内存资源保持不动，只需要切换线程的私有数据，寄存器等不共享的数据

# 中断上下文切换
    为了快速响应硬件的事件，中断处理会打断正常调度和执行，转而调用中断处理程序,响应设备事件。
    中断上下文切换不涉及到进程的用户态，即使中断过程打断一个正处于用户态的进程，也不需要保存和恢复这个进程的虚拟内存、全局变量等用户态资源。中断上下文，只包括内核态中断服务程序执行所必需的状态，包括CPU寄存器、内核堆栈、硬件中断参数.
    对于同一个CPU，中断处理比进程拥有更高优先级，

1. CPU上下文切换，是保证Linux系统正常工作的核心功能之一
2. 过多的上下文切换、会把CPU事件消耗在寄存器、内核栈以及虚拟内存等数据的保存和恢复上，从而缩短进程真正运行的事件，导致系统的整体性能大幅下降.

# vmstat 系统性能分析工具
    主要用来分析系统的总体内存的使用情况和CPU上下文切换和中断次数
    $ vmstat 5  # 每隔五秒输出一组数
    procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
     r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
     0  0 322420 356448  42168 398264    1    1    73    19   19    4  4  3 93  1  0
    cs: (content switch) 每秒上下文切换的次数
    in: (interrupt) 每秒中断的次数
    r: (Running or Runnable) 就绪队列的长度，正在运行和等待CPU的进程数 
    b: (Blocked) 处于不可中断睡眠状态的进程数 
    us(user), sy(system)
# pidstat -w : 查看每个进程上下文切换
╰─ pidstat -w 5
Linux 4.15.0-1043-raspi2 (RPi3BPlus)    09/02/2019      _aarch64_       (4 CPU)

06:30:19 PM   UID       PID   cswch/s nvcswch/s  Command
06:30:24 PM     0         7      1.78      0.00  ksoftirqd/0
06:30:24 PM     0         8     50.79      0.00  rcu_preempt
06:30:24 PM     0         9      0.59      0.00  rcu_sched
06:30:24 PM     0        15      2.37      0.00  ksoftirqd/1
06:30:24 PM     0        20      0.79      0.00  ksoftirqd/2
06:30:24 PM     0        25      1.58      0.00  ksoftirqd/3
06:30:24 PM     0       158      0.99      0.00  mmcqd/0
06:30:24 PM  1001       577      0.40      2.17  top
06:30:24 PM     0      1339      0.20      0.00  wpa_supplicant
06:30:24 PM   111      1356      9.88      0.00  redis-server
06:30:24 PM   114      1857      0.20      0.00  postgres
06:30:24 PM  1001      3167      5.73      0.00  tmux: server
06:30:24 PM  1001      3745      0.99      0.00  gitstatusd-linu
06:30:24 PM  1001      3934      0.99      0.00  gitstatusd-linu
06:30:24 PM  1001      4480      0.99      0.00  gitstatusd-linu
06:30:24 PM  1001      4827      0.40      0.00  sshd
06:30:24 PM  1001      4868      0.99      0.00  gitstatusd-linu
06:30:24 PM  1001      5889      0.99      0.00  gitstatusd-linu
06:30:24 PM  1001      6520      0.99      0.00  gitstatusd-linu
06:30:24 PM  1001      6769      0.99      0.00  gitstatusd-linu
06:30:24 PM  1001      6813      0.40      1.78  top
06:30:24 PM  1001      8715      9.88      0.20  nload
06:30:24 PM     0     14415      9.49      0.00  kworker/u8:3
06:30:24 PM     0     14528      0.40      0.00  kworker/1:1
06:30:24 PM     0     14602     14.03      0.00  kworker/u8:1
06:30:24 PM     0     14619      6.92      0.00  kworker/0:2
06:30:24 PM  1001     14663      0.99      0.00  gitstatusd-linu
06:30:24 PM     0     14675      0.20      0.00  kworker/2:0
06:30:24 PM     0     14686     21.15      0.00  kworker/1:2
06:30:24 PM     0     14688     19.57      0.20  kworker/2:1
06:30:24 PM     0     14692      9.88      0.00  kworker/3:2
06:30:24 PM  1001     14695      0.20      1.38  pidstat
06:30:24 PM  1001     18009      0.79      0.00  ssh
06:30:24 PM  1001     22813      0.99      0.00  gitstatusd-linu
06:30:24 PM  1001     29139      1.78      0.00  ssh
06:30:24 PM  1001     31596      0.99      0.00  gitstatusd-linu
06:30:24 PM  1001     31606      0.40      0.00  ssh
    cswch/s: 每秒自愿上下文切换(voluntary context switches) 
    nvcswch/s: 每秒非自愿上下文切换(non voluntary context switches) 次数
    自愿上下文切换: 是指进程无法获取所需资源，导致的上下文切换 (I/O,内存等系统资源不足，发生自愿上下文切换)
    非自愿上下文切换: 是指进程由于时间片耗尽等原因，被系统强制调度，进而发生上下文切换. (大量进程在争抢CPU时，就容易发生非自愿上下文切换)

# sysbench: 多线程基准测试工具,评估不同系统参数下的数据库负载情况 
$ sudo apt-get install sysbench 

# vmstat查看空闲系统上下文切换次数
$ vmstat 1 1  # 间隔1秒输出1组数据
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 0  0 296308  25092 193212 562232    1    1    59    16    6   20  3  2 94  1  0

# 以10个线程运行5分钟的基准测试，模拟多线程切换问题
$ sysbench --threads=10 --max-time=300 threads run 

$ vmstat 1
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 8  0 296308  21200 193328 563824    1    1    59    16    8   21  3  2 94  1  0
 5  0 296308  21076 193328 563824    0    0     0     0 58111 199585  6 68 26  0  0
 4  0 296308  21092 193328 563824    0    0     0     0 62652 207594  7 64 29  0  0
 7  0 296308  21092 193328 563824    0    0     0     0 69439 235364  7 65 28  0  0
 5  0 296308  21092 193328 563824    0    0     0     0 61985 202831  6 66 28  0  0
11  0 296308  18976 193328 563824    0    0     0     0 43352 225974 11 74 14  0  0

# pidstat 查看CPU和进程上下文切换
$ pidstat -wt  # 表示输出线程的上下文切换指标
Average:      UID       PID   cswch/s nvcswch/s  Command
Average:        0         7     12.02      0.00  ksoftirqd/0
Average:        0         8     61.02      0.00  rcu_preempt
Average:        0         9      2.99      0.00  rcu_sched
Average:        0        11      0.44      0.00  migration/0
Average:        0        14      0.31      0.00  migration/1
Average:        0        15     10.52      0.00  ksoftirqd/1
Average:        0        20      7.35      0.00  ksoftirqd/2
Average:        0        24      0.31      0.00  migration/3
Average:        0        25      7.60      0.00  ksoftirqd/3
Average:        0       158      0.37      0.00  mmcqd/0
Average:        0       585      0.19      0.00  jbd2/mmcblk0p2-
Average:        0       923    152.93      0.00  kworker/u8:1
Average:        0      1302      0.06      0.00  irqbalance
Average:        0      1339      0.12      0.00  wpa_supplicant
Average:      111      1356      9.96      0.00  redis-server
Average:     1001      1409      1.00      0.06  gitstatusd-linu
Average:      114      1856      0.12      0.00  postgres
Average:      114      1857      0.19      0.00  postgres
Average:     1001      3167      3.86      9.78  tmux: server
Average:     1001      3484      0.50      0.31  ssh
Average:     1001      3745      1.00      0.00  gitstatusd-linu
Average:     1001      3934      1.00      0.00  gitstatusd-linu
Average:     1001      4480      1.00      0.00  gitstatusd-linu
Average:     1001      5726      1.00      0.00  gitstatusd-linu
Average:        0     15260    107.16      0.00  kworker/u8:0
Average:     1001     17249      1.00      0.00  gitstatusd-linu
Average:        0     17546     24.91      0.00  kworker/3:2
Average:     1001     17624      1.00      0.00  gitstatusd-linu
Average:     1001     17862     42.84      9.65  sshd
Average:     1001     18009      0.75      0.31  ssh
Average:        0     18030     27.09      0.00  kworker/1:1
Average:        0     18917     27.15      0.00  kworker/2:2
Average:        0     18918     24.35      0.00  kworker/0:0
Average:     1001     19299      1.00    392.78  pidstat
Average:     1001     22813      1.00      0.12  gitstatusd-linu
Average:     1001     24193      0.12      0.00  ssh
Average:     1001     29139      1.99      0.93  ssh
Average:        0     30734      0.06      0.00  kworker/1:0
Average:     1001     31596      1.00      0.06  gitstatusd-linu
Average:     1001     31606      0.12      0.00  ssh

# /proc/interrupts
    /proc是Linux的虚拟文件系统，用于内存空间与用户空间之间的通信
    /proc/interrupts: 提供只读中断使用情况
    
$ watch -d cat /proc/interrupts  # -d 参数表示高亮显示变化的区域
Every 2.0s: cat /proc/interrupts                                            RPi3BPlus: Tue Sep  3 18:34:26 2019
           CPU0       CPU1       CPU2       CPU3
  2:   25926363   28694111   26208155   27868740  bcm2836-timer   1 Edge      arch_timer
  6:     495749     492728     495516     489639  ARMCTRL-level   1 Edge      3f00b880.mailbox
  7:          1          0          0          0  ARMCTRL-level   2 Edge      VCHIQ doorbell
  9:          0          0          0          0  bcm2836-pmu   9 Edge      arm-pmu
 15:  238759636  221331334  238767919  221407049  ARMCTRL-level  64 Edge      dwc_otg, dwc_otg_pcd, dwc_otg_hcd:usb1
 41:  902420602  884308649  902303339  884295265  ARMCTRL-level  41 Edge      dwc_otg_sim-fiq
 48:          0          0          0          0  ARMCTRL-level  48 Edge      bcm2708_fb dma
 50:          0          0          0          0  ARMCTRL-level  50 Edge      DMA IRQ
 52:          0          0          0          0  ARMCTRL-level  52 Edge      DMA IRQ
 53:          0          0          0          0  ARMCTRL-level  53 Edge      DMA IRQ
 56:          0          0          0          0  ARMCTRL-level  56 Edge      DMA IRQ
 57:      74887      74814      74435      79090  ARMCTRL-level  57 Edge      DMA IRQ
 58:     642815     643607     643224     644507  ARMCTRL-level  58 Edge      DMA IRQ
 61:          5          1          4          4  ARMCTRL-level  61 Edge      bcm2835-auxirq
 68:          0          0          0          0  ARMCTRL-level  85 Edge      3f804000.i2c
 69:          0          0          0          0  ARMCTRL-level  86 Edge      3f204000.spi
 71:     122183     121499     121409     121484  ARMCTRL-level  88 Edge      mmc0
 77:    4332185    4346108    4174511    4521970  ARMCTRL-level  94 Edge      mmc1
151:          4          1          3          4  bcm2835-auxirq   0 Edge      ttyS0
154:          0          0          0          0  lan78xx-irqs  17 Edge      usb-001:004:01
IPI0:  19104211   20438903   23613907   19665014       Rescheduling interrupts
IPI1:       167       2592       2562       2614       Function call interrupts
IPI2:         0          0          0          0       CPU stop interrupts

RES(Rescheduling interrupts) 重调度中断: 唤醒空闲状态CPU调度新任务运行,这是多处理器系统SMP中调度器用来分散任务到不同CPU的机制，通常也被称为处理器间中断(Inter-Processor Interrupts, IPI)
```

CPU使用率
---------
> CPU使用率是单位时间内CPU使用情况的统计.
```
Linux 作为一个多任务操作系统，将每个CPU的时间划分为很短时间片，再通过调度器轮流分配给各个任务使用，因此造成多任务同时运行的错觉.

# 查看节拍率HZ的内核可配选项
$ sudo grep 'CONFIG_HZ='  /boot/config-$(uname -r)
[sudo] password for pi:
CONFIG_HZ=250

# Jiffies 记录开机以来的Jiffy数(每发生一次时间中断, jiffies值加1)
# How to obtain the current number of jiffies since reboot in Linux?
Historically, the kernel used 100 as the value for HZ, yielding a jiffy interval of 10ms. With 2.4, the HZ value for i386 was changed to 1000, yeilding a jiffy interval of 1ms. Recently(2.6.13) the kernel changed HZ for i386 to 250. (1000 was deemed too high).

# 用户空间节拍率
USER_HZ = 100 # 1/100 秒 == 10ms 

# Linux通过/proc虚拟文件系统向用户空间提供系统内部状态的信息
/proc/stat : 系统统计CPU和任务统计信息
$ cat /proc/stat | grep ^cpu
cpu  557751 33324 475185 101564282 165505 0 49939 0 0 0     # 以下各行累加值
cpu0 178851 12729 72549 25343809 38723 0 18555 0 0 0        # 不同场景下CPU的累计节拍数，单位为USER_HZ 
cpu1 129852 5960 136469 25399794 40833 0 5550 0 0 0
cpu2 124554 5430 133233 25408847 42225 0 20515 0 0 0
cpu3 124493 9204 132932 25411831 43722 0 5318 0 0 0
    
    user (us) 代表用户态CPU的时间,不包括nice时间,包括guest时间
    nice (ni) 代表低优先级用户态CPU时间，进程nice值为1-19之间的CPU时间，nice值可取范围是-20到19,数值越大，优先级反而越低
    system (sys): 代表内核态CPU的时间
    idle (id): 代表空闲时间，不包括等待IO的时间iowait 
    iowait (wa): 代表等待I/O的CPU时间
    irq (hi): 代表处理硬中断的CPU时间
    softirq (si): 代表处理软中断的CPU时间
    steal (st): 代表当系统运行在虚拟机中时候，被其他虚拟机占用的CPU时间
    guest (guest): 代表通过虚拟化运行其他操作系统的时间，也就是运行虚拟机是的CPU时间
    guest_nice (gnice): 代表低优先级运行虚拟机的时间

CPU 使用率: 就是除去空闲外的其他时间占总CPU时间的百分比

# Linux 每个进程提供运行情况统计情况

性能分析工具给出的都是间隔一段时间的平均CPU使用率

$ top : 显示系统总体的CPU和内存使用情况，以及各个进程的资源使用情况
    默认每3秒刷新一次，默认是所有CPU的平均值，按下数字1，切换到每个CPU的使用率

$ pidstat: 显示进程CPU使用率 
    %usr: 用户态CPU使用率
    %system: 内核态CPU使用率
    %guest: 运行虚拟机CPU使用率
    %wait: 等待CPU使用率
    %CPU: 总的CPU使用率

$ ps: 只显示每个进程的资源使用情况

GDB: The GNU Project Debugger: 程序调试
$ sudo apt-get install linux-tools-common 
$perf: Linux2.6.31之后性能分析工具,以性能时间采集为基础,不仅可以分析系统的各种时间和内核性能，还用于分析指定应用程序的性能问题.
$ perf top : 显示占用CPU时钟最多的函数或者指令，用于查找热点函数
采样率          事件类型            事件总数
Samples: 53K of event 'cycles:ppp', Event count (approx.): 1734264782
Overhead  Shared Object                                   Symbol
  32.68%  [kernel]                                        [k] arch_cpu_idle
   4.58%  [kernel]                                        [k] _raw_spin_unlock
   3.28%  [kernel]                                        [k] _raw_spin_unlock
   1.45%  perf                                            [.] d_print_comp_inn
   1.37%  perf                                            [.] rb_next
   1.27%  containerd                                      [.] _start
   1.20%  perf                                            [.] __hists__add_ent
   1.20%  perf                                            [.] perf_hpp__is_dyn
   1.19%  [kernel]                                        [k] rcu_idle_exit
   1.16%  perf                                            [.] sort__sym_cmp
   1.11%  [kernel]                                        [k] __softirqentry_t
   1.01%  perf                                            [.] __symbols__inser
   0.89%  libc-2.27.so                                    [.] strcmp
   0.82%  libc-2.27.so                                    [.] __libc_calloc
   0.80%  [kernel]                                        [k] format_decode
   0.79%  perf                                            [.] sort__dso_cmp
   0.77%  [kernel]                                        [k] vsnprintf
   0.74%  [kernel]                                        [k] tick_nohz_idle_e
no symbols found in /bin/dash, maybe install a debug package?

第一列Overhead: 该符号的性能事件所有采样中的比例
第二列Shared Object: 是指函数或指令所在动态共享对象(Dynamic Shared Object) 内核、进程名、动态链接库名、内核模块名
第三列Object: 动态共享对象的类型 [.]用户空间的可执行程序或动态链接库 [k]内核空间
第四列Symbol: 函数名，函数名未知时使用十六进制地址表示

$ perf record -g  # 展示系统性能信息并保存
[sudo] password for pi:
^C[ perf record: Woken up 13 times to write data ]
[ perf record: Captured and wrote 3.657 MB perf.data (71445 samples) ]

$ pref report  # 解析保存后的perf record 
```
![Linux perf report command](/imgs/raspberrypi/Linux101/perf_report.png?raw=true)

* Nginx + PHP Performance Test
```
$ sudo apt-get install docker.io sysstat linux-tools-common apache2-utils 

ab (apache bench): 是一个常用的HTTP服务性能测试工具
    虚拟机01: Nginx php  - Web服务器
        $ docker run --name nginx -p 10000:80 -itd feisky/nginx 
        $ docker run --name phpfpm -itd --network container:nginx feisky/php-fpm 
    虚拟机02: ApacheBench - Web客户端
        $ curl http://[VM1 Public IP]:10000 
        It works!
        $ (centos) yum -y install httpd-tools
        $ ab -c 10 -n 100 http://chyidl.com:10000/  
             -c 10      # 并发10个请求
             -n 100     # 总共测试100请求
This is ApacheBench, Version 2.3 <$Revision: 1430300 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/
Benchmarking xxx.xxx.xxx.xxx (be patient).....done
Server Software:        nginx/1.15.4
Server Hostname:        xxx.xxx.xxx.xxx
Server Port:            10000
Document Path:          /
Document Length:        9 bytes
Concurrency Level:      10
Time taken for tests:   4.221 seconds
Complete requests:      100
Failed requests:        0
Write errors:           0
Total transferred:      17200 bytes
HTML transferred:       900 bytes
Requests per second:    23.69 [#/sec] (mean) -- Nginx能承受的每秒平均请求数
Time per request:       422.150 [ms] (mean)
Time per request:       42.215 [ms] (mean, across all concurrent requests)
Transfer rate:          3.98 [Kbytes/sec] received
Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:    89  399  86.4    401     589
Waiting:       89  399  86.4    401     589
Total:         89  399  86.4    401     589
Percentage of the requests served within a certain time (ms)
  50%    401
  66%    421
  75%    439
  80%    460
  90%    517
  95%    546
  98%    583
  99%    589
 100%    589 (longest request)
        $ ab -c 10 -n 10000 http://chyidl.com:10000/
        $ perf top -g -p 21027 
            -g 开启调用关系分析
            -p 指定php-fpm进程号21027

```

Signal numbering for standard signals
-------------------------------------
* signal - overview of signals
```
DESCRIPTION:
    Linux supports both POSIX reliable signals (hereinafer "standard signals") and POSIX real-time signals.
```

> The numberic value for each signal is given in the table below. As show in the table, many signals have different numberic values on different architectures. The first numberic value in each table row shows the signal number on x86, ARM, and most other architectures; the second value is for Alpha and SPARC; the third is for MIPS; and the last is for PARISC. A dash (-) doniotes that a signal is absent on the corresponding architecture.

| Signal    | x86/ARM | Alpha/SPARC | MIPS  | PARISC | Notes                                                                   |
| --------- | :-----: | :---------: | :---: | :----: | :---------------------------------------------------------------------- |
| SIGHUP    |    1    |      1      |   1   |   1    | Hangup detected on controlling terminal or death of controlling process |
| SIGINT    |    2    |      2      |   2   |   2    | Interrupt from keyboard                                                 |
| SIGQUIT   |    3    |      3      |   3   |   3    | Quit from keyboard                                                      |
| SIGILL    |    4    |      4      |   4   |   4    | Illegal Instruction                                                     |
| SIGTRAP   |    5    |      5      |   5   |   5    | Trace/breakpoint trap                                                   |
| SIGABRT   |    6    |      6      |   6   |   6    | Abort signal from abort(3)                                              |
| SIGIOT    |    6    |      6      |   6   |   6    | IOT trap. A synonym for SIGABRT                                         |
| SIGBUS    |    7    |     10      |  10   |   10   | Bus error (bad memory access)                                           |
| SIGEMT    |    -    |      7      |   7   |   -    | Emulator trap                                                           |
| SIGFPE    |    8    |      8      |   8   |   8    | Floating-point exception                                                |
| SIGKILL   |    9    |      9      |   9   |   9    | Kill signal                                                             |
| SIGUSR1   |   10    |     30      |  16   |   16   | User-defined signal 1                                                   |
| SIGSEGV   |   11    |     11      |  11   |   11   | Invalid memory reference                                                |
| SIGUSR2   |   12    |     31      |  17   |   17   | User-defined signal 2                                                   |
| SIGPIPE   |   13    |     13      |  13   |   13   | Broken pipe: write to pipe with no readers; see pipe(7)                 |
| SIGALRM   |   14    |     14      |  14   |   14   | Timer signal from alarm(2)                                              |
| SIGTERM   |   15    |     15      |  15   |   15   | Termination signal                                                      |
| SIGSTKFLT |   16    |      -      |   -   |   7    | Stack fault on coprocessor (unused)                                     |
| SIGCHLD   |   17    |     20      |  18   |   18   | Child stopped or terminated                                             |
| SIGCLD    |    -    |      -      |  18   |   -    | A synonym for SIGCHLD                                                   |
| SIGCONT   |   18    |     19      |  25   |   26   | Continue if stopped                                                     |
| SIGSTOP   |   19    |     17      |  23   |   24   | Stop process                                                            |
| SIGTSTP   |   20    |     18      |  24   |   25   | Stop typed at terminal                                                  |
| SIGTTIN   |   21    |     21      |  26   |   27   | Terminal input for background process                                   |
| SIGTTOU   |   22    |     22      |  27   |   28   | Terminal output for background process                                  |
| SIGURG    |   23    |     16      |  21   |   29   | Urgent condition on socket (4.2BSD)                                     |
| SIGXCPU   |   24    |     24      |  30   |   12   | CPU time limit exceeded (4.2BSD); see setrlimit(2)                      |
| SIGXFSZ   |   25    |     25      |  31   |   30   | File size limit exceeded (4.2BSD); see setrlimit(2)                     |
| SIGVTALRM |   26    |     26      |  28   |   20   | Virtual alarm clock (4.2BSD)                                            |
| SIGPROF   |   27    |     27      |  29   |   21   | Profiling timer expired                                                 |
| SIGWINCH  |   28    |     28      |  20   |   23   | Window resize signal (4.3BSD, Sun)                                      |
| SIGIO     |   29    |     23      |  22   |   22   | I/O now possible (4.2BSD)                                               |
| SIGPOLL   |         |             |       |        | Pollable event (Sys V). Synonym for SIGIO                               |
| SIGPWR    |   30    |    29/-     |  19   |   19   | Power failure (System V)                                                |
| SIGINFO   |    -    |    29/-     |   -   |   -    | A synonym for SIGPWR                                                    |
| SIGLOST   |    -    |    -/29     |   -   |   -    | File lock lost (unused)                                                 |
| SIGSYS    |   31    |     12      |  12   |   31   | Bad system call (SVr4); see also seccomp(2)                             |
| SIGUNUSED |   31    |      -      |   -   |   31   | Synonymous with SIGSYS                                                  |