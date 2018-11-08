# C & C++ Tutorial 


## C Programming Language 


## C++ Programming Language 

![c++ cookbook](/imgs/cc++/CC++Tutorial/C++Cookbook.png?raw=true)

C++ Cookbook
Solutions and Examples for C++ Programmers
Release Date: June 2009
Pages: 600

- [c++ cookbook](/root/cc++/CC++Tutorial/C++Cookbook/README.md)

## Third Library 

- [Boost C++ library](/root/cc++/CC++Tutorial/boost_c++_library_Intro.md)


## A Simple C++ Project Structure

```
# The Project Folder Tree 

bin: The output executables go here, both for the app and for any tests and spikes. 
build: This folder contains all object files, and is removed on a clean 
doc: Any notes, like my assembly notes and configuration files, are here. 
include: All project headers files. All necessary third-aprty headers files that do not exists under /usr/local/include are also placed here 
lib: Any libs that get compiled by the project, thierd party or any need in developement. 
spike: I often write smaller classes or files to test technologies or ideas, and keep them around for future reference. They go here, where they do not dilute the real application's files, but can still be found later.
src: The application and only the application's source files 
test: All test code files. 

.gitignore:

Since I use git for source code control, the .gitignore files is :
    # Ignore the build and lib dirs 
    build 
    lib/*

    # Ignore any executables
    bin/*

    # Ignore Mac specific files 
    .DS_Store 

Generic Makefile 
    
    #
    # TODO: Move `libmongoclient.a` to /usr/local/lib so this can work on production servers 
    # 

    CC := g++ # This is the main compiler 
    # CC := clang --analuze # and comment out the linker last line for sanity 
    SRCDIR := src
    BUILDDIR := build 
    TARGET := bin/runner 

    SRCEXT := cpp 
    SOURCES := $(shell find $(SRCDIR) -type f -name *.$(SRCEXT))
    OBJECTS := $(patsubst $(SRCDIR)/%,$(BUILDDIR)/%,$(SOURCES:/$(SRCEXT)=.o))
    CFLAGS := -g # -Wall 
    LIB := -pthread -lmongoclient -L lib -lboost_thread-mt -lboost_filesystem-mt -lboost_system-mt
    INC := -I include 

    $(TARGET): $(OBJECTS)
        @echo " Linking... "
        @echo " $(CC) $^ -o $(TARGET) $(LIB)"; $(CC) $^ -o $(TARGET) $(LIB)

    $(BUILDDIR)/%.o: $(SRCDIR)/%.$(SRCEXT)
        @mkdir -p $(BUILDDIR)
        @echo " $(CC) $(CFLAGS) $(INC) -c -o $@ $<"; $(CC) $(CFLAGS) $(INC) -c -o $@ $<

    clean:
        @echo " cleaning... "
        @echo " $(RM) -r $(BUILDDIR) $(TARGET)"; $(RM) -r $(BUILDDIR) $(TARGET)

    # Tests
    tester:
        $(CC) $(CFLAGS) test/tester.cpp $(INC) $(LIB) -o bin/tester 

    # Spikes 
    ticket:
        $(CC) $(CFLAGS) spikes/ticket.cpp $(INC) $(LIB) -o bin/ticket 

    .PHONY: clean
```
