package com.chyidl.tutorial;

/**
 * Java抽象类
 * 抽象类不能实例化对象，所以抽象类必须被继承才能被使用，
 * 一个类只能继承一个抽象类，而一个类却可以实现多个接口
 *
 * 如果一个类包含抽象方法，那么该类必须是抽象类
 * 任何子类必须重写父类的抽象方法，或者声明自身为抽象类
 * 抽象类不能被实例化，只有抽象类的非抽象子类可以创建对象
 * 抽象类中不一定包含抽象方法，但是有抽象方法的类必须是抽象类
 * 抽象类中的抽象方法只是声明，不包含方法体，就是不给出方法的具体实现也就是方法的具体功能
 * 构造方法，类方法不能声明为抽象方法
 * 抽象类的子类必须给出抽象类中的抽象方法的具体实现，除非该子类也是抽象类
 * */

abstract class EmployeeAbstract{
    private String name;
    private String address;
    private int number;

    public EmployeeAbstract(String name, String address, int number){
        System.out.println("Constructing an Employee");
        this.setName(name);
        this.setAddress(address);
        this.setNumber(number);
    }

    public double computePay(){
        System.out.println("Inside Employee computePay");
        return 0.0;
    }

    public void mailCheck(){
        System.out.println("Mailing a check to " + this.getName() + " " + this.getAddress());
    }

    public String toString(){
        return getName() + " " + getAddress() + " " + getNumber();
    }

    public String getName(){
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
}

class SalaryAbstract extends EmployeeAbstract{
    private double salary; // Annual salary

    public SalaryAbstract(String name, String address, int number, double salary){
        super(name, address, number);
        setSalary(salary);
    }

    public void mailCheck(){
        System.out.println("Within mailCheck of Salary class ");
        System.out.println("Mailing check to  " + getName() + " with salary " + salary);
    }

    public double computePay(){
        System.out.println("Computing salary pay for " + getName());
        return salary/52;
    }

    public double getSalary() {
        return salary;
    }

    public void setSalary(double salary) {
        this.salary = salary;
    }
}

public class AbstractTest {

    public static void main(String[] args){
        SalaryAbstract s = new SalaryAbstract("Mohd Mohtashim", "Ambehta, UP", 3, 3600.00);
        EmployeeAbstract e = new SalaryAbstract("John Adams", "Boston, MA", 2, 2400.00);

        System.out.println("Call mailCheck using Salary reference --");
        s.mailCheck();

        System.out.println("\nCall mailCheck using Employee reference --");
        e.mailCheck();
    }
}
