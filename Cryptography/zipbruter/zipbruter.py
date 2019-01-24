from zipfile import ZipFile
from os import mkdir


archiveFile = input("Enter name of zipfile:\n")
dictionaryFile = input("Enter name of dictionary file:\n")

line = "----------------------------------"
directory = "ExtractArchive"

def brute(string):
	for word in string:
		passwd = word.replace('\n','')
		archive.setpassword(passwd.encode())
		try: 
			archive.extractall(directory)
			return passwd
		except: 
			pass
	return

mkdir(directory)

print(line)

with open(dictionaryFile, errors='ignore') as dictionary:
	with ZipFile(archiveFile) as archive:
		password = brute(dictionary)
		if password != None:
			print("Password is '%s'" % password)
		else:
			print("Password not found")
print(line)
