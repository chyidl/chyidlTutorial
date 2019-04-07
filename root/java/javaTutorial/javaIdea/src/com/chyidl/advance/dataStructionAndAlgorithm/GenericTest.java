package com.chyidl.advance.dataStructionAndAlgorithm;

import java.util.ArrayList;
import java.util.List;

/**
 * Java泛型generics
 * 泛型提供编译时类型安全检查，该机制允许程序员在编译时检测到非法的类型
 * 泛型的本质是参数化类型，
 *
 * 所有泛型方法声明都有一个类型参数声明部分，该类型参数声明部分在方法返回类型之前
 * 每一个类型参数声明部分包含一个或多个类型参数，参数间逗号隔开，一个泛型参数，也就称为一个类型变量，是用于指定一个泛型类型名称的标识符
 * 类型参数能被用来声明返回值类型，并且能作为泛型方法得到的实际参数类型的占位符
 * 泛型方法体的声明和其他方法一样，注意类型参数只能代表引用型类型，不能是原始类型
 *
 * 有界类型参数：
 * 声明一个有界的类型参数，首先列出类型参数的名称，后跟extends关键字，最后紧跟它的上界
 *
 * 泛型类的声明和非泛型类的声明类似，除了在类名后面添加类型参数声明部分
 * 和泛型方法一样，泛型类的类型参数声明部分也包含一个或多个类型参数，参数间逗号隔开，一个泛型参数也被称为一个类型变量，是用于指定一个泛型类型名称的标识符，
 *
 * 类型通配符一般是使用?代替具体类型参数
 * */

class Box<T>{
    private T t;

    public void add(T t){
        this.t = t;
    }

    public T get(){
        return t;
    }
}

public class GenericTest {

    // 泛型方法 printArray
    public static <E> void printArray(E[] inputArray){
        // 输出数组元素
        for(E element: inputArray){
            System.out.printf("%s ", element);
        }
        System.out.println();
    }

    // 比较三个值并返回最大值
    public static <T extends Comparable<T>> T maximum(T x, T y, T z){
        T max = x; // 假设x是初始最大值
        if(y.compareTo(max) > 0) {
            max = y; // y更大
        }
        if (z.compareTo(max) > 0){
            max = z; // 现在z最大
        }
        return max; //返回最大对象
    }

    public static void main(String[] args){

        // 创建不同类型数组: Integer, Double 和 Character
        Integer[] intArray = {1, 2, 3, 4, 5};
        Double[] doubleArray = {1.1, 2.2, 3.3, 4.4, 5.5};
        Character[] charArray = {'H', 'E', 'L', 'L', 'O'};

        System.out.println("整形数组元素为:");
        printArray(intArray); // 传递一个整型数组

        System.out.println("\n双精度型数组元素为:");
        printArray(doubleArray); // 传递一个双精度型数组

        System.out.println("\n字符型数组元素为:");
        printArray(charArray); // 传递一个字符型数组

        System.out.printf("%d, %d 和 %d 中最大的数为 %d\n\n", 3, 4, 5, maximum(3, 4, 5));
        System.out.printf("%.1f, %.1f 和 %.1f 中最大的数为 %.1f\n\n", 6.6, 8.8, 7.7, maximum(6.6, 8.8, 7.7));
        System.out.printf("%s, %s 和 %s 中最大的数为 %s\n", "pear", "apple", "orange", maximum("pear", "apple", "orange"));

        Box<Integer> integerBox = new Box<Integer>();
        Box<String> stringBox = new Box<String>();

        integerBox.add(10);
        stringBox.add("菜鸟教程");

        System.out.printf("整型值为: %d\n\n", integerBox.get());
        System.out.printf("字符串为: %s\n", stringBox.get());

        List<String> name = new ArrayList<String>();
        List<Integer> age = new ArrayList<Integer>();
        List<Number> number = new ArrayList<Number>();

        name.add("icon");
        age.add(26);
        number.add(200);

        getData(name);
        getData(age);
        getData(number);

        getUperNumber(age);
        getUperNumber(number);
    }

    public static void getData(List<?>data){
        System.out.println("data :" + data.get(0));
    }

    // 限定参数泛型上限为Number所以泛型为String是不在这个范围之内所以会报错
    public static void getUperNumber(List<? extends Number> data){
        System.out.println("data :" + data.get(0));
    }
}
