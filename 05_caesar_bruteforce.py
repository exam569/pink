"""
Experiment No: 5  (E1-5)
Caesar Cipher Brute-Force Attack
"""

common_words = ["THE", "AND", "IS", "AM", "ARE", "BE", "TO", "OF", "IN", "THAT", "IT", "YOU", "FOR", "ON", "WITH", "AS", "I", "THIS", "HAVE", "AT", "BY", "FROM", "OR", "AN", "NOT", "BUT", "ALL", "WAS", "IF", "YOUR", "CAN", "MY", "WE", "SO", "ME", "NO", "DO", "WHAT", "ABOUT", "WHO", "WHEN", "WHERE", "WHY", "HOW", "THERE", "THEY", "SHE", "HE", "HIS", "HER", "THEIR", "THEM", "OUR", "US", "HIM", "THESE", "THOSE", "THEN", "THAN", "BECAUSE", "WHILE", "WHICH", "WHOM", "WHOSE", "EVERY", "SOME", "MANY", "FEW", "MAY", "MUST", "SHOULD", "WOULD", "COULD", "MIGHT", "WILL", "CAN'T", "DON'T", "ISN'T", "AREN'T", "WASN'T", "HASN'T", "HAVEN'T", "DIDN'T", "WON'T", "SHOULDN'T", "COULDN'T", "MIGHTN'T", "WOULDN'T", "CAN'T", "DON'T", "ISN'T", "AREN'T", "WASN'T", "HASN'T", "HAVEN'T", "DIDN'T", "WON'T", "SHOULDN'T", "COULDN'T", "MIGHTN'T", "WOULDN'T"]

def caesar_decrypt(text, shift):
    res = ""
    for ch in text:
        if ch.isalpha():
            base = 65 if ch.isupper() else 97
            res += chr((ord(ch) - base - shift) % 26 + base)
        else:
            res += ch
    return res

text = input("Enter ciphertext: ")
best_shift, best_score, best_text = 0, -1, ""

for shift in range(26):
    dec = caesar_decrypt(text, shift)
    score = sum(dec.upper().count(w) for w in common_words)
    print(shift, dec)
    if score > best_score:
        best_shift, best_score, best_text = shift, score, dec

print("\nMost likely shift:", best_shift)
print("Decrypted text   :", best_text)
