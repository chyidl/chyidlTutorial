Data Structures and Algorithms
==============================
> 人生路上、我们回遇到很多坎坷，跨过去，你就可以成长，跨不过去就是困难和停滞。而且后面很长的一段时间里，你都需要为这个困难买单。

复杂度分析
--------
```

```

Array
-----
* Implementation an array that supports dynamic expansion 
- [Python3 Implement : array_dynamic_append_implement.py](/root/os/DSAA/DataStructuresAndAlgorithms/python/array_dynamic_append_implement.py)
* Implementation an ordered array of fixed size, support dynamic additions and deletions 
- [Python3 Implement: array_fixed_size_CURD_implement.py](/root/os/DSAA/DataStructuresAndAlgorithms/python/array_fixed_size_CURD_implement.py)
* Implementation two ordered arrays into one ordered array. 
- [Python3 array_merge_sorted_implement.py](/root/os/DSAA/DataStructuresAndAlgorithms/python/array_merge_sorted_implement.py)

Linked List
-----------
* Implement single-linked list, circular linked list, and doubly linked list to support addition and deletion operations 
- [Python3 Implement : linked_list_singly_implement.py](/root/os/DSAA/DataStructuresAndAlgorithms/python/linked_list_singly_implement.py)
- [Python3 Implement : linked_list_singly_circular_implement.py](/root/os/DSAA/DataStructuresAndAlgorithms/python/linked_list_singly_circular_implement.py)
- [Python3 linked_list_doubly_implement.py](/root/os/DSAA/DataStructuresAndAlgorithms/python/linked_list_doubly_implement.py)
* Implement single-linked list reversed
- [Python3 Implement : linked_list_singly_implement.py](/root/os/DSAA/DataStructuresAndAlgorithms/python/linked_list_singly_implement.py)
* Implementing two ordered linked lists into one ordered list 
- [Python3 Implement : linked_list_merge_two_sorted_implement.py](/root/os/DSAA/DataStructuresAndAlgorithms/python/linked_list_merge_two_sorted_implement.py)
* Implement the intermediate node of the linked list 


Stack
-----
* Implement a sequential stack with arrays 
- [Python3 stack_array_implement.py](/root/os/DSAA/DataStructuresAndAlgorithms/python/stack_array_implement.py)
* Implement a chain stack with a linked list 
- [Python3 stack_linked_list_implement.py](/root/os/DSAA/DataStructuresAndAlgorithms/python/stack_linked_list_implement.py)
* Programming simulation to implement a browser's forward and backward functions
- [stack_browser_back_forward_button_implement.py](/root/os/DSAA/DataStructuresAndAlgorithms/python/stack_browser_back_forward_button_implement.py)


Heap
----
* Implement a small top heap, a large top heap, and a priority queue 
* Implement heap sorting 
* Merging K ordered arrays with priority queues 
* Find the largest Top K of a set of dynamic data sets

Queue
-----
* Implement an order queue with arrays 
- [Python3 queue_array_implement.py](/root/os/DSAA/DataStructuresAndAlgorithms/python/queue_array_implement.py)
* Implement a chained queue with a linked list 
- [Python3 queue_linked_list_implement.py](/root/os/DSAA/DataStructuresAndAlgorithms/python/queue_linked_list_implement.py)
* Implement a circular queue 
- [Python3 queue_circular_array_implement.py](/root/os/DSAA/DataStructuresAndAlgorithms/python/queue_circular_array_implement.py)

Binary Tree
-----------
* Implement a binary search tree and support insert, delete, and find operations 
* Implement the lookup of the successor and precursor nodes of a node in the binary search tree 
* Implement binary, pre-, post-, and post-order traversal 
```
Binary Tree 二叉树
    每个节点最多有两个字节点
    1. 满二叉树: 叶子节点全部在最底层、除了叶子结点之外、每个节点都有左右两个字节点
    2. 完全二叉树: 叶子结点都在最底下两层，最后一层的叶子结点都靠左排列，并且除了最后一层，其他层的节点个数都达到最大

    二叉树的链式存储：
        每个节点需要三个字段：一个存储数据、另外两个指向左右子节点
    二叉树的顺序存储：
        根节点存储在下标1的位置、左子节点存储在下标2*i的位置，右字节点存储在2*i+1位置

二叉树的遍历:
    1. 前序遍历: 对树中的任意节点来说，先打印这个节点、再打印左节点、最后打印右节点
        preOrder(r) = print r-> preOrder(r-left)->preOrder(r-right)
    2. 中序遍历: 对树中的任意节点来说，先打印左节点，然后打印本身，在打印右节点 
        inOrder(r) = print inOrder(r-left)-> print r ->inOrder(r-right)
    3. 后序遍历: 对于书中的任意节点来说，先打印左节点、在打印右节点、最后打印节点本身
        postOrder(r) = postOrder(r->left)->postOrder(r->right)->print r

Binary Search Tree 二叉查找树:
    二叉查找树要求在树中的任意节点、左子树的每个节点的值，都要小于这个节点的值，而右子树节点的值都要大于这个节点的值
    
```


