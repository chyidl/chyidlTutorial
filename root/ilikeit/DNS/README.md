 DNS Resolve 
 ===========
```
$ sudo vim /etc/resolv.conf 

# add two rows Google DNS Server 
nameserver 8.8.8.8
nameserver 4.4.4.4 

# Make above command effective
$ resolvconf -u 
```
