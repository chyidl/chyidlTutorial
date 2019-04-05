package com.chyidl.tutorial;

import java.sql.Array;
import java.sql.SQLSyntaxErrorException;
import java.util.ArrayList;

/**
 * Java 数组 用来存储固定大小的同类型元素
 * */
public class ArrayTest {

    public static void main(String[] args) {
        // Java 语言使用new操作符来创建数组
        String[] dateArray = new String[10];
        int size = 10; // 数组大小
        double[] myList = new double[size]; // 定义数组
        myList[0] = 5.6;
        myList[1] = 4.5;
        myList[2] = 3.3;
        myList[3] = 13.2;
        myList[4] = 4.0;
        myList[5] = 34.33;
        myList[6] = 34.0;
        myList[7] = 45.45;
        myList[8] = 99.993;
        myList[9] = 11123;
        double total = 0; // 计算所有元素之和
        for (int i = 0; i< size; i++) {
            total += myList[i];
        }
        System.out.println("总和为: " + total);

        /**
         * 处理数组: 数组的元素和数组大小都是确定的，所以当处理数组元素时候，for-Each
         * */
        double[] myList2 = {1.9, 2.9, 3.4, 3.5};

        //打印所有数组元素
        for(int i = 0; i<myList2.length; i++) {
            System.out.println(myList2[i] + " ");
        }

        // 计算所有元素的总和
        total = 0;
        for (int i=0; i < myList2.length; i++) {
            total += myList2[i];
        }
        System.out.println("Total is " + total);

        // 查找最大元素
        double max = myList2[0];
        for (int i=1; i < myList2.length; i++){
            if (myList2[i] > max)
                max = myList2[i];
        }
        System.out.println("Max is " + max);

        /**
         * For-Each 循环 ：加强型循环，能在不使用下标的情况下遍历数组
         * */
        // 打印所有数组元素
        for(double element: myList2) {
            System.out.println(element);
        }

        // 调用printArray方法打印3,1,2,6,4,2
        printArray(new int[] {3,1,2,6,4,2});

        /**
         * Arrays 类
         * java.util.Arrays
         * fill方法，给数组赋值
         * sort方法，给数组排序
         * equals方法，比较数组
         * binarySearch方法，查找数组元素
         * */
    }

    // 数组作为函数参数
    public static void printArray(int[] array) {
        for(int element: array) {
            System.out.println(element);
        }
    }

    // 数组作为函数的返回值
    public static int[] reverse(int[] list) {
        int[] result = new int[list.length];

        for (int i = 0, j = result.length-1; i < list.length; i++, j--) {
            result[j] = list[i];
        }
        return result;
    }
}
