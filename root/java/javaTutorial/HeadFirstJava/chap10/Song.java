/*
 * Song.java
 * chap10
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/22/19 09:54.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

public class Song {
    /**
     * Instance variable value affects the behavior of the play() method.
     * */
    String title;

    public Song(String t) {
        title = t;
    }

    public void play() {
        SoundPlayer player = new SoundPlayer();
        player.playSound(title);
    }
}

