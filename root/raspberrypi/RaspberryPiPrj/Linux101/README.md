Linux 101
=========

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
    虚拟机01: Nginx Php  - Web服务器
        $ docker run --name nginx -p 10000:80 -itd feisky/nginx 
        $ docker run --name phpfpm -itd --network container:nginx feisky/php-fpm 
    虚拟机02: ApacheBench - Web客户端
        $ ab -c 10 -n 100 http://chyidl.com:10000/  
             -c 10      # 并发10个请求
             -n 100     # 总共测试100请求
        This is ApacheBench, Version 2.3 <$Revision: 1826891 $>
        Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
        Licensed to The Apache Software Foundation, http://www.apache.org/
        Benchmarking chyidl.com (be patient).....done
        Server Software:        nginx/1.15.4
        Server Hostname:        chyidl.com
        Server Port:            10000
        Document Path:          /
        Document Length:        9 bytes
        Concurrency Level:      10
        Time taken for tests:   6.783 seconds
        Complete requests:      100
        Failed requests:        0
        Total transferred:      17200 bytes
        HTML transferred:       900 bytes
        Requests per second:    14.74 [#/sec] (mean)
        Time per request:       678.304 [ms] (mean)
        Time per request:       67.830 [ms] (mean, across all concurrent requests)
        Transfer rate:          2.48 [Kbytes/sec] received

        Connection Times (ms)
                      min  mean[+/-sd] median   max
        Connect:      168  199 144.6    176    1206
        Processing:   272  414 180.0    371    1309
        Waiting:      272  399 148.3    371    1309
        Total:        444  613 225.2    549    1572

        Percentage of the requests served within a certain time (ms)
          50%    549
          66%    590
          75%    611
          80%    626
          90%    876
          95%   1304
          98%   1529
          99%   1572
         100%   1572 (longest request)

```