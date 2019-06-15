Cryptography
============
> Cryptography is the practice and study of techniques for secure communication in the presence of third paries called adversaries. More generally, cryptography is about constructing and analyzing protocols that prevent third parties or the public from reading private messages;

/dev/urandom VS /dev/random 
---------------------------
```
/dev/urandom and /dev/random are using the exact same CSRPNG (a cryptographically secure pseudorandom number generator 安全加密伪随机数生成器).

# When to use /dev/random vs /dev/urandom ？
Use **/dev/urandom** for most practical purposes.

Linux:
    Histrically, /dev/random and /dev/urandom were both introdyced at the same time.
    using /dev/urandom is preferred in the vast majority of cases.

In Summary:
    /dev/random and /dev/urandom Both are fed by the same CSPRNG to generate randomness
    /dev/random blocks when it runs out of entropy.
    The amount of entropy is conservatively estimated, but not counted.
    /dev/urandom will never block, reading from /dev/random can halt processes execution.

```

What does tl;dr mean?
---------------------
```
Tl;dr stands for "too long; didn't read."
```
