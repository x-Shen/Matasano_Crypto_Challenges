'''
Created on Aug 7, 2016

@author: xinshen
'''
import binascii
from Crypto.Cipher import AES
from collections import Counter

file = open("q8data.txt",'rU')
data = file.readlines()
file.close()


def block_generator(data,block_size):
    for start in range(0, len(data),block_size):
        yield data[start:start+block_size]

def get_blocks(data,key_size):
    blocks = []        
    for block in block_generator(data,key_size):
        blocks.append(block)
    return blocks


for i in range(len(data)):
    b = get_blocks(data[i].strip(),16)
    cn = Counter(b)
    #print(i)
    if (cn.most_common()[0][1] > 1):
        print(i)
        print(data[i].strip())
        print(cn.most_common())

