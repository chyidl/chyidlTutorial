The actor model
===============
> The actual model is a conceptual model to deal with concurrent computation. It defines some general rules for how the system's components should behave and interact with each other. 

Actors
------
> An actor is the primitive unit of computation.
> https://www.brianstorti.com/the-actor-model/
```
Actors communicate with each other by sending asynchronous messages. Those message are stored in other actors' mailboxes until they're processed.

What actors do?
  1. Create more actors 
  2. Send message to other actors 
  3. Designate what to do with the next message 
```

Fault tolerance
--------------
```
```
