#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# square_root_binary_search_implement.py
# python
#
# 🎂"Here's to the crazy ones. The misfits. The rebels.
# The troublemakers. The round pegs in the square holes.
# The ones who see things differently. They're not found
# of rules. And they have no respect for the status quo.
# You can quote them, disagree with them, glority or vilify
# them. About the only thing you can't do is ignore them.
# Because they change things. They push the human race forward.
# And while some may see them as the creazy ones, we see genius.
# Because the poeple who are crazy enough to think thay can change
# the world, are the ones who do."
#
# Created by Chyi Yaqing on 02/19/19 13:14.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Square root of an integer:

A Better Solution to do Binary Search:
    1) Start with 'start'=0, end ='x'
    2) Do following while 'start' is smaller than or equal to 'end'
        a) Compute 'mid' as start+ (end-start)//2
        b) Compare mid*mid with x
        c) If x is equal to mid*mid, return mid
        d) if x is greater, do binary search between mid+1 and end. In this
        case, we also update ans(Note that we need floor)
        e) If x is smaller, do binary search between start and mid

Find square root of number upto given precision using binary search
    Given a positive number n and precision p. find the square root of number
    upto p decimal places using binary search

    1) As the square root of number lies in range 0 <= squareRoot <= number,
    therefore, initialize start and end as: start=0, end=number.
    2) Compare the square of mid integer with the given number. If it is equal
    to the number, then we found our integral part, else look for the same in
    left or right side depending upon the scenario
    3) Once we are done with finding the integral part, start computing the
    fractional part.
    4) Initialie the increment variable by 0.1 and iteratively compute the
    fractional part upto p places. For each iteration, increment changes to
    1/10th of it's previous value.
    5) Finally return the answer computed.
"""


# Python3 program to find flooe (sqrt(x))
# Returns floor of square root of x
def floorSqrt(x):
    # Base cases
    if (x == 0 or x == 1):
        return x

    # Do Binary Search for floor(sqrt(x))
    start = 1
    end = x
    while (start <= end):
        mid = start + (end-start)/2

        # If x is a perfect square
        if (mid*mid == x):
            return mid

        # Since we need floor, we update answer when mid*mid is smaller than
        # x, and move closer to sqrt(x)
        if (mid * mid < x):
            start = mid + 1
            ans = mid
        else:
            # If mid*mid is greater than x
            end = mid - 1

    return ans


# driver code
x = 11
print(floorSqrt(x))


# Python3 implementation to find square root of given number upto given
# precision using binary search
# Function to find square root of given number upto given precision
def squareRoot(number, precision):
    start = 0
    end = number

    # For computing integral part of square root of number
    while (start <= end):
        mid = start + (end-start)//2

        if (mid * mid == number):
            ans = mid
            break

        # incrementing start if integral part lies on right side of the mid
        if (mid * mid < number):
            start = mid + 1
            ans = mid

        # decrementing end if integral part lies on the left side of the mid
        else:
            end = mid - 1

    # For computing the fractional part of square root upto given precision
    increment = 0.1
    for i in range(0, precision):
        while (ans * ans <= number):
            ans += increment

        # loop terminates when ans * ans > number
        ans = ans - increment
        increment = increment / 10

    return ans


# Driver code
print(round(squareRoot(50, 3),3))
print(round(squareRoot(10, 4), 4))
