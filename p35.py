from eulerlib import seive
P = set(seive(1000000))

def iscircular(n):
	s = str(n)
	for i in xrange(len(s)):
		if int(s[i:] + s[:i]) not in P:
			return False
	return True
		

N = [ n for n in xrange(1000000) if iscircular(n) ]
print len(N)
