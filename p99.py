from math import log

N = [ (int(l[0]), int(l[1])) for l in \
			[l.strip().split(',') for l in open('data/p99.in')] ]

m = -1
l = -1
for i in xrange(len(N)):
	v = N[i][1] * log(N[i][0])
	if v > m:
		m = v
		l = i
print l+1
