/*
 * MiniMusicPlayer1.java
 * chap12
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 05/25/19 13:41.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

import javax.sound.midi.*;

public class MiniMusicPlayer1 {
    
    public static void main(String[] args)
    {
        try {
            // make and open a sequencer 
            Sequencer sequencer = MidiSystem.getSequencer();
            sequencer.open();
            
            // make a sequence and a track
            Sequence seq = new Sequence(Sequence.PPQ, 4);
            Track track = seq.createTrack();
            
            // make a bunch of events to make the notes keep going up
            for (int i = 5; i < 61; i += 4) {
                track.add(makeEvent(144, 1, i, 100, i));
                track.add(makeEvent(128, 1, i, 100, i + 2));
            }
            
            // start it running
            sequencer.setSequence(seq);
            sequencer.setTempoInBPM(220);
            sequencer.start();
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }

    public static MidiEvent makeEvent(int comd, int chan, int one, int two, int tick) {
        MidiEvent event = null;
        try {
            ShortMessage a = new ShortMessage();
            a.setMessage(comd, chan, one, two);
            event = new MidiEvent(a, tick);
        } catch (Exception e) {
        }
        return event;
    }
}

