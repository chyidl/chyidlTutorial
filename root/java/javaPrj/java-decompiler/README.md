Java Decompiler
===============

- [java-decompiler.jar](/root/java/javaPrj/java-decompiler.jar.removesuffix)

```
First Find **java-decompiler.jar** at the following location: 
$ (macOS) /Applications/IntelliJ IDEA CE.app/Contents/plugins/java-decompiler/lib/java-decompiler.jar

Second Try to invoke main class org.jetbrains.java.decompiler.main.decompiler.ConsoleDecompiler manually 
$ java -cp java-decompiler.jar org.jetbrains.java.decompiler.main.decompiler.ConsoleDecompiler com com 

Third Try to remove all class file from com/ folder 
$ find . -type f -name '*.o' -exec rm {} + 
```
![java-decompile png](/imgs/java/java-decompile.png?raw=true)
