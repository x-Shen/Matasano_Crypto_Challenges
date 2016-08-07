'''
Created on Aug 4, 2016

@author: xinshen
'''

import binascii

character_score = {"a":8, "A":8, "b":1.5, "B":1.5, "c":3, "C":3, "d":4.2, "D":4.2, "e":13, "E":13, "f":2, "F":2, "g":2, "G":2, "h":6, "H":6, "i":7, "I":7, "j":0.1, 'J':0.1, "k":0.7, "K":0.7, "l":4, "L":4, "m":2.5, "M":2.5, "n":7, "N":7, "o":7.5, "O":7.5, "p":2, "P":2, "q":0.1, "Q":0.1, "r":6, "R":6, "s":6, "S":6, "t":9, "T":9, "u":3, "U":3, "v":1, "V":1, "w":2, "W":2, "x":0.1, "X":0.1, "y":2, "Y":2, "z":0.1, "Z":0.1}
char_list = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .'",?!'''


def inc_key(key):
    int_key=int(key,16)
    int_key=int_key+1
    hex_key=hex(int_key)[2:]
    return hex_key



def decrypt(cipher_txt,key):
    
    answer = ''
    xor = lambda x, y: int(x,16)^int(y,16)
    i=0
    while (i <len(cipher_txt)):
        new_num = hex(xor(cipher_txt[i:i+2],key))
        new_num = new_num[2:]
        if (len(new_num)==1):
            new_num = '0'+new_num
        answer+= new_num
        i+=2
    return answer

def calc_scores(b_string,character_score,char_list):
    string = str(b_string)
    score = 0
    for char in string:
        if char in character_score:
            score+=character_score[char]
        if (char not in char_list):
            score-=20
    return score

def get_result(cipher_txt,character_score):
    key = '00'
    all_decrypts = []
    for i in range(255):
        ans=decrypt(cipher_txt,key)
        plain_txt = binascii.unhexlify(ans)
        score = calc_scores(plain_txt,character_score,char_list)
        all_decrypts.append((plain_txt,score,i))
        key = inc_key(key)
    all_decrypts = sorted(all_decrypts,key = lambda tup: tup[1],reverse=True)
    return all_decrypts

f = open('q4data.txt', 'r')
data = f.readlines()
#print(data)
f.close()

result_list = []
for i in range(len(data)):
        result_list.append(get_result(data[i][:-2],character_score))

possible_decrypts = []        
for dec in result_list:
    if (dec[0][1] > 0):
        possible_decrypts.append(dec[0])
        #print(dec[0])       

possible_decrypts = sorted(possible_decrypts,key = lambda tup: tup[1], reverse = True)
print(possible_decrypts)