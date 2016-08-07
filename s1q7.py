from Crypto.Cipher import AES
import base64
file = open("q7data.txt")
data = file.read()
file.close()
# Encryption
data = base64.b64decode(data)
decryption_suite = AES.new('YELLOW SUBMARINE', AES.MODE_ECB)

plain_text = decryption_suite.decrypt(data)
print(plain_text)





