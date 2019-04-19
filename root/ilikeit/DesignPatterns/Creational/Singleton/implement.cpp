//
// implement.cpp
// Downloads
//
// 🎂"Here's to the crazy ones. The misfits. The rebels.
// The troublemakers. The round pegs in the square holes.
// The ones who see things differently. They're not found 
// of rules. And they have no respect for the status quo.
// You can quote them, disagree with them, glority or vilify
// them. About the only thing you can't do is ignore them. 
// Because they change things. They push the human race forward.
// And while some may see them as the creazy ones, we see genius.
// Because the poeple who are crazy enough to think thay can change
// the world, are the ones who do."
// 
// Created by Chyi Yaqing on 01/22/19.
// Copyright © 2019. Chyi Yaqing. All rights reserved.
//


#include <iostream>

class Singleton
{
    private:

        /* Private constructor to prevent to accessible from the outside of the class to
        ensure the only way of instantiating the class would be only through the instance */
        Singleton(){
            std::cout << "Constructor called" << std::endl;
        };
        
        /* Destructor declaration */
        ~Singleton(){
            std::cout << "Destructor called" << std::endl;
        };

    public:
        /* Static access method. */
        static Singleton& instance(){
            // static variable initialization is thread-safe
            static Singleton INSTANCE;
            return INSTANCE;
        }

        Singleton(const Singleton&) = delete;
        Singleton(Singleton&&) = delete;
        Singleton& operator=(const Singleton&) = delete;
        Singleton& operator=(Singleton&&) = delete;

        /* Do Something */
        void doSomething(){
            std::cout << "doSomething() called" << std::endl;
        }
};

int main(int argc, const char * argv[]) 
{
	// Your Programming statements HERE!
    // use the singleton class 
    Singleton * MySingleton1 = &Singleton::instance();
    Singleton * MySingleton2 = &Singleton::instance();
    MySingleton1->doSomething();
    MySingleton2->doSomething();
    std::cout << MySingleton1 << ';' << MySingleton2 << std::endl;
	return 0;
}

