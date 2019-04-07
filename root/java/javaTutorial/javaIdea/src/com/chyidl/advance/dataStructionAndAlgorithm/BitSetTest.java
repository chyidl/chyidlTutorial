package com.chyidl.advance.dataStructionAndAlgorithm;

import java.util.BitSet;

/**
 * 位集合 BitSet
 * 位集合实现一组可以单独设置和清楚的位或标志
 *
 * */
public class BitSetTest {
    public static void main(String[] args){
        BitSet bits1 = new BitSet(16);
        BitSet bits2 = new BitSet(16);

        // set some bites
        for (int i = 0; i<16; i++) {
            if((i%2) == 0)
                // 将指定的index 位设置位true
                bits1.set(i);
            if((i%5) != 0)
                bits2.set(i);
        }

        System.out.println("Initial pattern in bits1: ");
        System.out.println(bits1);
        System.out.println("\nInitial pattern in bits2: ");
        System.out.println(bits2);

        // AND bits
        bits2.and(bits1);
        System.out.println("\nbits2 AND bits1: ");
        System.out.println(bits2);

        // OR bits
        bits2.or(bits1);
        System.out.println("\nbits2 OR bits1: ");
        System.out.println(bits2);

        // XOR bits
        bits2.xor(bits1);
        System.out.println("\nbits XOR bits1: ");
        System.out.println(bits2);
    }
}
