"""
Experiment No: 3  (E1-3)
Monoalphabetic Substitution Cipher - Encryption and Decryption
"""

import random, string

text = input("Enter message: ").upper()
plain = list(string.ascii_uppercase)
shuffled = plain.copy()
random.shuffle(shuffled)
key = dict(zip(plain, shuffled))
rev = {v: k for k, v in key.items()}

enc = "".join(key.get(c, c) for c in text)
dec = "".join(rev.get(c, c) for c in enc)

print("Key Mapping:")
for k in sorted(key):
    print(f"  {k} -> {key[k]}")
print("Encrypted:", enc)
print("Decrypted:", dec)
