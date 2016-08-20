'''
Created on Aug 8, 2016

@author: xinshen
'''
def pkcs7(plaintext,size):
    padded = bytes(plaintext,"ascii")
    padding = bytes('\x04',"ascii")
    if (len(plaintext) != size):
        padded = padded + padding * (size - len(plaintext))
    return padded

if __name__ == "__main__":
    print(pkcs7("YELLOW SUBMARINE", 20))