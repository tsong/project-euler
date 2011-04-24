import sys
P = [(3*n*n-n)/2 for n in xrange(1,1000000)]
S = set(P)

for i in xrange(len(P)):
	for j in xrange(i):
		if P[i] + P[j] in S and P[i] - P[j] in S:
			print P[i], P[j], P[i] - P[j]
			sys.exit(0)
