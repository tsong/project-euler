def digitalsum(n):
	return sum( [int(d) for d in str(n)] )

m = -1
for a in xrange(100):
	for b in xrange(100):
		s = digitalsum(a**b)
		m = max(m,s)
print m
