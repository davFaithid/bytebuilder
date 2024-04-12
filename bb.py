from io import BytesIO
import os, sys

#Other ideas:
from random import randbytes

#import secrets
#b"\x00" + secrets.token_bytes(4) + b"\x00"

#bytearray(random.getrandbits(8) for _ in xrange(size))

#set up args; bb.py hash filesize

if (len(sys.argv) < 3):
    print("too few args, try again")
    sys.exit()

target = sys.argv[1]
maxsize = sys.argv[2]

print(target,'\n')
print(maxsize,'\n')
  
import hashlib

def sha256sum(filename):
    h  = hashlib.sha256()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        for n in iter(lambda : f.readinto(mv), 0):
            h.update(mv[:n])
    return h.hexdigest()

def writeout():
    try: 
        write_byte = BytesIO(randbytes(int(maxsize)))
        with open("test.bin", "wb") as f:
                    # max file size in bytes
            while (os.stat("test.bin").st_size < int(maxsize)):
                f.write(write_byte.getbuffer())
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

while (str(writeout()) != str(target)):
    print("failure", sha256sum("test.bin"), os.stat("test.bin").st_size)
    writeout()
    if (sha256sum("test.bin") == target):
        print("success")
        break
        sys.exit()