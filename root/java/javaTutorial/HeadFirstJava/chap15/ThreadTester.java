/*
 * ThreadTester.java
 * chap15
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/28/19 14:33.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

/**
 * The three states of a new thread 
 *      1. Thread t = new Thread(r);  NEW 
 *      2. t.start();   RUNNABLE 
 *      3. Selected to run RUNNING
 * */

public class ThreadTester {

    public static void main(String[] args)
    {
        /**
         * Pass the new Runnable instance into the new Thread constructor. 
         * This tells the thread what method to put on the bottom of the 
         * new stack. In other words, the first method that the new thread will run.
         * */
        Runnable threadJob = new MyRunnable();
        // A Thread instance has been created but not started.
        Thread myThread = new Thread(threadJob);
        
        /**
         * You won't get a new thread of execution until you call start() on the Thread
         * instance. A thread is not really a thread until you start it.
         * Before that, it's just a Thread instance, like any other object,
         * but it won't have any real 'threadness'.
         * */
        myThread.start();

        System.out.println("back in main");
    }
}

