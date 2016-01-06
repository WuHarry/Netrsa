import random
from FastExpMod import fastExpMod
from primeTest import primeTest
from extendedGCD import extendedGCD

def findPrime(halfkeyLength):
    while True:
        #Select a random number n
        n = random.randint(0, 1 << halfkeyLength)
        if n % 2 != 0:
            found = True
            #If n satisfy primeTest 10 times, then n should be a prime number
            for i in range(0, 10):
                if primeTest(n) == "composite":
                    found = False
                    break
            if found:
                return n

def selectE(fn, halfkeyLength):
    while True:
        #e and fn are relatively prime
        e = random.randint(0, 1 << halfkeyLength)
        (x, y, r) = extendedGCD(e, fn)
        if r == 1:
            return e

def computeD(fn, e):
    (x, y, r) = extendedGCD(fn, e)
    #y maybe < 0, so convert it
    if y < 0:
        return fn + y
    return y

def keyGeneration(keyLength):
    #generate public key and private key
    p = findPrime(keyLength/2)
    q = findPrime(keyLength/2)
    n = p * q
    fn = (p-1) * (q-1)
    e = selectE(fn, keyLength/2)
    d = computeD(fn, e)
    return (n, e, d)

def encryption(M, e, n):
    #RSA C = M^e mod n
    return fastExpMod(M, e, n)

def decryption(C, d, n):
    #RSA M = C^d mod n
    return fastExpMod(C, d, n)


#Unit Testing
(n, e, d) = keyGeneration(1024)
print "n", n
print "e", e
print "d", d
#AES keyLength = 64
X = random.randint(0, 1 << 256)
print "PlainText:", X
C = encryption(X, e, n)
print "Encryption of plainText:", C
M = decryption(C, d, n)
print "Decryption of cipherText:", M
print "The algorithm is correct:", X == M