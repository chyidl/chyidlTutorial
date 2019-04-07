package com.chyidl.advance.dataStructionAndAlgorithm;

import java.util.Enumeration;
import java.util.Vector;

/**
 * 向量Vector
 * 向量Vector类和传统的数组非常相似，但是Vector的大小能根据需要动态的变化
 * 和数组一样，Vector对象能通过索引访问
 * 使用Vector类最主要的好处就是在创建对象的时候不必给对象指定大小，大小会根据需要动态的变化
 * */
public class VectorTest {
    public static void main(String[] args){
        // initial size is 3, increment is 2
        Vector v = new Vector(3, 2);
        System.out.println("Initial size: " + v.size());
        System.out.println("Initial capacity: " + v.capacity());
        v.addElement(1);
        v.addElement(2);
        v.addElement(3);
        v.addElement(4);
        System.out.println("Capacity after four additions: " + v.capacity());

        v.addElement(5.45);
        System.out.println("Current capacity: " + v.capacity());
        v.capacity();
        v.addElement(6.08);
        v.addElement(7);
        System.out.println("Current capacity: " + v.capacity());
        v.addElement(9.4);
        v.addElement(10);
        System.out.println("Current capacity: "+ v.capacity());
        v.addElement(11);
        v.addElement(12);
        System.out.println("First element: " + v.firstElement());
        System.out.println("Last element: " + v.lastElement());

        if(v.contains(3))
            System.out.println("Vector contains 3.");
        // enumerate the elements in the vector
        Enumeration vEnum = v.elements();
        System.out.println("\nElements in vector:");
        while(vEnum.hasMoreElements())
            System.out.print(vEnum.nextElement() + " ");

        System.out.println();
    }
}
