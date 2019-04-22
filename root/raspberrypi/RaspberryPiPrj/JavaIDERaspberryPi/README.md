Java IDE on Raspberry Pi
========================

Install OpenJDK 8 on Debian 9 Stretch
-------------------------------------

> Java Development Kit or JDK is used by Java Programmers all over the world. Java is a compiled language. But unlike C/C++, Java compiles Java source code into Java byte code. The JVM (Java Virtual Machine) then runs the Java byte code. Java byte code is not anything like C/C++ compiled binaries, which require recompilation when needed to run on different machine and operating systems. The Java byte code id the same no matter when operating system or machine you use to generate it. The only difference is the JVM. The JVM is operating system and machine specific. The JVM reads the Java byte code and converts it into machine specific codes and then runs it on that particular machine and operating system.

> There are 2 implementations of JDK. One is called the Oracle JDK and the other one is OpenJDK. OpenJDK is totally open source and it does not include any proprietary component of Oracle JDK. The licese of Oracle JDK and OpenJDK are not same either. Oracle JDK is more restrictive than OpenJDK. For those looking for a free and open source version of JDK, OpenJDK is the best choice for them.You won't really see much of a difference when you run OpenJDK. The experience is almost the same. You can use exactly the same command line utilities with OpenJDK as with Oracle JDK. It is really easy to install OpenJDK 8 and Debian 9 Stretch beacuse it is already on the official repository of Debian 9 Stretch.

```
First update the package repository cache of your Debian 9 operating system 
$ sudo apt-get update 

There are two versions of OpenJDK 8 on Debian 9 Stretch official repository. One is OpenJDK 8 headless and the other one is OpenJDK 8.

The difference between OpenJDK 8 headless and OpenJDK 8 is that OpenJDK 8 headless does not install any libraries for working with graphical user interfaces. It has less dependencies. So it is perfect for headless servers where you never need any graphical user interfaces (GUIs). The OpenJDK 8 provides everything that OpenJDK 8 headless provides along with libraries that are required for working with graphical user interfaces(GUIs). 

$ sudo apt-get install openjdk-8-jdk-headless 
or 
$ sudo apt-get install openjdk-8-jdk 

Check if OpenJDK 8 is installed correctly
$ javac -version 
$ java -version 
```

Install Tomcat 8.5 on Debian 9
------------------------------

> Apache Tomcat is an open source application server which supports Java Servlet, JavaServer Pages, Java Expression Language and Java WebSocket technologies. It is one of the most widely used application and web server in the world today.

```
Prerequisties:
# wget utility download the Tomcat; unzip extract the downloaded archive 
$ sudo apt install unzip wget 

Download Tomcat 
$ wget http://www-us.apache.org/dist/tomcat/tomcat-8/v8.5.40/bin/apache-tomcat-8.5.40.tar.gz
$ tar -xzvf apache-tomcat-8.5.40.tar.gz && mv apache-tomcat-8.5.40 /usr/local/ 

Update Permissions 
# make the scripts inside bin directory executable:
$ sudo sh -c 'chmod +x /usr/local/apache-tomcat-8.5.40/bin/*.sh'

Create a systemd unit file 
- Create a new tomcat.service unit file in the /etc/systemd/system/ directory with the following contents:

Create a systemd Service File
Tomcat needs to know where Java is installed. This path is commonly referred to as "JAVA_HOME". 

[Unit]
Description=Apache Tomcat 8.5.40 Web Application Container 
After=network.target 

[Service]
Type=forking 
User=pi
Group=pi
Environment=JAVA_HOME=/usr/local/jdk1.8.0_191
Environment=CATALINA_PID=/usr/local/apache-tomcat-8.5.40/temp/tomcat.pid
Environment=CATALINA_HOME=/usr/local/apache-tomcat-8.5.40
Environment=CATALINA_BASE=/usr/local/apache-tomcat-8.5.40
Environment='CATALINA_OPTS=-Xms512M -Xmx1024M -server -XX:+UseParallelGC'
Environment='JAVA_OPTS=-Djava.awt.headless=true -Djava.security.egd=file:/dev/./urandom'

ExecStart=/usr/local/apache-tomcat-8.5.40/bin/startup.sh 
ExecStop=/usr/local/apache-tomcat-8.5.40/bin/shutdown.sh 

RestartSec=10
Restart=always 

[Install]
WantedBy=multi-user.target

Next, reload the systemd daemon so that it knows about our service file:
$ sudo systemctl daemon-reload 

Start the Tomcat service by typing 
$ sudo systemctl start tomcat 

Double check that it started without errors by typing 
$ sudo systemctl status tomcat 

Enable the service file so that Tomcat automatically starts at boot.
$ sudo systemctl enable tomcat 

Configure Tomcat Web Management Interface 

# add a login to our Tomcat server. add a user who can access the manager-gui, admin-gui
$ sudo vim /usr/local/apache-tomcat-8.5.40/conf/tomcat-users.xml 

# By default, newer versions of Tomcat restrict access to the Manager and Host Manager apps to connections coming from the server itself. We will probably want to remove or alter this restriction. To change the IP address restrictions on these, open the appropriate context.xml files.

# For the Manager app, type: 
$ sudo vim /usr/local/apache-tomcat-8.5.40/webapps/manager/META-INF/context.xml 

# For the Host Manager app, 
$ sudo vim /usr/local/apache-tomcat-8.5.40/webapps/host-manager/META-INF/context.xml 

Inside, comment out the IP address restriction to allow connections from anywhere, ALternatively, if you would like to allow access only to connections comming from your own IP address, you can add your public IP address to the list:
	
	<!--
	<Value className="org.apache.catalina.valves.RemoteAddrValue" allow="127\.\d+\.\d+\.\d+|::1|0:0:0:0:0:0:0:1" />
	-->

To put our changes into effect, restart the Tomcat service:
$ sudo systemctl restart tomcat

Access the Web Interface 
Open in web browser: http://server_domain_or_IP:8080 

Access Manager APP, accessible via the link http://server_domain_or_IP:8080/manager/html 
The Web Application Manager is used to manage your Java applications. You can Start, Stop, Reload, Deploy, and Undeploy here.

Access Host Manager, accessible via the link http://server_domain_or_IP:8080/host-manager/html/
```

