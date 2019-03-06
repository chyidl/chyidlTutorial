Python3 Metaprogramming
=======================
    *Presented at PyCon'2013, Santa Clara,CA March 14, 2013*

**Requirements**
    Python 3.3 or more recent 

**Metaprogramming**
    In a nutshell: code that manipulates code 
    Common examples:
        *Decorators*
        *Metaclasses*
        *Descriptors*
    Essentially, it's doing things with code 

**Why Would You Care?**
    Extensively used in frameworks and libraries 
    Better understanding of how Python works 
    It's fun 
    It solves a practical problem

DRY -- Don't Repeat Youself
    *Highly repetitive code sucks*
    *Tedious to write*
    *Hard to read*
    *Difficult to modify*

**This Tutorial**
    *A modern hourney of metaprogramming*
    *Highlight unique aspects of Python 3*
    *Explode your brain*

**Target Audience**
    *Framework/library builders*
    *Anyone who wants to know how things work*

**Reading Books**
    *Tutorial lossely based on content in "Python Cookbook, 3rd Ed."*
    *Published May, 2013*
    *You'll find even more information in the book*

**Caution**
    *If you do everything in this tutorial all at once*
    *You will either be fired*
    *Or have permanent job security*
    *It's a fine line*

**Preliminaries**
**Basic Building Blocks**
    statement + def func(args): statements = class A: def method(self,args): statement1
    
    *Statements*
        Perform the actual work of your program 
        Always execute in two scopes:
            **globals** - Module dictionary 
            **locals**  - Enclosing function (if any)
        exec(statements [, globals, [, locals]])

    *Functions*
        def func(x, y, z):
            statements 1
            statements 2
            statements 3
        
        The fundamental unit of code in most programs 
            Module-level functions 
            Methods of classes 
        
        Calling Conventions 
            Positional arguments : func(1, 2, 3)
            Keyword arguments    : func(x=1, y=2, z=3)
            Default Arguments    : def func(x, debug=False): if names is None: names = [] 
                *Default values set at definition time*
                *Only use immutable values*
            *args and **kwargs 
'''code:: python3
    # *args and **kwargs 
    def func(*args, **kwargs):
        # args is tuple of position args 
        # kwargs is dict of keyword args 
    
    # args = (1, 2) kwargs = {'x': 3, 'y' : 4, 'z': 5}
    func(1, 2, x = 3, y = 4, z = 5)

    args = (1,2) 
    kwargs = {'x': 3, 'y': 4, 'z': 5}
    func(*args, **kwargs) # same as func(1, 2, x=3, y=4, z=5)
'''
    
            Keyword Only Args
            Named arguments appearing after '*' can only be passed by keyword 
    recv(8192, block=False) # Ok 
    recv(8192, False) # Error

**Closures**
    # You can make and return functions 
    def make_adder(x, y):
        def add():
            return x + y 
        return add 
```
    Local variables are captured 
    
    >>> a = make_adder(2,3)
    >>> b = make_adder(10, 20)
    >>> a()
    5
    >>> b()
    30
```

**Classes**
    
```   
    class Spam:
        a = 1                           # Class variable 
        def __init__(self, b):
            self.b = b                  # Instance variable 

        def imethod(self):              # Instance method
            pass 

        @classmethod 
        def cmethod(cls):               # Class method 
            pass 

        @staticmethod 
        def smethod():                  # Static method is like function
            pass 

    >>> Spam.a # Class variable 
    1 
    >>> s = Spam(2)
    >>> s.b     # Instance variaable 
    2 
    >>> s.imethod() # Instance method 
    >>> Spam.cmethod() # Class method 
    >>> Spam.smethod() # Staic method 
    
    # Special Methods

    class Array:
        def __getitem__(self, index):
            ...

        def __setitem__(self, index, value):
            ...

        def __delitem__(self, index):
            ...

        def __contains__(self, item):
            ...

    Almost everything can be customized.

    # Inheritance
    class Base:
        def spam(self):
            pass 

    class Foo(Base):
        def spam(self):
            pass
            # Call method in base class 
            r = super().spam() 

    # Dictionaries 
    # Objects are layered on dictionaries
    
    class Spam:
        def __init__(self, x, y):
            self.x = x 
            self.y = y 

        def foo(self):
            pass 

    # Example 
    >>> s = Spam(2,3)
    >>> s.__dict__ 
    {'x':2, 'y':3}
    >>> Spam.__dict__['foo']
    <function Spam.foo at 0x10d9b46a8>
```

