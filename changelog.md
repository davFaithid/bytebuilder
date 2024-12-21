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

## Other hashes

SHA-1 and MD5 have been implemented. They work great so far.

```
py -3 bb.py -bb 0cc175b9c0f1b6a831c399e269772661 -ht md5 -fs 1 -o "its the letter a.txt"

MD5 Hash Selected

***************************
# ByteBuilder: reconstructing files from a cryptographic hash
# Author: davFaithid
# Version 3
***************************


failure 0c78aef83f66abc1fa1e8477f296d394 1 0
failure b15835f133ff2e27c7cb28117bfae8f4 1 1
failure 97a6dd4c45b23db9c5d603ce161b8cab 1 2
failure 524a50782178998021a88b8cd4c8dcd8 1 3
failure 524a50782178998021a88b8cd4c8dcd8 1 4
failure dc5eccdcf293db4cfae59a97c28e7596 1 5
failure adf8db9586d0065d236cb8bf50bf2e5f 1 6
failure e1e1d3d40573127e9ee0480caf1283d6 1 7
failure 853ae90f0351324bd73ea615e6487517 1 8
failure 9e3669d19b675bd57058fd4664205d2a 1 9
failure 685d590a89f352d10644dd985da2a9a1 1 10
failure 03c7c0ace395d80182db07ae2c30f034 1 11
failure 415290769594460e2e485922904f345d 1 12
failure 9d5ed678fe57bcca610140957afab571 1 13
failure f616c83f2f0f188265c7004d81d45723 1 14
failure 1932a6849c6f575ca360266cc3f9a466 1 15
failure 28d397e87306b8631f3ed80d858d35f0 1 16
failure a03920e5994202f77b9c713941b5e055 1 17
failure 5058f1af8388633f609cadb75a75dc9d 1 18
failure 3beb9cf0eab8cbf2215990b4a6bdc271 1 19
failure 9d5a273e0fb6aebca825009ee2363e2c 1 20
failure 3389dae361af79b04c9c8e7057f60cc6 1 21
failure ade7a0dcf4ddc0673ed48b70a4a340d6 1 22
failure 167b86f21df376c96f10a0615b14200b 1 23
failure da630c00d04be7f24cdaaacd01cf2e30 1 24
failure 833344d5e1432da82ef02e1301477ce8 1 25
failure d6e4a86e03b9b1f0bbf5d9582a4ae8ef 1 26
failure 6067a176e5ed08f37f90537b9dbe76a5 1 27
failure 0398b4090f24adbccc218219f5746b10 1 28
failure 97775ba09eac63b5dcc98a94b2f779b9 1 29
failure 1d948537445132ebf746bd33d5494b70 1 30
failure 8666683506aacd900bbd5a74ac4edf68 1 31
failure ffe51d3e7d8297237588704eeddc6ab2 1 32
failure 685d590a89f352d10644dd985da2a9a1 1 33
failure 8fec378760f1e7e708e9f57edafc28fc 1 34
failure 97775ba09eac63b5dcc98a94b2f779b9 1 35
failure b9ece18c950afbfa6b0fdbfa4ff731d3 1 36
failure 02cb3522b35e58097e5fc3e9e093d9b6 1 37
failure d527ca074d412d9d0ffc844872c4603c 1 38
failure e4da3b7fbbce2345d7772b0674a318d5 1 39
failure 7b774effe4a349c6dd82ad4f4f21d34c 1 40
success 0cc175b9c0f1b6a831c399e269772661 1 41
```

```
py -3 bb.py -bb 86f7e437faa5a7fce15d1ddcb9eaeaea377667b8 -ht sha1 -fs 1 -o "its the letter a.txt"

SHA1 Hash Selected

***************************
# ByteBuilder: reconstructing files from a cryptographic hash
# Author: davFaithid
# Version 3
***************************


failure 1dcf0ec2351966fc2b0babee787f535a2683f130 1 0
failure 2ace62c1befa19e3ea37dd52be9f6d508c5163e6 1 1
failure b48f491783e98de10682f2d4455dfce5bdc3c233 1 2
failure c4dd3c8cdd8d7c95603dd67f1cd873d5f9148b29 1 3
failure c4dd3c8cdd8d7c95603dd67f1cd873d5f9148b29 1 4
failure f195c020a28dfc5f2fb6af256b524ddcd93756ed 1 5
failure 12bdd00fd4038756cbcf8ecdad1b0cd862603cd8 1 6
failure 06576556d1ad802f247cad11ae748be47b70cd9c 1 7
failure 05a79f06cf3f67f726dae68d18a2290f6c9a50c9 1 8
failure 7a38d8cbd20d9932ba948efaa364bb62651d5ad4 1 9
failure e67cb59b3168e12ea787b84372ab07560f8304d5 1 10
failure a0f1490a20d0211c997b44bc357e1972deab8ae3 1 11
failure 95cb0bfd2977c761298d9624e4b4d4c72a39974a 1 12
failure ae4f281df5a5d0ff3cad6371f76d5c29b6d953ec 1 13
failure 27f57cb359a8f86acf4af811c47a6380b4bb4209 1 14
failure 73b74736664ad85828ce1be2e29fb4a68d24402b 1 15
failure 08534f33c201a45017b502e90a800f1b708ebcb3 1 16
failure 8768a53e1d4c182907306300f9ca90cfd8018383 1 17
failure 3a52ce780950d4d969792a2559cd519d7ee8c727 1 18
failure 241cbd6dfb6e53c43c73b62f9384359091dcbf56 1 19
failure 132ccf0bbeffce4af8e88c1c38cb67d38432976f 1 20
failure df58248c414f342c81e056b40bee12d17a08bf61 1 21
failure c66be7210915f39e91456fc2eac9441012a0a3ea 1 22
failure 0ad052dd9f32405521e43c6ebdc52f5a025493b2 1 23
failure 45a65193e30784b0124f4fed659eb7e46552c2d0 1 24
failure 7e15bb5c01e7dd56499e37c634cf791d3a519aee 1 25
failure d3fe83b8d87ccda2bbca5e81ce3ab1a1400bfbe8 1 26
failure 4df7138b341559a90fcf19aac099bfa6cc432cb2 1 27
failure b830c46d24068069f0a43687826f355b21fdb941 1 28
failure 090cbc46c3a13cd05fceb2fe55cccaab870d6795 1 29
failure c4488af0c158e8c2832cb927cfb3ce534104cd1e 1 30
failure 9842926af7ca0a8cca12604f945414f07b01e13d 1 31
failure 5a8ca84c7d4d9b055f05c55b1f707f223979d387 1 32
failure e67cb59b3168e12ea787b84372ab07560f8304d5 1 33
failure ca632d28f91c1b8d638df71525fe22fd2473af10 1 34
failure 090cbc46c3a13cd05fceb2fe55cccaab870d6795 1 35
failure c2c53d66948214258a26ca9ca845d7ac0c17f8e7 1 36
failure d8fc60ccdd8f555c1858b9f0820f263e3d2b58ec 1 37
failure 121a9af889bd4ca2266be5a4f680d3bead8d02d6 1 38
failure ac3478d69a3c81fa62e60f5c3696165a4e5e6ac4 1 39
failure 51e69892ab49df85c6230ccc57f8e1d1606caccc 1 40
success 86f7e437faa5a7fce15d1ddcb9eaeaea377667b8 1 41
```

I have identified a bug where the program will just freeze for no reason when trying to generate excessive big files. Doesn't matter the hash, it just won't work. The only arbitrary file size I've tried that's resulted in this is ``8521449472``, although I suspect other multi-gigabyte files are the same.

Definitely need to fix.