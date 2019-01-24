import math
def addition(curcell, char, bfchar = ""):
	if (curcell - ord(char)) > ord(char):
		bfchar += (">" +("+" * ord(char)))
		curcell = ord(char)
	else:
		if ord(char) - curcell > 0:
			bfchar += ("+" * (ord(char) - curcell))
			curcell += (ord(char) - curcell)
		else:
			bfchar += ("-" * (curcell - ord(char)))
			curcell -= (curcell - ord(char))
	bfchar += "."
	return curcell, bfchar
def main():
	bfstring = ""
	
	string = input("Enter your string:")
	curcell = 0
	for ch in string:
		curcell, char = addition(curcell, ch)
		bfstring += char
	print(bfstring)
main()