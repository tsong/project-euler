def ispalindrome(s):
	for i in xrange(len(s)/2):
		if s[i] != s[len(s)-1-i]:
			return False
	
	return True

m = -1
for a in reversed(xrange(100,1000)):
	for b in reversed(xrange(100,1000)):
		if ispalindrome(str(a*b)):
			m = max(m, a*b)	
print m 
