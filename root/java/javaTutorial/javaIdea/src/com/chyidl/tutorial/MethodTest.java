package com.chyidl.tutorial;


class Cake extends Object{
    private int id;

    public Cake(int id) {
        this.id = id;
        System.out.println("Cake Object " + id + " is created");
    }

    protected void finalize() throws java.lang.Throwable {
        super.finalize();
        System.out.println("Cake Object " + id + " is disposed");
    }
}


/**
 * Java方法是语句的集合，一起执行一个功能
 *  方法是解决一类问题的步骤的有序组合
 *  方法在程序中被创建，在其他地方被引用
 * 方法命名规则：
 *      方法的名称的第一个单词应以小写字母开头，后面的单词则大写字母开头，不使用连接符
 *      下划线可能出现在JUnit测试方法名称中，用以分隔名称的逻辑组件
 * */
public class MethodTest {

    // 构造方法 -- 用来初始化该对象
    // java自动提供默认构造方法，默认构造方法的访问修饰符和类访问修饰符相同
    MethodTest(){

    }

    // finalize()方法在垃圾回收之前调用
    protected void finalize(){
        System.out.println("调用Java垃圾收集器");
    }

    // 返回两个整型变量数据的较大值
    public static int max(int num1, int num2) {
        return  num1 > num2 ? num1 : num2;
    }

    // 方法的重载 - 必须拥有不同的参数列表，不能仅仅依据修饰符或者返回类型的不同来重载方法
    public static double max(double num1, double num2) {
        return num1 > num2 ? num1 : num2;
    }

    // main方法是被JVM调用
    // String[] args: 方法的参数范围覆盖整个方法，参数实际上是一个局部变量
    public static void main(String[] args){
        int i=5, j=2;  // 局部变量
        int k = max(i, j);
        System.out.println(i + " 和 " + j + " 比较，最大值是: " + k);

        printGrade(78.5);

        int num1 = 1, num2 = 2;
        System.out.println("交换前 num1 的值为: " + num1 + " , num2 的值为: " + num2);

        // 调用swap方法
        swap(num1, num2);
        System.out.println("交换后 num1 的值为: " + num1 + ", num2 的值为: " + num2);

        // 打印所有的命令行参数
        for (int index=0; index<args.length; i++){
            System.out.println("args[" + i + "]: " + args[index]);
        }

        // 调用可变参数的方法
        printMax(new double[]{1, 2, 3});

        Cake c1 = new Cake(1);
        Cake c2 = new Cake(2);
        Cake c3 = new Cake(3);
        c2 = c3 = null;
        System.gc(); // 调用Java垃圾收集器
    }

    // printGrade方法是void方法，不返回值
    public static void printGrade(double score) {
        if (score >= 90.0) {
            System.out.println('A');
        } else if (score >= 80.0) {
            System.out.println('B');
        } else if (score >= 70.0) {
            System.out.println('C');
        } else if (score >= 60.0) {
            System.out.println('D');
        } else {
            System.out.println('F');
        }
    }

    public static void swap(int n1, int n2){
        System.out.println("\t进入 swap 方法");
        System.out.println("\t\t交换前 n1 的值为: " + n1 + ", n2的值: " + n2);
        // 交换 n1 与 n2的值
        int temp = n1;
        n1 = n2;
        n2 = temp;
        System.out.println("\t\t交换后 n1 的值为 " + n1 + ", n2 的值: " + n2);
    }

    // 调用可变参数的方法
    // JDK 1.5开始Java支持传递同类型的可变参数给方法
    // 一个方法只能指定一个可变参数，必须是方法的最后一个参数，任何普通的参数必须在它之前声明
    public static void printMax(double... numbers) {
        if (numbers.length == 0) {
            System.out.println("No argument passed");
            return;
        }
        double result = numbers[0];
        for (int i=1; i<numbers.length; i++) {
            if (numbers[i] > result){
                result = numbers[i];
            }
        }
        System.out.println("The max value is " + result);
    }
}
