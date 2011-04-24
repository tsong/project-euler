
def ispalindrome(n):
	s = str(n)
	for i in xrange(len(s)/2):
		if s[i] != s[len(s)-1-i]:
			return False
	return True

def islychrel(n):
	for i in xrange(50):
		n = n + int( ''.join([d for d in reversed(str(n))]) ) 
		if ispalindrome(n):
			return False 
	return True 

L = [n for n in xrange(1,10000) if islychrel(n)]
print len(L)
