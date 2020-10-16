''' the following function takes  an integer in the range of [0, 100[
    and print the tens digit and the ones digit'''
def print_digits(number2digits):
    print("The tens digit is " + str(number2digits//10) +
    ", and the ones digit is " + str(number2digits%10) + "." )

###################################################
# Tests
# Student should not change this code.
	
print_digits(42)
print_digits(99)
print_digits(5)