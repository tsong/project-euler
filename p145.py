N = 1000000000

def reverse(n):
	return int( ''.join([d for d in reversed(str(n))]) )

def reverse_sum(n):
	return n + reverse(n)

def is_reversible(n):
	if n % 10 == 0:
		return False

	for d in str(reverse_sum(n)):
		if int(d) % 2 == 0:
			return False

	return True

print len([n for n in xrange(1,N) if is_reversible(n)])
