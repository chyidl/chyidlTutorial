package com.chyidl.advance.dataStructionAndAlgorithm;

import java.util.Iterator;
import java.util.Properties;
import java.util.Set;

/**
 * Java Properties
 * Properties 继承与Hashtable表示一个持久的属性集，属性列表中每个键及其对应值都是一个字符串
 * Properties类被许多Java类使用，在获取环境变量时他就作为System.getProperties方法的返回值
 * Properties定义如下实例变量，这个变量持有一个Properties对象相关的默认属性列表
 * */
public class PropertiesTest {
    public static void main(String[] args){
        Properties capitals = new Properties();
        Set states;
        String str;

        capitals.put("Illinois", "Springfield");
        capitals.put("Missouri", "Jefferson City");
        capitals.put("Washington", "Olympia");
        capitals.put("California", "Sacramento");
        capitals.put("Indiana", "Indianapolis");

        // Show all states and capitals in hashtable.
        states = capitals.keySet(); // get set-view of keys
        Iterator itr = states.iterator();
        while (itr.hasNext()){
            str = (String) itr.next();
            System.out.println("The capital of " + str + " is " + capitals.getProperty(str) + ".");
        }
        System.out.println();

        // look for state not in list -- specify default
        str = capitals.getProperty("Florida", "Not Found");
        System.out.println("The capital of Florida is " + str + ".");
    }
}
