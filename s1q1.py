'''
Created on Aug 3, 2016

@author: xinshen
'''

import binascii
def hex_to_base64(hex_data):
    to_bytes = bytes(hex_data,"ascii")
    base_2 = binascii.unhexlify(to_bytes)
    base_64 = binascii.b2a_base64(base_2)
    return base_64[:-1]
                               

plaintext = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
print(hex_to_base64(plaintext))


