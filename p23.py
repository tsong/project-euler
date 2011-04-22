def isabundant(n):
	return n < sum( [i for i in range(1,n) if n % i == 0] ) 

A = [ n for n in range(12,28124) if isabundant(n) ]

s = set(range(1,28124))
for a in A:
	for b in A:
		if a+b in s:
			s.remove(a+b)

print sum( [v for v in s] )
