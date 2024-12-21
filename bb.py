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
parser.add_argument("-a", dest = "a",         help="Prints hash and file size, perfect for batch commands for folders")
parser.add_argument("-fs", "--size", dest = "fs")
parser.add_argument("-o", "--outfile", dest = "o")
parser.add_argument("-bh", dest = "bh")
parser.add_argument("-st", dest = "st")
parser.add_argument("-ns", dest = "ns")

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

def writeout(seed,maxsize,filename,startbyte=0):
    try: 
        if (startbyte==0):
            write_byte = randBytes(int(maxsize),seed)
            with open(filename, "wb") as f:
                    # max file size in bytes
                while (os.stat(filename).st_size < int(maxsize)):
                    f.write(write_byte)
                    if f.tell() == int(maxsize):    # f.tell() gives byte offset, no need to worry about multiwide chars
                        break
#                   sys.exit()
                f.close()
        else:
            with open(filename, "wb") as f:
                write_byte = bytes.fromhex(startbyte)
                while (os.stat(filename).st_size < int(len(startbyte)/2)):
                    f.write(write_byte)
                    if f.tell() == int(len(startbyte)/2):    # f.tell() gives byte offset, no need to worry about multiwide chars
                        break
#                       sys.exit()
                f.close()
            write_byte = randBytes(int(maxsize),seed)
            with open(filename, "ab") as f:
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

def ByteBuilder(target,maxsize,filename,start=0):
    print("""
***************************
# ByteBuilder: reconstructing files from a cryptographic hash
# Author: davFaithid
# Version 3
***************************
    """,'\n')
    seed = 0 + int(start)
    while (str(writeout(seed,maxsize,filename)) != str(target)):
        print("failure", sha256sum(filename), os.stat(filename).st_size,seed)
        seed += 1
        writeout(seed,maxsize,filename)
        if (sha256sum(filename) == target):
            print("success", sha256sum(filename), os.stat(filename).st_size,seed,'\n')
            break
            sys.exit()
     
def Header(target,seed,header):
    run = True
    while (run == True):
    #while (str(sha256sum("header")) != str(sha256sum("header2"))):
            writeout(seed,int(len(header)/2),"header")
            print("failure",seed,end='\r')
            seed += 1
            if (str(sha256sum("header")) == str(sha256sum("header2"))):
                print("header found at seed", seed,'\n')
                #print(type(seed))
                run = False
    return seed
     
def ByteBuilderh(target,maxsize,filename,header,start=0,noseed=False):
    print("""
***************************
# ByteBuilder: reconstructing files from a cryptographic hash
# Author: davFaithid
# Version 3
***************************
    """,'\n')
    seed = 0 + int(start)
    #try: 
    print("noseed:",bool(noseed))
    if (bool(noseed)==False):
        write_byte = bytes.fromhex(header)
        with open("header2", "wb") as f:
                    # max file size in bytes
            while (os.stat("header2").st_size < int(len(header))):
                f.write(write_byte)
                if f.tell() == int(len(header)/2):    # f.tell() gives byte offset, no need to worry about multiwide chars
                    break
#                   sys.exit()
            f.close()
        print(str(sha256sum("header2")))
        print(int(len(header)/2))
        writeout(seed,int(len(header)/2),"header")
        while (str(writeout(seed,maxsize,filename)) != str(target)):
            y=Header(target,seed,header)
            #print(type(y))
            try:
                seed = int(y)
                #print(seed)
                #print(writeout(seed,maxsize,filename),seed)
            except TypeError:
                y=Header(target,seed,header)
                #print(y)
            print("testing",writeout(seed,maxsize,filename), os.stat(filename).st_size,seed)
            if (sha256sum(filename) == target):
                print("success", sha256sum(filename), os.stat(filename).st_size,seed,'\n')
                break
                sys.exit()
            else:
                #print("failure", sha256sum(filename), os.stat(filename).st_size,seed,'\n')
                print("failure",seed)
                seed += 1
                #seed=Header(target,seed,header)
                pass
    else:
        while (str(writeout(seed,maxsize,filename)) != str(target)):
            print("testing",writeout(seed,(int(maxsize)-int(len(header)/2)),filename,header), os.stat(filename).st_size,seed)
            if (sha256sum(filename) == target):
                print("success", sha256sum(filename), os.stat(filename).st_size,seed,'\n')
                break
                sys.exit()
            else:
                #print("failure", sha256sum(filename), os.stat(filename).st_size,seed,'\n')
                print("failure",seed)
                seed += 1
                #seed=Header(target,seed,header)
                pass

def Analyze(filename):
    print(sha256sum(filename), os.stat(filename).st_size,'\n')
        
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
        if (args.st):
            ByteBuilder(args.bb,args.fs,args.o,args.st)
        else:
            ByteBuilder(args.bb,args.fs,args.o)
    if sys.argv[1] == '-ss':
        #print("ss",int(args.ss),args.fs,args.o)
        SeedSprout(int(args.ss),args.fs,args.o)
    if sys.argv[1] == '-i':
        #print("i",args.i)
        SeedSprouti(args.i)
    if sys.argv[1] == '-a':
        Analyze(args.a)
    if sys.argv[1] == '-bh':
        #print("bb",args.bb,args.fs,args.o)
        if (args.st):
            if (args.ns):
                #print(args.ns,bool(args.ns))
                ByteBuilderh(args.bb,args.fs,args.o,args.bh,start=int(args.st),noseed=bool(args.ns))
            else:
                ByteBuilderh(args.bb,args.fs,args.o,args.bh,args.st)
        elif (args.ns):
            #print(args.ns,bool(args.ns))
            if (args.st):
                #print(args.ns,bool(args.ns))
                ByteBuilderh(args.bb,args.fs,args.o,args.bh,start=int(args.st),noseed=bool(args.ns))
            else:
                ByteBuilderh(args.bb,args.fs,args.o,args.bh,noseed=bool(args.ns))
            
        else:
            ByteBuilderh(args.bb,args.fs,args.o,args.bh)
    if sys.argv[1] == '--bytebuilder':
        #print("bb",args.bb,args.fs,args.o)
        if (args.st):
            ByteBuilder(args.bb,args.fs,args.o,args.st)
        else:
            ByteBuilder(args.bb,args.fs,args.o)
    if sys.argv[1] == '--seedsprout':
        #print("ss",int(args.ss),args.fs,args.o)
        SeedSprout(int(args.ss),args.fs,args.o)
    if sys.argv[1] == '--infile':
        #print("i",args.i)
        SeedSprouti(args.i)

main()