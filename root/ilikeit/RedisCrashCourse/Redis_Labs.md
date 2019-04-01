Why Your MySQL Needs Redis
==========================

a Simple Storefront Example
---------------------------
> Database <--> Data Access Layer <--> Multi Applications <--> Multi Users

> More Database <--> Data Access Layer <--> More Application <--> More Users 
```
Challenge #1: How to munimize the cost of data management while scaling?

More users and applications implies 
    Higher data volumes .
    More tables, changes to schema.
    More computing resources to deliver low latency response.

Challenge #2: How to achieve faster time to the market?

Adding new apps and features require
    Flexible data models 
    Ease of developemnt 
    Lean processes for expansion 

Challenge #3: How to keep your applications responsive?

Given the average network latency of 200ms your apps require sub-millisecond latency for data access. 

Challenge #4: How to overcome the physical limits on database capacity?

Disk based databases are inherently limited, even adding more resources doesn't decrease latency.
```
> It's not the load that breaks you down, it's the way you carry it - Lena Home.


redis
-----
> Open source. The leading in-memory database platform, supporting any high performance operational, analytics or hybrid use case.

redislabs - Home of redis 
-------------------------
> redislabs is the company that's behind this open source project. The open source home and commercial provider of Redis Enterprise technilogy, platform, products & services. 
```
Redis Top Differentiators 
    
    1. Performance (NoSQL Benchmark) - The Most powerful Database.
        
    2. Simplicity (Redis Data Structures)
    3. Extensibility (Redis Modules)
```
