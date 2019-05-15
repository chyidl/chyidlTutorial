/*
 * BooksTestDrive.java
 * chap03
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/11/19 16:29.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

public class BooksTestDrive
{
    public static void main(String[] args)
    {
        Books[] myBooks = new Books[3];
        
        myBooks[0] = new Books();
        myBooks[1] = new Books();
        myBooks[2] = new Books();

        int x = 0;
        myBooks[0].title = "The Grapes of Java";
        myBooks[1].title = "The Java Gatsby";
        myBooks[2].title = "The Java Cookbook";
        myBooks[0].author = "bob";
        myBooks[1].author = "sue";
        myBooks[2].author = "ian";

        while (x < 3) {
            System.out.println(myBooks[x].title);
            System.out.print(" by ");
            System.out.println(myBooks[x].author);
            x += 1;
        }
    }
}

