from point import Point

point = Point.__new__(Point)

# The point object is not initialized

#  point.x
## Traceback (most recent call last):
##     ...
## AttributeError: 'Point' object has no attribute 'x'


#  point.y
## Traceback (most recent call last):
##     ...
## AttributeError: 'Point' object has no attribute 'y'

point.__init__(21, 42)
print(point)