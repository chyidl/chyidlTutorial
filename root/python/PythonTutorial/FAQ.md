Frequently Asked Question
=========================

* Why Doesn't Python Have Switch/Case?
> Unlike every other programming language used before, Python does not have switch or case statement. To get around this fact, we use dictionary mapping:
```
def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }
    return switcher.get(argument, "nothing")
```
> Dictionary Mapping for Functions, Many Python programs use dictionary mappings like this to dispatch complex procedures.
```
def zero():
    return "zero"

def one():
    return "one"

def numbers_to_functions_to_strings(argument):
    switcher = {
        0: zero,
        1: one,
        3: lambda: "two",
    }
    # Get the function from switcher dictionary 
    func = switcher.get(argument, lambda: "noting")
    # Execute the function 
    return func() 
```
> Dispatch Methods for Classes, If we don't know what method to call on a class, we can use a dispatch method to determine it at runtime.
```
class Swicther(object):
    def numbers_to_methods_to_strings(self, argument):
        """Dispatch method"""
        # prefix the method_name with 'number_' because method names 
        # cannot begin with an integer.
        method_name = 'number_' + str(argument)
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, method_name, lambda: "nothing")
        # Call the method as we return it
        return method() 

    def number_0(self):
        return "zero"

    def number_1(self):
        return "one"

    def number_2(self):
        return "two"
```
> The Official Answer
```
The official answer says, "You can do this enough with a sequence of if... elif... elif... else". And that you can use dictionary mapping for functions and dispatch methods for classes.
"Python doesn't need a case statement"
```
