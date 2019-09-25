VAPOR - The future of web development
=====================================
> Vapor, a Web Framwork for Swift that works on macOS and Ubuntu, and all of the packages that Vapor offers. Vapor is the most used web framework for Swift. It provides a beautifully expressive and easy to use foundation for your next website or API.
> Non-blocking, event-driven architecture built on top of Apple's SwiftNIO delivers high performance.
> Written in Swift, the powerful programming language that is also easy to learn.
> Expressive, protocol-oriented design with a focus on type-safety and maintainability.


Install Vapor
-------------
* Install on macOS 
```
Install Xcode:

Verify Installation:
$ swift --version 
Apple Swift version 5.1 (swiftlang-1100.0.270.13 clang-1100.0.33.7)
Target: x86_64-apple-darwin18.7.0

Install Vapor 
# The toolbox includes all of Vapor's dependencies as well as a handy CLI tool for creating new projects
$ brew tap vapor/tap 
$ brew install vapor/tap/vapor 

Verify Installation 
$ vapor --help 
Usage: vapor command

Join our team chat if you have questions, need help,
or want to contribute: http://vapor.team

Commands:
       new Creates a new Vapor application from a template.
           Use --template=repo/template for github templates
           Use --template=full-url-here.git for non github templates
           Use --web to create a new web app
           Use --auth to create a new authenticated API app
           Use --api (default) to create a new API
     build Compiles the application.
       run Runs the compiled application.
     fetch Fetches the application's dependencies.
    update Updates your dependencies.
     clean Cleans temporary files--usually fixes
           a plethora of bizarre build errors.
      test Runs the application's tests.
     xcode Generates an Xcode project for development.
           Additionally links commonly used libraries.
   version Displays Vapor CLI version
     cloud Commands for interacting with Vapor Cloud.
    heroku Commands to help deploy to Heroku.
  provider Commands to help manage providers.

Use `vapor command --help` for more information on a command.
```

* Install on Ubuntu 
```
Quick Script
# Easily add Vapor's APT repo with this handy script 
$ eval "$(curl -sL https://apt.vapor.sh)"

Install Vapor 
# you have Vapor's APT repo, install the required dependencies.
$ sudo apt-get install swift vapor 

Verify Installation 
# Double check everything worked with the following commands
$ swift --version 
$ vapor --help 
```

Getting Started
---------------
* Hello, world
```
# Create a new Vapor Project
$ vapor new HelloWorld
$ cd HelloWorld 

# Generate Xcode Project 
$ vapor xcode # build and run app from inside of Xcode

# Build & Run 

```
