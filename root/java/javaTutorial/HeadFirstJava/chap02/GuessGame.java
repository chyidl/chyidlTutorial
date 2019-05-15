/*
 * GuessGame.java
 * chap02
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/11/19 10:41.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

/**
 * The GuessGame object's startGame() method is where the entire game plays out.
 * It cretes three players,then "thinks" of a random number
 * */
public class GuessGame
{
    // GuessGame has three instance variable for the three Player Objects;
    Player p1;
    Player p2;
    Player p3;

    public void startGame() {
        // Create three Player objects and assign them to the three Player instance variable
        p1 = new Player();
        p2 = new Player();
        p3 = new Player();
        
        // declare three variable to hold the three guesses the Player make
        int guessp1 = 0;
        int guessp2 = 0;
        int guessp3 = 0;
        
        // declare three variable to hold a true or false based on the player answer
        boolean p1isRight = false;
        boolean p2isRight = false;
        boolean p3isRight = false;

        // make a "target" number that the player have to guess 
        int targetNumber = (int) (Math.random() * 10); 
        System.out.println("I'm thinking of a number between 0 and 9...");

        while (true) {
            System.out.println("Number to guess is " + targetNumber);
            
            // Call each player guess() method
            p1.guess();
            p2.guess();
            p3.guess();
            
            // get each player's guess (the result of their guess() method running) by accessing the number variable of each player
            guessp1 = p1.number;
            System.out.println("Player one guessed " + guessp1);

            guessp2 = p2.number;
            System.out.println("Player two guessed " + guessp2);

            guessp3 = p3.number;
            System.out.println("Player three guessed " + guessp3);
            
            // Check each player guess to see if it matches the target number if a player is right the set that player variable is right.
            if (guessp1 == targetNumber) {
                p1isRight = true;
            }
            if (guessp2 == targetNumber) {
                p2isRight = true;
            }
            if (guessp3 == targetNumber) {
                p3isRight = true;
            }
            
            // If player one OR player two OR player three is right 
            if (p1isRight || p2isRight || p3isRight) {
                System.out.println("We have a winner!");
                System.out.println("Player one got it right? " + p1isRight);
                System.out.println("Player two got it right? " + p2isRight);
                System.out.println("Player three got it right? " + p3isRight);
                System.out.println("Game is over.");
                break;
            } else {
                System.out.println("Players will have to try again.");
            }
        }
    }
}

