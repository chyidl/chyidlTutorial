/*
 * TextArea1.java
 * chap13
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/26/19 08:47.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class TextArea1 implements ActionListener {
    
    JTextArea text;

    public static void main(String[] args)
    {
        TextArea1 gui = new TextArea1();
        gui.go();
    }

    public void go() {
        JFrame frame = new JFrame();
        JPanel panel = new JPanel();
        JButton button = new JButton("Just Click it");
        button.addActionListener(this);
        text = new JTextArea(10, 20);
        // Turn on line wrapping
        text.setLineWrap(true);
        
        // Make a JScrollPane and give it the text area that it's going to scroll for
        JScrollPane scroller = new JScrollPane(text);
        // Tell the scroll pane to use only a vertical scroller
        scroller.setVerticalScrollBarPolicy(ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS);
        scroller.setHorizontalScrollBarPolicy(ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER);
        
        // You give the text area to the scroll pane, than add the scroll pane to the pane. 
        // You don't add the text area directly to the pane!
        panel.add(scroller);

        frame.getContentPane().add(BorderLayout.CENTER, panel);
        frame.getContentPane().add(BorderLayout.SOUTH, button);

        frame.setSize(350, 300);
        frame.setVisible(true);
    }

    public void actionPerformed(ActionEvent ev) {
        // Insert a new line so the word go on a separate line 
        text.append("button clicked \n");
    }
}

