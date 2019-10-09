Set Up OpenVPN Server
=====================
> OpenVPN is a full-featured SSL VPN (virtual private network). it implements OSI layer 2 or 3 secure network extension using the SSL/TLS protocol. it is an open source software and distributed under the GNU GPL. A VPN allows you to connect securely to an insecure public network such as wifi network at the airport or hotel. VPN is also required to access your corporate or enterprise or home server resources. You can bypass the geo-blocked site and increase your privacy or safety online.

* Setp 1 - Update your system 
```
$ sudo apt-get update 
$ sudo apt-get upgrade 
```

* Setp 2 - Find and note down your IP address 
```
$ ip a 
$ ip a show eth0 

# A note about IP address 
Most cloud servers have two types of IP address:
    1. Public static IP address directly assigned to your box and routed from the Internet 
    2. Private static IP address directly attached to your server and your server is behind NAT with public IP address 
```

* Step 3 - Download and run openvpn-install.sh script 
```
$ wget https://git.io/vpn -O openvpn-install.sh 

# Setup permissions using the chmod command 
$ chmod +x openvpn-install.sh 

# One can view the script using a text editor such as nano/vim: 
$ vim openvpn-install.sh
```

* Run OPENVPN_INSTALL.SH TO INSTALL OPENVPN SERVER 
```
$ sudo ./openvpn-install.sh 

# To avoid problem always choose DNS as 1.1.1.1 or Google DNS. Those are fast DNS server and reached from anywhere on the internet.

# How Do I Start/Stop/Restart OPENVPN SERVER ON UBUNTU
$ sudo systemctl stop openvpn@server    # stop server 
$ sudo systemctl start openvpn@server   # start server 
$ sudo systemctl restart openvpn@server # restart server 
$ sudo systemctl status openvpn@server  # get server status 
```

* Step 4 - Connect an OpenVPN server using IOS/Linux/Mac client
    - LINUX DESKTOP: OPENVPN CLIENT 
```
# First, install the openvpn client for your desktop, enter:
$ sudo yum install openvpn 
OR
$ sudo apt install openvpn 

# Next, copy desktop.ovpn as follows: 
$ sudo cp desktop.ovpn /etc/openvpn/client.conf 

# Test connectivity from the CLI:
$ sudo openvpn --client --config /etc/openvpn/desktop.conf 

# Your Linux system will automatically connect when computer restart openvpn script/service:
$ sudo systemctl start openvpn@client   # start client service 
```

* Step 5 - Verify/test the connectivity 
```
# Execute the following commands after connecting to OpenVPN server from your Linux desktop:
$ ping 10.8.0.1     # Ping to the OpenVPN server gateway 
$ ip route  # Make sure routing setup working 
$ dig TXT +short o-o.myaddr.l.google.com @ns1.google.com    # Must return public IP address of OpenVPN server
```
