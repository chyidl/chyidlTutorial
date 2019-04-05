package com.chyidl.tutorial;

public class VariableTypeTest {

    static int allClicks = 0;   // 类变量
    public String name; // 实例变量对子类可见
    private double salary; //私有变量，仅在该类可见

    // 构造函数对name赋值
    public VariableTypeTest(String name) {
        this.name = name;
    }

    //打印信息
    public void printVariableTypeTest(){
        System.out.print("名字: " + name);
        System.out.print("薪水: " + salary);
    }

    public static void main(String[] args) {
        // 局部变量
        int a, b, c;    // 声明三个int型整数: a,b,c
        int d = 3, e = 4, f = 5; // 声明三个整数并赋予初值
        byte z = 22;    // 声明并初始化 z
        String s = "runoob";  // 声明并初始化字符串
        double pi = 3.1415926; // 声明双精度浮点型变量pi
        char x = 'x';   // 声明变量x的值是字符'x'

        VariableTypeTest varInstance = new VariableTypeTest("ChyiYaqing");
        varInstance.setSalary(13000);
        varInstance.printVariableTypeTest();
    }

    public double getSalary() {
        return salary;
    }

    // 设定salary的值
    public void setSalary(double salary) {
        this.salary = salary;
    }
}