Graph
-----
* Implementing directed graph, undirected graph, entitlement graph, and unweight graph representation method Asymmetric matrix and adjacency list. 
* Depth-first search, breadth-first search for graphs 
* Implement Bellman-Ford algorithm, A algorithm.
- [Python3 Bellman-Ford_algorithm_implement.py](/root/os/DSAA/DataStructuresAndAlgorithms/python/Bellman-Ford_algorithm_implement.py)
* Implement Dijkstra algorithm, A algorithm 
* Kahn algorithm and DFS algroithm for toplogical sorting 

Recursive
---------
* Programming to achieve Fibonacci sequence evaluation 
- [Python3 recursion_implement.py](/root/os/DSAA/DataStructuresAndAlgorithms/python/recursion_implement.py)
* Programming to achieve factorial 
- [Python3 recursion_implement.py](/root/os/DSAA/DataStructuresAndAlgorithms/python/recursion_implement.py)
* Programming implements a full array of data sets 
- [Python3 recursion_arrangement_implement.py](/root/os/DSAA/DataStructuresAndAlgorithms/python/recursion_arrangement_implement.py)

Sort
----
* Implement merge sort, quick sort, insert sort, bubble sort, select sort
- [Python3 sort_bubble_array_implement.py](/root/os/DSAA/DataStructuresAndAlgorithms/python/sort_bubble_array_implement.py)
- [Python3 sort_insert_array_implement.py](/root/os/DSAA/DataStructuresAndAlgorithms/python/sort_insert_array_implement.py)
- [Python3 sort_selection_array_implement.py](/root/os/DSAA/DataStructuresAndAlgorithms/python/sort_selection_array_implement.py)
- [Python3 sort_merge_array_implement.py](/root/os/DSAA/DataStructuresAndAlgorithms/python/sort_merge_array_implement.py)
- [Python3 sort_quick_array_implement.py](/root/os/DSAA/DataStructuresAndAlgorithms/python/sort_quick_array_implement.py)
* Programming to achieve the Kth element of a set of data within O(n) time complexity

* 线性排序(Linear sort) - 桶排序、计数排序、基数排序
```
桶排序 (Bucket sort):
    1. 将要排序的数据分到几个有序的桶里，每个桶里的数据在单独进行排序，桶内排序完之后，再把每个桶里的数据按照顺序依照次序取出，组成的序列就是有序.
    2. 桶排序比较适合在外部排序中 

计数排序 (Counting sort):
    1. 计数排序只能用在数据范围不大的场景中,如果数据范围k比排序的数据大很多，就不使用

基数排序 Radix sort:
    基数排序要求数据可以划分为高低位， 位之间的有递进关系，比较两个数
```

* 排序的优化
```
    理想的分区点: 被分区点分开的两个分区中，数据的数量差不多
        1. 三数取中法
        2. 随机选取分区点 
    
```

