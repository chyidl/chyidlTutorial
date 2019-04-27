Swift (programming language)
============================
> Swift is a general-purpose, multi-paradigm, compiled programming language developed by Apple Inc. for iOS, macOS, watchOS, tvOS, Linux. It is built with the open source LLVM compiler framework.


Installing
----------
* Raspberry Pi + Ubuntu 18.04.2 AArch64/Arm64 systems
```
# Checking Your Ubuntu Version From the Terminal
$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 18.04.2 LTS
Release:        18.04
Codename:       bionic

$ uname -a
Linux RPi3BPlus 4.15.0-1034-raspi2 #36-Ubuntu SMP PREEMPT Fri Apr 5 06:21:41 UTC 2019 aarch64 aarch64 aarch64 GNU/Linux

# Install Dependencies 
$ sudo apt-get install clang libicu-dev libcurl4-openssl-dev -y 

# Download the Swift packages 
# Swift 5.0 RELEASE for Linux - Ubuntu - AArch64
$ wget https://github.com/futurejones/swift-arm64/releases/download/v5.0-RELEASE/swift-5.0-RELEASE-aarch64-Ubuntu-18.04_2019-03-26.tar.gz

# Extract Package 
$ sudo mkdir /usr/local/swift
$ tar -xzvf swift-5.0-RELEASE-aarch64-Ubuntu-18.04_2019-03-26.tar.gz 
$ sudo mv usr /usr/local/swift 

# Configuring environment variables 
# need to configure PATH variable 
$ sudo vim ~/.zshrc 
export PATH=/usr/local/swift/usr/bin:$PATH 

# Checking Swift 
$ swift -version 

# Creating Program Using the Swift Package Manager 
$ mkdir helloworld-project && cd helloworld-project 
$ swift package init --type executable 
 23:29:17  pi@RPi3BPlus  ...chyidl.com/SwiftPrj/helloworld-project  38s 
 $ swift package init --type executable
 Creating executable package: helloworld-project
 Creating Package.swift     # package description, and packages dependencies 
 Creating README.md
 Creating .gitignore
 Creating Sources/          # all Swift source files 
 Creating Sources/helloworld-project/main.swift
 Creating Tests/            # contain unit tests 
 Creating Tests/LinuxMain.swift
 Creating Tests/helloworld-projectTests/
 Creating Tests/helloworld-projectTests/helloworld_projectTests.swift
 Creating Tests/helloworld-projectTests/XCTestManifests.swift

# build the package and create an executable 
 23:39:26  pi@RPi3BPlus  ...chyidl.com/SwiftPrj/helloworld-project  15s 
 $ swift build
 [1/2] Compiling Swift Module 'helloworld_project' (1 sources)

# Execute the app by running
 23:39:43  pi@RPi3BPlus  ...chyidl.com/SwiftPrj/helloworld-project 
 $ .build/debug/helloworld-project
 Hello, world!

Congratulations: you've created and built your first Swift package on Linux Ubuntu 
```

What Apple Hasn't Released on Linux 
-----------------------------------
> Well, there's no Xcode, no AppKit and no UIKit. There's no Core Graphics, no Core Animation, no AVFoundation, nor many of the other familiar core Object-C libraries. Basically, most of what you need to create beautiful iOS or Mac apps isn't here yet.

> But what Apple has release is qqite significant. Consider the Core Libraries project. They provide higher-level functionality such as networking, file system interaction, data and time calculation. These are brand new, cross platform, Objective-C-free re-implementations of existing Apple libraries. The fact the Core Libraries project doesn't rely on the Objective-C runtime suggests that Apple is creaing the underpinning for Swift to replace Objective-C completely in the
> long run. And the fact that it's cross-platform by design suggests Apple is seriously hoping poeple will use the language for Linux software development - at least for server software, if not for GUI apps.

