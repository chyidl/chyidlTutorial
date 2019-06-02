/*
 * RunThreads.java
 * chap15
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/30/19 15:08.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

public class RunThreads implements Runnable {

    public static void main(String[] args)
    {
        // Make one Runnable instance. 
        RunThreads runner = new RunThreads();
        
        // Make two threads, with the same Runnable 
        Thread alpha = new Thread(runner);
        Thread beta = new Thread(runner);
        
        // Name the threads 
        alpha.setName("Alpha thread");
        beta.setName("Beta thread");
        
        // start the threads 
        alpha.start();
        beta.start();
    }

    public void run() {
        // Each thread will run through this loop, printing its name each time.

        for (int i = 0; i < 25; i++) {
            String threadName = Thread.currentThread().getName();
            System.out.println(threadName + " is running");
        }
    }
}

