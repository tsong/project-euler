from math import factorial
F = [factorial(n) for n in range(10)]

def iscurious(n):
	S = sum([F[int(d)] for d in str(n)])
	return S == n

C = [n for n in xrange(10,sum(F)+1) if iscurious(n)]
print sum(C)
