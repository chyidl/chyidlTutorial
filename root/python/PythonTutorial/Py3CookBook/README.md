Python CookBook Third Edition
=============================

1. Data Structures and Algorithms
----------------------------------
* [1.3.Keeping the Last N Items]()
    ```
    from collections import deque: cpython/Modules/_collectionsmodules.c
    ``` 
* [1.4.Finding the Largest or Smallest N Items]()
    ```
    import heapq: cpython/Lib/heapq.py 
    
    Heap queue algorithm (a.k.a. priority queue).

    Heaps are arrays for which a[k] <= a[2*k+1] and a[k] <= a[2*k+2] for all k. a[0] is always its smallest element.

    Usage:
        
    heap = []               # creates an empty heap 
    heappush(heap, item)    # pushes a new item on the heap 
    item = heappop(heap)    # pops the smallest item from the heap 
    item = heap[0]          # smallest item on the heap without popping it 
    heapify(x)              # transforms list into a heap, in-place, in linear time 
    item = heapreplace(heap, item) # pops and returns smallest item, and adds new item; the heap size is unchanged. 
    ```
* [1.5.Implementing a Priority Queue]() 
    ```
    import heapq; since the push and pop operations have O(logN) complexity where N is the number of items in the heap.
    ```
* [1.6.Mapping Keys to Multipe Values in a Dictionary]()
    ```
    from collections import defaultdict; cpython/Modules/_collectionsmodules.c 
    ```
* [1.7.Keeping Dictionaries in Order]()
    ```
    Be aware that the size of an OrderedDict is more than twice as large as a normal dictionary due to the extra linked list 
    ```
* [1.8.Calculating with Dictionaries]()
* [1.9.Finding Commonalities in Two Dictionaries]()
    ```
    dict.keys() support common set operations such as "union, intersection, difference." Thus, If you need to perform common set operations with keys, you can often just use the keys-view objects directly without first converting them into a set.

    dict.items() returns an items-view object consisting of (key,value) pairs. This object supports similar set operations and can be used to perform operations such as finding out which key-value pairs two dictionaries have in common. 
    dict.values() method of a dictionary does not support the set operations described in this recipe.
    ```
* [1.10.Removing Duplicates from a Sequence while Maintaining Order]()
    ```
    ```
