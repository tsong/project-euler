def pandigital(k,n):
	D = set(range(1,10))
	for i in xrange(1,n+1):
		s = str(k*i)
		if len(s) > len(D):
			return -1
		for d in [int(c) for c in s]:
			if d not in D:
				return -1
			D.remove(d)
	
	if len(D) == 0:
		return int(reduce( lambda x,y: x+y, \
				[str(k*i) for i in xrange(1,n+1)] ))
	else:
		return -1

m = -1
for k in xrange(1,10000):
	for n in range(2,10):
		m = max(m, pandigital(k,n))

print m
