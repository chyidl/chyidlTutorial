package com.chyidl.tutorial;

/**
 * Java Character类
 * */
public class CharacterTest {

    public static void main(String[] args){
        char ch = 'a';
        // 使用Character构造方法创建一个Character类对象
        Character cha = new Character('a');
        // Unicode 字符表示形式
        char uniChar = '\u039A';
        // 字符数组
        char[] charArray = {'a', 'b', 'c', 'd', 'e'};
        System.out.println("访问\"菜鸟教程!\"");

        /**
         * Character方法
         * */
        System.out.println(Character.isLetter(ch)); // 是否是一个字母
        System.out.println(Character.isDigit(ch)); // 是否是一个数字字符
        System.out.println(Character.isWhitespace(ch)); // 是否是一个空白字符
        System.out.println(Character.isUpperCase(ch)); // 是否是大写字母
        System.out.println(Character.isLowerCase(ch)); // 是否是消协字母
        System.out.println(Character.toUpperCase(ch)); // 转大写
        System.out.println(Character.toLowerCase(ch)); // 转小写
        System.out.println(cha.toString()); // 返回字符串形式
    }
}
