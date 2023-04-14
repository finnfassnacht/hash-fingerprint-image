import hashlib
from PIL import Image
import random
class fingerprint:
    def converttonum(hashlist):
        colors = []
        for el in hashlist:
            in4 = []
            for yy in list(el):
                if yy.isnumeric():
                    value = int(yy)+1*10
                    in4.append(value)
                else:
                    if yy == "a":
                        value = 10+1*10
                        in4.append(value)
                    if yy == "b":
                        value = 11+1*10
                        in4.append(value)
                    if yy == "c":
                        value = 12+1*10
                        in4.append(value)
                    if yy == "d":
                        value = 13+1*10
                        in4.append(value)
                    if yy == "e":
                        value = 14+1*10
                        in4.append(value)
                    if yy == "f":
                        value = 15+1*10
                        in4.append(value)
            colors.append(in4)
        return colors

    def sha256(data):
        result = hashlib.sha256(data.encode())
        return result.hexdigest()

    def splithash(hashh):
        splithash = []
        for ii in range(16):
            ii += 1
            x = ii*4
            splithash.append(hashh[x-4:x])
        return splithash

    def fingerprint(hashh):
        hashlist = (fingerprint.splithash(hashh))
        sums = fingerprint.converttonum(hashlist)

        img = Image.new("RGB", (400, 400))
        x = 0
        y = 0
        ni = 0
        for i2 in range(4):

            for i in range(4):
                arr = (sums[i+ni])
                mas = arr[0]
                color = (arr[1]*12, arr[2]*12, arr[3]*12)
                lay = Image.new("RGB", ((mas)*4, (mas)*4), color)
                img.paste(lay, (0+x, 0+y))
                x += 100
            x = 0
            ni += 4
            y += 100
        return img
