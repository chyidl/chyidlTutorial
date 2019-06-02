/*
 * DailyAdviceServer.java
 * chap15
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/28/19 11:13.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

import java.io.*;
import java.net.*;

/**
 * This program makes a ServerScoker and waits for client requests. When it gets a client
 * (i.e. client said new Socket() for this application), the server makes a new Socket 
 * connection to that client. The server makes a PrintWriter (using the Socket's output stream) 
 * and sends a message to the client.
 * */
public class DailyAdviceServer {
    
    String[] adviceList = {
        "Take smaller bites", 
        "Go for the right jeans. No they do NOT make you look fat.",
        "One word: inappropriate",
        "Just for today, be honest. Tell your boss what you *really* think",
        "You might want to rethink that haircut."
    };

    public void go() {
        try {
            /**
             * ServerSocket makes this server application "listen" for client
             * requests on port 4242 on the machine this code is running on.
             * */
            ServerSocket serverSock = new ServerSocket(4242);
            
            /**
             * The server goes into a permanent loop,
             * waitting for (and servicing) client requests 
             * */
            while (true) {
                /**
                 * The accept method blocks (just sits there) until a request comes in, and then the method returns a Socket
                 * (on some anonymous Port) for communicating with the client 
                 * */
                Socket sock = serverSock.accept();

                PrintWriter writer = new PrintWriter(sock.getOutputStream());
                String advice = getAdvice();

                /**
                 * we use the Socket connection to the client to make a PrintWriter and send it 
                 * (println()) a String advice message. Then we close the Socket because we're 
                 * done with this client.
                 * */
                writer.println(advice);
                writer.close();
                
                System.out.println(advice);
            } 
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }

    private String getAdvice() {
        int random = (int) (Math.random() * adviceList.length);
        return adviceList[random];
    }

    public static void main(String[] args)
    {
        DailyAdviceServer server = new DailyAdviceServer();
        server.go();
    }
}

