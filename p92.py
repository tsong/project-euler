lookup = {1:1, 89:89} 
def chain(n):
	if n <= 0: return -1

	if n not in lookup:
		s = 0
		nn = n
		while nn > 0:
			s += (nn%10)**2
			nn /= 10

		lookup[n] = chain(s)
	return lookup[n]

s = 0
for n in xrange(1,10000000):
	if chain(n) == 89:
		s += 1
print s
