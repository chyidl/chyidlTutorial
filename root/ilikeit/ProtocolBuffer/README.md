Protocol Buffer
===============

An Evolution of data
--------------------
```
CSV (Comma Separated Values)
    Advantages:
        Easy to parse
        Easy to read
        Easy to make sense of 
    Disadvantages:
        The data types of elements has to be inferred and is not a guarantee 
        Parsing becomes tricky when data contains commas 
        Column names may or may not be there 

Relational tables definitions 
    Relational table definitions add types
    Advantages:
        Data is fully typed 
        Data fits in a table 
    Disadvantages:
        Data has to be flat
        Data is stored in a database, and data definition will be different for each database 

JSON (JavaScript Object Notation)
    Json format can be shared across the network!
    Advantages:
        Data can take any form(arrys, nested elements)
        JSON is widely accepted format on the web 
        JSON can be read by pretty much any language
        JSON can be easily shared over a network 
    Disadvantages:
        Data has no schema enforcing 
        JSON objects can be quite big in size because of repeated keys 
        No comments, metadatam documentation

Protocol Buffers 
    Protocol Buffers is defined by a .proto text file: 
    Advantages:
        Data is fully typed 
        Data is compressed automatically (less CPU usage)
        Schema (define using .proto file) is needed to generate code and read the data 
        Documentation can be embedded in the schema 
        Data can be read across any language (Java, Go, Python, C++)
        Schema can evolve over time, in a safe manner (schema evolution)
        3-10x smaller, 20-100x faster than XML 
        Code is generated for you automatically 
    Disadvantages:
        Protobuf support for some languages might be lacking (but the main ones is fine)
        Can't "open" the serialized data with a text editor (because it's compressed and serialised)
```

How is Protocol Buffer Used
---------------------------
```
        .proto file (Human-readable) 
                |
                V
        Automated Generation of Code[Java, Python, Go] 
                |
                V 
        Create Objects 
                |
                V
        encode/decode Serialized Data(Can be interpreted by any language)


Some databases may have support for Protocol Buffers data format
Lots of RPC frameworks, including gPRC, use Protocol Buffers to exchange data 
Google uses it for all their internal API 

Proto2 vs Proto3
    Mid 2016, Google release the 3rd iteration of Protocol Buffers, named proto3 
```

Requirements
------------
```
1. Install VSCode https://code.visualstudio.com/
2. Install VSCode entensions:
    vscode-proto3
    Clang-Format 
3. Install Clang-Format 
    macOS: $ brew install clang-format 
    Windows: 
4. Optional - install Protoc 
    If you want your files to be syntax checked automatically 
```

Protocol Buffers Basics
-----------------------
* exmaple.proto file
```
// We are using proto3 
syntax = "proto3";

// In protocol Buffers define messages 
message MyMessage {

// int32: Field Type 
//id: Field Name
// 1: Field Tag(e.g. Number)
    int32 id = 1;
    string first_name = 2;
    bool is_validated = 3;
}
```

* Scalar Types: 
    - Numbers: can take various forms based on what values you expect them to have:
        * double, float, int32, int64, uint32, uint64, sint32, sint64, fixed32, fixed64, sfixed32, sfixed64
    - Boolean: Boolean can hold the value True of False 
        * bool 
    - String: represents an arbitrary length of text (support UTF-8 encoded or 7 bit ASCII)
        * string
    - Bytes: represents any sequence of byte array 
        * bytes 

* Enums:
    - If you know all the values a field can take in advance, you can leverage the Enum type 
    - The first value of an Enum is the default value 
    - Enum must start by the tag 0 (which is the default value)

* Tags:
> In Protocol Buffers, field names are not important! (but when programming the fields are important), For protobuf the important element is the tag. Smallest tag: 1; Largest tag:2²⁹ - 1, or 536870911; Cannot use the numbers 19000 through 19999.  
    - Tags numbered from 1 to 15 use 1 byte in space, so use them for frequently populated fields
    - Tags numbered from 16 to 2047 use 2 bytes in space 
    - There's a concept of reserved tag that we'll see in the advanced lectures 

* Repeated Fields:
    - To make a "list" or an "array", you can use the concept of repeated fields
    - The list can take any number (0 or more) of elements you want 
    - The opposite of repeated is "singular" 

* Comments:
    - It is possible to embed comments in your .proto file 
    - It is actually recommended to use comments as a form of documentation for your schemas.
    - Comments can be of these two forms:
        * // this is a comment 
        * /* this is a multiline comment */

* Default Values for fields:
    - All fields, if not specified or unknown, will take a default value 
    - bool: false 
    - number (int32, etc...): 0
    - string: empty string 
    - bytes: empty bytes 
    - enum: first value 
    - repeated: empty list 

```
Defining multiple Messages in the same .proto file

It is possible, in the same .proto file, to define multiple types 

It is possible to define types within types
    The reasons could be:
        Avoiding naming conflicts
        Enforcing some level of "locality" for that type 

Importing Types
You can also have different types in different .proto files

This is useful if you want to re-use code and import other .proto files created by people in your team.

```
