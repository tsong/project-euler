from eulerlib import addf 
	
def sqrt2(n):
	return addf( (1,1), expand(n) )

lookup = {}
def expand(n):
	if n <= 0:
		return (0,1)
	if not n in lookup.keys():
		frac = addf((2,1), expand(n-1))
		lookup[n] = (frac[1], frac[0])
	return lookup[n]

S = [sqrt2(n) for n in xrange(1,1001)]
N = [(n,d) for (n,d) in S if len(str(n)) > len(str(d))] 
print len(N)
