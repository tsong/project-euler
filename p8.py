n = ''.join([l.strip() for l in open('p8.in')])

m = -1
for i in xrange(len(n)-5):
	v = reduce(lambda x,y: int(x)*int(y), n[i:i+5])
	if v > m:
		m = v 
print m
