def fifth(n):
	return n == sum( [int(d)**5 for d in str(n)] )

print sum( [n for n in xrange(10,1000000) if fifth(n)] )
