package com.chyidl.tutorial;


/**
 * Java重写(Override) 与 重载(Overload)
 *
 * Override重写：是子类对父类允许访问的方法的实现过程进行重新编写，返回值和形参不能改变
 * 重写方法不能抛出新的检查异常或者比被重写方法声明更宽泛的异常
 *
 * 参数列表必须完全与被重写方法的相同
 * 返回类型与被重写方法的返回类型可以不相同，但是必须是父类返回值的派生类(java5 及更早版本返回类型要一样，java7及更高版本可以不同)
 * 反问权限不能比父类中被重写的方法的访问权限更低，如果父类的一个方法被声明为public，子类中重写该方法就不能声明为protected.
 * 父类的成员方法只能被它的子类重写
 * 声明为final的方法不能被重写
 * 声明为static的方法不能被重写，但是能够被再次声明
 * 子类和父类在同一个包中，那么子类可以重写父类所有方法，除了声明为private和final的方法
 * 子类和父类不再同一个包中，那么子类只能够重写父类中声明为public和protected的非final方法
 * 构造方法不能被重写
 * 如果不能继承一个方法，则不能重写这个方法
 *
 * 编译阶段，只是检查参数的引用类型，运行阶段，JVM运行该对象的方法
 * */

import com.sun.tools.javac.tree.JCTree;
import org.omg.PortableInterceptor.SYSTEM_EXCEPTION;

import java.util.stream.StreamSupport;

/**
 * 重载Overload
 * 重载是在一个类里面，方法名字相同，而参数不同，返回类型可以相同也可以不通过
 * 每一个重载的方法都必须有一个独一无二的参数类型列表
 * 最常见的地方就是构造器的重载
 *
 *  被重载的方法必须改变参数列表（参数个数或类型不一样）
 *  被重载的方法可以改变返回类型
 *  被重载的方法可以改变访问修饰符
 *  被重载的方法可以声明新的或更广的检查异常
 *  方法能够在同一个类中或者在一个子类中被重载
 *  无法以返回值类型作为重载函数的区分标准
 * */

public class OverrideOverloadTest {

    public int test(){
        System.out.println("test1");
        return 1;
    }

    public void test(int a){
        System.out.println("test2");
    }

    // 一下两个参数类型顺序不同
    public String test(int a, String s){
        System.out.println("test3");
        return "returntest3";
    }

    public String test(String s, int a){
        System.out.println("test4");
        return "returntest4";
    }


    public static void main(String[] args){
        /**
         * 方法的重写Overriding和重载Overloading是java多态性的不同表现，重写是父类与子类之间多态性的一种表现，重载可以理解成多态的具体表现形式
         *
         * */
        OverrideOverloadTest o = new OverrideOverloadTest();
        System.out.println(o.test());
        o.test(1);
        System.out.println(o.test(1,"test3"));
        System.out.println(o.test("test4", 1));
    }
}
