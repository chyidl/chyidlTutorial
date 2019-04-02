package com.chyidl.thread;

public class MultiThread {
    public static void main(String[] args) {
        // Create two Thread objects
        Thread t1 = new Thread(MultiThread::print);
        Thread t2 = new Thread(MultiThread::print);

        // Start both threads
        t1.start();
        t2.start();
    }

    public static void print() {
        for (int i = 1; i <= 10; i++) {
            System.out.println(i);
        }
    }
}
