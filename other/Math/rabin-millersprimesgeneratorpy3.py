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

def main():
	bits = int(input("Enter amount of bits in prime number (it must be more than 7 bits): "))
	if not bits > 7:
		print ("It must be more than 7 bits")
		raise SystemExit
	accuracy = int(input("Enter accuracy: "))
	prime = generaterandnumber(bits)
	while not isPrime(prime, accuracy):
		prime = generaterandnumber(bits)
		
	
	print(prime)
	print ("The probability that the number is a prime is", (1 - 1 / 4 ** accuracy))

main()

