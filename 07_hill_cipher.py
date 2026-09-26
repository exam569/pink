"""
Experiment No: 7  (E1-7)
2x2 Hill Cipher - Encryption and Decryption
"""

import random

def mod_inv(a, m):
    a %= m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x

def hill(text, k):
    text = text.upper().replace(" ", "")
    if len(text) % 2:
        text += "X"
    nums = [ord(c) - 65 for c in text]
    res = []
    for i in range(0, len(nums), 2):
        p1, p2 = nums[i], nums[i+1]
        res.append((k[0]*p1 + k[1]*p2) % 26)
        res.append((k[2]*p1 + k[3]*p2) % 26)
    return "".join(chr(n + 65) for n in res)

def random_key():
    while True:
        k = [random.randint(0, 25) for _ in range(4)]
        det = (k[0]*k[3] - k[1]*k[2]) % 26
        if mod_inv(det, 26):
            return k

def key_inverse(k):
    det = (k[0]*k[3] - k[1]*k[2]) % 26
    det_inv = mod_inv(det, 26)
    return [k[3]*det_inv % 26, -k[1]*det_inv % 26, -k[2]*det_inv % 26, k[0]*det_inv % 26]

text = input("Enter plaintext: ")
k = random_key()

enc = hill(text, k)
dec = hill(enc, key_inverse(k))

print("Key matrix:", k)
print("Encrypted:", enc)
print("Decrypted:", dec)