/*
 * Pond.java
 * chap14
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/26/19 23:22.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

import java.io.*;

public class Pond implements Serializable {
    
    // Class Pond has one instance variable a Duck
    private Duck duck = new Duck();

    public static void main(String[] args)
    {
        Pond myPond = new Pond();
        try {
            FileOutputStream fs = new FileOutputStream("Pond.ser");
            ObjectOutputStream os = new ObjectOutputStream(fs);

            os.writeObject(myPond);
            os.close();
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
    
    /**
     * Duck is not serializable, It doesn't implement Serializable
     * */
    public class Duck {
        // duck code here
    }
}

