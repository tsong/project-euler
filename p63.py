s = 0
for a in xrange(1,10):
	for b in xrange(1,100):
		n = str(a**b)
		if len(n) == b:
			s += 1
print s
