Apache Maven
============
> Maven is widely used build-management tool developed by the Apache Software Foundation(ASF).

* Installing and configuring Maven
```
1. Install the latest version 
$ brew update 
$ brew install maven 

2. Verify install:
$ mvn -version 

3. Confirm the path:
$ which mvn 

4. Confirm the path.
$ cd  /usr/local/Cellar/maven/3.6.2/libexec/bin
$ ls 
m2.conf  mvn      mvnDebug mvnyjp

5. Add the following to under export PATH=, 
$ sudo ~/.zshrc
    export M2_HOME=/usr/local/Cellar/maven/3.6.2/libexec
    export M2=$M2_HOME/bin 
    export PATH=$PATH:$M2_HOME/bin 

6. view changed environment variable. 
$ echo $M2_HOME
$ echo $M2
```

* Change Default Configurations 
```
1. Navigate to the hidden folder Maven installed 
$ cd ~/.m2/repository 

Some prefer to change Maven's local repository to another location 
$ vim ~/.m2/settings.xml 
    <localRepository>~//maven/repo/</localRepository>
```

* Using Maven
```
pom.xml (Project Object Model) file describes project dependencies which Maven resolves by downloading them.

1. The vast majority of Maven-built projects can be built with this command:
$ mvn clean install 
$ mvn clean install -Dmaven.test.skip=true 

# To create the JAR file in the project's build directory ("target")
$ mvn package 

# To store the JAR file in the local repository 
$ mvn install 

# To post the JAR file to the global repository 
$ mvn deploy
```

* Maven lifecycle phase
    - validate : Checks whether the project is correct and all necessary information is available
    - compile : Compiles the source code of the project 
    - test : Tests the compiled source code using a suitable unit testing framework.
    - package : Packages the compiled code in its distributable format, such as a JAR.
    - integration-test : Processes and deploys the package into an environment where integration tests can be run.
    - verify : Runs any checks to verify the package is valid and meets quality criteria.
    - install : Installs the package in the local repository, where it can be referenced as a dependency by other locally built projects.
    - deploy : 

* Basic WAR project directory layout
| Folder               | Description                              |
| :------------------- | :--------------------------------------- |
| ${project.basedir}   | Project root                             |
| ---\src              | source root                              |
| -------\main         | Program source                           |
| ----------\java      | Java sources                             |
| ----------\resources | Properties files, XML schema, etc.       |
| ----------\webapp    | Web application resources                |
| -------\test         | Test source root                         |
| ----------\java      | Java sources, such as JUnit test classes |
| ----------\resources | Properties files, XML schema, etc.       |
| ---\target           | Files created by the build process       |