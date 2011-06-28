def num_rectangles(w,h):
	rects = 0
	for i in xrange(1,w+1):
		for j in xrange(1,h+1):
			rects += (w-i+1)*(h-j+1)
	return rects
	
N = 100
target = 2000000
closest_rects = 0
(closest_width, closest_height) =  (0, 0)

for w in xrange(1,N):
	for h in xrange(1,w):
		rects = num_rectangles(w,h)
		if abs(target-rects) < abs(target-closest_rects):
			closest_rects = rects
			(closest_width, closest_height) = (w,h)

print closest_width*closest_height
