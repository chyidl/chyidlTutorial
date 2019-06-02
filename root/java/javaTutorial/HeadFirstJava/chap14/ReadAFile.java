/*
 * ReadAFile.java
 * chap14
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/27/19 11:18.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

import java.io.*;

public class ReadAFile {

    public static void main(String[] args)
    {
        try {
            File myFile = new File("MyText.txt");
            // A FileReader is connection steam for cgaracter, that connects to a text file
            FileReader fileReader = new FileReader(myFile);
            // Chain the FileReader to a BufferedReader for more efficient reading.
            // It'll go back to the file to read only when the buffer is empty(because the program has read everything in it)
            BufferedReader reader = new BufferedReader(fileReader);
            
            // Make a String variable to hold each line as the line is read
            String line = null;

            while ((line = reader.readLine()) != null) {
                // This says. "Read a line of text, and assign it to the String variable line.
                // While that variable is not null"
                System.out.println(line);
            }
            reader.close();
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
}

