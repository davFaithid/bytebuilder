# ByteBuilder

This is a project I have dreamed about for years, and I hope to see it to completion.

I seek to bruteforce solve sha hashes so that files that may have once been lost can one day be recovered.

Similar to other bruteforce tools, this will take a long time to replicate a file, especially since I just have it randomize every byte instead of sort of sensible algorithm.

##First breakthrough
Coded python file able to write a file of random bytes to a specified size

Specified size is modifiable by args

should probably find a way to keep a log of the past hashes of test files to prevent repeats, although I fail to see how useful that would be as I would be copying the bytes as well as the hash, that would be a waste of space

what if I create a repository of all hashes encountered purely so file size is known outside of merely the hash... it's an idea but I don't have the resources to host and manage all of that

successfully passed sha256 and file size to write out a desired file

```
py -3 bb.py ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb 1
ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb

1

failure 13598656f10fa962b75f6c4587a61a067c14c1ef7dc9ca3703da76bae4c1beb1 1
failure 9d1e0e2d9459d06523ad13e28a4093c2316baafe7aec5b25f30eba2e113599c4 1
failure 13598656f10fa962b75f6c4587a61a067c14c1ef7dc9ca3703da76bae4c1beb1 1
failure a9f51566bd6705f7ea6ad54bb9deb449f795582d6529a0e22207b8981233ec58 1
failure 245843abef9e72e7efac30138a994bf6301e7e1d7d7042a33d42e863d2638811 1
failure 4d7b3ef7300acf70c892d8327db8272f54434adbc61a4e130a563cb59a0d0f47 1
failure 949f94d858ef6ad1333164d796a0d777fd82f9155ece7d6fad68c0b992f0e7af 1
failure 9d277175737fb50041e75f641acf94d10df9b9721db8fffe874ab57f8ffb062e 1
failure 2d3193691934124461809fb9bc7e671215099fc7d961bfbe31943d40d477c890 1
failure 4f362f9093bb8e7012f466224ff1237c0746d8c8f660b16699f5036ccba9c64a 1
failure bbf3f11cb5b43e700273a78d12de55e4a7eab741ed2abf13787a4d2dc832b8ec 1
failure 4f362f9093bb8e7012f466224ff1237c0746d8c8f660b16699f5036ccba9c64a 1
success
```
already seeing that it will repeat the same file over (`13598656f10fa962b75f6c4587a61a067c14c1ef7dc9ca3703da76bae4c1beb1`, `4f362f9093bb8e7012f466224ff1237c0746d8c8f660b16699f5036ccba9c64a`), if there is a way to minimize that I need to find it

Can I replicate a file by simply dumping the seed? That might solve the duplicate issue by making sure the seed stays unique