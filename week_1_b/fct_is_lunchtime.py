def is_lunchtime(hour, is_am):
    """ given time and an Boolean value this function
        gives weither the current is before or after noon
        and weither it is then lunch time 
    """
    if (hour == 11 and is_am == True) or (hour == 12 and is_am == False):
        return True
    else:
        return False
    # return (hour == 11 and is_am == True) or (hour == 12 and is_am == False)
########################################################################
# Tests
# Student should not change this code.

def test(hour, is_am):
	"""Tests the is_lunchtime function."""
	print( hour, end=" "),
	if is_am:
		print("AM", end=" "),
	else:
		print("PM", end=" "),
	if is_lunchtime(hour, is_am):
		print("is lunchtime.")
	else:
		print("is not lunchtime.")

test(11, True)
test(12, True)
test(11, False)
test(12, False)
test(10, False)