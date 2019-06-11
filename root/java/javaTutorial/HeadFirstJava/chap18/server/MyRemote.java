/*
 * MyRemote.java
 * server
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 06/11/19 11:23.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

// RemoteException and Remote interface are in java.rmi package
import java.rmi.*;

// Make a Remote Interface
// You interface must extend java.rmi.remote
public interface MyRemote extends Remote {

    // All of your remote methods must declare a RemoteException
    public String sayHello() throws RemoteException;

}

