
def root(number, n):
	nearestRoot = 1
	while True:
		lastNearestRoot = nearestRoot
		nearestRoot = ((n - 1) * lastNearestRoot + number / (lastNearestRoot ** (n - 1))) / n
		if lastNearestRoot == nearestRoot:
			return nearestRoot

	