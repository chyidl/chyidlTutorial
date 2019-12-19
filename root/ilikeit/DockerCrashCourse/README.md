Docker Crash Course
===================
> It works on my machine.
```
Virtual Machine: 虚拟机
    1. 资源占用多(独占部分内存和硬盘空间)
    2. 启动慢(启动操作系统多久，启动虚拟机就需要多久,然后应用程序才能真正运行)
```

Introduction Conceptual Guides Containers, VMs and Docker
---------------------------------------

```
1. What are "Containers" and "VMs"? 
    Containers and VMs are similar in their goals: to isolate an application and its dependencies into a self-contained unit that can run anywhere.

The Main Difference Between Containers And VMs Is In Their Architectural. 

2. Virtual Machines 
    A VM is essentially an emulation of a real computer that executes programs like a real computer. VMs run on top of a physical machine using a "hypervisor". A hypervisor, in turn, runs on either a host machine or on "bare-metal".

    A **hypervisor** is a piece of software, firmware, or hardware that VMs run on top of. The VM that is running on the "host machine", The VM that is running on the host machine (again, using a hypervisor) is also often called a "guest machine". 

    As mentioned above, a "guest machine" can run on either a "hosted hypervisor" or a "bare-metal hypervisor". 
        
        "hosted hypervisor" : the underlying hardware is less important. The host's operating system is responsible for the hardware drivers instead of the hypervisor itself. 

        "bare metal hypervisor" : interfaces directly with the underlying hardware, it doesn't need a host operating system to run on. 
```
![](/imgs/ilikeit/DockerCrashCourse/VirtualMachineDiagram.png?raw=true) Virtual Machine Diagram image

```
Container : provides operating-system-level virtualization by abstacting the "user space". The one big difference between containers and VMs is that containers *share* the host system's kernel with other containers. 
```
![](/imgs/ilikeit/DockerCrashCourse/ContainerDiagram.png?raw=true)Container Diagram image

```
Docker: a helperful tool for packing, shipping, and running applications within "containers."
```

Guides for Docker
-----------------
Docker is an open-source project based on Linux containers. It uses Linux Kernel features like namespaces and control groups to create containers on top of an operating system.

* Ease of use: Containers in order to quickly build and test portable applications. The mantra is "build once, run anywhere."

* Speed: Docker containers are very lightweight and fast. 

* Docker Hub: DOcker users also benefit from the incresingly rich ecosystem of Docker Hub

* Modularity and Scalability: Docker makes it easy to break out your application's functionality into individual containers. With Docker, it's become easier to link these containers together to create your application, making it easy to scale or update components independently in the future.

Fundamental Docker Concepts
---------------------------

![](/imgs/ilikeit/DockerCrashCourse/DockerConcept.png?raw=true) Fundamental Docker Concepts

* Docker Engine: is the layer on which Docker runs. It's a lightweight runtime and tooling that manages containers, images, builds, and more. 
    1. A Docker Daemon that runs in the host computer 
    2. A Docker Client that then communicates with the Docker Daemon to execute commands 
    3. A REST API for interacting with the Docker Daemon remotely 

* Docker Client: is what you, as the end-user of Docker, communicate with

* Docker Daemon: is what actually executes commands sent to the Docker Client -- like building, running, and distributing your containers.

* Dockerfile: is where your write the instructions to build a Docker image. These instructions can be :
    1. RUN apt-get y install some-package: to install a software package 
    2. EXPOSE 8000: to expose a port 
    3. ENV ANT_HOME /usr/loca/apache-ant to pass an environment variable 
    4. CAN use the docker build command to build an image from dockerfile. 

* Docker Image: Images are read-only templates that you build from a set of instructions written in your Dockerfile. The Docker image is built using a Dockerfile. Each instruction in the Dockerfile adds a new "layer" to the image, with layers representing a portion of the images file system that either adds to or replaces the layer below it. Layers are key to Docker's lightweight yet powerful structure. Docker uses a Union File System to achieve this:

