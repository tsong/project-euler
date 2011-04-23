from eulerlib import *

P = set(sieve(1000000)) #pick arbitrarily large number

def consecprimes(a,b):
	n = 0
	while True:
		f = n**2 + a*n + b
		if f not in P:
			return n + 1
		n += 1


res = reduce(lambda x,y: x if x[2] > y[2] else y,\
			[(a,b, consecprimes(a,b,)) \
				for a in xrange(-999,999) for b in range(-999,999) ])

print res, res[0] * res[1]


