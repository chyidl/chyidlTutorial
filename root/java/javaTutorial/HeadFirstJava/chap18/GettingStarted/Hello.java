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

// Define the remote interface
public interface Hello extends Remote {
    
    String sayHello() throws RemoteException;
}

