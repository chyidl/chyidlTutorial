# Mastering Algorithms With C

.xcodeproj file is Xcode Project Files.

## macOS OR Linux Run:

$ ./run.sh sort 

![./run.sh sort ](/imgs/os/DSAA/MasteringAlthorithmsWithC/Details_Page1.png?raw=true)

## Data Structure

### Recursion

A resursive function is a function that calls itself.Each successive call works on a more refined set of inputs, bringing us closer and closer to the solution of a problem.

Two basic phases of recursive process: winding and unwinding.
    1. In the winding phase, each recursive call perpetuates the recursion by making and additional recursive call itself. The winding phase terminates when one of the calls reaches a terminating condition.
    2. The unwinding phase, in which previous instances of the function are revistied in reverse order. This phase continues until the original call returns, at which point the resursive process is complete.

![The Organization of a C program in memory](/imgs/os/DSAA/MasteringAlthorithmsWithC/organization_of_c_program_in_memory.png?raw=true)

C Program consist of four areas as it executes: 
    1. A code area          -- contains the machine instructions that are executed as the program runs.
    2. A static data area   -- contains the data that persists throughout the life of the program. such as global variables and static local variables.
    3. A heap               -- contains dynamically allocated storage, such as memory allocated by malloc.
    4. A stack              -- contains information about function calls.


![The stack of a C program while computing 4! recursively](/imgs/os/DSAA/MasteringAlthorithmsWithC/Factories_Recursion.png?raw=true) 
- [Factorials Recursion](/root/os/DSAA/MasteringAlgorithmsWithC/MasterAlgorithmsWithC/source/fact.c)

![The Stack of a C program while computing 4! in a tail-recursive manner](/imgs/os/DSAA/MasteringAlthorithmsWithC/Tail_Recursive.png?raw=true)
- [Tail Recursive Mannger](/root/os/DSAA/MasteringAlgorithmsWithC/MasterAlgorithmsWithC/source/facttail.c)


### Linked lists 

![single linked list](/imgs/os/DSAA/MasteringAlthorithmsWithC/Singly_linked_lists.png?raw=true)
- [Singly-linked lists](/root/os/DSAA/MasteringAlgorithmsWithC/MasterAlgorithmsWithC/source/list.c)

![Virtual memory](/imgs/os/DSAA/MasteringAlthorithmsWithC/Virtual_memory.png?raw=true)

Virtual memory is a mapping of address space that allows a process (a running program) to execute without being completely in physical memory, the real memory of the system. One advantage of this is that a process can make use of an address space that is much larger than that which the physical memory of the system would allow otherwise. Another advantage is that multiple processes can share the memory of the system while running concurrently.

Each process has its own page table that maps pages of its virtual address space to frames in physical memory.

- [Frame Management](/root/os/DSAA/MasteringAlgorithmsWithC/MasterAlgorithmsWithC/source/frames.c)

![Doubly Linked lists](/imgs/os/DSAA/MasteringAlthorithmsWithC/Doubly_linked_lists.png?raw=true)

Doubly-linked list consists of three parts: a data member, a pointer to the next, and a pointer to the previous element.

- [Doubly-linked lists](/root/os/DSAA/MasteringAlgorithmsWithC/MasterAlgorithmsWithC/source/dlist.c)

![circular list](/imgs/os/DSAA/MasteringAlthorithmsWithC/circular_list.png?raw=true)

A circular list may be singly-linked or doubly-linked, but its distinguishing feature is that it has no tail. In a circular list, the next pointer of the last element points back to its first element rather than to NULL. In the case of a doubly-linked circular list, the prev pointer of the first element is set to point to the last element as well.

- [Circular lists](/root/os/DSAA/MasteringAlgorithmsWithC/MasterAlgorithmsWithC/source/clist.c)

![Second-chance Page-replacement algorithm](/imgs/os/DSAA/MasteringAlthorithmsWithC/second-chancePage.png?raw=true)

The system uses a **page-replacement algorithm** to determine which frame is best to free at a given moment. One example of a page-replacement algorithm is the **second-chance algorithm**, sometimes called the **clock algorithm**

However, since operation system can't predict the future, a system sometimes uses an assumption that the past will be a reasonable indication of the future and replaces the page that has been accessed least recently. This is known as **least recently used**, or LRU, page replacement.

