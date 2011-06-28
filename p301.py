N = 1 << 30

print len( [n for n in xrange(N) if n ^ (2*n) ^ (3*n) == 0] )
