def is_cool(name):
    """ this function schould estimate weither 
        a name is cool and return True 
    """
    # if name=="Joe":
    #     return True
    # elif name=="John":
    #     return True
    # elif name=="Stephan":
    #     return True
    # else:
    #     return False
    return (name=="Stephan") or (name=="John") or (name=="Joe")
######################################
# Tests

def test(name):
    """ Tests the is_cool function """
    if is_cool(name):
        print(name, "is cool")
    else:
        print(name, "is not cool")

test("Joe")
test("John")
test("Stephan")
test("Scott")