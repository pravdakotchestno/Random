import random

def powerMod(num, power, mod, result = 1):
	for _ in range(int(power)):
		result = result * num % mod
	return result

def isPrime(p, probability, a = 2):
	for i in range(probability):
		print(i, "/", probability)
		powmod = powerMod(a, (p - 1) / 2, p)
		if not (powmod == 1 or powmod == -1 % p):
			return False
		a += 1
	return True

def generaterandnumber(bits):
	number = random.getrandbits(bits)
	number = number | 2 ** bits
	number = number | 1
	return number

def main():
	bits = int(input("Enter amount of bits in prime number (it must be more than 7 bits): "))
	if not bits > 7:
		print("It must be more than 7 bits");raise SystemExit
	accuracy = int(input("Enter accuracy: "))
	prime = generaterandnumber(bits)
	while not isPrime(prime, accuracy):
		prime = generaterandnumber(bits)
	
	print(prime)
	print("The probability that the number is a prime is",1 - 1 / 2 ** accuracy)

main()