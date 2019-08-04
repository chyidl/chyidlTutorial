Monitor network bandwidth
=========================
> This post mentions some linux command line tools that can be used to monitor the network usage. These tools monitor the traffic flowing through network interfaces and measure the speed at which data is currently being transaferred. Incoming and outgoing traffic is shown separately.

> The tools have different mechanisms of generating the traffic report. Some of the tools like nload read the "/proc/net/dev" file to get traffic stats, whereas some tools use the pcap library to capture all packets and then calculate the total size to estimate the traffic load.
```
Here is a list of the commands, strted by their features.

1. Overall bandwidth - nload, bmon, slurm, bwm-ng, cbm, speedometer, netload
2. Overall bandwidth (batch style output) - vnstat, ifstat, dstat, collectl
3. Bandwith per socket connection - iftop, iptraf, tcptrack, pktstat, netwatch, trafshow 
4. Bandwidth per process - nethogs
```

1. nload
--------
> nload is a commandline tool that allows users to monitor the incoming and outgoing traffic separately. It also draws out a graph to indicate the same, the scale of which can be adjusted. Easy and simple to use, and does not support many options.
> So if you just need to take a quick look at the total bandwidth usage without details of individual processes, then nload will be handy.
```
# fedora or centos 
$ sudo yum install nload -y 

# ubuntu/debian 
$ sudo apt-get install nload

$ nload 
```
![nload command line](/imgs/raspberrypi/MonitorBandwidth/nload.png?raw=true)

2. iftop
--------
> iftop measures the data flowing through individual socket connections, and it works in a manager that is different from nload. iftop uses the pcap library to capture the packets moving in and out of the network adapter. and then sums up the size and cunt to find the total bandwidth under use.
> Although iftop reports the bandwidth used by individual connections, it cannot report the process name/id involved in the particular socket connection. But being based on the pcap library. iftop is able to filter the traffic and report bandwidth usage over selected connections as specified by the filter.
```
# fedora or centos 
$ sudo yum install iftop -y 

# ubuntu or debian 
$ sudo apt-get install iftop 

$ sudo iftop -n -i wlan0 
   -n                  don't do hostname lookups, which cuases additional network traffic of its own.
   -i interface        listen on named interface

```
![iftop command line](/imgs/raspberrypi/MonitorBandwidth/iftop.png?raw=true)

3. iptraf
---------
> iptraf is an interactive and colorful IP lan monitor. It shows individual connections and the amount of data flowing between the hosts.
```
# Centos (base repo)
$ sudo yum install iptraf 

# fedora or centos (with epel)
$ sudo yum install iptraf-ng -y 

# ubuntu or debian 
$ sudo apt-get install iptraf iptraf-ng 

$ sudo iptraf-ng 
```
![iptraf command line](/imgs/raspberrypi/MonitorBandwidth/iftraf.png?raw=true)

4. nethogs
----------
> nethogs is a small 'net top' tool that shows the bandwidth used by individual processes and sorts the list putting the most intensive processes on top. In the event of a sudden bandwidth spike, quickly open nethogs and find the process responsible. Nethogs reports the PID, user and the path of the program.
```
# fedora or centos (from epel)
$ sudo yum install nethogs -y 

# ubuntu or debian (default repos)
$ sudo apt-get install nethogs

$ sudo nethogs 
```
![nethogs command line](/imgs/raspberrypi/MonitorBandwidth/nethogs.png?raw=true)

5. bmon
-------
> bmon (Bandwidth monitor) is a tool similar to nload that shows the traffic load over all the network interfaces on the system. The output also consists of a graph and a section with packet level details.
```
# fedora or centos (from repoforge)
$ sudo yum install bmon 

# ubuntu or debian 
$ sudo apt-get install bmon 

$ sudo bmon
```
![bmon command line](/imgs/raspberrypi/MonitorBandwidth/bmon.png?raw=true)

