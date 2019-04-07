package com.chyidl.advance.dataStructionAndAlgorithm;

import java.util.HashMap;

/**
 * Java Map接口
 * Map接口中键和值 -- 一一映射，可以通过键获取值
 *  当访问的值不存在的时候，方法就会抛出一个NoSuchElementException异常
 *  当对象的类型和Map里元素类型不兼容的时候，就会抛出一个ClassCastException异常
 *  当不允许使用Null对象的Map中使用Null对象，会抛出NullPointerException一样
 *  当尝试修改一个只读的Map时，会抛出一个UnsupportedOperationException异常
 * */
public class MapTest {
    public static void main(String[] args){
        HashMap m1 = new HashMap<String, String>();
        m1.put("Zara", "8");
        m1.put("Mahnaz", "31");
        m1.put("Ayan", "12");
        m1.put("Daisy", "14");
        System.out.println();
        System.out.println("Map Elements");
        System.out.print("\t" + m1);
    }
}
