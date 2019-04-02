package com.chyidl;


class Dog {
    // 类变量
    static String name = "Dobby";

    // 成员变量
    private String breed;
    private String color;
    private int age;

    // 构造方法，一个类可以有多个构造方法
    public Dog(){
        System.out.println("This is class Dog constract function");
    }

    void brking() {
        // 局部变量
        System.out.printf("I am %s, wang wang",this.getBreed());
    }

    void hungry() {

    }

    void sleeping(){

    }

    public String getBreed() {
        return breed;
    }

    public void setBreed(String breed) {
        this.breed = breed;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
}

public class ClassInstanceProgram {
    public static void main(String[] args) {
        // 实例化对象
        Dog dog = new Dog();
        // 通过方法设定age
        dog.setAge(25);
        dog.setColor("Blue");
        dog.setBreed("Labrador");
        // 访问类中的变量
        System.out.println("How old are you? " + dog.getAge());
        // 访问类中的方法
        dog.brking();
    }
}
