package com.chyidl.thread;

/**
 * 三线程打印ABC的问题
 *  A 线程打印10次A
 *  B 线程打印10次B
 *  C 线程打印10次C
 *  要求线程同时运行，交替打印10次ABC
 * */
public class ThreeThreadPrint implements Runnable {
    private String name;
    private Object prev;
    private Object self;

    private ThreeThreadPrint(String name, Object prev, Object self) {
        this.name = name;
        this.prev = prev; // 前一个对象的同步锁
        this.self = self; // 自身对象的同步锁
    }

    @Override
    public void run() {
        int count = 10;
        while (count > 0) {
            synchronized (prev) {  // 先持有前一对象锁
                synchronized (self) { // 持有自身锁
                    System.out.println(name);
                    count--;
                    self.notify(); // 释放自身对象锁，唤醒下一个等待线程
                }
                try{
                    prev.wait(); // 释放前一个对象线程锁
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    public static void main(String[] args) throws Exception {
        // JVM调度程序main创建的线程
        System.out.println(Thread.currentThread().getName() + " Starting...");

        Object a = new Object();
        Object b = new Object();
        Object c = new Object();

        ThreeThreadPrint pa = new ThreeThreadPrint("A", c, a);
        ThreeThreadPrint pb = new ThreeThreadPrint("B", a, b);
        ThreeThreadPrint pc = new ThreeThreadPrint("C", b, c);

        Thread threadA = new Thread(pa);
        Thread threadB = new Thread(pb);
        Thread threadC = new Thread(pc);

        // 三个线程按照A，B，C的顺序启动，这种假设依赖JVM中线程调度、执行的顺序
        threadA.start();
        threadB.start();
        threadC.start();

        try {
            threadA.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println(Thread.currentThread().getName() + " End...");
    }
}
