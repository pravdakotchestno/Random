alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def bitLen(x):
	return len(bin(x)) - 2

def bitLenWithUpRounding(b, r):
	return bitLen(b) + (r - (bitLen(b) % r)) % r

def stringIntoBits(string, bits = 0):
	for ch in string:
		bits <<= 8
		bits ^= ord(ch)
	return bits

def encodeBase64(string):
	bits = stringIntoBits(string)

	bits = bits << ((6 - (bitLenWithUpRounding(bits, 8) % 6)) % 6)

	final = ""
	countofcycles = bitLenWithUpRounding(bits, 6) // 6

	for _ in range(countofcycles):

		final += alf[bits % (1 << 6)]
		bits >>= 6

	final = final[::-1]
	final += (4 - (len(final) % 4)) % 4 * '='
	return final

def main():

	encodedstr = encodeBase64(input("Enter string to encode:\n"))
	print(encodedstr)

main()