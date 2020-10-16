def is_even(number):
    """ This function check if a number is even or odd
        and return true when even else false
    """
    return number % 2 == 0

def test(number):
    """ Test the function is_even function """
    if is_even(number):
        print(number, "is even")
    else:
        print(number, "is odd")

test(8)
test(3)
test(12)