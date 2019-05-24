/*
 * MiniMiniMusicApp.java
 * chap11
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/23/19 23:42.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

import javax.sound.midi.*;

public class MiniMiniMusicApp {
    
    public static void main(String[] args)
    {
        MiniMiniMusicApp mini = new MiniMiniMusicApp();
        mini.play();
    }

    public void play() {
        try {
            /**
             * Get a Sequencer and open it
             * */
            Sequencer player = MidiSystem.getSequencer();
            player.open();
            
            /**
             * 
             * */
            Sequence seq = new Sequence(Sequence.PPQ, 4);
            
            /**
             * the Track lives in the Sequence, and the MIDI data lives in the Track.
             * */
            Track track = seq.createTrack();
            
            /**
             * Put some MidiEvent into the Track.
             * */
            // Make a Message 
            ShortMessage a = new ShortMessage();
            // Put the Instruction in the Message 
            a.setMessage(144, 1, 20, 100);
            // Make a new MidiEvent using the Message
            MidiEvent noteOn = new MidiEvent(a, 1);
            // Add the MidiEvent to the Track
            track.add(noteOn);

            ShortMessage b = new ShortMessage();
            b.setMessage(128, 1, 20, 100);
            MidiEvent noteOff = new MidiEvent(b, 3);
            track.add(noteOff);
            
            /**
             * Give the Sequence to the Sequence
             * */
            player.setSequence(seq);

            /**
             * Start() the Sequencer
             * */
            player.start();
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
}

