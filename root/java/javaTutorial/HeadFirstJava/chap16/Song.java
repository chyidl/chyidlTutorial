/*
 * Song.java
 * chap16
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 06/04/19 00:03.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

/**
 * The Song class needs to implement Comparable.
 * */
public class Song  implements Comparable<Song> {
    
    // Four instance variable for the four song attributes in the file.
    String title;
    String artist;
    String rating;
    String bpm;
    
    /**
     * The HashSet (or anyone else calling this method sends it another Song)
     * */
    public boolean equals(Object aSong) {
        Song s = (Song) aSong;
        /**
         * The Great news is that title is a String, and String have an override equals() method. 
         * So all we have to do is ask one title if it's equal to the other song's title.
         * */
        return getTitle().equals(s.getTitle());
    }

    public int hashCode() {
        /**
         * the String class has an overridden hasCode() method, so you can just return the 
         * result of calling hasCode() on the title. Notice how hasCode() and equals() are 
         * using the Same instance variable.
         * */
        return title.hashCode();
    }

    /**
     * The sort() method sends a Song to compareTo() to see 
     * how that Song compares to the Song on which the method was invoked.
     * */
    public int compareTo(Song s) {
        /**
         * Simple! We just pass the work on to the title String objects,
         * since we know String have a compareTo() method.
         * */
        return title.compareTo(s.getTitle());
    }

    Song(String t, String a, String r, String b) {
        // The variables are all set in the constructor when the new song is created.
        title = t;
        artist = a;
        rating = r;
        bpm = b;
    }
    
    /**
     * The getter methods for the four attributes.
     * */
    public String getTitle() {
        return title;
    }

    public String getArtist() {
        return artist;
    }

    public String getRating() {
        return rating;
    }

    public String getBpm() {
        return bpm;
    }
    
    /**
     * We override toString(), because when you do a System.out.println(a Song Object),
     * we want to see the title. When you do a System.out.println(a ListOfSongs), it 
     * calls the toString() method of EACH element in the list.
     * */
    public String toString() {
        return title;
    }
}

