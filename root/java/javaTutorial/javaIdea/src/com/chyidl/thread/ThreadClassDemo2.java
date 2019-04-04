package com.chyidl.thread;

import java.util.Vector;

/**
 *  通过实现Runnable 接口创建线程
 * */
class WriteMessage2 implements Runnable {
    private String message;
    // private Object lock;
    // 生成零长度的byte[] 只需要3条操作码，Object lock = new Object()需要7行操作码
    Object lock;  // 同步锁

    private Vector<Integer> shareVar;

    // 构造函数 -- 通过构造方法传递数据
    public WriteMessage2(String message, Object lock,Vector<Integer> shareVar) {
        this.message = message;
        // 将传入的数据使用类变量保存起来
        this.lock = lock;
        // this.setShareVar(shareVar);
        this.shareVar = shareVar;
    }

    @Override
    public void run() {
        // 线程同步
        synchronized (lock) {
            try {
                for (int i = 0; i < 10; i++) {
                    shareVar.add(i);
                    Thread.sleep(50); // 保持对象锁，阻塞当前线程
                }
                lock.notify();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        System.out.printf("%s activeCount: %d\n", message, Thread.activeCount());
        System.out.printf("%s %s %s\n", Thread.currentThread().getName(), message, shareVar);
    }
}

/**
 *  通过实现Runnable 接口创建线程
 * */
class DisplayMessage2 implements Runnable {
    private String message;
    //private Object lock;
    Object lock;  // 同步锁
    public Vector<Integer> shareVar;

    // 构造函数
    public DisplayMessage2(String message, Object lock, Vector<Integer> shareVar) {
        this.message = message;
        this.lock = lock;
        this.shareVar = shareVar;
    }

    @Override
    public void run() {
        synchronized (lock) {
            try {
                lock.wait();  // 主动释放对象锁，同时线程休眠
                System.out.printf("%s activeCount: %d\n", message, Thread.activeCount());
                System.out.printf("%s %s %s\n", Thread.currentThread().getName(), message, shareVar);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

public class ThreadClassDemo2 {

    public static Vector<Integer> shareVar = new Vector<Integer>();
    // private static byte[] lock = new byte[0]; // instance 变量


    public static void main(String[] args) {
        System.out.println(Thread.currentThread().getName() + " is Running...");
        long startTime = System.currentTimeMillis(); // 获取开始时间

        Object lock = new Object();  // 同步锁

        WriteMessage2 T1 = new WriteMessage2("WriteMessage", lock, shareVar);
        DisplayMessage2 T2 = new DisplayMessage2("DisplayMessage", lock, shareVar);

        Thread thread2 = new Thread(T2);
        Thread thread1 = new Thread(T1);
        thread2.start();
        thread1.start();

        try {
            thread1.join();
        } catch (InterruptedException e){
            e.printStackTrace();
        }
        try {
            thread2.join();
        } catch (InterruptedException e){
            e.printStackTrace();
        }

        int count = Thread.activeCount();
        System.out.printf("%s activeCount: %d\n", Thread.currentThread().getName(), count);
        Thread th[] = new Thread[count];
        // returns the number of threads put into the array
        Thread.enumerate(th);
        // prints active threads
        for (int i=0; i < count; i++){
            System.out.println(i + ": " + th[i]);
        }

        System.out.println(Thread.currentThread().getName() + " is Ending...");
        System.out.println("程序运行时间: " + (System.currentTimeMillis() - startTime) + "ms");
    }
}
