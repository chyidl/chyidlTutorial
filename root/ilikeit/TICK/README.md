Monitor System Metrics With the TICK Stack 
==========================================
> https://www.digitalocean.com/community/tutorials/how-to-monitor-system-metrics-with-the-tick-stack-on-ubuntu-16-04 
> InfluxDB 1.x is a time series database designed to handle high write and query loads
>> High performance: allows for high throughput ingest, compression and real-time querying 
>> InfluxDB is written entirely in Go and compiles into a single binary with no external dependecies. 
>> InfluxDB works with InfluxQL, a SQL-like query language for interacting with data. 
>> InfluxQL supports regular expressions, arithmetic expressions, and time series-specific functions to speed up data processing. 
>> InfluxDB can handle millions of data points per seconds. 

TICK Stack
----------
> Collectively, Telegraf, InfluxDB, Chronograf and Kapacitor are known as the TICK Stack.
> The TICK Stack is a loosely coupled yet tightly integrated set of open source projects designed to handle massive amounts of time-stamped information to support your metrics analysis needs.
* Telegraf : is a plugin-driven server agent for collecting and reported metrics.
* InfluxDB : is a time series database built from the ground up to handle high write and query loads.
* Chronograf : is the administrative user interface and visualization engine of the stack.
* Kapacitor : is a native data processing engine. 

```
In this tutorial you'll set up and use the this platform as an open-source monitoring system. generate a bit of CPU usage and receive an email alert when the usage gets too high.
```

* Step 1 - Adding the TICK Stack Repository 
```
# Use the following commands to add the InfluxData repository:
$ curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add - 
$ source /etc/lsb-release 
$ echo "deb https://repos.influxdata.com/${DISTRIB_ID,,} ${DISTRIB_CODENAME} stable" | sudo tee /etc/apt/sources.list.d/influxdb.list 

# With the new repository in place, update the package list: 
$ sudo apt-get update
```

* Step 2 - Installing InfluxDB and Configuring AUthentication 
> InfluxDB is an open-source database optimized for fast, high-availabity storage and retrieval of time series data. InfluxDB is great for operations monitoring, application metrics, and real-time analytics.
```
# Install InfluxDB: 
$ sudo apt-get install influxdb 

# start the influxDB service:
$ sudo systemctl start influxdb 

# start the InfluxDB service 
$ sudo systemctl start influxdb 

# ensure the service is running properly 
$ sudo systermctl status influxdb 

# Start the InfluxDB console 
$ influx 
Connected to http://localhost:8086 version 1.8.0
InfluxDB shell version: 1.8.0
> CREATE USER "user" WITH PASSWORD 'sammy_admin' WITH ALL PRIVILEGES 
# Verify that the user is created: 
> SHOW users 
user admin
---- -----
chyi true
# Now that exists the InfluxDB console 
> exit

# open /etc/influxdb/influxdb.conf This is the configuration file for InfluxDB 
$ sudo vim /etc/influxdb/influxdb.conf 
  Locate the [http] section, uncomment the auth-enabled option, and set its value to true.
  auth-enabled = true 

# Save the file, exit the editor, and restart the InfluxDB service:
$ sudo systemctl restart inflxudb 
```

* Step 3 - Installing and Configuring Telegraf 
> Telegraf is an open-source agent that collects metrics and data on the system it's running on, or from other services. Telegraf then writes the data to InfluxDB.
```
# Run the following command to install Telegraf 
$ sudo apt-get install telegraf 
# The Telegraf service starts automatically after installation 
# Telegraf uses plugins to input and output data. The default output plugin is for InfluxDB. Since we've enabled user authentication for IndexDB, we have to modify Telegraf's configuratrion file to specify the username and password we've configured. Open the Telegraf configuration file in your editor
$ sudo vim /etc/telegraf/telegraf.conf 
  Locate the [outputs.influxdb] section and provide the username and password: 

$ sudo systemctl restart telegraf 

# The check whether the service is running propertly 
$ sudo systemctl status telegraf 

# Telegraf is now collecting data and writing it to InfluxDB. 
# Open the InfluxDB console and see which measurements Telegraf is storing in the database. 
$ influx -username 'user' -password 'password'
# see the available databases:
> show databases 
name: databases
name
----
_internal
telegraf

# Let's see what Telegraf is storing in that databse, Execute the following command to switch to the Telegraf database. 
> use telegraf 
# Display the various measurements Telegraf has collected by executing this command: 
> show measurements 
name: measurements
name
----
cpu
disk
diskio
kernel
mem
processes
swap
system
# As you can see, telegraf has collected and stored lots of information in this database. 
# There are more than input plugins for Telegraf, It can be gather metrics from many popular services and databases 
  Redis 
  PostgresSQL 
  MySQL 
  Docker 
> exit
# view usage instructions for each input plugins by running telegraf -usage plugin-name in the terminal window
```

* Step 4 - Installing Kapacitor 
> Kapacitor is a data processing engine. It lets you plug in your own custom logic to process alerts with dynamic thresholds, match metrics for patterns, or identify statistical anomalies. will use Kapacitor to read data from InfluxDB, generate alerts, and send those alerts to a specified email address. 
```
# install Kapacitor 
$ sudo apt-get install kapacitor

# open the kapacitor configuration file in your editor 
$ sudo vim /etc/kapacitor/kapacitor.conf 

  Locate the [[influxdb]] section and provide the username and password to connect to the InfluxDB database 

# start Kapacitor 
$ sudo systemctl start kapacitor 

# verify Kapacitor is running 
$ kapacitor list task
D Type      Status    Executing Databases and Retention Policies

# Kapacitor supports multiple alert endpoints:
```

* Step 5 - Chronograf 
> Chronograf is a graphiling and visualization application that provides tools to visualize monitoring data and create alerting and automation rules.
```
# Download and install the latest package: 
$ wget https://dl.influxdata.com/chronograf/releases/chronograf_1.8.4_amd64.deb
$ sudo dpkg -i chronograf_1.8.4_amd64.deb

# start the Chronograf service:
$ sudo systemctl start chronograf 

# If you are using Uncomplicated Firewall, configure it to allow connections to port 8888 
$ sudo ufw allow 8888/tcp 

# You can access the Chronograf interface by visiting http://your_server_ip:8888
# Use the default connection details, didnot configure a username and password for kapacitor

# Managing Chronograf security 
> To enhance security, configure Chronograf to authenticate and authorize with OAuth 2.0 and use TLS/HTTPS/     
1. Configure OAuth 2.0:
  > Configure Chronograf to use an OAuth 2.0 provider and JWT (JSON Web Token) to authenticate users and enable role-based access controls.
  > Generate a Token Secret 
  >> configure the TOKEN_SECRET environment variable (or command line option). Chronograf will use this secret to generate the JWT Signature for all access tokens.
  >> 1. Generate a secret, high-entropy pseudo-random string. 
  >> $ openssl rand -base64 256 | tr -d '\n'
  >> 2. Set the environment variables:
  >> export TOKEN_SECRET=<mysecret>
2. Set configuration for your OAuth provider 
  » 

3. Testing with self-signed certificates:
  # to create a certificate and key in one file with OpenSSL:
  $ openssl req -x509 -newkey rsa:4096 -sha256 -nodes -keyout testing.pem -out 
```
