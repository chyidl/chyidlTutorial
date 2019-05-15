/*
 * Triangle.java
 * chap03
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/11/19 18:52.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

public class Triangle
{
    double area;
    int height;
    int length;

    public static void main(String[] args)
    {
        int x = 0;
        Triangle[] ta = new Triangle[4];
        
        while (x < 4) {
            ta[x] = new Triangle();
            ta[x].height = (x + 1) * 2;
            ta[x].length = x + 4;
            ta[x].setArea();
            System.out.print("triangle "+x+", area");
            System.out.println(" = " + ta[x].area);
            x += 1;
        }
        int y = x;
        x = 27;
        Triangle t5 = ta[2];
        ta[2].area = 343;
        System.out.print("y = " + y);
        System.out.println(", t4 area = "+ t5.area);
    }

    void setArea() {
        area = (height * length) / 2;
    }
}

