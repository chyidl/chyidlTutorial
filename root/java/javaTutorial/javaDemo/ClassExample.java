/*
 * ClassExample.java
 * javaPrj
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 03/28/19 18:14.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */
import java.util.Properties;


public class ClassExample
{
    // don't make main() method public, there is no compilation error. You will runtime error.
    // don't make main() method static, there is no compilation error. You will runtime error.
    // The purpose of main method in Java is to be program execution start point.
    // JNI (Java Native Interface) is the tool that we use how to bridge between the virtual machine world, and the world of C,C++,etc..
    // java.exe is a super simple C application that parses the command line, creates a new String array in the JVM to hold those arguments. 
    // parses out the class name that you specified as containing main(), uses JNI calls to find the main() methods itself. then invokes the main()
    // method, passing in the newly created string array as a parameter.
    public static void main(String[] args)
    {
        // <Class> <variable> = new <Call to Class Constructor>
        ClassDeclare c = new ClassDeclare();
        
        // Set system property from code using System.setProperty() method.
        System.setProperty("custom_key", "custom_value");

        // List all System properties 
        Properties pros = System.getProperties();
        pros.list(System.out);
        
        // Get a particular System property given its key
        // Return the property value or null 
        System.out.println(System.getProperty("java.home"));
        System.out.println(System.getProperty("java.library.path"));
        System.out.println(System.getProperty("java.ext.dirs"));
        System.out.println(System.getProperty("java.class.path"));
    }
}

