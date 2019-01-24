import re
import os

def searchInFile(regexp, filepath):
	try:
		file = open(filepath, "r").readlines()
		for i in range(len(file)):
			matches = re.finditer(regexp, file[i])
			for m in matches:
				print(regexp, "find in line", i + 1, "in", os.path.abspath(filepath))
	except:
		pass
		
def searchInDirectory(regexp,dirname):

	for i in os.listdir(dirname):
		if os.path.isfile(i):
			searchInFile(regexp,i)
		elif os.path.isdir(i):
			searchInDirectory(regexp,i)

def main():
	regexp = input("Enter regular expression to search: ")
	searchInDirectory(regexp, "./")

main()