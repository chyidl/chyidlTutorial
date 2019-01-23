Netdata
=======
    
Netdata is distributed, real-time, performance and health monitoring for systems and applications. It is a highly optimized monitoring agent your install on all your systems and containers.

Quick Start
-----------
* make sure you run **bash** for your shell 
* $ bash 
* install netdata, directly from github sources 
* bash <(curl -Ss https://my-netdata.io/kickstart.sh)

How it works
------------
* Collect: Data collection plugins collect metrics from all possible sources, every single second.
* Store: Internal round robin metrics database, supporting multiple readers and one writer concurrently.
* Check: An internal lockless watchdog evaluates health checks and triggers alarms.
* Stream: Metrics can be streamed, in full resolution and in real-time, between netdata servers.
* Archive: Metrics can be archived to industry standard time-series databases (backends).
* Query: The internal API with its low latency query engine supports highly interactive single page apps.

What does it monitor
--------------------
* APM (Application Performance Monitoring)
    - statsd - netdata is a fully featured statsd server 
    - Go expvar - collects metrics exposed by applications written in the Go programming language using the expvr package.
    - Spring Boot - monitors running Java Sprintg Boot applications that expose their metrics wth the use of the Spring Boot Actuator included in Spring Boot Libary
    - uWSGI - collects performance metrics from uWSGI applications.
* System Resources
    - CPU Utilization - total and per core CPU usage 
    - Interrupts - total and per core CPU interrupts 
    - SoftIRQs - total and per core SoftIRQs
    - SoftNet - total and per core SoftIRQs related to network activity.
    - CPU Throttling - collects per core CPU throttling.
    - CPU Frequency - collects the current CPU frequency
    - CPU Idle - collects the time spent per processor state 
    - IdleJitter - measyres CPU latency 
    - Entropy - random numbers pool, using in cryptigraphy 
    - Interprocess Communication - IPC - such as semaphores and semaphores arrays.
* Memory 
    - ram - collects info about RAM usage
    - swap - collects info about swap memory usage
    - available memory - collects the amount of RAM available for userspace processes.
    - committed memory - collects the amount of RAM committed to userspace processes.
    - Page Faults - collects the system page faults (major and minor)
    - writeback memory - collects the system dirty memory and writeback activity
    - huge pages - collects the amount of RAM used for huge page 
    - KSM - collects info about Kernel Same Merging (memory dedupper)
    - Numa - collects Numa info on systems that support it.
    - slab - collects info about the Linux kernel memory usage.
* Disks
    - block devices - per disk: I/O, operations, backlog, utilization, space, etc.
    - BCACHE - detailed performance of SSD caching devices.
    - DiskSpace - monitors disk space usage.
    - mdstat - software RAID 
    - hddtemp - disk temperatures
    - smartd - disk S.M.A.R.T.values 
    - device mapper - naming disks 
    - Veritas Volume Manager - naming disks 
    - megacli - adapter, physical drives and battery stats 
    - adaptec_raid - logical and physical devices health metrics 
* Filesystems
    - BTRFS - detailed disk space allocation and usage.
    - Caph - OSD usage, Pool usage, number of objects, etc
    - NFS file servers and clients - NFS v2,v3,v4:I/O,cache,read ahead, RPC calls
    - Samba - performance metrics of Samba SMB2 file sharing.
    - ZFS - detailed performance and resource usage.
* Networking 
    - Network Stack - ...


Getting Started
---------------
* Accessing the dashboard (http://your.server.ip:19999/)
* Starting and stopping Netdata 
    - $ sudo systemctl start|stop netdata
* Sizing Netdata
    - The default installation of netdata is configured for a small round-robin database,just 1 hour of data.
    - For every hour of data, Netdata needs about 25MB of RAM.
    - $ sudo vim /etc/netdata/netdata.conf 
```
[global]
    history = SECONDS (HOURS * 3600)
```
* Configuration quick start 
    - 