Aria2 on Raspberry Pi
=====================

* aria2 - The next generation download utility.
> aria2 is a lightweight multi-protocol & multi-source command-line download utility. It supports HTTP/HTTPS,FTP,BitTorrent and Metalink. aria2 can be manipulated via built-in JSON-RPC and XML-RPC interfaces.,w
```
# Step 1 -- Install Aria2 
$ sudo apt-get update 
$ sudo apt-get install aria2 

# Step 2 -- Folders for the Aria2 config file
$ mkdir -p ~/aria2/log/
$ mkdir -p ~/aria2/conf/
$ mkdir -p ~/aria2/ses/
$ touch ~/aria2/ses/aria2.session

$ Step 3 -- Configuration file 
$ vim ~/aria2/conf/aria2.conf 

#####files 
# The directory to store the downloaded file
dir=/home/pi/Downloads

# Specify file allocation method. none doesn't pre-allocate file space. prealloc pre-allocates file space before download begins. This may take some time depending on the size of the file. If you are using newer file systems such as ext4 (with extents support), btrfs, xfs or NTFS(MinGW build only), falloc is your best choice. It allocates large(few GiB) files almost instantly. Don't use falloc with legacy file systems such as ext3 and FAT32 because it takes almost same time as prealloc and it blocks aria2 entirely until allocation finishes. falloc may not be available if your system doesn't have posix_fallocate(3) function. trunc uses ftruncate(2) system call or platform-specific counterpart to truncate a file to a specified length.
# Possible Values: none, prealloc, trunc, falloc Default: prealloc
file-allocation=falloc

# Continue downloading a partially downloaded file. Use this option to resume a download started by a web browser or another program which downloads files sequentially from the beginning. Currently this option is only applicable to HTTP(S)/FTP downloads
continue=true

# Run as daemon. The current working directory will be changed to / and standard input, standard output and standard error will be redirected to /dev/null. Default: false
daemon=true

# Enable disk cache. If SIZE is 0, the disk cache is disabled. This feature caches the downloaded data in memory, which grows to at most SIZE bytes. The cache storage is created for aria2 instance and shared by all downloads. The one advantage of the disk cache is reduce the disk I/O because the data are written in larger unit and it is reordered by the offset of the file. If hash checking is involved and the data are cached in memory, we don't need to read them from the disk. SIZE can include K or M (1K = 1024, 1M = 1024K). Default: 16M
disk-cache=32M

#####logging 
# The file name of the log file. If - is specified, log is written to stdout. If empty string("") is specified, or this option is omitted, no log is written to disk at all.
log=/home/pi/aria2/log/aria2.log

console-log-level=warn 

# Set log level to output. LEVEL is either debug, info, notice, warn or error. Default: debug
log-level=notice

####downloads 
# Set the maximum number of parallel downloads for every queue item. See also the --split option. Default: 5
max-concurrent-downloads=5

# The maximum number of connections to one server for each download. Default: 1
max-connection-per-server=5
 
min-split-size=20M 

# Download a file using N connections. If more than N URIs are given, first N URIs are used and remaining URIs are used for backup. If less than N URIs are given, those URIs are used more than once so that N connections total are made simultaneously. The number of connections to the same host is restricted by the --max-connection-per-server option. See also the --min-split-size option. Default: 5
split=5
 
# Disable IPv6. This is useful if you have to use broken DNS and want to avoid terribly slow AAAA record lookup. Default: false
disable-ipv6=true

####sessions 
# Save download with - save-session option even if the download is completed or removed. This option also saves control file in that situation.
force-save=true 

# Downloads the URIs listed in FILE. You can specify multiple sources for a single entity by putting multiple URIs on a single line separated by the TAB character. Additionally, options can be specified after each URI line. Option lines must start with one or more white space characters (SPACE or TAB) and must only contain one option per line. Input files can use gzip compression. 
input-file=/home/pi/aria2/ses/aria2.session

# Save error/unfinished downloads to FILE on exit. You can pass this output file to aria2c with --input-file option on restart. If you like the output to be gzipped append a .gz extension to the file name. Please note that downloads added by aria2.addTorrent() and aria2.addMetalink() RPC method and whose meta data could not be saved as a file are not saved. Downloads removed using aria2.remove() and aria2.forceRemove() will not be saved. GID is also saved with gid, but there are some restrictions, see below.
## Normally, GID of the download itself is saved. But some downloads use meta data (e.g., BitTorrent and Metalink). In this case, there are some restrictions.
## 1.magnet URI, and followed by torrent download
##   GID of BitTorrent meta data download is saved.
## 2.URI to torrent file, and followed by torrent download
##   GID of torrent file download is saved.
## 3.URI to metalink file, and followed by file downloads described in metalink file
##   GID of metalink file download is saved.
## 4.local torrent file
##   GID of torrent download is saved.
## 5.local metalink file
##   Any meaningful GID is not saved.
save-session=/home/pi/aria2/ses/aria2.session

# Save error/unfinished downloads to a file specified by --save-session option every SEC seconds. If 0 is given, file will be saved only when aria2 exits. Default: 0
save-session-interval=10

####security 
http-auth-challenge=true 

check-certificate=false 

### RPC Options 
# Enable JSON-RPC/XML-RPC server. It is strongly recommended to set secret authorization token using --rpc-secret option. See also --rpc-listen-port option. Default: false
enable-rpc=true

# Listen incoming JSON-RPC/XML-RPC requests on all network interfaces. If false is given, listen only on local loopback interface. Default: false
rpc-listen-all=true

rpc-secret=*<YOUR TOKEN>*

# Add Access-Control-Allow-Origin header field with value * to the RPC response. Default: false
rpc-allow-origin-all=true
### RPC Options ###
#rpc-certificate=/home/pi/aria2/cet/aria2.pfx 

####ports 
rpc-listen-port=6800

####others
summary-interval=120 
enable-dht=true

####times 
# Set timeout in seconds. Default: 60
timeout=600

# Set number of tries. 0 means unlimited. See also --retry-wait. Default: 5
max-tries=10

# Set the seconds to wait between retries. When SEC > 0, aria2 will retry downloads when the HTTP server returns a 503 response. Default: 0
retry-wait=30
  
## FTP Specific Options
## Use the passive mode in FTP. If false is given, the active mode will be used. Default: true
#ftp-pasv[=true|false]
 
## Stop BitTorrent download if download speed is 0 in consecutive SEC seconds. If 0 is given, this feature is disabled. Default: 0
#bt-stop-timeout=<SEC>
## Set max overall upload speed in bytes/sec. 0 means unrestricted. You can append K or M (1K = 1024, 1M = 1024K). To limit the upload speed per torrent, use --max-upload-limit option. Default: 0
max-overall-upload-limit=512

### Advance ### 
## iptables -I INPUT -p tcp --dport 6800 -j ACCEP

# Step 04 - Testing configurations 
> Change daemon to fasle and console-log-level to info in the config file and save it.
$ sudo aria2c --conf-path="/home/pi/aria2/conf/aria2.conf"
11/10 23:08:54 [INFO] <<--- --- --- ---

11/10 23:08:54 [INFO]   --- --- --- ---

11/10 23:08:54 [INFO]   --- --- --- --->>

11/10 23:08:54 [INFO] aria2 1.33.1

11/10 23:08:54 [INFO] gcc 7.2.0
  built by  aarch64-unknown-linux-gnu
  on        Jan  5 2018 16:55:22

11/10 23:08:54 [INFO] Linux 4.15.0-1049-raspi2 #53-Ubuntu SMP PREEMPT Wed Oct 2 01:04:00 UTC 2019 aarch64

11/10 23:08:54 [INFO] zlib/1.2.11 libxml2/2.9.4 sqlite3/3.21.0 GnuTLS/3.5.8 nettle GMP/6.1.2 c-ares/1.13.0

11/10 23:08:54 [INFO] Logging started.

11/10 23:08:54 [INFO] Checking configured addresses

11/10 23:08:54 [INFO] Not considered: 127.0.0.1

11/10 23:08:54 [INFO] Found configured address: 192.168.31.156

11/10 23:08:54 [INFO] Found configured address: 172.17.0.1

11/10 23:08:54 [INFO] Not considered: ::1

11/10 23:08:54 [INFO] Not considered: fe80::ba27:ebff:fe89:8885%wlan0

11/10 23:08:54 [INFO] IPv4 configured=1, IPv6 configured=0

11/10 23:08:54 [INFO] CUID#8 - Using port 6800 for accepting new connections

11/10 23:08:54 [NOTICE] IPv4 RPC: listening on TCP port 6800

11/10 23:08:54 [INFO] 133 certificate(s) were imported.
                                                                                                                              
11/10 23:09:05 [NOTICE] Serialized session to '/home/pi/aria2/ses/aria2.session' successfully.

11/10 23:09:05 [NOTICE] Shutdown sequence commencing... Press Ctrl-C again for emergency shutdown.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================

11/10 23:09:05 [NOTICE] Serialized session to '/home/pi/aria2/ses/aria2.session' successfully.

Change back the configs (daemon to true and console-log-level to warn) and save the file.

# Step 5 - Adding aria2 to as a systemd service 
$ sudo vim /etc/systemd/system/aria2.service 

[Unit]
Description=Aria2c Download Manager 
Requires=network.target 
After=dhcpcd.service 

[Service]
Type=forking
RemainAfterExit=yes
ExecStart=/usr/bin/aria2c --conf-path=/home/pi/aria2/conf/aria2.conf 
ExecReload=/usr/bin/kill -HUP $MAINPID
ExecStop=/usr/bin/kill -s STOP $MAINPID
RestartSec=1min
Restart=on-failure

[Install]
WantedBy=multi-user.target

$ sudo systemctl start|stop|restart|status aria2 
● aria2.service - Aria2c Download Manager
   Loaded: loaded (/etc/systemd/system/aria2.service; disabled; vendor preset: enabled)
   Active: active (running) since Sun 2019-11-10 23:15:00 HKT; 5s ago
  Process: 7199 ExecStart=/usr/bin/aria2c --conf-path=/home/pi/aria2/conf/aria2.conf (code=exited, status=0/SUCCESS)
 Main PID: 7200 (aria2c)
    Tasks: 1 (limit: 1056)
   CGroup: /system.slice/aria2.service
           └─7200 /usr/bin/aria2c --conf-path=/home/pi/aria2/conf/aria2.conf

Nov 10 23:15:00 RPi3B systemd[1]: Starting Aria2c Download Manager...
Nov 10 23:15:00 RPi3B systemd[1]: Started Aria2c Download Manager.

# Step 6 - Aria2 at startup 
$ sudo systemctl enable aria2
Created symlink /etc/systemd/system/multi-user.target.wants/aria2.service → /etc/systemd/system/aria2.service.

# Step 7 starting Nginx 
$ sudo systemctl enable nginx 

# Step 8 - Getting aria2 Web UI 
$ cd /usr/local/nginx/html/   # Go to the folder which nginx servers the web pages 
$ sudo git clone https://github.com/ziahamza/webui-aria2.git 

Now Access your aria2 service through a Web-UI from any device in your LAN.You need to enter your token Which you genrated in Step 03-07 into Setting -> Connection Setting -> Enter the secret token.
```
* webui-aria2 
> The aim for webui-aria2 is to create the worlds best and hottest interface to interact with aria2. Very simple to use, just donwload and open index.html in any web browser.
![Aria2 WebUI](/imgs/raspberrypi/Aria2WebUI.png?raw=true)