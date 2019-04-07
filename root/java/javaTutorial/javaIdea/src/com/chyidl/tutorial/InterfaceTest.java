package com.chyidl.tutorial;

/**
 * Java接口
 * 接口并不是类，编写接口的方式和类很相似，但是他们属于不同的概念，类描述对象的属性和方法，接口则包含类要实现的方法
 * 除非实现接口的类是抽象类否则该类要定义接口中的所有方法
 * 接口无法被实例化，但是可以被实现，一个实现接口的类，必须实现接口内所描述的所有方法，否则就必须声明为抽象类。
 *
 * 接口与类相似点：
 *      一个接口可以有多个方法
 *      接口文件保存在java结尾的文件中，文件名使用接口名
 *
 * 接口与类的区别:
 *      接口不能用于实例化对象
 *      接口没有构造方法
 *      接口中所有的方法必须是抽象方法
 *      接口不能包含成员变量，除了static,final变量
 *      接口不能被类继承，而是要被类实现
 *      接口支持多继承
 *
 * 接口特性
 * 接口中每一个方法必须隐式抽象，接口中的方法会被隐式的指定为public abstract(只能是public abstract,其他修饰符都会报错)
 * 接口中可以含有变量，但是接口中的变量会被隐式的指定为public static final变量， ( 并且只能是public,用private修饰会包编译错误)
 *
 * 抽象类和接口的区别
 *      抽象类中的方法可以有方法体，就是能实现方法的具体功能，但是接口中的方法不行
 *      抽象类中的成员变量可以是各种类型，而接口中的成员变量只能是public static final类型
 *      接口中不能含有静态代码快以及静态方法，而抽象类是可以有静态代码块和静态方法
 *      一个类只能继承一个抽象类，而一个类却可以实现多个接口
 *
 * 接口的多继承
 *      在Java中，类的多继承是不合法，但接口允许多继承
 *
 * 标记接口：简单形象的说就是给某个对象打个标，使对象拥有某个或某些特权
 *      没有任何方法的接口称为标记接口，标记接口主要用于
 *      建立一个公共的父接口
 *      像一个类添加数据类型
 * */

interface AnimalInterface{
    // 任何类型 final, static 字段
    // 抽象方法
    public void eat();
    public void travel();
}

public class InterfaceTest  implements AnimalInterface{

    public static void main(){
        InterfaceTest m = new InterfaceTest();
        m.eat();
        m.travel();
        System.out.println("He");
    }

    @Override
    public void eat() {
        System.out.println("Mammal eats");
    }

    @Override
    public void travel() {
        System.out.println("Mammal travels");
    }
}
