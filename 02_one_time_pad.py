"""
Experiment No: 2  (E1-2)
One-Time Pad - Encryption and Decryption
"""

import random


def generate_key(length):
    return [random.randint(0, 255) for _ in range(length)]

def otp(text_or_nums, key):
    if isinstance(text_or_nums, str):
        return [ord(c) ^ k for c, k in zip(text_or_nums, key)]
    else:
        return "".join(chr(c ^ k) for c, k in zip(text_or_nums, key))

message = input("Enter message: ")
key = generate_key(len(message))

encrypted = otp(message, key)
decrypted = otp(encrypted, key)

print("Key      :", key)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)