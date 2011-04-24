from eulerlib import sieve 

P = set(sieve(10000))


def isperm(a,b):
	s1 = set(str(a))
	s2 = set(str(b))
	return s1 == s2 

for n0 in xrange(1000,10000):
	if n0 not in P: 
		continue

	for i in xrange(1,10000):
		n1 = n0 + i
		n2 = n1 + i
		if n1 > 9999 or n2 > 9999:
			break

		if n1 in P and n2 in P and isperm(n0,n1) and isperm(n0,n2):
			print n0,n1,n2,i
