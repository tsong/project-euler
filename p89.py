rtoi_map = \
		{	
			'I' : 1,
			'IV' : 4,
			'V' : 5,
			'IX' : 9,
			'X' : 10,
			'XL' : 40,
			'L' : 50,
			'XC' : 90,
			'C' : 100,
			'CD' : 400,
			'D' : 500,
			'CM' : 900,
			'M' : 1000
		}
itor_map = dict(zip(rtoi_map.values(), rtoi_map.keys()))

def roman_to_integer(r):
	assert len(r) > 0
	s = 0

	last_pair = False
	for i in xrange(len(r)): 
		if last_pair:
			last_pair = False
			continue

		pair = r[i] + r[i+1] if i < len(r) - 1 else ''
		if pair in rtoi_map:
			s += rtoi_map[pair]
			last_pair = True
		else:
			s += rtoi_map[r[i]]

	return s

def integer_to_roman(n):
	r = ''

	values = reversed(sorted(itor_map.keys()))	
	nn = n
	for v in values:
		while nn >= v: 
			r += itor_map[v]
			nn -= v

	assert roman_to_integer(r) == n
	return r

f = open('data/p89.in')
lines = [l.strip() for l in f.readlines()]
N = [roman_to_integer(l.strip()) for l in lines]
R = [integer_to_roman(n) for n in N]

print sum( [ len(lines[i]) - len(R[i]) for i in xrange(len(R)) ] ) 
