def is_leap_year(year):
    """this function return true if the given Year is a leap year
    """
    if year % 4 != 0:
        return False
    elif year % 25 != 0:
        return True
    elif year % 16 != 0:
        return False
    else:
        return True
    #return(year % 4 == 0  and (year % 100 != 0 or year % 400 == 0))

###################################################
# Tests
# Student should not change this code.

def test(year):
	"""Tests the is_leapyear function."""
	if is_leap_year(year):
		print( year, "is a leap year.")
	else:
		print( year, "is not a leap year.")

test(2000)
test(1996)
test(1800)
test(2013)