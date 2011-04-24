from math import factorial

def C(n,r):
	p = 1
	for x in xrange(r+1,n+1):
		p *= x

	return p / factorial(n-r)

s = 0
for n in xrange(1,101):
	for r in xrange(n+1):
		if C(n,r) > 1000000:
			s += 1

print s

