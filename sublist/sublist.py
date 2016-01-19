import math

SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def check_lists(first, second):
	result = -1
	diff = len(second) - len(first)

	# Deal with equality cases
	if ( diff == 0 and first == second ): return EQUAL
	elif ( diff == 0 ) : return UNEQUAL

	if diff < 0 : 
		longest = first
		shortest = second
	else:
		longest = second
		shortest = first

	n = len(shortest)
	
	if n == 0:
		if ( shortest == first ): return SUBLIST
		else: return SUPERLIST
		
	superList = [ longest[i:i+n] for i in range( n-1 ) ]
	if ( shortest in superList ):
		if ( shortest == first ): return SUBLIST
		else: return SUPERLIST

	return result

print( check_lists([], [1, 2]) )