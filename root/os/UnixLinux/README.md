GNU/Linux Operating System 
==========================

The GNU Manifesto
-----------------

* What's GNU? Gnu's Not Unix!
    GNU, which stands for Gnu's Not Unix, is the name for the complete Unix-compatible software system. 
    The GNU Project set out to develop a complete free Unix-like system: GNU 
    Once Trovalds freed Linux in 1992, it fit into the last major gap in the GNU system. People could then combine Linux with the GNU system to make a complete free system -- a version of the GNU system which also contained Linux. The GNU/Linux system, in other words. 

Linux and the GNU System
------------------------

Linux is the kernel: the program in the system that allocates the machine's resources to the other programs that you run. The kernel is an essential part of an operating system, but useless by itself; it can only function in the context of a complete operating system. Linux is normally used in combination with the GNU operating system: the whole system is basically GNU with Linux added. or GNU/Linux. All the so-called "Linux" distributions are really distributions of GNU/Linux.

Today there are many different variants of the GNU/Linux system (often called "distros"). 

Add a User to a Group on Linux
------------------------------
```
# add a New Group 
$ sudo groupadd mynewgroup 

# Add an existing User Account to a Group 
$ sudo usermod -a -G examplegroup exampleusername 

# Change a User's Primary Group 
# While a user account can be part of multiple groups, one of the groups is alwasys the "primary group" and the others are "secondary groups".
$ sudo usermod -g groupname username 

# View the Groups a User Account is Assigned To 
$ groups 

# To View the numericial IDs associated with each group, run the id command instead.
$ id 

# View All Groups on the System
$ getent group 
```
