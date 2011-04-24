S = set()
for a in xrange(2,101):
	for b in xrange(2,101):
		S.add(a**b)
print len(S)
