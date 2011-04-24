from eulerlib import sieve

N = 1000000
P = sieve(N)
S = set(P)

m = -1
p = -1
for i in xrange(len(P)):
	s = 0
	j = i
	while s < N and j < len(P):
		s += P[j]
		j += 1
		if s in S and j-i > m:
			m = j-i
			p = s

print p
