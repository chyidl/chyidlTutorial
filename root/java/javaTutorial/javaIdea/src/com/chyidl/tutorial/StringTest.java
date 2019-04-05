package com.chyidl.tutorial;

/**
 * Java String类
 * */
public class StringTest {

    public static void main(String[] args) {
        String name = "齐昱"; // String对象immutable
        char[] helloArray = {'r', 'u', 'n', 'o', 'o', 'b'};
        String helloString = new String(helloArray);
        System.out.println(helloString);
        System.out.println(name.length()); // 返回字符串对象包含的字符数
        System.out.println("Steve Jobs".concat(name)); // 连接字符串

        // 格式化字符串
        String fs = String.format("Stay hungry Stay foolish");
        System.out.println(fs);
        System.out.println(fs.charAt(1)); // 返回指定索引处的char值
        System.out.println(fs.compareTo("Stay Hungry Stay Foolish"));
        System.out.println(fs.compareToIgnoreCase("stay hungry stay foolish")); // 比较不考虑大小写
        System.out.println(fs.endsWith("Foolish")); // 后缀
        System.out.println(fs.startsWith("Stay")); // 前缀
        System.out.println(fs.getBytes()); // bytes
        System.out.println(fs.hashCode()); // 返回字符串的哈希吗
        System.out.println(fs.indexOf('a')); // 返回字符串中第一次出现处的索引
        System.out.println(fs.lastIndexOf('a')); // 返回指定字符串最右边出现的索引
        System.out.println(fs.intern()); // 规范化表示形式
        System.out.println(fs.length()); // 返回字符串中的长度
        System.out.println(fs.trim()); // 返回字符串的副本，忽略前岛空白和尾部空白

        /**
         * Java StringBuffer 和 StringBuilder
         * StringBuffer  是线程安全
         * StringBuilder 不是线程安全，不能同时访问，但是速度快
         * */
        StringBuffer sBuffer = new StringBuffer("菜鸟教程官网:");
        sBuffer.append("www");  // 将指定字符串追加到字符序列
        sBuffer.append(".runoob");
        sBuffer.append(".com");
        System.out.println(sBuffer);
        System.out.println(sBuffer.reverse()); // 反转形式
        System.out.println(sBuffer.reverse().delete(0,7)); // 移除序列的字符串的值
        System.out.println(sBuffer.insert(0,"https://")); // 插入字符串
        System.out.println(sBuffer.replace(0,5,"http")); // 替换自字符串
        System.out.println(sBuffer.capacity()); // 返回当前的容量
        System.out.println(sBuffer.charAt(4)); // 返回序列中指定索引处的char值
        System.out.println(sBuffer.indexOf(":")); // 返回第一次出现指定字符串的索引
        System.out.println(sBuffer.lastIndexOf(":")); // 返回最右边出现指定字符串中的索引
        System.out.println(sBuffer.length()); // 返回长度
        sBuffer.setCharAt(4, '='); // 将给定索引处的字符设置为ch
        System.out.println(sBuffer);
        System.out.println(sBuffer.subSequence(0,4)); // 返回一个新的字符序列，该字符序列是此序列的子序列
    }
}
