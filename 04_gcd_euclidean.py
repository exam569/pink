"""
Experiment No: 4  (E1-4)
GCD using Euclidean Algorithm
"""

def gcd(a, b):
    steps = []
    while b != 0:
        steps.append(f"gcd({a}, {b}) => {a} = {a // b} * {b} + {a % b}")
        a, b = b, a % b
    return a, steps

if __name__ == "__main__":
    a = int(input("Enter first number a: "))
    b = int(input("Enter second number b: "))

    result, steps = gcd(a, b)
    print(f"Finding GCD({a}, {b}) using Euclidean Algorithm:")
    for s in steps:
        print(" ", s)
    print("GCD =", result)
