''' the following function express
    the name of a person given the 
        first name and the last name'''

def name_tag(first_name, last_name):
    return "My name is "+first_name + " "+ last_name+ "."

###################################################
#Test
def test(first_name, last_name):
	print (name_tag(first_name, last_name))
	
test("Joe", "Warren")
test("Scott", "Rixner")
test("John", "Greiner")