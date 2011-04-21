# In general, program can be solved 2n C n for a n by n grid
# Regardless of the route, we must have n right movements and
# n down movements, and each route will have 2n movements. 
# 2n C n = number of distinct arrangements of the movements

routes = reduce(lambda x,y : x*y, range(21,41)) / reduce(lambda x,y: x*y, range(1,21)) 

print routes
