ones = ['','one','two','three','four','five','six','seven','eight','nine']
teens = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']


def to_word(n):
	if n == 1000: return len('onethousand')
	h = n / 100
	t = n % 100	

	l = 0
	if h != 0:
		l += len(ones[h]) + len('hundred') 
	if h != 0 and t != 0:
		l += len('and')
	if t != 0:
		if t < 10:
			l += len(ones[t])
		elif t < 20:
			l += len(teens[t-10])
		else:
			l += len(tens[t/10])
			if t % 10 != 0:
				l += len(ones[t%10])

	return l



s = 0
for n in xrange(1,1001):
	s += to_word(n)

print s
