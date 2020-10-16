''' this following function should computer circumference of 
a circle given a radius''' 
import math
def circle_circumference(radius):
    return 2* math.pi* radius

###################################################
# Tests

def test(radius):
	print( "A circle with a radius of " + str(radius),
	"inches has a circumference of",
	str(circle_circumference(radius)) + " inches.")

test(8)
test(3)
test(12.9)