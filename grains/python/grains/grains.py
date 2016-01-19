def on_square(squareNb):
	return 2 ** (squareNb - 1)

def total_after(squareNb):
	return sum(2 ** i for i in range (0 , squareNb) )