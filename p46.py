from eulerlib import * 

N = 100000
S = [2*n*n for n in xrange(N)]
P = set(seive(N))
C = [n for n in xrange(9,N,2) if n not in P]

for n in C:
	satisfied = False
	for s in S:
		if n-s in P:
			satisfied = True
			break
	if not satisfied:
		print n
		break
