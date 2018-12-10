# Unix/Linux Operating System 

The C standard library or **libc** is the standard library for the C programming language, as specified in the ANSI C standard. It was developed at the same time as the C library POSIX specification, which is a superset of it. Since ANSI C was adpted by the International Organization for Standardization, the C standard library is also called the ISO C library.

- [C Standard Library](/root/os/UnixLinux/libc/README.md) 
- [The GNU C Library](/root/os/UnixLinux/glibc/README.md)


## Linux Commands 

- [SSH, also known as Secure Socket Shell](/root/os/UnixLinux/Commands/ssh.md)

## Connect To Ubuntu 18.04 Desktop Via Remote Desktop Connection (RDP) with Xrdp

xrdp is an open source remote desktop protocol server which uses RDP to present a GUI to the client. It provides a fully functional Linux terminal server. capable of accepting connections from rdesktop, frrrdp, and Microsoft's own terminal server/ remote desktop clients.

```
Step 1: Install Xrdp Server 
# To get Ubuntu desktop accepting RDP connections, you must first install and enable Xrdp too... to do that, run the commands below.
$ sudo apt-get install xrdp 
$ sudo systemctl enable xrdp 
# After running the commands below, logout or reboot your desktop. 

Step 2: Connect From Windows 10 
# Now that Xrdp server is installed, go and open Windows Remote Desktop Connection app and connect to teh server IP or hostname.
```
