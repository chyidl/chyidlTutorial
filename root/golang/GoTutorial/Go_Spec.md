The Go Programming Language Specification
=========================================

Contents:
---------
* Introduction 
> Go is a general-purpose language designed with systems programming in mind. It is strongly typed and garbage-collected and has explicit support for concurrent programming. Programs are constructed from packages, whose properties allow efficient management of dependencies.
* Notation 
* Source code representation 
```
upper and lower case letters are different characters.
compiler disallow the NUL character (U+0000) in the source text.
compiler ignore a UTF-8-encoded byte order mark (U+FEFF)
```
    - Characters 
```
The following terms are used to denote specific Unicode character classes:
    newline : the Unicode code point U+000A 
    unicode_char : an arbitrary Unicode code point except newline 
    unicode_letter : a Unicode code point classified as "Letter"
    unicode_digit : a Unicode code point classified as "Number, decimal digit"
```
    - Letters and digits 
```
The underscore character _(U+005F) is considered a letter 
    letter = unicode_letter | "_" 
    decimal_digit = "0" ... "9"
    binary_digit = "0" | "1" 
    octal_digit = "0" ... "7"
    hex_digit = "0" ... "9" | "A" ... "F" | "a" ... "f"
```
* Lexical elements 
    - Comments 
```
There are two forms:
    1. Line comments start with the character sequence // and stop at the end of the line.
    2. General comments start with the character sequence /* and stop with the first subsequent character sequence */ 

A comment cannot start inside a rune or string literal, or inside a comment. A general comment containing no newlines acts like a space. Any other comment acts like a newline.
```
    - Tokens 
```
Tokens form the vacabulary of the Go language. There are four classes: identifiers, operators and punctuation, and literals. White space, formed from spaces (U+0020), horizontal tabs (U+0009), carriage returns (U+000D), and newlines(U+000A), is ignored except as it separates tokens that would otherwise combine into a single token.
```
    - Semicolons
```
Go program may omit most of these semicolons using the following two rules:
```
    - Identifiers
```
An identifier is a sequence of one or more letters and digits. The first character in an identifier must be a letter.
    identifier = letter { letter | unicode_digit } 
```
    - Keywords
```
The following keywords are reserved and may not be used as identifiers.
```
| keywords    | meaning                                                                                                                   |
| :---------- | :------------------------------------------------------------------------------------------------------------------------ |
| break       | A "break" statement terminates execution of the innermost "for","switch", or "select" statement within the same function. |
| case        |                                                                                                                           |
| chan        |                                                                                                                           |
| const       |                                                                                                                           |
| continue    |                                                                                                                           |
| default     |                                                                                                                           |
| defer       |                                                                                                                           |
| else        |                                                                                                                           |
| fallthrough |                                                                                                                           |
| for         |                                                                                                                           |
| func        |                                                                                                                           |
| go          |                                                                                                                           |
| goto        |                                                                                                                           |
| if          |                                                                                                                           |
| import      |                                                                                                                           |
| interface   |                                                                                                                           |
| map         |                                                                                                                           |
| package     |                                                                                                                           |
| range       |                                                                                                                           |
| return      |                                                                                                                           |
| select      |                                                                                                                           |
| struct      |                                                                                                                           |
| switch      |                                                                                                                           |
| type        |                                                                                                                           |
| var         |                                                                                                                           |
    - Operators and punctuation
```
+   &   +=  &=  &&  ==  !=  (   )
-   |   -=  |=  ||  <   <=  [   ] 
*   ^   +*  ^=  <-  >   >=  {   }
/   <<  /=  <<= ++  =   :=  ,   ; 
%   >>  %=  >>= --  !   ... .   :
    &^      &^= 
```
    - Integer literals 
```
An integer literal is a sequence of digits representing an integer constant.
    0b or 0B for binary 
    0o or 0O for octal 
    0x or 0X for hexadecimal
    A single 0 is considered a deciaml zero

For readability, an underscore character _ may appear after a base prefix or between successive digits; such underscores do not change the literal's value. 
    int_lit         = decimal_lit | binary_lit | octal_lit | hex_lit 
    decimal_lit     = "0" | ( "1" ... "9" ) [ [ "_" ] decimal_digits ]
    bianry_lit      = "0" ( "b" | "B" ) [ "_" ] binary_digits 
    octal_lit       = "0" [ "o" | "O" ] [ "_" ] octal_digits 
    hex_lit         = "0" ( "x" | "X" ) [ "_" ] hex_digits 

    decimal_digits  = decimal_digit { [ "_" ] decimal_digit }
    binary_digits   = binary_digit { [ "_" ] binary_digit }
    octal_digits    = octal_digit { [ "_" ] octal_digit }
    hex_digits      = hex_digit { [ "_" ] hex_digit }
```
    - Floating-point literals 
```
A floating-point literal is a decimal or hexadecimal representation of a floating-point constant.


```
    - Imaginary literals 
    - Rune literals 
    - String literals
* Constants
* Variables
* Types 
    - Method sets
    - Boolean types 
    - Numeric types
    - String types
    - Array types
    - Slice types 
    - Struct types 
    - Pointer types 
    - Function types
    - Interface types 
    - Map types 
    - Channel types 
* Properties of types and values 
    - Type identity 
    - Assignability 
    - Representability 
* Blocks 
* Declaratons and scope 
    - Label scopes 
    - Blank identifier 
    - Predeclared identifiers 
    - Exported identifiers 
    - Exported identifiers 
    - Uniqueness of identifiers 
    - Constant declarations
    - lota
    - Type declarations
    - Variable declarations
    - Short variable declarations 
    - Function declarations
    - Method declarations
* Expressions 
    - Operands 
    - Qualified identifiers 
    - Composite literals 
    - Function literals 
    - Primary expressions
    - Selectors
    - Method expressions 
    - Method values 
    - Index expressions 
    - Slice expressions 
    - Type assertions 
    - Calls 
    - Passing arguments to ... parameters 
    - Operators 
    - Arithmetic operators 
    - Comparison operators 
    - Logical operators 
    - Address operators 
    - Receive operators
    - Conversions 
    - Constant expressions 
    - Order of evaluation 
* Statements 
    - Terminating statements 
    - Empty statements 
    - Labeled statements 
    - Expression statements 
    - Send statements 
    - IncDec statements 
    - Assignments 
    - If statements 
    - Switch statements 
    - For statements 
    - Go statements 
    - Select statements 
    - Return statements 
    - Break statements 
    - Continue statements
    - Goto statements 
    - Fallthrough statements 
    - Defer statements 
* Built-in functions 
    - Close 
    - Length and capacity 
    - Allocation 
    - Making slices, maps and channels 
    - Appending to and copying slices 
    - Deletion of map elements 
    - Manipulating complex numbers 
    - Handling panics
    - Bootstrapping
* Packages 
    - Source file organization 
    - Package clause 
    - Import declarations 
    - An example package 
* Program initialization and execution 
    - The zero value 
    - Package initialization 
    - Program execution 
* Errors 
* Run-time panics 
* System considerations
    - Package unsafe 
    - Size and alignment guarantees 