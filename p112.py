def is_bouncy(n):
	if n < 100:
		return False

	d0 = n % 10
	n /= 10
	dec = False
	inc = False

	while n > 0:
		d1 = n % 10
		if d1 > d0:
			inc = True
		elif d1 < d0:
			dec = True

		if inc and dec:
			return True

		d0 = d1
		n /= 10
	return False
	

n = 1 
b = 0
while True:
	if is_bouncy(n):
		b += 1

	if b % 99 == 0 and n % 100 == 0 and b / 99 == n / 100:
		print "%d/%d" % (b,n)
		break

	n += 1
