Introduction to Golang
======================
```
Creators:
    Robert Griesemar、Rob Pike、Ken Thompson

Why a New Language?
    Python + Java + C/C++ 
    Python: Easy to use, but slow 
    Java: Increasingly complex type system
    C/C++: Complex type system Slow compile times
    Go: Concurrency

Go (golang)
    Strong and statically typed 
    Excellent community 
    Key features
        Simplicity 
        Fast compile times 
        Garbage collected 
        Built-in concurrency 
        Compile to standalone binaries 

https://golang.org
https://golang.org/doc/
https://golang.org/doc/effective_go.html 
https://golang.org/pkg/
https://golang.org/project/
https://golang.org/help/
https://golangbridge.org/
https://play.golang.org/ -- The Go Playground 
```

Install Golang on MacOS With Homebrew!
--------------------------------------
```
Installing Go via the Terminal 
$ brew install go 

Setup the GOPATH environment variable
$ vim ~/.zshrc 
# Keep in mind that $HOME is equal to "~" AKA /Users/your_username. 
First of all export some paths, and save them in your .zshrc or .bashrc files for easy use. Use sudo if you get error.
# Go development 
export GOPATH="${HOME}/.go"
export GOROOT="$(brew --prefix golang)/libexec"
export PATH=$PATH:${GOPATH}/bin:${GOROOT}/bin
$ test -d "${GOPATH}" || mkdir "${GOPATH}"
$ test -d "${GOPATH}/src/github.com" || mkdir -p "${GOPATH}/src/github.com"

# Also a bunch of dev tools!
$ go get golang.org/x/tools/cmd/godoc 
$ go get github.com/golang/lint/golint 

Setting up the VS Code text editor for Go 
Open VS Code via spotlight. Press Command + Space and type "VS Code" then press enter 
When VS Code opens, press command + shift + p and type "shell".
"Shell Command: Install 'code' command in PATH"
Click "Auto Save" in the file dropdown at the top of the screen. 
```

Go Running 
----------
```
go run 
go build 
go install 
```

Go Fundation
------------
* Variables (type value address)
    - Type -> What kind of information can be stored inside the variable 
    - Value -> The stored value inside the variable.
    - Address -> Where the variable can be found in computer memory 
```
# If declare a variable without a value, the  it'll have a zero-value depending on the type of the variable.
    zero-values 
    booleans    ->  false 
    float       ->  0.0 
    integers    ->  0 
    strings     ->  "" 

# Long Declaration [declare name type = value]
    =  assigning values
# Short Declaration [name := value]
    := declare and assign 
# type-inferring 
# Multiple declarations [declare name type = value name2 type, name3 type = value2, value3]
# Multiple short declaration [name, name2 := value, value2]

Can't redeclare variables, but can shadow them.
All variables must be used 

Use a long declaration when you can't know what data to store beforehand, otherwise, use a short declaration. 
Use the multiple declarations when you want to define multiple variables together or as a hint for code readability that the variables will be used together.

Can't use short declarations outside of functions including the main function. Or: you will meet with this error: "syntax error: non-declaration statement outside function body". Not good.

# Making a variable accessible to other packages 
This is called exporting. To define a variable in the package scope, you can only use a long declaration or a multiple declaration. After that, you need to capitalize its first letter.

# Visibility 
    lower case first letter for package scope 
    upper case first letter to export 
    no private scope 

# Naming conventions 
    Pascal or camelCase 
        Capitalize acronyms (HTTP, URL)
    As short as reasonable 
        longer names for longer lives 

# type conversions 
    destination Type (variable)
    use strconv package for strings 
```

* PRIMITIVES 
```
    - Boolean type 
        * values are true and false 
        * not an lias for other types 
        * zero value is false 
    - Arithmetic operations 
        * Addition 
        * Subtraction 
        * Multiplication 
        * Division 
        * Remainder 
    - Bitwise operations 
        * And 
        * Or 
        * Xor 
        * Not 
    - Numeric types 
        * Integers (Signed integers, Unsigned integers)
            - int8:     -128 ~ 127 
            - uint8:    0   ~ 255 
            - int16     -32768 ~ 32767
            - uint16    0   ~ 65535 
            - int32     -2147483648 ~ 2147483647 
            - uint32    0   - 4294967295 
            - int64     -9223372036854775808 - 9223372036854775807 
        * Floating point 
            - Follow IEEE-754 standard 
            - Zero value is 0 
            - 32 and 64 bit version 
            - Literal styles 
                * Deciaml (3.14)
                * Exponential (13e18 or 2E10)
                * Mixed (13.7e12)
        * Complex numbers 
            - Zero value is (0+0i)
            - 64 and 128 bit versions 
            - complex - make complex number from two floats 
            - real - get real part as float 
            - imag - get imaginary part as float 
    - Text types 
        * String 
            - UTF-8 
            - Immutable 
            - Can be concatenated with plus (+) operator 
            - Can be converted to []byte 
        * Rune 
            - UTF-32 
            - Alias for int32 
            - Special methods normally required to process 
```     

* CONSTANTS
```
    - Immutable, but can be shadowed 
    - Replaced by the compiler at compile time 
        * Value must be calculable at compile time 
    - Naming convention 
        * PascalCase for exported constants 
        * camelCase for internal constans 
    - Typed constants work like immutable variables 
        * can interoperate only with same type 
    - Untyped constants 
        * Can interoperate with similar types 
    - Enumerated constants 
        * Special symbol itoa allows related constants to be created easily 
        * Itoa starts at 0 in each const block and increments by one
        * Watch out of constant values that match zero values for variables 
    - Enumeration expressions 
        * Operations that can be determined at compile time are allowed 
        * Arithmetic 
        * Bitwise operations 
        * Bitshifting 

itoa: Elegant Constants in Golang 
Golang is to use the itoa identifier, which simplifies constant definitions that use incrementing numbers, giving the categories exactly the same values as above.
```

* ARRAYS AND SLICES 
```
    - Arrays 
        * Collection of items with same type 
        * Fixed size 
        * Declaration styles 
            - a := [3]int{1, 2, 3}
            - a := [...]int{1, 2, 3}
            - var a [3]int 
        * access via zero-based index 
            - a := [3]int {1, 3, 5} // a[1] == 3 
        * len function returns size of array 
        * Copies refer to different underlying data 
    - Slices 
        * Backed by array 
        * Creation styles 
            - Slice existing array or slice 
            - Literal style 
            - Via make function 
                * a := make([]int, 10)  // create slice with capacity and length == 10 
                * a := make([]int, 10, 100) // slice with length == 10 and capacity == 100 
        * len function returns length of slice 
        * cap function returns length of underlying array 
        * append function to add elements to slice 
            - May cause expensive copy operation if underlying array is too small 
        * Copies refer to same underlying array 
```

* MAPS AND STRUCTS 
```
    Maps 
    Structs 
```
