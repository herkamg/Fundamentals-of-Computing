''' the following function compute the futue value
    of an invest present value in a number of years
    at a given interest rate'''

def future_value(present_value, annual_rate, years):
    return present_value * (1 + 0.01* annual_rate) ** years

###################################################
# Tests
# Student should not change this code.

def test(present_value, annual_rate, years):
	"""Tests the future_value function."""
	
	print( "The future value of $" + str(present_value) + " in " + str(years),
	"years at an annual rate of " + str(annual_rate) + "% is",
	"$" + str(future_value(present_value, annual_rate, years)) + ".")


###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

test(1000, 7, 10)
test(200, 4, 5)
test(1000, 3, 20)