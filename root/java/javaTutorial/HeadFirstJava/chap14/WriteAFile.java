/*
 * WriteAFile.java
 * chap14
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/27/19 10:20.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

import java.io.*;

public class WriteAFile {

    public static void main(String[] args)
    {
        /**
         * All the I/O stuff must be in a try/catch Everything can throw an IOException.
         * */
        try {
            // If the file "Foo.txt" doesn't exist, FileWriter will create it.
            FileWriter writer = new FileWriter("Foo.txt");
            // The write() method takes a String 
            writer.write("hello foo!");
            // Close it when you're done!
            writer.close();
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }
}

