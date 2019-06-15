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
 * Created by Chyi Yaqing on 06/13/19 22:39.
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
            // null: local address
            Registry registry = LocateRegistry.getRegistry(host);
            Hello stub = (Hello) registry.lookup("sayHello");
            /**
             * The client-side runtime opens a connection to the server using the host and port information in the remote object's stub and then serializes the call data.
             * The server-side running accepts the incoming call, dispatching the call to the remote object, and serializes the result to the client.
             * The client-side runtime receives, deserializes,and returns the result to the caller.
             * */
            String response = stub.sayHello();
            System.out.println("response: " + response);
        } catch (Exception e) {
            System.out.println("Client exception: " + e.toString());
            e.printStackTrace();
        }
    }
}