**Metaprogramming Basics**

"I love the smell of debugging in the morning."
    
    *Problem: Debugging*
        Will illustrate basics with a simple problem 
        Debugging 
        Note the only application, but simple enough to fit on slides

    *Debugging with Print*
        A function 
            def add(x,y):
                return x + y 
        
        A function with debugging 
            def add(x, y):
                print('add')
                return x + y 

        The one and only true way to debug

**Decorators**
    A decorator is a function that creates a *wrapper* around another function 

    The *wrapper* is a new function that works exactly like the original function (same arguments, same return value) except that some kind of extra processing is carried out.

**A Debugging Decorator**
    
```    
    #!/usr/bin/env python3
    # -*- coding:utf-8 -*- 
    from functools import wraps 

    def debug(func):
        msg = func.__qualname__ 
        # @wraps copies metadata {Name and doc string, Function attributes}
        @wraps(func) 
        # A decorator creates a "wrapper" function 
        def wrapper(*args, **kwargs):
            print(msg)
            return func(*args, **kwargs)
        return wrapper 
```

**Decorator Syntax**
    The definition of a function and wrapping almost always occur together 
        def add(x, y):
            return x + y 
        add = debug(add)

    @decorator syntax performs the same steps 
        @debug 
        def add(x, y):
            return x + y

**Big Picture**
    Debugging code is isolated to single location 
    This makes it easy to change (or to disable)
    User of a decorator doesn't worry about it 
    That's really the whole idea

**Decorators With Args**
    
    Calling convention
        @decorator(args)
        def func():
            pass

    Evaluates as 
        func = decorator(args)(func)

    It's a little weired two levels of calls 

**A Reformulation**
    
```
    from functools import wraps, partial 

    def debug(func=None, *, prefix=''):
        if func is None:
            return partial(debug, prefix=prefix)

        msg = prefix + func.__qualname__
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(msg)
            return func(*args, **kwargs)
        return wrapper
```

**Usage**
    
    Use as a simple decorator 
        @debug 
        def add(x, y):
            return x + y 

    Or as a decorator with optional configuration 
        @debug(prefix='***')
        def add(x, y):
            return x + y

**Debug All of This Class** 
    
    Debug all of the methods of a class 
```
    class Spam:
        @debug
        def grok(self):
            pass 

        @debug
        def bar(self):
            pass 

        @debug 
        def foo(self):
            pass 
```
    Can you decorate all methods at once?

**Class Decorator**

```
    def debugmethods(cls):
        for name, val in vars(cls).items():
            if callable(val):
                setattr(cls, name, debug(val))
        return cls 

    
    @debugmethods
    class Spam:
        def grok(self):
            pass 

        def bar(self):
            pass 

        def foo(self):
            pass 
    
    @debugmethods
    class BrokenSpam:
        @classmethod
        def grok(cls):  # Not wrapped 
            pass 

        @staticmethod 
        def bar():      # Not wrapped 
            pass 
    # Only instance methods get wrapped 
```
    Idea:
        Walk through class dictionary 
        Identify callables (e.g. methods)
        Wrap with a decorator
        One decorator application 
        Covers all definitions within the class 
        It even mostly works...

**Variation: Debug Access**

```
    def debugattr(cls):
        orig_getattribute = cls.__getattribute__ 

        def __getattribute__(self, name):
            print('Get:', name)
            return orig_getattribute(self, name)

        cls.__getattribute__ = __getattribute__ 
        return cls

    @debugattr
    class Point:
        def __init__(self, x, y):
            self.x = x 
            self.y = y 

    p = Point(2, 3)
    >>> p.x
    Get: x
    2
    >>> p.y
    Get: y 
    3
```

**Debug All The Classes**
**Solution: A Metaclass** 

```
    class debugmeta(type):
        def __new__(cls, clsname, bases, clsdict):
            # Class gets created normally 
            clsobj = super().__new__(cls, clsname, bases, clsdict)
            
            # Immediately wrapped by class decorator  
            clsobj = debugmethods(clsobj)
            return clsobj 

    # Usage 
    class Base(metaclass=debugmeta):
        ... 

    class Spam(Base):
        ...
```

