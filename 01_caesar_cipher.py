"""
Experiment No: 1  (E1-1)
Caesar Cipher - Encryption and Decryption
"""

import string
def caesar(text, shift):
   
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase

    shift = shift % 26
    shifted_lower = lower[shift:] + lower[:shift]
    shifted_upper = upper[shift:] + upper[:shift]

    table = str.maketrans(lower + upper, shifted_lower + shifted_upper)
    return text.translate(table)

message = input("Enter your message: ")
key = int(input("Enter shift key: "))

encrypted = caesar(message, key)
decrypted = caesar(encrypted, -key)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)