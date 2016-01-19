def slices(theStr, order):
	if ( order > len(theStr) or order == 0 ):
		raise ValueError("Order is superior to total string length")
	else:
		result = []
		i = 0
		while ( i <= len(theStr) - order ):
			result = result + [ [ int(x) for x in theStr[i:i+order] ] ]
			i = i + 1
		return result