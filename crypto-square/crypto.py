import string
import math

def encode(clearText):
	gen = [letter for letter in clearText.lower() if letter in string.ascii_lowercase]
	length = len(gen)
	
	# Determine size of square
	size = math.sqrt(length)
	if size != math.floor(size): size = math.floor(size) + 1
	
	#matrix = [ [ ['-1'] * size] * size ]
	matrix = [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l'], ['m', 'n', 'o', 'p']]
	i = 0
	for x in matrix:
		print( "x = {}".format(x) )
		for pos, element in enumerate(x):
			if i < length:
				x[pos] = gen[i]
				i += 1
		"""
		for y in x:
			print( "y = {}".format(y) )
			for pos, element in enumerate(y):
				print( "pos = {} , element = {}".format(pos, element) )
				if i < length:
					y[pos] = gen[i]
					i += 1
		"""
	print ( matrix ) 

encode('youpilegros test')