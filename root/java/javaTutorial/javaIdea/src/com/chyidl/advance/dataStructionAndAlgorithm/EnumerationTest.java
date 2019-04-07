package com.chyidl.advance.dataStructionAndAlgorithm;

import java.util.Enumeration;
import java.util.Vector;

/**
 * 枚举 EnumerationTest
 * 枚举定义了一个nextElement方法，该方法用来得到一个包含多元素的数据结构的下一个元素
 *
 * 这种传统接口已经被迭代器取代，虽然Enumeration还未被遗弃，但在现代代码中已经很少使用，
 *      boolean hasMoreElement() : 测试该枚举是否包含更多的元素
 *      Object nextElement(): 如果枚举对象至少还有一个可提供的元素，则返回枚举的下一个元素
 * */
public class EnumerationTest {
    public static void main(String[] args) {
        Vector<String> dayNames = new Vector<String>();
        dayNames.add("Sunday");
        dayNames.add("Monday");
        dayNames.add("Tuesday");
        dayNames.add("Wednesday");
        dayNames.add("Thurday");
        dayNames.add("Friday");
        dayNames.add("Saturday");
        for (Enumeration days = (Enumeration) dayNames.elements(); days.hasMoreElements();)
            System.out.println(days.nextElement());
    }
}
