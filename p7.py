seive = [False for x in xrange(999999)]

p = 0
n = 2
while p < 10001:
	while seive[n]:
		n += 1
	nn = n
	p += 1
	while nn < len(seive):
		seive[nn] = True
		nn += n

print n
