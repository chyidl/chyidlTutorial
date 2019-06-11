Getting Started Using Java RMI
==============================

> create a distributed version of the classic Hello World program using Java Remote Method Invocation (Java RMI). 
> The distributed Hello World Example uses a simple client to make a remote method invocation to a server which may be running on a remote host. The client receives the "Hello, World!" message from the server. 

* Hello.java - a remote interface 
```
import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Hello extends Remote {
    String sayHello() throws RemoteException;
}
```
* Server.java - a remote object implementation that implements the remote interface
* Client.java - a simple client that invokes a method of the remote interface
