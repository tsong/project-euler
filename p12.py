from eulerlib import factor

def divisors(n):
	if n == 1: return 1
	F = factor(n)
	return reduce( lambda x,y: x*y , [F.count(i)+1 for i in set(F)] )

def tri(n):
	return n*(n+1)/2

n = 8
while divisors(tri(n)) <= 500:
	n += 1

print tri(n)
