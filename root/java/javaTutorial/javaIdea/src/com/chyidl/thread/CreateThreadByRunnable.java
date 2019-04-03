package com.chyidl.thread;

/**
 * Runnable 接口
 * */
class RunnableWriteThread implements Runnable {
    private Thread t;
    private String threadName;
    public static Object lock;


    public RunnableWriteThread(String name, Object lock) {
        this.threadName = name;
        this.lock = lock;
        System.out.println("Creating " + threadName);
    }

    @Override
    public void run(){
        System.out.println("Running " + threadName);
        try{
            for(int i = 4; i > 0; i--) {
                System.out.println("Thread: " +threadName + ", " + i);
                Thread.sleep(50); // 线程睡眠，进入阻塞状态
                // 当睡眠结束，就转为Runnable就绪状态
            }
        }catch (InterruptedException e){
            System.out.println("Thread " + threadName + " interrupted.");
            e.printStackTrace();
        }
        finally{
            //lock.notify();
        }
        System.out.println("Thread " + threadName + " exiting.");
    }

    public void start(){
        System.out.println("Starting " + threadName);
        if (t == null) {
            t = new Thread(this, threadName);
            t.start();
        }
    }

}

class RunnableReadThread implements Runnable {
    private Thread t;
    private String threadName;
    public static Object lock;


    public RunnableReadThread(String name, Object lock) {
        this.threadName = name;
        this.lock = lock;
        System.out.println("Creating " + threadName);
    }

    @Override
    public void run(){
        System.out.println("Running " + threadName);
        try{
           // lock.wait();
            for(int i = 4; i > 0; i--) {
                System.out.println("Thread: " +threadName + ", " + i);
                Thread.sleep(50); // 线程睡眠，进入阻塞状态
                // 当睡眠结束，就转为Runnable就绪状态
            }
        }catch (InterruptedException e){
            System.out.println("Thread " + threadName + " interrupted.");
            e.printStackTrace();
        }
        System.out.println("Thread " + threadName + " exiting.");
    }

    public void start(){
        System.out.println("Starting " + threadName);
        if (t == null) {
            t = new Thread(this, threadName);
            t.start();
        }
    }
}

public class CreateThreadByRunnable {

    public static Object chyi_write_read_lock = new Object();

    public static void main(String args[]){
        RunnableWriteThread chyi_write = new RunnableWriteThread("Thread-write", chyi_write_read_lock);
        chyi_write.start();

        RunnableReadThread chyi_read = new RunnableReadThread("Thread-read", chyi_write_read_lock);
        chyi_read.start();

        System.out.println("Main threading End!");
    }
}
