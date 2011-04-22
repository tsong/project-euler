def isprime(n):
	i = 2
	while i < n:
		if n % i == 0:
			return False
		i += 1
	return True

i = 2
n = 600851475143
m = -1
while n > 1: 
	if n % i == 0 and isprime(i):
		n /= i
		m = max(m,i)
	i += 1

print m

