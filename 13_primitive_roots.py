"""
Experiment No: 13  (E2-4)
Modular Arithmetic using Primitive Root
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primitive_roots(p):
    if not is_prime(p):
        return []
    roots = []
    for g in range(2, p):
        seen = set()
        for i in range(1, p):
            seen.add(pow(g, i, p))
        if len(seen) == p - 1:
            roots.append(g)
    return roots

def modular_exponentiation_table(p, g):
    print(f"Powers of primitive root g={g} modulo p={p}:")
    for i in range(1, p):
        print(f"  g^{i} mod {p} = {pow(g, i, p)}")

if __name__ == "__main__":
    p = int(input("Enter a prime number p: "))

    roots = find_primitive_roots(p)
    print(f"All primitive roots of {p}:", roots)

    g = roots[0]
    modular_exponentiation_table(p, g)

    a, b = 3, 5
    print(f"g^{a} mod {p} * g^{b} mod {p} mod {p} =", (pow(g, a, p) * pow(g, b, p)) % p)
    print(f"g^({a}+{b}) mod {p}                  =", pow(g, a + b, p))
