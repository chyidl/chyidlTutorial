数据结构与算法-Java篇
==================
> 书读百遍其义自见

* 数据结构和算法的定义?
```
数据结构:就是指一组数据的存储结构
算法:就是操作数据的一组方法

数据结构是为算法服务的，算法要作用在特定的数据结构之上.
```

* 时间、空间复杂度分析?
```
事后统计法: 
    测试结果非常依赖测试环境
    测试结果受数据规模的影响很大 

大O复杂度表示法:
    - 大O时间复杂度表示法并不具体表示代码真正的执行时间，而是表示代码执行时间随数据规模增长的变化趋势.也称为渐进时间复杂度(asymptotic time complexity),简称时间复杂度. 总的时间复杂度就等于量级最大的那段代码的时间复杂度.

    - 大O空间复杂度分析:(asymptotic space complexity)表示算法的存储空间与数据规模之间的增长关系

常见的时间复杂度量级:
    多项式量级:
        常量阶 O(1)
        对数阶 O(logn)
        线性对数阶 O(nlogn) - 归并排序、快速排序的时间复杂度都是O(nlogn)
        线性阶 O(n)
        平方阶 O(n^2)
        立方阶 O(n^3)
        K次方阶 O(n^k)
    非多项式量级:(NP - Non-Deterministic Polynomial非确定多项式)
        指数阶 O(2^n)
        阶乘(O(n!))

常见的空间复杂度量级:
    O(1)
    O(n)
    O(n^2)
    O(logn)
    O(nlongn)

最好情况时间复杂度(best case time complexity)
最坏情况时间复杂度(worst case time complexity)
平均情况时间复杂度(average case time complexity): 加权平均时间复杂度;期望时间复杂度
均摊时间复杂度(amortized time complexity)


```