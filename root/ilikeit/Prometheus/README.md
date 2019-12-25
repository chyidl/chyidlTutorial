Prometheus Grafana MySQL监控
===========================
![Prometheus Grafana MySQL](/imgs/ilikeit/Prometheus/Prometheus_Grafana_MySQL.png?raw=true)
```
> Prometheus广泛用于Kubernetes集群监控系统
Prometheus 是一套开源的系统监控报警框架
    1. 强大的多维度数据模型
        1.1. 实践序列数据通过metric名和键值对区分
        1.2. 所有的metrics都可以设置任意的多纬标签
        1.3. 数据模型随意
        1.4. 可以对数据模型进行聚合，切割和分片操作
        1.5. 支持双精度浮点类型，标签可以设为全unicode 
    2. 灵活强大的查询语句PromQL: 
        2.1: 同一查询语句可以对多个metrics进行乘法、加法、连接、取分数位等操作 
    3. 易于管理: Prometheus server是一个单独的二进制文件，可直接在本地工作，不依赖分布式存储
    4. 高效：平均每个采样点仅占3.5bytes. 一个Prometheus server可以处理数百万的metrics 
    5. 使用pull模式采集时间序列数据，这样不仅有利于本机测试而且可以避免有问题的服务器推送坏的metrics
    6. 可以采用push gateway的方式把时间序列数据推送到prometheus server端 
    7. 可以通过服务发现或者静态配置获取监控的targets 
    Prometheus 不适用对采集数据100%准确的场景，但是用于记录时间序列数据，Prometheus具有很大的查询优势

Prometheus 组成及架构:
    1. Prometheus Server: 用于收集和存储时间序列数据 
    2. Client Library: 客户端库，为需要监控的服务生成响应的metrics并暴露给Prometheus Server.当Prometheus server来pull时，直接返回实时状态的metrics 
    3. Push gateway: 主要用于短期的Jobs,主要用于服务层面的metrics，对于机器层面的metrics需要使用node exporter 
    4. Exporters: 用于暴露已有的第三方服务的metrics 给 Prometheus 
    5. AlterManager: 从Prometheus Server端接受到alerts后，会进行去重复数据、分组、并路由接受方式、发出报警[email, pagerduty, OpsGenie, webhook]
```
![Prometheus](imgs/ilike/Prometheus/Prometheus.png?raw=true)
```
工作流程:
    1. Prometheus server定期从配置好的jobs或者exporters中拉metrics,或者接收来自Pushgateway发过来的metrics.或者从其他的Prometheus server中拉metrics.
    2. Prometheus server 在本地存储收集到的metrics并运行alert.rules 记录新的时间序列或者向Alertmanager推送报警 
    3. Altermanager根据配置文件，对接收的报警进行处理、发出告警
    4. 在图形界面中，可视化采集数据

Promethues 客户端库提供四种主要的metric类型:
    1. Counter 
    2. Gauge: 
    3. Histogram: 
    4. Summary 
    5. instance 和 jobs 
    6. instance :一个单独的instances
    7. jobs: 一组同种类型的instances 
```

