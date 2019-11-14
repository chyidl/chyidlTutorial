Architecture Design
===================

* CQRS (Command Query Responsibility Segregation)
```
CQRS 架构就是一个系统从架构上拆分为两部分：命令处理(写请求) + 查询处理(读请求).然后读写两边可以使用不同的架构实现，以实现CQ两端(Command Side; Query Side)的分别优化。
CQRS 作为一个读写分离思想的结构，在数据存储方面，没有做过多约束
    1. CQ两端数据数据共享，CQ两端只是在上层代码上分离，这种做法带来的好处是可以让我们的代码读写分离，更好维护，且没有CQ两端的数据一致性问题。因为是共享一个数据库。
    2. CQ两端数据库和上层代码都分离，然后Q的数据由C端同步，一般是通过Domain Event进行同步.同步方式有两种，同步或异步，如果需要CQ两端的强一致性，
```

* CORS (Cross Origin Resource Sharing)
> Cross-origin resource sharing (CORS) is a mechainism that allows restricted resources on a web page to be requested from another domain outside the domain from which the first resource was served.
```

```