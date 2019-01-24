import math

import random

primesTo256 =[2,3,5,7,11,13,17,19,23,29,31,
            37,41,43,47,53,59,61,67,71,73,79,
            83,89,97,101,103,107,109,113,127,131,137,
            139,149,151,157,163,167,173,179,181,191,193,
            197,199,211,223,227,229,233,239,241,251]

def bruteIsPrime(p):
    for i in primesTo256:
        if p % i == 0:
            return False
    return True

def searchBM(m):
    m -= 1
    b = 0
    while m % 2 == 0:
        b += 1
        m //= 2
    return b, m

def doRabinMillersTest(p, a):
    b,m = searchBM(p)
    x = pow(a, m, p)
    if x == p - 1 or x == 1:
        return True
    for j in range(1, b):
        power = pow(2, j) * m
        x = pow(a, power, p)
        if x == 1:
            return False
        if x == p - 1:
            return True
    return False

def isPrime(p, probability):
    if not bruteIsPrime(p):
        return False

    for i in range(probability):
        a = random.randint(2, probability + 2)
        if not doRabinMillersTest(p, a):
            return False
        
    return True

def generaterandnumber(bits):
    number = random.getrandbits(bits)
    number = number | 2 ** bits
    number = number | 1
    return number

def generatePrime(amountofbits):
    
    accuracy = 7

    prime = generaterandnumber(amountofbits)
    while not isPrime(prime, accuracy):
        prime = generaterandnumber(amountofbits)
    return prime
    



def generateKeys(amountofbits):
    print("first prime is generating")
    p1 = generatePrime(amountofbits // 2)
    print("second prime is generating")
    p2 = generatePrime(amountofbits // 2)
    module = p1 * p2
    ef = (p1 - 1) * (p2 - 1)
    exp = searchExp()

    d = searchD(exp,ef)
    
    return [exp,module],[d,module]

def searchExp():
    exp = 65537
    return exp

def searchD(exp,ef):
    d = 0
    for k in range(1, exp):
        if (k * ef + 1) % exp == 0:
            d = (k * ef + 1) // exp
            break;
    return d

def encrypt(number,openkey):
    return pow(number,openkey[0],openkey[1])


def decrypt(number,secretkey):
    return pow(number,secretkey[0],secretkey[1])


def main():
    amountofbits = int(input("Enter amount of bits in RSA key:\n"))
    

    openkey,secretkey = generateKeys(amountofbits)
    print("Open key:",openkey)
    print("Secret key:",secretkey)

    message = int(input("Enter your message (number): \n"))
    secretmess = encrypt(message,openkey)
    print("Message is",message,"\nEncrypted message is ",secretmess)
    decryptedmess = decrypt(secretmess,secretkey)
    print("Decrypted message is",decryptedmess)

main()
