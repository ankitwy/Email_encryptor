


#E(x) = (x+n) % 26


open("encrypted_file.txt",'w').close()
with open("encryptor.txt") as fileObj:
    for line in fileObj:
        for ch in line:
            m=ord(ch)
            m=m+3 %26
            print(m)
            k = unichr(m)
            # print k

            file = open("encrypted_file.txt","a")
            file.write(k)
            # file.close()

import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("sender email", "password")


file = open("encrypted_file.txt","r")
msg = file.read()
server.sendmail("senders email", "recivers email", msg)
server.quit()

