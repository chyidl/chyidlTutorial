package com.chyidl.advance.dataStructionAndAlgorithm;

import java.util.*;

/**
 * Java集合框架
 * 集合 Collection: 存储一个元素集合[List, Set, Queue] - ArrayList, LinkedList, HashSet, LinkedHashSet, HashMap, LinkedHashMap
 * 图 Map：存储键值对映射
 * 几个框架是一个用来代表和操纵集合的统一架构，所有的集合框架都包含：
 *  接口： 代表集合的抽象数据类型， Collection, List, Set, Map
 *  实现类：集合接口的具体实现，ArrayList, LinkedList, HashSet, HashMap
 *  算法:是实现集合接口的对象里的方法执行的一些有用的计算，例如搜索和排序，这些算法被称为多态，那是因为相同的方法可以在相似的接口上有着不同的实现
 *
 *  List接口：有序的Collection,使用此接口能够精确的控制每一元素插入的位置，能够通过索引来访问List中的元素，第一个元素的索引为0，而且允许有相同的元素
 *  List接口存储一组不唯一，有序的对象
 *
 *  Set具体Collection完全一样的接口，Set中不保存重复的元素 ，Set接口存储一组唯一，无序的对象
 *
 *  SortedSet: 继承于Set保存有序的集合
 *
 *  Map 接口存储一组键值对象，提供key 到 value的映射
 *
 *  Map.Entry: 描述一个Map中的一个元素，是一个Map的内部类
 *
 *  SortedMap: 继承于Map，使Key保持在生序排序
 *
 *  Enumeration: 可以枚举对象集合中的元素，这个传统接口已被迭代器取代
 *
 *  Set 和 List:
 *      Set接口实例存储的是无序，不重复的数据，List接口实例存储的是有序的，可以重复的元素
 *      Set检索效率地下，删除和插入效率高，插入和删除不会引用元素位置改变实现类有HashSet, TreeSet
 *      List和数组类似，可以动态增长，根据实际存储数据的长度自动增长List的长度，查找元素效率高，插入删除效率低，因为会引起其他元素改变，实现类ArrayList, LinkedList, Vector
 *
 * ArrayList: 实现List接口，实现了可变大小的数组，随机访问和遍历元素，提供更好的性能，该类也是非同步的，在多线程下不要使用，ArrayList增长当前长度的50%，插入删除效率低
 * HashSet: 该类实现Set接口，不允许出现重复元素，不保证集合元素的顺序，允许包含值为Null的元素，但最多只有一个
 * LinkedHashSet: 具有可预知迭代顺序的Set接口的哈希表和链表实现
 * TreeSet: 该类实现Set接口，可以实现排序功能
 * HashMap是一个散列表，存储的内容是键值对Key-value映射 不支持线程同步
 * TreeMap:实现一棵树
 *
 * Vector:可以在多线程的情况下使用，同步，该类允许设置默认的增长长度，默认扩容方式为原来的2倍
 * Stack: 是Vector的一个子类，实现一个标准的后进先出的栈
 * Dictionary:类是一个 抽象类，用来存储键值对，作用和Map类似
 * Hashtable:是Dictionary类的子类，位于Java.util 包中
 * Properties:继承于Hashtable，表示一个持久的属性集，属性列表中每个键及其值都是一个字符串
 * BitSet:创建一种特殊类型的数据来保存位置
 *
 * 任何对象加入集合类后，自动转变为Object类型，所以在取出的时候，需要进行强制类型转换
 */
public class CollectionTest {

    //

    public static void main(String[] args){

        /**
         * 遍历ArrayList
         * */
        List<String> list = new ArrayList<String>();
        list.add("Hello");
        list.add("World");
        list.add("HAHAHAHA");

        // 第一种遍历方法使用for each遍历List
        for (String str: list){ // 也可以改写for (int i=0; i<list.size(); i++) 这种形式
            System.out.println(str);
        }

        // 第二种遍历，把链表变为数组相关的内容进行遍历
        String[] strArray = new String[list.size()];
        list.toArray(strArray);
        for(int i=0; i<strArray.length; i++){
            System.out.println(strArray[i]);
        }

        //第三种遍历，使用迭代器进行相关遍历
        Iterator<String> ite = list.iterator();
        while (ite.hasNext()){
            System.out.println(ite.next());
        }

        /**
         * 遍历Map
         * */
        Map<String, String> map = new HashMap<String, String>();
        map.put("1", "value1");
        map.put("2", "value2");
        map.put("3", "value3");

        // 第一种：普遍使用，二次取值
        System.out.println("通过Map.keySet遍历key和value: ");
        for(String key: map.keySet()){
            System.out.println("key= " + key + " and value= " + map.get(key));
        }

        // 第二种
        System.out.println("通过Map.entrySet使用iterator遍历key和value: ");
        Iterator<Map.Entry<String, String>> it = map.entrySet().iterator();
        while (it.hasNext()){
            Map.Entry<String, String> entry = it.next();
            System.out.println("key= " + entry.getKey() + " and value= " + entry.getValue());
        }

        // 第三种:推荐，尤其是容量大时
        System.out.println("通过Map.entrySet遍历key和value");
        for(Map.Entry<String, String> entry : map.entrySet()){
            System.out.println("key= " + entry.getKey() + " and value= " + entry.getValue());
        }

        // 第四种
        System.out.println("通过Map.values()遍历所有的value,但不能遍历key");
        for(String v: map.values()){
            System.out.println("value= " + v);
        }

    }
}
