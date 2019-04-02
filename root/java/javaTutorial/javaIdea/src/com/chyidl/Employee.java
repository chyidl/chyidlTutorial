package com.chyidl;

import java.io.*;

public class Employee {
    String name;
    private String designation;
    private int age;
    private double salary;

    // Employee类构造函数
    public Employee(String name){
        this.name = name;
    }

    public String getDesignation() {
        return designation;
    }

    public void setDesignation(String designation) {
        this.designation = designation;
    }

    public int getAge() {
        return age;
    }

    // 设置age值
    public void setAge(int age) {
        this.age = age;
    }

    public double getSalary() {
        return salary;
    }

    public void setSalary(double salary) {
        this.salary = salary;
    }

    // 打印信息
    public void printEmployee(){
        System.out.println("Name:" + name);
        System.out.println("Age:" + getAge());
        System.out.println("Designation:" + getDesignation());
        System.out.println("Salary:"+getSalary());
    }
}
