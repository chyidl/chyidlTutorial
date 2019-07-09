Generators: The Final Frontier (David Beazley)
==============================================

Part I
------
* Preliminaries - Generators and Coroutines 
    - yield statement defines a generator function 
```
def countdown(n):
    while n > 0:
        yield n 
        n -= 1 

# You typically use it to feed iteration 
for x in countdown(10):
    print("T-minus", x)
```
    - Generator object runs in response to next() StopIteration raised when function returns
```
next(gen) - Advances to the next yield 
>>> c = countdown(3)
>>> c
<generator object countdown at 0x10a372318>
>>> next(c)
3
>>> next(c)
2
>>> next(c)
1
>>> next(c)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```
    - Generators as Pipelines 
```
Stacked generators result in processing pipelines 
Similar to shell pipes in Unix 

input sequence -> generator -> generator -> for x in s:
```
    - yield can receive a value instead 
```
gen.send(item) - Send an item tp a generator 
def receiver():
    while True:
        item = yield 
        print("Got), item

# It defines a generator that you send things to 
    recv = receiver() 
    next(recv)      # Advance to first yield 
    recv.send('Hello')
    recv.send('World')

gen.close() - Terminate a generator 
def generator():
    try:
        yield 
    except GeneratorExit:
        # Shutting down 

g = generator()
next(g)     # Advance to yield 
g.close()   # Terminate 
Raises GeneratorExit at the yield 
Only allowed action is to return 
If uncaught, generator silently terminates 

Raising Exceptions 
# gen.throw(typ [, va [,tb]]) - Throw exception 
def generator():
    ...
    try:
        yield 
    except RuntimeError as e:
        ...
    yield val 

g = generator() 
next(g)     # Advance to yield 
val = g.throw(RuntimeError, 'Broken')

Raises exception at yield 
Return the next yield value (if any)

Generator Return Values 
StopIteration raised on generator exit 
def generator():
    ...
    yield 
    ...
    return result 

g = generator()
try:
    next(g)
except StopIteration as e:
    result = e.value 

Return value (if any) passed with exception 

Generator Delegation 
yield from gen - Delegate to a subgenerator 
def generator():
    ...
    yield value 
    ...
    return result 

def func():
    result = yield from generator()
Allows generators to call other generators 
Operations take place at the current yield 
Return value (if any) is returned

Delegation Example 
Chain iterables together 

def chain(x, y):
    yield from x 
    yield from y 

Example:
>>> a = [1, 2, 3]
>>> b = [4, 5, 6]
>>> for x in chain(a, b):
        print(x, end=' ')
1 2 3 4 5 6

Mini-Reference 
Generator definition 

def generator():
    ...
    yield 
    ...
    return result 

Generator instance operations 
gen = generator()
next(gen)                   # Advance to next yield 
gen.send(item)              # Send an item 
gen.close()                 # Terminate 
gen.throw(exc, val, tb)     # Raise exception 
result = yield from gen     # Delegate 
```

    - Coroutines and Dataflow 
```
Coroutines enable dataflow style processing 
Public/subscribe, event simulation, etc 
```

Part II 
-------
```
    A Common Motif 
Consider the following
    f = open 
    ...
    f.close() 
~~~~~~~~~~~~~~~~~~~~~
    lock.acquire() 
    ...
    local.release() 
~~~~~~~~~~~~~~~~~~~~~
    db.start_transaction() 
    ...
    db.commit() 
~~~~~~~~~~~~~~~~~~~~~
    start = time.time()
    ...
    end = time.time 

It's so common, you'll see it everywhere!
```
```
    Context Managers 
The 'with' statement 
    with open(filename) as f:
        statement
        statement
        ...

    with lock:
        statement
        statement 
        ...
Allows control over entry/exit of a code block 
Typical use: everything on the previous slide 
```
```
    Context Management 
It's easy to make your own (@contextmanager)
    import time 
    from contextlib import contextmanager 

    @contextmanager 
    def timethis(label):
        start = time.time() 
        try:
            yield 
        finally:
            end = time.time() 
            print('%s: %0.3f' % (label, end-start))
This times a block of statements
```
