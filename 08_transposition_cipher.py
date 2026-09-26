"""
Experiment No: 8  (E1-8)
Transposition Cipher with Double Encryption
"""

import random, string

def encrypt(text, key):
    text = text.replace(" ", "").upper()
    while len(text) % len(key):
        text += "X"
    order = sorted(range(len(key)), key=lambda i: key[i])
    rows = [text[i:i+len(key)] for i in range(0, len(text), len(key))]
    return "".join(row[i] for i in order for row in rows)

def random_key(n=5):
    return "".join(random.sample(string.ascii_uppercase, n))

text = input("Enter plaintext: ")
key1 = random_key()
key2 = random_key()

first = encrypt(text, key1)
final = encrypt(first, key2)

print("Key 1:", key1, " Key 2:", key2)
print("After 1st pass  :", first)
print("Final Ciphertext:", final)