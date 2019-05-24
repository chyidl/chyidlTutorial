/*
 * MyAnimalList.java
 * chap08
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/15/19 16:54.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

public class MyAnimalList {

    private Animal[] animals = new Animal[5];
    private int nextIndex = 0;

    public void add(Animal d) {
        /**
         * If we're not already at the limit of the dogs array, add the Dog
         * and print a message.
         * */
        if (nextIndex < animals.length) {
            animals[nextIndex] = d;
            System.out.println("Animal added at " + nextIndex);
            // Increment, to give us the next index to use
            nextIndex++;
        }
    }

    public static void main(String[] args)
    {
        
    }
}

