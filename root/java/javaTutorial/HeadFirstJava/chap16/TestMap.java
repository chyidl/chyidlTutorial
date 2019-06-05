/*
 * TestMap.java
 * chap16
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 06/05/19 10:27.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

import java.util.*;

public class TestMap {

    public static void main(String[] args)
    {
        // HashMap needs two type parameters one for the key and one for the value.
        HashMap<String, Integer> scores = new HashMap<String, Integer>();
        
        // Use put() instead of add(), and now of course it takes two arguments (key, value)
        scores.put("Kathy", 42);
        scores.put("Bert", 343);
        scores.put("Skyler", 420);
    
        // When you print a Map, it gives you the key=value, in braces{} 
        // instead of the brackets [] you see when you print lists and sets
        System.out.println(scores);
        // The get() method takes a key, and returns the value (in this case, and Integer)
        System.out.println(scores.get("Bert"));
    }
}

