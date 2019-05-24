/*
 * SimpleGui1.java
 * chap12
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/24/19 09:58.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

import javax.swing.*;

public class SimpleGui1 {

    public static void main(String[] args)
    {
        // make a frame and a button 
        JFrame frame = new JFrame();
        JButton button = new JButton("click me");
        
        // this line makes the program quit as soon as you close 
        // the window (if you leave this out it will just sit there 
        // the screen forever)
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        // Add the button to the frame's content pane
        frame.getContentPane().add(button);

        // give the frame a size in pixels
        frame.setSize(300, 300);
        
        // finally, make it visible
        frame.setVisible(true);
    }
}

