package com.chyidl.thread;

/**
 *
 * */
class ChyiThread extends Thread {
    private Thread t;
    private String threadName;

    public ChyiThread(String name) {
        threadName = name;
        System.out.println("Creating " + threadName);
    }

    @Override
    public void run() {
        System.out.println("Running " + threadName);
        try {
            for(int i = 4; i > 0; i--) {
                System.out.println("Thread: " + threadName + ", " + i);
                // 不让当前线程独占该进程所获的的CPU资源，已留出一定时间给其它线程执行的机会
                Thread.sleep(50);
            }
        }catch (InterruptedException e) {
            System.out.println("Thread " + threadName + " exiting.");
        }
    }

}

public class CreateThreadByThread {

    public static void main(String args[]) {
        System.out.println(Thread.currentThread().getName() + " Thread Running...");

        ChyiThread T1 = new ChyiThread("Thread-1");
        // 更改线程的优先级
        T1.setPriority(Thread.MAX_PRIORITY);
        // start()方法调用并不是立即执行多线程代码，而是使得该线程编程可运行状态Runnable,
        // 什么时候运行由操作系统决定
        T1.start();
        try {
            T1.join();
        }catch (InterruptedException e){
            e.printStackTrace();
        }

        System.out.println(Thread.currentThread().getName() + " Thread Ending...");
    }
}
