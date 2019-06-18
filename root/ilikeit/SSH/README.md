# SSH, also known as Secure Socket Shell

## About 

SSH, is a network protocl that provides administrators with a secure way to access a remote computer. SSH also referes to the suite of utilities that implement the protocol. Secure Shell provides strong **authentication** and secure **encrypted** data communications between two computers connectingover an insecure network such as the Internet. 

SSH uses the **client-server model**, connecting a secure shell client application, the end at whcih the session is displayed, with an SSH server

**OpenSSH** is the premier connectivity tool for remote login with the SSH protocol. OpenSSH provides a large suite of secure tunneling capabilities, several authentication methods, and sophisticated configuration options.

### How Does SSH Work 

ssh - OpenSSH SSH client (remote login program)

The SSH protocol employs a **client-server** model to authenticate two parties and encrypt the data between them.

**server** component listens on a designated port for connections. It is responsible for negotiating the secure connection, authenticating the connecting party, and spawning the correct environment if the credentials are accepted. 

**client** is responsible for beginning the initial TCP handshake with the server, negotiating the secure connection, verifying that the server's identity matches previously recorded information, and providing credentials to authenticate.

An **SSH session** is established in two separate stages.
    1. Negotiating Encryption for the Session 
    2. Authenticating the User's Access to the Server 


```
# 远程登陆
$ ssh [-p port] [user@]hostname [command] 
```

### 中间人攻击

SSH之所以能够保持安全，原因在于采用公钥加密。

整个流程是：
    1. 远程主机收到用户登陆请求，把自己的公钥发给用户
    2. 用户使用远程主机的公钥，将登陆密码加密后，发送给远程主机。
    3. 远程主机用自己的私钥，解密登陆密码，如果密码正确，就同意用户登陆。

这个过程本身是安全的，但是实施的时候存在一个风险，如果有人截获了登陆请求，然后冒充远程主机，将伪造的公钥发给用户，那么用户很难辨别真伪，因为不想HTTPS协议，SSH协议的公钥是没有证书中心（CA）公证的，也就是说，都是自己签发。

可以设想，如果攻击者插在用户和远程主机之间 (比如在公共wifi区域)，用伪造的公钥，获取用户的登陆密码。再用这个密码登陆远程主机，那么SSH的安全机制就有风险，这种风险就是著名的“中间人攻击”Man-in-the-middle-attack.

SSH 协议如何应对呢？

### 口令登陆

如果是第一次登陆对方主机，系统会出现下面的提示：
![第一次登陆对方主机](/imgs/os/UnixLinux/ssh_password_login.png?raw=true)

"RSA key fingerprint" 是指公钥长度较长（采用RSA算法，长达1024位），很难比较，所以对其进行MD5计算，将它变为128位的指纹，很自然一个问题就是，用户怎么知道主机的公钥指纹应该是多少？没有好办法，远程铸就必需在自己的网站上贴出公钥指纹，以便用户自行核对。

假设经过比对，用户决定接受远程主机的公钥。然后会要求输入密码。如果密码正确，就可以登陆了。

Establish a Reverse Tunnel 
--------------------------
> Establish a reverse tunnel with port forwarding in order to consistently ssh into a host behind NAT router that has a dynamic private IP.

![Reverse tunnel SSH](/imgs/os/UnixLinux/reverse_tunnel_ssh.png?raw=true)

1. Attempt to setup a reverse tunnel with port and ip forwarding. More specifically, the blue host should forward all ssh connection to it on port **2222** to the greenhost on port 22. This is done from the green host.
```
greenusr@greenhost: $ ssh -p [vps ssh port] -NR 2222:localhost:22 vps@[vps public ip]
```

2. The point of setting up the reverse tunnel is so that following command will work so as to allow the read host to into the greenhost.
```
vps@vpshost: $ ssh -p 2222 greenuser@[greenhost] 
```

