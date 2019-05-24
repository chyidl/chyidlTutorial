/*
 * Foof.java
 * chap10
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/22/19 21:35.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

public class Foof {
    // can't change size 
    final int size = 3;
    final int whuffie;

    Foof() {
        // Now you can't change whuffie
        whuffie = 42;
    }
    
    void doStuff(final int x) {
        // you can't change x
    }

    void doMore() {
        final int z = 7;
        // you can't change z 
    }

    public static void main(String[] args)
    {
        
    }
}

