'''
Created on Aug 3, 2016

@author: xinshen
'''
import binascii
cipher_txt = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

character_score = {"a":8, "A":8, "b":1.5, "B":1.5, "c":3, "C":3, "d":4.2, "D":4.2, "e":13, "E":13, "f":2, "F":2, "g":2, "G":2, "h":6, "H":6, "i":7, "I":7, "j":0.1, 'J':0.1, "k":0.7, "K":0.7, "l":4, "L":4, "m":2.5, "M":2.5, "n":7, "N":7, "o":7.5, "O":7.5, "p":2, "P":2, "q":0.1, "Q":0.1, "r":6, "R":6, "s":6, "S":6, "t":9, "T":9, "u":3, "U":3, "v":1, "V":1, "w":2, "W":2, "x":0.1, "X":0.1, "y":2, "Y":2, "z":0.1, "Z":0.1, " ":15}
char_list = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .'",?!'''

        
def decrypt(cipher_txt,key):
    cipher_txt = bytes.fromhex(cipher_txt)
    key = key*len(cipher_txt)
    xored = bytes([x^y for x,y in zip(cipher_txt,key)])
    return str(xored)

def calc_scores(b_string,character_score,char_list):
    score = 0
    for char in b_string:
        if char in character_score:
            score+=character_score[char]
        if (char not in char_list):
            score-=20
    return score  

def decrypt_all(cipher_txt,character_score,char_list):
    all_decrypts = []
    for i in range(255):
        key = bytes([i])
        de = decrypt(cipher_txt,key)
        all_decrypts.append((de,calc_scores(de,character_score,char_list),i))
    all_decrypts = sorted(all_decrypts,key = lambda tup: tup[1],reverse=True)
    return all_decrypts
        
      
if __name__ =="__main__":
    print(decrypt_all(cipher_txt,character_score,char_list)[0][0])
#print(bytes.fromhex('00'))