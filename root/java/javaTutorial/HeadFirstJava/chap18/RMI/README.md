Getting Started with Java RMI
==============================
> RMI stands for Remote Method Invocation and it is the object-oriented equivalent of RPC (Remote Procedure Calls). RMI was designed to make the interaction between applications using the object-oriented model and run on different machines seem like that of stand-alone programs.

> RMI is used to build distributed applications; it provides remote communication between Java programs. It is provided in the package java.rmi.

Architecture of an RMI Application 
----------------------------------
```
Designing and Implementing the Application Components
    1. Define the remote Interfaces: - A remote interface specifies the methods that can be invoked remotely by a client.  
    2. Implement the remote objects: - Remote objects must implement one or more remote interfaces.
    3. Implement the clients: - 

        Client                              Server 
          ^                                   ^
          |                                   |
          V                                   V
         Stub                              Skeleton
          ^                                   ^
          |                                   |
          V                                   V
         RRL    <__ Virtual connection __>   RRL
          ^                                   ^
          |                                   |
          V                                   V
  Transport Layer <_ Network Connection _> Transport Layer 

Transport Layer - This layer connects the client and ther server. It manages the existing connection and also sets up new connections. 

Stub - A stub is a representation (proxy) of the remote object at client. It resides in the client system, it acts as a gateway for the client program 

Skeleton - This is the object which resides on the server side. Stub communications with this skeleton to pass request to the remote object. 

RRL (Remote Reference Layer) - It is the layer which manage the reference made by the client to the remote object.

Running an RMI application 
    Complie the application 
    Execute the application 
    1. Run rmiregistry 
    2. Run the server 
    3. Run the client 
```

Define The Remote Interface
---------------------------
> A remote interface provides the description of all the methods of a particular remote object.
* Hello.java - a remote interface 
```
/*
 * Hello.java
 * GettingStarted
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 06/11/19 15:08.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

import java.rmi.Remote;
import java.rmi.RemoteException;

// A rmeote object is an instance of a class that 
// implements a remote interface.
public interface Hello extends Remote {
    
    // Each remote method must declare java.rmi.RemoteException
    String sayHello() throws RemoteException;
}
```

Implement the server
--------------------
* Server.java - a remote object implementation that implements the remote interface
```
/*
 * Server.java
 * GettingStarted
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 06/11/19 15:12.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

import java.rmi.registry.Registry;
import java.rmi.registry.LocateRegistry;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class Server implements Hello {

    public Server() {}

    public String sayHello() {
        return "Hello, world!";
    }

    public static void main(String[] args)
    {
        try {
            // Create and export a remote object
            Server obj = new Server();
            /**
             * The static method UnicastRemoteObject.exportObject exports the supplied remote object
             * to receive incoming method invocations on an anonymous TCP port and returns the stub
             * for the remote object to pass to clients.
             * */
            Hello stub = (Hello) UnicastRemoteObject.exportObject(obj, 0);

            // Register the remote object with a Java RMI registry
            Registry registry = LocateRegistry.getRegistry();
            registry.bind("Hello", stub);

            System.err.println("Server ready");
        } catch (Exception e) {
            System.err.println("Server exception: " + e.toString());
            e.printStackTrace();
        }
    }
}
```

Implement the client
--------------------
* Client.java - a simple client that invokes a method of the remote interface
```
/*
 * Client.java
 * chap18
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 06/12/19 10:19.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Client {

    private Client() {}

    public static void main(String[] args)
    {
        String host = (args.length < 1) ? null : args[0];
        try {
            // obatin the stub for the registry
            Registry registry = LocateRegistry.getRegistry(host);
            Hello stub = (Hello) registry.lookup("Hello");
            /**
             * the client invokes the sayHello method on the remote object's stub, 
             * which causes the following actions to happen:
             *  1. The client-side runtime opens a connection to the server using 
             *      the host and port information in the remote object stub and 
             *      then serializes the call data.
             *  2. The server-side runtime accepts the incoming call, dispatches 
             *      the call to the remote object, and serializes the result 
             *      (the reply string "Hello, world!") to the client.
             *  3. The client-side runtime receives, deserilizes, and returns the result to the caller.
             * */
            String response = stub.sayHello();
            System.out.println("response: " + response);
        } catch (Exception e) {
            System.err.println("Client exception: " + e.toString());
            e.printStackTrace();
        }
    }
}
```

Start the application running the RMI remote object registry,the server, and the client.
----------------------------------------------------------------------------------------
```
# Compiling Sources 

Note: With versions prior to Java platform, Standard Edition 5.0, an additonal step was required to build stub classes, by using the rmic compiler. However, this step is no longer necessary.

$ javac -d destDir Hello.java Server.java Client.java  # where destDir is the desrination directory to put the class files in 

# Start the Java RMI registry 
# To start the registry, run the rmiregistry command on the server's host. This command produces no output (when successful) and is typically run in the background.
# RMI Registry: is a namespace on which all server objects are placed. 
$ rmiregistry # run the rmiregistry command on the server host.

# Start the server 
# To start the server, run the Server class using the java command as follows:
$ java -classpath classDir -Djava.rmi.server.codebase=file:classDir/ Server 

# Run the client
# Once the server is ready, the client can be run as follows:
$ java -classpath classDir Client 
```
