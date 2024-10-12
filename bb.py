# ByteBuilder/SeedSprout: reconstructing files from a cryptographic hash or seed
# Author: davFaithid
# Version 3

from io import BytesIO
import os, sys
import traceback
from random import randbytes
xrange = range

import argparse
parser = argparse.ArgumentParser()

#-bb ByteBuilder -ss SeedSprout -f File
parser.add_argument("-bb", "--bytebuilder", dest = "bb", help="Build file from hash using ByteBuilder:    -bb sha256 -fs filesize -o filename")
parser.add_argument("-ss", "--seedsprout", dest = "ss",  help="Build file from seed using SeedSprout:     -ss seed -fs filesize -o filename")
parser.add_argument("-i", "--infile", dest = "i",         help="Build file from SeedSprout container file: -i filename")
parser.add_argument("-fs", "--size", dest = "fs")
parser.add_argument("-o", "--outfile", dest = "o")

args = parser.parse_args()

# Eventually I'm going to add one to state what type of hash ByteBuilder will be using

import hashlib
import random

gl = 0
def randBytes(size, seed):
    random.seed(seed)
    global gl
    nr = bytearray(random.getrandbits(8) for _ in xrange(size))
    gl = nr
    return nr

def sha256sum(filename):
    h  = hashlib.sha256()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        for n in iter(lambda : f.readinto(mv), 0):
            h.update(mv[:n])
    return h.hexdigest()

def writeout(seed,maxsize,filename):
    try: 
        write_byte = randBytes(int(maxsize),seed)
        with open(filename, "wb") as f:
                    # max file size in bytes
            while (os.stat(filename).st_size < int(maxsize)):
                f.write(write_byte)
                if f.tell() == int(maxsize):    # f.tell() gives byte offset, no need to worry about multiwide chars
                    break
#                   sys.exit()
            f.close()
            
        return sha256sum(filename)
    except:
        traceback.print_exc()
        import subprocess, time
        subprocess.check_call(["attrib", "-H", filename])
        print("pausing for cooldown")
        time.sleep(5)

def ByteBuilder(target,maxsize,filename):
    print("""
***************************
# ByteBuilder: reconstructing files from a cryptographic hash
# Author: davFaithid
# Version 3
***************************
    """,'\n')
    seed = 0
    #print(target,'\n')
    #print(maxsize,'\n')
    while (str(writeout(seed,maxsize,filename)) != str(target)):
        print("failure", sha256sum(filename), os.stat(filename).st_size,seed)
        seed += 1
        writeout(seed,maxsize,filename)
        if (sha256sum(filename) == target):
            print("success", sha256sum(filename), os.stat(filename).st_size,seed,'\n')
            break
            sys.exit()
            
def SeedSprout(seed,maxsize,filename):
    print("""
***************************
# SeedSprout: reconstructing files from a ByteBuilder seed
# Author: davFaithid
# Version 3
***************************
""",'\n')
    print("SHA256: ",writeout(seed,maxsize,filename),'\n')
    sys.exit()
    
def SeedSprouti(infile):
    print("""
***************************
# SeedSprouti: reconstructing files from a SeedSprout container file
# Author: davFaithid
# Version 3
***************************
""",'\n')
    fileopen = open(infile, "r")
    fileread = fileopen.read()
    fileread = fileread.split("/")
    #print(fileread)
    fileopen.close()
    target = fileread[1]
    maxsize = int(fileread[2])
    seed = int(fileread[3])
    filename = str(fileread[4])
    #print(target,maxsize,seed)
    if sha256sum(filename) == target:
        print("success", sha256sum(filename),'\n')
    else:
        print("failure", sha256sum(filename),'\n')    
            
def main():
    if sys.argv[1] == '-bb':
        #print("bb",args.bb,args.fs,args.o)
        ByteBuilder(args.bb,args.fs,args.o)
    if sys.argv[1] == '-ss':
        #print("ss",int(args.ss),args.fs,args.o)
        SeedSprout(int(args.ss),args.fs,args.o)
    if sys.argv[1] == '-i':
        #print("i",args.i)
        SeedSprouti(args.i)
    if sys.argv[1] == '--bytebuilder':
        #print("bb",args.bb,args.fs,args.o)
        ByteBuilder(args.bb,args.fs,args.o)
    if sys.argv[1] == '--seedsprout':
        #print("ss",int(args.ss),args.fs,args.o)
        SeedSprout(int(args.ss),args.fs,args.o)
    if sys.argv[1] == '--infile':
        #print("i",args.i)
        SeedSprouti(args.i)

main()