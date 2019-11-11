Docker Crash Course
===================

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

> 用户使用Docker时，需要使用Docker命令工具docker与Docker daemon建立通信,Docker daemon时Docker守护进程，负责接收并分发执行Docker命令.
> the Docker daemon 默认绑定一个UNIX socket at unix:///var/run/docker.sock.
```
➜  chyi sudo docker  

Usage:  docker [OPTIONS] COMMAND

A self-sufficient runtime for containers

Options:
      --config string      Location of client config files (default "/root/.docker")
  -c, --context string     Name of the context to use to connect to the daemon (overrides DOCKER_HOST
                           env var and default context set with "docker context use")
  -D, --debug              Enable debug mode
  -H, --host list          Daemon socket(s) to connect to
  -l, --log-level string   Set the logging level ("debug"|"info"|"warn"|"error"|"fatal") (default "info")
      --tls                Use TLS; implied by --tlsverify
      --tlscacert string   Trust certs signed only by this CA (default "/root/.docker/ca.pem")
      --tlscert string     Path to TLS certificate file (default "/root/.docker/cert.pem")
      --tlskey string      Path to TLS key file (default "/root/.docker/key.pem")
      --tlsverify          Use TLS and verify the remote
  -v, --version            Print version information and quit

Management Commands:
  builder     Manage builds
  config      Manage Docker configs
  container   Manage containers
  context     Manage contexts
  engine      Manage the docker engine
  image       Manage images
  network     Manage networks
  node        Manage Swarm nodes
  plugin      Manage plugins
  secret      Manage Docker secrets
  service     Manage services
  stack       Manage Docker stacks
  swarm       Manage Swarm
  system      Manage Docker
  trust       Manage trust on Docker images
  volume      Manage volumes

Commands:
  attach      Attach local standard input, output, and error streams to a running container
  build       Build an image from a Dockerfile
  commit      Create a new image from a container's changes
  cp          Copy files/folders between a container and the local filesystem
  create      Create a new container
  diff        Inspect changes to files or directories on a container's filesystem
  events      Get real time events from the server
  exec        Run a command in a running container
  export      Export a container's filesystem as a tar archive
  history     Show the history of an image
  images      List images
  import      Import the contents from a tarball to create a filesystem image
  info        Display system-wide information
  inspect     Return low-level information on Docker objects
  kill        Kill one or more running containers
  load        Load an image from a tar archive or STDIN
  login       Log in to a Docker registry
  logout      Log out from a Docker registry
  logs        Fetch the logs of a container
  pause       Pause all processes within one or more containers
  port        List port mappings or a specific mapping for the container
  ps          List containers
  pull        Pull an image or a repository from a registry
  push        Push an image or a repository to a registry
  rename      Rename a container
  restart     Restart one or more containers
  rm          Remove one or more containers
  rmi         Remove one or more images
  run         Run a command in a new container
  save        Save one or more images to a tar archive (streamed to STDOUT by default)
  search      Search the Docker Hub for images
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
  top         Display the running processes of a container
  unpause     Unpause all processes within one or more containers
  update      Update configuration of one or more containers
  version     Show the Docker version information
  wait        Block until one or more containers stop, then print their exit codes

Run 'docker COMMAND --help' for more information on a command.
```

| Docker 命令分类  | 子命令                                                                        |
| ---------------- | :---------------------------------------------------------------------------- |
| Docker环境信息   | info, version                                                                 |
| 容器生命周期管理 | create, exec, kill, pause, restart, rm, run, start, stop, unpause             |
| 镜像仓库命令     | login, logout, pull, push, search                                             |
| 镜像管理         | build, images, import, load, rmi, save, tag, commit                           |
| 容器运维操作     | attach, export, inspect, port, ps, rename, stats, top, wait, cp, diff, update |
| 容器资源管理     | volume, network                                                               |
| 系统日志信息     | events, history, logs                                                         |

![Docker 命令结构图](/imgs/ilikeit/DockerCrashCourse/docker_command_structure.png?raw=true)

* Docker 环境信息
```
$ sudo docker info  #  Display system-wide information

Client:
 Debug Mode: false

Server:
 Containers: 1
  Running: 0
  Paused: 0
  Stopped: 1
 Images: 1
 Server Version: 19.03.4
 Storage Driver: overlay2
  Backing Filesystem: extfs
  Supports d_type: true
  Native Overlay Diff: true
 Logging Driver: json-file
 Cgroup Driver: cgroupfs
 Plugins:
  Volume: local
  Network: bridge host ipvlan macvlan null overlay
  Log: awslogs fluentd gcplogs gelf journald json-file local logentries splunk syslog
 Swarm: inactive
 Runtimes: runc
 Default Runtime: runc
 Init Binary: docker-init
 containerd version: b34a5c8af56e510852c35414db4c1f4fa6172339
 runc version: 3e425f80a8c931f88e6d94a8c831b9d5aa481657
 init version: fec3683
 Security Options:
  seccomp
   Profile: default
 Kernel Version: 3.10.0-1062.4.1.el7.x86_64
 Operating System: CentOS Linux 7 (Core)
 OSType: linux
 Architecture: x86_64
 CPUs: 4
 Total Memory: 7.638GiB
 Name: jumpmachine
 ID: SQHV:3P2A:VXLM:3Z6A:7B3M:OIWF:CY2A:YEP6:CAO6:U7ZY:GAC6:XICC
 Docker Root Dir: /var/lib/docker
 Debug Mode: false
 Registry: https://index.docker.io/v1/
 Labels:
 Experimental: false
 Insecure Registries:
  127.0.0.0/8
 Live Restore Enabled: false

➜  ~ sudo docker version       # Show the Docker version information
Client: Docker Engine - Community
 Version:           19.03.4
 API version:       1.40
 Go version:        go1.12.10
 Git commit:        9013bf583a
 Built:             Fri Oct 18 15:52:22 2019
 OS/Arch:           linux/amd64
 Experimental:      false

Server: Docker Engine - Community
 Engine:
  Version:          19.03.4
  API version:      1.40 (minimum version 1.12)
  Go version:       go1.12.10
  Git commit:       9013bf583a
  Built:            Fri Oct 18 15:50:54 2019
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.2.10
  GitCommit:        b34a5c8af56e510852c35414db4c1f4fa6172339
 runc:
  Version:          1.0.0-rc8+dev
  GitCommit:        3e425f80a8c931f88e6d94a8c831b9d5aa481657
 docker-init:
  Version:          0.18.0
  GitCommit:        fec3683
```

* 2. 容器生命周期管理
```
# docker run 用基于特定的镜像创建一个容器
$ sudo docker run ubuntu echo "Hello World" 

# -i, --interactive Keep STDIN open even if not attached
# -t, --tty Allocate a pseudo-TTY
# --name string Assign a name to the container
# -c, --cpu-shares int CPU shares (relative weight)
# -m, --memory bytes Memory limit
# -v, --volume list Bind mount a volume
# -p, --publish list Publish a container's port(s) to the host
➜  ~ sudo docker run -i -t --name mytest ubuntu:latest /bin/bash
root@867bb5eb767a:/# 

# docker start/stop/restart 命令启动、停止和重启容器
``` 

* 3. Docker registry 
```
Docker registry是存储容器镜像的仓库，用户可以通过Docker client与Docker registry进行通信

# Pull an image or a repository from a registry
$ sudo docker pull
```