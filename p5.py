def gcd(a,b):
	if b == 0: 
		return a
	return gcd(b,a % b)

def lcm(a,b):
	return a*b/gcd(a,b)

print reduce(lambda x, y: lcm(x,y), range(1,21))
