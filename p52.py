n = 1
while True:
	s = set(str(n))
	satisfied = True
	for i in xrange(2,7):
		if s != set(str(i*n)):
			satisfied = False
			break
	if satisfied:
		print n
		break
	n += 1
