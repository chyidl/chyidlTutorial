/*
 * MyRemoteImpl.java
 * server
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 06/11/19 11:27.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

import java.rmi.*;
import java.rmi.server.*;

// Make a Remote Implementation
public class MyRemoteImpl extends UnicastRemoteObject implements MyRemote {
    
    public String sayHello() {
       return "Server says, 'Hey'";
    }

    public MyRemoteImpl() throws RemoteException {}

    public static void main (String[] args) {
        
        try {
            MyRemote service = new MyRemoteImpl();
            // Register the service with the RMI registry
            Naming.rebind("Remote Hello", service);
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
}

