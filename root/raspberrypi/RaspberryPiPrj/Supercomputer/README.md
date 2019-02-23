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

Running an MPI CLuster within a LAN on Raspberry Cluster
---------------------------------------------------
```
2+ Raspberry Pis, One of the Pis will be the master node, the rest are worker nodes.

Step 1: Configure your hosts file 
    $ cat /etc/hosts 

Downloading and installing MPICH3 
MPICH, the MPI iplementation from Argonne National Laboratory.
    $ sudo apt-get update  # update the system 
    $ sudo apt-get dist-upgrade  # update packages 
    $ sudo mkdir mpich3 && cd ~/mpich3  # create the folder for mpich3 
    $ sudo wget http://www.mpich.org/static/downloads/3.3/mpich-3.3.tar.gz  # download the version 3.3 of mpich 

# From a Standing Start to Running an MPI program 

    $ sudo tar xfz mpich-3.3.tar.gz  # Unpack the tar file
    $ mkdir ~/mpich-install  # Choose an installation directory (the default is /usr/local/bin)
    $ mkdir ~/mpich-build  # Choose a build directory 
    # Configure MPICH, specifying the installation directory, and running the configure script in the source directory, c.txt is created by configure and contains a record of the tests that configure performed.
    $ cd ~/mpich-build && ~/mpich-3.3/configure --prefix=~/mpich-install --disable-fortran |& tee c.txt 
    $ make -j2 2>&1 | tee m.txt  # Build MPICH (for bash and sh)
    $ make install |& tee mi.txt  # Install the MPICH commands 
    # Add the bin subdirectory of the installation directory to your path:
    $ PATH=~/mpich-install/bin:$PATH && export PATH 
    # Check that you can reach these machines with ssh or rsh without entering a password.
    $ which mpicc && which mpiexec 

Step 3: Setting up SSH 
# Check that you can reach these machine with ssh or rsh without entering a password
    $ ssh-keygen -t 'rsa' -C 'mpi-master'
    $ ssh-copy-id mpi@mpi-node_public_ip
    # test by doing below, if you cannot get this to work without entering a password, you will need to configure ssh or rsh so that this can be done. 
    $ ssh othermachine date 

Step 4: Setting up NFS
    You share a directory via NFS in master which the client mounts to exchange data.


# Test the setup you just created:
    # A machinefile is a file that contains a list of the possible machine on which you want your MPI program to run.
    $ mpiexec -f machinefile -n <number> hostname
    $ cat machinefile 
        host1   # Run 1 process on host1
        host2:4 # Run 4 processes on host2
        host3:2 # Run 2 processes on host3 
```
