def name_and_age(name, age):
    """ this function return a string (phrase)
        giving the name of name and the age as long as the age is valid  
    """
    if age < 0:
        return "Error: Invalid age"
    else:
        return str(name)+" is "+ str(age)+" years old."

###################################################
# Tests
# Student should not change this code.

def test(name, age):
	"""Tests the name_and_age function."""
	
	print( name_and_age(name, age))
	
test("Joe Warren", 52)
test("Scott Rixner", 40)
test("John Greiner", -46)