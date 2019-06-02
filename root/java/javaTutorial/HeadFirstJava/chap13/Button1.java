/*
 * Button1.java
 * chap13
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/25/19 22:12.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

import javax.swing.*;
import java.awt.*;

public class Button1 {
    
    public static void main(String[] args)
    {
        Button1 gui = new Button1();
        gui.go();
    }

    public void go() {
        JFrame frame = new JFrame();
        JButton button = new JButton("Click This!");
        // A bigger font will force the frame to allocate more space for the button height
        Font bigFont  = new Font("serif", Font.BOLD, 28);
        button.setFont(bigFont);
        frame.getContentPane().add(BorderLayout.NORTH, button);
        frame.setSize(200, 200);
        frame.setVisible(true);
    }
}

