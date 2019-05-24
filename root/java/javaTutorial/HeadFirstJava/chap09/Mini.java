/*
 * Mini.java
 * chap09
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/22/19 09:20.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

public class Mini extends Car {
    Color color;

    public Mini() {
        this(Color.Red); 
    }

    public Mini(Color c) {
        super("Mini");
        color = c;
        // more initialization 
    }

    public Mini(int size) {
        /**
         * Can't have super() and this() in the same constructor
         * Because they each must be the first statement!
         * */
        this(Color.Red);
        super(size);
    }
}

