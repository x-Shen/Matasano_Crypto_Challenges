'''
Created on Aug 5, 2016

@author: xinshen
'''
import binascii



def encrypt(key,plain_text):
    def key_generator(key):
        index = 0
        while True:
            yield ord(key[index%(len(key))])
            index+=1
    plain_text = bytes(plain_text,"ascii")
    k = key_generator(key)
    xored = bytes([a^b for (a,b) in zip(plain_text,k)])
    return xored
    


    
if __name__ == "__main__":
    key = "ICE"
    plain_text = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    print(binascii.hexlify(encrypt(key,plain_text)))
    