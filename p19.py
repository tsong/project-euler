def feb(yr):
	return  range(1,30) \
			if yr % 4 == 0 and (yr % 100 != 0 or yr % 400 == 0) \
			else range(1,29)

days = sum([	range(1,32) + \
				feb(yr) + \
				range(1,32) + \
				range(1,31) + \
				range(1,32) + \
				range(1,31) + \
				range(1,32) + \
				range(1,32) + \
				range(1,31) + \
				range(1,32) + \
				range(1,31) + \
				range(1,32) \
				for yr in xrange(1901, 2001)	], [])

#1 Jan 1901 is a Tuesday
print len( [ i for i in range(5,len(days)) if (i-5) % 7 == 0 and days[i] == 1 ])
