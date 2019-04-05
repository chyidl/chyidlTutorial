package com.chyidl.tutorial;

// 抽象类
abstract class Caravan{
    private double price;
    private String model;
    private String year;

    public abstract void goFast(); // 抽象方法
    public abstract void changeColor();
}

class Volkswagen extends Caravan{

    // 实现抽象方法
    @Override
    public void goFast() {

    }

    @Override
    public void changeColor() {

    }
}

public class ModifierTest {
    private static int numInstances = 0;
    private boolean myFlag;  // 访问私有修饰符-private
    static final double weeks = 9.5; // 静态变量也被称为类变量，局部变量不能被声明为static变量
    protected static final int BOXWIDTH = 42; // 受保护的访问修饰符-protected

    protected static int getCount() {
        return numInstances;
    }

    private static  void addInstance(){
        numInstances++;
    }

    // 构造函数
    ModifierTest(){
        ModifierTest.addInstance();
    }

    // 共有访问修饰符-public
    // 静态方法不能使用非静态变量，静态方法从参数类标得到数据
    public static void main(String[] args) {
        System.out.println("Starting with " + ModifierTest.getCount() + " instances");
        for (int i = 0; i<500; i++){
            new ModifierTest();
        }
        System.out.println("Created " + ModifierTest.getCount() + " instances");
    }

    public boolean isMyFlag() {
        return myFlag;
    }

    public void setMyFlag(boolean myFlag) {
        this.myFlag = myFlag;
    }
}
