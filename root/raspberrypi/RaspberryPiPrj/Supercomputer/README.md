Build a Supercomputer with Raspberry Pi's
=========================================

If you've build and own a supercomputer is not enough, that's fine. you will also learn about networking and parallel processing.

Parallel Computing
------------------
```
Solving small parts of a greater problem in a synchronized fashion. 

FLOPS: Floating Point Operations Per Second
FLOPs: # of floating Point operations (not per second.)
GPU: stands for general purpose graphics processing unit 

Main Types of SUpercomputers:
    Clusters:
        Nodes close to eachother in procimity 

    Distributed:
        Nodes spread around, usually connected via TCP/IP (the internet)

Bitcoin network is the largest supercomputing network: No central server, as the Bitcoin network's purpose is to be decentralized server,and this is what the power is focused on.
    
    Communication is important!
        MPI - Message Passing Interphase, Share data, variables, and work in a synchronized fashion.
```

What's you'll need to build your own supercomputer.
---------------------------------------------------
```
2+ Raspberry Pis, One of the Pis will be the master node, the rest are worker nodes.

Downloading and installing MPICH3 
    $ sudo apt-get update  # update the system 
    $ sudo apt-get dist-upgrade  # update packages 
    $ sudo mkdir mpich3 && cd ~/mpich3  # create the folder for mpich3 
    $ sudo wget http://www.mpich.org/static/downloads/3.3/mpich-3.3.tar.gz  # download the version 3.3 of mpich 
    $ sudo tar xfz mpich-3.3.tar.gz  # unzip it  
    $ mkdir ~/mpich-install  # Choose an installation directory (the default is /usr/local/bin)
    $ mkdir ~/mpich-build  # Choose a build directory 
    # Configure MPICH, specifying the installation directory, and running the configure script in the source directory
    $ cd ~/mpich-build && ~/mpich-3.3/configure --prefix=~/mpich-install --disable-fortran 
    $ make -j2 2>&1 | tee m.txt  # Build MPICH (for bash and sh)
    $ make install |& tee mi.txt  # install the MPICH commands 
    # Add the bin subdirectory of the installation directory to your path:
    $ PATH=~/mpich-install/bin:$PATH && export PATH 
    # Check that you can reach these machines with ssh or rsh without entering a password.
    $ 
    
    
```
