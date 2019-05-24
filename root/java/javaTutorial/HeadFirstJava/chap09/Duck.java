/*
 * Duck.java
 * chap09
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/17/19 10:23.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

public class Duck {
    
    /**
     * Instance variables live within the object they belong to, on the Heap
     * */
    int size;
    
    /**
     * Constructor Code.
     * The Constructor gives you a chance to step into the middle of new.
     *
     * The thing that separates a method from a constructor is the return type.
     * Methods must have a return type, but constructors cannot have a return type.
     * */
    public Duck(int duckSize) {
        System.out.println("Quack");
        // Use the argument value to set the size instance variable.
        size = duckSize;
        System.out.println("Size is " + size);
    }

    public Duck() {
        System.out.println("supply default size");
        size = 27;
        System.out.println("Size is " + size);
    }
}

