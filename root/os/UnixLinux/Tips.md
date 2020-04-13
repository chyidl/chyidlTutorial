# Tips 

* 1. How to get a list of all valid IP addresses in a local network?
```
$ sudo apt-get install nmap

$ nmap -sn 192.168.1.0/24
will scan the entire .1 to .254 range 
This does a simple ping scan in the entire subnet to see which hosts are online.
```
