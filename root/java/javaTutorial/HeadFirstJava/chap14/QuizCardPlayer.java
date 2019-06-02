/*
 * QuizCardPlayer.java
 * chap14
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/27/19 11:27.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

import java.util.*;
import java.awt.event.*;
import javax.swing.*;
import java.io.*;

public class QuizCardPlayer {

    private JTextArea display;
    private JTextArea answer;
    private ArrayList<QuizCard> cardList;
    private QuizCard currentCard;
    private int currentCardIndex;
    private JFrame frame;
    private JButton nextButton;
    private boolean isShowAnswer;
    
    public static void main (String[] args) {
        QuizCardPlayer reader = new QuizCardPlayer();
        reader.go();
    }

    public void go() {
        // build and display gui 
        frame = new JFrame("Quiz Card Player");
        JPanel mainPanel = new JPanel();
        Font bigFont = new Font("sanserif", Font.BOLD, 24);

        display = new JTextArea(10, 20);
        display.setFont(bigFont);

        display.setLineWrap(true);
        display.setEditable(false);

        JScrollPane qScroller = new JScrollPane(display);
        qScroller.setVerticalScrollBarPolicy(ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS);
        qScroller.setHorizontalScrollBarPolicy(ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER);
        nextButton = new JButton("Show Question");
        mainPanel.add(qScroller);
        mainPanel.add(nextButton);
        nextButton.addActionListener(new NextCardListener());

        JMenuBar menuBar = new JMenuBar();
        JMenu fileMenu = new JMenu("File");
        JMenuItem loadMenuItem = new JMenuItem("Load card set");
        loadMenuItem.addActionListener(new OpenMenuListener());
        fileMenu.add(fileMenu);
        menuBar.add(fileMenu);
        frame.setJMenuBar(menuBar);
        menuBar.add(fileMenu);
        frame.setJMenuBar(menuBar);
        frame.getContentPane().add(BorderLayout.CENTER, mainPanel);
        frame.getSize(640, 500);
        frame.setVisible(true);
    }
    
    class NextCardListener implements ActionListener {
        public void actionPerformed(ActionEvent ev) {
            // if this is a question, show the answer, otherwise show next question 
            // set a flag for whether we're viewing a question or answer.
            if (isShowAnswer) {
                // show the answer because they've seen the question 
                display.setText(currentCard.getAnswer());
                nextButton.setText("Next Card");
                isShowAnswer = false;
            } else {
                // show the next question 
                if (currentCardIndex < cardList.size()) {
                    showNextCard();
                } else {
                    // there are no more card!
                    display.setText("That was last card");
                    nextButton.setEnabled(false);
                }
            }
        }
    }
    
    class OpenMenuListener implements ActionListener {
        public void actionPerformed(ActionEvent ev) {
            // bring up a file dialog box 
            // let the user navigate to and choose a card set to open 
            JFileChooser fileOpen = new JFileChooser();
            fileOpen.showOpenDialog(frame);
            loadFile(fileOpen.getSelectedFile());
        }
    }

    private void loadFile(File file) {
        // must build an ArrayList of cards, by reading them from a text fiel 
        // called from the OpenMenuListener event handler, reads the file one line at a time
        // and tells the makeCard() method to make a new card out of the line 
        // (one line in the file holds both the question and answer, separated by a "/")
        cardList = new ArrayList<QuizCard>();
        try {
            BufferedReader reader = new BufferedReader(new FileReader(file));
            String line = null;
            while ((line = reader.readLine()) != null) {
                makeCard(line);
            }
            reader.close();
        } catch (Exception ex) {
            System.out.println("couldn't read the card file");
            ex.printStackTrace();
        }

        // now time to start by showing the first card 
        showNextCard();
    }

    private void makeCard(String lineToParse) {
        // called by the loadFile method, takes a line from the text file 
        // and parses into two pieces--question and answer--and creates a new QuizCard 
        // and adds it to the ArrayList called CardList.

        // String split() lets you break a String into pieces.
        String[] result = lineToParse.split("/");
        QuizCard card = new QuizCard(result[0], result[1]);
        cardList.add(card);
        System.out.println("made a card");
    }

    private void showNextCard() {
        currentCard = cardList.get(currentCardIndex);
        currentCardIndex++;
        display.setText(currentCard.getQuestion());
        nextButton.setText("Show Answer");
        isShowAnswer = true;
    }
}

