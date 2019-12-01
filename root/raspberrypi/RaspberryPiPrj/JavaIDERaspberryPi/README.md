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

# Install Java on CentOS and Fedora 
$ sudo yum install java-1.8.0-openjdk  # install JRE using yum 
or 
$ sudo yum install java-1.8.0-openjsk-devel  # install JDK using yum

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

Centos Automatically Start Apache Tomcat Server on Boot 
-------------------------------------------------------
```
Step 1: Create a file named tomcat8.5 in your /etc/init.d directory 
$ cd /etc/init.d
$ sudo vim tomcat8.5 

Step 2: Copy the following script and save the file 
#!/bin/bash 
# chkconfig: 2345 80 20 
# Description: Tomcat Server basic start/shutdown script 
# /etc/init.d/tomcat8.5 -- startup script for the Tomcat 8.5 servlet engine 

TOMCAT_HOME=/usr/local/apache-tomcat-8.5.41/bin
START_TOMCAT=/usr/local/apache-tomcat-8.5.41/bin/startup.sh 
STOP_TOMCAT=/usr/local/apache-tomcat-8.5.41/bin/shutdown.sh

start() {
    echo -n "Stating tomcat8.5.41: "
    cd $TOMCAT_HOME 
    ${START_TOMCAT}
    echo "done."
}

stop() {
    echo -n "Shutting down tomcat8.5.41: "
    cd $TOMCAT_HOME
    ${STOP_TOMCAT}
    echo "done."
}

case "$1" in 

start) 
    start
    ;;

stop)
    stop
    ;;

restart)
    stop
    sleep 10
    start
    ;;

*)
    echo "Usage: $0 {start|stop|restart}"

esac
exit 0

Step 3: Update the file permissions to make it executable by any user 
$ chmod 755 tomcat8.5 

Step 4: Make sure you have chkconfig command installed 
$ chkconfig --help 
$ sudo apt-get install chkconfig 

Step 5: Run chkconfig command to add the script to the startup services 
$ chkconfig --add tomcat8.5 
Basically the chkconfig command automatically adds the symbolic links for starting and stopping the service based on the parameters passed to it.

Step 6: Make sure scripts got added to the startup services 
$ chkconfig --list tomcat8.5 

Step 7: Verify your service is working 
To start the Tomcat server 
$ service tomcat start 
To stop the Tomcat server 
$ service tomcat stop 
```

MacBook Pro for Java Install with Homebrew
------------------------------------------
```
The version of Java available in Homebrew Cask previous to October 3, 2018 was indeed the Oracle JVM, Now homeever, it has now been updated to OpenJDK. Be sure to update Homebrew and then you will see the lastest version available for install.

1. Install Homebrew if you havn't already. Make sure it is updated.
$ brew update 

2. Add the casks tap, if you havn't already (or you are not seeing older Java versions anymore with step #3)
$ brew tap homebrew/cask=versions 
and for the AdoptOpenJDK versions, add that tap:
$ brew tap ado[topenjdk/openjdk 

3. Look for installable versions:
$ brew search java 
or for AdoptOpenJDK versions:
$ brew search jdk 

4. Check the details on the version that will be installed:
$ brew cask info java 
or for the AdoptOpenJDK version:
$ brew cask info adoptopenjdk 

5. Install a specific version of the JDK such as java11, adoptopenjdk8, or just java or adoptopenjdk for the current. For example:
$ brew cask install java 
You can use the fully qualified path to older versions as well:
$ brew cask install homebrew/cask-versions/java11
And these will be installed into /Library/Java/JavaVirtualMachines/ which is the traditional location expected on Mac OS X.
```

