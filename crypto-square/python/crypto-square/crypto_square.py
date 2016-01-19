import string
import math
import itertools

def encode(clearText):
	gen = ''.join( [letter for letter in clearText.lower() if letter in string.ascii_lowercase + string.digits] )
	length = len(gen)
	
	# Determine size of square
	size = math.sqrt(length)
	if size != math.floor(size): size = math.floor(size) + 1

	temp = split(gen, int(size))
	superTmp = [''.join(i) for i in itertools.zip_longest(*temp, fillvalue='') ]
	return ' '.join(superTmp)

def split(input, l):
	if len(input) <= l:
		return [input]
	return [ input[:l] ] + split(input[l:], l)