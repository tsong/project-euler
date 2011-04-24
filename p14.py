lookup = {0:-1, 1:1}
def collatz(n):
	if not n in lookup: 
		lookup[n] = 1 + (collatz(n/2) if n%2 == 0 else collatz(3*n+1))
	return lookup[n]	

m = -1
s = -1
for n in xrange(1,1000000):
	c = collatz(n)	
	if c > m:
		m = c
		s = n

print s