Memory Problem: Process killed by OOM Killer
--------------------------------------------
```
$ cd /var/log/
[root@rabbitmq_test_01 log]# cat messages | grep 'Out of memory'
Aug 12 18:00:24 iZbp1h7tr5p83bwyejuss9Z kernel: Out of memory: Kill process 8074 (java) score 108 or sacrifice child
Aug 12 18:00:24 iZbp1h7tr5p83bwyejuss9Z kernel: Out of memory: Kill process 8081 (VM Thread) score 108 or sacrifice child
Aug 12 18:00:24 iZbp1h7tr5p83bwyejuss9Z kernel: Out of memory: Kill process 8112 (mysql-cj-abando) score 108 or sacrifice child
Aug 13 12:00:08 iZbp1h7tr5p83bwyejuss9Z kernel: Out of memory: Kill process 15578 (java) score 95 or sacrifice child
Aug 13 12:00:08 iZbp1h7tr5p83bwyejuss9Z kernel: Out of memory: Kill process 15592 (VM Periodic Tas) score 95 or sacrifice child
Aug 13 13:50:09 iZbp1h7tr5p83bwyejuss9Z kernel: Out of memory: Kill process 2767 (java) score 105 or sacrifice child
Aug 13 13:50:09 iZbp1h7tr5p83bwyejuss9Z kernel: Out of memory: Kill process 2835 (org.springframe) score 105 or sacrifice child

A Java process is made up of:
    Java heap space (set via -Xms and Xmx)
    the Metaspace (previously PermGen in Java 7)
    the Native Memory area 

Each one of these areas will use RAM. The memory is the sum of the maximum Java heap size, the Metaspace size and the native memory area.

It is important to understand that the Operating System itself and any other process running on the machine have their own requirements regarding RAM and CPU. The operating System uses a certain amount of RAM which leaves the remaining RAM to be split among any other processes on the machine.

Resolution:
(This does not indicate a problem with Programs. It indicates that the Operating System is unable to prodive enough resources for all the programs it has been asked to run.)

The OOM Killer is a function of the linux kernel that kill rogue processes that are requesting more memory that the OS can allocate so that the system can survive. The function applies some heuristics(it gives each process a score) to decide which process to kill when the system is in such state. The process 
```

Install OpenJDK 11 on Mac using brew 
------------------------------------
> have to pay for Oracle JDK, so it's better to use OpenJDK 
```
OpenJDK(Open Java Developerment Kit) is a free and open-source implementation of the Java Platform, Standard Edition(Java SE.) It is the result fo an effort Sun Microsystem begain in 2006. The implementation is licensed under the GNU General Public License(GNU GPL) version 2 with a linking exception. Where it not for the GPL linking exception, components that linked to the Java class library would be subject to the terms of the GPL license.
```
```
1. Brew tap 
# First of all, we need to tap a brew repo. Execute the following command:
$ brew tap AdoptOpenJDK/openjdk

2. Install OpenJDK 11 Mac 
$ brew cask install adoptopenjdk11 

3. Check JDK Version 
# Now we can check the JDK version 
$ java -version 
openjdk version "11.0.5" 2019-10-15
OpenJDK Runtime Environment AdoptOpenJDK (build 11.0.5+10)
OpenJDK 64-Bit Server VM AdoptOpenJDK (build 11.0.5+10, mixed mode)

4. Java Location 
# Now let's check the java path 
$ which java 
/usr/bin/java
```

Install Maven on Mac Using brew 
-------------------------------
```
Run following command to Terminal 
$ brew update 
$ brew install maven 

Check the version using mvn 
$ mvn -v 
Apache Maven 3.6.3 (cecedd343002696d0abb50b32b541b8a6ba2883f)
Maven home: /usr/local/Cellar/maven/3.6.3/libexec
Java version: 11.0.5, vendor: AdoptOpenJDK, runtime: /Library/Java/JavaVirtualMachines/adoptopenjdk-11.jdk/Contents/Home
Default locale: en_CN, platform encoding: UTF-8
OS name: "mac os x", version: "10.15.1", arch: "x86_64", family: "mac"

Check location of mvn 
$ which mvn 

Configure .zshrc 
export M2_HOME=/usr/local/Cellar/maven/3.6.3/libexec
export M2=${M2_HOME}/bin
export PATH=${PATH}:${M2_HOME}/bin
```