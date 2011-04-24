coins = [1, 2, 5, 10, 20, 50, 100, 200]
def waystomake(n,D):
	if n == 0: return 1
	if len(D) == 0: return 0

	s = 0
	for i in xrange(n/D[0]+1):
		w = waystomake(n-D[0]*i,D[1:])
		if w > 0:
			s += w

	return s

print waystomake(200,coins)
