How to Install Python 3 on CentOS6/CentOS7 
------------------------------------------
* Enable Software Collections (SCL)
> Software Collections, also known as SCL is a community project that allows you to build, install, and use multiple versions of software on the same system, without affecting system default packages.
    - $ sudo yum install centos-release-scl 

* Installing Python 3 on CentOS 6/7 
    - $ sudo yum install rh-python36 

* Using Python3 
> To access Python 3.6 you need to launch a new shell instance using the Software Collection scl tool:
    - $ scl enable rh-python36 bash  # What the command does is calling the script /opt/rh/rh-python3.6/enable which changes the shell environment variables.
```
$ python3 
Python 3.6.3 (default, May 14 2019, 16:15:26)
[GCC 4.4.7 20120313 (Red Hat 4.4.7-23)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

* Install Development Tools 
> Development tools are required of building Python modules, you can install the necessary tools and libraries by typing 
    - $ sudo yum groupinstall 'Development Tools'
    
* Creating a Virtual Environment 
> Python virtual Environments allows you to install Python modules in an isolated location for a specific project, rather than being installed globally.
