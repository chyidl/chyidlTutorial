/*
 * MyDrawPanel.java
 * chap12
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/24/19 23:28.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

import java.awt.*;
import javax.swing.*;

/**
 * Make subclass of JPanel, a widget that you can add to a frame
 * just like anything else. Except this one is your own customized
 * widget.
 * */
public class MyDrawPanel extends JPanel {
    
    /**
     * This is the Big Important Graphics method you will never call 
     * this yourself.
     * */
    public void paintComponent(Graphics g) {
        Graphics2D g2d  = (Graphics2D) g;

        int red = (int) (Math.random() * 255);
        int green = (int) (Math.random() * 255);
        int blue = (int) (Math.random() * 255);
        Color startColor = new Color(red, green, blue);

        red = (int) (Math.random() * 255);
        green = (int) (Math.random() * 255);
        blue = (int) (Math.random() * 255);
        Color endColor = new Color(red, green, blue);

        GradientPaint gradient = new GradientPaint(70, 70, startColor, 150, 150, endColor);
        g2d.setPaint(gradient);
        g2d.fillOval(70, 70, 100, 100);
    }
}

