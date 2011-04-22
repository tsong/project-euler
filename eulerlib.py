#returns True if n is prime
def isprime(n):
	for i in xrange(2,n/2):
		if n % i == 0:
			return False
	return True

#returns a list of prime numbers up to n using a seive algorithm
def seive(n):
	P = [False,False] + [True for i in xrange(n-2)]
	i = 1
	while i < n:
		i += 1
		while i < n and not P[i]: i += 1
		ii = 2*i
		while ii < n:
			P[ii] = False 
			ii += i

	return [i for i in xrange(len(P)) if P[i]]


	
	
