from eulerlib import factor

n = 1
while True:
	satisfied = True
	for i in xrange(n,n+4):
		if len(set(factor(i))) != 4:
			satisfied = False
			break
	if satisfied:
		print range(n,n+4)
		break
	n += 1
