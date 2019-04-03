package com.chyidl.thread;


import javax.print.DocFlavor;

/**
 * 三线程打印ABC的问题
 *  A 线程打印10次A
 *  B 线程打印10次B
 *  C 线程打印10次C
 *  要求线程同时运行，交替打印10次ABC
 * */
public class ThreeThreadPrint implements Runnable {
    private  String name;
    private Object prev;
    private Object self;

    private ThreeThreadPrint(String name, Object prev, Object self) {
        this.name = name;
        this.prev = prev;
        this.self = self;
    }

    @Override
    public void run() {
        int count = 10;
        while (count > 10) {
            synchronized (prev) {
                synchronized (self) {
                    System.out.print(name);
                    count--;
                    self.notify();
                }
                try{
                    prev.wait();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
    }

//    public void start(){
//        if (t == null) {
//            t = new Thread(this);
//            t.start();
//        }
//    }

    public static void main(String[] args) throws Exception {
        Object a = new Object();
        Object b = new Object();
        Object c = new Object();

        ThreeThreadPrint pa = new ThreeThreadPrint("A", c, a);
        ThreeThreadPrint pb = new ThreeThreadPrint("B", a, b);
        ThreeThreadPrint pc = new ThreeThreadPrint("C", b, c);

        new Thread(pa).start();
        Thread.sleep(100);
        new Thread(pb).start();
        Thread.sleep(100);
        new Thread(pc).start();
        Thread.sleep(100);

    }
}
