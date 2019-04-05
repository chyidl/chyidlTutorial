package com.chyidl.tutorial;

import java.time.format.SignStyle;

public class LoopTest {

    public static void main(String[] args) {
        int x = 1;

        /**
         * while 循环
         * */
        while (x <= 10) {
            System.out.println("value of x : " + x);
            x++;
        }

        /**
         * do while循环
         * */
        do{
            System.out.println("value of x : " + x);
            x++;
        } while (x < 10);

        /**
         * for 循环
         * */
        for(;x < 20; x++){
            System.out.println("value of x : " + x);
        }

        /**
         * Java 增强for循环
         * */
        int [] numbers = {10, 20, 30, 40, 50};

        for(int number :  numbers){

            if (number == 20) {
                continue; // 让程序立刻跳转到下一次循环迭代
            }

            if (number == 30) {
                break; // 跳出最里面的循环，并且继续执行该循环下面的语句
            }
            System.out.println(number + ", ");

        }

        /**
         * if else 条件语句
         * */
        x = 10;

        if(x == 10) {
            System.out.println("Value of x is 10");
        } else if (x == 20) {
            System.out.println("Value of x is 20");
        } else if (x == 30) {
            System.out.println("Value of x is 30");
        } else {
            System.out.println("这是 else 语句");
        }

        /**
         *  Java switch case语句
         *  swich case语句判断一个变量与一些列值中的某个值是否相等
         *  switch 语句中的变量类型可以是：byte,short,int或者char，
         *  从Java SE7开始，switch支持字符串String类型，同时case标签必须为字符串常量或字面值
         *  switch case执行时，一定会先进行匹配，匹配成功返回当前case值，在根据是否有break，判断是否继续输出，或者跳出判断
         * */

        char grade = 'C';
        switch(grade) {
            case 'A':
                System.out.println("优秀");
                break;
            case 'B':
            case 'C':
                System.out.println("良好");
                break;
            case 'D':
                System.out.println("及格");
                break;
            case 'F':
                System.out.println("需要再努力");
                break;
            default:
                System.out.println("未知等级");
        }
        System.out.println("你的等级是 " + grade);
    }
}
