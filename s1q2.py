'''
Created on Aug 3, 2016

@author: xinshen
'''
import binascii


s1 = '1c0111001f010100061a024b53535009181c'
s2 = '686974207468652062756c6c277320657965'


def xor_hex_values(value1, value2):
    vv1 = bytes.fromhex(s1)
    vv2 = bytes.fromhex(s2)
    xored = bytes([x^y for x, y in zip(vv1,vv2)])
    return binascii.hexlify(xored)


print(xor_hex_values(s1,s2))

