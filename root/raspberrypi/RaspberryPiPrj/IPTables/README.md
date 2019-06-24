Open and ClosePorts Using IPTables 
==================================

> IPTables is the default firewall used on CentOS and RHEL systems.

* List Current Firewall Rules
    - This command lists all the current firewall rules loaded into IPTables.
```
$ iptables -L 
➜  ~ sudo iptables -L
[sudo] password for chyi:
Chain INPUT (policy ACCEPT)
target     prot opt source               destination
ACCEPT     tcp  --  anywhere             anywhere            tcp dpt:mysql
ACCEPT     all  --  anywhere             anywhere            state RELATED,ESTABLISHED
ACCEPT     icmp --  anywhere             anywhere
ACCEPT     all  --  anywhere             anywhere
ACCEPT     tcp  --  anywhere             anywhere            state NEW tcp dpt:ssh
REJECT     all  --  anywhere             anywhere            reject-with icmp-host-prohibited

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination
REJECT     all  --  anywhere             anywhere            reject-with icmp-host-prohibited

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination
```

* Open a port in IPTables -- CentOS 6 
    - $ iptables -I INPUT -p tcp -m tcp --dport 80 -j ACCEPT 
    - $ service iptables save 

* Close a port in IPTables -- CentOS 6 
    - $ iptables -I INPUT -p tcp -m tcp --dport 80 -j REJECT 
    - $ service iptables save 


* Open a port in IPTables -- CentOS 7 
    - $ firewall-cmd --zone=public --add-port=80/tcp --permanent
    - $ firewall-cmd --reload 

* Close a port in IPTables -- CentOS 7
    - $ firewall-cmd --zone=public --remove-port=80/tcp 
    - $ firewall-cmd --runtime-to-permanent 
    - $ firewall-cmd --reload 
