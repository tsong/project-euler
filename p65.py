from itertools import cycle
from eulerlib import addf

def eval_continued(cont, depth):
	if depth <= 0:
		return (0,1)
	n = cont.next()
	f = addf( (n,1), eval_continued(cont, depth-1) )
	f = (f[1], f[0])
	return f

def eval_continued_fraction(fraction, depth):
	assert(len(fraction) == 2)
	return addf( (fraction[0],1),  eval_continued(fraction[1], depth) )

def e_cont():
	i = 0
	while True:
		if i % 3 == 1:
			yield 2*(i/3 + 1)
		else:
			yield 1
		i += 1

cont_frac = [2, e_cont()]
f = eval_continued_fraction(cont_frac, 99)	
print sum([int(d) for d in str(f[0])])
