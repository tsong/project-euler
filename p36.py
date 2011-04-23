
def ispalindrome(s):
	for i in xrange(len(s)/2):
		if s[i] != s[len(s)-1-i]:
			return False
	return True

def binstr(n):
	s = str(n%2) 
	while n > 1:
		n /= 2
		s = str(n%2) + s
	return s

P = [ n for n in xrange(1000000) if ispalindrome(str(n)) \
		and ispalindrome(binstr(n)) ]
