"""
Experiment No: 6  (E1-6)
Playfair Cipher - Encryption and Decryption
"""

import random, string

def matrix(key):
    key = key.upper().replace("J", "I")
    seen = []
    for c in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if c.isalpha() and c not in seen:
            seen.append(c)
    return [seen[i:i+5] for i in range(0, 25, 5)]

def find(m, c):
    for i in range(5):
        for j in range(5):
            if m[i][j] == c:
                return i, j

def make_pairs(text):
    text = text.upper().replace("J", "I")
    text = "".join(c for c in text if c.isalpha())
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else "X"
        if a == b:
            pairs.append(a + "X")
            i += 1
        else:
            pairs.append(a + b)
            i += 2
    return pairs

def crypt(text, key, encrypt=True):
    m = matrix(key)
    pairs = make_pairs(text)
    d = 1 if encrypt else -1
    result = ""
    for a, b in pairs:
        r1, c1 = find(m, a)
        r2, c2 = find(m, b)
        if r1 == r2:
            result += m[r1][(c1+d)%5] + m[r2][(c2+d)%5]
        elif c1 == c2:
            result += m[(r1+d)%5][c1] + m[(r2+d)%5][c2]
        else:
            result += m[r1][c2] + m[r2][c1]
    return result

text = input("Enter plaintext: ")
key = "".join(random.sample(string.ascii_uppercase.replace("J", ""), 6))

enc = crypt(text, key, True)
dec = crypt(enc, key, False)

print("Key used:", key)
print("Encrypted:", enc)
print("Decrypted:", dec)