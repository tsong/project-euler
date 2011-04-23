from eulerlib import *

N = 1000000 #arbitrarily large number
P = set(seive(N))

def ltruncatable(n):
	s = str(n)
	for i in xrange(len(s)):
		if int(s[i:]) not in P:
			return False
	return True


def rtruncatable(n):
	s = str(n)
	for i in xrange(len(s)):
		if int(s[:len(s)-i]) not in P:
			return False
	return True

T = [n for n in range(10,N) if ltruncatable(n) and rtruncatable(n)]
print sum(T)