Conclusion
----------
```
Currently, your Tomcat installation is functional, but entirely unencrypted. This means that all data, including sensitive items like passwords, are sent in plain text that can be intercepted and read by other parties on the internet. In order to prevent this from happending, it is strongly recommended
```

"""CREATE TABLE `history_{0}` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`JSID` int(11) DEFAULT NULL,
	`XGRQ` datetime DEFAULT NULL COMMENT 'Modified date',
	`Code` varchar(20) DEFAULT NULL COMMENT 'Stock code (not include market suffix)',
	`RECID` int(11) DEFAULT NULL ,
	`Seid` int(11) DEFAULT NULL ,
	`StockCode` varchar(20) DEFAULT NULL COMMENT 'Stock code (include market suffix)',
	`StockAbbr` varchar(20) DEFAULT NULL COMMENT 'Stock code short name',
	`BargainDate` datetime DEFAULT NULL COMMENT 'Bargain DateTime',
	`BargainTime` varchar(20) DEFAULT NULL COMMENT 'Bargain Time',
	`PrevClosePrice` decimal(20,4) DEFAULT NULL COMMENT 'Prev Close Price',
	`OpenPrice` decimal(20,4) DEFAULT NULL COMMENT 'Open Price',
	`ClosePrice` decimal(20,4) DEFAULT NULL COMMENT 'Close Price',
	`HighPrice` decimal(20,4) DEFAULT NULL COMMENT 'High Price',
	`LowPrice` decimal(20,4) DEFAULT NULL COMMENT 'Low Price',
	`AccuBargainAmount` decimal(20,4) DEFAULT NULL COMMENT 'Accumulate Transaction Amount',
	`AccuBargainSum` decimal(20,4) DEFAULT NULL COMMENT 'Accumulate Transaction ',
	`AccuTurnoverDeals` decimal(20,4) DEFAULT NULL,
	`PE1` decimal(20,4) DEFAULT NULL,
	`PE2` decimal(20,4) DEFAULT NULL,
	`ChangePCT1` decimal(20,4) DEFAULT NULL,
	`ChangePCT2` decimal(20,4) DEFAULT NULL,
	`OpenInterest` int(11) DEFAULT NULL,
	`Buy1Price` decimal(20,4) DEFAULT NULL,
	`Buy1Amount` decimal(20,4) DEFAULT NULL,
	`Buy2Price` decimal(20,4) DEFAULT NULL,
	`Buy2Amount` decimal(20,4) DEFAULT NULL,
	`Buy3Price` decimal(20,4) DEFAULT NULL,
	`Buy3Amount` decimal(20,4) DEFAULT NULL,
	`Buy4Price` decimal(20,4) DEFAULT NULL,
	`Buy4Amount` decimal(20,4) DEFAULT NULL,
	`Buy5Price` decimal(20,4) DEFAULT NULL,
	`Buy5Amount` decimal(20,4) DEFAULT NULL,
	`Sell1Price` decimal(20,4) DEFAULT NULL,
	`Sell1Amount` decimal(20,4) DEFAULT NULL,
	`Sell2Price` decimal(20,4) DEFAULT NULL,
	`Sell2Amount` decimal(20,4) DEFAULT NULL,
	`Sell3Price` decimal(20,4) DEFAULT NULL,
	`Sell3Amount` decimal(20,4) DEFAULT NULL,
	`Sell4Price` decimal(20,4) DEFAULT NULL,
	`Sell4Amount` decimal(20,4) DEFAULT NULL,
	`Sell5Price` decimal(20,4) DEFAULT NULL,
	`Sell5Amount` decimal(20,4) DEFAULT NULL,
	PRIMARY KEY (`id`),
	KEY `ix_{0}_BargainDate` (`BargainDate`),
	KEY `ix_{0}_Code` (`Code`)) 
	ENGINE=InnoDB DEFAULT CHARSET=utf8
	"""


CREATE TABLE `asharecalendar` (
  `OBJECT_ID` varchar(100) NOT NULL DEFAULT '' COMMENT '对象ID',
  `TRADE_DAYS` varchar(12) DEFAULT NULL COMMENT '交易日',
  `S_INFO_EXCHMARKET` varchar(60) DEFAULT NULL COMMENT '交易所英文简称',
  `OPDATE` datetime DEFAULT NULL,
  `OPMODE` varchar(1) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`OBJECT_ID`),
  KEY `index_trade_days` (`TRADE_DAYS`),
  KEY `index_s_info_exchange` (`S_INFO_EXCHMARKET`)
) ENGINE=InnoDB DEFAULT CHARSET=gbk