6. slurm
--------
> slurm is 'yet' another network load monitor that shows device statistics along with an ascii graph. It supports 3 different styles of graphs each of which can be activated using the c,s and I keys. Simple in features, slurm does not any further details about the network load.
```
# fedora or centos 
$ sudo yum install slurm -y 

# debian or ubuntu 
$ sudo apt-get install slurm

$ sudo slurm -s -i wlan0
```
![slurm command line](/imgs/raspberrypi/MonitorBandwidth/slurm.png?raw=true)

7. tcptrack
-----------
> tcptrack is similar to iftop, and uses the pcap library to capture packets and calculate various statistics like the bandwidth used in each connection. It also support the standard pcap filters that can be used to monitor specific connections.
```
# fedora, centos (from repoforge repository)
$ sudo yum install tcptrack 

# ubuntu, debian 
$ sudo apt-get install tcptrack 

$ sudo tcptrack -i wlan0
```
![tcptrack command line](/imgs/raspberrypi/MonitorBandwidth/tcptrack.png?raw=true)

8.vnstat 
--------
> vnstat is bit different from most of the other tools, it actualy runs a background service/daemon and keeps recording the size of data transfer all the time. Next it can be to generate a report of history of network usage.
```
# fedora or centos (from epel)
$ sudo yum install vnstat 

# ubuntu or debian 
$ sudo apt-get install vnstat 

$ sudo service vnstat status 

# Monitor the bandwidth usage in realtime, use the '-l' option (live mode). It would then show the total bandwidth used by incoming and outgoing data, but in a very precise manner without any internal detail about host connections or processes.
$ vnstat -l -i wlan0

# vnstat is more like a tool to get historic reports of how much bandwidth is used everyday or over the past month. it is not strctly a tool for monitoring the network in real time.
```

9. bwm-ng
> bwm-ng (Bandwidth monitor next generation) is another very simple real time network load monitor that reports a summary of the speed at which data is being trasferred in and out of all available network interfaces on the system.
```
# fedora or centos (from epel)
$ sudo yum install bwm-ng 

# ubuntu or debian 
$ sudo apt-get install bwm-ng 
```
![bwm-ng command line](/imgs/raspberrypi/MonitorBandwidth/bwm-ng.png?raw=true)

10. cbm - Color Bandwdith meter 
-------------------------------
> A tiny little bandwidth monitor that siplays the traffic volume through network interfaces. No further options, just the traffic stats are display and updated in realtime.
```
# fedora or centos (from epel)
$ sudo yum install cbm

# ubuntu or debian 
$ sudo apt-get install bcm 
```
![cbm command line](/imgs/raspberrypi/MonitorBandwidth/cbm.png?raw=true)

11. speedometer 
---------------
> Another small and simple tool that just draws out good looking graphs of incoming and outgoing traffic through a given interface.
```
# fedora or centos (from epel)
$ sudo yum install speedometer 

# ubuntu or debian 
$ sudo apt-get install speedometer
```
![speedometer command line](/imgs/raspberrypi/MonitorBandwidth/speedometer.png?raw=true)

12. pkstat 
----------
> pkstat displays all the active connections in real time, and the speed at which data is being transferred through them. It also displays the type of the connection,i.e.tcp or udp and also details about http requests if involved.
```
# fedora or centos (from epel)
$ sudo yum install pktstat

# ubuntu or debian 
$ sudo apt-get install pktstat
```
![pktstat command line](/imgs/raspberrypi/MonitorBandwidth/pktstat.png?raw=true)

13. netwatch 
------------
> netwatch is part of the netdiag collection of tools, and it too displays the connections between local host and other remote hosts, and the speed at which data is transferring on each connection.
```
# fedora or centos (from epel)
$ sudo yum install netdiag

# ubuntu or debian 
$ sudo apt-get install netdiag
```
![netwatch command line](/imgs/raspberrypi/MonitorBandwidth/netwatch.png?raw=true)

