/*
 * Server.java
 * chap18
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 06/13/19 22:35.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

import java.rmi.registry.Registry;
import java.rmi.registry.LocateRegistry;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

/**
 * Implement the server
 * A "Server" class, in this context, is the class which has a main method
 * that creates an instance of the remote object implementation, exports 
 * the remote object, and the binds that instance to a name in a Java RMI registry.
 * */
public class Server implements Hello {
    
    public Server(){}
    
    @Override
    public String sayHello() {
        return "Hello, world!";
    }

    public static void main(String[] args)
    {
        try {
            // Create an export a remote object
            Server obj = new Server();
            //  
            Hello stub = (Hello) UnicastRemoteObject.exportObject(obj, 0);

            // Bind the remote object's stub in the registry 
            Registry registry = LocateRegistry.getRegistry(); // default port of 1099
            registry.bind("sayHello", stub);

            System.err.println("Server ready");
        } catch (Exception e) {
            System.err.println("Server exception: " + e.toString());
            e.printStackTrace();
        }
    }
}

