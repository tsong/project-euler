seive = [False for i in xrange(2000000)]
n = 2
s = 0
while n < len(seive):
	nn = n
	s += n

	while nn < len(seive):
		seive[nn] = True
		nn += n

	while n < len(seive) and seive[n]:
		n += 1
print s
