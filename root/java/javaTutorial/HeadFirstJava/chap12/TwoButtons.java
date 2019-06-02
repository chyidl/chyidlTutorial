/*
 * TwoButtons.java
 * chap12
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/25/19 05:42.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class TwoButtons {
    
    JFrame frame;
    JLabel label;

    public static void main(String[] args)
    {
        TwoButtons gui = new TwoButtons();
        gui.go();
    }

    public void go() {
        frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        /**
         * Instead of passing (this) to the button listener registration
         * method, pass a new instance of the appropriate listener class.
         * */
        JButton labelButton = new JButton("Change Label");
        labelButton.addActionListener(new LabelListener());

        JButton colorButton = new JButton("Change Circle");
        colorButton.addActionListener(new ColorListener());
        
        label = new JLabel("I'm a label");
        MyDrawPanel drawPanel = new MyDrawPanel();

        frame.getContentPane().add(BorderLayout.SOUTH, colorButton);
        frame.getContentPane().add(BorderLayout.CENTER, drawPanel);
        frame.getContentPane().add(BorderLayout.EAST, labelButton);
        frame.getContentPane().add(BorderLayout.WEST, label);

        frame.setSize(500, 500);
        frame.setVisible(true);
    }

    class LabelListener implements ActionListener {

        public void actionPerformed(ActionEvent event) {
            // inner class knoew about label
            label.setText("Ouch!");
        }
    }

    class ColorListener implements ActionListener {

        public void actionPerformed(ActionEvent event) {
            // the inner class gets to use the 'frame' instance variable, without
            // having an explicit reference to the outer class object
            frame.repaint();
        }
    }
}

