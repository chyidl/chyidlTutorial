/*
 * Duck.java
 * chap10
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/22/19 16:50.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

public class Duck {

    private int size; 
    private static int duckCount = 0;
    
    public Duck() {
        /**
         * Now it will keep incrementing each time the Duck constructor runs
         * because duckCount is static and won't be reset to 0
         * */
        duckCount++;
    }

    public static void main(String[] args)
    {
        // non-static method getSize() connot be referenced from a static context
        // System.out.println("Size is " + getSize()) ;   
        
    }

    public void setSize(int s) {
        size = s; 
    }

    public int getSize() {
        return size;
    }
}

