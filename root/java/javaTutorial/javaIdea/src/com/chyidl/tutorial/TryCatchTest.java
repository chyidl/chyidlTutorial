package com.chyidl.tutorial;

import javax.naming.InsufficientResourcesException;
import java.io.FileInputStream;
import java.rmi.RemoteException;

class InsufficientFundsException extends Exception{
    // 此处的amount用来存储当出现异常（取出钱多于余额时）所缺乏的钱
    private double amount;

    public InsufficientFundsException (double amount){
        this.amount = amount;
    }

    public double getAmount(){
        return amount;
    }
}

/**
 * Java 异常处理
 *  异常发生的种类：
 *      用户输入了非法数据
 *      要打开的文件不存在
 *      网络通信时连接中断，或者JVM内存溢出
 *  检查性异常：是由用户错误或问题引起的异常
 *  运行时异常：
 *  错误：
 *
 *  所有的异常是从java.lang.Exception类继承的子类
 *  Exception类是Throwable的子类，除了Exception类外，Throwable还有一个子类Error
 *  Exception主要有两个子类：
 *      IOException:
 *      RuntimeException:
 *
 *  Java语言定义一些异常类在java.lang标准包中
 * */
public class TryCatchTest {
    // balance 为余额，number为卡号
    private double balance;
    private int number;

    public TryCatchTest(int number) {
        this.number = number;
    }

    // 方法：存钱
    public void deposit(double amount){
        balance += amount;
    }

    // 方法：取钱
    public void withdraw(double amount) throws InsufficientFundsException{
        if(amount <= balance){
            balance -= amount;
        } else {
            double needs = amount - balance;
            throw new InsufficientFundsException(needs);
        }
    }

    // 方法： 返回余额
    public double getBalance(){
        return balance;
    }

    // 方法：返回卡号
    public int getNumber(){
        return number;
    }

    public static void main(String[] args){
        /**
         * ArithmeticException: 当出现异常的运算条件时，抛出异常
         * ArrayIndexOutOfBoundsException: 非法索引访问数组抛出异常
         * ArrayStoreException: 试图将错误类型的对象存储到一个对象数组时抛出异常
         * ClassCastException: 试图将对象强制转换为不是实例的子类时，抛出该异常
         * lllegalArgumentException: 向方法传递一个不合法或不正确的参数
         * lllegalMonitorStateException: 抛出异常表明某一线程已经试图等待对象的监视器
         *
         * */
        try {
            int[] a = new int[2];
            System.out.println("Access element three : " + a[2]);
        }catch (ArrayIndexOutOfBoundsException e){
            System.out.println("Exception thrown : " + e);
        }
        System.out.println("Out of the block");

        /**
         * 多重捕获块
         * */

        /**
         * throws/throw关键字
         * */

        /**
         * finally关键字
         * finally关键字用来创建在try代码块后面执行的代码块，无论是否发生异常，finally代码块中的代码总会被执行
         * */

        /**
         * 声明自定义异常
         * 所有异常都必须是Throwable的子类
         * 如果希望写一个检查性异常类，则需要继承Exception类
         * 如果你想写一个运行时异常类，那么需要继承RuntimeException类
         * */

    }
}
