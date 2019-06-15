/*
 * ServiceServerImpl.java
 * UniversalServiceBrowser
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 06/15/19 10:08.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

import java.rmi.*;
import java.util.*;
import java.rmi.server.*;

/**
 * class ServiceServletImpl (the remote implementation)
 * */
public class ServiceServerImpl extends UnicastRemoteObject implements ServiceServer {
    
    /**
     * The services will be stored in a HashMap collection.
     * */
    HashMap serviceList; 

    public ServiceServerImpl() throws RemoteException {
        setUpServices();
    }

    private void setUpServices() {
        serviceList = new HashMap();
        serviceList.put("Dice Rolling Service", new DiceService());
        serviceList.put("Day of the Week Service", new DayOfTheWeekService());
        serviceList.put("Visual Music Service", new MiniMusicService());
    }

    public Object[] getServiceList() {
        System.out.println("in remote");
        /**
         * Client calls this in order to get a list of services to 
         * display in the browser.
         * */
        return serviceList.keySet().toArray();
    }
    
    /**
     * get the corresponding service out of the HashMap
     * */
    public Service getService(Object serviceKey) throws RemoteException {
        Service theService = (Service) serviceList.get(serviceKey);
        return theService;
    }

    public static void main (String[] args) {
        try {
            Naming.rebind("ServiceServer", new ServiceServerImpl());
        } catch (Exception ex) {
            ex.printStackTrace();
        }
        System.out.println("Remote service is running");
    }
}

