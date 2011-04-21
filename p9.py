import sys
for c in xrange(1000):
	for b in xrange(c):
		for a in xrange(b):
			if a*a + b*b == c*c and a+b+c == 1000:
				print a*b*c
				sys.exit(0)
