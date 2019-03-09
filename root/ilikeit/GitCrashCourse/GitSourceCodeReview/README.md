GIT SOURCE CODE REVIEW
======================

Since its release in December 2005, git has taken over the software industry. In combination with GitHub it is now a powerful tool to publish and share code: From big teams (linux kernel), many have adopted it as their main SCM.


I wanted to get a better understanding of the "stupid content tracker" and see how it was built so I spent a few weeks in may spare time reading the source code. I found it tiny, tidy, well-documented and overall pleasant to read.

read more souce code and become better enginerrs.


GENESIS
-------



First contact
-------------
```
# Getting the source code is easy:
$ git clone https://github.com/git/git 

# Compiling on Linux or MacOS X works "out of the box" as long as you only need English. 
$ cd git 
$ make 

# What language is used? 
In its infancy Git was programmed entirely in C(the ver first Git commit was performed with just 5 tiny executables:)
```
