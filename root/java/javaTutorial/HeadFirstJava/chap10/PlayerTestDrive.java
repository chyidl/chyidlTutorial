/*
 * PlayerTestDrive.java
 * chap10
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/22/19 17:55.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

public class PlayerTestDrive {

    public static void main(String[] args)
    {
        System.out.println(Player.playerCount);
        Player one = new Player("Tiger Woods");
        // Access a static variable just like a static method-with the class name.
        System.out.println(Player.playerCount);
    }
}

