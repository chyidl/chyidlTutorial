/*
 * StringRemoveWhiteSpaces.java
 * javaPrj
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 03/28/19 17:24.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

public class StringRemoveWhiteSpaces
{
    public static void main(String[] args)
    {
        String blogName = "  how to  do   in   java .   com  ";

        // Using regular expression, to replace 2 or more white spaces with single space, 
        // \s matches a space, tab, new line, carriage return, form feed or vertical tab.
        // + says one or more occurrences.
        // Note that this method with not trim the String, That means there might be single
        // space at start at end of string, if original string has such white spaces at beginning or end.
        String nameWithProperSpacing = blogName.replaceAll("\\s+", " ");
        System.out.println(nameWithProperSpacing);
        
        // Java remove leading whitespaces from String 
        nameWithProperSpacing = nameWithProperSpacing.replaceAll("^\\s+", "");
        System.out.println(nameWithProperSpacing);

        // Java remove trailing spaces of a String 
        nameWithProperSpacing = nameWithProperSpacing.replaceAll("\\s+$", "");
        System.out.println(nameWithProperSpacing);

    }
}