Binary search 
-------------
```
二分查找针对是一个有序的数据集合: 
    时间复杂度 - O(logn)
    二分查找依赖顺序表结构 -- 数组 
    二分查找针对的是有序数据
    二分查找只能用于插入、删除操作不频繁，一次排序多次查询的场景中 

IP地址库查找 
    1. 查找第一个值等于给定值的元素
    2. 查找最后一个值等于给定值的元素
    3. 查找第一个大于等于给定值的元素
    4. 查找最后一个小于等于给定值的元素 

```
* Implement a binary search algorithm with ordered array 
- [Python3 binary_search_array_implement.py](/root/os/DSAA/DataStructuresAndAlgorithms/python/binary_search_array_implement.py)
* Implement fuzzy binary search algorithm (Such as the first element greater than or euqal to the given value)
```
平衡二叉树: 任意一个节点的左右子树的高度相差不能大于1
    1. AVL树: 任意节点的左右子树的高度相差不超过1，是一种高度平衡的二叉查找树
    2. Splay Tree 伸展树 
    3. Treap 树堆
    4. Red-Black Tree: R-B Tree红黑树 是一种不严格的平衡二叉查找树
        1. 根节点是黑色
        2. 每个叶子节点都是黑色的空节点NULL, 叶子节点不存储数据
        3. 任何相邻的节点都不能同时为红色，红色节点是被黑色节点隔开的
        4. 每个节点从该节点到达叶子结点的所有路径都包含相同树目的黑色节点

实现红黑树的基本思想：
    一颗合格的红黑树需要满足:
        1. 根节点是黑色
        2. 每个叶子节点都是黑色的空节点NULL,
        3. 任何相邻的节点都不能同时为红色
        4. 每个节点从该节点到达叶子节点的所有路径都包含相同数目的黑色节点
    左旋: rotate left 

    右旋: rotate right 

    插入操作:
        红黑树规定：插入的节点必须是红色，而且，二叉查找树的新插入的节点都放在叶子节点上
            1. 插入节点的父节点是黑色
            2. 插入节点是根节点，直接改变插入节点的颜色，变成黑色 
        调整过程：左右旋转、改变颜色 
    CASE 1: 如果关注节点是a,叔叔节点d是红色，
```


* Skip List 
```
跳表：动态数据结构，可以支持快速的插入、删除、查找操作，甚至可以代替红黑树 Red-black Tree 
Redis:
    Sort Set:有序集合 就是使用跳表实现 
    链表加上多级索引的结构，就是跳表 
    
```

Hash Table
----------
* Implement a list of calculations based on linked list method to solve conflict problems
* LRU(Least Recently Used) Cache Implementation
- [Python3 linked_list_LRU_implement.py](/root/os/DSAA/DataStructuresAndAlgorithms/python/linked_list_LRU_implement.py)
```
散列函数(Hash函数)
    1. 散列函数计算得到的散列值是一个非负整数
    2. 如果key1==key2, hash(key1) == hash(key2)
    3. 如果key1=/=key2, hash(key1)=/=hash(key2)
    MD5、SHA、CRC哈希算法：无法完全避免散列冲突

散列值(Hash值)

散列冲突:
    1. 开放寻址Open addressing 
        可以利用CPU缓存加快查询速度，
            Java中ThreadLocalMap使用开发寻址解决散列表冲突的原因 
        线性探测 linear Probing 
        二次探测Quadratic probing 
        双重散列Double hashing [一组hash函数]
    2. 链表法 chaining 
        skiplist、红黑树
    装载因子load factor:填入表中的元素个数/散列表的长度
    装载因子越大，说明空闲位置越少，冲突越多，散列表的性能会下降

散列表碰撞攻击的基本原理:
一次性扩容耗时过多的情况，可以将扩容操作穿插在插入操作的过程中。分批完成

哈希算法 : MD5 SHA 
    将任意长度的二进制串映射为固定长度的二进制串，这个映射的规则就是哈希算法
    1. 从哈希值不能反响推导出原始数据 - 单向哈希算法
    2. 输入数据非常敏感
    3. 散列冲突的概率低 
    4. 哈希算法的执行效率要尽量高效，针对较长的文本，也能快速的计算出哈希值

    MD5哈希值128Bit长度

哈希算法应用:
    1. 安全加密
        MD5(Message Digest Algorithm消息摘要算法) -- 号称已经被破解
        SHA (Secure Hash Algorithm) 安全散列算法 -- 
        DES(Data Encryption Standard)数据加密标准 
        AES（Advanced Encryption Standard）高级加密标准 
    2. 唯一标识
        比对数据
    3. 数据校验
        BT下载原理是基于P2P协议
    4. 散列函数
        salt盐 跟用户密码组合使用，增加密码的复杂度
    5. 负载均衡
        通过hash算法对客户端IP地址或会话计算哈希值，将取得的哈希值与服务器列表的大小进行取模运算，最终得到的值就是应该被路由到的服务器编号
    6. 数据分片
        MapReduce设计思想
        采用多机分布式处理，这种分片的思路可以突破单机内存、CPU等资源的限制
    7. 分布式存储
        雪崩效应: 缓存失效，所有数据请求都会穿透缓存，直接请求数据库
        一致性hash算法：
```


