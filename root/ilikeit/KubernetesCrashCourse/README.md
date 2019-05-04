容器技术
========

> 从过去以物理机和虚拟机为主体的开发运维环境，向以容器为核心的基础设施的转变过程涵盖了对网络、存储、调度、操作系统、分布式原理等各个方面的容器化理解和改造。

> Linux 进程模型对于容器本身具有重要意义，控制器模式对于整个Kubernetes项目具有提纲作用

> 一个人的命运，要靠自我的奋斗，也要考虑历史的行程.
```
PaaS项目:提供一种名叫"应用托管"的能力.
    
    1.最原始的方式，在当时，虚拟机和云计算已经是比较普遍的技术和服务，那时主流用户的普遍用法，就是租一批AWS或者OpenStack的虚拟机，然后想管理物理服务器那样，用脚本或者手工的方式在这些机器上部署。【部署过程难免会碰到云端虚拟机和本地环境不一致的问题，所以当时的云计算服务，比的就是谁能更好的模拟本地服务器环境,带来更好的“上云”体验.】
    2. PaaS项目最核心的组件就是一套应用的打包和分发机制，Cloud Foundry为每种主流编程语言都定义一种打包格式，基本上等同于用户把应用的可执行文件和启动脚本打包进入一个压缩包，上传到云上Cloud Foundry的存储，接着，Cloud Foundry 会通过调度器选择一个可以运行这个应用的虚拟机，然后通知这个机器上的Agent把应用压缩包下载下来启动.Cloud
       Foundry会调用操作系统的Cgroups和Namespace机制为每一个应用单独创建一个称作"沙盒"的隔离环境，然后在"沙盒“中启动应用程序

Docker 镜像由一个完整的操作系统所有文件和目录构成，同时包含一个应用运行所需要的所有依赖.
$ docker build "images" # 制作镜像
$ docker run "镜像" # 运行镜像, 使用Cgroups和Namespace机制创建隔离环境。 

Docker原生容器集群管理项目Swarm：完全使用Docker项目原本的容器管理API来完成集群管理.
Mesos: 擅长大规模集群的调度与管理
Kubernetes: 容器编排与管理的生态,从API到容器运行时的每一层，Kubernetes项目都为开发者提供可以扩展的插件机制，鼓励用户通过代码的方式介入Kubernetes项目的每一个阶段.
$ docker run " 单机Docker项目"
$ docker run H "Swarm集群API地址" “多机Docker项目”

Docker 三件套: Docker Compose, Swarm, Machine
Container Runtime:容器运行库作为Docker项目的核心依赖

Istio: 微服务治理项目
Operator: 有状态应用部署框架

CO: Container Orchestration容器编排:主要是指用户通过某些工具或者配置完成一组虚拟机以及关联资源的定义、配置、创建、删除等工作，然后由云计算平台按照这些指令的逻辑完成的过程
CaaS: Container-as-a-Service 
PaaS: Platform-as-a-Service
DC/OS: 数据中心操作系统,旨在使用户能够管理一台机器那样管理一个万级别的物理机机群。
```

> 容器技术的兴起源于PaaS技术的普及; Docker公司发布的Docker项目具有里程碑式的意义；Docker项目通过容器镜像解决应用打包这个根本性难题.

> “ 容器本身没有价值，有价值的事容器编排”

