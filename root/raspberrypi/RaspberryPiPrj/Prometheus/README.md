Prometheus - 普罗米修斯
=======================
> Prometheus is an open-source systems monitoring and alerting toolkit originally built at SoundCloud.
> Most Prometheus components are written in Go, making them easy to build and deploy as static biraries.

* Features
    - a multi-dimensional data model with time series data identified by metric name and key-value pairs
    - PromQL, a flexible query language to leverage this dimensionality
    - no reliance on distributed storage; single server nodes are autonomous 
    - time series collection happens via a pull model over HTTP
    - pushing time series is supported via an intermediary gateway
    - targets are discovered via service discovery or static configuration 
    - multiple modes of graphing and dashboarding support

* Components
    - The main Prometheus server which scrapes and stores time series data 
    - client libraries for instrumenting application code 
    - a push gateway for supporting short-lived jobs 
    - special-purpose exporters for services like HAProxy, StatsD,Graphite,etc.
    - an alertmanager to handle alerts.
    - various support tools 

* Architecture
![Prometheus_architecture](/imgs/raspberrypi/Prometheus_architecture.png?raw=true)

Getting Started
---------------
```
# Downloading and running Prometheus 
$ wget https://github.com/prometheus/prometheus/releases/download/v2.12.0/prometheus-2.12.0.linux-amd64.tar.gz
$ tar -xcfz prometheus-*.tar.gz
$ cd prometheus-* 

# Configuring Prometheus to monitor itself 
$ vim /usr/local/prometheus-2.12.0.linux-amd64/prometheus.ymml
        global:
            scrape_interval: 60s    # By default, scrape targets every 60 seconds. 
            # Attach these labels to any time series or alerts when communicating with 
            # external systems (federation, remote storage, Alertmanager).
            external_labels:
                monitor: 'codelab-monitor'
        # A scrape configuration containing exactly one endpoint to scrape:
        # Here it's Prometheus itself.
        scrape_configs:
            # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
            - job_name: 'prometheus'
                # Override the global default and scrape targets from this job every 60 seconds 
                scrape_interval: 60s 

                static_configs:
                    - targets: ['localhost:9090']

# Staring Prometheus
# By default, Prometheus stores its database in ./data (flag --storage.tsdb.path).
$ ./prometheus --config.file=prometheus.yml 
# browse to a status page about itself at localhost:9090 

```
