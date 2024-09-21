# ByteBuilder: reconstructing files from a cryptographic hash
# Author: davFaithid
# Version 2

from io import BytesIO
import os, sys

from random import randbytes
xrange = range

if (len(sys.argv) < 3):
    print("too few args, try again")
    sys.exit()

seed = 0
maxsize = sys.argv[2]
target = sys.argv[1]

print(target,'\n')
print(maxsize,'\n')
  
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

def writeout(seed):
    try: 
        write_byte = randBytes(int(maxsize),seed)
        with open("test.bin", "wb") as f:
                    # max file size in bytes
            while (os.stat("test.bin").st_size < int(maxsize)):
                f.write(write_byte)
                if f.tell() == int(maxsize):    # f.tell() gives byte offset, no need to worry about multiwide chars
                    break
#                   sys.exit()
            f.close()
            return sha256sum("test.bin")
    except:
        import subprocess, time
        subprocess.check_call(["attrib", "-H", "test.bin"])
        print("pausing for cooldown")
        time.sleep(5)

while (str(writeout(seed)) != str(target)):
    print("failure", sha256sum("test.bin"), os.stat("test.bin").st_size,seed)
    seed += 1
    writeout(seed)
    if (sha256sum("test.bin") == target):
        print("success", sha256sum("test.bin"), os.stat("test.bin").st_size,seed)
        break
        sys.exit()