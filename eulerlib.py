from math import sqrt, ceil

#returns the greatest common denominator of a and b
def gcd(a,b):
	while b != 0:
		t = b
		b = a % b
		a = t
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
	if n <= 1: return False
	if n < 4: return True
	if n % 2 == 0 or n % 3 == 0: return False 

	for i in xrange(5,int(sqrt(n))+2,6):
		if n % i == 0 or n % (i+2) == 0:
			return False
	return True

#returns a list of prime numbers up to n using a sieve algorithm
def sieve(n):
	P = [False,False] + [True for i in xrange(n-2)]

	for i in xrange(2,int(sqrt(n))+2):
		if P[i]:
			for j in xrange(i*i,n,i):
				P[j] = False

	return [i for i in xrange(len(P)) if P[i]]

#returns a list of all prime factors of n
def factor(n):
	if n < 1: return []
	if n == 1: return [1]

	F = []
	for p in sieve(int(sqrt(n))+2):
		while n % p == 0:
			n /= p
			F.append(p)
	if n != 1:
		F.append(n)
	return F
