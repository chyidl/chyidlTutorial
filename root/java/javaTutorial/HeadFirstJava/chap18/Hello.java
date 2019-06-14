/*
 * Hello.java
 * chap18
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 06/13/19 22:34.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

import java.rmi.Remote;
import java.rmi.RemoteException;

/**
 * Define the remote interface 
 * */
public interface Hello extends Remote {
    
    String sayHello() throws RemoteException;
}

