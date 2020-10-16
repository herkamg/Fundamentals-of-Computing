''' the following function compute the area of 
    a circle given the radius '''
import math
def circle_area(radius):
    return math.pi * radius**2

###################################################
# Tests

def test(radius):
	print( "A circle with a radius of " + str(radius),
	"inches has an area of",
	str(circle_area(radius)) + " square inches.")

test(8)
test(3)
test(12.9)