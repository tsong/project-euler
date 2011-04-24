def decrypt(A,k):
	D = [a for a in A]
	for i in xrange(0,len(A),3):
		for j in xrange(min(len(A)-i,len(k))):
			D[i+j] = A[i+j] ^ k[j]
	return D


A = [int(n.strip()) for n in open('data/p59.in').readline().split(',')]
words = set([l.strip().lower() for l in open('data/words')])


i = ord('a')
n = ord('z')+1
keys =  [(a,b,c) for a in xrange(i,n) \
			for b in xrange(i,n) for c in xrange(i,n)]

for k in keys:
	D = decrypt(A,k)
	s = ''.join([chr(v) for v in D])	

	#if a threshold of valid words are read, this could be plain text
	thres = 0
	found = False
	for w in s.lower().split(' '):
		if w in words: thres += 1
		if thres >= 30:
			found = True
			break
	if found:
		print sum(D)
		break	
