'''
Created on Aug 5, 2016

@author: xinshen
'''
import binascii
import s1q3
import s1q5


f = open('q6data.txt', 'rU')
data = f.read()
f.close()
data = binascii.a2b_base64(data)
#print(data)
#print(data)
def distance(b1, b2):
    #print(type(b1))
    xored = bytes([a^b for (a,b) in zip(b1,b2)])
    dis = 0
    for j in range(len(xored)):
        diff = 0
        for i in range(8):
            diff += (xored[j] >> i) & 1
        dis+=diff
        
    return dis


def block_generator(data,block_size):
    for start in range(0, len(data),block_size):
        yield data[start:start+block_size]

def get_blocks(data,key_size):
    blocks = []        
    for block in block_generator(data,key_size):
        #if (len(block)==key_size):
        blocks.append(block)
    return blocks


def average_distance(str,ks):
    blocks = get_blocks(str,ks)
    #print(blocks)
    pairs = zip(blocks,blocks[1:])
    total_dis = 0
    for b1,b2 in pairs:
        total_dis += distance(b1,b2)/ks
    #print(total_dis)
    if (len(blocks[1:])==0):
        return total_dis
    return total_dis/len(blocks[1:])
    
def get_key_length(data):
    key_length = []
    for i in range(2, 40):
        key_length.append((i,average_distance(data,i)))
   
    key_length.sort(key=lambda tup: tup[1])
    return key_length

print(get_key_length(data))

'''def transpose_blocks(blocks,block_size, pos):
    transposed = ''
    for block in blocks:
        if(len(block)==block_size):
            transposed+=block[pos]
    return transposed

def all_transpose(blocks, block_size):
    all_transpose = []
    for i in range(block_size):
        all_transpose.append(transpose_blocks(blocks,block_size,i))
    return all_transpose'''

n = 29
transposed = [data[i::n] for i in range(n)]
#print(transposed)

def decrypt(cipher_txt,key):
    key = key*len(cipher_txt)
    xored = bytes([x^y for x,y in zip(cipher_txt,key)])
    return str(xored)

def decrypt_all(cipher_txt,character_score,char_list):
    all_decrypts = []
    for i in range(255):
        key = bytes([i])
        de = decrypt(cipher_txt,key)
        all_decrypts.append((de,s1q3.calc_scores(de,character_score,char_list),i))
    all_decrypts = sorted(all_decrypts,key = lambda tup: tup[1],reverse=True)
    return all_decrypts

key_string = bytearray()
for chuck in transposed:
    key_string.append(decrypt_all(chuck,s1q3.character_score,s1q3.char_list)[0][2])
print(key_string)

def encrypt(key,plain_text):
    def key_generator(key):
        index = 0
        while True:
            yield ord(key[index%(len(key))])
            index+=1
    k = key_generator(key)
    xored = bytes([a^b for (a,b) in zip(plain_text,k)])
    return xored

decrypted = encrypt('Terminator X: Bring the noise',data)
print(decrypted)

    
        