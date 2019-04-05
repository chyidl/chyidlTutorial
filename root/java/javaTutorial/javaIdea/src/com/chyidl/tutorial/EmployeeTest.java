package com.chyidl.tutorial;

public class EmployeeTest {
    public static void main(String args[]) {
        // 使用构造函数创建两个对象
        Employee empOne = new Employee("James Smith");
        Employee empTwo = new Employee("Mary Anne");

        // 调用类对象的成员方法
        empOne.setAge(26);
        empOne.setDesignation("Senior Software Engineer");
        empOne.setSalary(1000);
        empOne.printEmployee();

        empTwo.setAge(21);
        empTwo.setDesignation("Software Engineer");
        empTwo.setSalary(500);
        empTwo.printEmployee();
    }
}
