A Guide to Python's Magic Methods
=================================

> What are magic methods? They're everything in object-oriented Python. They're special methods that you can define to add "magic" to your classes. they're always surrounded by double underscores(e.g. __init__ or __lt__). They're also not as well documented as thet need to be.

Construction and Initialization
-------------------------------

> Everyone knows the most basic magic method, __init__. It's the way that we can define the initialization behavior of an object. However, when I call x = SomeClass(), __init__ is not the first thing to get called. Actually, it's a method called __new__, which actually creates the instance, then passes any arguments at creation on to the initializer. At the other end of the object's lifespan, there's __del__.

```
__new__(cls, [...])
    __new__ is the first method to get called in an object's instantiation. It takes the class, then any other arguments that it will pass along to __init__. __new__ is used fairly rarely, but it does have its purposes

__init__(self)
    The initializer for the class, It gets passed whatever the primary constructor was called with(so, for example, if we called x = SomeClass(10, 'foo'), __init__ would get passed 10 and 'foo' as arguments.) __init__ is almost universally used in Python class definitions.

__del__(self)
    If __new__ and __init__ formed the constructor of the object, __del__ is the destructor. It doesn't implement behaviror for the statement del x (so that code would not translate to x.__del__()). Rather, it defines behavior for when an object is garbage collected. It can be quite useful for objects that might require extra cleanup upon deletion, like sockets or file objects.Be careful, however, as there is no guarantee that __del__ will be executed if the object is still alive
    when the interpreter exits, so __del__ can't serve as a replacement for good coding practices (like always closing a connection when you're done with it. In fact, __del__ should almost never be used because of the precarious circumstances under which it is called; use it with caution!)
```
> Here's an example of __new__, __init__ and __del__ 
```
# Use __new__ when you need to control the creation of a new instance, Use __init__ when you need to control initialization of a new instance. 
# __new__ is the first step of instance creation. It's called first, and is responsible for returning a new instance of your class. In contrast, __init__ doesn't return anything; it's only respinsible for initializing the instance after it's been created.
from os.path import join 


class FileObject:
    '''Wrapper for file objects to make sure the file gets closed on deletion.'''
    
    def __init__(self, filepath='~', filename='smaple.txt'):
        # open a file filename in filepath in read and write mode 
        self.file = open(join(filepath, filename), 'r+')

    def __del__(self):
        self.file.close() 
        del self.file
```

Making Operators Work on Custom Classes
---------------------------------------

> One of the biggesr advantages of using Python's magic methods is that they provide a simple way to make objects behave like built-in types.

```
Comparison magic methods
    __cmp__(self, other)
        __cmp__ is the most basic basic of the comparison magic methods. __cmp__ should return a negative integers if self < other, zero if self == other, and positive if self > other. It's usually best to define each comparison you need rather than define them all at once, but __cmp__ can be a good way to save repetition and improve clarity when you need all comparisons implemented with similar criteria.

    __eq__(self, other)
        Defines behavior for the equality operator, == 

    __ne__(self, other)
        Defines behavior for the inequality operator, != 

    __lt__(self, other)
        Defines behavior for the less-than operator, < 

    __gt__(self, other)
        Defines behavior for the greater-than operator, > 

    __le__(self, other)
        Defines behavior for the less-than-or-equal-to operator, <= 
    
    __ge__(self, other)
        Defines behavior for the greater-than-or-equal-to operator, >= 
``` 

> In this example, we'll compare by length. Here's an implementation:

```
class Word(str):
    '''Class for words, defining comparison based on word length'''
    
    def __new__(cls, word):
        # Note that we have to use __new__. This is because str is an immutable
        # type, so we have to initialize it early (at creation)
        if ' ' in word:
            print("Value contains spaces, Truncating to first space.")
            word = word[:word.index(' ')] # Word is now all chars before first space 
        return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __ge__(self, other):
        return len(self) >= len(other)

    def __le__(self, other):
        return len(self) <= len(other)
```
```
Unary operators and functions
    __pos__(self)
        Implements behavior for unary positive (e.g. +some_object)

    __neg__(self)
        Implements behavior for negation(e.g. -some_object)

    __invert__(self)
        Implements behavior for inversion using the ~ operator.

    __round__(self, n)
        Implements behavior for the built in round() function, n is the numbers of decimal places to round to 

    __floor__(self)
        Implements behavior for math.floor(), i.e., rounding down to the nearest integer. 

    __ceil__(self):
        Implements behavior for math.ceil(), i.e rounding up to the nearest integer 

    __trunc__(self):
        Implements behavior for math.trunc(), i.e., truncating to an integral.

Normal arithmetic operators 
    __add__(self, other)
        Implements addition 

    __sub__(self, other)
        Implements subtraction 

    __mul__(self, other)
        Implements multiplication 

    __floordiv__(self, other)
        Implements integer division using the // operator 

    __div__(self, other)
        Implements division using the / operator 
    
    __truediv__(self, other)
        Implements true division. Note that this only works when from __future__ import division is in effect.

    __mod__(self, other)
        Implements modulo using the % operator 

    __divmod__(self, other)
        Implements behavior for long division using the vidmod() built in function.

    __pow__
        Implements behavior for exponents using the ** operator 

    __lshift__(self, other)
        Implements left bitwise shift using the << operator.

    __rshift__(self, other)
        Implements right bitwise shift using the >> operator.

    __and__(self, other)
        Implements bitwise and using the & operator. 

    __or__(self, other)
        Implements bitwise or using the | operator.

    __xor__(self, other)
        Implements bitwise xor using the ^ operator.

Reflected arithmetic operators all of these magics methods do the same thing as their normal equivalents, except the perform the operation with other as the first operand and self as the second, rather than the other way around.
    
```
