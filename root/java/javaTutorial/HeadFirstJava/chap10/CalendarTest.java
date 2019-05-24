/*
 * CalendarTest.java
 * chap10
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/23/19 12:34.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

import java.util.Calendar;

public class CalendarTest {

    public static void main(String[] args)
    {
        Calendar c = Calendar.getInstance();
        // Notice the month is zero based
        c.set(2019, 4, 21, 00, 00);
        // Convert this to big amount of milliseconds
        long day1 = c.getTimeInMillis(); 
        day1 += 1000 * 60 * 60; 
        // Add an hour's worth of millis, then update the time
        c.setTimeInMillis(day1); 
        System.out.println("new hour " + c.get(c.HOUR_OF_DAY));
        // Add 35 days to the date, which should move us into February.
        c.add(c.DATE, 35);
        System.out.println("add 35 days " + c.getTime());
        // roll 35 days onto this date, this rolls the date ahead 35 days, but does not change the month.
        c.roll(c.DATE, 35);
        System.out.println("roll 35 days " + c.getTime());
        // We're not incrementing here, just doing a "set" of the date
        c.set(c.DATE, 1);
        System.out.println("set to 1 " + c.getTime());
    }
}

