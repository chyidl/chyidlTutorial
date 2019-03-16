# 关于Python面试题

## Python 语言特性

### 1. Python Parameters Passed by Reference or Value?

If you pass a mutable object into a method, the method gets a reference to that same object and you can mutate it to your heart's delight, but if you rebind the reference in the method, the outer scope will know nothing about it, and after your're done, the outer reference will still point at the original object.
  
If you pass an immutable object to a method, you still can't rebind the outer reference, and 

To make it even more clear, let's have some examples.

**List - a mutable type**

Let's try to modify the list that was passed to a method:

```python3
# Since the parameter passed in is a reference to outer_list, not a copy of it, we can use the mutating list methods to change it and have the changes reflected in the outer scope.
def try_to_change_list_contents(the_list):
    print('got', the_list)
    the_list.append('four')
    print('changed to', the_list)

outer_list = ['one', 'two', 'three']

print('before, outer_list =', outer_list)
try_to_change_list_contents(outer_list)
print('after, outer_list =', outer_list)
```

Output:

```python
before, outer_list = ['one', 'two','three']                                   
got ['one', 'two', 'three']
changed to ['one', 'two', 'three', 'four']                                     
after, outer_list = ['one', 'two', 'three', 'four']  
```

**Now let's see what happens when we try to change the reference that was passed in as a parameter:**

```python
# Since the the_list parameter was passed by value, assigning a new list to it had no effect that the code outside the method could see. The the_list was a copy of the outer_list reference.
def try_to_change_list_reference(the_list):
    print('got', the_list)
    the_list = ['and', 'we', 'can', 'not', 'lie']
    print('set to', the_list)

outer_list = ['we', 'like', 'proper', 'English']

print('before, outer_list =', outer_list)
try_to_change_list_reference(outer_list)
print('after, outer_list =', outer_list)
```

Output:

```python
before, outer_list = ['we', 'like', 'proper', 'English']
got ['we', 'like', 'proper', 'English']
set to ['and', 'we', 'can', 'not', 'lie']
after, outer_list = ['we', 'like', 'proper', 'English']
```

**String - an immutable type**

It's immutable, so there's nothing we can do to change the contents of the string

```python
def try_to_change_string_reference(the_string):
    print('got', the_string)
    the_string = 'In a kingdom by the sea'
    print('set to', the_string)

outer_string = 'It was many and many a year ago'

print('before, outer_string =', outer_string)
try_to_change_string_reference(outer_string)
print('after, outer_string =', outer_string)
```

Output:

```python
before, outer_string = It was many and many a year ago
got It was many and many a year ago 
set to In a kingdom by the sear
after, outer_string = It was many and many a year ago
```

**Question: Is there somethng I can do to pass the variable by actual reference?**

1. You could return the new value. This doesn't change the way things are passed in, but does let you get information you want back out:

```python
def return_a_whole_new_string(the_string):
    new_string = something_to_do_with_the_old_string(the_string)
    return new_string

# then you could call it like 
my_string = return_a_whole_new_string(my_string)
```
(https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference)

### 2. Python Metaclasses?

A metaclass is the class of a class. Like a class defines how an instance of the class behaves, a metaclass defines how a class behaves. A class is an instance of a metaclass. 

**type** is the usual metaclass in Python. **type** is itself a class, and it is its own type. A metaclass is most commonly used as a class-factory. Combined with the normal __intit__ and __new__ methods, metaclasses therefor allow you to do 'extra things' when creating a class, like registering the new class with some registry, or even replace the class with something else entirely.

metaclasses actually define the type of a class, not just a factory for it, so you can do much more with them. metaclass can define normal methods like classmethods, can be called on the class without an instance, but cannot called on an instance of the class.

```python

```

### 3. @staticmethod @classmethod  @instancemethod 

```python
class A(object):
    def foo(self, x):
        print("executing foo(%s, %s)"%(self, x))

    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s, %s)" %(cls, x))

    @staticmethod 
    def static_foo(x):
        print("executing static_foo(%s)" %x)

a = A(1)

```

### 4. OrderedDict vs defaultdict vs dict 

```


```


Interesting interview questions
--------------------------------

* Monkeys eating peach 
```
"""
猴子吃桃的问题:一只小猴子吃桃子的问题，话说，一只小猴子第一天摘下若干个桃子，并吃了一半，感觉还不过瘾，于是又多吃了一个
第二天早上，又将剩下的桃子吃掉一半，又多吃一个
以后每天早上都吃了前一天剩下的一半多一个。
请问到了第10天早上想吃时却发现只剩下1个桃子。求第一天共摘多少个？
题目分析：
第一天的桃子数量，等于第二天桃子数 + 1 * 2
第二天的桃子数量, 等于第三天桃子数 + 1 * 2
...
第九天的桃子数量，等于第十天桃子数 + 1 * 2
"""


def howManyPeach_v1(days):
    sum = 0  # 初始化总桃子数
    sum = 1
    print("第{:0>2d}天，有{:0>4d}桃子".format(days, sum))
    while days > 1:
        sum = (sum + 1)*2
        days -= 1
        print("第{:0>2d}天，有{:0>4d}桃子".format(days, sum))
    return sum
```
