def d(n):
	s = 0
	for i in range(1,n):
		if n%i == 0:
			s += i
	return s

D = dict( [(i,d(i)) for i in range(1,10000)] )

s = 0
for (a,b) in D.items():
	if b < 10000 and b > 0 and D[b] == a and a != b:
		s += a

print s


