/*
 * Animal.java
 * chap09
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/17/19 13:54.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

public class Animal {
    
    private String name;

    public String getName() {
        return name;
    }

    public Animal(String theName) {
        name = theName;
    }

    public Animal() {
        System.out.println("Making an Animal");
    }
}

