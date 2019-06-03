/*
 * TestSync.java
 * chap15
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 06/03/19 10:57.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

/**
 * The "Lost Update" problem 
 * */

public class TestSync implements Runnable {
    
    private int balance;
    
    public void run() {
        // Each thread runs 50 times incrementing the balance on each iteration
        for (int i = 0; i < 50; i++) {
            increment();
            System.out.println("balance is " + balance);
        }
    }

    /**
     * Synchronizing the increment() method solves the "Lost Update" problem
     * because it keeps the two steps in the method as one unbreakable unit.
     * */
    public synchronized void increment() {
        int i = balance;
        /**
         * Here's the crucial part! We increment the balance by 
         * adding I to whatever the value of balance was AT The
         * Time We Read It (rather than adding I to whatever the 
         * current value is)
         * */
        balance = i + 1;
    }
}

