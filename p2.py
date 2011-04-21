f0 = 1
f1 = 1
s = 0
while f1 <= 4000000:
	s += f1 if f1 % 2 == 0 else 0
	tmp = f1
	f1 = f0 + f1
	f0 = tmp

print s
