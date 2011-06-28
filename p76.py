def count(n,m):
	if n <= 1:
		return 1

	s = 1
	for i in xrange(1,n/2+1):
		if i >= m:
			s += count(n-i, i)
	return s

print count(100,1)-1