```
"程序",也叫做代码可执行镜像 executable image; 程序运行之后就会从磁盘上的二进制文件，变成计算机内存中的数据、寄存器中的值、堆栈中的指令、以及被操作的文金啊，以及各种设备的状态信息的一个集合。

“进程”：静态状态就是磁盘上的可执行镜像，动态状态是计算机内数据和状态的集合.

容器的核心功能就是通过约束和修改进程的动态表现，从而为其创造出一个“边界”.

Cgroups技术：是用来制作约束的主要手段 
Namespace技术：用来修改进程试图的主要方法

$ uname -a
Darwin Chyis-MacBook-Pro.local 18.5.0 Darwin Kernel Version 18.5.0: Mon Mar 11 20:40:32 PDT 2019; root:xnu-4903.251.3~3/RELEASE_X86_64 x86_64

$ docker info
Containers: 0
Running: 0
Paused: 0
Stopped: 0
Images: 0
Server Version: 18.09.2
Storage Driver: overlay2
Backing Filesystem: extfs
Supports d_type: true
Native Overlay Diff: true
Logging Driver: json-file
Cgroup Driver: cgroupfs
Plugins:
Volume: local
Network: bridge host macvlan null overlay
Log: awslogs fluentd gcplogs gelf journald json-file local logentries splunk syslog
Swarm: inactive
Runtimes: runc
Default Runtime: runc
Init Binary: docker-init
containerd version: 9754871865f7fe2f4e74d43e2fc7ccd237edcbce
runc version: 09c8266bf2fcf9519a651b04ae54c967b9ab86ec
init version: fec3683
Security Options:
seccomp
Profile: default
Kernel Version: 4.9.125-linuxkit
Operating System: Docker for Mac
OSType: linux
Architecture: x86_64
CPUs: 2
Total Memory: 1.952GiB
Name: linuxkit-025000000001
ID: UJDS:KEB5:OAXE:HHJN:E5SP:XJOH:XBI6:ZRRR:WEZI:C7ZM:SRI2:WDM7
Docker Root Dir: /var/lib/docker
Debug Mode (client): false
Debug Mode (server): true
File Descriptors: 24
Goroutines: 50
System Time: 2019-05-04T05:51:47.88145313Z
EventsListeners: 2
HTTP Proxy: gateway.docker.internal:3128
HTTPS Proxy: gateway.docker.internal:3129
Registry: https://index.docker.io/v1/
Labels:
Experimental: false
Insecure Registries:
127.0.0.0/8
Live Restore Enabled: false
Product License: Community Engine

# -it 参数，交互模式 /bin/sh : Dock容器运行的程序
$ docker run -it busybox /bin/sh
Unable to find image 'busybox:latest' locally
latest: Pulling from library/busybox
fc1a6b909f82: Pull complete
Digest: sha256:954e1f01e80ce09d0887ff6ea10b13a812cb01932a0781d6b0cc23f743a874fd
Status: Downloaded newer image for busybox:latest
/ # ps
PID   USER     TIME  COMMAND
    1 root      0:00 /bin/sh    # PID=1; 是Namespace机制
    6 root      0:00 ps
/ #

PID Namespace, Mount Namespace, UTS Namespace, IPC Namespace, Network Namespace, User Namespace,用来对各种不同的进程上下文进行障眼法操作. 

容器,其实是一种特殊的进程而已.

Hypervisor: 硬件虚拟化，模拟出运行一个操作系统需要的各种硬件，比如CPU、内存、I/O设备。

容器注视运行在宿主机上一种特殊的进程，那么多个容器之间使用的就还是同一个宿主机的操作系统内核. Linux内核中，有很多资源和对象不是能被Namespace化的，最典型的例子就是事件.
Linux Cgroups 就是Linux内核中用来为进程设置资源限制，Linux Control Group就是限制一个进程组使用的资源上限，包括CPU、内存、磁盘、网络带宽.

在Linux中，Cgroups给用户暴露出来的操作接口是文件系统，即以文件和目录的方式组织在操作系统的/sys/fs/cgroup路径下.
$ mount -t cgroup 
cgroup on /sys/fs/cgroup/systemd type cgroup (rw,nosuid,nodev,noexec,relatime,xattr,release_agent=/lib/systemd/systemd-cgroups-agent,name=systemd)
# 设定CPU限制
cgroup on /sys/fs/cgroup/cpu,cpuacct type cgroup (rw,nosuid,nodev,noexec,relatime,cpu,cpuacct)
cgroup on /sys/fs/cgroup/perf_event type cgroup (rw,nosuid,nodev,noexec,relatime,perf_event)
cgroup on /sys/fs/cgroup/net_cls,net_prio type cgroup (rw,nosuid,nodev,noexec,relatime,net_cls,net_prio)
# memory: 为进程设定内存使用的限制
cgroup on /sys/fs/cgroup/memory type cgroup (rw,nosuid,nodev,noexec,relatime,memory)
# cpuset 为鼎城分配单独的CPU核和对应的内存节点
cgroup on /sys/fs/cgroup/cpuset type cgroup (rw,nosuid,nodev,noexec,relatime,cpuset)
# Blkio,为块设备设定I/O限制，一般用于磁盘设备
cgroup on /sys/fs/cgroup/blkio type cgroup (rw,nosuid,nodev,noexec,relatime,blkio)
cgroup on /sys/fs/cgroup/devices type cgroup (rw,nosuid,nodev,noexec,relatime,devices)
cgroup on /sys/fs/cgroup/hugetlb type cgroup (rw,nosuid,nodev,noexec,relatime,hugetlb)
cgroup on /sys/fs/cgroup/freezer type cgroup (rw,nosuid,nodev,noexec,relatime,freezer)
cgroup on /sys/fs/cgroup/pids type cgroup (rw,nosuid,nodev,noexec,relatime,pids)

$ ls /sys/fs/cgroup/cpu
  cgroup.clone_children     cpuacct.usage_percpu_user  init.scope
  cgroup.procs              cpuacct.usage_sys          notify_on_release
  cgroup.sane_behavior      cpuacct.usage_user         release_agent
  cpuacct.stat              cpu.cfs_period_us          system.slice
  cpuacct.usage             cpu.cfs_quota_us           tasks
  cpuacct.usage_all         cpu.shares                 user.slice
  cpuacct.usage_percpu      cpu.stat
  cpuacct.usage_percpu_sys  docker

cpu.cfs_period_us vs cpu.cfs_quota_us : 用来限制在长度为cfs_period的一段时间内，只能分配到总量为cfs_quota的CPU时间.

Linux Cgroups的设计就是在一个子系统目录上加上一组资源限制文件的组合.对于Docker等Linux容器项目来说，他们只需要在每个子系统下面，为每个容器创建一个控制组(即创建一个新目录),然后在启动容器进程之后，把这个进程的PID填写到对应控制组的tasks文件中就可以.

"容器是一个单进程模型"用户的应用进程实际上就是容器里PID=1的进程，也是其他后续的所有进程的父进程，在一个容器中，你不能同时运行两个不同的应用，除非能事先找到一个公共的PID=1的程序来充当两个不同的应用.systemd或者supervisord。 

“容器的设计就是希望容器和应用能够同生命周期”.

Linux下，/proc目录存储的是记录当前内核运行状态的一系列特殊文件,用户可以通过访问这些文件，查看系统以及当前正在运行的进程信息.

"Namespace"作用是隔离，“Cgroups”的作用是限制.

chroot: change root file system改变进程的根目录到你指定的位置.
rootfs:跟文件系统包含的文件、配置和目录，并不包括操作系统内核

Docker项目最核心的原理实际上是为待创建的用户进程：
    1.启动Linux Namespace配置 
    2.设置指定的Cgroups参数
    3.切换进程的根目录Change Root (privot_root | chroot)

实际上，同一台机器上的所有容器，都共享宿主操作系统的内核.对于一个应用来说，操作系统本身才是它运行所需要的最完整的“依赖库”.

Docker 在镜像的设计中，引入了层(layer)的概念，也就是说，用户执行镜像的每一步操作，都会生成一个层，也就是一个增量rootfs.

Union File System: 联合文件系统UnionFS,将多个不同位置的目录联合挂载Union Mount到同一个目录下，
AuFS: Advance UnionFS: 对Linux原生的UnionFS重写和改进

$ docker run -d ubuntu:latest sleep 3600
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
f476d66f5408: Pull complete  # 由四层增量rootfs
8882c27f669e: Pull complete
d9af21273955: Pull complete
f5029279ec12: Pull complete
Digest: sha256:d26d529daa4d8567167181d9d569f2a85da3c5ecaf539cace2c6223355d69981
Status: Downloaded newer image for ubuntu:latest
742d7eef9c942d5435d4425b8125305d98c71f55ea2158154a2ccf99a7c883fb

一个容器的rootfs由三部分组成: 
    可读写层(rw) read write: 在没有写入文件之前，这个目录是空的，而一旦在容器里做了写操作，你修改产生的内容就会以增量的方式出现在这个层中.
    Init层(ro+wh):是Docker项目单独生成一个内部层，专门用来存放/etc/hosts、/etc/resolv.conf等信息; 
    只读层(ro+wh) readonly+whiteout

删除操作，AuFS会在可读写层创建一个whiteout文件，把只读层的文件“遮盖”起来.
Docker commit只会提交可读写层
容器技术"强一致性"的重要体现; 容器镜像的发明，不仅打通了开发-测试-部署流程的每一个环节，“容器镜像将会成为未来软件的主流发布方式”.

copy-on-write: 

Docker on Mac, Windows Docker（Hyper-V）是基于虚拟化技术实现
```

Docker Deploy Python Web App 
----------------------------
* app.py 
```
from flask import Flask 
import socket 
import os 

app = Flask(__name__)

@app.route('/')
def hello():
    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
```
* requirements.txt 
```
Flask 
```
* Dockerfile
```
# 使用官方提供的Python开发镜像最为基础镜像
FROM python:3.7-slim 

# 将工作目录切换到 /app 
WORKDIR /app 

# 将当前目录下的所有app.py, requirements.txt内容复制到 /app下 
ADD . /app 

# 使用 pip 命令安装这个应用所需要的依赖 
RUN pip install --trusted-host pypi.python.org -r requirements.txt 

# 允许外界访问容器的80端口 
EXPOSE 80 

# 设置环境变量 
ENV NAME World 

# 设置容器进程为: python3 app.py, 即: 这个Python应用的启动命令 
CMD ["python3", "app.py"]
```
