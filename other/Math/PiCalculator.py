import math
def calculate(accuracy, result = 3.0):
	for i in range(1, accuracy * 4, 4):
		result += 4 / ((i + 1) * (i + 2) * (i + 3))
		result -= 4 / ((i + 3) * (i + 4) * (i + 5))
	return result
def main():
	accuracy = int(input("Enter accuracy:\n"))
	pi = calculate(accuracy)
	print(pi,"is calculated PI")
	print(math.pi,"is PI from 'math' package")

main()