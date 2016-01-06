"""
e = e0*(2^0) + e1*(2^1) + e2*(2^2) + ... + en * (2^n)

b^e = b^(e0*(2^0) + e1*(2^1) + e2*(2^2) + ... + en * (2^n))
    = b^(e0*(2^0)) * b^(e1*(2^1)) * b^(e2*(2^2)) * ... * b^(en*(2^n))

b^e mod m = ((b^(e0*(2^0)) mod m) * (b^(e1*(2^1)) mod m) * (b^(e2*(2^2)) mod m) * ... * (b^(en*(2^n)) mod m) mod m
"""
import random
from FastExpMod import fastExpMod

def primeTest(n):
    q = n - 1
    k = 0
    # Find k, q, satisfied 2^k * q = n - 1
    while q % 2 == 0:
        k += 1
        q /= 2
    a = random.randint(2, n - 2);
    # If a^q mod n= 1, n maybe is a prime number
    if fastExpMod(a, q, n) == 1:
        return "inconclusive"
    # If there exists j satisfy a ^ ((2 ^ j) * q) mod n == n-1, n maybe is a prime number
    for j in range(0, k):
        if fastExpMod(a, (2 ** j) * q, n) == n - 1:
            return "inconclusive"
    # a is not a prime number
    return "composite"
