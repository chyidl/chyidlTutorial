/*
 * RecursiveExample.java
 * javaDemo
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 04/01/19 13:09.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */
// Recursion Types 
//  1. Tail recursion -- When recursive method call is the last statement executed inside the method (usually along with a return statement)
//  2. Head recursion -- Any recursion which is not tail recursion, can be referred as head recursion.

public class RecursiveExample
{
    // Fibonacci series is a sequence of numbers where each number is defined as the sum of the two numbers proceeding it.
    // For example - 1,1,2,3,5,8,13,21,34 and so on... 
    public static int fibonacci(int n)
    {
        if (n <= 1) {
            return n;
        }
        return fibonacci(n-1) + fibonacci(n-2);
    }
    
    // The greatest common divisor (gcd) of two positive integers is the largesr integer that divides evenly into both of them.
    public static int gcd(int p, int q) {
        if (q == 0) 
            return p;
        else 
            return gcd(q, p % q);
    }

    public static void main(String[] args)
    {
        int number = 10;

        for (int i=1; i<=number; i++)
        {
            System.out.print(fibonacci(i) + " ");
        }
        
        int number1 = 40;
        int number2 = 500;

        System.out.println(gcd(number1, number2));
    }
}

