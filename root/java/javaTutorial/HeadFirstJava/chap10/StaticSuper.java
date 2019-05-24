/*
 * StaticSuper.java
 * chap10
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/23/19 14:37.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

public class StaticSuper {

    static {
        System.out.println("super static block");
    }
    
    StaticSuper() {
        System.out.println("super constructor");
    }
}

