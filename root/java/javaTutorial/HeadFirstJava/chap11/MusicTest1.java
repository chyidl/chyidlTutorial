/*
 * MusicTest1.java
 * chap11
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/23/19 17:57.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

import javax.sound.midi.*;

public class MusicTest1 {

    public void play() {
        try{
            // put the risky thing in a 'try' block.
            /**
             * The Sequencer is the thing that actually causes a song to be played. 
             * think of it like a music CD player.
             * */
            Sequencer sequencer = MidiSystem.getSequencer();
            System.out.println("Successfully got a sequencer");
            sequencer.open(); 

            // Make a new Sequence 
            Sequence seq = new Sequence(timing, 4);

            // Get a new Track from the Sequence 
            Track t = seq.createTrack(); 

            // Fill the Track with MidiEvents and give the Sequence to the Sequencer 
            t.add(myMidiEvent1);
            player.setSequence(seq);

            
        } catch (MidiUnavailableException ex) {
            System.out.println("Bummer");
        }
    }

    public static void main(String[] args)
    {
        MusicTest1 mt = new MusicTest1();
        mt.play();
    }
}

