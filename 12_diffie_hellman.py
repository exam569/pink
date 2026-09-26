"""
Experiment No: 12  (E2-3)
Diffie-Hellman Key Exchange
"""

import random

def diffie_hellman(p, g):
    a = random.randint(2, p - 2)          
    A = pow(g, a, p)                      

    b = random.randint(2, p - 2)          
    B = pow(g, b, p)                      

    alice_shared_key = pow(B, a, p)
    bob_shared_key = pow(A, b, p)

    return a, b, A, B, alice_shared_key, bob_shared_key

if __name__ == "__main__":
    p = int(input("Enter public prime modulus p: "))
    g = int(input("Enter public base g: "))

    a, b, A, B, alice_key, bob_key = diffie_hellman(p, g)

    print("Public Prime (p)      :", p)
    print("Public Base (g)       :", g)
    print("Alice's Private (a)   :", a)
    print("Alice's Public (A)    :", A)
    print("Bob's Private (b)     :", b)
    print("Bob's Public (B)      :", B)
    print("Alice's Shared Secret :", alice_key)
    print("Bob's Shared Secret   :", bob_key)
    print("Keys Match?           :", alice_key == bob_key)
