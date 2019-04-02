package com.chyidl.thread;


/**
 * Java两种线程同步
 *      互斥同步，同一个时间点只允许一个线程访问代码段
 *      条件同步，通过条件变量和三个操作实现，等待，信号和广播
 * */
public class MultiThreadSynchronized {
    public synchronized void someMethod_1() {
        // Method code goes here
    }

    public static synchronized void someMethod_2() {
        // Method code goes here
    }
}