Install and Configure Prometheus on CentOS 
------------------------------------------
```
# Create Prometheus System User and Group 
$ sudo useradd -M -r -s /bin/false prometheus 
$ id prometheus 

# Create Prometheus Configuration Directories 
$ mkdir /etc/promethus
$ mkdir /var/lib/prometheus

# Download Prometheus 
$ wget https://github.com/prometheus/prometheus/releases/download/v2.15.0/prometheus-2.15.0.linux-amd64.tar.gz
$ tar -xvf prometheus-* 
$ cd prometheus-* 
$ sudo cp prometheus-2.15.0.linux-amd64/{prometheus, promtool} /usr/local/bin/
$ sudo cp -r prometheus-2.15.0.linux-amd64/{consoles,console_libraries} /etc/prometheus/
$ sudo cp prometheus-2.15.0.linux-amd64/prometheus.yml /etc/prometheus/
$ sudo vim /etc/prometheus/prometheus.yml 

# Allow Prometheus through firewall 
$ firewall-cmd --add-port=9090/tcp --permanent 
# Reload firewalld
$ firewall-cmd --reload 

# Set Proper Ownership on Configuration Files and Directories 
$ sudo chown -R prometheus:prometheus /etc/prometheus
$ sudo chown -R prometheus:prometheus /var/lib/prometheus
$ sudo chown prometheus.prometheus /usr/local/bin/{prometheus,promtool}

# Starting Prometheus 
$ prometheus --config.file=/etc/prometheus/prometheus.yml  

# Create prometheus Systemd Service file 
$ sudo vim /etc/systemd/system/prometheus.service 
    [Unit]
    Description=Prometheus Time Series Collection and Processing Server 
    Wants=network-online.target 
    After=network-online.target 

    [Service]
    User=prometheus
    Group=prometheus 
    Type=simple
    ExecStart=/usr/local/bin/prometheus \ 
        --config.file /etc/prometheus/prometheus.yml \
        --storage.tsdb.path /var/lib/prometheus/ \
        --web.console.templates=/etc/prometheus/consoles \
        --web.console.libraries=/etc/prometheus/console_libraries 
    
    [Install]
    WantedBy=multi-user.target 

# Reload systemd daemon configuration 
$ sudo systemctl daemon-reload 
# Start and Enable prometheus service to run at boot time 
$ sudo systemctl enable --now prometheus 
$ sudo systemctl status prometheus 
```

Install Prometheus Node exporter
--------------------------------
```
# Create Node Exporter System User 
$ sudo useradd -M -r -s /bin/false node_exporter

# Download and Install Node Exporter
$ wget https://github.com/prometheus/node_exporter/releases/download/v0.18.1/node_exporter-0.18.1.linux-amd64.tar.gz
$ tar -xvf node_exporter-0.18.1.linux-arm64.tar.gz 
$ sudo cp node_exporter-*.*/node_exporter /usr/local/bin/
$ sudo chown node_exporter:node_exporter /usr/local/bin/node_exporter 

# Create Node Exporter System Service 
$ sudo vim /etc/systemd/system/node_exporter.service 
    [Unit]
    Description=Prometheus Node Exporter 
    Wants=network-online.target 
    After=network-online.target 

    [Service]
    User=node_exporter 
    Group=node_exporter 
    Type=simple 
    ExecStart=/usr/local/bin/node_exporter --collector.cpu --collector.meminfo --collector.loadavg --collector.filesystem

    [Install]
    WantedBy=multi-user.target 

$ sudo systemctl enable node_exporter 
$ sudo systemctl start node_exporter 

$ sudo ss -altnp | grep 9100

# Open Port 9100 on FirewallD
> To allow remote connection to Node Exporter from Prometheus server only, you can use Firewall rich rules as follows 
$ curl http://localhost:9100/metrics 查看server metrics 信息 

# Add Node Exporter Target to Prometheus 
$ sudo vim /etc/prometheus/prometheus.yml 

    ...
    # Here it's Prometheus itself. 
    scrape_configs:
        ...
        ## Add Node Exporter
        - job_name: 'node01'
            scrape_interval: 5s
            static_configs:
            - targets: ['127.0.0.1:9100']

# Restart prometheus service 
$ sudo systemctl restart prometheus 
```

