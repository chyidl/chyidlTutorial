package com.chyidl.tutorial;

/**
 * 多态是同一个行为具有多个不同表现形式或形态的能力
 * 多态就是同一接口，使用不同的实例而执行不同操作
 *
 * 多态的优点：
 *      消除类型之间的耦合关系
 *      可替换性
 *      可扩充性
 *      接口性
 *      灵活性
 *      简化性
 *
 * 多态存在的三个必要条件
 *      继承
 *      重写
 *      弗雷引用指向子类对象
 * */

/**
 * 虚函数的存在是为了多态
 * Java中没有虚函数的概念，它的普通函数就相当于C++的虚函数，动态绑定是Java的默认行为，如果Java中不希望某个函数具有虚函数特性，可以加上final关键字编程非虚函数
 * */
class EmployeePoly{
    private String name;
    private String address;
    private int number;

    public EmployeePoly(String name, String address, int number){
        System.out.println("Employee 构造函数");
        this.name = name;
        this.address = address;
        this.number = number;
    }

    public void mailCheck(){
        System.out.println("邮票支票给: " + this.name + " " + this.address);
    }

    public String toString(){
        return name + " " + address + " " + number;
    }

    public String getname(){
        return name;
    }

    public String getAddress(){
        return address;
    }

    public void setAddress(String newAddress){
        address = newAddress;
    }

    public int getNumber(){
        return number;
    }
}

class SalaryPoly extends EmployeePoly{
    private double salary; // 全年工资

    public SalaryPoly(String name, String address, int number, double salary){
        super(name, address, number);
        setSalary(salary);
    }

    public void mailCheck(){
        System.out.println("Salary 类的 mailCheck方法");
        System.out.println("邮寄支票给：" + getname() + ", 工资为：" + salary);
    }

    public double computePay(){
        System.out.println("计算工资,付给：" + getname());
        return salary/52;
    }

    public double getSalary() {
        return salary;
    }

    public void setSalary(double salary) {
        this.salary = salary;
    }
}


public class PolymorphismTest {
    public static void main(String[] args){
        show(new CatPoly()); // 以 Cat对象调用show方法
        show(new DogPoly()); // 以 Dog对象调用show方法

        AnimalPoly a = new CatPoly(); // 向上转型
        a.eat();   // 调用的是Cat的eat
        CatPoly c = (CatPoly) a; // 向下转型
        c.work(); // 调用的是Cat的work

        SalaryPoly s = new SalaryPoly("员工 A", "北京", 3, 3600.00);
        EmployeePoly e = new SalaryPoly("员工 B", "上海", 2, 2400.00);
        System.out.println("使用Salary的引用调用mailCheck -- ");
        s.mailCheck();
        System.out.println("\n使用 Employee的引用调用mailCheck--");
        e.mailCheck();
    }

    public static void show(AnimalPoly a){
        a.eat();
        // 类型判断
        if (a instanceof CatPoly) { // 猫做的事情
            CatPoly c = (CatPoly) a;
            c.work();
        } else if (a instanceof DogPoly){ // 狗做的事情
            DogPoly c = (DogPoly) a;
            c.work();
        }
    }
}

abstract class AnimalPoly{
    abstract void eat();
}

class CatPoly extends AnimalPoly{
    @Override
    void eat() {
        System.out.println("吃鱼");
    }

    public void work(){
        System.out.println("抓老鼠");
    }
}

class DogPoly extends AnimalPoly{
    public void eat(){
        System.out.println("吃骨头");
    }

    public void work(){
        System.out.println("看家");
    }
}
