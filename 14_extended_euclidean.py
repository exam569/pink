"""
Experiment No: 14  (E2-5)
Extended Euclidean Algorithm + Modular Inverse
"""

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

if __name__ == "__main__":
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    gcd, x, y = extended_gcd(a, b)
    print(f"GCD({a}, {b}) = {gcd}")
    print(f"Bezout coefficients: x = {x}, y = {y}")
    print(f"Verification: {a}*({x}) + {b}*({y}) = {a*x + b*y}")

    # Modular inverse of a under modulo m
    m = int(input("Enter modulus m to find modular inverse of a: "))
    g, x2, _ = extended_gcd(a, m)
    if g == 1:
        inverse = x2 % m
        print(f"Modular inverse of {a} mod {m} = {inverse}")
        print(f"Check: ({a} * {inverse}) mod {m} =", (a * inverse) % m)
    else:
        print(f"Modular inverse does not exist since gcd({a},{m}) != 1")
