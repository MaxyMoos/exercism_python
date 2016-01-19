import fractions

def primitive_triplets(i):
	m_times_n = int(i/2)
	possibilities = [ [m,n] for n in range(1, m_times_n) for m in range(n, m_times_n + 1) if (m-n % 2 != 0) and (m*n*2 == i) and fractions.gcd(m,n) == 1]
	
	res = []

	for [m,n] in possibilities:
		a = (m ** 2 - n ** 2)
		b = 2 * m * n
		c = m ** 2 + n ** 2
		tmp = [a,b,c]
		tmp.sort()
		res += [tmp]
	return res
	# print("a = {}, b = {}, c = {} - Result = {}".format(a,b,c, (a**2 + b**2 == c**2)))

def triplets_in_range(rg):
	pass

def is_triplet(cand):
	for [a,b,c] in cand:
		return a**2 + b**2 == c**2


print(primitive_triplets(4))
print(primitive_triplets(84))
print(primitive_triplets(420))

