''' The following function should compute the area of rectangle
given the height and width '''
def rectangle_area(width, height):
    return width*height

###################################################
# Tests

def test(width, height):
	print ("A rectangle " + str(width) + " inches wide and " + str(height),
	"inches high has an area of",
	str(rectangle_area(width, height)) + " square inches.")

test(4, 7)
test(7, 4)
test(10, 10)