String 
------
* Implement a character set that contains only the 26-character Trie tree of a~z 
* Implement a simple string matching algorithm 

Backtracking
---------------
* Using backtracking algorithm to solve the problem of eight queens 
* Using backtracking algorithm to solve 0-1 knapsack problem 

Division and treatment algorithm
-------------------------------------
* Using the divide and conquer algorithm to find the reverse order of a set of data 

Dynamic planning 
--------------------
* 0-1 backpack problem 
* Sum of Minimum path 
* Programming to achieve the shortest edit distance of Levins 
* Programmatically find the longest common subsequence of two strings 
* Programming to implement the longest increasing subsequence of a data sequence

Chyidl Utils -- chutils
-----------------------
A series of convenience functions to make programming easier with python3
<<<<<<< HEAD
- [chutils](/root/os/DSAA/DataStructuresAndAlgorithms/python/chutils)
||||||| d5d8e56
- [chutils](/root/os/DSAA/DataStructuresAndAlgorithms/python/chutils)
=======
- [chutils](/root/os/DSAA/DataStructuresAndAlgorithms/python/chutils)

Scheduling Algorithm
--------------------

* Bloom Filter - 布隆过滤器
> 布隆过滤器是1970年由布隆提出，它实际上是一个很长的二进制向量和一系列随机映射函数.布隆过滤器可以用于检索一个元素是否在一个集合中。优点是空间效率和查询时间都远远超过一般的算法，缺点是有一定的误识别率和删除困难.
```
判断一个元素是不是在一个集合中，一般思路是将集合中所有元素保存起来，然后比较确定
    链表结构: 时间复杂度O(n)
    树结构: 时间复杂度O(log n)
    散列表结构: 时间复杂度O(1)

布隆过滤器的原理是当一个元素被加入集合中，通过K个散列函数将这个元素映射成一个数组中的K个点，把他们置为1.检索时，只要查看这些点是不是都是1就(大约)知道集合中有没有它，如果这些点有任何一个0，则被检元素一定不在。如果都是1，怎被检元素很可能在.

优点:
    相比其他数据结构，布隆过滤器在空间和时间方面都有巨大的优势，布隆过滤器存储空间和插入/查询时间都是常数(O(K)). 另外，散列函数相互之间没有关系，方便由硬件并行实现。布隆过滤器不需要存储元素本身，在某些对保密要求非常严格的场合有优势.
    布隆过滤器可以表示全集，其他任何数据结构都不能
    k和m相同,使用同一组散列函数的两个布隆过滤器的交并运算可以使用位操作进行.

缺点:
    但是布隆过滤器的缺点和优点一样明显，误算率是其中之一，随着存入的元素数量的增加，误算率随之增加，但是如果元素数量太少，则使用散列表足以
    一般情况下不能从布隆过滤器中删除元素，很容易想到把位数组变成整数数组,每插入一个元素响应的计算器加一，这样删除元素时将计数器减掉就可以，然而要保证安全地删除元素并非如此简单，首先我们必须保证删除的元素的确在布隆过滤器里面，这一点单凭这个过滤器时无法保证的，另外计数器回绕也会造成问题
```

* Round-robin scheduling 
```
Round-robin (RR) is one of the algorithms employed by process and network schedulers in computing. Round-robin scheduling is simple, easy to implement, and starvation-free.Round-robin scheduling can also be applied to other scheduling problems, such as data packet scheduling in computer networks. It is an operating system concept.

Round Robin is a CPU scheduling algorithm where each process is assigned a fixed time slot in a cyclic way. 

    1. It is simple, easy to implement, and starvation-free as all processes get fair share of CPU. 
    2. One of the most commonly used technique in CPU scheduling as a core. 
    3. It is preemptive as processes are assigned CPU only for a fixed slice of time at most.
    4. The disadvantage of it is more overhead of context switching.

AWT(average waiting time): 
```
>>>>>>> 17e65b27933a988ecb5aa15f7047add37944e12c
