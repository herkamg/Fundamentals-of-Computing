''' the following function computes the distance 
    between to points'''
def point_distance(x0,y0, x1, y1):
    return ((x0-x1)**2+(y0-y1)**2)**0.5

''' the following function computes the area of a triangle
    given are the point of the triangle x0, y0, x1,y1, x2, and y2'''

def triangle_area(x0, y0, x1,y1, x2, y2):
    a = point_distance(x0,y0, x1, y1)
    b = point_distance(x0,y0, x2, y2)
    c = point_distance(x1,y1, x2, y2)
    #semi perimeter
    s = (a + b + c) /2
    return ( s * (s - a) * (s - b) * (s - c) )**0.5


###################################################
# Tests

def test(x0, y0, x1, y1, x2, y2):
	print( "A triangle with vertices (" + str(x0) + "," + str(y0) + "),",
	"(" + str(x1) + "," + str(y1) + "), and",
	"(" + str(x2) + "," + str(y2) + ") has an area of",
	str(triangle_area(x0, y0, x1, y1, x2, y2)) + ".")

test(0, 0, 3, 4, 1, 1)
test(-2, 4, 1, 6, 2, 1)
test(10, 0, 0, 0, 0, 10)