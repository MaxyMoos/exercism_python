def isPalindrome(integer):
	return str(integer) == str(integer)[::-1]

def smallest_palindrome(min_factor=0, max_factor=999):
	if min_factor == 0: min_factor = 1

	# Initialization
	result = [max_factor ** 2, (0,0)]

	for i in range(min_factor, max_factor + 1):
		for j in range(min_factor, max_factor + 1):
			candidate = i * j
			if isPalindrome(candidate):
				if candidate > result[0]: break
				if candidate < result[0]:
					result = [candidate, [min(i,j), max(i,j)]]
				elif candidate == result[0] and [min(i,j), max(i,j)] not in result[1]:
					result[1] += [min(i,j), max(i,j)]
	return result

def largest_palindrome(max_factor = 999, min_factor=0):
	if min_factor == 0: min_factor = 1

	# Initialization
	biggest = 1
	factors = []
	
	for i in reversed(range(min_factor, max_factor + 1)):
		for j in reversed(range(min_factor, max_factor + 1)):
			candidate = i * j
			if isPalindrome(candidate):
				if candidate < biggest: break
				if candidate > biggest:
					biggest = candidate
					factors = tuple([min(i,j),max(i,j)])
				elif candidate == biggest:
					if tuple([i,j]) not in factors: factors += tuple([i,j])
	return (biggest, factors)

# I cannot find the way to return factors as the test intends.
# All tests pass except for one (largest palindrome of single digits) that will fail
# I submit this exercise and will try to come back to it later to sort this out