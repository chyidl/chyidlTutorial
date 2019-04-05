package com.chyidl.tutorial;

import java.text.SimpleDateFormat;
import java.util.Date;  // 当前日期和时间

public class DateAndTimeTest {

    public static void main (String[] args) {
        // 初始化 Date 对象
        Date now = new Date();
        // SimpleDateFormat格式化日期
        SimpleDateFormat ft = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        // 接收一个毫秒数的参数
        Date someNow = new Date(1000);

        // 获取当前日期和时间
        System.out.println(now);
        // 返回自1970年1月1日00:00:00 GMT以来Date对象表示毫秒数
        System.out.println(now.getTime());
        // 获取哈希码值
        System.out.println(now.hashCode());
        // 转换为String dow mon dd hh:mm:ss zzz yyyy dow表示某一周的某一天
        System.out.println(now.toString());
        System.out.println(someNow);

        /* Java中比较两个日期 */
        // getTime()方法获取两个日期，然后比较两个值
        // before(), after(), equals()
        // compareTo()

        //
        System.out.println("当前时间为: " + ft.format(now));

        // printf格式化日期 %t开头
        System.out.printf("全部日期和时间信息: %tc\n",now);
        System.out.printf("年-月-日格式: %tF\n", now);
        System.out.printf("月/日/年格式: %tD\n", now);
        System.out.printf("HH:MM:SS PM格式（12时制）: %tr\n", now);
        System.out.printf("HH:MM格式（24时制）: %tR\n", now);
    }
}
