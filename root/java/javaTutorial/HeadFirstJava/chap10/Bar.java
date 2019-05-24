/*
 * Bar.java
 * chap10
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/22/19 18:18.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

public class Bar {

    public static final double BAR_SIGN;
    
    /**
     * This code runs as soon as the class is loaded, 
     * before any static method is called and even before any static
     * variable can be used.
     * */
    static {
        BAR_SIGN = (double) Math.random();
        System.out.println(BAR_SIGN);
    }

    public static void main(String[] args)
    {
        System.out.println("Start main...");    
    }
}

