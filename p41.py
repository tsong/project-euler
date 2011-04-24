from itertools import permutations
from eulerlib import isprime

for n in reversed(xrange(1,10)):
	D = [str(d) for d in reversed(xrange(1,n+1))]

	found = False
	for p in permutations(range(len(D))):
		n = int(''.join([D[i] for i in p]))
		if isprime(n):
			print n
			found = True
			break
	if found: 
		break
