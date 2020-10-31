def interval_intersect(a,b,c,d):
    """ this function returns True if [a,b] und 
        [c, d ] intersects otherwise False
    """
    return (a<b and c>=a and c<=b) or( a<b and d>=a and d<=b)
"""Returns whether the intervals [a,b] and [c,d] intersect."""
    # return (c <= b) and (a <= d)
###################################################
# Tests

def test(a, b, c, d):
    """Tests the interval_intersect function."""
    print("Intervals [" + str(a) + ", " + str(b) + "] and [" + str(c) + ", " + str(d) + "]",end ="")
    if interval_intersect(a, b, c, d):
        print("intersect.")
    else:
        print("do not intersect.")

test(0, 1, 1, 2)
test(1, 2, 0, 1)
test(0, 1, 2, 3)
test(2, 3, 0, 1)
test(0, 3, 1, 2)