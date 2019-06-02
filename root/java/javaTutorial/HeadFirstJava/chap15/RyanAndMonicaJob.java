/*
 * RyanAndMonicaJob.java
 * chap15
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/30/19 15:41.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

public class RyanAndMonicaJob implements Runnable {
    
    /**
     * Both threads will access this one account.
     * */
    private BankAccount account = new BankAccount();

    public static void main(String[] args)
    {   
        // Instantiate the Runnable (job)
        RyanAndMonicaJob theJob = new RyanAndMonicaJob();
        
        /**
         * Make the threads, giving each thread the same Runnable job. 
         * That means both threads will be accessing the one account instance variable in the Runnable class
         * */
        Thread one = new Thread(theJob);
        Thread two = new Thread(theJob);

        one.setName("Ryan");
        two.setName("Monica");

        one.start();
        two.start();
    }

    public void run() {
        
        for (int x = 0; x < 10; x ++) {
            makeWithdraw1(10);
            if (account.getBalance() < 0) {
                System.out.println("Overdrawn!");
            }
        }
    }

    private void makeWithdraw1(int amount) {
        if (account.getBalance() >= amount) {
            System.out.println(Thread.currentThread().getName() + " is about to withdraw");
            try {
                System.out.println(Thread.currentThread().getName() + " is going to sleep");
                Thread.sleep(500);
            } catch (InterruptedException ex) {
                ex.printStackTrace();
            }
            System.out.println(Thread.currentThread().getName() + " work up.");
            account.withdraw(amount);
            System.out.println(Thread.currentThread().getName() + " completes the withdraw1");
        } else {
            System.out.println("Sorry, not enough for " + Thread.currentThread().getName());
        }
    }
}

