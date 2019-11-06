PYTHON TRICKS THE BOOK - A Buffet of Awesome Python Features
============================================================

Chapter 1 - Introduction
------------------------

* 1.1 What's a Python Trick?
> Python Trick: A short Python code snippet meant as a teaching tool. A Python trick either teaches an aspect of Python with a simple illustration, or it serves as a motivating example, enabling you to dig deeper and develop an intuitive understanding.

Chapter 2 - Patterns for Cleaner Python 
---------------------------------------

* 2.1 Covering Your A** With Assertions 
> Sometimes a genuinely helpful language feature gets less attention than it deserves.
```
# Python's built-in assert statement. 
    Python's assert statement is a debugging aid that tests a condition. If the assert condition is true, nothing happens, and your program continues to execute as normal. But if the condition evaluates to false, an AssertionError exception is raised with an optional error message.

Python 3.7.4 (default, Sep  7 2019, 18:27:02) 
[Clang 10.0.1 (clang-1001.0.46.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> display = {'name': 'Pro Display XDR', 'price': 4999}
>>> 
>>> def apply_discount(product, discount):
...     price = int(product['price'] * (1.0 - discount))
...     # guarantee that, no matter what, discounted prices calculated by this function cannot be lower than $0 and they cannot be higher than the original price of the product.
...     assert 0 <= price <= product['price']
...     return price 
... 
>>> apply_discount(display, 0.25)
3749
>>> apply_discount(display, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in apply_discount
AssertionError


```