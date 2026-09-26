"""
Experiment No: 10  (E2-1)
DES - Encryption and Decryption
"""

import random, string
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

text = input("Enter plaintext: ")
key = "".join(random.choices(string.ascii_letters + string.digits, k=8)).encode()

enc = DES.new(key, DES.MODE_ECB).encrypt(pad(text.encode(), 8))
dec = unpad(DES.new(key, DES.MODE_ECB).decrypt(enc), 8).decode()

print("Key:", key)
print("Plaintext      :", text)
print("Encrypted:", enc.hex())
print("Decrypted:", dec)
