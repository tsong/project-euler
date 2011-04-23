from itertools import permutations

s = set()

def num(li):
	b = 1
	n = 0
	for d in reversed(li):
		n += b*d
		b *= 10
	return n


for p in permutations(range(1,10)):
	for e in xrange(1,10):
		for x in xrange(e):
			m1 = num(p[:x])
			m2 = num(p[x:e])
			pr = num(p[e:])

			if m1 * m2 == pr:
				s.add(pr)	

print sum(s)
