"""
DOS attacks on network traffic are on the rise. AES encryption can be used to ensure a TCP is not vulnerable.

Write a function to pass the plain_text as an encrypted message on line 16 in the template code.

"""

import hashlib
from Crypto.Cipher import AES
from Crypto.Util import Counter
from base64 import b64encode, b64decode
import os
 
class AESCipher(object):
    def __init__(self, key):
        self.block_size = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()
 
    def encrypt(self, plain_text):
        plain_text = self.__pad(plain_text)
        counter = Counter.new(self.block_size * 8)
        cipher = AES.new(self.key, AES.MODE_CTR, counter=counter)
        # Fix ME: pass the plain_text to the encrypt function
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(encrypted_text).decode("utf-8")
 
    def __pad(self, plain_text):
        number_of_bytes_to_pad = self.block_size - len(plain_text) % self.block_size
        ascii_string = chr(number_of_bytes_to_pad)
        padding_str = number_of_bytes_to_pad * ascii_string
        padded_plain_text = plain_text + padding_str
        return padded_plain_text
 
if __name__ == '__main__':
 
    msg = input("Enter message: ")
    cipher = AESCipher(msg)
    #Test the message size
    msg = msg*10
    
    print(cipher.encrypt(msg))