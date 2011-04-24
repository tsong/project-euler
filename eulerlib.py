from math import sqrt

#returns the greatest common denominator of a and b
def gcd(a,b):
	if a == 0:
		return b
	while b != 0:
		if a > b:
			a -= b
		else:
			b -= a
	return a

#returns least common multiple of a and b
def lcm(a,b):
	return abs(a*b)/gcd(a,b)

#returns result of addition of two fractions, represented as tuples
def addf(x,y):
	l = lcm(x[1],y[1])
	f = (l/x[1]*x[0] + l/y[1]*y[0], l)
	return simplify(f)

#returns result of multiplication of two fractions, represented as tuples
def multf(f,v):
	return (f[0]*v, f[1]*v)

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
