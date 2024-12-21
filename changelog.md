# Changelog

## First breakthrough

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

## Second breakthrough

Five months later and I finally revisited the project, I was able to easily implement seeding and just increment the seed each iteration. This prevents duplicate hashes from being formed and is a much better system than randomly generating bytes and hoping for the best.

Output now includes the current seed that is being used, which I think is very useful and can be used to easily recreate the file from just the seed and the file size. I have tested that and it works beautifully.

For example the seed for ``ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb`` is 41 with a size of 1

Could I shorten the seeds by using hexadecimal? Yes. Am I going to? Probably not.

```
py -3 bb.py ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb 1
ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb

1

failure af193a8cdcd0e3fb39e71147e59efa5cad40763d2611f5beff34a274f514362f 1 0
failure 8a331fdde7032f33a71e1b2e257d80166e348e00fcb17914f48bdb57a1c63007 1 1
failure 2017ff3461395672aa0aa4f64894fd2f95a4b120e2690e8951656d79adc2eed2 1 2
failure dabd3aff769f07eb2965401eb029974ebba3407afd02b26ddb564ea5f8efae72 1 3
failure dabd3aff769f07eb2965401eb029974ebba3407afd02b26ddb564ea5f8efae72 1 4
failure 1f184f101c67d585ba00d24cfde36863f747fbab9e84af7760ec771e9b36ca51 1 5
failure 383e5d7d58caa41ce723cf16af471b38f6ee9065c032d07fa6bef1678cb72f1d 1 6
failure 8c2574892063f995fdf756bce07f46c1a5193e54cd52837ed91e32008ccf41ac 1 7
failure e7ac0786668e0ff0f02b62bd04f45ff636fd82db63b1104601c975dc005f3a67 1 8
failure 4c94485e0c21ae6c41ce1dfe7b6bfaceea5ab68e40a2476f50208e526f506080 1 9
failure 956062137518b270d730d4753000896de17c100a42f9e24f5acee2faa75d5fdd 1 10
failure 043a718774c572bd8a25adbeb1bfcd5c0256ae11cecf9f9c3f925d0e52beaf89 1 11
failure a1fce4363854ff888cff4b8e7875d600c2682390412a8cf79b37d0b11148b0fa 1 12
failure df7e70e5021544f4834bbee64a9e3789febc4be81470df629cad6ddb03320a5c 1 13
failure 77adfc95029e73b173f60e556f915b0cd8850848111358b1c370fb7c154e61fd 1 14
failure 50868f20258bbc9cce0da2719e8654c108733dd2f663b8737c574ec0ead93eb3 1 15
failure a9253dc8529dd214e5f22397888e78d3390daa47593e26f68c18f97fd7a3876b 1 16
failure c00e7f889cfc9216ec818bf2e1682fc6af0d89939c91776669478caf27c9727c 1 17
failure cdb4ee2aea69cc6a83331bbe96dc2caa9a299d21329efb0336fc02a82e1839a8 1 18
failure 22adaf058a2cb668b15cb4c1f30e7cc720bbe38c146544169db35fbf630389c4 1 19
failure d0752b60adb148ca0b3b4d2591874e2dabd346373e731c27463d65b449cc234c 1 20
failure 684888c0ebb17f374298b65ee2807526c066094c701bcc7ebbe1c1095f494fc1 1 21
failure 27abdeddfe8503496adeb623466caa47da5f63abd2bc6fa19f6cfcb73ecfed70 1 22
failure 45f83d17e10b34fca01eb8f4454dac34a777d9404a464e732cf4abf2c0da94c4 1 23
failure ca41841c5c98e34f4a3ae83d9220940395301a9616f69d6672b04ea322f28eb0 1 24
failure 8d33f520a3c4cef80d2453aef81b612bfe1cb44c8b2025630ad38662763f13d3 1 25
failure b12dc850a3b0a3b79fc2255e175241ce20489fe45df93ff35c42c6c348df4fbf 1 26
failure fe1dcd3abfcd6b1655a026e60a05d03a7f71e4b6070f36e6c7e9c4b6f3d3bf1b 1 27
failure bd4fc42a21f1f860a1030e6eba23d53ecab71bd19297ab6c074381d4ecee0018 1 28
failure 9defb0a9e163278be0e05aa01b312ec78cfa3726869503385e76e3a4b7950648 1 29
failure 2d3193691934124461809fb9bc7e671215099fc7d961bfbe31943d40d477c890 1 30
failure 084fed08b978af4d7d196a7446a86b58009e636b611db16211b65a9aadff29c5 1 31
failure ab897fbdedfa502b2d839b6a56100887dccdc507555c282e59589e06300a62e2 1 32
failure 956062137518b270d730d4753000896de17c100a42f9e24f5acee2faa75d5fdd 1 33
failure 4bfa260a661d68110a7a0a45264d2d43af9727de925cc2e09fb687b3651efe9d 1 34
failure 9defb0a9e163278be0e05aa01b312ec78cfa3726869503385e76e3a4b7950648 1 35
failure e632b7095b0bf32c260fa4c539e9fd7b852d0de454e9be26f24d0d6f91d069d3 1 36
failure 19753a9b7681b36104c1f79dfc8a6a1eccc088b8c7d2903a446d81694d2fb3a9 1 37
failure 6d90fbacc073ee0b4c43f3a3291cecda33764f6d66d14224ad60f471f2c8334b 1 38
failure ef2d127de37b942baad06145e54b0c619a1f22327b2ebbcfbec78f5564afe39d 1 39
failure 0bfe935e70c321c7ca3afc75ce0d0ca2f98b5422e008bb31c00c6d7f1f1c0ad6 1 40
success ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb 1 41
```

