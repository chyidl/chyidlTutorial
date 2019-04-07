package com.chyidl.advance.dataStructionAndAlgorithm;

import java.util.Enumeration;
import java.util.HashMap;
import java.util.Hashtable;

/**
 * Java Hashtable
 * HashTable是原始的java.util的部分，是一个Dictionary的实现
 *
 * */
public class HashtableTest {
    public static void main(String[] args){
        // Create a hash map
        Hashtable balance = new Hashtable();
        Enumeration names;
        String str;
        double bal;

        balance.put("Zara", 3434.34);
        balance.put("Mahnaz", 123.22);
        balance.put("Ayan", 1378.00);
        balance.put("Diasy", 99.22);
        balance.put("Qadir", -19.08);

        // Show all balances in hash table
        names = balance.keys();
        while (names.hasMoreElements()) {
            str = (String) names.nextElement();
            System.out.println(str + ": " + balance.get(str));
        }

        System.out.println();
        // Deposit 1,000 into Zara's account
        bal = ((Double)balance.get("Zara")).doubleValue();
        balance.put("Zara", bal + 1000);
        System.out.println("Zara's new balance: " + balance.get("Zara"));
    }
}
