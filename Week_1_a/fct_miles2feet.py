# this function  convert miles to feet 
def miles_to_feet(miles):
    return miles * 5280


###################################################
# Tests
def test(miles):
	print( str(miles) + " miles equals",
	str(miles_to_feet(miles)) + " feet.")

test(13)
test(57)
test(82.67)