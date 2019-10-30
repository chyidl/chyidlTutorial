Distributed Systems in One lession
==================================

What is a distributed System?
-----------------------------
```
A collection of independent computers taht appear to its users as one computer. 
    - Andrew Tannenbaum 

# Three Characteristics
    1. The computer operate concurrently 
    2. The computers fail independently 
    3. The computers do not share a global clock 

# Three Topics 
    1. Storage 
    2. Computation 
    3. Messaging 
```

Distributed Storage
-------------------
```
Single-Master Storage -> Read Replication(broken consistency) -> Sharding(broken consistency;Consistent Hashing;Replication;)

Consistent Hashing: 一致性哈希

R + W > N  : strong consistency 
    number of nodes Writes
    number of nodes Reads
    number of node replices

everything is a problem in a distributed system and solving one problem creates another one 

CAP Theorem:


typically in a web systems there are more reads than writes 
```

```
KafKa -- 
```