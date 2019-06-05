/*
 * TestGenerics1.java
 * chap16
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 06/05/19 10:32.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

import java.util.*;

public class TestGenerics1 {

    public static void main(String[] args)
    {
        new TestGenerics1().go();
    }
    
    public void go() {    
        
        // Declare and create an Animal array, that holds both dogs and cats.
        Animal[] animals = {new Dog(), new Cat(), new Dog()};
        // Declare and create a Dog array, that holds only Dogs (the compiler won't let you put a Cat in)
        Dog[] dogs = {new Dog(), new Dog(), new Dog()};
        takeAnimals(animals);
        takeAnimals(dogs);
    }
    

    public void takeAnimals(Animal[] animals) {
        for (Animal a: animals) {
            // Remember, we can call only the methods declared in type animal.
            a.eat();
        }
    }
}

