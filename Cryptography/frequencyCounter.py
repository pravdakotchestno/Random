E = ['E','T','A','O','N','R','I','S','H','D','L','F','C','M','U','Q','Y','P','W','B','V','K','X','J','Q','Z']
R = ['О','Е','А','И','Н','Т','С','Р','В','Л','К','М','Д','П','У','Я','Ы','Ь','Г','З','Б','Ч','Й','Х','Ж','Ш','Ю','Ц','Щ','Э','Ф','Ъ','Ё',]

def change(text, a, b):
	newtext = ""
	for l in text:
		n = l
		if n == a:
			n = b
		elif n == b:
			n = a
		newtext += n
	return newtext

def manualPermutation(text):

	inputstr = ""
	while True:
		print(text)
		inputstr = input("symbols to change:\n")
		if len(inputstr) < 2:
			print("Exit");raise SystemExit
		text = change(text, inputstr[0], inputstr[1])

def autoPermutation(text, lang, symbolsnottochange):
	alf = None
	if lang == 'E':
		alf = E
	else:
		alf = R
	symbols = set(text)
	frequency = dict.fromkeys(symbols, 0)
	for i in text:
		frequency[i] += 1
	symbolsbyfreq = sorted(frequency.items(), key = lambda k: k[1])
	print(symbolsbyfreq)
	i = 0
	j = 0
	for _ in range(min(len(alf), len(symbolsbyfreq))):

		if not (symbolsbyfreq[-j - 1][0] in symbolsnottochange):

			print("change %c to %c" % (symbolsbyfreq[-j - 1][0], alf[i]))

			text = change(text, symbolsbyfreq[-j - 1][0], alf[i])
			i += 1
		j += 1

	return str(text)

def main():
	lang = input("Enter language ([E]nglish or [R]ussian):").upper()
	if lang not in ['E', 'R']:
		print("Unknown language!");raise SystemExit
	ignoredchars = set(input("Enter chars which you want to ignore (press enter if you want to use default config):\n"))
	if ignoredchars == set():
		ignoredchars = set(" -,.?!()[]'\"")
	text = input("Enter the crypted text:\n")
	text = autoPermutation(text, lang, ignoredchars)
	manualPermutation(text)

main()