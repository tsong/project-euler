import sys
from eulerlib import sieve

P = sieve(1000000)
S = set(P)

def rotate(s,I):
	d = 0
	for n in xrange(1 if 0 in I else 0, 10):
		C = [c for c in s]
		for i in I: 
			C[i] = str(n)
		if int(''.join(C)) in S:
			d += 1
	return d

for p in P:
	s = str(p)
	for d in set(s): 
		I = []
		for i in xrange(len(s)):
			v = -1
			if s[i] == d:
				I.append(i)
				v = rotate(s,I)
			if v == 8:
				print s
				found = True
				sys.exit(0)	


