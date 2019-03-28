/*
 * ClassDeclare.java
 * javaPrj
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 03/28/19 17:51.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

public class ClassDeclare
{
    // Fields of a class represent properties (also called state attributes) of objects of 
    // that class. The fields are declared inside the body of the class.
    String name;
    String gender;
    
    // In Java, methods may - 
    //  accept zero or more arguments 
    //  return void or a single value 
    //  be overloaded - means we can define more than one method with same name but different syntax
    //  be overrided  - means we can define methods with same syntax in parent and child classes
    public void eat() 
    {
        System.out.println("I am a methods, about eat");
    }
    
    // A constructor is a named block of code that is used to initialize an object of a class immediately.
    // after the object is created.
    // The constructor name is the same as the simple name of the class.
    // The constructor name is followed by a pair of opening and closing parentheses, which may include parameters.
    // Unlike a method, a constuctor does not have a return type.
    // Remember that is the name of a construct is the same as the simple name of the class, it could be a method or 
    // a constructor, If it is specifies a return type, it is a method. If it does not specify a return type, it is a constructor.
    public ClassDeclare() {
        System.out.println("I am ClassDeclare constructor!");
    }
    
    // An instance initialization block, also called instance initializer
    // An instance initializer is simply a block of code inside the body of a class, but outside of any methods or constructors.
    // An instance initializer does not have a name, Its code is simply placed inside an opening brace and a closing brace.
    // All instance initializers are executed before any constructor. An instance initializer cannot have a return statement.
    {
        System.out.println("I am ClassDeclare instance initializer block!");
    }

    // Static Initialization Block 
    // An instance initializer is executed once per object whereas a static initializer is executed only once for a class when the 
    // class definition is loaded into JVM.
    // All static initializers are executed in textual order in which they appear, and execute before any instance initializers.
    static {
        System.out.println("I am ClassDeclare static initializer block - 1!");
    }
    static {
        System.out.println("I am ClassDeclare static initializer block - 2!");
    }
}