**Types**

    All values in Python have a type

**Types and Classes**
    
    Classes definie new types 
    
    class Spam:
        pass 

    >>> s = Spam() 
    >>> type(s)
    <class '__main__.Spam'>
    >>>

    The class is the type of instance created 
    The class is a callable that creates instance

**Types of Classes**

    Classes are instances of types 
```
    >>> type(int)
    <class 'type'>
    >>> type(list)
    <class 'type'>
    >>> type(Spam)
    <class 'type'>
    >>> isinstance(Spam, type)
    True 
    >>>
```

**Creating Types**

    Types are their own class (builtin)
    
    class type:
        ...

    >>> type
    <class 'type'>
    This class creates new "Type" objects
    Used when defining classes 

**Class Deconstructed**

    Consider a class: 
```
    class Spam(Base):
        def __init__(self, name):
            self.name = name 

        def bar(self):
            print("I'm Spam.")
```
    # What are its components?
    # Name("Spam")
    # Base classes(Base,)
    # Functions(__init__, bar)

**Class Definition Process** 

    # What happends during class definition?
    """
        Step 1: Body of class is isolated 
        body = '''
            def __init__(self, name):
                self.name = name 
            def bar(self):
                print("I'm Spam.bar")
                '''
        Step 2: The class dictionary is created 
            # This dictionary serves as local namespace for statements in the class body 
            # By default, it's simple dictionary (more later)
            clsdict = type.__prepare__('Spam', (Base,))
        
        Step 3: Body is executed in returned dict 
            exec(body, globals(), clsdict)

        Afterwards, clsdict is populated 
        >>> clsdict
        {'__init__': <function __init__ at 0x00000>,
        'bar': <function bar at 0x03432>}
        
        Step 4: Class is constructed from its name, base classes, and the dictionary 
            
            >>> Spam = type('Spam', (Base,), clsdict)
            >>> Spam 
            <class '__main__.Spam'>
            >>> s = Spam('Guido')
            >>> s.bar()
            I'm Spam.bar
            >>> 
    """

**Changing the Metaclass**
    
    metaclass keyword argument 
    Sets the class used for creating the type 
    
    class Spam(metaclass=type):
        def __init__(self, name):
            self.name = name 

        def bar(self):
            print("I'm Spam.bar")

    By default, it's set to 'type', but you can change it to something else

**Defining a New Metaclass**

    You typically inherit from type and redefie __new__ or __init__ 

    class mytype(type):
        def __new__(cls, name, bases, clsdict):
            clsobj = super().__new__(cls, name, bases, clsdict)
            return clsobj 

    To use
    class Spam(metaclass=mytype):
        pass 

**Using a Metaclass**
    Metaclasses get information about class definitions at the time of definition 
        Can inspect this data 
        Can modify this data 
    Essentially, similar to a class decorator 
    Metaclasses propagate down hierarchies 

**Inheritance**

    Metaclasses propagate down hierarchies 
    
    class base(metaclass=mytype):
        ... 
    
    class Spam(Base):       # metaclass = mytype 
        ...

    class Grok(Spam):       # metaclass = mytype 
        ... 

    Think of it as a genetic mutation

**Big Picture**
    It's mostly about wrapping/rewriting 
        Decorators: Functions 
        Class Decorators: Classes 
        Metaclasses: Class hierarchies
    You have the power to change things 

**Problem: Structures**

```
    class Structure:
        _fields = [] 
        
        def __init__(self, *args):
            for name, val in zip(self._fields, args):
                setattr(self, name, val)


    class Stock(Structure):
        _fields = ['name', 'shares', 'price']

        # def __init__(self, name, shares, price):
        #    self.name = name 
        #    self.shares = shares 
        #    self.price = price 


    class Point(Structure):
        _fields = ['x', 'y']

        # def __init__(self, x, y):
        #    self.x = x 
        #    self.y = y 


    class Host(Structure):
        _fields = ['address', 'port']

        # def __init__(self, address, port):
        #    self.address = address 
        #    self.port = port
```

**New Approach: Signatures**
    
    Build a function signature object 

```
    from inspect import Parameter, Signature  

    fields = ['name', 'shares', 'price']
    parms = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in fields]
    sig = Signature(parms)
```
    
    Signatures are more than just metadata 


