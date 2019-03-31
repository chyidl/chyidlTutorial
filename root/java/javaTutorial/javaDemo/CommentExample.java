/*
 * CommentExample.java
 * javaDemo
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 03/29/19 10:17.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

/*
 * 1. Single Line Comment:  // 
 * 2. Multi Line Comment: 
 * 3. Documentation Comment: 
 *
 * Java comments have no impact on application performance as well.
 *
 * Java Comments Best Practices:
 *  1. Do not use unnecessary comments in sourcecode. If your code needs more than normal explanation, then possibly re-factor your code 
 *  2. Keep comments indentation uniform and match for best readability 
 *  3. Comments are for human so use simple language to explain.
 *  4. Always add documentation comments in your sourcecode.
 * */


public class CommentExample
{   
    /**
     * Launches the application
     *
     * @param args - Application startup arguments
     * */
    public static void main(String[] args)
    {
        getMessage("Lokesh", "India");
        
    }

    /**
     * Return welcome message for a customer by customer name and location
     * @param name - Name of the visitor 
     * @param region - Location 
     * @return - Welcome message
     * */
    public static String getMessage (String name, String region) 
    {
        StringBuilder builder = new StringBuilder();
        builder.append("hello ");
        builder.append(name);
        builder.append(", Welcome to ");
        builder.append(region);
        builder.append(" !!");
        return builder.toString();
    }
}

