from math import sqrt 

T = [(a,b,c) for c in xrange(1001) \
		for b in xrange(1000-c) for a in range(1000-c-b) \
		if a*a + b*b == c*c]
			
P = {}
for t in T:
	s = sum(t)
	if s not in P.keys():
		P[s] = 0
	P[s] += 1

print reduce( lambda x,y: x if x[1] > y[1] else y, P.items() )
