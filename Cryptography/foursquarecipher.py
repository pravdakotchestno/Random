import re
square = [
'ABCDE','THEQU',
'FGHIK','ICKBR',
'LMNOP','OWNFX',
'QRSTU','MPSVL',
'VWXYZ','AZYDG',
################
'VWXYZ','ABCDE',
'UQMHD','FGHIK',
'TPLGC','LMNOP',
'SOKFB','QRSTU',
'RNIEA','VWXYZ']

square_x = len(square[0])
square_y = len(square)//4

def split_by_2(string):
	return re.findall('..',string)

def get_quarter(num):
	quarter = ''
	for i in range(square_y):
		quarter += square[i * 2 + (num % 2) + (num // 2) * square_y * 2]
	return quarter

def get_by_letter(num, letter):
	index = get_quarter(num).index(letter)
	return index % square_x, index // square_y

def get_by_coordinates(num, x, y):
	quarter = get_quarter(num)
	return quarter[y * square_y + x]

def get_letters_enc(letters):
	x1, y1 = get_by_letter(0, letters[0])
	x2, y2 = get_by_letter(3, letters[1])
	return get_by_coordinates(1, x2, y1) + get_by_coordinates(2, x1, y2)

def get_letters_dec(letters):
	x1, y1 = get_by_letter(1, letters[0])
	x2, y2 = get_by_letter(2, letters[1])
	return get_by_coordinates(0, x2, y1) + get_by_coordinates(3, x1, y2)

def encrypt(message):
	message = split_by_2(message)
	crypted = ''
	for letters in message:
		crypted += get_letters_enc(letters)
	return crypted

def decrypt(message):
	message = split_by_2(message)
	decrypted = ''
	for letters in message:
		decrypted += get_letters_dec(letters)
	return decrypted
