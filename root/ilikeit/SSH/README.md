SSH TUNNELLING
==============

Local vs Remote SSH port forwarding
-----------------------------------
```
* Local Port Forwarding: relay a port from a remote server to your local machine with **ssh -L** (-L: forward to local machine)
    - For Example: If your rmeote server has a MySQL database daemon listening on port 3306 and you want to access this daemon from your local computer.
    # Remote MySQL server (remote port 3306) to local machine on local port 5000:
    $ ssh -L 5000:remote_ip:3306 -p xx user@remote_ip 

# Local port forwarding (Make a remote port available locally)
# In this example, make a remote MySQL Server (Port 3306) available on our local computer on port 5000
$ ssh -L [<LocalAddress>]:<LocalPort>:<RemoteHost>:<RemotePort> sshUser@remoteServer
    LocalAddress: The local address is an optional parameter, If you do not specify it. the remote port will be bound locally to all interfaces(0.0.0.0). SO you can also only bind it locally to your 127.0.0.1 (on your local machine).
    LocalPort: The port on your local machine where the whole thing should be reachable 
    RemoteHost: This specifies on which interface inside the remote server(remoteServer) the daemon is listening on.
    RemotePort: This is the actual port on the remote machine (remoteServer) you want to relay to your local machine.
    sshUser: This is the SSH username you have on the remote server 
    remoteServer: The address (IP or hostname) by which your remote server is reachable via ssh.

# Check all interface for Port 
$ netstat -an | grep 3306 | grep LISTEN 

* Remote Port Forwarding: make your local port available on a remote server with **ssh -R** (-R: forward to remote machine)
    - For Example: If your want to make your local web-srever available on a port of a public server. So that someone can quickly check what your local web-server provides without having to deploy it somewhere publicly.
    # Local web-server (local port 80) to rmeote server on remote port 5000:
    $ ssh -R 5000:localhost:80 -p xx user@remote_ip 

# Remote port forwarding (Make a local port available remotely)
# In this exmaple we are going to make our local web-server(Port 80) available on a remote server on Port 5000.
$ ssh -R [<RemoteAddress>]:<RemotePort>:<LocalHost>:<LocalPort> sshUser@remoteServer 
    RemoteAddress: The remote address is an optional parameter. If you do not specify it, the remote port will be bound remotely (on remoetServer) to all interfaces(0.0.0.0). So you can also only bind it remotely to a specific interface.
    RemotePort: The port on your remote server (remoteServer) where the whole thing should be reachable 
    LocalHost: This sepcifies on whic interface inside your local computer the daemon is listening on.
    LocalPort: This is the actual port on your local machine you want to relay to the remote server (remoteServer)
    sshUser: This is the SSH username you have on the remote server 
    remoteServer: The address (IP or hostname) by which your remote server is reachable via ssh.
$ ssh -R remote_ip:5000:localhost:8080 -p xx user@remote_ip 
# You can now simply reach your local webserver via http://remote_ip:5000

# Enabled GateWayPorts option (on remote server):
$ vim /etc/ssh/ssh_config 
GatewayPorts yes 

# Ports below 1024 
#Every system user can allocate ports above and including 1024 (high ports). Ports below that require root privileges.

# As allocate a low port on your local machine, you must either do that as root(locally) or with sudo (locally)
$ sudo ssh -L 10:remote_ip:3306 -p xx user@remote_ip 

# As you allocate a low port on the remote server, you will need to ssh into the machine as root 
$ ssh -R 10:localhost:8080 -p root@remote_ip 
```

