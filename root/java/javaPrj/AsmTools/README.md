AsmTools - tools for the production of proper and improper Java '.class' files
==============================================================================
> The AsmTools open source project is used to develop tools for the production of proper and improper Java '.class' files. AsmTools are being opened in order to facilitate a community of Java .class file production for various testing and other OpenJDK development applications.

* Jasm/Jdis - an assembler language that provides a Java-like declaration of member signatures, while providing Java VM specification compliant mnemonics for byte-code instructions.

* JCod/JDec - an assembler language that provides byte-code containers of class-file constructs.

Requirement:
------------
```
jdk8, ant 
    1. clone asmtools 
        $ brew install mercurial, ant
        $ hg clone http://hg.openjdk.java.net/code-tools/asmtools 
    2. compile 
        $ cd asmtools/build 
        $ ant 
    3. copy asmtools.jar file 
        $ cd ../../asmtools-7.0-build/release/lib/asmtools.jar .
```
- [asmtools.jar](/root/java/javaPrj/AsmTools/asmtools.jar)

Test Java Class file
--------------------
```
/*
 * Test.java
 * AsmTools
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 06/11/19 23:09.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

public class Test {

    public static void main(String[] args)
    {
        System.out.println("Hello World!");
    }
}

# compile java file to class file 
$ javac Test.java 

# check Jasm 
$ java -jar asmtools.jar jdis Test.class 

super public class Test
	version 52:0
{


public Method "<init>":"()V"
	stack 1 locals 1
{
		aload_0;
		invokespecial	Method java/lang/Object."<init>":"()V";
		return;
}

public static Method main:"([Ljava/lang/String;)V"
	stack 2 locals 1
{
		getstatic	Field java/lang/System.out:"Ljava/io/PrintStream;";
		ldc	String "Hello World!";
		invokevirtual	Method java/io/PrintStream.println:"(Ljava/lang/String;)V";
		return;
}

} // end Class Test

# Check Jcod 
$ java -jar asmtools.jar jdec Test.class 

class Test {
  0xCAFEBABE;
  0; // minor version
  52; // version
  [] { // Constant Pool
    ; // first element is empty
    Method #6 #15; // #1
    Field #16 #17; // #2
    String #18; // #3
    Method #19 #20; // #4
    class #21; // #5
    class #22; // #6
    Utf8 "<init>"; // #7
    Utf8 "()V"; // #8
    Utf8 "Code"; // #9
    Utf8 "LineNumberTable"; // #10
    Utf8 "main"; // #11
    Utf8 "([Ljava/lang/String;)V"; // #12
    Utf8 "SourceFile"; // #13
    Utf8 "Test.java"; // #14
    NameAndType #7 #8; // #15
    class #23; // #16
    NameAndType #24 #25; // #17
    Utf8 "Hello World!"; // #18
    class #26; // #19
    NameAndType #27 #28; // #20
    Utf8 "Test"; // #21
    Utf8 "java/lang/Object"; // #22
    Utf8 "java/lang/System"; // #23
    Utf8 "out"; // #24
    Utf8 "Ljava/io/PrintStream;"; // #25
    Utf8 "java/io/PrintStream"; // #26
    Utf8 "println"; // #27
    Utf8 "(Ljava/lang/String;)V"; // #28
  } // Constant Pool

  0x0021; // access
  #5;// this_cpx
  #6;// super_cpx

  [] { // Interfaces
  } // Interfaces

  [] { // fields
  } // fields

  [] { // methods
    { // Member
      0x0001; // access
      #7; // name_cpx
      #8; // sig_cpx
      [] { // Attributes
        Attr(#9) { // Code
          1; // max_stack
          1; // max_locals
          Bytes[]{
            0x2AB70001B1;
          }
          [] { // Traps
          } // end Traps
          [] { // Attributes
            Attr(#10) { // LineNumberTable
              [] { // LineNumberTable
                0  19;
              }
            } // end LineNumberTable
          } // Attributes
        } // end Code
      } // Attributes
    } // Member
    ;
    { // Member
      0x0009; // access
      #11; // name_cpx
      #12; // sig_cpx
      [] { // Attributes
        Attr(#9) { // Code
          2; // max_stack
          1; // max_locals
          Bytes[]{
            0xB200021203B60004;
            0xB1;
          }
          [] { // Traps
          } // end Traps
          [] { // Attributes
            Attr(#10) { // LineNumberTable
              [] { // LineNumberTable
                0  23;
                8  24;
              }
            } // end LineNumberTable
          } // Attributes
        } // end Code
      } // Attributes
    } // Member
  } // methods

  [] { // Attributes
    Attr(#13) { // SourceFile
      #14;
    } // end SourceFile
  } // Attributes
} // end class Test

# From jasm file to .class file 
$ java -jar asmtools.jar jasm Test.jasm 

# From jcod file to .class file             # produces Test.class 
$ java -jar asmtools.jar jcod Test.jcod     # produces Test.class 
```
