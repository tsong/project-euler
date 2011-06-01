N = 1000000

candidates = []
for d in xrange(1,N+1):
	n = 3*d/7
	if (3*d) % 7 == 0:
		n -= 1
	if n > 0:
		candidates.append( (n,d) )

m = reduce(lambda x,y: x if x[0]*y[1] > y[0]*x[1] else y, candidates)
print m


	


