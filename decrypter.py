

file = open("decrypter.txt","w").close()
with open("encrypted_file.txt") as fileObj:
    for line in fileObj:
        for ch in line:
            m=ord(ch)
            m=m-3 %26
            #print(m)
            k = unichr(m)
            print k

            file = open("decrypter.txt","a")
            file.write(k)


