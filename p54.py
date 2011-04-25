values = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
suits = ['H', 'S', 'D', 'C']

V = dict( [ (values[i],i) for i in xrange(len(values)) ] ) 
S = dict( [ (suits[i],i) for i in xrange(len(suits)) ] )

def rank(c):
	return (V[c[0]],S[c[1]])

def tostr(v):
	return values[v[0]] + suits[v[1]]

games =  [ [rank(c) for c in l] for l in \
			[l.strip().split(' ') for l in open('data/p54.in')] ]


h = games[1][:5]


def count(h):
	C = {}
	for v in [c[0] for c in h]:
		if v not in C.keys():
			C[v] = 0
		C[v] += 1

	return C

def high(h,C):
	return sum( [13**i * h[i][0] for i in xrange(len(h))] )

def pair(h,C):
	v = reduce( lambda x,y: x if x[1] == 2 else y, C.items() )
	return high([c for c in h if c[0] != v[0]], C) + 13**3 * v[0] \
			if v[1] == 2 else -1
	
def twop(h,C):
	if sorted(C.values()) == [1,2,2]:
		P = sorted( [c[0] for c in C.items() if c[1] == 2] )
		v = [c[0] for c in C.items() if c[1] != 2][0]
		return v + P[0]*13 + P[1]*13*13 
	return -1

def three(h,C):
	v = reduce( lambda x,y: x if x[1] == 3 else y, C.items() )
	return high([c for c in h if c[0] != v[0]], C) + 13**2 * v[0] \
			if v[1] == 3 else -1

def straight(h,C):
	return reduce( lambda x,y: y if y-x==1 else -2, [c[0] for c in h] )

def flush(h,C):
	return high(h,C) if len(set([c[1] for c in h])) == 1 else -1

def fullhouse(h,C):
	if set(C.values()) == set([3,2]):
		rev = dict( [ (v,k) for (k,v) in C.items() ] )
		return rev[3]*13 + rev[2]
	return -1

def four(h,C):
	v = reduce( lambda x,y: x if x[1] == 4 else y, C.items() )
	return high([c for c in h if c[0] != v[0]], C) + 13**1 * v[0] \
			if v[1] == 4 else -1

def sflush(h,C):
	s = straight(h,C)
	return s if flush(h,C) > 0 else -1

def score(h):
	h = sorted(h, cmp = lambda x,y: x[0] - y[0])
	S = [sflush,four,fullhouse,flush,straight,three,twop,pair,high]
	for i in xrange(len(S)):
		v = S[i](h,count(h))
		if v > 0:
			return (len(S)-i)*13**6 + v

	return -1

print len( [h for h in games if score(h[:5]) > score(h[5:])] )
