package com.chyidl.tutorial;

import java.util.Scanner;
import java.util.stream.StreamSupport;

/**
 * Java Scanner类 可以获取用户的输入
 */

public class ScannerTest {
    public static void main(String[] args) {
        // 创建Scanner对象
        Scanner scan = new Scanner(System.in);
        // 从键盘接收数据
        // next方式接收字符串
        System.out.println("next方式接收: ");
        // 判断是否还有输入
        if (scan.hasNext()){
            // 一定要读取到有效字符后才可以结束输入
            // 对输入有效字符之前遇到的空白，next()方法会自动将其去掉
            // next不能得到带有空格的字符串
            String str1 = scan.next();
            System.out.println("输入的数据为: " + str1);
        }
        scan.close();

        // nextLine方法接收字符串
        scan = new Scanner(System.in);
        System.out.println("nextLine方式接收: ");
        // 判断是否还有输入
        if (scan.hasNextLine()) {
            // 以Enter结束，返回的是输入回车之前的所有字符
            // 可以获得空白
            String str2 = scan.nextLine();
            System.out.println("输入的数据为: " + str2);
        }
        scan.close();
    }
}
