''' the following function computes the distance 
    between to points'''
def point_distance(x0,y0, x1, y1):
    return ((x0-x1)**2+(y0-y1)**2)**0.5

###################################################
# Tests
# Student should not change this code.

def test(x0, y0, x1, y1):
    print( "The distance from (" + str(x0) + ", " + str(y0) + ") to",
    "(" + str(x1) + ", " + str(y1) + ") is",
    str(point_distance(x0, y0, x1, y1)) + ".")

test(2, 2, 5, 6)
test(1, 1, 2, 2)
test(0, 0, 3, 4)