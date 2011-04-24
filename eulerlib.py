from math import sqrt

#returns the greatest common denominator of a and b
def gcd(a,b):
	if b == 0:
		return a
	return gcd(b, a%b)

#simplifies a fraction f, represented as tuple (numerator, demoniator)
def simplify(f):
	g = gcd(f[0],f[1])
	return (f[0]/g, f[1]/g)

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

#returns a list of all prime factors of n
def factor(n):
	if n < 1: return []
	if n == 1: return [1]

	F = []
	for p in seive(int(sqrt(n))+2):
		while n % p == 0:
			n /= p
			F.append(p)
	if n != 1:
		F.append(n)
	return F
