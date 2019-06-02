/*
 * Panel1.java
 * chap13
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/26/19 07:42.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

import javax.swing.*;
import java.awt.*;

public class Panel1 {
    
    public static void main(String[] args)
    {
        Panel1 gui = new Panel1();
        gui.go();
    }

    public void go() {
        JFrame frame = new JFrame();
        JPanel panel = new JPanel();
        panel.setBackground(Color.darkGray);
        
        // Change the layout manager to be a new instance of BoxLayout
        panel.setLayout(new BoxLayout(panel, BoxLayout.Y_AXIS));

        JButton button = new JButton("shock me");
        JButton buttonTwo = new JButton("bliss");
        
        /**
         * Add the button to the panel and add the panel to the frame
         * */
        panel.add(button);
        panel.add(buttonTwo);
        frame.getContentPane().add(BorderLayout.EAST, panel);

        frame.setSize(200, 200);
        frame.setVisible(true);
    }
}

