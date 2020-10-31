def matexpr(number):
    return -5*number**5 + 69*number**2 -47

print(matexpr(0), matexpr(1), matexpr(2), matexpr(3))

print ("")

def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years

    # Put your code here.
    return present_value * (1+rate_per_period)**periods


print("$1000 at 2% compounded daily for 3 years yields $",future_value(500, .04, 10, 10))
print("  ")
print("$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3))

print (" regular polygon area")

import math
def area_regular_polygon(n,s):
    """ return the area of a regular polygon of n side of length's' and """
    return (n * s**2)/(4 * math.tan(math.pi/n))

print(area_regular_polygon(5, 7))

def max_of_2(a, b):
    if a > b:
        return a
    else:
        return b

def max_of_3(a, b, c):
    return max_of_2(a, max_of_2(b, c))


def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)
    scale = distance / dist_to_origin
    print( point_x * scale, point_y * scale)

project_to_distance(2, 7, 4)