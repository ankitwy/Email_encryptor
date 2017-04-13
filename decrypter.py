# -*- coding: utf-8 -*-
def Dec(key):
    key = key % 26
    file = open("decrypter.txt","w").close()
    with open("encrypted_file.txt") as fileObj:
        for line in fileObj:
            for ch in line:
                m=ord(ch)
                S = (m - key)
                k = unichr(S)
                file = open("decrypter.txt","a")
                file.write(str(k))