Still only have sha256 implemented, but from this point it's only a matter of time before I implement other hashes.

Should also note that for obvious reasons generating large files from a hash is going to still take forever but this reduces the time overall for bigger files by eliminating duplicates.

Working on SeedSprout (``ss.py``) which is dedicated to creating a file from a seed, working out some kinks some right now (the seed produced by bb.py is different than what ss.py uses, 0 on SeedSprout is 16 on ByteBuilder and 1 on SeedSprout is 293 and 2 is 209, really wish I knew why it's doing that)

## Third breakthrough

The fix for SeedSprout was actually insultingly easy. I was struck today that maybe the inputted seed was not being treated as an int and turns out that was right. Now SeedSprout is fully operational.

```
py -3 ss.py 41 1
41

1

ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb
```

My next idea to implement is file headers and whatever the equivalent is for the ending of a file (file footers?) for ByteBuilder, that way certain file types will generate faster. 

Maybe I'll even make a file container for SeedSprout with a seed, a hash, and a file size for easy sharing of files for the command-line averse. 

## Combining

I created a Python script that can generate a file from a container with the hash of the file to verify the file, the size of the file, the seed that SeedSprout will use, and the file name.

Format:  ``ss#!/sha256/size/seed/filename``
Example: ``ss#!/ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb/1/41/its the letter a.txt``

After that I decided to combine all three into one script and just switch between the three through flags in the arguments. Easy implementation.

Now that it's all in one file, ``-bb`` invokes ByteBuilder, ``-ss`` invokes SeedSprout, and ``-i`` inputs a container file. I can probably make this even simpler by making a GUI.

Oh also now file size and file name are arguments called by flags, so don't forget the flags when using it. (``-fs`` filesize, ``-o`` filename)

## File Header and Start Seed

Obviously files generated using a file header cannot have usable seeds without that header. Currently I have not set up a way in the container file to handle headers or footers. I wonder if its possible to reverse engineer the seed for the file with the header without regenerating the entire file.

The analyzing files feature (``-a``) returns the SHA-256 hash and file size of a given file. 

I am planning on implementing a feature that allows users to analyze files, generate their ByteBuilder seed, and upload their hash, seed, and size to a public repo, effectively acting as a method of cloud storage for quick regeneration with SeedSprout. Additionally during ByteBuilder generation, all failed hashes and seeds will be uploaded in this mode as well. If ByteBuilder has access to an internet connection and the repo is available, then the program will check the database before beginning generation just in case it can invoke SeedSprout instead to save time.

I am curious about when, if ever, a duplicate hash may arise, and how to handle that. Erroneous hashes might also be added to the repo if down the line SHA can be spoofed like CRC has been in the past, which will effectively render a given file useless for hash verification. Due to SHA and CRC functioning differently I doubt that this will happen if at all, but it is a possible worst case scenario concern. To combat duplicate hashes, the repo will report any duplicate hashes and their size so they can coexist in the repo but exist at different file sizes. I wonder what format I should use for this repo, CSV? Maybe JSON like ``{"ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb|1":"41"}`` or something.

Also to be clear this feature is optional and needs to be turned on to upload these hashes to the database. I wonder what I should call the database. Hashiverse? Hashingbase? Hashipedia? I'll probably come up with something better when I actually set this up.

So I figured about headers, a seed will produce the same bytes at any given size. So we'd just narrow down the seeds that produce those headers first before generating the rest of the file. That speeds up generation by a lot, and if I can have the two running concurrently then it can figure out the seeds that produce the hashes as the files are generated!

The header implementation is actually really awesome, I had a file generating for three days and stopped it at seed 228603, with the header implemented the seed surpassed it in about three minutes. 

Header mode also has a "no seed" option which iterates slow and cannot produce a usable seed for SeedSprout but guarantees that the generated file starts with the header for every "seed".

```
py -3 bb.py -bb ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb -fs 1 -o a -st 40

***************************
# ByteBuilder: reconstructing files from a cryptographic hash
# Author: davFaithid
# Version 3
***************************


failure 0bfe935e70c321c7ca3afc75ce0d0ca2f98b5422e008bb31c00c6d7f1f1c0ad6 1 40
success ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb 1 41
```

## Actually making the commit

Hello! It is currently December 21, 2024. I coded in the whole file header and start seed portions pretty much immediately after my last commit (10/12/24) and the last time I touched the code was October 19, 2024. But um yeah, forgot to commit any of that, my bad.

Have not implemented the database thing yet