/*
 * Jukebox1.java
 * chap16
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 06/03/19 22:41.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

import java.util.*;
import java.io.*;

public class Jukebox1 {
    // We'll store the song titles in an ArrayList of Strings.
    ArrayList<String> songList = new ArrayList<String>();

    public static void main(String[] args)
    {
        new Jukebox1().go();
    }

    /**
     * The method that starts loading the file and then prints the contents of the songList ArrayList
     * */
    public void go() {
        getSongs();
        System.out.println(songList);
        // Call the static Collections sort() method
        Collections.sort(songList);
        // Then print the list again. The second print out is in alphabetical order!
        System.out.println(songList);
    }
    
    /**
     * read the file and call the addSong() method for each line.
     * */
    void getSongs() {
        try {
            File file = new File("SongList.txt");
            BufferedReader reader = new BufferedReader(new FileReader(file));
            String line = null;
            while ((line = reader.readLine()) != null) {
                addSong(line);
            }
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
    
    /**
     * The addSong method 
     * */
    void addSong(String lineToParse) {
        String[] tokens = lineToParse.split("/");
        // We only want the song title.so add only the first token to the SongList(the ArrayList)
        songList.add(tokens[0]);
    }
}

