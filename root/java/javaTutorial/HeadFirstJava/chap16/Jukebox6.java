/*
 * Jukebox6.java
 * chap16
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 06/05/19 06:38.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

import java.util.*;
import java.io.*;

public class Jukebox6 {
    
    ArrayList<Song> songList = new ArrayList<Song>();

    public static void main(String[] args)
    {
        new Jukebox6().go();    
    }

    public void go() {
        // We didn't change getSongs(), so it stil puts the songs in an ArrayList
        getSongs();
        System.out.println(songList);
        Collections.sort(songList);
        System.out.println(songList);

        // Here we create a new HashSet parameterized to hold songs.
        HashSet<Song> songSet = new HashSet<Song>();
        // HashSet has a simple addAll() method that can take another collection and use
        // it to populate the HashSet. It's the same as if we added each song one at a time
        songSet.addAll(songList);
        System.out.println(songSet);
    }

    void getSongs() {
        try {
            File file = new File("SongListMore.txt");
            BufferedReader reader = new BufferedReader(new FileReader(file));
            String line = null;
            while ((line = reader.readLine()) != null) {
                addSong(line);
            }
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }

    void addSong(String lineToParse) {
        String[] tokens = lineToParse.split("/");
        Song nextSong = new Song(tokens[0], tokens[1], tokens[2], tokens[3]);
        songList.add(nextSong);
    }
}

