def print_digits (number):
    """ 
    """
    if number>=100 or number < 0:
        print("Error: Input is not a two-digit number.")
    else:
        print("The tens digit is "+ str(number//10) + ", and the ones digit is "+str(number%10) +".")
# Tests
# Student should not change this code.
	
print_digits(42)
print_digits(99)
print_digits(5)
print_digits(459)