3. **autossh** - is a program to start a copy of ssh and monitor it, restarting it as necessary should it die or stop passing traffic. 
```
$ sudo apt-get install autossh 
$ autossh -p [vps ssh port] -M [localhost autossh monitor port] -NR 4444:localhost:22 vps@[vps public ip] 
# **autossh** will send test data on the base monitoring port, and receive it back on the port above.

# log in vps public server
$ netstat -tunelp | grep 4444
tcp        0      0 127.0.0.1:4444          0.0.0.0:*               LISTEN      1000       485429     13063/sshd: vps
tcp6       0      0 ::1:4444                :::*                    LISTEN      1000       485428     13063/sshd: vps
```

4. add lines to **/etc/ssh/sshd_config**
```
$ sudo vim /etc/ssh/sshd_config 
# add the lines to /etc/ssh/sshd_config 
# GatewayPorts yes 
$ sudo systemctl restart sshd 
```

5. Create SSH key 
```
$ ssh-keygen -t 'rsa' -C 'vps@goku163'
$ ssh-copy-id -p [vps ssh port] vps@[vps public ip]
$ ssh-copy-id -i ~/.ssh/id_rsa.pub -p 22 vps@public ip
```

6. autossh.service (/etc/systemd/system/)
```
# autossh.service file content 
[Unit]
Description=Keeps a tunnel to 'chyidl.com' open 
After=network.target 

[Service]
User=pi 
Type=simple
# -p [PORT]
# -l [user]
# -M 0 --> no monitoring 
# -N Just open the connection and do nothing (not interactive)
ExecStart=/usr/bin/autossh -M 9527 -NR '*:4444:localhost:22' -p [vps ssh port] vps@[vps public ip] -i /home/vps/.ssh/id_rsa
ExecReload=/bin/kill -HUP $MAINPID
KillMode=process
Restart=always

[Install]
WantedBy=multi-user.target 

$ sudo systemctl enable autossh.service 
$ sudo systemctl start autossh 
```

### How can I keep SSH session from freezing? 

![](/imgs/ilikeit/SSH/ssh_connection_closed_by_remote_host.png?raw=true)

* First change on the client:
```
$ sudo vim /etc/ssh/ssh_config 

Host * 

# ServerAliveInterval: The client will send a null packet to the server every 60 seconds to keep the connection alive.
ServerAliveInterval 60 
```

* Second change on the server:
```
$ sudo vim /etc/ssh/sshd_config 

# ClientAliveInterval: The server will wait 60 seconds before sending a null packet to the client to keep the connection alive
ClientAliveInterval 60 

# TCPKeepAlive: Is there to ensure that certain firewalls don't drop idle connections.
TCPKeepAlive yes 

# ClientAliveCountMax: Server will send alive messages to the client event though it has not received any message back from the client.
ClientAliveCountMax 10000
```

* Finally restart the ssh server

```
$ sudo service ssh restart 
or 
$ service sshd restart #  depending on what system you are on.
```

Keep SSH Session Alive (resolve a ssh connection closed by remote host due to inactivity)
-----------------------------------------------------------------------------------------
> sshd (the server) closes the connection if it doesn't hear anything from the client for a while. You can tell your client to send a sign-of-life signal to the server once in a while.

> The configuration for this is in the file "~/.ssh/config", create it if the configuration file does not exist. To send the signal every four minutes (240 seconds) to the remote host, put the following in your "~/.ssh/config" file.

```
$ vim ~/.ssh/config
# add below content to the "~/.ssh/config" file
Host *
    TCPKeepAlive yes
    # ServerAliveInterval: This sets a timeout interval in seconds, which is pecified by you, from which if no packets are sent from the SSH client to the SSH server, SSH will send an encrypted request to the server for a TCP response. To make that request every 30 seconds.
    ServerAliveInterval 30 
```

Also make sure to run:
```
$ chmod 600 ~/.ssh/config 
# Because the config file must not be world-readable
```