- [Second-Chance Page Replacement](/root/os/DSAA/MasteringAlgorithmsWithC/MasterAlgorithmsWithC/source/page.c)


### Stacks and Queues

![Stack](/imgs/os/DSAA/MasteringAlthorithmsWithC/stack.png?raw=true)

**Stack** is that it stores and retrieves data in a last-in, first-out, or LIFO.

The structure **Stack** is the stack data structure. One way to implement at stack is as a linked list. A simple way to do this is to **typedef Stack List**

determine whether a specific element resides in the stack. to do this, we get the element at the head of the list using **list_head** and traverse the list using **list_next**. Using only stack operations, we would have to **pop** the elements one at a time, inspect them, and **push**  them onto another stack temporarily.Then, after accessing all of the elements, we would need to rebuild the original stack by popping the elements off the temporary stack and pushing them back onto the
original one. This method would be **less efficient** and **undoubtedly** would look less than intutive in a program. 

- [Stacks](/root/os/DSAA/MasteringAlgorithmsWithC/MasterAlgorithmsWithC/source/stack.c)

![Queues](/imgs/os/DSAA/MasteringAlthorithmsWithC/queue.png?raw=true)

The distinguishing characteristic of a queue is that it stores and retrieves data in first-in, first-out, or FIFO, manner. In computing, to place an element at the tail of a queue, we **enqueue** it; to remove an element from the head, we **dequeue** it. Sometimes it is useful to inspect the element at the head of a queue without actually removing it, in which case we **peek** at it.

- [Queues](/root/os/DSAA/MasteringAlthorithmsWithC/MasterAlgorithmsWithC/source/queue.c)

**Event Handling**: One popular application of queue is handling events in **event-driven applications**. In nearly all event-driven applications, events can occur at any moment, so queues play an important role in storing events until an application is ready to deal with them.

- [Event Handling](/root/os/DSAA/MasteringAlthorithmsWithC/MasterAlgorithmsWithC/source/events.c)


### Sets 

![sets](/imgs/os/DSAA/MasteringAlthorithmsWithC/sets.png?raw=true)

*Sets* Abstract datatypes based on the mathematical concept of a set. Sets are unordered collections of related members in which no members occur more than once.

```
# A set containing no members is the **empty set**. The set of all possible members is the **universe**
S = U is the universe; S = Ø is the empty set

# Two sets are equal if they contain exactly the same members. 
S₁ = S₂ means S₁ and S₂ are equal; S₁ ‡ S₂ means S₁ and S₂ are not equal. 

S₁ ⊂ S₂ means S₁ is a subset of S₂; S₁ is not a subset of S₂

## Basic Operations 
S₁ ∪ S₂ represents the union of S₁ and S₂. 
S₁ ∩ S₂ represents the intersection of S₁ and S₂. 
S₁ - S₂ represents the difference of S₁ and S2₂. 

# The intersection of a set with the empty set is the empty set. The union of a set with the empty set is the original set. 

S ∩ Ø = Ø; S ∪ Ø = S 

# The intersection of a set with itself is the original set. the union of a set with itself is the original set. 

S ∩ S = S; S ∪ S = S; 

# The intersection of a set, S₁ with another set S₂, result in the same as the intersection of S₂ with S₁. The same is true for the union of two sets. This behavior is described by the commutative laws. 

S₁ ∪ S₂ = S₂ ∪ S₁; S₁ ∩ S₂ = S₂ ∩ S₁; 

# The intersection of a number of sets can be performed in any order. 
S₁ ∪ (S₂ ∪ S₃) = (S₁ ∪ S₂) ∪ S₃; 
S₁ ∩ (S₂ ∩ S₃) = (S₁ ∩ S₂) ∩ S₃; 

# The intersection of a set with the union of two others can be carried out in a distributed manner. 
S₁ ∩ (S₂ ∪ S₃) = (S₁ ∩ S₂) ∪ (S₁ ∩ S₃) 

# The intersection of a set with the union of itself and another results in the original set. 
S₁ ∩ (S₁ ∪ S₂) = S₁ 

# An interesting result occurs when the difference of one set is taken with either the intersection or union of two others.
S₁ - (S₂ ∪ S₃) = (S₁ - S₂)∩(S₁-S₃) 
```

- [Set](/root/os/DSAA/MasteringAlgorithmsWithC/MasterAlgorithmsWithC/source/set.c)

