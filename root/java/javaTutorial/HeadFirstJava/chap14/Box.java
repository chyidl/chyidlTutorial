/*
 * Box.java
 * chap14
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/26/19 10:46.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

import java.io.*;

/**
 * No methods to implement, but when you say "implements Seriable" it say to the JVM
 * "it's OK" to serialize objects of this type.
 * */
public class Box implements Serializable {
    
    // These two value will be saved
    private int width;
    private int height;
    
    public void setWidth(int w) {
        width = w;
    }

    public void setHeight(int h) {
        height = h;
    }

    public static void main(String[] args)
    {
        Box myBox = new Box();
        myBox.setWidth(50);
        myBox.setHeight(20);

        try {
            // IO operations can throw exception
            // Connect to a file named "foo.ser" if it exists. If it done't make a new file named "foo.ser"
            FileOutputStream fs = new FileOutputStream("foo.ser");
            // Make an ObjectOutputStream chaned to the connection stream Tell it to write the object
            ObjectOutputStream os = new ObjectOutputStream(fs);
            os.writeObject(myBox);
            os.close();
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
}

