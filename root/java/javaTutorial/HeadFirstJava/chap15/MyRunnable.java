/*
 * MyRunnable.java
 * chap15
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/28/19 14:27.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

/**
 * Runnable is in the java.lang package, so you don't need to import it.
 * */
public class MyRunnable implements Runnable {
    
    /**
     * Runnable has only one method to implement:
     *      public void run()
     * This is where you put the Job the thread is supposed to run.
     * This is the method that goes at the bottom of the new stack.
     * */
    public void run() {
        go();
    }

    public void go() {

        /**
         * Calling sleep here will force the new thread to leave the currently-running state!
         * */
        try {
            Thread.sleep(2000);
        } catch (InterruptedException ex) {
            ex.printStackTrace();
        }
        doMore(); 
    }

    public void doMore() {
        System.out.println("top o' the stack");
    }
}

