TDengine
========
> An open-source big data platform designed and optimized for the Internet of Things (loT)

What is TDengine?
-----------------
```
TDengine is an open-source big data platform, designed and optimized for the Internet of Things (loT), Connected Cars, Industrial loT, and IT Infrastructure and Application Monitoring. Besides the 10x faster time-series database, it provides caching, stream computing, message queuing and other functionlities to reduce the complexity and cost of development and operation. 
    
    10x Faster on Insert/Query Speeds: Through the innovative design on storage, on a single-core machine, over 20K requests can be processed, millions of data points can be ingested, and over 10 million data points can be retrieved in a second. It is 10 times faster than other databases. 

    1/5 Hardware/Cloud Service Costs: Compared with typical big data solutions, less than 1/5 of computing resources are required. Via column-based storage and tuned compression algorithms for different data types, less than 1/10 of storage space if needed.

    Full Stack for Time-Series Data: By integrating a database with message queueing, caching, and stream computing features together, it is no longer necessary to integrate Kafka/Redis/HBase/Spark or other software. It makes the system architecture much simpler and more robust..

    Powerful Data Analysis: Whether it is 10 years or one minute age, data can be queries just by specifying the time range, Data can be aggregated over time, multiple time streams or both. Ad Hoc queries or analyses can be executed via TDengine shell, Python, R or Matlab.

    Seamless Integration with Other Tools: Telegraf, Grafana, Matlab, R, and other tools can be integrated with TDengine without a line of code. MQTT, OPC, Hadoop, Spark, and many others will be integrated soon. 

    Zero Management, No Learning Curve: It takes only seconds to downloed, install, and run it successful; there are no other dependencies. Automatic partitioning on tables or DBs, Standard SQL is used, with C/C++, Python, JDBC, Go and RESTful connectors.
```

Install
-------
```
$ git clone https://github.com/taosdata/TDengine.git 
$ cd TDengine 
$ mkdir build && cd build 
$ cmake .. && cmake --build . 
# After building successfully, TDengine can be installed by:
$ make install 
Install the project...
/usr/bin/cmake -P cmake_install.cmake
-- Install configuration: "Debug"
make install script: /home/chyi/chyidl.com/TDengine/packaging/tools/make_install.sh
source directory: /home/chyi/chyidl.com/TDengine
binary directory: /home/chyi/chyidl.com/TDengine/build
Start to install TDEngine...
[sudo] password for chyi:
Created symlink /etc/systemd/system/multi-user.target.wants/taosd.service → /etc/systemd/system/taosd.service.

TDengine is installed successfully!

To configure TDengine : edit /etc/taos/taos.cfg
To start TDengine     : sudo systemctl start taosd
To access TDengine    : use taos in shell

TDengine is installed successfully!
```


