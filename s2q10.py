'''
Created on Aug 19, 2016

@author: xinshen
'''

from Crypto.Cipher import AES
import base64
f = open('q10data.txt',"rU")
data = f.read()


def CBC_mode():
    encryption_suite = AES.new('YELLOW SUBMARINE', AES.MODE_ECB)
    plain_text = encryption_suite.encrypt(data)

