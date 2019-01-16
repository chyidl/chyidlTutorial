RabbitMQ 
========

RabbitMQ is the most widely deployed open source message broker [消息中间件].It supports multiple messaging protocols.
RabbitMQ can be deplyed in distributed and federated configurations to meet high-scale, high-availability requirements.

RabbitMQ Tutorials
------------------

These tutorials cover the basics of creating messaging applications using RabbitMQ.

```
# install rabbitmq with following command 
$ sudo apt-get install rabbitmq-server 

# rabbitmq-management plugin provides an HTTP-based API for management and monitoring of RabbitMQ nodes and clusters,along with a browser-based UI and a command line tool.
$ sudo rabbitmq-plugins enable rabbitmq_management

# Management UI Access using a Web browser http://localhost:15672 
# create a new user with admin grants
$ sudo rabbitmqctl ad_user test test 
$ sudo rabbitmqctl set_user_tags test administrator 
$ sudo rabbitmqctl set_permissions -p / test ".*" ".*" ".*"

# Now you can access using test test 
```

- [Hello World](/root/ilikeit/RabbitMQCrashCourse/tutorials/facttail.c)
    - producer: A Program that sends message is a producer.
    - consumer: A consumer is a program that mostly waits to receive message.
    - queue: A queue is only bound by the host's memory & disk limits.
    - (using the Pika Python client): 
    - RabbitMQ libraries: RabbitMQ speaks AMQP 0.9.1 which is an open, general-purpose protocol for messaging
    



Best Practices [最佳实践]
------------------------
    
