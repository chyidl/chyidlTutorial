/*
 * Foo.java
 * chap18
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 06/10/19 18:24.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

public class Foo {

    void go() {
        Bar b = new Bar();
        b.doStuff();
    }

    public static void main(String[] args)
    {
        Foo f = new Foo();
        f.go();
    }
}

