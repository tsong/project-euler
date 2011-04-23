from math import sqrt, ceil

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
