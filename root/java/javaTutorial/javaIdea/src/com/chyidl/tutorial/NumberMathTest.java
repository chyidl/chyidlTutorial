package com.chyidl.tutorial;

/**
 * Java语言为每一个内置数据类型提供一个包装类
 * int,long,byte,double,float,short 内置数据类型
 * Integer,Long, Byte, Double, Float, Short 都是抽象类Number的子类
 * */
public class NumberMathTest {

    public static void main(String[] args) {
        /**
         * Number 类
         * */
        Integer x = 5; // 编译器对x进行装箱
        x += 10; // 为了加法运算，需要对x拆箱
        System.out.println(x);

        /**
         * Java.Math类
         */
        System.out.println("90度的正弦值: " + Math.sin(Math.PI/2));
        System.out.println("0度的余弦值: "+ Math.cos(0));
        System.out.println("60度的正切值: " + Math.tan(Math.PI/3));
        System.out.println("1的反正切值: " + Math.atan(1));
        System.out.println("PI/2的角度值: " + Math.toDegrees(Math.PI/2));
        System.out.println(Math.PI);

        /**
         * Number & Math类方法
         * */
        Integer salary = 13000;
        System.out.println(salary.intValue());  // 将Number对象转为int数据类型的值
        System.out.println(salary.compareTo(13)); // compareTo 比较
        System.out.println(salary.equals(13000)); // equals判断number对象是否与参数相等
        System.out.println(Integer.valueOf(13000)); // 返回一个Number对象指定的内置数据类型
        System.out.println(salary.toString()); // 以字符串形式返回值
        System.out.println(Math.abs(salary)); // 返回绝对值
        System.out.println(Math.ceil(salary)); // 返回一个大于等于给定参数的最小整数，类型为双精度浮点数
        System.out.println(Math.floor(salary)); // 返回一个小于等于给定参数的最大整数，类型为双精度浮点数
        System.out.println(Math.rint(salary)); // 返回与参数最接近的整数，类型为double
        System.out.println(Math.round(salary)); // 四舍五入，算法是Math.floor(x+0.5),
        System.out.println(Math.min(10, 11)); // 返回两个参数中的最小值
        System.out.println(Math.max(10, 11)); // 返回两个参数中的最大值
        System.out.println(Math.exp(2)); // 返回自然数底数e的参数次方
        System.out.println(Math.log(1)); // 返回参数的自然数底数的对数值
        System.out.println(Math.pow(2, 3)); // 返回第一个参数和第二参数次方
        System.out.println(Math.sqrt(8)); // 求算术平方根
        System.out.println(Math.sin(9)); // 求指定double类型参数的正弦值
        System.out.println(Math.cos(9)); // 求指定double类型参数的余弦值
        System.out.println(Math.tan(9)); // 求指定double类型参数的正切值
        System.out.println(Math.asin(9)); // 求指定double类型参数的反正弦值
        System.out.println(Math.acos(9)); // 指定double类型参数的反余弦值
        System.out.println(Math.atan2(10, 20)); // 将笛卡尔坐标转为极坐标，并返回极坐标的角度值
        System.out.println(Math.random()); // 返回一个随机数
    }
}
