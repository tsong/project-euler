N = 1000000
T = set([n*(n+1)/2 for n in xrange(286, N)])
P = set([n*(3*n-1)/2 for n in xrange(166, N)])
H = set([n*(2*n-1) for n in xrange(144, N)])

for t in T:
	if t in P and t in H:
		print t
		break