* Union File Systems: Docker uses Union File Systems to build up an image. That's how file systems can *appear* writeable without actually allowing writes. (In other words, a "copy-on-write" system.)
    1. Duplication-free: layers help avoid duplicating a complete set of files every time you use an image to create and run a new container,making instantiation of docker containers very fast amd cheap. 
    2. Layer segregation: Making a change is much faster -- when you change an image, Docker only propagates the updates to the layer that was changed. 

* Volumes: are the "data" part of container,initialized when a container is created. Volumes allow you to persist and share a container's data. Data volumes are separate from the default Union File System and exist as normal directories and files on the host filesystem. So, even if you destroy, update, or rebuild your container, the data volumes will remain untouched. When you want to update a volume,you make change to it directly. 

* Docker Containers: Docker containers are built off Docker images, Since images are read-only, Docker adds a read-write file system over the read-only file system of the image to create a container. 

![](/imgs/ilikeit/DockerCrashCourse/DockerContainer.png?raw=true) Fundamental Docker Concepts

* 1) Namespace: provides containers with their own view of the underlying Linux system, limiting what the container can see and access. 
    a. NET: Provides a container with its own view of the network stack of the system 
    b. PID: PID stands for Process ID. PID1, which is the "ancestor of all processes". 
    c. MNT: Gives a container its own view of the "mounts" on the system. 
    d. UTS: UTS stands for UNIX Timesharing System. It allows a process to identify system identifiers
    e. IPC: IPC stands for InterProcess Communication.
    f. USER: It functions by allowing containers to have a different view of the uid (user ID) and gid (group ID) ranges, as compared with the host system. 

* 2) Control groups: is a Linux kernel feature that isolates, prioritizes, and accounts for the resource usage (CPU, memory, disk I/O, network, etc.) of a set of processes. Cgroups also ensure that a single container doesn't exhaust one of those resources and bring the entire system down. 

* 3) Isolated Union file system: 

The Future of Docker: Docker and VMs Will Co-exist 
--------------------------------------------------

If you need to run multiple applications on multiple servers, it probably makes sense to use VMs. On the other hand, if you need to run mant *copies* of a single application, Docker offers some compelling advantages. 

Install and Use Docker
----------------------
```
# First, in order to ensure the downloads are valid, add the GPG key for the official Docker repository to your system.
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# Add the Docker repository to APT sources
$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

# Next, update the package database with the Docker packages from the newly added repo:
$ sudo apt-get update 

# Make sure you are about to install from the Docker repo instead of the default Ubuntu 16.04 repo:
$ apt-cache policy docker-ce 

# Finally, install Docker 
$ sudo apt-get install -y docker-ce 

# Docker should now be installed, the daemon started, and the process enabled to start on boot
$ sudo systemctl status docker 


# Using the Docker Command 
$ docker [option] [command] [arguments]

# To view the switches available to a specific command 
$ docker docker-subcommand --help 

# To view system-wide information about Docker 
$ docker info 

# Working with Docker Images 
➜  ~ sudo docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
1b930d010525: Pull complete
Digest: sha256:2557e3c07ed1e38f26e389462d03ed943586f744621577a99efb77324b0fe535
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

# Search for images available on Docker Hub by using the docker 
$ docker search mysql

# download MySQL Server Docker Image to your computer 
$ sudo docker pull mysql

# Starting a MySQL Server Instance; 
$ sudo docker run --name chyidl -e MYSQL_ROOT_PASSWORD=my-secret -d mysql 

# To see the images that have been downloaded to your computer 
$ docker images 

# Running a Docker Container
$ docker run -it mysql  # -i -t switches gives you interactive shell access 

# Managing Docker Containers 
# To view the active containers 
$ docker ps  

# To view all containers - active and inactive 
$ docker ps -a 

# To start a stoped container 
$ sudo docker start 45e252bab938
$ sudo docker stop 45e252bab938 

# remove it with docker rm 
$ sudo docker rm 45e252bab938 
```