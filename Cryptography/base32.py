alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"

def bitLen(x):
	return len(bin(x)) - 2

def bitLenWithUpRounding(b, r):
	return bitLen(b) + (r - (bitLen(b) % r)) % r

def stringIntoBits(string, bits = 0):
	for ch in string:
		bits <<= 8
		bits ^= ord(ch)
	return bits

def encodeBase32(string):
	bits = stringIntoBits(string)

	bits = bits << ((5 - (bitLenWithUpRounding(bits, 8) % 5)) % 5)

	final = ""
	countofcycles = bitLenWithUpRounding(bits, 5) // 5

	for _ in range(countofcycles):

		final += alf[bits % (1 << 5)]
		bits >>= 5

	final = final[::-1]
	final += (8 - (len(final) % 8)) % 8 * '='
	return final

def main():

	encodedstr = encodeBase32(input("Enter string to encode:\n"))
	print(encodedstr)

main()