/*
 * QuizCardBuilder.java
 * chap14
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/27/19 10:26.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

import java.util.*;
import java.awt.event.*;
import javax.swing.*;
import java.awt.*;
import java.io.*;

public class QuizCardBuilder {
    
    private JTextArea question;
    private JTextArea answer;
    private ArrayList<QuizCard> cardList; 
    private JFrame frame;

    public void go() {
        // build and display gui, including making and registering event listeners.
        // the MenuBar, Menu and MenuItems code.
        frame = new JFrame("Quiz Card Builder");
        JPanel mainPanel = new JPanel();
        Font bigFont = new Font("sanserif", FOnt.BOLD, 24);
        question = new JTextArea(6, 20);
        question.setLineWrap(true);
        question.setWrapStyleWord(true);
        question.setFont(bigFont);

        JScrollPane qScroller = new JScrollPane(question);
        qScroller.setVerticalScrollBarPolicy(ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS);
        qScroller.setHorizontalScrollBarPolicy(ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER);

        answer = new JTextArea(6, 20);
        answer.setLineWrap(true);
        answer.setWrapStyleWord(true);
        answer.setFont(bigFont);

        JScrollPane aScroller = new JScrollPane(answer);
        aScroller.setVerticalScrollBarPolicy(ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS);
        aScroller.setHorizontalScrollBarPolicy(ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER);

        JButton nextButton = new JButton("Next Card");
        cardList = new ArrayList<QuizCard>();

        JLabel qLabel = new JLabel("Question:");
        JLabel aLabel = new JLabel("Answer:");

        mainPanel.add(qLabel);
        mainPanel.add(qScroller);
        mainPanel.add(aLabel);
        mainPanel.add(aScroller);
        mainPanel.add(nextButton);
        nextButton.addActionListener(new NextCardListener());
        JMenuBar menuBar = new JMenu();
        JMenu fileMenu = new JMenu("File");
        JMenuItem newMenuItem = new JMenuItem("New");
        JMenuItem saveMenuItem = new JMenuItem("Save");
        newMenuItem.addActionListener(new NewMenuListener());
        saveMenuItem.addActionListener(new SaveMenuListener());
        fileMenu.add(newMenuItem);
        fileMenu.add(saveMenuItem);
        menuBar.add(fileMenu);
        frame.setJMenuBar(menuBar);
        frame.getContentPane().add(BorderLayout.CENTER, mainPanel);
        frame.setSize(500, 600);
        frame.setVisible(true);
    }

    // Inner class 
    private class NextCardListener implements ActionListener {
        /**
         * Triggered when user hits 'Next Card' button; means the user wants to store
         * that card in the list and start a new card.
         * */
        public void actionPerformed(ActionEvent ev) {
            // Add the current card to the list and clear the text areas
            QuizCard card = new QuizCard(question.getText(), answer.getText());
            cardList.add(card);
            clearCard();
        }
    }

    private class SaveMenuListener implements ActionListener {
        /**
         * Triggered when use choose 'Save' from the File menu; means the user wants to save all
         * the cards in the current list as a 'set' (like, Quantum Mechanics Sets, Holly wood Trivia,
         * Java Rules, etc.).
         * */
        public void actionPerformed(ActionEvent ev) {
            // bring up a file dialog box
            // let the user name and save the set
            QuizCard card = new QuizCard(question.getText(), answer.getText());
            cardList.add(card);

            JFileChooser fileSave = new JFileChooser();
            fileSave.showSaveDialog(frame);
            saveFile(fileSave.getSelectedFile());
        }
    }

    private class NewMenuListener implements ActionListener {
        /**
         * triggered by choosing 'New' from the File menu, means the wants to start to 
         * a brand new set (so we clear out the card list and the text areas).
         * */
        public void actionPerformed(ActionEvent ev) {
            // clear out the card list, and clear out the text areas
            cardList.clear();
            clearCard();
        }
    }

    private void clearCard() {
        question.setText("");
        answer.setText("");
        question.requestFocus();
    }

    private void saveFile(File file) {
        // iterate through the list of cards, and write each one out to a text file 
        // in a parseable way (in other words, with clear separations between parts)
        try {
            BufferedWriter writer = new BufferedWriter(new FileWriter(file));

            for (QuizCard card: cardList) {
                writer.write(card.getQuestion() + "/");
                writer.write(card.getAnswer() + "\n");
            }
            writer.close();
        } catch (IOException ex) {
            System.out.println("couldn't write the cradList out");
            ex.printStackTrace();
        }
    }

    public static void main(String[] args)
    {
        QuizCardBuilder builder = new QuizCardBuilder();
        builder.go();
    }
}

