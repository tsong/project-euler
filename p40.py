N = ''.join([str(n) for n in xrange(1000000)]) 
print reduce( lambda x,y: x*y, [int(N[10**n]) for n in xrange(7)] )
