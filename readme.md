# ByteBuilder

This is a project I have dreamed about for years, and I hope to see it to completion.

I seek to bruteforce solve sha hashes so that files that may have once been lost can one day be recovered.

Similar to other bruteforce tools, this will take a long time to replicate a file, especially since I just have it randomize every byte instead of sort of sensible algorithm.

## How to use

Currently ByteBuilder is CLI only, but if you are command-line averse do plan on building a GUI for it. ByteBuilder also currently only features SHA-256 hash building, but other hashes will be implemented.

ByteBuilder is comprised of three modules: ByteBuilder, the main module which builds files from hashes, SeedSprout, which builds files from ByteBuilder seeds, and SeedSprouti, the module which builds from a container file. The i doesn't stand for anything I just wanted to reference the Nintendo DSi.

Currently the following arguments must be present first before the file size and file name can be specified:

```
arguments:
  -bb, --bytebuilder
                        Build file from hash using ByteBuilder: -bb sha256 -fs filesize -o filename
  -ss, --seedsprout
                        Build file from seed using SeedSprout: -ss seed -fs filesize -o filename
  -i, --infile    
						Build file from SeedSprout container file: -i filename
```

### Examples

The following commands all output a lowercase letter ``a`` to the file ``its the letter a.txt``:

```
py -3 bb.py -bb ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb -fs 1 -o "its the letter a.txt"

***************************
# ByteBuilder: reconstructing files from a cryptographic hash
# Author: davFaithid
# Version 3
***************************


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

```
py -3 bb.py -ss 41 -fs 1 -o "its the letter a.txt"

***************************
# SeedSprout: reconstructing files from a ByteBuilder seed
# Author: davFaithid
# Version 3
***************************


SHA256:  ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb
```

```
py -3 bb.py -i container.ss

***************************
# SeedSprouti: reconstructing files from a SeedSprout container file
# Author: davFaithid
# Version 3
***************************


success ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb
```

## To-do

- [ ] Build a GUI
- [ ] Implement hashes other than SHA-256
- [ ] Implement file header/footer writing to accelerate ByteBuilder generation of files of certain file types