TUNNEL OPTIONS
--------------
```
$ ssh -L 5000:remote_ip:3306 -p xx user@remote_ip 
# Once executed the above command, a tunnel is established. However, you will also be logged in into the remote server with a SSH session. If you simply want to do some port forwarding you will not need or might not event want to remote login session.You can disable it via -N, Which is a very common option for SSH tunnels:
$ ssh -N -L 5000:remote_ip:3306 -p xx user@remote_ip 
    -N: connect just hang there(you won't get a shell prompt)
# So if you are not going to execute remote commands and will not need a login sheel, you also do not need to request a pseudo terminal in the first place.
$ ssh -T -N -L 5000:remote_ip:3306 -p xx user@remote_ip 
    -T: Disable pseudo-terminal allocaton.

# Note: Be aware that this example requires private/public key authentication as cron will not be able to enter passwords.
$ ssh -f -T -N -L 5000:remote_ip:3306 -p xx user@remote_ip 
    -f: Requests ssh to go to background just before command execution.

# SSH tunnel on a non-standard port
# What if the SSH server is listening on a non-standard port(not tcp 22). You can always add a port option.
$ ssh -T -N -L 5000:remote_ip:3306 -p xx user@remote_ip 
    -p : Port to connect to on the remote host

# SHH tunnel with a non standard private key.
# If not explicitly, SSH will look for a file called ~/.ssh/id_rsa. In this case however, you file is called ~/.ssh/id_rsa-cytopia@remove_ip. So you will also pass this information to the tunnel command.
$ ssh -T -N -L 5000:remote_ip:3306 -p xx user@remote_ip -i ~/.ssh/id_rsa-cytopia@remote_ip

# SSH tunnel via SSH config 
# Adding user and host 
$ vim ~/.ssh/config 
    Host remote-mysql-tunnel
        HostName remote_ip
        User    username 
        Port    xxx 
        IdentityFile ~/.ssh/id_rsa 
        LocalForward 5000 remote_ip:3306 
# create an alias remote for host remote_ip with user username . Now command can be written like this
$ ssh -T -N -L remote-mysql-tunnel 
```

