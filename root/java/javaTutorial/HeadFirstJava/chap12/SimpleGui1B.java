/*
 * SimpleGui1B.java
 * chap12
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/24/19 10:29.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

import javax.swing.*;
import java.awt.event.*;  // A new import statement for the package that ActionListener and ActionEvent are in 

/**
 * Implement the interface. This says "an instance of SimpleGui1B IS-A ActionListener"
 * */
public class SimpleGui1B implements ActionListener {
    JButton button;

    public static void main(String[] args)
    {
        SimpleGui1B gui = new SimpleGui1B();
        gui.go();
    }

    public void go() {
        JFrame frame = new JFrame();
        button = new JButton("click me");

        /**
         * register your interest with the button, this says 
         * to the button, "Add me to your list of listener"
         * The argument you pass MUST be an object from a 
         * class that implements ActionListener!!
         * */
        button.addActionListener(this);

        frame.getContentPane().add(button);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 300);
        frame.setVisible(true);
    }

    /**
     * Implement the ActionListener interface actionPerformaed() method
     * */
    public void actionPerformed(ActionEvent event) {
        button.setText("I've been clicked!");
    }
}

