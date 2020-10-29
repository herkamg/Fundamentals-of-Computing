def name_lookup(first_name):
    """ this function return the name of the instructor if its in the list
        otherwise throw an notification for instructor not found
    """
    if first_name=="Joe":
        return "Warren"
    elif first_name=="Scott":
        return "Rixner"
    elif first_name=="John":
        return "Greiner"
    elif first_name=="Stephen":
        return "Wong"
    else:
        return "Error: Not an instructor"


###################################################
# Tests
# Student should not change this code.

def test(first_name):
	"""Tests the name_lookup function."""
	
	print(name_lookup(first_name))
	
test("Joe")
test("Scott")
test("John")
test("Stephen")
test("Mary")