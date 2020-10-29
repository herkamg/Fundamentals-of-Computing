import math
def smaller_root(a,b,c):
    """ this function compute the solution of a equation of grade 2
     and return the solution if it exist
     """
    Discriminant = b**2 - 4 * (a * c)
    if Discriminant < 0 or a == 0:
         print("Error: no real solutions")
         return
    elif Discriminant == 0:
        return - b/(2*a)
    else:
        return min ((-b + math.sqrt(Discriminant) ) / (2*a), (-b - math.sqrt(Discriminant) ) / (2*a))


###################################################
# Tests

def test(a, b, c):
    """Tests the smaller_root function."""
    
    print( "The smaller root of " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + " is:") 
    print( str(smaller_root(a, b, c)))
        

test(1, 2, 3)
test(2, 0, -10)
test(6, -3, 5)
test(0, 2, 3)