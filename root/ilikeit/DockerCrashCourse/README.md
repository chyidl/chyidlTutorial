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
![Virtual Machine Diagram image](imgs/ilikeit/DockerCrashCourse/VirtualMachineDiagram.png?raw=true)
```
Container : provides operating-system-level virtualization by abstacting the "user space". The one big difference between containers and VMs is that containers *share* the host system's kernel with other containers. 
```
![Container Diagram image](imgs/ilikeit/DockerCrashCourse/ContainerDiagram.png?raw=true)
```
Docker: a helperful tool for packing, shipping, and running applications within "containers."
```

Guides for Docker
-----------------
