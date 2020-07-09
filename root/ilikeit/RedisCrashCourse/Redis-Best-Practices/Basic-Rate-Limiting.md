Basic Rate Limiting
===================
> The basic concept is that you want to limit requests to a particular service in a given time period. 
```
have a service that has users identified by an API key 
This service states that it is limited to 20 requests in any given minute

1. Create a Redis key for every minute per API key. To make sure we don't fill up our entire database with junk, expire that key after one minute as well. 
  User API Key: xxxx
  Redis Key: xxxx:0 
    Value: x 
    Expires at: x 
    Time: x 

1. > GET [user-api-key]:[current minute number]
2. > if the resuklt from line is less than 20 (or unset) go to 4 otherwise line 3 
3. > Show error message and end connection. Exit 
4. > MULTI 
   OK 
   > INCR [user-api-key]:[current minute number]
   QUEUED 
   > EXPIRE [user-api-key]:[current minute number] 59 
   QUEUED 
  > EXEC 
  OK 

Two key points to understand from this routine:
1. INCR on a non-existent key will always be 1. the first call of the minute will be result the value of 1 
2. EXPIRE is inside a MULTI transaction along with the INCR, which means form a single atomic operation. 
```