Set covering is an optimization problem that nicely models many problems of combinatorics and resource selection. Here is the idea: given a set S and a set P of subset A₁ to Aش of S, set C, which is composed of one or more sets from P, is said to cover S if each member in S is contained in at least one of the subsets in C; in addition, C contains as few sets from P as possible.

The algorithm for set covering is an approximation algorithm. It does not always obtain the best solution. the algorithm is greedy. As each set is selected from P, it is removed, and its members are removed from S as well. When there are no members left to cover in S, the cover set C is complete.

![set cover](/imgs/os/DSAA/MasteringAlthorithmsWithC/set_cover.png?raw=true)
- [Set covering](/root/os/DSAA/MasteringAlgorithmsWithC/MasterAlgorithmsWithC/source/cover.c)


### Hash Tables

The primary idea behind a hash table is to establish a mapping between the set of all possible **keys** and positions in the array using a **hash function**. A hash function accepts a key and returns its hash coding, or hash value. Keys vary in type, but hash codings are always integers. 

Most has functions map some keys to the same position in the table. When two keys map to the same position, they collide.

![chain Hash Table](/imgs/os/DSAA/MasteringAlthorithmsWithC/chain_Hash_Table.png?raw=true)

A chained hash table fundamentally consists of an array of linked lists. Each list forms a bucket in which we place all elements hashing to a specific position in the array.  To insert an element, we first pass its key to a hash function in a process called hashing the key. This tells us in which bucket the element belongs. We then insert the element at the head of the approproate list. Because each bucket is a linked list, a chained hash table is not limited to a fixed
number of elements.However, performance degrades if the table becomes too full.

**uniform hashing** is to distribute elements about the table in as uniform and random a manner as possible.

**load factor** of a hash table is defined as: α = n/m where n is the number of elements in the table and m is the number of positions.

A hash function **h** is a function we define to map a key **k** to some position **x** in a hash table. x is called the hash coding of k. **h(k)=x**

- [Chained hash tables](/root/os/DSAA/MasteringAlgorithmsWithC/MasterAlgorithmsWithC/source/chtbl.c)

A chained hash table is a good way to implement a symbol table because, in addition to being an efficient way to store and retrieve information.

- [Symbol Tables]()
- [Open-addressed hash tables]()


### Trees

![Trees](/imgs/os/DSAA/MasteringAlthorithmsWithC/trees.png?raw=true)

**Preorder traversal**: first traverse its root,then to the left and then to the right. explore subtrees to the left and right.The preorder traversal is a depth-first exploration

**Inorder traversal**: first traversae to the left, then to the root, and then to the right.

**Postorder traversal**: first traverse to the left, then to the right, and then to the root.

**Level-order traversal**: beginning at the root and proceed downward,visiting the nodes at each level from left to right. The level-order traversal is a breadth-first exploration.

**Tree Balancing**: This means making sure that one level of the tree is completely full before allowing a node to exist at the next level. A tree is balanced if all leaf nodes are at the same level or, if not, all leaf nodes are in the last two levels and the second-to-last level is full.

- [Binary Trees]()
- [Binary Traversal Trees]()
- [Binary Search Trees]()


### Heaps and Priority Queues

- [Heap]()
- [Priority queues]()
- [Parcel Sorting]()


### Graphs

- [Graphs]()
- [Depth-First Search]()
- [Breadth-First Search]()

## Algorithms 

### Sorting and Searching 

- [Insertion sort]()
- [Quick sort]()
- [Merge sort]()
- [Counting sort]()
- [Radix sort]()
- [Binary search]()


### Numerical Methods 

- [Polynomial interpolation]()
- [Least-squares estimation]()
- [Solution of equations]()


### Data Compression 

- [Bit operations]() 
- [Huffman coding]() 
- [Optimized Networking]()
- [LZ77]()


### Data Encryption

- [Data Encryption Standard]()
- [Block Cipher Modes]()
- [Rivest-Shamir-Adleman]()


### Graph Algorithms 

- [Minimum spanning trees]()
- [Shortest paths]()
- [Routing Tables]()
- [Traveling-salesman problem]()


### Geometric Algorithms

- [Testing whether line segments intersect]()
- [Convex hulls]()
- [Arc length on spberical surfaces]()
- [Approximating Distances on Earth]()
