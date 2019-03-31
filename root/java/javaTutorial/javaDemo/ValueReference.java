/*
 * ValueReference.java
 * javaDemo
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 03/29/19 17:37.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

public class ValueReference
{
    public static void main(String[] args)
    {
        // create an instance of class Foo. 
        Foo f = new Foo("f");

        changeReference(f); // It won't change the reference!
        modifyReference(f); // It will change the object that the reference variable "f" referes to!
    }

    public static void changeReference(Foo a) {
        Foo b = new Foo("b");
        a = b;
    }

    public static void modifyReference(Foo c) {
        c.setAttribute("c");
    }
}

