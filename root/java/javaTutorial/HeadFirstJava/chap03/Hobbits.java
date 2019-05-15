/*
 * Hobbits.java
 * chap03
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/11/19 16:35.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

public class Hobbits
{
    String name;

    public static void main(String[] args)
    {
        Hobbits[] h = new Hobbits[3];
        int z = 0;
        while (z < 3) {
            h[z] = new Hobbits();
            h[z].name = "bilbo";
            
            if (z == 1) {
                h[z].name = "frodo";
            }
            
            if (z == 2) {
                h[z].name = "sam";
            }
            System.out.println(h[z].name + " is a ");
            System.out.println("good Hobbit name");
            z += 1;
        }
    }
}

