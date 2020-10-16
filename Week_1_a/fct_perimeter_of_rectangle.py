# this following function should compute the perimeter of rectangle 
def rectangle_perimeter(width, height):
    return 2* (width + height)

###################################################
# Tests
# Student should not change this code.

def test(width, height):
	print( "A rectangle " + str(width) + " inches wide and " + str(height),
	"inches high has a perimeter of",
	str(rectangle_perimeter(width, height)) + " inches.")

test(4, 7)
test(7, 4)
test(10, 10)