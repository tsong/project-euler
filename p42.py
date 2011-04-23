W = [w.strip('"') for w in open('data/p42.in').readline().split(',')]
S = set([n*(n+1)/2 for n in xrange(100000)])

def score(w):
	s = 0
	for c in w:
		s += ord(c.lower()) - ord('a') + 1
	return s

T = [w for w in W if score(w) in S]
print len(T)
