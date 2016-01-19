import itertools
from math import sqrt

def checkIrregular(matrix):
	if len(matrix) == 0: return
	length = len(matrix[0])
	for row in matrix[1:]:
		if len(row) != length:
			raise ValueError("The matrix is irregular")

def saddle_points(inMatrix):
	checkIrregular(inMatrix)
	transposed = [list(i) for i in itertools.zip_longest(*inMatrix, fillvalue='')]
	result = []
	for row in inMatrix:
		i = max(row)
		# Get the indexes of max values in current row (may be several!)
		max_pos = [a for a,b in enumerate(row) if b == i]
		for pos in max_pos:
			candidate = row[pos]
			if ( candidate == min( transposed[pos] ) ):
				result += [tuple([inMatrix.index(row), pos])]
	return set(result)