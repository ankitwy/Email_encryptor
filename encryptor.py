# -*- coding: utf-8 -*-
import smtplib
def Enc(key):
    key = key % 26
    open("encrypted_file.txt",'w').close()
    with open("normal_text.txt") as fileObj:
        for line in fileObj:
            for ch in line:
                m=ord(ch)

                S= (m+key)
                file = open("encrypted_file.txt","a")
                file.write(str(unichr(S)))
                file.close()

def Send_ENC_email(email,password,to):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email,password)
    file = open("encrypted_file.txt","r")
    msg = file.read()
    server.sendmail(email,to, msg)
    server.quit()
