import hashlib
from PIL import Image
import random
import sys
from mf import fingerprint
try:
    flag = sys.argv[1]
except IndexError:
    flag = "none" 
if flag == "--file":
    value = sys.argv[2]
    file = sys.argv[3]
    size = sys.argv[4]
    f = open(value, "r")
    hashh = fingerprint.sha256(f.read())
    print(hashh)
    image = fingerprint.fingerprint(hashh, int(size))
    image.save(file)
if flag == "--hash":
    value = sys.argv[2]
    file = sys.argv[3]
    size = sys.argv[4]
    image = fingerprint.fingerprint(value, int(size))
    image.save(file)
if flag == "--data":
    value = sys.argv[2]
    file = sys.argv[3]
    size = sys.argv[4]
    hashh = fingerprint.sha256(value)
    print(hashh)
    image = fingerprint.fingerprint(hashh, int(size))
    image.save(file)

if flag == "--help" or flag == "none":
    print(""" Fingerprint a Hash
        
    --help display this help message
    --file fingerprint a file (its hash)
    --data fingerprint data i.e 'Bill' (its hash)
    --hash fingerprint a hash (must be sha256)

    example : 
    --data "test" test.jpg 100
    * the file name and size require no flag
    * the image size is in pixel, note that all images are sqaures
    """)