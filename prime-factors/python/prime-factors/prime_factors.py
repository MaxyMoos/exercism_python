def prime_factors(number):
	result = []
	factor = 2
	
	while ( number != 1 ):
		if ( number % factor == 0 ):
			result = result + [factor]
			number = number / factor
		else: factor += 1
	return result