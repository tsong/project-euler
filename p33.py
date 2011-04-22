from eulerlib import simplify 

def iscurious(a,b):
	N = str(a)
	D = str(b)

	for d in N:
		if d in D:
			i = N.index(d)
			j = D.index(d)

			f1 = (int(N[:i] + N[i+1:]), int(D[:j] + D[j+1:]))
			f2 = (a,b)

			return True if simplify(f1) == simplify(f2) else False

P = (1,1)
for b in xrange(10,100):
	for a in xrange(10,b):
		if a % 10 == 0 and b % 10 == 0:
			continue
		if iscurious(a,b):
			print a,b
			P = (P[0] * a, P[1] * b)

print simplify(P)


		