AUTOSSH
-------
```
Make a tunnel persistent. By persistent I mean, that it is made sure the tunnel will always run.For example, Once you ssh connection times out(By server-side timeout), your tunnel should be re-established automatically.

$ autossh -M 0 -o "ServerAliveInterval 30" -o "ServerAliveCountMax 3" -L 5000:remote_ip:3306 -p xx user@remote_ip -i ~/.ssh/rsa_ip 

# AutoSSH is a prpgram to start a copy of ssh and monitor it, restarting it as necessary should it die or stop passing traffic.
$ sudo apt-get install autossh 

# Basic usage:
usage: autossh [-V] [-M minitor_port[:echo_port]] [-f] [SSH_OPTIONS]
    -V: simply displays the version and exits 
    -f: run in backgrounds
    -M: minitoring port, AutoSSH will continuously send data back and forth through the pair of monitoring ports in order to keep track of an extablished connection. The specified monitoring and the port directly above (+1) must be free. The first one is used to send data and the one above to receive data on. 
    
    Unfortuately, this is not too handy, as it must be made sure both ports(the specified one and the one directly above) a free (not used). So in order to overcome this problem, there is a better solution.

$ autossh -T -N -L 5000:remote_ip:3306 -p xx user@remote_ip -i ~/.ssh/id_rsa-cytopia@remote_ip
# Make sure you use public/private key authentification instead of password-based authentification when you use -f. Because in a background run a passphrase cannot be entered interactively.

# ServerAliveInterval and ServerAliveCountMax - they cause the SSH client to send traffic through the encrypted link to the server. This will keep the connection alive when there is no other activity and also when it does not receive any alive data,it will tell AutoSSH that the connection is broken and AutoSSH will then restart the connection.

$ autossh -M 0  # disable the built-in AutoSSH monitoring port by giving it a value of 0

# Additionally you will also have to specify values for ServerAliveInterval and ServerAliveCountMax 
$ autossh -M 0 -o "ServerAliveInterval 30" -o "ServerAliveCountMax 3"

# So Now the complete tunnel command will look like this:
$ autossh -M 0 -o "ServerAliveInterval 30" -o "ServerAliveCountMax 3" -L 5000:remote_ip:3306 -p xx user@remote_ip -i ~/.ssh/id_rsa-cytopia@remote_ip
    ServerAliveInterval: number of seconds that the client will wait before sending a null packet to the server (to keep the connection alive)
    ServerAliveCountMax: Sets the number of server alive messages which may be sent without ssh receiving any messages back from the server. If this threshold is reached while server alive messages are being sent, ssh will disconnect from the server, terminating the session.

# AutoSSH and ~/.ssh/config 
$ vim ~/.ssh/config 
    Host remote-mysql-tunnel
        HostName remote_ip
        User    username 
        Port    xxx 
        IdentifyFile ~/.ssh/id_rsa 
        LocalForward 5000 remote_ip:3306 
        ServerAliveInterval 30 
        ServerAliveCountMax 3 

# If you recall all the ssh options we had used already, we can not simply start the autossh tunnel like so:
$ autossh -M 0 -f -T -N remote-mysql-tunnel 

# AutoSSH environment variables 
# AutoSSH can also be controlled via a couple of environment variables. Those are useful if you want to run AutoSSH unattended via cron.using shell scripts or during boot time with the help of systemd services.
    AUTOSSH_GATETIME: How long ssh must be up before we consider it a successful connection. Default is 30 seconds. If set to 0, then this behaviour is disabled. and as well, autossh will retry even on failure of first attempt to run ssh.

# Create SSH key and upload id.pub file
$ ssh-keygen -t 'rsa' -C 'vps@goku163'
$ ssh-copy-id -p [vps ssh port] vps@[vps public ip]
$ ssh-copy-id -i ~/.ssh/id_rsa.pub -p 22 vps@public ip

# AutoSSH during boot with systemd 
# if you want a permanent SSH tunnel already created during boot time, You will have to create a systemd service and enable it. There is however an important thing to note about systemd and AutoSSH.
$ sudo vim /etc/systemd/system/autossh.service
[Unit]
Description=Keeps a tunnel service everything
After=network.target

[Service]
User=pi
Type=simple
# How long ssh must be up before we consider it a successful connection. Default is 30 seconds. If set to 0, this behaviour is disabled. and as well, autossh will retry even on failure of first attempt to run ssh
Environment="AUTOSSH_GATETIME=0"
ExecStart=/usr/bin/autossh -M 0 -o "ServerAliveInterval 30" -o "ServerAliveCountMax 3" -NR '*:xxxx:localhost:xx' user@           remote_ip -p xx
ExecReload=/bin/kill -HUP $MAINPID
KillMode=process
Restart=always

[Install]
WantedBy=multi-user.target


# Notice here that the general definitions are at the very top and more wildcarded definitions (using the asterisk *) are followed below.
# If you want to ssh connect to c1 (ssh c1), the file is read as follows:
    1. Find section Host c1 and use its corresponding HostName (192.168.0.1)
    2. Find more general section Host c* and use their values (User, Port, etc).
    3. Find most general section Host * 
        i. Don't use User as it has already been defined for this connection in c* 
        ii. Don't use Port as it has already been defined for this connection in c* 
        iii. Don't use PubkeyAuthentication as it has already been defined for this connection in c* 
        iv. User ServerAliveInterval as there is no previous definition.

# So from that you must always remember that whenever a specific value has been found, it cannot be overwritten by values definied below.

$ vim ~/.ssh/config 
Host RPi3BPlus
    HostName 192.168.31.127

Host RPi3B
    HostName 192.168.31.156

Host RPi2B
    HostName 192.168.31.138

Host RPi*
    User pi
    Port 22
    PubkeyAuthentication yes
    IdentityFile ~/.ssh/id_rsa

# Identity leak via ssh keys 
# be aware that once you connect to any ssh server, all of your public keys that are hold by your ssh-agent, are sent to this server.
# Recommends is to turn off public key autentification in general and explicitly turn it on per host (where u need it):

# Securing know_hosts 
[104.xx.xx.31]:26861 ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBGIBuui0UwpqdYTb5Sv3Sj+            Uykp9LsnkHvF8yS7ilavqLndRsSIvhiRVjTVF+/BA=
# So in order to only store hashes of the hostname inside ~/.ssh/known_hosts, you will need to alter ~/.ssh/config 
Host *
    HashKnownHosts yes 
# The hashed version for the file will look like this:
|1|YZ1Z68Ka8xv9JeMmIfPfsi3+Y7I=|xK0ZsRUZ7AXndnBGs0kuuLLOes
    Note 1: Keep in mind that the hashing will start from now on and previous entries will not be hashed 
    Note 2: With hashing you will loose the autocompletion feature from known_hosts, but when you use aliase, you still have the alias based autocompletion described above.

# Multiple connections inside a single one 
# There is a way to reduce it by multiplexing multiple ssh connections over a single one from the same host/user by re-using an already established connection.
$ vim ~/.ssh/config 

Host * 
    ControlMaster auto 
    ControlPath ~/.ssh/sockets/%r@%h-%p
    ControlPersist 600 


ControlMaster: Tell SSH to re-use an existing connection (if there is already an established one) without having to authenticate again 
ControlPath: This is the path of the socket for open SSH connections. Every new connection will hook into this socket and can use the alredy established connection.
ControlPersist: Keep the master (the first) SSH connection open for X seconds after the last connection has been closed.This means you have X seconds to connect again without authentification after all connections have been closed to this host.

# Private ssh key leak 
# In order to avoid possible private leaks via ssh to a malicious SSH server add the following undocumented setting to your ~/.ssh/config at the bottom inside the general section 

Host * 
    UseRoaming no 

# Useful tools 
    
```
