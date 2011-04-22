f0 = 1
f1 = 1
t = 2
while len(str(f1)) < 1000:
	tmp = f1
	f1 = f0 + f1
	f0 = tmp
	t += 1

print t 
