"""
Experiment No: 11  (E2-2)
RSA Algorithm - Encryption and Decryption
"""

import random

def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5)+1))

def random_prime(low=100, high=300):
    n = random.randint(low, high)
    while not is_prime(n):
        n = random.randint(low, high)
    return n

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

msg = input("Enter message: ")
p = random_prime()
q = random_prime()
while q == p:
    q = random_prime()

n = p * q
phi = (p - 1) * (q - 1)
e = random.randrange(2, phi)
while gcd(e, phi) != 1:
    e = random.randrange(2, phi)
d = pow(e, -1, phi)

width = len(hex(n)[2:])
enc_nums = [pow(ord(c), e, n) for c in msg]
enc_hex = "".join(f"{c:0{width}x}" for c in enc_nums)
chunks = [enc_hex[i:i+width] for i in range(0, len(enc_hex), width)]
dec = "".join(chr(pow(int(ch, 16), d, n)) for ch in chunks)

print("p, q:", p, q)
print("Public key :", (e, n))
print("Private key:", (d, n))
print("Encrypted  :", enc_hex)
print("Decrypted  :", dec)