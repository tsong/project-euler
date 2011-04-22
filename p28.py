def spiral(n):
	if n % 2 == 0: return -1
	if n == 1: return 1

	start = (n-2)**2 + 1

	corner = start + n-2
	s = corner
	for i in range(3):
		corner += n-1 
		s += corner 

	return s + spiral(n-2)

print spiral(1001)

