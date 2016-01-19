def sieve(finalNumber):
	numbers = range(2, finalNumber + 1)
	for element in numbers:
		if element != -1:
			for x in numbers[numbers.index(element) + 1:]:
				if ( x != -1 and x % element == 0 ):
					numbers[numbers.index(x)] = -1
	while (numbers.count(-1) > 0): numbers.remove(-1)
	return numbers