from eulerlib import cmpf, gcd

N = 12000 

f1 = (1,3)
f2 = (1,2)

c = 0
for d in xrange(1,N+1):
	for n in xrange(d/3,d/2+1):
		if gcd(n,d) == 1:
			f = (n,d)
			if cmpf(f,f1) > 0 and cmpf(f,f2) < 0:
				c += 1

print c