Install Prometheus mysqld exporter
--------------------------------
```
# Create Node Exporter System User 
$ sudo useradd -M -r -s /bin/false mysqld_exporter

# Download and Install Node Exporter
$ wget https://github.com/prometheus/mysqld_exporter/releases/download/v0.12.1/mysqld_exporter-0.12.1.linux-amd64.tar.gz
$ tar -xvf mysqld_exporter-0.12.1.linux-arm64.tar.gz 
$ sudo cp mysqld_exporter-*.*/mysqld_exporter /usr/local/bin/
$ sudo chown mysqld_exporter:mysqld_exporter /usr/local/bin/mysqld_exporter 

# Required Grants 
mysql> CREATE USER 'mysqld_exporter'@'localhost' IDENTIFIED BY 'xxxx' WITH MAX_USER_CONNECTIONS 3;
mysql> GRANT PROCESS, REPLICATION CLIENT, SELECT ON *.* TO 'mysqld_exporter'@'localhost';
mysql> FLUSH PRIVILEGES;

# Configure database credentials 
$ sudo vim /etc/mysqld_exporter.cnf 
    [client]
    user=mysqld_exporter 
    password=xxx 
    host=localhost
    port=3306
$ sudo chown mysqld_exporter:mysqld_exporter /etc/mysqld_exporter.cnf 


# Create Node Exporter System Service 
$ sudo vim /etc/systemd/system/mysqld_exporter.service 
    [Unit]
    Description=Prometheus Mysqld Exporter 
    Wants=network-online.target 
    After=network-online.target 

    [Service]
    User=mysqld_exporter 
    Group=mysqld_exporter 
    Type=simple 
    ExecStart=/usr/local/bin/mysqld_exporter \
        --config.my-cnf /etc/mysqld_exporter.cnf \
        --collect.global_status \
        --collect.info_schema.innodb_metrics \
        --collect.auto_increment.columns \
        --collect.info_schema.processlist \
        --collect.binlog_size \
        --collect.info_schema.tablestats \
        --collect.global_variables \
        --collect.info_schema.query_response_time \
        --collect.info_schema.userstats \
        --collect.info_schema.tables \
        --collect.perf_schema.tablelocks \
        --collect.perf_schema.file_events \
        --collect.perf_schema.eventswaits \
        --collect.perf_schema.indexiowaits \
        --collect.perf_schema.tableiowaits \
        --collect.slave_status \
        --web.listen-address=0.0.0.0:9104

    [Install]
    WantedBy=multi-user.target 

$ sudo systemctl enable mysqld_exporter 
$ sudo systemctl start mysqld_exporter 

$ sudo ss -altnp | grep 9104

# Open Port 9104 on FirewallD
> To allow remote connection to Node Exporter from Prometheus server only, you can use Firewall rich rules as follows 
$ curl http://localhost:9104/metrics 查看server metrics 信息 

# Add MySQLD Exporter Target to Prometheus 
$ sudo vim /etc/prometheus/prometheus.yml 

    ...
    # Here it's Prometheus itself. 
    scrape_configs:
        ...
        ## Add Node Exporter
        - job_name: 'zong_mysql'
            static_configs:
            - targets: ['xxxxx:9104']

# Restart prometheus service 
$ sudo systemctl restart prometheus 
```

Grafana - The Open observability platform 
-----------------------------------------
> Grafana是一个开源的功能丰富的数据可视化平台，用于时序数据的可视化
```
Grafana is the open source analytics & monitoring solution for every database 
# Install via YUM Repository 
$ sudo vim /etc/yum.repos.d/grafana.repo 
    [grafana]
    name=grafana
    baseurl=https://packages.grafana.com/oss/rpm
    repo_gpgcheck=1
    enabled=1
    gpgcheck=1
    gpgkey=https://packages.grafana.com/gpg.key
    sslverify=1
    sslcacert=/etc/pki/tls/certs/ca-bundle.crt
$ sudo yum install grafana 

# Start the server (via systemd)
$ sudo systemctl daemon-reload 
$ sudo systemctl start grafana-server 
$ sudo systemctl status grafana-server 
# Enable the systemd service to start at boot 
$ sudo systemctl enable grafana-server.service 

https://localhost:3000 
    user:admin
    password:admin -> 

# 安装仪表盘
$ git clone https://github.com/percona/grafana-dashboards.git
$ cp -r grafana-dashboards/dashboards /var/lib/grafana/ 

导入仪表盘
MySQL_Overview.json
```
![MySQL_Overview](/imgs/ilikeit/Prometheus/mysql_overview.png?raw=true)

Prometheus 生态
---------------
```
Prometheus 是一个监控采集与数据存储框架(监控server端),具体采集什么数据依赖于具体的exporter(监控client端)
    mysql_exporter: 采集MySQL各种性能的
    node_exporter: 采集主机磁盘、内存、CPU等硬件性能指标

```