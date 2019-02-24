Build a Supercomputer with Raspberry Pi's
=========================================
How to create your own Raspberry Pi cluster for parallel computing via MPI(Messaging Passing Interface) library. Message Passing Interface(MPI) is a standardized and portable message-passing standard designed to exchange messages between multiple computers running a parallel program across distributed memory.

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

How to Build Raspberry Pi Supercomputer With Raspberry Pi Cluster?
------------------------------------------------------------------
```
2+ Raspberry Pis, One of the Pis will be the master node, the rest are worker nodes.
    $ cat /etc/os-release 
PRETTY_NAME="Raspbian GNU/Linux 9 (stretch)"
NAME="Raspbian GNU/Linux"
VERSION_ID="9"
VERSION="9 (stretch)"
ID=raspbian
ID_LIKE=debian
HOME_URL="http://www.raspbian.org/"
SUPPORT_URL="http://www.raspbian.org/RaspbianForums"
BUG_REPORT_URL="http://www.raspbian.org/RaspbianBugs"

In this case, select Python, as it has plenty of libraries available and also a nice integration with MPI via **mpi4py** library.
```

Installing MPICH3
-----------------
```
# Downloading and installing MPICH3 (install version 3.3)
# MPICH, the MPI iplementation from Argonne National Laboratory.
    $ sudo apt-get update  			# update the system 
    $ sudo apt-get dist-upgrade  	# update packages 
	# create the folder for mpich3
    $ sudo mkdir mpich3 && cd ~/mpich3   
    # download the version 3.2 of mpich 
	$ sudo wget http://www.mpich.org/static/downloads/3.3/mpich-3.3.tar.gz 
    $ sudo tar xfz mpich-3.3.tar.gz  # Unpack the tar file
	# create folders for mpi
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
	# Test that MPI works 
	$ mpiexec -n 1 hostname 
```

Installing mpi4py
-----------------
```
	# These steps will allow you to install MPI4py to your Raspbian stretch distro
	$ sudo apt-get install python3-mpi4py 
	[helloworld.py](/root/raspberrypi/RaspberryPiPrj/Supercomputer/mpi_helloworld.py)
	# Test that MPI works on your device 
	$ mpiexec -n 5 python3 mpi_helloworld.py
Hello world from process 0 at RPi3B.
Hello world from process 0 at RPi3B.
Hello world from process 0 at RPi3B.
Hello world from process 0 at RPi3B.
```

Configuring SSH keys for each RPi
---------------------------------
```
you need to be able to command each RPi without using users/passwords. To do this, you will have to generate SSH keys for each RPi and then share each key to each device under authroized devices. By doing this, MPI will be able to communicate with each device without bothering about credentials. 
	# Setting up SSH 
# Check that you can reach these machine with ssh or rsh without entering a password
    $ ssh-keygen -t 'rsa' -C 'mpi-master'
    $ ssh-copy-id mpi@mpi-node_public_ip
    # test by doing below, if you cannot get this to work without entering a password, you will need to configure ssh or rsh so that this can be done. 
    $ ssh othermachine date 


# Test the setup you just created:
    # A machinefile is a file that contains a list of the possible machine on which you want your MPI program to run.
    $ mpiexec -f machinefile -n <number> hostname
	# add the following IP address(or hostname). This will be used by the MPICH3 to communicate and send/receive messages between various nodes.
    $ vim machinefile 
        host1:4  # Run 4 process on host1
        host2:4  # Run 4 processes on host2
	# Testing the cluster (If everything is configured correctly, the following command should work fine)
	$ mpiexec -f mpi_machinefile -n 8 hostname
RPi3B
RPi3B
RPi3B
RPi3B
RPi2B
RPi2B
RPi2B
RPi2B
```

Now, your system is ready to take any parallel computing application that you wnat to develop.
