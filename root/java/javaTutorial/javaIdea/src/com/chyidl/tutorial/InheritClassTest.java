package com.chyidl.tutorial;


/**
 * Java不支持多继承，但支持多重继承
 * 继承的特性:
 *  子类拥有父类非private的属性、方法
 *  子类可以拥有自己的属性和方法，
 *  子类可以用的自己的方法实现父类的方法，重载
 *  Java的继承是单继承，但是可以多重继承，单继承就是一个子类只能继承一个父类，多重继承
 *  提高类之间的耦合性(继承的缺点、耦合度高就会造成代码之间的联系越紧密，代码独立性差)
 *
 *  super关键字：通过super关键字实现对父类成员的访问，用来引用当前对象的父类
 *  this关键字：指向自己的引用
 * */
class Animal{
    private String name;
    private int id;

    public Animal(){

    }

    public Animal(String name, int id){
        this.name = name;
        this.id = id;
    }

    public void move(){
        System.out.println("动物们可以移动");
    }

    public void eat(){
        System.out.println(name + "正在吃");
    }

    public void sleep(){
        System.out.println(name + "正在睡");
    }

    public void introduction(){
        System.out.println("大家好！我是" + id + "号" + name +".");
    }
}

/**
 * 继承使用extends, implements 两个关键字实现继承
 * 所有类都是继承于java.lang.Object
 * */
class Penguin extends Animal{
    public Penguin(String name, int id){
        super(name, id);
    }
}

class Mouse extends Animal{
    public Mouse(String name, int id){
        super(name, id);
    }


    @Override
    public void eat() {
        System.out.println("mouse: eat");
    }

    void eatTest(){
        this.eat();  // this调用自己的方法
        super.eat(); // super调用父类的方法
    }
}

interface A{
    public void eat();
    public void sleep();
}

interface B{
    public void show();
}

class C implements A,B{
    @Override
    public void eat() {

    }

    @Override
    public void sleep() {

    }

    @Override
    public void show() {

    }
}

class SuperClass{
    private int n;

    SuperClass(){
        System.out.println("SuperClass()");
    }

    SuperClass(int n){
        System.out.println("SuperClass(int n)");
        this.n = n;
    }
}

class SubClass extends SuperClass{
    private int n;

    SubClass(){ // 自动调用父类的无参数构造器
        System.out.println("SubClass");
    }

    public SubClass(int n) {
        super(300); // 调用弗雷中带有参数的构造器
        System.out.println("SubClass(int n): " + n);
        this.n = n;
    }
}

class SubClass2 extends SuperClass{
    private int n;

    SubClass2(){
        super(300); // 调用父类中带有参数的构造函数
        System.out.println("SubClass2");
    }

    public SubClass2(int n){ // 自动调用父类的无参数构造器
        System.out.println("SubClass2(int n):" + n);
        this.n = n;
    }
}

/**
 * Java 继承
 *
 * final关键字声明类可以把类定义为不能继承，或者用于修饰方法，该方法不能被子类重写
 * final class 类名 {//类体}  // 声明类
 * */

/**
 * 构造器：子类是不能继承父类的构造器(构造方法或者构造函数)，他只是调用(隐式或显式)
 * 如果父类的构造器带有参数，则必须在子类的构造器中显式通过super关键字调用父类的构造器并配以适当的参数列表。
 * 如果父类的构造器没有参数，则在子类的构造器中不需要使用super关键字调用父类构造器，系统会自动调用父类的无参构造器
 * */
public class InheritClassTest {
    public static void main(String[] args){
        Animal a = new Animal("Animal", 1);
        a.eat();
        Mouse m = new Mouse("mouse", 2);
        m.eatTest();

        System.out.println("------SubClass 类继承---------");
        SubClass sc1 = new SubClass();
        SubClass sc2 = new SubClass(100);
        System.out.println("-------SubClass2 类继承-------");
        SubClass2 sc3 = new SubClass2();
        SubClass2 sc4 = new SubClass2(200);
    }
}
