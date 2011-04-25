def cross(x,y):
	return x[0]*y[1] - x[1]*y[0]

def sub(x,y):
	return (x[0] - y[0], x[1] - y[1])

o = (0,0)
def hasorigin(a,b,c):
	v0 = sub(o,a)
	v1 = sub(o,b)
	return cross(sub(b,a),v0) * cross(sub(c,a),v0) < 0 \
			and cross(sub(a,b),v1) * cross(sub(c,b),v1) < 0


L = [ [int(n) for n in l.strip().split(',')] for l in open('data/p102.in') ]
T = [ [(t[0],t[1]),(t[2],t[3]),(t[4],t[5])] for t in L ]

print len( [t for t in T if hasorigin(t[0],t[1],t[2])] )
