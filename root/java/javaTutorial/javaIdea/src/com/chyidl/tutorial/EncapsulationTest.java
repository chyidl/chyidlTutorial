package com.chyidl.tutorial;

/**
 * Java 封装 Encapsulation 是指一种将抽象性函式接口的实现细节部分包装，隐藏起来的方法
 * 封装可以被认为一个保护屏障，防止该类的代码和数据被外部类定义的代码随机访问
 * 要访问该类的代码和数据，必须通过严格的接口控制
 * 封装最主要的功能是在于我们能修改自己的实现代码而不用修改那些调用我们代码的程序片段
 * 适当的封装可以让程序更容易理解与维护，也加强了程序的安全性
 *
 * 良好的封装能够减少耦合
 * 类内部的结构可以自由修改
 * 可以对成员变量进行更精确的控制
 * 隐藏信息，实现细节
 * */

class Person{
    // 属性设置为私有，只能本类才能访问，其他类都访问不了
    private String name;
    private int age;

    // public方法是外部类访问该类成员变量的入口
    public String getName() {
        return name;
    }

    public void setName(String name) {
        // 采用this关键字为了解决实例变量和局部变量之间发生同名的冲突
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
}

public class EncapsulationTest {

    public static void main(){

    }
}
