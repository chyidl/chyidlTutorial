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
- Create a new **tomcat.service** unit file in the /etc/systemd/system/ directory with the following contents:

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

# Configure Tomcat Web Management Interface 
In order to use the manager web app that comes with Tomcat, we must add a login to our Tomcat server.
# add a login to our Tomcat server. add a user who can access the manager-gui, admin-gui
$ sudo vim /usr/local/apache-tomcat-8.5.40/conf/tomcat-users.xml 
# add the manager-gui and admin-gui role to a user named tomcat with a password of s3cret, add the following to the config file listed above.   
    <role rolename="manager-gui" />
    <role rolename="manager-script" />
    <role rolename="manager-jmx" />
    <role rolename="manager-status" />
    <role rolename="admin-gui" />
    <role rolename="admin-script" />
    <user username="tomcat" password="s3cret" roles="manager-gui, manager-script, manager-jmx, manager-status, admin-gui, admin-script" />
# Save and close the file when you are finished

# By default, newer versions of Tomcat restrict access to the Manager and Host Manager apps to connections coming from the server itself. We will probably want to remove or alter this restriction. To change the IP address restrictions on these, open the appropriate context.xml files.
# For the Manager app, type: 
$ sudo vim /usr/local/apache-tomcat-8.5.40/webapps/manager/META-INF/context.xml 
	<!--
	<Value className="org.apache.catalina.valves.RemoteAddrValue" allow="127\.\d+\.\d+\.\d+|::1|0:0:0:0:0:0:0:1" />
	-->

# For the Host Manager app, 
$ sudo vim /usr/local/apache-tomcat-8.5.40/webapps/host-manager/META-INF/context.xml 
# Inside, comment out the IP address restriction to allow connections from anywhere, ALternatively, if you would like to allow access only to connections comming from your own IP address, you can add your public IP address to the list:
	<!--
	<Value className="org.apache.catalina.valves.RemoteAddrValue" allow="127\.\d+\.\d+\.\d+|::1|0:0:0:0:0:0:0:1" />
	-->

# In the above images, as you can see that I have defined serveral roles and for all these roles I hava give one single username and password.

To put our changes into effect, restart the Tomcat service:
$ sudo systemctl restart tomcat

# Access the Web Interface 
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

Run Multiple Tomcat Instances on One Server
-------------------------------------------
```
Tomcat Directory Structure
    - When creating multiple instances of tomcat server. we need to play with the folders inside the server. These folders contain the actual scripts and code for the server. 
    /bin: This directory contains the startup and shutdown scripts for both Windows and Linux.
    /conf: This directory contains the main configuration files for Tomcat. 
    /server: This directory contains the Tomcat Java Archive files.
    /lib: This directory contains Java Archive files that Tomcat is dependent upon.
    /logs: This directory contains Tomcat's log files.
    /src: This directory contains the source code used by the Tomcat server.
    /webapps: All web applications are deployed in this directory; it contains the WAR file.
    /work: This is the directory in which Tomcat will place all servlet that are generated from JSPs

Tomcat Server ports:
    Connector Port: This is the port where Apache Tomcat listen for the HTTP requests.
    Shutdown Port: This port is used when we try to shudown the Apache Tomcat Server.
    AJP (Apache JServ Protocol) Connector Port: The Apache JServ Protocol (AJP) is a binary protocol that can conduct inbound requests from a web server through to an application server that sits behind the web server.
    Redirect Port: Any redirection happening inside Apache Tomcat will happen through this port. In Apache TOMCAT there are two instance where redirect Port is mentioned. First one is for the Apache TOMCAT server and other one is for the AJP port.

Lets Start creating multiple Tomcat Instances 
    Tomcat1/ 
    Tomcat2/

Change tomcat/conf/server.xml file, HTTP, HTTPS, AJP, Shutdown Ports 

<Server port="8006" shutdown="SHUTDOWN">
  <Listener className="org.apache.catalina.startup.VersionLoggerListener" />

<Connector port="8081" protocol="HTTP/1.1"
               connectionTimeout="20000"
               redirectPort="8444" />

<!-- Define an AJP 1.3 Connector on port 8009 -->
    <Connector port="8010" protocol="AJP/1.3" redirectPort="8444" />

The **bin/startup.sh** and **bin/shutdown.sh** script files make use of **bin/catalina.sh** for performing the startup and shutdown operations. We shall edit **bin/catalina.sh** file as described below:
    a): specify following two variables in catalina.sh script file present in the bin folder of the tomcat_home 
        export CATALINA_HOME = /path/Tomcat 
        export CATALINA_BASE = /path/Tomcat 
        export JAVA_HOME = /path/java  
```
