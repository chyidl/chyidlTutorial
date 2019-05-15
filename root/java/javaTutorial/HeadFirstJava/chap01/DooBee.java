/*
 * DooBee.java
 * chap00
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/11/19 09:19.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

public class DooBee
{
    public static void main(String[] args)
    {
        int x = 1;
        while(x < 3) {
            System.out.print("Doo");
            System.out.print("Bee");
            x += 1;
        }
        if (x == 3) {
            System.out.print("Do");
        }
    }
}

