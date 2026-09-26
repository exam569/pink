"""
Experiment No: 9  (E1-9)
ElGamal Cryptosystem - Encryption and Decryption
"""

import random

def find_primitive_root(p):
    for g in range(2, p):
        seen = set()
        for i in range(1, p):
            seen.add(pow(g, i, p))
        if len(seen) == p - 1:
            return g
    return None

def generate_keys(p, g):
    x = random.randint(2, p - 2)          # private key
    y = pow(g, x, p)                      # public key
    return x, y

def encrypt(m, p, g, y):
    k = random.randint(2, p - 2)
    c1 = pow(g, k, p)
    c2 = (m * pow(y, k, p)) % p
    return c1, c2

def decrypt(c1, c2, p, x):
    s = pow(c1, x, p)
    s_inv = pow(s, p - 2, p)
    m = (c2 * s_inv) % p
    return m

if __name__ == "__main__":
    p = int(input("Enter a prime number p: "))
    message = int(input("Enter message (integer, less than p): "))

    g = find_primitive_root(p)
    x, y = generate_keys(p, g)

    c1, c2 = encrypt(message, p, g, y)
    decrypted = decrypt(c1, c2, p, x)

    print("Prime (p)          :", p)
    print("Primitive Root (g) :", g)
    print("Private Key (x)    :", x)
    print("Public Key (y)     :", y)
    print("Plaintext (M)      :", message)
    print("Ciphertext (C1,C2) :", (c1, c2))
    print("Decrypted (M)      :", decrypted)
