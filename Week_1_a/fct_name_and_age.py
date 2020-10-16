''' the following function give out 
    the name and the age in consistent sentence
    given is the name and the age '''

def name_and_age(name, age):
    return name + " is " + str(age) + " years old."

###################################################
# Tests

def test(name, age):
	print(name_and_age(name, age))
	
test("Joe Warren", 52)
test("Scott Rixner", 40)
test("John Greiner", 46)