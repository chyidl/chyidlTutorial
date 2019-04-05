package com.chyidl.tutorial;

import java.awt.dnd.DropTarget;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;  // 当前日期和时间
import java.util.GregorianCalendar;
import java.util.Locale;

public class DateAndTimeTest {

    public static void main (String[] args) {
        // 使用当前日期和时间初始化对象, 初始化 Date 对象
        Date now = new Date();
        // 接收一个毫秒数的参数初始化 Date 对象
        Date someNow = new Date(1000);

        /**
         * Date对象调用的方法
         * */
        // 获取当前日期和时间
        System.out.println(now);
        // 当调用次方法的Date对象在指定日期之前返回true否则返回false
        System.out.println(now.before(new Date()));
        // 返回对象的副本
        System.out.println(now.clone());
        System.out.println(now.compareTo(new Date()));
        System.out.println(now.equals(new Date()));
        // 返回自1970年1月1日00:00:00 GMT以来Date对象表示毫秒数
        System.out.println(now.getTime());
        // 获取哈希码值
        System.out.println(now.hashCode());
        // 使用自1970年1月1日00:00:00 GMT 以后time毫秒数设置时间和日期
        now.setTime(0);
        System.out.println(now);
        // 转换为String dow mon dd hh:mm:ss zzz yyyy dow表示某一周的某一天
        System.out.println(now.toString());
        System.out.println(someNow);

        /* Java中比较两个日期 */
        // getTime()方法获取两个日期，然后比较两个值
        // before(), after(), equals()
        // compareTo()
        //

        /**
         * SimpleDateFormat格式化日期
         * */
        // SimpleDateFormat格式化日期
        SimpleDateFormat ft = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        System.out.println("当前时间为: " + ft.format(new Date()));

        // printf格式化日期 %t开头
        System.out.printf("全部日期和时间信息: %tc\n",now);
        System.out.printf("年-月-日格式: %tF\n", now);
        System.out.printf("月/日/年格式: %tD\n", now);
        System.out.printf("HH:MM:SS PM格式（12时制）: %tr\n", now);
        System.out.printf("HH:MM格式（24时制）: %tR\n", now);
        // 利用格式化字符串指出要被格式化的参数的索引，索引必须紧跟在%之后，必须以$结束
        System.out.printf("%1$s %2$tB %2$td, %2$tY\n", "Due date:", new Date());
        // 使用<标志，表明先前被格式化的参数要被再次使用
        System.out.printf("%s %tB %<te, %<tY\n", "Due date:", new Date());

        /**
         * 日期转换符
         * */
        // b的使用，月份简称
        String str = String.format(Locale.CHINA, "中文月份简称: %tb", new Date());
        System.out.println(str);
        System.out.printf("本地月份简称: %tb%n", new Date());
        // B的使用，月份全称
        str = String.format(Locale.CHINA, "中文月份全称: %tB", new Date());
        System.out.println(str);
        System.out.printf("本地月份全称: %tB%n", new Date());
        // a的使用，星期简称
        str = String.format(Locale.CHINA, "中文星期的简称: %ta", new Date());
        System.out.println(str);
        // A的使用，时期全称
        System.out.printf("本地星期的简称: %tA%n", new Date());
        // C的使用,年前两位
        System.out.printf("年的前两位数字 (不足两位前面补0) : %tC%n", new Date());
        // y的使用，年后两位
        System.out.printf("年的后两位数字 (不足两位前面补0) : %ty%n", new Date());
        // j的使用,一年的天数
        System.out.printf("一年中的天数 (即年的第几天) : %tj%n", new Date());
        // m的使用，月份
        System.out.printf("两位数字的月份 (不足两位前面补0) : %tm%n", new Date());
        // d的使用，日(两位，不够补零)
        System.out.printf("两位数字的日 (不足两位前面补0) : %td%n", new Date());
        // e的使用, 日(一位不补零)
        System.out.printf("月份的日(前面不补0) : %te\n", new Date());

        /**
         * 解析字符串为时间
         * */
        ft = new SimpleDateFormat("yyyy-MM-dd");
        String input = args.length == 0 ? "1949-10-01": args[0];
        System.out.print(input + " Parses as ");
        Date t;
        try{
            t = ft.parse(input);
            System.out.println(t);
        }catch (ParseException e){
            System.out.println("Unparseable using " + ft);
        }

        /**
         * Java 休眠sleep
         * sleep()使当前线程进入停滞状态 阻塞当前线程，让出CPU的使用，目的是不让当前线程独占所获的的CPU资源
         * */
        try {
            System.out.println(new Date());
            Thread.sleep(1000*3); // 休眠3秒
            System.out.println(new Date());
        } catch (Exception e) {
            System.out.println("Got an exception!");
        }

        /**
         * 测量时间间隔
         * */
        try{
            long start = System.currentTimeMillis();
            System.out.println(new Date());
            Thread.sleep(5*60*10);
            System.out.println(new Date());
            long end  = System.currentTimeMillis();
            long diff = end - start;
            System.out.println("Difference is : " + diff);
        } catch (Exception e){
            System.out.println("Got an exception!");
        }

        /**
         * Calendar 类 是一个抽象类，
         * */
        // 创建一个代表系统当前日期的Calendar对象
        Calendar c = Calendar.getInstance();
        // 获取年份
        int year = c.get(Calendar.YEAR);
        // 获取月份
        int month = c.get(Calendar.MONTH)+1;
        // 获取日期
        int date = c.get(Calendar.DATE);
        // 获取小时
        int hour = c.get(Calendar.HOUR_OF_DAY);
        // 获取分钟
        int minute = c.get(Calendar.MINUTE);
        // 获得秒
        int second = c.get(Calendar.SECOND);
        // 获得星期几 1表示星期日，
        int day = c.get(Calendar.DAY_OF_WEEK);
        System.out.printf("%s-%s-%s %s:%s:%s / %s\n",year,month,date,hour,minute,second,day);
        // 创建一个代表2009年6月12日的Calendar对象
        Calendar c1 = Calendar.getInstance();
        c1.set(2019,4,5);

        // 初始化Gregorian日历
        GregorianCalendar gcalendar = new GregorianCalendar();
        // 显示当前时间和日期信息
        String months[] = {
                "Jan", "Feb", "Mar", "Apr",
                "May", "Jun", "Jul", "Aug",
                "Sep", "Oct", "Nov", "Dec"};
        System.out.print("Date: ");
        System.out.print(months[gcalendar.get(Calendar.MONTH)]);
        System.out.print(" " + gcalendar.get(Calendar.DATE) + " ");
        System.out.print(year = gcalendar.get(Calendar.YEAR));
        System.out.print("Time: ");
        System.out.print(gcalendar.get(Calendar.HOUR) + ":");
        System.out.print(gcalendar.get(Calendar.MINUTE) + ":");
        System.out.print(gcalendar.get(Calendar.SECOND));

        // 测试当前年份是否为闰年
        if (gcalendar.isLeapYear(year)) {
            System.out.println("当前年份为闰年");
        }else{
            System.out.println("当前年份不是闰年");
        }
    }
}
