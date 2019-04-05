package com.chyidl.tutorial;

import java.util.stream.StreamSupport;

/**
 * Java方法是语句的集合，一起执行一个功能
 *  方法是解决一类问题的步骤的有序组合
 *  方法在程序中被创建，在其他地方被引用
 * 方法命名规则：
 *      方法的名称的第一个单词应以小写字母开头，后面的单词则大写字母开头，不使用连接符
 *      下划线可能出现在JUnit测试方法名称中，用以分隔名称的逻辑组件
 * */
public class MethodTest {

    // 返回两个整型变量数据的较大值
    public static int max(int num1, int num2) {
        return  num1 > num2 ? num1 : num2;
    }

    // 方法的重载
    public static double max(double num1, double num2) {
        return num1 > num2 ? num1 : num2;
    }

    // main方法是被JVM调用
    public static void main(String[] args){
        int i=5, j=2;
        int k = max(i, j);
        System.out.println(i + " 和 " + j + " 比较，最大值是: " + k);

        printGrade(78.5);

        int num1 = 1, num2 = 2;
        System.out.println("交换前 num1 的值为: " + num1 + " , num2 的值为: " + num2);

        // 调用swap方法
        swap(num1, num2);
        System.out.println("交换后 num1 的值为: " + num1 + ", num2 的值为: " + num2);
    }

    // printGrade方法是void方法，不返回值
    public static void printGrade(double score) {
        if (score >= 90.0) {
            System.out.println('A');
        } else if (score >= 80.0) {
            System.out.println('B');
        } else if (score >= 70.0) {
            System.out.println('C');
        } else if (score >= 60.0) {
            System.out.println('D');
        } else {
            System.out.println('F');
        }
    }

    public static void swap(int n1, int n2){
        System.out.println("\t进入 swap 方法");
        System.out.println("\t\t交换前 n1 的值为: " + n1 + ", n2的值: " + n2);
        // 交换 n1 与 n2的值
        int temp = n1;
        n1 = n2;
        n2 = temp;
        System.out.println("\t\t交换后 n1 的值为 " + n1 + ", n2 的值: " + n2);
    }
}
