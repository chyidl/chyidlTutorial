/*
 * SimpleAnimation.java
 * chap12
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/25/19 08:36.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

import javax.swing.*;
import java.awt.*;

public class SimpleAnimation {
    
    /**
     * Make two instance variables in the main GUI class, for the x and y coordinates of the circle.
     * */
    int x = 70;
    int y = 70;

    public static void main(String[] args)
    {
        SimpleAnimation gui = new SimpleAnimation();
        gui.go();
    }

    public void go() {
        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        MyDrawPanel drawPanel = new MyDrawPanel();

        frame.getContentPane().add(drawPanel);
        frame.setSize(300, 300);
        frame.setVisible(true);

        for (int i = 0; i < 130; i++) {
            // increment the x and y coordinates
            x++;
            y++;
            
            // tell the panel to repaint itself
            drawPanel.repaint();

            try {
                // slow it doen a little 
                Thread.sleep(50);
            } catch (Exception ex) {

            }
        }
    }

    class MyDrawPanel extends JPanel {
        
        public void paintComponent(Graphics g) {

            g.setColor(Color.white);
            g.fillRect(0, 0, this.getWidth(), this.getHeight());

            g.setColor(Color.green);
            g.fillOval(x, y, 40, 40);
        }
    }
}

