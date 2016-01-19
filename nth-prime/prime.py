def nth_prime(rank):
	primes = [2]
	i = 3
	while len(primes) < rank:
		notprime = False
		for j in range (3, int(i/2) , 2):
			if i % j == 0:
				notprime = True
				break
		if not notprime:
			primes += [i]
		i += 2
	return primes[-1]