/*
 * StringReverse.java
 * javaPrj
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 03/28/19 17:05.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

public class StringReverse
{
    public static void main(String[] args)
    {
        String blogName = "How To Do In Java";
        String reverseString = reverseString(blogName);
        System.out.println(reverseString);
    }

    public static String reverseString(String string)
    {
        if (string.isEmpty()){
            return string;
        }
        // Calling function recurisively
        return reverseString(string.substring(1)) + string.charAt(0);
    }
}

