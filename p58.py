from eulerlib import isprime

lookup = {1: (0,1)}
def spiral(n):
	if n % 2 == 0: return None 

	if n not in lookup:
		start = (n-2)**2 + 1
		corner = start + n-2
		C = [corner]
		for i in range(3):
			corner += n-1 
			C.append(corner)

		r1 = (sum( [1 for c in C if isprime(c)] ) , len(C)) 
		r2 = spiral(n-2)
		lookup[n] = (r1[0] + r2[0], r1[1] + r2[1])

	return lookup[n]

n = 9
while True:
	ratio = spiral(n)
	if ratio[0]*10 < ratio[1]:
		print n, ratio
		break
	n += 2
